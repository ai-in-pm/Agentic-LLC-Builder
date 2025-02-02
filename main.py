"""
Main application entry point for the LLC Builder system.
"""

from typing import Dict, List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator
from agents.agent_manager import AgentManager, LLCFormationRequest

app = FastAPI(title="Agentic LLC Builder")
agent_manager = AgentManager()

class OwnerInfo(BaseModel):
    """Owner information model."""
    name: str
    ownership_percentage: float
    is_licensed: bool = False
    license_number: Optional[str] = None
    license_state: Optional[str] = None
    role: str = "member"  # member, manager, or both

class LLCFormationDetails(BaseModel):
    """LLC Formation details input model."""
    business_name: str
    state_code: str
    llc_type: str  # single-member, multi-member, professional, series
    industry: str
    owner_info: List[OwnerInfo]
    is_foreign: bool = False
    foreign_state: Optional[str] = None
    expedited: bool = False
    registered_agent_needed: bool = True
    
    @validator('llc_type')
    def validate_llc_type(cls, v):
        valid_types = ['single-member', 'multi-member', 'professional', 'series']
        if v not in valid_types:
            raise ValueError(f'llc_type must be one of: {", ".join(valid_types)}')
        return v
    
    @validator('state_code')
    def validate_state_code(cls, v):
        if len(v) != 2 or not v.isalpha():
            raise ValueError('state_code must be a two-letter state code (e.g., CA, NY)')
        return v.upper()
    
    @validator('owner_info')
    def validate_owners(cls, v, values):
        # Check ownership percentages sum to 100
        total = sum(owner.ownership_percentage for owner in v)
        if not (99.9 <= total <= 100.1):  # Allow for small floating point differences
            raise ValueError('Total ownership percentage must equal 100%')
        
        # For single-member LLCs, only one owner allowed
        if values.get('llc_type') == 'single-member' and len(v) != 1:
            raise ValueError('Single-member LLCs must have exactly one owner')
        
        # For professional LLCs, verify licensing info
        if values.get('llc_type') == 'professional':
            licensed_owners = [owner for owner in v if owner.is_licensed]
            if not licensed_owners:
                raise ValueError('Professional LLCs must have at least one licensed owner')
            for owner in licensed_owners:
                if not owner.license_number or not owner.license_state:
                    raise ValueError('Licensed owners must provide license number and state')
        
        return v
    
    @validator('foreign_state')
    def validate_foreign_state(cls, v, values):
        if values.get('is_foreign') and not v:
            raise ValueError('foreign_state is required when is_foreign is True')
        if v and len(v) != 2:
            raise ValueError('foreign_state must be a two-letter state code')
        return v.upper() if v else None

@app.post("/api/v1/form-llc")
async def form_llc(details: LLCFormationDetails):
    """
    Form an LLC using the multi-agent system.
    
    Args:
        details: LLC formation details
        
    Returns:
        Formation results and next steps
    """
    try:
        # Convert Pydantic model to LLCFormationRequest
        request = LLCFormationRequest(
            business_name=details.business_name,
            state_code=details.state_code,
            llc_type=details.llc_type,
            industry=details.industry,
            owner_info=[owner.dict() for owner in details.owner_info],
            is_foreign=details.is_foreign,
            foreign_state=details.foreign_state,
            expedited=details.expedited,
            registered_agent_needed=details.registered_agent_needed
        )
        
        # Process formation request
        result = agent_manager.process_llc_formation(request)
        
        return {
            "status": "success",
            "data": result
        }
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/requirements/{state_code}")
async def get_state_requirements(state_code: str):
    """Get LLC formation requirements for a state."""
    try:
        from states.state_factory import StateFactory
        requirements = StateFactory.get_requirements(state_code.upper())
        return {
            "status": "success",
            "data": requirements
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Requirements not found for state: {state_code}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
