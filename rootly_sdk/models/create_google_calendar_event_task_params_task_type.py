from enum import Enum


class CreateGoogleCalendarEventTaskParamsTaskType(str, Enum):
    CREATE_GOOGLE_CALENDAR_EVENT = "create_google_calendar_event"

    def __str__(self) -> str:
        return str(self.value)
