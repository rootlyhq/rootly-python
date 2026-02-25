from typing import Literal, cast

PulseResponseDataType = Literal["pulses"]

PULSE_RESPONSE_DATA_TYPE_VALUES: set[PulseResponseDataType] = {
    "pulses",
}


def check_pulse_response_data_type(value: str | None) -> PulseResponseDataType | None:
    if value is None:
        return None
    if value in PULSE_RESPONSE_DATA_TYPE_VALUES:
        return cast(PulseResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PULSE_RESPONSE_DATA_TYPE_VALUES!r}")
