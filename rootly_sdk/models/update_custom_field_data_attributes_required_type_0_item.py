from typing import Literal, cast

UpdateCustomFieldDataAttributesRequiredType0Item = Literal[
    "incident_form",
    "incident_mitigation_form",
    "incident_mitigation_slack_form",
    "incident_post_mortem_form",
    "incident_resolution_form",
    "incident_resolution_slack_form",
    "incident_slack_form",
]

UPDATE_CUSTOM_FIELD_DATA_ATTRIBUTES_REQUIRED_TYPE_0_ITEM_VALUES: set[
    UpdateCustomFieldDataAttributesRequiredType0Item
] = {
    "incident_form",
    "incident_mitigation_form",
    "incident_mitigation_slack_form",
    "incident_post_mortem_form",
    "incident_resolution_form",
    "incident_resolution_slack_form",
    "incident_slack_form",
}


def check_update_custom_field_data_attributes_required_type_0_item(
    value: str | None,
) -> UpdateCustomFieldDataAttributesRequiredType0Item | None:
    if value is None:
        return None
    if value in UPDATE_CUSTOM_FIELD_DATA_ATTRIBUTES_REQUIRED_TYPE_0_ITEM_VALUES:
        return cast(UpdateCustomFieldDataAttributesRequiredType0Item, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_CUSTOM_FIELD_DATA_ATTRIBUTES_REQUIRED_TYPE_0_ITEM_VALUES!r}"
    )
