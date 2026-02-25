from typing import Literal, cast

UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0IdentifierMatchableType = Literal["AlertField"]

UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_IDENTIFIER_MATCHABLE_TYPE_VALUES: set[
    UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0IdentifierMatchableType
] = {
    "AlertField",
}


def check_update_alerts_source_data_attributes_resolution_rule_attributes_type_0_identifier_matchable_type(
    value: str | None,
) -> UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0IdentifierMatchableType | None:
    if value is None:
        return None
    if value in UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_IDENTIFIER_MATCHABLE_TYPE_VALUES:
        return cast(UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0IdentifierMatchableType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_IDENTIFIER_MATCHABLE_TYPE_VALUES!r}"
    )
