from typing import Literal

UpdateWorkflowCustomFieldSelectionDataAttributesIncidentCondition = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

UPDATE_WORKFLOW_CUSTOM_FIELD_SELECTION_DATA_ATTRIBUTES_INCIDENT_CONDITION_VALUES: set[
    UpdateWorkflowCustomFieldSelectionDataAttributesIncidentCondition
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


def check_update_workflow_custom_field_selection_data_attributes_incident_condition(
    value: str | None,
) -> UpdateWorkflowCustomFieldSelectionDataAttributesIncidentCondition | None:
    if value is None:
        return None
    if value in UPDATE_WORKFLOW_CUSTOM_FIELD_SELECTION_DATA_ATTRIBUTES_INCIDENT_CONDITION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_WORKFLOW_CUSTOM_FIELD_SELECTION_DATA_ATTRIBUTES_INCIDENT_CONDITION_VALUES!r}"
    )
