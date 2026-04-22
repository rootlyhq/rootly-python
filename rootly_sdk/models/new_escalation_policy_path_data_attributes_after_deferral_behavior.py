from typing import Literal, cast

NewEscalationPolicyPathDataAttributesAfterDeferralBehavior = Literal["execute_path", "re_evaluate"]

NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_AFTER_DEFERRAL_BEHAVIOR_VALUES: set[
    NewEscalationPolicyPathDataAttributesAfterDeferralBehavior
] = {
    "execute_path",
    "re_evaluate",
}


def check_new_escalation_policy_path_data_attributes_after_deferral_behavior(
    value: str | None,
) -> NewEscalationPolicyPathDataAttributesAfterDeferralBehavior | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_AFTER_DEFERRAL_BEHAVIOR_VALUES:
        return cast(NewEscalationPolicyPathDataAttributesAfterDeferralBehavior, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_AFTER_DEFERRAL_BEHAVIOR_VALUES!r}"
    )
