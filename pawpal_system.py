from dataclasses import dataclass, field
from datetime import datetime


class Owner:
    def __init__(self, name: str, phone_number: str):
        self.name = name
        self.phone_number = phone_number
        self.pets = []

    def add_pet(self, pet):
        pass

    def remove_pet(self, pet):
        pass

    def view_pets(self):
        pass


@dataclass
class Pet:
    name: str
    age: int
    animal_type: str
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        pass

    def remove_task(self, task):
        pass

    def view_tasks(self):
        pass


@dataclass
class Task:
    description: str
    priority_level: int
    scheduled_time: datetime
    completed_status: bool = False

    def due_task(self):
        pass

    def mark_complete(self):
        pass

    def reschedule_task(self, time: datetime):
        pass

    def change_priority(self, level: int):
        pass


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner
        self.tasks = []

    def collect_tasks(self):
        pass

    def create_schedule(self):
        pass

    def view_schedule(self):
        pass

    def sort_tasks_by_priority(self):
        pass

    def sort_tasks_by_time(self):
        pass
