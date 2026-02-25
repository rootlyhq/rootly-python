from typing import Literal, cast

NewFormFieldDataAttributesKind = Literal[
    "acknowledged_at",
    "attach_alerts",
    "causes",
    "closed_at",
    "custom",
    "custom_sub_status",
    "detected_at",
    "environments",
    "functionalities",
    "in_triage_at",
    "labels",
    "manual_starting_datetime_field",
    "mark_as_backfilled",
    "mark_as_in_triage",
    "mark_as_test",
    "mitigated_at",
    "mitigation_message",
    "notify_emails",
    "resolution_message",
    "resolved_at",
    "services",
    "severity",
    "show_ongoing_incidents",
    "started_at",
    "summary",
    "teams",
    "title",
    "trigger_manual_workflows",
    "types",
    "visibility",
]

NEW_FORM_FIELD_DATA_ATTRIBUTES_KIND_VALUES: set[NewFormFieldDataAttributesKind] = {
    "acknowledged_at",
    "attach_alerts",
    "causes",
    "closed_at",
    "custom",
    "custom_sub_status",
    "detected_at",
    "environments",
    "functionalities",
    "in_triage_at",
    "labels",
    "manual_starting_datetime_field",
    "mark_as_backfilled",
    "mark_as_in_triage",
    "mark_as_test",
    "mitigated_at",
    "mitigation_message",
    "notify_emails",
    "resolution_message",
    "resolved_at",
    "services",
    "severity",
    "show_ongoing_incidents",
    "started_at",
    "summary",
    "teams",
    "title",
    "trigger_manual_workflows",
    "types",
    "visibility",
}


def check_new_form_field_data_attributes_kind(value: str | None) -> NewFormFieldDataAttributesKind | None:
    if value is None:
        return None
    if value in NEW_FORM_FIELD_DATA_ATTRIBUTES_KIND_VALUES:
        return cast(NewFormFieldDataAttributesKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_FORM_FIELD_DATA_ATTRIBUTES_KIND_VALUES!r}")
