from typing import Literal, cast

NewAlertsSourceDataType = Literal["alert_sources"]

NEW_ALERTS_SOURCE_DATA_TYPE_VALUES: set[NewAlertsSourceDataType] = {
    "alert_sources",
}


def check_new_alerts_source_data_type(value: str | None) -> NewAlertsSourceDataType | None:
    if value is None:
        return None
    if value in NEW_ALERTS_SOURCE_DATA_TYPE_VALUES:
        return cast(NewAlertsSourceDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_ALERTS_SOURCE_DATA_TYPE_VALUES!r}")
