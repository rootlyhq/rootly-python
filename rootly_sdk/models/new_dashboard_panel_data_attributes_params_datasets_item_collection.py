from enum import Enum


class NewDashboardPanelDataAttributesParamsDatasetsItemCollection(str, Enum):
    ALERTS = "alerts"
    INCIDENTS = "incidents"
    INCIDENT_ACTION_ITEMS = "incident_action_items"
    INCIDENT_POST_MORTEMS = "incident_post_mortems"
    USERS = "users"

    def __str__(self) -> str:
        return str(self.value)
