from typing import Literal, cast

CreateWebexMeetingTaskParamsRecordingMode = Literal["audio_only", "gallery_view", "gallery_view_v2", "speaker_view"]

CREATE_WEBEX_MEETING_TASK_PARAMS_RECORDING_MODE_VALUES: set[CreateWebexMeetingTaskParamsRecordingMode] = {
    "audio_only",
    "gallery_view",
    "gallery_view_v2",
    "speaker_view",
}


def check_create_webex_meeting_task_params_recording_mode(
    value: str | None,
) -> CreateWebexMeetingTaskParamsRecordingMode | None:
    if value is None:
        return None
    if value in CREATE_WEBEX_MEETING_TASK_PARAMS_RECORDING_MODE_VALUES:
        return cast(CreateWebexMeetingTaskParamsRecordingMode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_WEBEX_MEETING_TASK_PARAMS_RECORDING_MODE_VALUES!r}"
    )
