from dataclasses import dataclass, field
from datetime import datetime, date, time
from typing import ClassVar

from app.services.util import generate_unique_id, date_lower_than_today_error, event_not_found_error, \
    reminder_not_found_error, slot_not_available_error

@dataclass
class Reminder:
    EMAIL: ClassVar[str] = "email"
    SYSTEM: ClassVar[str] = "system"
    date_time: datetime
    type : str = field(default=EMAIL)
    def __str__(self):
        return f"Reminder on {self.date_time} of type {self.type}"

from dataclasses import dataclass, field
from datetime import date, time
from app.services.util import generate_unique_id, reminder_not_found_error
from app.models.reminder import Reminder

@dataclass
class Event:
    title: str
    description: str
    date_ : date
    start_at: time
    end_at: time
    reminders: list[Reminder] = field(default_factory=list)
    id: str = field(default_factory=generate_unique_id)

    def add_reminder(self,reminder_time: time, message: str):
        reminder = Reminder(time=reminder_time, message=message)
        self.reminders.append(reminder)
    
    def delete_reminder(self,reminder_index: int):
        if 0 <= reminder_index < len (self.reminders):
            del self.reminders[reminder_index]
        else:
            reminder_not_found_error()

    def __str__(self)-> str:
        return (f"ID: {self.id}\n"
                f"Event title: {self.title}\n"
                f"Description: {self.description}\n"


from datetime import date, time, timedelta
from app.services.util import slot_not_avaliable_error, event_not_found_error

Class Day:
    def__init__(self, date_:date):
        self.






















# TODO: Implement Reminder class here


# TODO: Implement Event class here


# TODO: Implement Day class here


# TODO: Implement Calendar class here
