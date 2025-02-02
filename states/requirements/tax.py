"""
Tax registration requirements by state.
"""

TAX_REGISTRATION_REQUIREMENTS = {
    "default": {
        "state_tax_id": True,
        "sales_tax_permit": "If selling goods",
        "employer_tax_registration": "If employees",
        "deadlines": {
            "state_tax_id": "30 days",
            "sales_tax_permit": "Before sales begin",
            "employer_tax": "Before hiring"
        }
    },
    "CA": {
        "state_tax_id": True,
        "sales_tax_permit": True,
        "employer_tax_registration": "If employees",
        "local_tax_registration": True,
        "deadlines": {
            "state_tax_id": "30 days",
            "sales_tax_permit": "Before sales begin",
            "employer_tax": "Before hiring",
            "local_tax": "Varies by locality"
        },
        "special_requirements": {
            "board_of_equalization": True,
            "city_business_license": True
        },
        "tax_rates": {
            "sales_tax": {
                "state_rate": 0.0725,
                "local_rates": True
            },
            "franchise_tax": {
                "minimum": 800.00,
                "rate": "Based on income"
            }
        }
    },
    "NY": {
        "state_tax_id": True,
        "sales_tax_permit": "Certificate of Authority",
        "employer_tax_registration": "If employees",
        "local_tax_registration": "If applicable",
        "deadlines": {
            "state_tax_id": "30 days",
            "sales_tax_permit": "20 days before business begins",
            "employer_tax": "When hiring first employee",
            "local_tax": "Varies by locality"
        },
        "special_requirements": {
            "workers_compensation": "If employees",
            "disability_insurance": "If employees"
        },
        "tax_rates": {
            "sales_tax": {
                "state_rate": 0.04,
                "local_rates": True
            },
            "franchise_tax": {
                "minimum": 25.00,
                "rate": "Based on NY income"
            }
        }
    },
    "TX": {
        "state_tax_id": True,
        "sales_tax_permit": True,
        "employer_tax_registration": "If employees",
        "deadlines": {
            "state_tax_id": "30 days",
            "sales_tax_permit": "Before sales begin",
            "employer_tax": "Before hiring"
        },
        "special_requirements": {
            "franchise_tax_registration": True,
            "nexus_questionnaire": True
        },
        "tax_rates": {
            "sales_tax": {
                "state_rate": 0.0625,
                "local_rates": True,
                "max_combined": 0.0825
            },
            "franchise_tax": {
                "threshold": 1230000,  # No tax below this revenue
                "rate": "0.375% or 0.75%"
            }
        }
    },
    "DE": {
        "state_tax_id": "If employees or sales tax",
        "sales_tax_permit": False,  # No sales tax
        "employer_tax_registration": "If employees",
        "deadlines": {
            "state_tax_id": "30 days",
            "employer_tax": "Before hiring"
        },
        "special_requirements": {
            "gross_receipts_tax": "If applicable",
            "business_license": True
        },
        "tax_rates": {
            "sales_tax": {
                "state_rate": 0.00,  # No sales tax
                "local_rates": False
            },
            "franchise_tax": {
                "flat_fee": 300.00
            }
        }
    }
}
