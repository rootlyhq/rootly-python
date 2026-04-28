from typing import Literal, cast

UpdateEscalationPolicyPathDataAttributesMatchMode = Literal["match-all-rules", "match-any-rule"]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_MATCH_MODE_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesMatchMode
] = {
    "match-all-rules",
    "match-any-rule",
}


def check_update_escalation_policy_path_data_attributes_match_mode(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesMatchMode | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_MATCH_MODE_VALUES:
        return cast(UpdateEscalationPolicyPathDataAttributesMatchMode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_MATCH_MODE_VALUES!r}"
    )
