from typing import Literal, cast

ActionItemTriggerParamsIncidentActionItemStatusesItem = Literal["cancelled", "done", "in_progress", "open"]

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_ACTION_ITEM_STATUSES_ITEM_VALUES: set[
    ActionItemTriggerParamsIncidentActionItemStatusesItem
] = {
    "cancelled",
    "done",
    "in_progress",
    "open",
}


def check_action_item_trigger_params_incident_action_item_statuses_item(
    value: str | None,
) -> ActionItemTriggerParamsIncidentActionItemStatusesItem | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_ACTION_ITEM_STATUSES_ITEM_VALUES:
        return cast(ActionItemTriggerParamsIncidentActionItemStatusesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_ACTION_ITEM_STATUSES_ITEM_VALUES!r}"
    )
