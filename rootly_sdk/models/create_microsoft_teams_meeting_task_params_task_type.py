from typing import Literal, cast

CreateMicrosoftTeamsMeetingTaskParamsTaskType = Literal["create_microsoft_teams_meeting"]

CREATE_MICROSOFT_TEAMS_MEETING_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateMicrosoftTeamsMeetingTaskParamsTaskType] = {
    "create_microsoft_teams_meeting",
}


def check_create_microsoft_teams_meeting_task_params_task_type(
    value: str | None,
) -> CreateMicrosoftTeamsMeetingTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_MICROSOFT_TEAMS_MEETING_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateMicrosoftTeamsMeetingTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_MICROSOFT_TEAMS_MEETING_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
