from typing import Literal, cast

CreateZoomMeetingTaskParamsRecordingMode = Literal["audio_only", "gallery_view", "gallery_view_v2", "speaker_view"]

CREATE_ZOOM_MEETING_TASK_PARAMS_RECORDING_MODE_VALUES: set[CreateZoomMeetingTaskParamsRecordingMode] = {
    "audio_only",
    "gallery_view",
    "gallery_view_v2",
    "speaker_view",
}


def check_create_zoom_meeting_task_params_recording_mode(value: str | None) -> CreateZoomMeetingTaskParamsRecordingMode | None:
    if value is None:
        return None
    if value in CREATE_ZOOM_MEETING_TASK_PARAMS_RECORDING_MODE_VALUES:
        return cast(CreateZoomMeetingTaskParamsRecordingMode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_ZOOM_MEETING_TASK_PARAMS_RECORDING_MODE_VALUES!r}"
    )
