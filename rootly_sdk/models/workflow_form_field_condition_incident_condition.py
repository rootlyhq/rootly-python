from typing import Literal, cast

WorkflowFormFieldConditionIncidentCondition = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

WORKFLOW_FORM_FIELD_CONDITION_INCIDENT_CONDITION_VALUES: set[WorkflowFormFieldConditionIncidentCondition] = {
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


def check_workflow_form_field_condition_incident_condition(
    value: str | None,
) -> WorkflowFormFieldConditionIncidentCondition | None:
    if value is None:
        return None
    if value in WORKFLOW_FORM_FIELD_CONDITION_INCIDENT_CONDITION_VALUES:
        return cast(WorkflowFormFieldConditionIncidentCondition, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WORKFLOW_FORM_FIELD_CONDITION_INCIDENT_CONDITION_VALUES!r}"
    )
