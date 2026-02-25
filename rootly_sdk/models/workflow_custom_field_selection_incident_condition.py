from typing import Literal, cast

WorkflowCustomFieldSelectionIncidentCondition = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

WORKFLOW_CUSTOM_FIELD_SELECTION_INCIDENT_CONDITION_VALUES: set[WorkflowCustomFieldSelectionIncidentCondition] = {
    "ANY",
    "CONTAINS",
    "CONTAINS_ALL",
    "CONTAINS_NONE",
    "IS",
    "IS NOT",
    "NONE",
    "SET",
    "UNSET",
}


def check_workflow_custom_field_selection_incident_condition(
    value: str | None,
) -> WorkflowCustomFieldSelectionIncidentCondition | None:
    if value is None:
        return None
    if value in WORKFLOW_CUSTOM_FIELD_SELECTION_INCIDENT_CONDITION_VALUES:
        return cast(WorkflowCustomFieldSelectionIncidentCondition, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WORKFLOW_CUSTOM_FIELD_SELECTION_INCIDENT_CONDITION_VALUES!r}"
    )
