from typing import Literal, cast

NewAlertEventDataAttributesKind = Literal["note"]

NEW_ALERT_EVENT_DATA_ATTRIBUTES_KIND_VALUES: set[NewAlertEventDataAttributesKind] = {
    "note",
}


def check_new_alert_event_data_attributes_kind(value: str | None) -> NewAlertEventDataAttributesKind | None:
    if value is None:
        return None
    if value in NEW_ALERT_EVENT_DATA_ATTRIBUTES_KIND_VALUES:
        return cast(NewAlertEventDataAttributesKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_ALERT_EVENT_DATA_ATTRIBUTES_KIND_VALUES!r}")
