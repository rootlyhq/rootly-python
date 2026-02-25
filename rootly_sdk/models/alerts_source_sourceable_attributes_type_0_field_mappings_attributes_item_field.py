from typing import Literal, cast

AlertsSourceSourceableAttributesType0FieldMappingsAttributesItemField = Literal[
    "alert_description",
    "alert_external_url",
    "alert_title",
    "external_id",
    "notification_target_id",
    "notification_target_type",
    "state",
]

ALERTS_SOURCE_SOURCEABLE_ATTRIBUTES_TYPE_0_FIELD_MAPPINGS_ATTRIBUTES_ITEM_FIELD_VALUES: set[
    AlertsSourceSourceableAttributesType0FieldMappingsAttributesItemField
] = {
    "alert_description",
    "alert_external_url",
    "alert_title",
    "external_id",
    "notification_target_id",
    "notification_target_type",
    "state",
}


def check_alerts_source_sourceable_attributes_type_0_field_mappings_attributes_item_field(
    value: str | None,
) -> AlertsSourceSourceableAttributesType0FieldMappingsAttributesItemField | None:
    if value is None:
        return None
    if value in ALERTS_SOURCE_SOURCEABLE_ATTRIBUTES_TYPE_0_FIELD_MAPPINGS_ATTRIBUTES_ITEM_FIELD_VALUES:
        return cast(AlertsSourceSourceableAttributesType0FieldMappingsAttributesItemField, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERTS_SOURCE_SOURCEABLE_ATTRIBUTES_TYPE_0_FIELD_MAPPINGS_ATTRIBUTES_ITEM_FIELD_VALUES!r}"
    )
