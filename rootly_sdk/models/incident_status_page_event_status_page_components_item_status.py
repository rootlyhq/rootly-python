from typing import Literal, cast

IncidentStatusPageEventStatusPageComponentsItemStatus = Literal[
    "degraded_performance", "major_outage", "operational", "partial_outage"
]

INCIDENT_STATUS_PAGE_EVENT_STATUS_PAGE_COMPONENTS_ITEM_STATUS_VALUES: set[
    IncidentStatusPageEventStatusPageComponentsItemStatus
] = {
    "degraded_performance",
    "major_outage",
    "operational",
    "partial_outage",
}


def check_incident_status_page_event_status_page_components_item_status(
    value: str | None,
) -> IncidentStatusPageEventStatusPageComponentsItemStatus | None:
    if value is None:
        return None
    if value in INCIDENT_STATUS_PAGE_EVENT_STATUS_PAGE_COMPONENTS_ITEM_STATUS_VALUES:
        return cast(IncidentStatusPageEventStatusPageComponentsItemStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_STATUS_PAGE_EVENT_STATUS_PAGE_COMPONENTS_ITEM_STATUS_VALUES!r}"
    )
