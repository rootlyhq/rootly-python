from typing import Literal, cast

EscalationPathRuleFieldRuleType = Literal["field"]

ESCALATION_PATH_RULE_FIELD_RULE_TYPE_VALUES: set[EscalationPathRuleFieldRuleType] = {
    "field",
}


def check_escalation_path_rule_field_rule_type(value: str | None) -> EscalationPathRuleFieldRuleType | None:
    if value is None:
        return None
    if value in ESCALATION_PATH_RULE_FIELD_RULE_TYPE_VALUES:
        return cast(EscalationPathRuleFieldRuleType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ESCALATION_PATH_RULE_FIELD_RULE_TYPE_VALUES!r}")
