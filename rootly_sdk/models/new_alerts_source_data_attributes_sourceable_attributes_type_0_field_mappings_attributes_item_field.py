from typing import Literal, cast

NewAlertsSourceDataAttributesSourceableAttributesType0FieldMappingsAttributesItemField = Literal[
    "alert_description",
    "alert_external_url",
    "alert_title",
    "external_id",
    "notification_target_id",
    "notification_target_type",
    "state",
]

NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_SOURCEABLE_ATTRIBUTES_TYPE_0_FIELD_MAPPINGS_ATTRIBUTES_ITEM_FIELD_VALUES: set[
    NewAlertsSourceDataAttributesSourceableAttributesType0FieldMappingsAttributesItemField
] = {
    "alert_description",
    "alert_external_url",
    "alert_title",
    "external_id",
    "notification_target_id",
    "notification_target_type",
    "state",
}


def check_new_alerts_source_data_attributes_sourceable_attributes_type_0_field_mappings_attributes_item_field(
    value: str,
) -> NewAlertsSourceDataAttributesSourceableAttributesType0FieldMappingsAttributesItemField:
    if (
        value
        in NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_SOURCEABLE_ATTRIBUTES_TYPE_0_FIELD_MAPPINGS_ATTRIBUTES_ITEM_FIELD_VALUES
    ):
        return cast(NewAlertsSourceDataAttributesSourceableAttributesType0FieldMappingsAttributesItemField, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_SOURCEABLE_ATTRIBUTES_TYPE_0_FIELD_MAPPINGS_ATTRIBUTES_ITEM_FIELD_VALUES!r}"
    )
