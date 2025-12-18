from typing import Literal, cast

PostMortemTriggerParamsIncidentKindsItem = Literal[
    "backfilled", "example", "example_sub", "normal", "normal_sub", "scheduled", "scheduled_sub", "test", "test_sub"
]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_KINDS_ITEM_VALUES: set[PostMortemTriggerParamsIncidentKindsItem] = {
    "backfilled",
    "example",
    "example_sub",
    "normal",
    "normal_sub",
    "scheduled",
    "scheduled_sub",
    "test",
    "test_sub",
}


def check_post_mortem_trigger_params_incident_kinds_item(value: str) -> PostMortemTriggerParamsIncidentKindsItem:
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_KINDS_ITEM_VALUES:
        return cast(PostMortemTriggerParamsIncidentKindsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_KINDS_ITEM_VALUES!r}"
    )
