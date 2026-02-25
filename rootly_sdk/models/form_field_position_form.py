from typing import Literal, cast

FormFieldPositionForm = Literal[
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

FORM_FIELD_POSITION_FORM_VALUES: set[FormFieldPositionForm] = {
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


def check_form_field_position_form(value: str | None) -> FormFieldPositionForm | None:
    if value is None:
        return None
    if value in FORM_FIELD_POSITION_FORM_VALUES:
        return cast(FormFieldPositionForm, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FORM_FIELD_POSITION_FORM_VALUES!r}")
