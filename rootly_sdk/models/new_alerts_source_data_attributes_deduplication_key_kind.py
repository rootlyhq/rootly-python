from typing import Literal

NewAlertsSourceDataAttributesDeduplicationKeyKind = Literal["payload"]

NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_DEDUPLICATION_KEY_KIND_VALUES: set[
    NewAlertsSourceDataAttributesDeduplicationKeyKind
] = {
    "payload",
}


def check_new_alerts_source_data_attributes_deduplication_key_kind(
    value: str | None,
) -> NewAlertsSourceDataAttributesDeduplicationKeyKind | None:
    if value is None:
        return None
    if value in NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_DEDUPLICATION_KEY_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_DEDUPLICATION_KEY_KIND_VALUES!r}"
    )
