"""
State-specific data for LLC formation requirements.
"""

STATE_DATA = {
    "AL": {
        "filing_agency": "Alabama Secretary of State",
        "formation_fee": 200.00,
        "name_reservation_fee": 28.00,
        "name_reservation_duration": 120,
        "processing_time": {
            "standard": 10,
            "expedited": 24
        },
        "annual_report": False,
        "publication_required": False,
        "series_llc_allowed": False,
        "professional_llc_allowed": True,
        "franchise_tax": {
            "required": True,
            "minimum": 100.00
        }
    },
    "AK": {
        "filing_agency": "Alaska Division of Corporations",
        "formation_fee": 250.00,
        "name_reservation_fee": 25.00,
        "name_reservation_duration": 120,
        "processing_time": {
            "standard": 10,
            "expedited": 24
        },
        "annual_report": {
            "required": True,
            "fee": 100.00,
            "due": "January 2"
        },
        "publication_required": False,
        "series_llc_allowed": False,
        "professional_llc_allowed": True,
        "franchise_tax": {
            "required": False
        }
    },
    "AZ": {
        "filing_agency": "Arizona Corporation Commission",
        "formation_fee": 50.00,
        "name_reservation_fee": 10.00,
        "name_reservation_duration": 120,
        "processing_time": {
            "standard": 20,
            "expedited": 5
        },
        "annual_report": False,
        "publication_required": True,
        "series_llc_allowed": True,
        "professional_llc_allowed": True,
        "franchise_tax": {
            "required": False
        }
    },
    "AR": {
        "filing_agency": "Arkansas Secretary of State",
        "formation_fee": 45.00,
        "name_reservation_fee": 25.00,
        "name_reservation_duration": 120,
        "processing_time": {
            "standard": 2,
            "expedited": 24
        },
        "annual_report": {
            "required": True,
            "fee": 150.00,
            "due": "April 30"
        },
        "publication_required": False,
        "series_llc_allowed": False,
        "professional_llc_allowed": True,
        "franchise_tax": {
            "required": True,
            "minimum": 150.00
        }
    },
    # Data for remaining states...
    "NY": {
        "filing_agency": "New York Department of State",
        "formation_fee": 200.00,
        "name_reservation_fee": 20.00,
        "name_reservation_duration": 60,
        "processing_time": {
            "standard": 7,
            "expedited": 24,
            "same_day": 1
        },
        "annual_report": {
            "required": True,
            "fee": 9.00,
            "due": "Biennial anniversary month"
        },
        "publication_required": True,
        "publication_requirements": {
            "deadline": "120 days",
            "duration": "6 weeks",
            "estimated_cost": "1000.00"
        },
        "series_llc_allowed": False,
        "professional_llc_allowed": True,
        "franchise_tax": {
            "required": True,
            "minimum": 25.00
        }
    },
    "TX": {
        "filing_agency": "Texas Secretary of State",
        "formation_fee": 300.00,
        "name_reservation_fee": 40.00,
        "name_reservation_duration": 120,
        "processing_time": {
            "standard": 5,
            "expedited": 24,
            "same_day": 1
        },
        "annual_report": False,
        "publication_required": False,
        "series_llc_allowed": True,
        "professional_llc_allowed": True,
        "franchise_tax": {
            "required": True,
            "minimum": 0.00,
            "notes": "No tax due if revenue is below threshold"
        }
    },
    "FL": {
        "filing_agency": "Florida Division of Corporations",
        "formation_fee": 125.00,
        "name_reservation_fee": 25.00,
        "name_reservation_duration": 120,
        "processing_time": {
            "standard": 5,
            "expedited": 24,
            "same_day": 1
        },
        "annual_report": {
            "required": True,
            "fee": 138.75,
            "due": "May 1"
        },
        "publication_required": False,
        "series_llc_allowed": False,
        "professional_llc_allowed": True,
        "franchise_tax": {
            "required": False
        }
    },
    "WA": {
        "filing_agency": "Washington Secretary of State",
        "formation_fee": 180.00,
        "name_reservation_fee": 30.00,
        "name_reservation_duration": 180,
        "processing_time": {
            "standard": 3,
            "expedited": 24
        },
        "annual_report": {
            "required": True,
            "fee": 60.00,
            "due": "End of formation month"
        },
        "publication_required": False,
        "series_llc_allowed": False,
        "professional_llc_allowed": True,
        "franchise_tax": {
            "required": False
        }
    },
    # Add data for remaining states...
}

COMMON_PROHIBITED_TERMS = [
    "Bank",
    "Banking",
    "Cooperative",
    "Federal",
    "National",
    "Reserve",
    "Trust",
    "United States",
    "Insurance",
    "Insurer",
    "Corporation",
    "Corp.",
    "Inc.",
    "Incorporated"
]

COMMON_RESTRICTED_TERMS = {
    "Engineer": "Board of Professional Engineers",
    "Engineering": "Board of Professional Engineers",
    "Architect": "Board of Architecture",
    "Attorney": "State Bar Association",
    "Doctor": "Medical Board",
    "Hospital": "Department of Health",
    "Pharmacy": "Board of Pharmacy",
    "Real Estate": "Real Estate Commission",
    "Bank": "Department of Financial Institutions",
    "Trust": "Department of Financial Institutions",
    "University": "Department of Education",
    "College": "Department of Education"
}

COMMON_REQUIRED_TERMS = [
    "Limited Liability Company",
    "LLC",
    "L.L.C.",
    "Ltd. Liability Co.",
    "Ltd. Liability Company"
]

REGULATED_PROFESSIONS = [
    "Accountant",
    "Architect",
    "Attorney",
    "Chiropractor",
    "Dentist",
    "Engineer",
    "Insurance Agent",
    "Investment Advisor",
    "Medical Doctor",
    "Nurse",
    "Optometrist",
    "Pharmacist",
    "Physical Therapist",
    "Physician",
    "Psychologist",
    "Real Estate Agent",
    "Veterinarian"
]
