from enum import Enum


class UpdateIncidentPermissionSetBooleanDataType(str, Enum):
    INCIDENT_PERMISSION_SET_BOOLEANS = "incident_permission_set_booleans"

    def __str__(self) -> str:
        return str(self.value)
