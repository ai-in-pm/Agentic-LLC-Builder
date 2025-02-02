# ARTICLES OF ORGANIZATION
## {{business_name}}
### State of {{state_name}}

## ARTICLE I - ENTITY NAME AND TYPE
The name of the Limited Liability Company is: {{business_name}}

## ARTICLE II - REGISTERED AGENT
### Section 2.1 - Registered Agent Name
{{registered_agent_name}}

### Section 2.2 - Registered Office Address
{{registered_agent_address}}
{{registered_agent_city}}, {{state_name}} {{registered_agent_zip}}

{{#if state_code_is_ny_or_ct}}
### Section 2.3 - Service of Process Address
Address for Service of Process:
{{service_of_process_address}}
{{/if}}

## ARTICLE III - PRINCIPAL OFFICE
{{principal_office_address}}
{{principal_office_city}}, {{state_name}} {{principal_office_zip}}

## ARTICLE IV - PURPOSE
{{#if specific_purpose_required}}
The specific purpose of this Limited Liability Company is:
{{business_purpose}}
{{else}}
This Limited Liability Company is organized to engage in any lawful activity for which a Limited Liability Company may be organized in {{state_name}}.
{{/if}}

{{#if state_code_is_ca}}
## ARTICLE V - LLC TYPE
This LLC will be managed by:
[ ] One Manager
[ ] More than One Manager
[ ] All Limited Liability Company Member(s)
{{/if}}

{{#if state_code_is_ny}}
## ARTICLE V - PUBLICATION
The Secretary of State is designated as agent of the Limited Liability Company upon whom process against it may be served. The address to which the Secretary of State shall mail a copy of any process against the Limited Liability Company served upon him or her is:
{{service_of_process_address}}
{{/if}}

{{#if state_code_is_az}}
## ARTICLE V - STATUTORY AGENT ACCEPTANCE
I, {{registered_agent_name}}, having been designated to act as Statutory Agent, hereby consent to act in that capacity until removed or resignation is submitted.

Signature: _________________________
Date: _________________________
{{/if}}

## ARTICLE {{next_article}} - DURATION
{{#if perpetual_duration}}
The duration of this Limited Liability Company shall be perpetual.
{{else}}
This Limited Liability Company shall dissolve on {{dissolution_date}}.
{{/if}}

## ARTICLE {{next_article}} - MANAGEMENT
{{#if member_managed}}
This Limited Liability Company shall be managed by its members.
{{else}}
This Limited Liability Company shall be managed by managers.
{{/if}}

{{#if state_code_is_fl}}
## ARTICLE {{next_article}} - EFFECTIVE DATE
{{#if delayed_effective_date}}
The effective date of these Articles of Organization shall be {{effective_date}}.
{{else}}
These Articles of Organization shall be effective upon filing.
{{/if}}
{{/if}}

{{#if state_code_is_tx}}
## ARTICLE {{next_article}} - GOVERNING REGULATIONS
A. The Limited Liability Company will have regulations.
B. The regulations are to be adopted by the member(s).
C. The authority to amend or repeal regulations is reserved to the member(s).
{{/if}}

## ARTICLE {{next_article}} - ORGANIZER
The name and address of the organizer is:
{{organizer_name}}
{{organizer_address}}
{{organizer_city}}, {{organizer_state}} {{organizer_zip}}

{{#if state_code_is_ca_or_ny}}
## ARTICLE {{next_article}} - EXECUTION
IN WITNESS WHEREOF, the undersigned has executed these Articles of Organization on {{execution_date}}.

Signature: _________________________
Name: {{organizer_name}}
Title: Organizer
{{/if}}

{{#if state_code_is_de}}
## CERTIFICATE OF FORMATION
This Certificate of Formation has been executed by the undersigned on {{execution_date}}.

By: _________________________
{{organizer_name}}, Authorized Person
{{/if}}

{{#if state_code_is_nv}}
## ARTICLES OF ORGANIZATION EXECUTION
I declare that I am the person who executed this instrument, which execution is my act and deed.

Signature: _________________________
{{organizer_name}}
{{/if}}

{{#if additional_state_requirements}}
## ADDITIONAL STATE REQUIREMENTS
{{additional_state_requirements}}
{{/if}}

STATE FILING INFORMATION:
Filing Agency: {{filing_agency}}
Filing Fee: ${{filing_fee}}
Processing Time: {{processing_time}}
{{#if publication_required}}
Publication Required: Yes
Publication Period: {{publication_period}}
Publication Deadline: {{publication_deadline}}
{{/if}}
