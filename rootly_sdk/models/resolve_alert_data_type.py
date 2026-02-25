from typing import Literal, cast

ResolveAlertDataType = Literal["alerts"]

RESOLVE_ALERT_DATA_TYPE_VALUES: set[ResolveAlertDataType] = {
    "alerts",
}


def check_resolve_alert_data_type(value: str | None) -> ResolveAlertDataType | None:
    if value is None:
        return None
    if value in RESOLVE_ALERT_DATA_TYPE_VALUES:
        return cast(ResolveAlertDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESOLVE_ALERT_DATA_TYPE_VALUES!r}")
