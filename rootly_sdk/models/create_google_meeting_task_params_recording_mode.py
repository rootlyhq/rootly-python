from typing import Literal, cast

CreateGoogleMeetingTaskParamsRecordingMode = Literal["audio_only", "gallery_view", "gallery_view_v2", "speaker_view"]

CREATE_GOOGLE_MEETING_TASK_PARAMS_RECORDING_MODE_VALUES: set[CreateGoogleMeetingTaskParamsRecordingMode] = {
    "audio_only",
    "gallery_view",
    "gallery_view_v2",
    "speaker_view",
}


def check_create_google_meeting_task_params_recording_mode(value: str | None) -> CreateGoogleMeetingTaskParamsRecordingMode | None:
    if value is None:
        return None
    if value in CREATE_GOOGLE_MEETING_TASK_PARAMS_RECORDING_MODE_VALUES:
        return cast(CreateGoogleMeetingTaskParamsRecordingMode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_GOOGLE_MEETING_TASK_PARAMS_RECORDING_MODE_VALUES!r}"
    )
