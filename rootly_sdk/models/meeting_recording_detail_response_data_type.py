from typing import Literal, cast

MeetingRecordingDetailResponseDataType = Literal["meeting_recordings"]

MEETING_RECORDING_DETAIL_RESPONSE_DATA_TYPE_VALUES: set[MeetingRecordingDetailResponseDataType] = {
    "meeting_recordings",
}


def check_meeting_recording_detail_response_data_type(
    value: str | None,
) -> MeetingRecordingDetailResponseDataType | None:
    if value is None:
        return None
    if value in MEETING_RECORDING_DETAIL_RESPONSE_DATA_TYPE_VALUES:
        return cast(MeetingRecordingDetailResponseDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEETING_RECORDING_DETAIL_RESPONSE_DATA_TYPE_VALUES!r}"
    )
