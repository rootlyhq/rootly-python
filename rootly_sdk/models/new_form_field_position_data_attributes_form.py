from typing import Literal, cast

NewFormFieldPositionDataAttributesForm = Literal[
    "incident_post_mortem",
    "slack_incident_cancellation_form",
    "slack_incident_mitigation_form",
    "slack_incident_resolution_form",
    "slack_new_incident_form",
    "slack_scheduled_incident_form",
    "slack_update_incident_form",
    "slack_update_incident_status_form",
    "slack_update_scheduled_incident_form",
    "web_incident_cancellation_form",
    "web_incident_mitigation_form",
    "web_incident_post_mortem_form",
    "web_incident_resolution_form",
    "web_new_incident_form",
    "web_scheduled_incident_form",
    "web_update_incident_form",
    "web_update_scheduled_incident_form",
]

NEW_FORM_FIELD_POSITION_DATA_ATTRIBUTES_FORM_VALUES: set[NewFormFieldPositionDataAttributesForm] = {
    "incident_post_mortem",
    "slack_incident_cancellation_form",
    "slack_incident_mitigation_form",
    "slack_incident_resolution_form",
    "slack_new_incident_form",
    "slack_scheduled_incident_form",
    "slack_update_incident_form",
    "slack_update_incident_status_form",
    "slack_update_scheduled_incident_form",
    "web_incident_cancellation_form",
    "web_incident_mitigation_form",
    "web_incident_post_mortem_form",
    "web_incident_resolution_form",
    "web_new_incident_form",
    "web_scheduled_incident_form",
    "web_update_incident_form",
    "web_update_scheduled_incident_form",
}


def check_new_form_field_position_data_attributes_form(
    value: str | None,
) -> NewFormFieldPositionDataAttributesForm | None:
    if value is None:
        return None
    if value in NEW_FORM_FIELD_POSITION_DATA_ATTRIBUTES_FORM_VALUES:
        return cast(NewFormFieldPositionDataAttributesForm, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_FORM_FIELD_POSITION_DATA_ATTRIBUTES_FORM_VALUES!r}"
    )
