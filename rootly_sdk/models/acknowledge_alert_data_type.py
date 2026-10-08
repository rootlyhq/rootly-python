from typing import Literal

AcknowledgeAlertDataType = Literal["alerts"]

ACKNOWLEDGE_ALERT_DATA_TYPE_VALUES: set[AcknowledgeAlertDataType] = {
    "alerts",
}


def check_acknowledge_alert_data_type(value: str | None) -> AcknowledgeAlertDataType | None:
    if value is None:
        return None
    if value in ACKNOWLEDGE_ALERT_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACKNOWLEDGE_ALERT_DATA_TYPE_VALUES!r}")
