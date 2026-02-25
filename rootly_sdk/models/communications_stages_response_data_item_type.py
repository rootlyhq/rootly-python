from typing import Literal, cast

CommunicationsStagesResponseDataItemType = Literal["communications_stages"]

COMMUNICATIONS_STAGES_RESPONSE_DATA_ITEM_TYPE_VALUES: set[CommunicationsStagesResponseDataItemType] = {
    "communications_stages",
}


def check_communications_stages_response_data_item_type(value: str | None) -> CommunicationsStagesResponseDataItemType | None:
    if value is None:
        return None
    if value in COMMUNICATIONS_STAGES_RESPONSE_DATA_ITEM_TYPE_VALUES:
        return cast(CommunicationsStagesResponseDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMMUNICATIONS_STAGES_RESPONSE_DATA_ITEM_TYPE_VALUES!r}"
    )
