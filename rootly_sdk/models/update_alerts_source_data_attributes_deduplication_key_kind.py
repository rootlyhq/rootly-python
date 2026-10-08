from typing import Literal

UpdateAlertsSourceDataAttributesDeduplicationKeyKind = Literal["payload"]

UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_DEDUPLICATION_KEY_KIND_VALUES: set[
    UpdateAlertsSourceDataAttributesDeduplicationKeyKind
] = {
    "payload",
}


def check_update_alerts_source_data_attributes_deduplication_key_kind(
    value: str | None,
) -> UpdateAlertsSourceDataAttributesDeduplicationKeyKind | None:
    if value is None:
        return None
    if value in UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_DEDUPLICATION_KEY_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_DEDUPLICATION_KEY_KIND_VALUES!r}"
    )
