from typing import Literal

AlertConfigurationResponseDataType = Literal["alert_configurations"]

ALERT_CONFIGURATION_RESPONSE_DATA_TYPE_VALUES: set[AlertConfigurationResponseDataType] = {
    "alert_configurations",
}


def check_alert_configuration_response_data_type(value: str | None) -> AlertConfigurationResponseDataType | None:
    if value is None:
        return None
    if value in ALERT_CONFIGURATION_RESPONSE_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_CONFIGURATION_RESPONSE_DATA_TYPE_VALUES!r}")
