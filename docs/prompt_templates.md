# Prompt Templates

This project uses several targeted prompts instead of a single large prompt. 
Each prompt has a specific role in the agent pipeline.

## Resume Structuring Prompt (Planner)

Purpose:
Convert extracted resume text into a structured representation.

Main instructions given to the model:
- Organize the resume into sections such as summary, education, skills, experience, projects, and certifications
- Preserve the original content
- Do not invent new information
- Return a structured JSON format

The output becomes the structured resume representation used by later stages of the pipeline.

---

## Optimization Prompt (Generator)

Purpose:
Generate suggestions that improve the resume’s alignment with the job description.

Main instructions given to the model:
- Improve wording of summaries and bullet points
- Suggest phrasing that better reflects the job description
- Do not fabricate tools, experience, or responsibilities
- Return suggestions in structured JSON

These suggestions are presented to the user before any changes are applied.

---

## Skill Placement Prompt (Validator / Organizer)

Purpose:
Decide where newly added skills should appear in the resume.

Main instructions given to the model:
- Prefer placing skills in existing sections
- Create a new section only when necessary
- Return a JSON structure mapping each skill to a section
