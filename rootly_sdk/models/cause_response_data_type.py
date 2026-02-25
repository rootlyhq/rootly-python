from typing import Literal, cast

CauseResponseDataType = Literal["causes"]

CAUSE_RESPONSE_DATA_TYPE_VALUES: set[CauseResponseDataType] = {
    "causes",
}


def check_cause_response_data_type(value: str | None) -> CauseResponseDataType | None:
    if value is None:
        return None
    if value in CAUSE_RESPONSE_DATA_TYPE_VALUES:
        return cast(CauseResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CAUSE_RESPONSE_DATA_TYPE_VALUES!r}")
