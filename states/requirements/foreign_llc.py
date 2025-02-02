"""
Foreign LLC requirements by state.
"""

FOREIGN_LLC_REQUIREMENTS = {
    "default": {
        "registration_requirements": {
            "certificate_of_good_standing": True,
            "certificate_age_limit": 90,  # days
            "registered_agent": True,
            "local_office": False
        },
        "maintenance_requirements": {
            "annual_report": True,
            "registered_agent_maintenance": True,
            "state_tax_registration": True
        }
    },
    "CA": {
        "registration_requirements": {
            "certificate_of_good_standing": True,
            "certificate_age_limit": 60,
            "registered_agent": True,
            "local_office": True,
            "statement_of_information": True
        },
        "maintenance_requirements": {
            "annual_report": True,
            "registered_agent_maintenance": True,
            "state_tax_registration": True,
            "local_business_license": True
        },
        "additional_requirements": {
            "foreign_name_registration": True,
            "tax_board_registration": True
        }
    },
    "DE": {
        "registration_requirements": {
            "certificate_of_good_standing": True,
            "certificate_age_limit": 30,
            "registered_agent": True,
            "local_office": False
        },
        "maintenance_requirements": {
            "annual_report": True,
            "registered_agent_maintenance": True,
            "state_tax_registration": "If doing business"
        }
    },
    "NY": {
        "registration_requirements": {
            "certificate_of_good_standing": True,
            "certificate_age_limit": 90,
            "registered_agent": True,
            "local_office": False,
            "publication": True
        },
        "maintenance_requirements": {
            "biennial_report": True,
            "registered_agent_maintenance": True,
            "state_tax_registration": True
        },
        "publication_requirements": {
            "deadline": "120 days",
            "duration": "6 weeks",
            "newspapers": 2
        }
    },
    "TX": {
        "registration_requirements": {
            "certificate_of_good_standing": True,
            "certificate_age_limit": 90,
            "registered_agent": True,
            "local_office": False,
            "tax_clearance": True
        },
        "maintenance_requirements": {
            "annual_report": True,
            "registered_agent_maintenance": True,
            "state_tax_registration": True,
            "franchise_tax": True
        }
    }
}
