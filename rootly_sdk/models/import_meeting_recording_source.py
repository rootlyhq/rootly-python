from typing import Literal, cast

ImportMeetingRecordingSource = Literal["recall_desktop_sdk"]

IMPORT_MEETING_RECORDING_SOURCE_VALUES: set[ImportMeetingRecordingSource] = {
    "recall_desktop_sdk",
}


def check_import_meeting_recording_source(value: str | None) -> ImportMeetingRecordingSource | None:
    if value is None:
        return None
    if value in IMPORT_MEETING_RECORDING_SOURCE_VALUES:
        return cast(ImportMeetingRecordingSource, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IMPORT_MEETING_RECORDING_SOURCE_VALUES!r}")
