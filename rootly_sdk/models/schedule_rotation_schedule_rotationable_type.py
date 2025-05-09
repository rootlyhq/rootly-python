from enum import Enum


class ScheduleRotationScheduleRotationableType(str, Enum):
    SCHEDULEBIWEEKLYROTATION = "ScheduleBiweeklyRotation"
    SCHEDULECUSTOMROTATION = "ScheduleCustomRotation"
    SCHEDULEDAILYROTATION = "ScheduleDailyRotation"
    SCHEDULEMONTHLYROTATION = "ScheduleMonthlyRotation"
    SCHEDULEWEEKLYROTATION = "ScheduleWeeklyRotation"

    def __str__(self) -> str:
        return str(self.value)
