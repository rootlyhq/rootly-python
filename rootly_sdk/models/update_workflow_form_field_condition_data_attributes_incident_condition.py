from typing import Literal, cast

UpdateWorkflowFormFieldConditionDataAttributesIncidentCondition = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

UPDATE_WORKFLOW_FORM_FIELD_CONDITION_DATA_ATTRIBUTES_INCIDENT_CONDITION_VALUES: set[
    UpdateWorkflowFormFieldConditionDataAttributesIncidentCondition
] = {
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


def check_update_workflow_form_field_condition_data_attributes_incident_condition(
    value: str | None,
) -> UpdateWorkflowFormFieldConditionDataAttributesIncidentCondition | None:
    if value is None:
        return None
    if value in UPDATE_WORKFLOW_FORM_FIELD_CONDITION_DATA_ATTRIBUTES_INCIDENT_CONDITION_VALUES:
        return cast(UpdateWorkflowFormFieldConditionDataAttributesIncidentCondition, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_WORKFLOW_FORM_FIELD_CONDITION_DATA_ATTRIBUTES_INCIDENT_CONDITION_VALUES!r}"
    )
