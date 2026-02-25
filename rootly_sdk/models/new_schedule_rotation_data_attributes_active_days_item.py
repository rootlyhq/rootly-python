from typing import Literal, cast

NewScheduleRotationDataAttributesActiveDaysItem = Literal["F", "M", "R", "S", "T", "U", "W"]

NEW_SCHEDULE_ROTATION_DATA_ATTRIBUTES_ACTIVE_DAYS_ITEM_VALUES: set[NewScheduleRotationDataAttributesActiveDaysItem] = {
    "F",
    "M",
    "R",
    "S",
    "T",
    "U",
    "W",
}


def check_new_schedule_rotation_data_attributes_active_days_item(
    value: str | None,
) -> NewScheduleRotationDataAttributesActiveDaysItem | None:
    if value is None:
        return None
    if value in NEW_SCHEDULE_ROTATION_DATA_ATTRIBUTES_ACTIVE_DAYS_ITEM_VALUES:
        return cast(NewScheduleRotationDataAttributesActiveDaysItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_SCHEDULE_ROTATION_DATA_ATTRIBUTES_ACTIVE_DAYS_ITEM_VALUES!r}"
    )
