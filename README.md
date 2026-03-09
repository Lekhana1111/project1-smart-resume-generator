# Smart Resume Generator

## Project Description
This project builds an LLM-based resume optimization agent that improves a resume based on a target job description. The system parses a resume into structured sections, analyzes a job description to extract important skills and concepts, compares the two for alignment, and then generates controlled suggestions for improving the resume. The user stays involved throughout the editing process by choosing which suggestions to apply.

## Chosen Domain
This project falls under an approved custom domain: document optimization / resume optimization agent.

## Main Demo File
The full project is implemented in a single Google Colab notebook:

`demo.ipynb`

This notebook demonstrates the complete pipeline end to end.

## What the Agent Does
The agent performs the following steps:
- parses and structures resume content
- extracts important features from a job description
- measures alignment between the resume and the job description
- suggests skill additions and phrasing improvements
- lets the user review and apply selected changes
- exports the final optimized resume

## How to Run the Demo
This project is designed to run in Google Colab.

### Steps
1. Open `Agentic AI Project.ipynb` in Google Colab
2. Upload the required resume and job description files when prompted
3. Set your HuggingFace API token in the notebook environment
4. Run the notebook cells from top to bottom


## Repository Contents
- `Agentic AI Project.ipynb.ipynb` — full end-to-end Colab notebook
- `docs/` — design and architecture notes
- `Example Interactions/` - The notebook includes three example interaction sections demonstrating the
full agent loop. Due to privacy concerns, outputs generated using personal
resume data are not committed to the repository.

During the presentation, the notebook will be executed live to demonstrate
the full pipeline using sample inputs.
- `tests/` — simple validation and constraint checks

## Notes
The system is designed as a structured multi-stage agent instead of a single-prompt workflow. Each stage has a clear role, which makes the system easier to inspect, debug, and extend.
