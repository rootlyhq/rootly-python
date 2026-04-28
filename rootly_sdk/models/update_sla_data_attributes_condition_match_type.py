from typing import Literal, cast

UpdateSlaDataAttributesConditionMatchType = Literal["ALL", "ANY"]

UPDATE_SLA_DATA_ATTRIBUTES_CONDITION_MATCH_TYPE_VALUES: set[UpdateSlaDataAttributesConditionMatchType] = {
    "ALL",
    "ANY",
}


def check_update_sla_data_attributes_condition_match_type(
    value: str | None,
) -> UpdateSlaDataAttributesConditionMatchType | None:
    if value is None:
        return None
    if value in UPDATE_SLA_DATA_ATTRIBUTES_CONDITION_MATCH_TYPE_VALUES:
        return cast(UpdateSlaDataAttributesConditionMatchType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_SLA_DATA_ATTRIBUTES_CONDITION_MATCH_TYPE_VALUES!r}"
    )
