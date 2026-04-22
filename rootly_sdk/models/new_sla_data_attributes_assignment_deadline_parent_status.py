from typing import Literal, cast

NewSlaDataAttributesAssignmentDeadlineParentStatus = Literal[
    "cancelled", "closed", "in_triage", "mitigated", "resolved", "started"
]

NEW_SLA_DATA_ATTRIBUTES_ASSIGNMENT_DEADLINE_PARENT_STATUS_VALUES: set[
    NewSlaDataAttributesAssignmentDeadlineParentStatus
] = {
    "cancelled",
    "closed",
    "in_triage",
    "mitigated",
    "resolved",
    "started",
}


def check_new_sla_data_attributes_assignment_deadline_parent_status(
    value: str | None,
) -> NewSlaDataAttributesAssignmentDeadlineParentStatus | None:
    if value is None:
        return None
    if value in NEW_SLA_DATA_ATTRIBUTES_ASSIGNMENT_DEADLINE_PARENT_STATUS_VALUES:
        return cast(NewSlaDataAttributesAssignmentDeadlineParentStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_SLA_DATA_ATTRIBUTES_ASSIGNMENT_DEADLINE_PARENT_STATUS_VALUES!r}"
    )
