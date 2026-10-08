from typing import Literal

OverrideShiftResponseDataType = Literal["shifts"]

OVERRIDE_SHIFT_RESPONSE_DATA_TYPE_VALUES: set[OverrideShiftResponseDataType] = {
    "shifts",
}


def check_override_shift_response_data_type(value: str | None) -> OverrideShiftResponseDataType | None:
    if value is None:
        return None
    if value in OVERRIDE_SHIFT_RESPONSE_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OVERRIDE_SHIFT_RESPONSE_DATA_TYPE_VALUES!r}")
