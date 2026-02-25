from typing import Literal, cast

NewCustomFieldDataAttributesRequiredType0Item = Literal[
    "incident_form",
    "incident_mitigation_form",
    "incident_mitigation_slack_form",
    "incident_post_mortem_form",
    "incident_resolution_form",
    "incident_resolution_slack_form",
    "incident_slack_form",
]

NEW_CUSTOM_FIELD_DATA_ATTRIBUTES_REQUIRED_TYPE_0_ITEM_VALUES: set[NewCustomFieldDataAttributesRequiredType0Item] = {
    "incident_form",
    "incident_mitigation_form",
    "incident_mitigation_slack_form",
    "incident_post_mortem_form",
    "incident_resolution_form",
    "incident_resolution_slack_form",
    "incident_slack_form",
}


def check_new_custom_field_data_attributes_required_type_0_item(
    value: str | None,
) -> NewCustomFieldDataAttributesRequiredType0Item | None:
    if value is None:
        return None
    if value in NEW_CUSTOM_FIELD_DATA_ATTRIBUTES_REQUIRED_TYPE_0_ITEM_VALUES:
        return cast(NewCustomFieldDataAttributesRequiredType0Item, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_CUSTOM_FIELD_DATA_ATTRIBUTES_REQUIRED_TYPE_0_ITEM_VALUES!r}"
    )
