from typing import Literal, cast

CommunicationsGroupsResponseDataItemType = Literal["communications_groups"]

COMMUNICATIONS_GROUPS_RESPONSE_DATA_ITEM_TYPE_VALUES: set[CommunicationsGroupsResponseDataItemType] = {
    "communications_groups",
}


def check_communications_groups_response_data_item_type(
    value: str | None,
) -> CommunicationsGroupsResponseDataItemType | None:
    if value is None:
        return None
    if value in COMMUNICATIONS_GROUPS_RESPONSE_DATA_ITEM_TYPE_VALUES:
        return cast(CommunicationsGroupsResponseDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMMUNICATIONS_GROUPS_RESPONSE_DATA_ITEM_TYPE_VALUES!r}"
    )
