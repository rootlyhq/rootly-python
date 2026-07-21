from typing import Literal, cast

EscalateAlertDataType = Literal["alerts"]

ESCALATE_ALERT_DATA_TYPE_VALUES: set[EscalateAlertDataType] = {
    "alerts",
}


def check_escalate_alert_data_type(value: str | None) -> EscalateAlertDataType | None:
    if value is None:
        return None
    if value in ESCALATE_ALERT_DATA_TYPE_VALUES:
        return cast(EscalateAlertDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ESCALATE_ALERT_DATA_TYPE_VALUES!r}")
