from typing import Literal, cast

FormFieldKind = Literal[
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

FORM_FIELD_KIND_VALUES: set[FormFieldKind] = {
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


def check_form_field_kind(value: str | None) -> FormFieldKind | None:
    if value is None:
        return None
    if value in FORM_FIELD_KIND_VALUES:
        return cast(FormFieldKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FORM_FIELD_KIND_VALUES!r}")
