from typing import Literal, cast

UpdateAlertsSourceDataAttributesSourceableAttributesType0FieldMappingsAttributesItemField = Literal[
    "alert_description",
    "alert_external_url",
    "alert_title",
    "external_id",
    "notification_target_id",
    "notification_target_type",
    "state",
]

UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_SOURCEABLE_ATTRIBUTES_TYPE_0_FIELD_MAPPINGS_ATTRIBUTES_ITEM_FIELD_VALUES: set[
    UpdateAlertsSourceDataAttributesSourceableAttributesType0FieldMappingsAttributesItemField
] = {
    "alert_description",
    "alert_external_url",
    "alert_title",
    "external_id",
    "notification_target_id",
    "notification_target_type",
    "state",
}


def check_update_alerts_source_data_attributes_sourceable_attributes_type_0_field_mappings_attributes_item_field(
    value: str,
) -> UpdateAlertsSourceDataAttributesSourceableAttributesType0FieldMappingsAttributesItemField:
    if (
        value
        in UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_SOURCEABLE_ATTRIBUTES_TYPE_0_FIELD_MAPPINGS_ATTRIBUTES_ITEM_FIELD_VALUES
    ):
        return cast(UpdateAlertsSourceDataAttributesSourceableAttributesType0FieldMappingsAttributesItemField, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_SOURCEABLE_ATTRIBUTES_TYPE_0_FIELD_MAPPINGS_ATTRIBUTES_ITEM_FIELD_VALUES!r}"
    )
