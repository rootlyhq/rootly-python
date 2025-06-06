from enum import Enum


class NewIncidentStatusPageEventDataType(str, Enum):
    INCIDENT_STATUS_PAGE_EVENTS = "incident_status_page_events"

    def __str__(self) -> str:
        return str(self.value)
