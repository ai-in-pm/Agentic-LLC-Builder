# NOTICE OF FORMATION
## {{business_name}}

NOTICE IS HEREBY GIVEN that {{business_name}}, a Limited Liability Company, was formed on {{formation_date}} under the laws of the State of {{state_name}}.

{{#if state_code_is_ny}}
The office of the Limited Liability Company is located in {{county_name}} County. The Secretary of State has been designated as agent of the Limited Liability Company upon whom process against it may be served and the Secretary of State shall mail a copy of any process against the Limited Liability Company to:

{{business_name}}
{{mailing_address}}

The purpose of the Limited Liability Company is to engage in any lawful act or activity for which Limited Liability Companies may be organized under the Limited Liability Company Law.
{{/if}}

{{#if state_code_is_az}}
The address of the registered office is:
{{registered_agent_address}}

The name and address of the statutory agent is:
{{registered_agent_name}}
{{registered_agent_address}}

Management of the Limited Liability Company is {{#if member_managed}}vested in its member(s){{else}}vested in its manager(s){{/if}}.
{{/if}}

{{#if state_code_is_ne}}
The Limited Liability Company commenced on {{formation_date}} and its duration is {{#if perpetual_duration}}perpetual{{else}}until {{dissolution_date}}{{/if}}.

The affairs of the Company are to be conducted by its {{#if member_managed}}member(s){{else}}manager(s){{/if}}.
{{/if}}

This notice is being published in accordance with state law requirements for:
- First Publication Date: {{first_publication_date}}
- Final Publication Date: {{final_publication_date}}
- Publication Period: {{publication_period}} weeks
- Required Newspapers: {{newspapers}}

{{#if affidavit_required}}
An affidavit of publication with copies of the published notices will be filed with:
{{filing_agency}}
{{filing_address}}
{{/if}}
