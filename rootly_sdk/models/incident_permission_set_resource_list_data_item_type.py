from enum import Enum


class IncidentPermissionSetResourceListDataItemType(str, Enum):
    INCIDENT_PERMISSION_SET_RESOURCES = "incident_permission_set_resources"

    def __str__(self) -> str:
        return str(self.value)
