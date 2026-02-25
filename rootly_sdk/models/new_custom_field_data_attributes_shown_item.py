from typing import Literal, cast

NewCustomFieldDataAttributesShownItem = Literal[
    "incident_form",
    "incident_mitigation_form",
    "incident_mitigation_slack_form",
    "incident_post_mortem",
    "incident_post_mortem_form",
    "incident_resolution_form",
    "incident_resolution_slack_form",
    "incident_slack_form",
]

NEW_CUSTOM_FIELD_DATA_ATTRIBUTES_SHOWN_ITEM_VALUES: set[NewCustomFieldDataAttributesShownItem] = {
    "incident_form",
    "incident_mitigation_form",
    "incident_mitigation_slack_form",
    "incident_post_mortem",
    "incident_post_mortem_form",
    "incident_resolution_form",
    "incident_resolution_slack_form",
    "incident_slack_form",
}


def check_new_custom_field_data_attributes_shown_item(
    value: str | None,
) -> NewCustomFieldDataAttributesShownItem | None:
    if value is None:
        return None
    if value in NEW_CUSTOM_FIELD_DATA_ATTRIBUTES_SHOWN_ITEM_VALUES:
        return cast(NewCustomFieldDataAttributesShownItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_CUSTOM_FIELD_DATA_ATTRIBUTES_SHOWN_ITEM_VALUES!r}"
    )
