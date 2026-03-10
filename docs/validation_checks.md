# Validation and Safety Checks

Several validation steps are included to ensure the system produces safe and consistent results.

## Structured Resume Validation

The resume is represented using structured schemas.  
These schemas enforce the expected format for sections such as education, experience, projects, and skills.

## Similarity Thresholds

Semantic similarity thresholds are used when comparing resume content with job description features.  
This prevents unrelated text from being incorrectly treated as a matching skill.

## Duplicate Skill Prevention

When skills are added to the resume, the system checks whether that skill already exists in another section.  
This prevents repeated or redundant skill entries.

## Prompt Constraints

The language model prompts explicitly instruct the model:

- not to invent new experience
- not to fabricate tools or responsibilities
- only to improve phrasing of existing information

## Human-in-the-Loop Validation

All generated suggestions are shown to the user before they are applied.  
The user can accept, reject, or ignore each suggestion before the final resume is generated.
