from typing import Literal, cast

UpdateFormFieldPositionDataAttributesForm = Literal[
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

UPDATE_FORM_FIELD_POSITION_DATA_ATTRIBUTES_FORM_VALUES: set[UpdateFormFieldPositionDataAttributesForm] = {
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


def check_update_form_field_position_data_attributes_form(value: str | None) -> UpdateFormFieldPositionDataAttributesForm | None:
    if value is None:
        return None
    if value in UPDATE_FORM_FIELD_POSITION_DATA_ATTRIBUTES_FORM_VALUES:
        return cast(UpdateFormFieldPositionDataAttributesForm, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_FORM_FIELD_POSITION_DATA_ATTRIBUTES_FORM_VALUES!r}"
    )
