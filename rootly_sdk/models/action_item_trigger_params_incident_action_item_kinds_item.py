from typing import Literal, cast

ActionItemTriggerParamsIncidentActionItemKindsItem = Literal["follow_up", "task"]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_ACTION_ITEM_KINDS_ITEM_VALUES: set[
    ActionItemTriggerParamsIncidentActionItemKindsItem
] = {
    "follow_up",
    "task",
}


def check_action_item_trigger_params_incident_action_item_kinds_item(
    value: str | None,
) -> ActionItemTriggerParamsIncidentActionItemKindsItem | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_ACTION_ITEM_KINDS_ITEM_VALUES:
        return cast(ActionItemTriggerParamsIncidentActionItemKindsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_ACTION_ITEM_KINDS_ITEM_VALUES!r}"
    )
