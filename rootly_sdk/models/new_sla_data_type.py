from typing import Literal, cast

NewSlaDataType = Literal["slas"]

NEW_SLA_DATA_TYPE_VALUES: set[NewSlaDataType] = {
    "slas",
}


def check_new_sla_data_type(value: str | None) -> NewSlaDataType | None:
    if value is None:
        return None
    if value in NEW_SLA_DATA_TYPE_VALUES:
        return cast(NewSlaDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_SLA_DATA_TYPE_VALUES!r}")
