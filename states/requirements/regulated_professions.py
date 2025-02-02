"""
Regulated professions and their requirements.
"""

REGULATED_PROFESSIONS = {
    "Medical": {
        "professions": [
            "Physician",
            "Surgeon",
            "Dentist",
            "Chiropractor",
            "Optometrist",
            "Psychologist",
            "Physical Therapist"
        ],
        "requirements": {
            "board_approval": True,
            "liability_insurance": True,
            "annual_renewal": True,
            "continuing_education": {
                "required": True,
                "hours_per_year": 50
            },
            "controlled_substance_registration": {
                "required": "If prescribing",
                "dea_registration": True,
                "state_registration": True
            }
        }
    },
    "Legal": {
        "professions": [
            "Attorney",
            "Lawyer"
        ],
        "requirements": {
            "bar_admission": True,
            "liability_insurance": True,
            "trust_account": True,
            "continuing_education": {
                "required": True,
                "hours_per_year": 24
            },
            "character_fitness": True,
            "disciplinary_reporting": True
        }
    },
    "Financial": {
        "professions": [
            "Accountant",
            "Investment Advisor",
            "Insurance Agent"
        ],
        "requirements": {
            "license": True,
            "bonding": True,
            "continuing_education": {
                "required": True,
                "hours_per_year": {
                    "Accountant": 40,
                    "Investment_Advisor": 12,
                    "Insurance_Agent": 24
                }
            },
            "sec_registration": {
                "required": "If managing over $25M",
                "form_adv": True
            }
        }
    },
    "Real Estate": {
        "professions": [
            "Real Estate Agent",
            "Real Estate Broker",
            "Property Manager"
        ],
        "requirements": {
            "license": True,
            "bonding": True,
            "continuing_education": {
                "required": True,
                "hours_per_year": {
                    "Agent": 12,
                    "Broker": 15
                }
            },
            "trust_account": True,
            "errors_and_omissions": True
        }
    },
    "Engineering": {
        "professions": [
            "Professional Engineer",
            "Structural Engineer",
            "Civil Engineer"
        ],
        "requirements": {
            "license": True,
            "liability_insurance": True,
            "continuing_education": {
                "required": True,
                "hours_per_year": 15
            },
            "seal_requirements": True,
            "experience_requirements": {
                "years": 4,
                "supervised": True
            }
        }
    },
    "Architecture": {
        "professions": [
            "Architect",
            "Landscape Architect"
        ],
        "requirements": {
            "license": True,
            "liability_insurance": True,
            "continuing_education": {
                "required": True,
                "hours_per_year": 12
            },
            "seal_requirements": True,
            "experience_requirements": {
                "years": 3,
                "supervised": True
            }
        }
    }
}
