from typing import Literal, cast

NewPulseDataType = Literal["pulses"]

NEW_PULSE_DATA_TYPE_VALUES: set[NewPulseDataType] = {
    "pulses",
}


def check_new_pulse_data_type(value: str | None) -> NewPulseDataType | None:
    if value is None:
        return None
    if value in NEW_PULSE_DATA_TYPE_VALUES:
        return cast(NewPulseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_PULSE_DATA_TYPE_VALUES!r}")
