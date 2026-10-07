from typing import Literal

UpdateCauseDataType = Literal["causes"]

UPDATE_CAUSE_DATA_TYPE_VALUES: set[UpdateCauseDataType] = {
    "causes",
}


def check_update_cause_data_type(value: str | None) -> UpdateCauseDataType | None:
    if value is None:
        return None
    if value in UPDATE_CAUSE_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_CAUSE_DATA_TYPE_VALUES!r}")
