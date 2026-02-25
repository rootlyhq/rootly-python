from typing import Literal, cast

NewAlertsSourceDataAttributesResolutionRuleAttributesType0IdentifierMatchableType = Literal["AlertField"]

NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_IDENTIFIER_MATCHABLE_TYPE_VALUES: set[
    NewAlertsSourceDataAttributesResolutionRuleAttributesType0IdentifierMatchableType
] = {
    "AlertField",
}


def check_new_alerts_source_data_attributes_resolution_rule_attributes_type_0_identifier_matchable_type(
    value: str | None,
) -> NewAlertsSourceDataAttributesResolutionRuleAttributesType0IdentifierMatchableType | None:
    if value is None:
        return None
    if value in NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_IDENTIFIER_MATCHABLE_TYPE_VALUES:
        return cast(NewAlertsSourceDataAttributesResolutionRuleAttributesType0IdentifierMatchableType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_IDENTIFIER_MATCHABLE_TYPE_VALUES!r}"
    )
