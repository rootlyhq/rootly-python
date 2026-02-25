from typing import Literal, cast

CreateZoomMeetingTaskParamsAutoRecording = Literal["cloud", "local", "none"]

CREATE_ZOOM_MEETING_TASK_PARAMS_AUTO_RECORDING_VALUES: set[CreateZoomMeetingTaskParamsAutoRecording] = {
    "cloud",
    "local",
    "none",
}


def check_create_zoom_meeting_task_params_auto_recording(
    value: str | None,
) -> CreateZoomMeetingTaskParamsAutoRecording | None:
    if value is None:
        return None
    if value in CREATE_ZOOM_MEETING_TASK_PARAMS_AUTO_RECORDING_VALUES:
        return cast(CreateZoomMeetingTaskParamsAutoRecording, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_ZOOM_MEETING_TASK_PARAMS_AUTO_RECORDING_VALUES!r}"
    )
