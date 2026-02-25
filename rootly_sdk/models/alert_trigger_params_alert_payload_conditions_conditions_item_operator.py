from typing import Literal, cast

AlertTriggerParamsAlertPayloadConditionsConditionsItemOperator = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

ALERT_TRIGGER_PARAMS_ALERT_PAYLOAD_CONDITIONS_CONDITIONS_ITEM_OPERATOR_VALUES: set[
    AlertTriggerParamsAlertPayloadConditionsConditionsItemOperator
] = {
    "ANY",
    "CONTAINS",
    "CONTAINS_ALL",
    "CONTAINS_NONE",
    "IS",
    "IS NOT",
    "NONE",
    "SET",
    "UNSET",
}


def check_alert_trigger_params_alert_payload_conditions_conditions_item_operator(
    value: str | None,
) -> AlertTriggerParamsAlertPayloadConditionsConditionsItemOperator | None:
    if value is None:
        return None
    if value in ALERT_TRIGGER_PARAMS_ALERT_PAYLOAD_CONDITIONS_CONDITIONS_ITEM_OPERATOR_VALUES:
        return cast(AlertTriggerParamsAlertPayloadConditionsConditionsItemOperator, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_TRIGGER_PARAMS_ALERT_PAYLOAD_CONDITIONS_CONDITIONS_ITEM_OPERATOR_VALUES!r}"
    )
