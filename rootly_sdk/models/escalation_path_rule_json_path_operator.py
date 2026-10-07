from typing import Literal

EscalationPathRuleJsonPathOperator = Literal[
    "contains",
    "contains_key",
    "does_not_contain",
    "does_not_contain_key",
    "does_not_match",
    "does_not_start_with",
    "is",
    "is_not",
    "is_not_one_of",
    "is_not_set",
    "is_one_of",
    "is_set",
    "matches",
    "starts_with",
]

ESCALATION_PATH_RULE_JSON_PATH_OPERATOR_VALUES: set[EscalationPathRuleJsonPathOperator] = {
    "contains",
    "contains_key",
    "does_not_contain",
    "does_not_contain_key",
    "does_not_match",
    "does_not_start_with",
    "is",
    "is_not",
    "is_not_one_of",
    "is_not_set",
    "is_one_of",
    "is_set",
    "matches",
    "starts_with",
}


def check_escalation_path_rule_json_path_operator(value: str | None) -> EscalationPathRuleJsonPathOperator | None:
    if value is None:
        return None
    if value in ESCALATION_PATH_RULE_JSON_PATH_OPERATOR_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ESCALATION_PATH_RULE_JSON_PATH_OPERATOR_VALUES!r}")
