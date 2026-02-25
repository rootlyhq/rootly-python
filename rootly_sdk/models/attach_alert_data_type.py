from typing import Literal, cast

AttachAlertDataType = Literal["alerts"]

ATTACH_ALERT_DATA_TYPE_VALUES: set[AttachAlertDataType] = {
    "alerts",
}


def check_attach_alert_data_type(value: str | None) -> AttachAlertDataType | None:
    if value is None:
        return None
    if value in ATTACH_ALERT_DATA_TYPE_VALUES:
        return cast(AttachAlertDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ATTACH_ALERT_DATA_TYPE_VALUES!r}")
