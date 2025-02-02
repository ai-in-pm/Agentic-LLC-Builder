"""
Professional LLC requirements by state.
"""

PROFESSIONAL_LLC_REQUIREMENTS = {
    "default": {
        "ownership_restrictions": {
            "all_members_licensed": True,
            "minimum_licensed_members": 1.0,  # 100%
            "non_professional_managers": False
        },
        "insurance_requirements": {
            "professional_liability": True,
            "minimum_coverage": "1000000"
        },
        "name_requirements": {
            "suffix": ["Professional Limited Liability Company", "PLLC", "P.L.L.C."],
            "board_approval": True
        }
    },
    "CA": {
        "ownership_restrictions": {
            "all_members_licensed": True,
            "minimum_licensed_members": 1.0,
            "non_professional_managers": False
        },
        "insurance_requirements": {
            "professional_liability": True,
            "minimum_coverage": "100000",
            "per_occurrence": "500000"
        },
        "name_requirements": {
            "suffix": ["Professional Limited Liability Company", "PLLC", "P.L.L.C."],
            "board_approval": True,
            "include_profession": True
        }
    },
    "NY": {
        "ownership_restrictions": {
            "all_members_licensed": True,
            "minimum_licensed_members": 0.75,  # 75%
            "non_professional_managers": True
        },
        "insurance_requirements": {
            "professional_liability": True,
            "minimum_coverage": "1000000",
            "per_occurrence": "3000000"
        },
        "name_requirements": {
            "suffix": ["Professional Limited Liability Company", "PLLC", "P.L.L.C."],
            "board_approval": True,
            "include_profession": True,
            "name_approval": True
        }
    },
    "TX": {
        "ownership_restrictions": {
            "all_members_licensed": False,
            "minimum_licensed_members": 0.51,  # 51%
            "non_professional_managers": True
        },
        "insurance_requirements": {
            "professional_liability": True,
            "minimum_coverage": "500000",
            "per_occurrence": "1000000"
        },
        "name_requirements": {
            "suffix": ["Professional Limited Liability Company", "PLLC", "P.L.L.C."],
            "board_approval": True
        }
    }
}
