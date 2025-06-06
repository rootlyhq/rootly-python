from enum import Enum


class NewWorkflowCustomFieldSelectionDataType(str, Enum):
    WORKFLOW_CUSTOM_FIELD_SELECTIONS = "workflow_custom_field_selections"

    def __str__(self) -> str:
        return str(self.value)
