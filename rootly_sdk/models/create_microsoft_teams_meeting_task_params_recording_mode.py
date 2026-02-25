from typing import Literal, cast

CreateMicrosoftTeamsMeetingTaskParamsRecordingMode = Literal[
    "audio_only", "gallery_view", "gallery_view_v2", "speaker_view"
]

CREATE_MICROSOFT_TEAMS_MEETING_TASK_PARAMS_RECORDING_MODE_VALUES: set[
    CreateMicrosoftTeamsMeetingTaskParamsRecordingMode
] = {
    "audio_only",
    "gallery_view",
    "gallery_view_v2",
    "speaker_view",
}


def check_create_microsoft_teams_meeting_task_params_recording_mode(
    value: str | None,
) -> CreateMicrosoftTeamsMeetingTaskParamsRecordingMode | None:
    if value is None:
        return None
    if value in CREATE_MICROSOFT_TEAMS_MEETING_TASK_PARAMS_RECORDING_MODE_VALUES:
        return cast(CreateMicrosoftTeamsMeetingTaskParamsRecordingMode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_MICROSOFT_TEAMS_MEETING_TASK_PARAMS_RECORDING_MODE_VALUES!r}"
    )
