from enum import Enum


class UpdateIncidentFormFieldSelectionDataType(str, Enum):
    INCIDENT_FORM_FIELD_SELECTIONS = "incident_form_field_selections"

    def __str__(self) -> str:
        return str(self.value)
