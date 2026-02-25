from typing import Literal, cast

CreateWebexMeetingTaskParamsTaskType = Literal["create_webex_meeting"]

CREATE_WEBEX_MEETING_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateWebexMeetingTaskParamsTaskType] = {
    "create_webex_meeting",
}


def check_create_webex_meeting_task_params_task_type(value: str | None) -> CreateWebexMeetingTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_WEBEX_MEETING_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateWebexMeetingTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_WEBEX_MEETING_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
