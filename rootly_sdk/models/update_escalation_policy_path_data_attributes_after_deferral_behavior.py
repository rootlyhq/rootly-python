from typing import Literal, cast

UpdateEscalationPolicyPathDataAttributesAfterDeferralBehavior = Literal["execute_path", "re_evaluate"]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_AFTER_DEFERRAL_BEHAVIOR_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesAfterDeferralBehavior
] = {
    "execute_path",
    "re_evaluate",
}


def check_update_escalation_policy_path_data_attributes_after_deferral_behavior(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesAfterDeferralBehavior | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_AFTER_DEFERRAL_BEHAVIOR_VALUES:
        return cast(UpdateEscalationPolicyPathDataAttributesAfterDeferralBehavior, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_AFTER_DEFERRAL_BEHAVIOR_VALUES!r}"
    )
