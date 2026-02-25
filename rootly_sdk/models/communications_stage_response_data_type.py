from typing import Literal, cast

CommunicationsStageResponseDataType = Literal["communications_stages"]

COMMUNICATIONS_STAGE_RESPONSE_DATA_TYPE_VALUES: set[CommunicationsStageResponseDataType] = {
    "communications_stages",
}


def check_communications_stage_response_data_type(value: str | None) -> CommunicationsStageResponseDataType | None:
    if value is None:
        return None
    if value in COMMUNICATIONS_STAGE_RESPONSE_DATA_TYPE_VALUES:
        return cast(CommunicationsStageResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMMUNICATIONS_STAGE_RESPONSE_DATA_TYPE_VALUES!r}")
