from typing import Literal, cast

UpdateSlaDataAttributesCompletionDeadlineParentStatus = Literal[
    "cancelled", "closed", "in_triage", "mitigated", "resolved", "started"
]

UPDATE_SLA_DATA_ATTRIBUTES_COMPLETION_DEADLINE_PARENT_STATUS_VALUES: set[
    UpdateSlaDataAttributesCompletionDeadlineParentStatus
] = {
    "cancelled",
    "closed",
    "in_triage",
    "mitigated",
    "resolved",
    "started",
}


def check_update_sla_data_attributes_completion_deadline_parent_status(
    value: str | None,
) -> UpdateSlaDataAttributesCompletionDeadlineParentStatus | None:
    if value is None:
        return None
    if value in UPDATE_SLA_DATA_ATTRIBUTES_COMPLETION_DEADLINE_PARENT_STATUS_VALUES:
        return cast(UpdateSlaDataAttributesCompletionDeadlineParentStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_SLA_DATA_ATTRIBUTES_COMPLETION_DEADLINE_PARENT_STATUS_VALUES!r}"
    )
