from enum import Enum


class NewScheduleRotationUserDataType(str, Enum):
    SCHEDULE_ROTATION_USERS = "schedule_rotation_users"

    def __str__(self) -> str:
        return str(self.value)
