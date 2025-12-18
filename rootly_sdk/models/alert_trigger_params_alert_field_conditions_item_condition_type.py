from typing import Literal, cast

AlertTriggerParamsAlertFieldConditionsItemConditionType = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "NONE", "SET", "UNSET"
]

ALERT_TRIGGER_PARAMS_ALERT_FIELD_CONDITIONS_ITEM_CONDITION_TYPE_VALUES: set[
    AlertTriggerParamsAlertFieldConditionsItemConditionType
] = {
    "ANY",
    "CONTAINS",
    "CONTAINS_ALL",
    "CONTAINS_NONE",
    "IS",
    "NONE",
    "SET",
    "UNSET",
}


def check_alert_trigger_params_alert_field_conditions_item_condition_type(
    value: str,
) -> AlertTriggerParamsAlertFieldConditionsItemConditionType:
    if value in ALERT_TRIGGER_PARAMS_ALERT_FIELD_CONDITIONS_ITEM_CONDITION_TYPE_VALUES:
        return cast(AlertTriggerParamsAlertFieldConditionsItemConditionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_TRIGGER_PARAMS_ALERT_FIELD_CONDITIONS_ITEM_CONDITION_TYPE_VALUES!r}"
    )
