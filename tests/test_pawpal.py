from datetime import datetime
from pawpal_system import Owner, Pet, Task, Scheduler


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


def test_sort_tasks_by_priority_returns_ascending_order():
    owner = Owner(name="Sajidah", phone_number="555-0100")
    pet = Pet(name="Luna", age=3, animal_type="Dog")
    owner.add_pet(pet)
    pet.add_task(Task(description="Groom", priority_level=3, scheduled_time=datetime(2026, 6, 30, 14, 0)))
    pet.add_task(Task(description="Medicate", priority_level=1, scheduled_time=datetime(2026, 6, 30, 8, 0)))
    pet.add_task(Task(description="Walk", priority_level=2, scheduled_time=datetime(2026, 6, 30, 7, 0)))
    scheduler = Scheduler(owner=owner)
    sorted_tasks = scheduler.sort_tasks_by_priority()
    priorities = [t.priority_level for t in sorted_tasks]
    assert priorities == sorted(priorities)


def test_filter_by_status_returns_only_matching_tasks():
    owner = Owner(name="Sajidah", phone_number="555-0100")
    pet = Pet(name="Mochi", age=1, animal_type="Cat")
    owner.add_pet(pet)
    done = Task(description="Feed", priority_level=1, scheduled_time=datetime(2026, 6, 30, 8, 0))
    pending = Task(description="Groom", priority_level=2, scheduled_time=datetime(2026, 6, 30, 10, 0))
    done.mark_complete()
    pet.add_task(done)
    pet.add_task(pending)
    scheduler = Scheduler(owner=owner)
    assert all(t.completed_status for t in scheduler.filter_by_status(completed=True))
    assert not any(t.completed_status for t in scheduler.filter_by_status(completed=False))
