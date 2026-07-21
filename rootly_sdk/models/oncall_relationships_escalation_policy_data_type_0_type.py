from typing import Literal, cast

OncallRelationshipsEscalationPolicyDataType0Type = Literal["escalation_policies"]

ONCALL_RELATIONSHIPS_ESCALATION_POLICY_DATA_TYPE_0_TYPE_VALUES: set[
    OncallRelationshipsEscalationPolicyDataType0Type
] = {
    "escalation_policies",
}


def check_oncall_relationships_escalation_policy_data_type_0_type(
    value: str | None,
) -> OncallRelationshipsEscalationPolicyDataType0Type | None:
    if value is None:
        return None
    if value in ONCALL_RELATIONSHIPS_ESCALATION_POLICY_DATA_TYPE_0_TYPE_VALUES:
        return cast(OncallRelationshipsEscalationPolicyDataType0Type, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ONCALL_RELATIONSHIPS_ESCALATION_POLICY_DATA_TYPE_0_TYPE_VALUES!r}"
    )
