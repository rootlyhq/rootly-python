from typing import Literal, cast

EscalationPolicyPathAfterDeferralBehavior = Literal["execute_path", "re_evaluate"]

ESCALATION_POLICY_PATH_AFTER_DEFERRAL_BEHAVIOR_VALUES: set[EscalationPolicyPathAfterDeferralBehavior] = {
    "execute_path",
    "re_evaluate",
}


def check_escalation_policy_path_after_deferral_behavior(
    value: str | None,
) -> EscalationPolicyPathAfterDeferralBehavior | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_AFTER_DEFERRAL_BEHAVIOR_VALUES:
        return cast(EscalationPolicyPathAfterDeferralBehavior, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_AFTER_DEFERRAL_BEHAVIOR_VALUES!r}"
    )
