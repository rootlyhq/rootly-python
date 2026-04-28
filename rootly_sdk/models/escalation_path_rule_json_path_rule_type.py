from typing import Literal, cast

EscalationPathRuleJsonPathRuleType = Literal["json_path"]

ESCALATION_PATH_RULE_JSON_PATH_RULE_TYPE_VALUES: set[EscalationPathRuleJsonPathRuleType] = {
    "json_path",
}


def check_escalation_path_rule_json_path_rule_type(value: str | None) -> EscalationPathRuleJsonPathRuleType | None:
    if value is None:
        return None
    if value in ESCALATION_PATH_RULE_JSON_PATH_RULE_TYPE_VALUES:
        return cast(EscalationPathRuleJsonPathRuleType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ESCALATION_PATH_RULE_JSON_PATH_RULE_TYPE_VALUES!r}")
