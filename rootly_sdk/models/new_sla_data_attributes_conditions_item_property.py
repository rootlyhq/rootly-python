from typing import Literal, cast

NewSlaDataAttributesConditionsItemProperty = Literal[
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

NEW_SLA_DATA_ATTRIBUTES_CONDITIONS_ITEM_PROPERTY_VALUES: set[NewSlaDataAttributesConditionsItemProperty] = {
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


def check_new_sla_data_attributes_conditions_item_property(
    value: str | None,
) -> NewSlaDataAttributesConditionsItemProperty | None:
    if value is None:
        return None
    if value in NEW_SLA_DATA_ATTRIBUTES_CONDITIONS_ITEM_PROPERTY_VALUES:
        return cast(NewSlaDataAttributesConditionsItemProperty, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_SLA_DATA_ATTRIBUTES_CONDITIONS_ITEM_PROPERTY_VALUES!r}"
    )
