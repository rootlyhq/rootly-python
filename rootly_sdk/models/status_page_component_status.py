from typing import Literal, cast

StatusPageComponentStatus = Literal[
    "degraded_performance", "impacted", "maintenance", "major_outage", "operational", "partial_outage"
]

STATUS_PAGE_COMPONENT_STATUS_VALUES: set[StatusPageComponentStatus] = {
    "degraded_performance",
    "impacted",
    "maintenance",
    "major_outage",
    "operational",
    "partial_outage",
}


def check_status_page_component_status(value: str | None) -> StatusPageComponentStatus | None:
    if value is None:
        return None
    if value in STATUS_PAGE_COMPONENT_STATUS_VALUES:
        return cast(StatusPageComponentStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_COMPONENT_STATUS_VALUES!r}")
