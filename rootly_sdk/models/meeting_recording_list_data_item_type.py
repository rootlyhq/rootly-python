from typing import Literal, cast

MeetingRecordingListDataItemType = Literal["meeting_recordings"]

MEETING_RECORDING_LIST_DATA_ITEM_TYPE_VALUES: set[MeetingRecordingListDataItemType] = {
    "meeting_recordings",
}


def check_meeting_recording_list_data_item_type(value: str | None) -> MeetingRecordingListDataItemType | None:
    if value is None:
        return None
    if value in MEETING_RECORDING_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(MeetingRecordingListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MEETING_RECORDING_LIST_DATA_ITEM_TYPE_VALUES!r}")
