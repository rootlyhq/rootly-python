from typing import Literal, cast

SlaResponseDataType = Literal["slas"]

SLA_RESPONSE_DATA_TYPE_VALUES: set[SlaResponseDataType] = {
    "slas",
}


def check_sla_response_data_type(value: str | None) -> SlaResponseDataType | None:
    if value is None:
        return None
    if value in SLA_RESPONSE_DATA_TYPE_VALUES:
        return cast(SlaResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SLA_RESPONSE_DATA_TYPE_VALUES!r}")
