from typing import Literal, cast

PostMortemTriggerParamsIncidentConditionAcknowledgedAtType1 = Literal["SET", "UNSET"]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_ACKNOWLEDGED_AT_TYPE_1_VALUES: set[
    PostMortemTriggerParamsIncidentConditionAcknowledgedAtType1
] = {
    "SET",
    "UNSET",
}


def check_post_mortem_trigger_params_incident_condition_acknowledged_at_type_1(
    value: str | None,
) -> PostMortemTriggerParamsIncidentConditionAcknowledgedAtType1 | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_ACKNOWLEDGED_AT_TYPE_1_VALUES:
        return cast(PostMortemTriggerParamsIncidentConditionAcknowledgedAtType1, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_ACKNOWLEDGED_AT_TYPE_1_VALUES!r}"
    )
