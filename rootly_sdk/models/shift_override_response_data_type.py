from typing import Literal, cast

ShiftOverrideResponseDataType = Literal["shift_override"]

SHIFT_OVERRIDE_RESPONSE_DATA_TYPE_VALUES: set[ShiftOverrideResponseDataType] = {
    "shift_override",
}


def check_shift_override_response_data_type(value: str | None) -> ShiftOverrideResponseDataType | None:
    if value is None:
        return None
    if value in SHIFT_OVERRIDE_RESPONSE_DATA_TYPE_VALUES:
        return cast(ShiftOverrideResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SHIFT_OVERRIDE_RESPONSE_DATA_TYPE_VALUES!r}")
