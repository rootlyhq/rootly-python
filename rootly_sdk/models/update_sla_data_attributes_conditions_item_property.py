from typing import Literal, cast

UpdateSlaDataAttributesConditionsItemProperty = Literal[
    "acknowledged_at",
    "cause",
    "detected_at",
    "environment",
    "functionality",
    "group",
    "incident_role",
    "incident_type",
    "kind",
    "mitigated_at",
    "resolved_at",
    "service",
    "severity",
    "started_at",
    "status",
    "sub_status",
    "summary",
    "visibility",
]

UPDATE_SLA_DATA_ATTRIBUTES_CONDITIONS_ITEM_PROPERTY_VALUES: set[UpdateSlaDataAttributesConditionsItemProperty] = {
    "acknowledged_at",
    "cause",
    "detected_at",
    "environment",
    "functionality",
    "group",
    "incident_role",
    "incident_type",
    "kind",
    "mitigated_at",
    "resolved_at",
    "service",
    "severity",
    "started_at",
    "status",
    "sub_status",
    "summary",
    "visibility",
}


def check_update_sla_data_attributes_conditions_item_property(
    value: str | None,
) -> UpdateSlaDataAttributesConditionsItemProperty | None:
    if value is None:
        return None
    if value in UPDATE_SLA_DATA_ATTRIBUTES_CONDITIONS_ITEM_PROPERTY_VALUES:
        return cast(UpdateSlaDataAttributesConditionsItemProperty, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_SLA_DATA_ATTRIBUTES_CONDITIONS_ITEM_PROPERTY_VALUES!r}"
    )
