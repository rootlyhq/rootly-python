from typing import Literal, cast

CreateGoToMeetingTaskParamsTaskType = Literal["create_go_to_meeting_task"]

CREATE_GO_TO_MEETING_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateGoToMeetingTaskParamsTaskType] = {
    "create_go_to_meeting_task",
}


def check_create_go_to_meeting_task_params_task_type(value: str | None) -> CreateGoToMeetingTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_GO_TO_MEETING_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateGoToMeetingTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_GO_TO_MEETING_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
