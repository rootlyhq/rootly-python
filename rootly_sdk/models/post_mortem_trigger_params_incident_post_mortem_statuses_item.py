from typing import Literal, cast

PostMortemTriggerParamsIncidentPostMortemStatusesItem = Literal["draft", "published"]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_POST_MORTEM_STATUSES_ITEM_VALUES: set[
    PostMortemTriggerParamsIncidentPostMortemStatusesItem
] = {
    "draft",
    "published",
}


def check_post_mortem_trigger_params_incident_post_mortem_statuses_item(
    value: str | None,
) -> PostMortemTriggerParamsIncidentPostMortemStatusesItem | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_POST_MORTEM_STATUSES_ITEM_VALUES:
        return cast(PostMortemTriggerParamsIncidentPostMortemStatusesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_POST_MORTEM_STATUSES_ITEM_VALUES!r}"
    )
