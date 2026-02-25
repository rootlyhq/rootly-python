from typing import Literal, cast

UpdateOverrideShiftDataType = Literal["shifts"]

UPDATE_OVERRIDE_SHIFT_DATA_TYPE_VALUES: set[UpdateOverrideShiftDataType] = {
    "shifts",
}


def check_update_override_shift_data_type(value: str | None) -> UpdateOverrideShiftDataType | None:
    if value is None:
        return None
    if value in UPDATE_OVERRIDE_SHIFT_DATA_TYPE_VALUES:
        return cast(UpdateOverrideShiftDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_OVERRIDE_SHIFT_DATA_TYPE_VALUES!r}")
