from typing import Literal, cast

UpdateAlertsSourceDataType = Literal["alert_sources"]

UPDATE_ALERTS_SOURCE_DATA_TYPE_VALUES: set[UpdateAlertsSourceDataType] = {
    "alert_sources",
}


def check_update_alerts_source_data_type(value: str | None) -> UpdateAlertsSourceDataType | None:
    if value is None:
        return None
    if value in UPDATE_ALERTS_SOURCE_DATA_TYPE_VALUES:
        return cast(UpdateAlertsSourceDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_ALERTS_SOURCE_DATA_TYPE_VALUES!r}")
