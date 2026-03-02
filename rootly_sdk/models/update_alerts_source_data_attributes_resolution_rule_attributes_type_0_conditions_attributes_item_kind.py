from typing import Literal, cast

UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemKind = Literal[
    "alert_field", "payload"
]

UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITIONS_ATTRIBUTES_ITEM_KIND_VALUES: set[
    UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemKind
] = {
    "alert_field",
    "payload",
}


def check_update_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item_kind(
    value: str | None,
) -> UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemKind | None:
    if value is None:
        return None
    if (
        value
        in UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITIONS_ATTRIBUTES_ITEM_KIND_VALUES
    ):
        return cast(UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITIONS_ATTRIBUTES_ITEM_KIND_VALUES!r}"
    )
