from typing import Literal, cast

AlertsSourceDeduplicationKeyKind = Literal["payload"]

ALERTS_SOURCE_DEDUPLICATION_KEY_KIND_VALUES: set[AlertsSourceDeduplicationKeyKind] = {
    "payload",
}


def check_alerts_source_deduplication_key_kind(value: str | None) -> AlertsSourceDeduplicationKeyKind | None:
    if value is None:
        return None
    if value in ALERTS_SOURCE_DEDUPLICATION_KEY_KIND_VALUES:
        return cast(AlertsSourceDeduplicationKeyKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERTS_SOURCE_DEDUPLICATION_KEY_KIND_VALUES!r}")
