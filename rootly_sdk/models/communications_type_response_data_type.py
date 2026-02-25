from typing import Literal, cast

CommunicationsTypeResponseDataType = Literal["communications_types"]

COMMUNICATIONS_TYPE_RESPONSE_DATA_TYPE_VALUES: set[CommunicationsTypeResponseDataType] = {
    "communications_types",
}


def check_communications_type_response_data_type(value: str | None) -> CommunicationsTypeResponseDataType | None:
    if value is None:
        return None
    if value in COMMUNICATIONS_TYPE_RESPONSE_DATA_TYPE_VALUES:
        return cast(CommunicationsTypeResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMMUNICATIONS_TYPE_RESPONSE_DATA_TYPE_VALUES!r}")
