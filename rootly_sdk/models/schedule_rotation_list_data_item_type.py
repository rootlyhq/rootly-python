from typing import Literal, cast

ScheduleRotationListDataItemType = Literal["schedule_rotations"]

SCHEDULE_ROTATION_LIST_DATA_ITEM_TYPE_VALUES: set[ScheduleRotationListDataItemType] = {
    "schedule_rotations",
}


def check_schedule_rotation_list_data_item_type(value: str | None) -> ScheduleRotationListDataItemType | None:
    if value is None:
        return None
    if value in SCHEDULE_ROTATION_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(ScheduleRotationListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SCHEDULE_ROTATION_LIST_DATA_ITEM_TYPE_VALUES!r}")
