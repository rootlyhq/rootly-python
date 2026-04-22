from typing import Literal, cast

UpdateSlaDataType = Literal["slas"]

UPDATE_SLA_DATA_TYPE_VALUES: set[UpdateSlaDataType] = {
    "slas",
}


def check_update_sla_data_type(value: str | None) -> UpdateSlaDataType | None:
    if value is None:
        return None
    if value in UPDATE_SLA_DATA_TYPE_VALUES:
        return cast(UpdateSlaDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_SLA_DATA_TYPE_VALUES!r}")
