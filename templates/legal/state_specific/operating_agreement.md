# OPERATING AGREEMENT
## {{business_name}}
### A {{state_name}} Limited Liability Company

THIS OPERATING AGREEMENT (the "Agreement") is made and entered into effective {{effective_date}}, by and among {{business_name}} (the "Company") and its member(s) ("Member(s)").

## ARTICLE I - COMPANY FORMATION

### 1.1 Formation
The Company was formed on {{formation_date}} when Articles of Organization were filed with the {{filing_agency}} of {{state_name}}.

### 1.2 Name
The name of the Company is {{business_name}}.

### 1.3 Principal Place of Business
The principal place of business is {{principal_office_address}}, {{principal_office_city}}, {{state_name}} {{principal_office_zip}}.

### 1.4 Registered Agent
The registered agent for service of process is {{registered_agent_name}}, located at {{registered_agent_address}}.

### 1.5 Term
{{#if perpetual_duration}}
The Company shall continue perpetually unless dissolved by:
a) A vote of the Member(s)
b) Operation of law
{{else}}
The Company shall continue until {{dissolution_date}} unless dissolved earlier by:
a) A vote of the Member(s)
b) Operation of law
{{/if}}

## ARTICLE II - BUSINESS PURPOSE

### 2.1 Purpose
{{#if specific_purpose}}
The specific purpose of the Company is: {{business_purpose}}
{{else}}
The Company is organized to engage in any lawful business purpose or activity for which Limited Liability Companies may be formed under the {{state_name}} Limited Liability Company Act.
{{/if}}

## ARTICLE III - MEMBERSHIP

### 3.1 Initial Member(s)
The initial Member(s) of the Company and their respective ownership interests are:
{{#each members}}
- {{name}}: {{ownership_percentage}}%
{{/each}}

### 3.2 Additional Members
{{#if single_member}}
Additional members may be admitted upon consent of the sole Member.
{{else}}
Additional members may be admitted upon consent of members holding {{new_member_approval_percentage}}% of the ownership interests.
{{/if}}

### 3.3 Member Capital Contributions
Initial capital contributions of the Member(s):
{{#each members}}
- {{name}}: ${{initial_contribution}}
{{/each}}

## ARTICLE IV - MANAGEMENT

### 4.1 Management Structure
{{#if member_managed}}
The Company shall be managed by its Member(s).
{{else}}
The Company shall be managed by Manager(s).
{{/if}}

### 4.2 {{#if member_managed}}Member{{else}}Manager{{/if}} Authority
{{#if member_managed}}
The Member(s) shall have full authority to bind the Company and make all decisions.
{{else}}
The following Manager(s) have been appointed:
{{#each managers}}
- {{name}}: {{title}}
{{/each}}
{{/if}}

{{#if state_code_is_de}}
### 4.3 Delaware Requirements
The Member(s) shall manage the Company in accordance with the Delaware Limited Liability Company Act.
{{/if}}

{{#if state_code_is_ca}}
### 4.3 California Requirements
The Company shall comply with all requirements of the California Revised Uniform Limited Liability Company Act.
{{/if}}

## ARTICLE V - CAPITAL ACCOUNTS AND ALLOCATIONS

### 5.1 Capital Accounts
Individual capital accounts shall be maintained for each Member.

### 5.2 Profits and Losses
Profits and losses shall be allocated as follows:
{{#each members}}
- {{name}}: {{profit_loss_percentage}}%
{{/each}}

## ARTICLE VI - DISTRIBUTIONS

### 6.1 Distributions
{{#if single_member}}
Distributions shall be made at the discretion of the Member.
{{else}}
Distributions shall be made in proportion to the Members' ownership interests.
{{/if}}

## ARTICLE VII - DISSOLUTION

### 7.1 Dissolution Events
The Company shall be dissolved upon:
a) Vote of the Member(s)
b) Sale of all Company assets
c) Operation of law

### 7.2 Winding Up
Upon dissolution, the Company shall wind up its affairs in accordance with {{state_name}} law.

## ARTICLE VIII - AMENDMENTS

### 8.1 Amendment Process
{{#if single_member}}
This Agreement may be amended by the sole Member.
{{else}}
This Agreement may be amended with approval of Members holding {{amendment_approval_percentage}}% of ownership interests.
{{/if}}

## ARTICLE IX - GOVERNING LAW

### 9.1 Governing Law
This Agreement shall be governed by the laws of {{state_name}}.

{{#if state_specific_provisions}}
## ARTICLE X - STATE-SPECIFIC PROVISIONS

### 10.1 {{state_name}} Requirements
{{state_specific_provisions}}
{{/if}}

## SIGNATURES

IN WITNESS WHEREOF, the Member(s) have executed this Operating Agreement as of the date first above written.

MEMBER(S):
{{#each members}}
_________________________
{{name}}
Date: _________________________

{{/each}}

{{#unless member_managed}}
MANAGER(S):
{{#each managers}}
_________________________
{{name}}
Date: _________________________

{{/each}}
{{/unless}}
