from typing import Literal, cast

NewSlaDataAttributesCompletionDeadlineParentStatus = Literal[
    "cancelled", "closed", "in_triage", "mitigated", "resolved", "started"
]

NEW_SLA_DATA_ATTRIBUTES_COMPLETION_DEADLINE_PARENT_STATUS_VALUES: set[
    NewSlaDataAttributesCompletionDeadlineParentStatus
] = {
    "cancelled",
    "closed",
    "in_triage",
    "mitigated",
    "resolved",
    "started",
}


def check_new_sla_data_attributes_completion_deadline_parent_status(
    value: str | None,
) -> NewSlaDataAttributesCompletionDeadlineParentStatus | None:
    if value is None:
        return None
    if value in NEW_SLA_DATA_ATTRIBUTES_COMPLETION_DEADLINE_PARENT_STATUS_VALUES:
        return cast(NewSlaDataAttributesCompletionDeadlineParentStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_SLA_DATA_ATTRIBUTES_COMPLETION_DEADLINE_PARENT_STATUS_VALUES!r}"
    )
