from typing import Literal, cast

NewAlertsSourceDataAttributesResolutionRuleAttributesType0IdentifierReferenceKind = Literal["alert_field", "payload"]

NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_IDENTIFIER_REFERENCE_KIND_VALUES: set[
    NewAlertsSourceDataAttributesResolutionRuleAttributesType0IdentifierReferenceKind
] = {
    "alert_field",
    "payload",
}


def check_new_alerts_source_data_attributes_resolution_rule_attributes_type_0_identifier_reference_kind(
    value: str | None,
) -> NewAlertsSourceDataAttributesResolutionRuleAttributesType0IdentifierReferenceKind | None:
    if value is None:
        return None
    if value in NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_IDENTIFIER_REFERENCE_KIND_VALUES:
        return cast(NewAlertsSourceDataAttributesResolutionRuleAttributesType0IdentifierReferenceKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_IDENTIFIER_REFERENCE_KIND_VALUES!r}"
    )
