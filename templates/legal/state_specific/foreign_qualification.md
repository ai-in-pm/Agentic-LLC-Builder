# APPLICATION FOR CERTIFICATE OF AUTHORITY
## FOREIGN LIMITED LIABILITY COMPANY
### STATE OF {{state_name}}

## 1. ENTITY INFORMATION

### Limited Liability Company Name:
{{business_name}}

### Alternate Name (if required):
{{#if alternate_name}}{{alternate_name}}{{/if}}

### Jurisdiction of Formation:
{{formation_state}}

### Date of Formation:
{{formation_date}}

### Duration:
{{#if perpetual_duration}}Perpetual{{else}}Until {{dissolution_date}}{{/if}}

## 2. PRINCIPAL OFFICE ADDRESS

{{principal_office_address.street1}}
{{#if principal_office_address.street2}}{{principal_office_address.street2}}{{/if}}
{{principal_office_address.city}}, {{principal_office_address.state}} {{principal_office_address.zip}}

## 3. REGISTERED AGENT INFORMATION

### Name:
{{registered_agent_name}}

### Physical Address in {{state_name}}:
{{registered_agent_address.street1}}
{{#if registered_agent_address.street2}}{{registered_agent_address.street2}}{{/if}}
{{registered_agent_address.city}}, {{state_name}} {{registered_agent_address.zip}}

## 4. MANAGEMENT

The Limited Liability Company is:
[ ] Member-Managed
[ ] Manager-Managed

{{#if manager_managed}}
### Manager Information:
{{#each managers}}
Name: {{name}}
Address: {{address}}

{{/each}}
{{/if}}

## 5. BUSINESS PURPOSE

{{#if specific_purpose_required}}
The specific purpose of the business is:
{{business_purpose}}
{{else}}
The purpose of the Limited Liability Company is to engage in any lawful business activity for which a Foreign Limited Liability Company may be registered under the laws of {{state_name}}.
{{/if}}

## 6. ADDITIONAL INFORMATION

### Date Began Business in {{state_name}}:
{{business_start_date}}

### Federal Employer ID Number (FEIN):
{{ein}}

{{#if state_code_is_ny}}
### Registered Office in New York:
{{ny_registered_office}}

### Service of Process Address:
{{service_of_process_address}}
{{/if}}

{{#if state_code_is_ca}}
### LLC Type in California:
[ ] Professional
[ ] Non-Professional
{{/if}}

## 7. REQUIRED ATTACHMENTS

1. Certificate of Good Standing from jurisdiction of formation (dated within 90 days)
2. Filing fee of ${{filing_fee}}
{{#if additional_requirements}}
3. {{additional_requirements}}
{{/if}}

## 8. EXECUTION

The undersigned affirms, under penalties of perjury, that the statements made in this Application are true and correct.

Signature: _________________________
Name: {{signer_name}}
Title: {{signer_title}}
Date: {{execution_date}}

{{#if notary_required}}
## NOTARY ACKNOWLEDGMENT

State of {{notary_state}}
County of {{notary_county}}

The foregoing instrument was acknowledged before me this {{execution_date}} by {{signer_name}}, who is personally known to me or who has produced _________________ as identification.

Notary Public Signature: _________________________
Name: _________________________
Commission Number: _________________________
Commission Expires: _________________________
{{/if}}

{{#if state_specific_requirements}}
## ADDITIONAL STATE REQUIREMENTS
{{state_specific_requirements}}
{{/if}}
