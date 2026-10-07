from typing import Literal

UpdateAlertConfigurationDataType = Literal["alert_configurations"]

UPDATE_ALERT_CONFIGURATION_DATA_TYPE_VALUES: set[UpdateAlertConfigurationDataType] = {
    "alert_configurations",
}


def check_update_alert_configuration_data_type(value: str | None) -> UpdateAlertConfigurationDataType | None:
    if value is None:
        return None
    if value in UPDATE_ALERT_CONFIGURATION_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_CONFIGURATION_DATA_TYPE_VALUES!r}")
