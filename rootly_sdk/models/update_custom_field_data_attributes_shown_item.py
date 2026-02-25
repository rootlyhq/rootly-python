from typing import Literal, cast

UpdateCustomFieldDataAttributesShownItem = Literal[
    "incident_form",
    "incident_mitigation_form",
    "incident_mitigation_slack_form",
    "incident_post_mortem",
    "incident_post_mortem_form",
    "incident_resolution_form",
    "incident_resolution_slack_form",
    "incident_slack_form",
]

UPDATE_CUSTOM_FIELD_DATA_ATTRIBUTES_SHOWN_ITEM_VALUES: set[UpdateCustomFieldDataAttributesShownItem] = {
    "incident_form",
    "incident_mitigation_form",
    "incident_mitigation_slack_form",
    "incident_post_mortem",
    "incident_post_mortem_form",
    "incident_resolution_form",
    "incident_resolution_slack_form",
    "incident_slack_form",
}


def check_update_custom_field_data_attributes_shown_item(
    value: str | None,
) -> UpdateCustomFieldDataAttributesShownItem | None:
    if value is None:
        return None
    if value in UPDATE_CUSTOM_FIELD_DATA_ATTRIBUTES_SHOWN_ITEM_VALUES:
        return cast(UpdateCustomFieldDataAttributesShownItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_CUSTOM_FIELD_DATA_ATTRIBUTES_SHOWN_ITEM_VALUES!r}"
    )
