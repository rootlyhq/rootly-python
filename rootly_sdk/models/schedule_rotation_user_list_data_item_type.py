from typing import Literal, cast

ScheduleRotationUserListDataItemType = Literal["schedule_rotation_users"]

SCHEDULE_ROTATION_USER_LIST_DATA_ITEM_TYPE_VALUES: set[ScheduleRotationUserListDataItemType] = {
    "schedule_rotation_users",
}


def check_schedule_rotation_user_list_data_item_type(value: str | None) -> ScheduleRotationUserListDataItemType | None:
    if value is None:
        return None
    if value in SCHEDULE_ROTATION_USER_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(ScheduleRotationUserListDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SCHEDULE_ROTATION_USER_LIST_DATA_ITEM_TYPE_VALUES!r}"
    )
