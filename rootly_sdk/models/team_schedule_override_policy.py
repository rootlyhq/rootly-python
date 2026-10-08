from typing import Literal

TeamScheduleOverridePolicy = Literal["admins", "everyone", "members"]

TEAM_SCHEDULE_OVERRIDE_POLICY_VALUES: set[TeamScheduleOverridePolicy] = {
    "admins",
    "everyone",
    "members",
}


def check_team_schedule_override_policy(value: str | None) -> TeamScheduleOverridePolicy | None:
    if value is None:
        return None
    if value in TEAM_SCHEDULE_OVERRIDE_POLICY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TEAM_SCHEDULE_OVERRIDE_POLICY_VALUES!r}")
