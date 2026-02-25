from typing import Literal, cast

ScheduleRotationActiveDayListDataItemType = Literal["schedule_rotation_active_days"]

SCHEDULE_ROTATION_ACTIVE_DAY_LIST_DATA_ITEM_TYPE_VALUES: set[ScheduleRotationActiveDayListDataItemType] = {
    "schedule_rotation_active_days",
}


def check_schedule_rotation_active_day_list_data_item_type(value: str | None) -> ScheduleRotationActiveDayListDataItemType | None:
    if value is None:
        return None
    if value in SCHEDULE_ROTATION_ACTIVE_DAY_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(ScheduleRotationActiveDayListDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SCHEDULE_ROTATION_ACTIVE_DAY_LIST_DATA_ITEM_TYPE_VALUES!r}"
    )
