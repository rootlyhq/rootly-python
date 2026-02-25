from typing import Literal, cast

DashboardPanelParamsDatasetsItemCollection = Literal[
    "alerts", "incident_action_items", "incident_post_mortems", "incidents", "users"
]

DASHBOARD_PANEL_PARAMS_DATASETS_ITEM_COLLECTION_VALUES: set[DashboardPanelParamsDatasetsItemCollection] = {
    "alerts",
    "incident_action_items",
    "incident_post_mortems",
    "incidents",
    "users",
}


def check_dashboard_panel_params_datasets_item_collection(
    value: str | None,
) -> DashboardPanelParamsDatasetsItemCollection | None:
    if value is None:
        return None
    if value in DASHBOARD_PANEL_PARAMS_DATASETS_ITEM_COLLECTION_VALUES:
        return cast(DashboardPanelParamsDatasetsItemCollection, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DASHBOARD_PANEL_PARAMS_DATASETS_ITEM_COLLECTION_VALUES!r}"
    )
