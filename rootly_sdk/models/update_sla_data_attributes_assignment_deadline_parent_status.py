from typing import Literal, cast

UpdateSlaDataAttributesAssignmentDeadlineParentStatus = Literal[
    "cancelled", "closed", "in_triage", "mitigated", "resolved", "started"
]

UPDATE_SLA_DATA_ATTRIBUTES_ASSIGNMENT_DEADLINE_PARENT_STATUS_VALUES: set[
    UpdateSlaDataAttributesAssignmentDeadlineParentStatus
] = {
    "cancelled",
    "closed",
    "in_triage",
    "mitigated",
    "resolved",
    "started",
}


def check_update_sla_data_attributes_assignment_deadline_parent_status(
    value: str | None,
) -> UpdateSlaDataAttributesAssignmentDeadlineParentStatus | None:
    if value is None:
        return None
    if value in UPDATE_SLA_DATA_ATTRIBUTES_ASSIGNMENT_DEADLINE_PARENT_STATUS_VALUES:
        return cast(UpdateSlaDataAttributesAssignmentDeadlineParentStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_SLA_DATA_ATTRIBUTES_ASSIGNMENT_DEADLINE_PARENT_STATUS_VALUES!r}"
    )
