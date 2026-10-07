from typing import Literal

UpdateTeamDataAttributesScheduleOverridePolicy = Literal["admins", "everyone", "members"]

UPDATE_TEAM_DATA_ATTRIBUTES_SCHEDULE_OVERRIDE_POLICY_VALUES: set[UpdateTeamDataAttributesScheduleOverridePolicy] = {
    "admins",
    "everyone",
    "members",
}


def check_update_team_data_attributes_schedule_override_policy(
    value: str | None,
) -> UpdateTeamDataAttributesScheduleOverridePolicy | None:
    if value is None:
        return None
    if value in UPDATE_TEAM_DATA_ATTRIBUTES_SCHEDULE_OVERRIDE_POLICY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_TEAM_DATA_ATTRIBUTES_SCHEDULE_OVERRIDE_POLICY_VALUES!r}"
    )
