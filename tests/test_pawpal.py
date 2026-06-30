from datetime import datetime
from pawpal_system import Pet, Task


def test_mark_complete_changes_status():
    task = Task(description="Feed", priority_level=1, scheduled_time=datetime(2026, 6, 30, 8, 0))
    assert task.completed_status is False
    task.mark_complete()
    assert task.completed_status is True


def test_add_task_increases_pet_task_count():
    pet = Pet(name="Luna", age=3, animal_type="Dog")
    assert len(pet.tasks) == 0
    pet.add_task(Task(description="Walk", priority_level=1, scheduled_time=datetime(2026, 6, 30, 7, 0)))
    assert len(pet.tasks) == 1
