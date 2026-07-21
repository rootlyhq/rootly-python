from typing import Literal, cast

AlertEventFeedListDataItemType = Literal["alert_events"]

ALERT_EVENT_FEED_LIST_DATA_ITEM_TYPE_VALUES: set[AlertEventFeedListDataItemType] = {
    "alert_events",
}


def check_alert_event_feed_list_data_item_type(value: str | None) -> AlertEventFeedListDataItemType | None:
    if value is None:
        return None
    if value in ALERT_EVENT_FEED_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(AlertEventFeedListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_EVENT_FEED_LIST_DATA_ITEM_TYPE_VALUES!r}")
