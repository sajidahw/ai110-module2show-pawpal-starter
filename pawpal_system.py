from dataclasses import dataclass, field
from datetime import datetime


class Owner:
    def __init__(self, name: str, phone_number: str):
        self.name = name
        self.phone_number = phone_number
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def remove_pet(self, pet):
        self.pets.remove(pet)

    def view_pets(self):
        return self.pets


@dataclass
class Pet:
    name: str
    age: int
    animal_type: str
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        task.pet = self
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def view_tasks(self):
        return self.tasks


@dataclass
class Task:
    description: str
    priority_level: int
    scheduled_time: datetime
    completed_status: bool = False
    pet: object = field(default=None)

    def is_overdue(self):
        return not self.completed_status and datetime.now() > self.scheduled_time

    def mark_complete(self):
        self.completed_status = True

    def reschedule_task(self, time: datetime):
        self.scheduled_time = time

    def change_priority(self, level: int):
        self.priority_level = level


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    @property
    def tasks(self):
        return [task for pet in self.owner.pets for task in pet.tasks]

    def filter_by_date(self, date: datetime):
        return [t for t in self.tasks if t.scheduled_time.date() == date.date()]

    def filter_by_status(self, completed: bool):
        return [t for t in self.tasks if t.completed_status == completed]

    def sort_tasks_by_priority(self):
        return sorted(self.tasks, key=lambda t: t.priority_level)

    def sort_tasks_by_time(self):
        return sorted(self.tasks, key=lambda t: t.scheduled_time)

    def create_schedule(self):
        return sorted(self.tasks, key=lambda t: (t.priority_level, t.scheduled_time))

    def view_schedule(self):
        for task in self.create_schedule():
            status = "done" if task.completed_status else "pending"
            overdue = " [OVERDUE]" if task.is_overdue() else ""
            pet_name = task.pet.name if task.pet else "unknown"
            print(f"[{status}] Priority {task.priority_level} | {task.scheduled_time:%Y-%m-%d %H:%M} | {task.description} ({pet_name}){overdue}")
