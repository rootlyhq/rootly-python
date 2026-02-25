from typing import Literal, cast

PostMortemTriggerParamsIncidentStatusesItem = Literal[
    "acknowledged",
    "cancelled",
    "closed",
    "completed",
    "detected",
    "in_progress",
    "in_triage",
    "mitigated",
    "resolved",
    "scheduled",
    "started",
]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_STATUSES_ITEM_VALUES: set[PostMortemTriggerParamsIncidentStatusesItem] = {
    "acknowledged",
    "cancelled",
    "closed",
    "completed",
    "detected",
    "in_progress",
    "in_triage",
    "mitigated",
    "resolved",
    "scheduled",
    "started",
}


def check_post_mortem_trigger_params_incident_statuses_item(value: str | None) -> PostMortemTriggerParamsIncidentStatusesItem | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_STATUSES_ITEM_VALUES:
        return cast(PostMortemTriggerParamsIncidentStatusesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_STATUSES_ITEM_VALUES!r}"
    )
