from typing import Literal, cast

EscalationPathRuleJsonPathOperator = Literal[
    "contains", "does_not_contain", "is", "is_not", "is_not_one_of", "is_one_of"
]

ESCALATION_PATH_RULE_JSON_PATH_OPERATOR_VALUES: set[EscalationPathRuleJsonPathOperator] = {
    "contains",
    "does_not_contain",
    "is",
    "is_not",
    "is_not_one_of",
    "is_one_of",
}


def check_escalation_path_rule_json_path_operator(value: str | None) -> EscalationPathRuleJsonPathOperator | None:
    if value is None:
        return None
    if value in ESCALATION_PATH_RULE_JSON_PATH_OPERATOR_VALUES:
        return cast(EscalationPathRuleJsonPathOperator, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ESCALATION_PATH_RULE_JSON_PATH_OPERATOR_VALUES!r}")
