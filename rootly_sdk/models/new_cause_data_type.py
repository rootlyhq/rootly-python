from typing import Literal, cast

NewCauseDataType = Literal["causes"]

NEW_CAUSE_DATA_TYPE_VALUES: set[NewCauseDataType] = {
    "causes",
}


def check_new_cause_data_type(value: str | None) -> NewCauseDataType | None:
    if value is None:
        return None
    if value in NEW_CAUSE_DATA_TYPE_VALUES:
        return cast(NewCauseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_CAUSE_DATA_TYPE_VALUES!r}")
