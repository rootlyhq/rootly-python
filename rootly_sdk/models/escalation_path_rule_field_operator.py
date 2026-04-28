from typing import Literal, cast

EscalationPathRuleFieldOperator = Literal[
    "contains",
    "contains_key",
    "does_not_contain",
    "does_not_contain_key",
    "does_not_match",
    "does_not_start_with",
    "is",
    "is_empty",
    "is_not",
    "is_not_empty",
    "is_not_one_of",
    "is_one_of",
    "matches",
    "starts_with",
]

ESCALATION_PATH_RULE_FIELD_OPERATOR_VALUES: set[EscalationPathRuleFieldOperator] = {
    "contains",
    "contains_key",
    "does_not_contain",
    "does_not_contain_key",
    "does_not_match",
    "does_not_start_with",
    "is",
    "is_empty",
    "is_not",
    "is_not_empty",
    "is_not_one_of",
    "is_one_of",
    "matches",
    "starts_with",
}


def check_escalation_path_rule_field_operator(value: str | None) -> EscalationPathRuleFieldOperator | None:
    if value is None:
        return None
    if value in ESCALATION_PATH_RULE_FIELD_OPERATOR_VALUES:
        return cast(EscalationPathRuleFieldOperator, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ESCALATION_PATH_RULE_FIELD_OPERATOR_VALUES!r}")
