from typing import Literal, cast

ScheduleListDataItemType = Literal["schedules"]

SCHEDULE_LIST_DATA_ITEM_TYPE_VALUES: set[ScheduleListDataItemType] = {
    "schedules",
}


def check_schedule_list_data_item_type(value: str | None) -> ScheduleListDataItemType | None:
    if value is None:
        return None
    if value in SCHEDULE_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(ScheduleListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SCHEDULE_LIST_DATA_ITEM_TYPE_VALUES!r}")
