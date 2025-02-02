# REGISTERED AGENT CONSENT TO APPOINTMENT
## {{business_name}}

### STATE OF {{state_name}}
### DEPARTMENT OF {{department_name}}

I, {{registered_agent_name}}, hereby consent to serve as the Registered Agent in the State of {{state_name}} for {{business_name}}, a Limited Liability Company.

## REGISTERED AGENT INFORMATION

### Individual/Entity Name:
{{registered_agent_name}}

### Physical Address in {{state_name}}:
{{registered_agent_address.street1}}
{{#if registered_agent_address.street2}}{{registered_agent_address.street2}}{{/if}}
{{registered_agent_address.city}}, {{state_name}} {{registered_agent_address.zip}}

### Mailing Address (if different):
{{#if registered_agent_mailing_address}}
{{registered_agent_mailing_address.street1}}
{{#if registered_agent_mailing_address.street2}}{{registered_agent_mailing_address.street2}}{{/if}}
{{registered_agent_mailing_address.city}}, {{registered_agent_mailing_address.state}} {{registered_agent_mailing_address.zip}}
{{else}}
Same as Physical Address
{{/if}}

## CONSENT AND ACKNOWLEDGMENT

1. I consent to serve as Registered Agent for {{business_name}} (the "Company").

2. I understand and acknowledge that, as Registered Agent, I am agreeing to:
   - Accept service of process and official mail on behalf of the Company
   - Forward all service of process and official mail to the Company in a timely manner
   - Maintain a physical address in {{state_name}} that is open during normal business hours
   - Notify the {{department_name}} if my address changes
   - Resign in accordance with state law if I can no longer serve as Registered Agent

{{#if state_code_is_az}}
3. I am either:
   - A resident of Arizona and am not a member, manager, or employee of the Company; or
   - An entity authorized to transact business in Arizona
{{/if}}

{{#if state_code_is_ca}}
3. If an individual, I am a resident of California and am at least 18 years of age.
{{/if}}

{{#if state_code_is_de}}
3. I certify that I maintain a business office in Delaware that is generally open during normal business hours to accept service of process and otherwise perform the functions of a registered agent.
{{/if}}

{{#if state_code_is_fl}}
3. I am:
   - A permanent resident of Florida and am not a member or employee of the Company; or
   - An entity authorized to transact business in Florida
{{/if}}

## SIGNATURE

By signing below, I affirm that I have read and understand this Consent to Appointment, and that the information provided is true and correct.

Signature: _________________________
Name: {{registered_agent_name}}
Date: {{execution_date}}

{{#if notary_required}}
## NOTARY ACKNOWLEDGMENT

State of {{state_name}}
County of {{county_name}}

The foregoing instrument was acknowledged before me this {{execution_date}} by {{registered_agent_name}}, who is personally known to me or who has produced _________________ as identification.

Notary Public Signature: _________________________
Name: _________________________
Commission Number: _________________________
Commission Expires: _________________________
{{/if}}

{{#if state_specific_requirements}}
## ADDITIONAL STATE REQUIREMENTS
{{state_specific_requirements}}
{{/if}}
