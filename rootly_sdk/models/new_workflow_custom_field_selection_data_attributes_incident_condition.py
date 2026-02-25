from typing import Literal, cast

NewWorkflowCustomFieldSelectionDataAttributesIncidentCondition = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

NEW_WORKFLOW_CUSTOM_FIELD_SELECTION_DATA_ATTRIBUTES_INCIDENT_CONDITION_VALUES: set[
    NewWorkflowCustomFieldSelectionDataAttributesIncidentCondition
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


def check_new_workflow_custom_field_selection_data_attributes_incident_condition(
    value: str | None,
) -> NewWorkflowCustomFieldSelectionDataAttributesIncidentCondition | None:
    if value is None:
        return None
    if value in NEW_WORKFLOW_CUSTOM_FIELD_SELECTION_DATA_ATTRIBUTES_INCIDENT_CONDITION_VALUES:
        return cast(NewWorkflowCustomFieldSelectionDataAttributesIncidentCondition, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_WORKFLOW_CUSTOM_FIELD_SELECTION_DATA_ATTRIBUTES_INCIDENT_CONDITION_VALUES!r}"
    )
