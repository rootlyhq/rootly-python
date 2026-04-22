from typing import Literal, cast

NewSlaDataAttributesConditionMatchType = Literal["ALL", "ANY"]

NEW_SLA_DATA_ATTRIBUTES_CONDITION_MATCH_TYPE_VALUES: set[NewSlaDataAttributesConditionMatchType] = {
    "ALL",
    "ANY",
}


def check_new_sla_data_attributes_condition_match_type(
    value: str | None,
) -> NewSlaDataAttributesConditionMatchType | None:
    if value is None:
        return None
    if value in NEW_SLA_DATA_ATTRIBUTES_CONDITION_MATCH_TYPE_VALUES:
        return cast(NewSlaDataAttributesConditionMatchType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_SLA_DATA_ATTRIBUTES_CONDITION_MATCH_TYPE_VALUES!r}"
    )
