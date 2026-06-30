from dataclasses import dataclass, field
from datetime import datetime


class Owner:
    def __init__(self, name: str, phone_number: str):
        self.name = name
        self.phone_number = phone_number
        self.pets = []

    def add_pet(self, pet):
        """Add a pet to this owner's list."""
        self.pets.append(pet)

    def remove_pet(self, pet):
        """Remove a pet; raises ValueError if the pet has pending tasks."""
        if any(not t.completed_status for t in pet.tasks):
            raise ValueError(
                f"{pet.name} has pending tasks. Complete or remove them first."
            )
        self.pets.remove(pet)

    def view_pets(self):
        """Return the list of pets belonging to this owner."""
        return self.pets


@dataclass
class Pet:
    name: str
    age: int
    animal_type: str
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        """Assign a task to this pet and set the back-reference."""
        task.pet = self
        self.tasks.append(task)

    def remove_task(self, task):
        """Remove a specific task from this pet's task list."""
        self.tasks.remove(task)

    def view_tasks(self):
        """Return all tasks assigned to this pet."""
        return self.tasks


@dataclass
class Task:
    description: str
    priority_level: int
    scheduled_time: datetime
    completed_status: bool = False
    pet: object = field(default=None)

    def is_overdue(self):
        """Return True if past scheduled time and not yet complete."""
        return (
            not self.completed_status and datetime.now() > self.scheduled_time
        )

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed_status = True

    def reschedule_task(self, time: datetime):
        """Update the scheduled time for this task."""
        self.scheduled_time = time

    def change_priority(self, level: int):
        """Update the priority level for this task."""
        self.priority_level = level


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    @property
    def tasks(self):
        """Flatten all tasks across every pet owned by this owner."""
        return [
            task for pet in self.owner.pets for task in pet.tasks
        ]

    def filter_by_date(self, date: datetime):
        """Return tasks scheduled on the given date."""
        return [
            t for t in self.tasks
            if t.scheduled_time.date() == date.date()
        ]

    def filter_by_status(self, completed: bool):
        """Return tasks matching the given completion status."""
        return [t for t in self.tasks if t.completed_status == completed]

    def sort_tasks_by_priority(self):
        """Return tasks sorted by priority level ascending."""
        return sorted(self.tasks, key=lambda t: t.priority_level)

    def sort_tasks_by_time(self):
        """Return tasks sorted by scheduled time ascending."""
        return sorted(self.tasks, key=lambda t: t.scheduled_time)

    def create_schedule(self):
        """Return tasks sorted by priority then time as a tiebreaker."""
        return sorted(
            self.tasks, key=lambda t: (t.priority_level, t.scheduled_time)
        )

    def view_schedule(self):
        """Print the daily schedule sorted by priority and time."""
        for task in self.create_schedule():
            status = "done" if task.completed_status else "pending"
            overdue = " [OVERDUE]" if task.is_overdue() else ""
            pet_name = task.pet.name if task.pet else "unknown"
            print(
                f"[{status}] Priority {task.priority_level} | "
                f"{task.scheduled_time:%Y-%m-%d %H:%M} | "
                f"{task.description} ({pet_name}){overdue}"
            )
