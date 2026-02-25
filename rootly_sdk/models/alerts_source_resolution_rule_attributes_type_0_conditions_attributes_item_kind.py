from typing import Literal, cast

AlertsSourceResolutionRuleAttributesType0ConditionsAttributesItemKind = Literal["alert_field", "payload"]

ALERTS_SOURCE_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITIONS_ATTRIBUTES_ITEM_KIND_VALUES: set[
    AlertsSourceResolutionRuleAttributesType0ConditionsAttributesItemKind
] = {
    "alert_field",
    "payload",
}


def check_alerts_source_resolution_rule_attributes_type_0_conditions_attributes_item_kind(
    value: str | None,
) -> AlertsSourceResolutionRuleAttributesType0ConditionsAttributesItemKind | None:
    if value is None:
        return None
    if value in ALERTS_SOURCE_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITIONS_ATTRIBUTES_ITEM_KIND_VALUES:
        return cast(AlertsSourceResolutionRuleAttributesType0ConditionsAttributesItemKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERTS_SOURCE_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITIONS_ATTRIBUTES_ITEM_KIND_VALUES!r}"
    )
