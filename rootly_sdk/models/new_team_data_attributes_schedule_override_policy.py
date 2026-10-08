from typing import Literal

NewTeamDataAttributesScheduleOverridePolicy = Literal["admins", "everyone", "members"]

NEW_TEAM_DATA_ATTRIBUTES_SCHEDULE_OVERRIDE_POLICY_VALUES: set[NewTeamDataAttributesScheduleOverridePolicy] = {
    "admins",
    "everyone",
    "members",
}


def check_new_team_data_attributes_schedule_override_policy(
    value: str | None,
) -> NewTeamDataAttributesScheduleOverridePolicy | None:
    if value is None:
        return None
    if value in NEW_TEAM_DATA_ATTRIBUTES_SCHEDULE_OVERRIDE_POLICY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_TEAM_DATA_ATTRIBUTES_SCHEDULE_OVERRIDE_POLICY_VALUES!r}"
    )
