import pytest
from datetime import datetime
from pawpal_system import Owner, Pet, Task, Scheduler


def make_task(description, priority, hour):
    return Task(
        description=description,
        priority_level=priority,
        scheduled_time=datetime(2026, 6, 30, hour, 0),
    )


def test_mark_complete_changes_status():
    task = make_task("Feed", 1, 8)
    assert task.completed_status is False
    task.mark_complete()
    assert task.completed_status is True


def test_add_task_increases_pet_task_count():
    pet = Pet(name="Luna", age=3, animal_type="Dog")
    assert len(pet.tasks) == 0
    pet.add_task(make_task("Walk", 1, 7))
    assert len(pet.tasks) == 1


def test_sort_tasks_by_priority_returns_ascending_order():
    owner = Owner(name="Sarah", phone_number="555-0100")
    pet = Pet(name="Luna", age=3, animal_type="Dog")
    owner.add_pet(pet)
    pet.add_task(make_task("Groom", 3, 14))
    pet.add_task(make_task("Medicate", 1, 8))
    pet.add_task(make_task("Walk", 2, 7))
    scheduler = Scheduler(owner=owner)
    sorted_tasks = scheduler.sort_tasks_by_priority()
    priorities = [t.priority_level for t in sorted_tasks]
    assert priorities == sorted(priorities)


def test_remove_pet_drops_pet_and_all_tasks():
    owner = Owner(name="Sarah", phone_number="555-0100")
    pet = Pet(name="Luna", age=3, animal_type="Dog")
    owner.add_pet(pet)
    task = make_task("Walk", 1, 7)
    task.mark_complete()
    pet.add_task(task)
    owner.remove_pet(pet)
    assert pet not in owner.pets
    assert len(owner.pets) == 0


def test_remove_pet_raises_if_pending_tasks():
    owner = Owner(name="Sarah", phone_number="555-0100")
    pet = Pet(name="Luna", age=3, animal_type="Dog")
    owner.add_pet(pet)
    pet.add_task(make_task("Walk", 1, 7))
    with pytest.raises(ValueError, match="pending tasks"):
        owner.remove_pet(pet)


def test_filter_by_status_returns_only_matching_tasks():
    owner = Owner(name="Sarah", phone_number="555-0100")
    pet = Pet(name="Mochi", age=1, animal_type="Cat")
    owner.add_pet(pet)
    done = make_task("Feed", 1, 8)
    pending = make_task("Groom", 2, 10)
    done.mark_complete()
    pet.add_task(done)
    pet.add_task(pending)
    scheduler = Scheduler(owner=owner)
    completed = scheduler.filter_by_status(completed=True)
    not_completed = scheduler.filter_by_status(completed=False)
    assert all(t.completed_status for t in completed)
    assert not any(t.completed_status for t in not_completed)
