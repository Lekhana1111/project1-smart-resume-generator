import re

def test_no_duplicate_skills():
    skills = ["Python", "SQL", "Python"]
    deduped = []
    seen = set()

    for s in skills:
        key = s.lower()
        if key not in seen:
            seen.add(key)
            deduped.append(s)

    assert deduped == ["Python", "SQL"]


def test_json_extraction_from_llm():
    raw = """```json
    {"placements":[{"skill":"BI tools","target_section":"Data Analysis"}]}
    ```"""

    match = re.search(r"\{[\s\S]*\}", raw)
    assert match is not None


def test_similarity_threshold():
    similarity_score = 0.42
    threshold = 0.45

    assert similarity_score < threshold
