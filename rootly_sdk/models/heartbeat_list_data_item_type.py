from typing import Literal, cast

HeartbeatListDataItemType = Literal["heartbeats"]

HEARTBEAT_LIST_DATA_ITEM_TYPE_VALUES: set[HeartbeatListDataItemType] = {
    "heartbeats",
}


def check_heartbeat_list_data_item_type(value: str | None) -> HeartbeatListDataItemType | None:
    if value is None:
        return None
    if value in HEARTBEAT_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(HeartbeatListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HEARTBEAT_LIST_DATA_ITEM_TYPE_VALUES!r}")
