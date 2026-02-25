from typing import Literal, cast

CreateZoomMeetingTaskParamsTaskType = Literal["create_zoom_meeting"]

CREATE_ZOOM_MEETING_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateZoomMeetingTaskParamsTaskType] = {
    "create_zoom_meeting",
}


def check_create_zoom_meeting_task_params_task_type(value: str | None) -> CreateZoomMeetingTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_ZOOM_MEETING_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateZoomMeetingTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_ZOOM_MEETING_TASK_PARAMS_TASK_TYPE_VALUES!r}")
