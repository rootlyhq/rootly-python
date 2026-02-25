from typing import Literal, cast

CreateGoogleMeetingTaskParamsTaskType = Literal["create_google_meeting"]

CREATE_GOOGLE_MEETING_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateGoogleMeetingTaskParamsTaskType] = {
    "create_google_meeting",
}


def check_create_google_meeting_task_params_task_type(
    value: str | None,
) -> CreateGoogleMeetingTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_GOOGLE_MEETING_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateGoogleMeetingTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_GOOGLE_MEETING_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
