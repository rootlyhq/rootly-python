from typing import Literal, cast

NewIncidentStatusPageEventDataAttributesStatusPageComponentsType0ItemStatus = Literal[
    "degraded_performance", "major_outage", "operational", "partial_outage"
]

NEW_INCIDENT_STATUS_PAGE_EVENT_DATA_ATTRIBUTES_STATUS_PAGE_COMPONENTS_TYPE_0_ITEM_STATUS_VALUES: set[
    NewIncidentStatusPageEventDataAttributesStatusPageComponentsType0ItemStatus
] = {
    "degraded_performance",
    "major_outage",
    "operational",
    "partial_outage",
}


def check_new_incident_status_page_event_data_attributes_status_page_components_type_0_item_status(
    value: str | None,
) -> NewIncidentStatusPageEventDataAttributesStatusPageComponentsType0ItemStatus | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_STATUS_PAGE_EVENT_DATA_ATTRIBUTES_STATUS_PAGE_COMPONENTS_TYPE_0_ITEM_STATUS_VALUES:
        return cast(NewIncidentStatusPageEventDataAttributesStatusPageComponentsType0ItemStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_STATUS_PAGE_EVENT_DATA_ATTRIBUTES_STATUS_PAGE_COMPONENTS_TYPE_0_ITEM_STATUS_VALUES!r}"
    )
