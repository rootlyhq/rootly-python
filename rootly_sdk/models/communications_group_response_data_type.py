from typing import Literal, cast

CommunicationsGroupResponseDataType = Literal["communications_groups"]

COMMUNICATIONS_GROUP_RESPONSE_DATA_TYPE_VALUES: set[CommunicationsGroupResponseDataType] = {
    "communications_groups",
}


def check_communications_group_response_data_type(value: str) -> CommunicationsGroupResponseDataType:
    if value in COMMUNICATIONS_GROUP_RESPONSE_DATA_TYPE_VALUES:
        return cast(CommunicationsGroupResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMMUNICATIONS_GROUP_RESPONSE_DATA_TYPE_VALUES!r}")
