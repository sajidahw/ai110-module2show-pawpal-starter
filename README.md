# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Output from running `python main.py`:

```
=== Today's Schedule ===

[pending] Priority 1 | 2026-06-30 07:00 | Morning walk (Luna)
[pending] Priority 2 | 2026-06-30 09:00 | Clean litter box (Mochi)
[pending] Priority 2 | 2026-06-30 18:00 | Feed dinner (Luna)
[pending] Priority 3 | 2026-06-30 14:00 | Groom (Mochi)
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
 python -m pytest -v
======================================================================================== test session starts ========================================================================================
platform darwin --//.venv/bin/python
cachedir: .pytest_cache
rootdir: /pawpal+
plugins: anyio-4.13.0
collected 4 items                                                                                                                                                                                                          

tests/test_pawpal.py::test_mark_complete_changes_status PASSED                                                                                                                                                       [ 25%]
tests/test_pawpal.py::test_add_task_increases_pet_task_count PASSED                                                                                                                                                  [ 50%]
tests/test_pawpal.py::test_sort_tasks_by_priority_returns_ascending_order PASSED                                                                                                                                     [ 75%]
tests/test_pawpal.py::test_filter_by_status_returns_only_matching_tasks PASSED                                                                                                                                       [100%]

======================================================================================== 4 passed in 0.01s ========================================================================================

```

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | | e.g., by priority, duration |
| Filtering | | e.g., skip tasks if time runs out |
| Conflict handling | | e.g., overlapping time slots |
| Recurring tasks | | e.g., daily vs. weekly |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
