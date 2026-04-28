from typing import Literal, cast

NewEscalationPolicyPathDataAttributesMatchMode = Literal["match-all-rules", "match-any-rule"]

NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_MATCH_MODE_VALUES: set[NewEscalationPolicyPathDataAttributesMatchMode] = {
    "match-all-rules",
    "match-any-rule",
}


def check_new_escalation_policy_path_data_attributes_match_mode(
    value: str | None,
) -> NewEscalationPolicyPathDataAttributesMatchMode | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_MATCH_MODE_VALUES:
        return cast(NewEscalationPolicyPathDataAttributesMatchMode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_MATCH_MODE_VALUES!r}"
    )
