from typing import Literal, cast

AlertTriggerParamsTriggersItem = Literal["alert_created", "alert_status_updated"]

ALERT_TRIGGER_PARAMS_TRIGGERS_ITEM_VALUES: set[AlertTriggerParamsTriggersItem] = {
    "alert_created",
    "alert_status_updated",
}


def check_alert_trigger_params_triggers_item(value: str | None) -> AlertTriggerParamsTriggersItem | None:
    if value is None:
        return None
    if value in ALERT_TRIGGER_PARAMS_TRIGGERS_ITEM_VALUES:
        return cast(AlertTriggerParamsTriggersItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_TRIGGER_PARAMS_TRIGGERS_ITEM_VALUES!r}")
