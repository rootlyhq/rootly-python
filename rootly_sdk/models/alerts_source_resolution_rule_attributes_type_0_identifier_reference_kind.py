from typing import Literal, cast

AlertsSourceResolutionRuleAttributesType0IdentifierReferenceKind = Literal["alert_field", "payload"]

ALERTS_SOURCE_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_IDENTIFIER_REFERENCE_KIND_VALUES: set[
    AlertsSourceResolutionRuleAttributesType0IdentifierReferenceKind
] = {
    "alert_field",
    "payload",
}


def check_alerts_source_resolution_rule_attributes_type_0_identifier_reference_kind(
    value: str | None,
) -> AlertsSourceResolutionRuleAttributesType0IdentifierReferenceKind | None:
    if value is None:
        return None
    if value in ALERTS_SOURCE_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_IDENTIFIER_REFERENCE_KIND_VALUES:
        return cast(AlertsSourceResolutionRuleAttributesType0IdentifierReferenceKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERTS_SOURCE_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_IDENTIFIER_REFERENCE_KIND_VALUES!r}"
    )
