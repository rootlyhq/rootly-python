from typing import Literal, cast

AlertsSourceResolutionRuleAttributesType0IdentifierMatchableType = Literal["AlertField"]

ALERTS_SOURCE_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_IDENTIFIER_MATCHABLE_TYPE_VALUES: set[
    AlertsSourceResolutionRuleAttributesType0IdentifierMatchableType
] = {
    "AlertField",
}


def check_alerts_source_resolution_rule_attributes_type_0_identifier_matchable_type(
    value: str | None,
) -> AlertsSourceResolutionRuleAttributesType0IdentifierMatchableType | None:
    if value is None:
        return None
    if value in ALERTS_SOURCE_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_IDENTIFIER_MATCHABLE_TYPE_VALUES:
        return cast(AlertsSourceResolutionRuleAttributesType0IdentifierMatchableType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERTS_SOURCE_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_IDENTIFIER_MATCHABLE_TYPE_VALUES!r}"
    )
