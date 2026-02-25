from typing import Literal, cast

UpdateScheduleRotationDataAttributesActiveDaysItem = Literal["F", "M", "R", "S", "T", "U", "W"]

UPDATE_SCHEDULE_ROTATION_DATA_ATTRIBUTES_ACTIVE_DAYS_ITEM_VALUES: set[
    UpdateScheduleRotationDataAttributesActiveDaysItem
] = {
    "F",
    "M",
    "R",
    "S",
    "T",
    "U",
    "W",
}


def check_update_schedule_rotation_data_attributes_active_days_item(
    value: str | None,
) -> UpdateScheduleRotationDataAttributesActiveDaysItem | None:
    if value is None:
        return None
    if value in UPDATE_SCHEDULE_ROTATION_DATA_ATTRIBUTES_ACTIVE_DAYS_ITEM_VALUES:
        return cast(UpdateScheduleRotationDataAttributesActiveDaysItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_SCHEDULE_ROTATION_DATA_ATTRIBUTES_ACTIVE_DAYS_ITEM_VALUES!r}"
    )
