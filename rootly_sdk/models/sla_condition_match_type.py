from typing import Literal, cast

SlaConditionMatchType = Literal["ALL", "ANY"]

SLA_CONDITION_MATCH_TYPE_VALUES: set[SlaConditionMatchType] = {
    "ALL",
    "ANY",
}


def check_sla_condition_match_type(value: str | None) -> SlaConditionMatchType | None:
    if value is None:
        return None
    if value in SLA_CONDITION_MATCH_TYPE_VALUES:
        return cast(SlaConditionMatchType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SLA_CONDITION_MATCH_TYPE_VALUES!r}")
