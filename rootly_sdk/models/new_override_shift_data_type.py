from typing import Literal

NewOverrideShiftDataType = Literal["shifts"]

NEW_OVERRIDE_SHIFT_DATA_TYPE_VALUES: set[NewOverrideShiftDataType] = {
    "shifts",
}


def check_new_override_shift_data_type(value: str | None) -> NewOverrideShiftDataType | None:
    if value is None:
        return None
    if value in NEW_OVERRIDE_SHIFT_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_OVERRIDE_SHIFT_DATA_TYPE_VALUES!r}")
