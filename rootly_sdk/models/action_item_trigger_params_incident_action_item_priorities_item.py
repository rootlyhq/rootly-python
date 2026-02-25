from typing import Literal, cast

ActionItemTriggerParamsIncidentActionItemPrioritiesItem = Literal["high", "low", "medium"]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_ACTION_ITEM_PRIORITIES_ITEM_VALUES: set[
    ActionItemTriggerParamsIncidentActionItemPrioritiesItem
] = {
    "high",
    "low",
    "medium",
}


def check_action_item_trigger_params_incident_action_item_priorities_item(
    value: str | None,
) -> ActionItemTriggerParamsIncidentActionItemPrioritiesItem | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_ACTION_ITEM_PRIORITIES_ITEM_VALUES:
        return cast(ActionItemTriggerParamsIncidentActionItemPrioritiesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_ACTION_ITEM_PRIORITIES_ITEM_VALUES!r}"
    )
