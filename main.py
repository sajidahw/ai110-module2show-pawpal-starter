from datetime import datetime
from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner(name="Sajidah", phone_number="555-0100")

luna = Pet(name="Luna", age=3, animal_type="Dog")
mochi = Pet(name="Mochi", age=1, animal_type="Cat")

owner.add_pet(luna)
owner.add_pet(mochi)

luna.add_task(Task(description="Morning walk", priority_level=1, scheduled_time=datetime(2026, 6, 30, 7, 0)))
luna.add_task(Task(description="Feed dinner", priority_level=2, scheduled_time=datetime(2026, 6, 30, 18, 0)))
mochi.add_task(Task(description="Clean litter box", priority_level=2, scheduled_time=datetime(2026, 6, 30, 9, 0)))
mochi.add_task(Task(description="Groom", priority_level=3, scheduled_time=datetime(2026, 6, 30, 14, 0)))

scheduler = Scheduler(owner=owner)

print("=== Today's Schedule ===\n")
scheduler.view_schedule()
