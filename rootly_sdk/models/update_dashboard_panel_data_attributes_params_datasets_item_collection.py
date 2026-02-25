from typing import Literal, cast

UpdateDashboardPanelDataAttributesParamsDatasetsItemCollection = Literal[
    "alerts", "incident_action_items", "incident_post_mortems", "incidents", "users"
]

UPDATE_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_COLLECTION_VALUES: set[
    UpdateDashboardPanelDataAttributesParamsDatasetsItemCollection
] = {
    "alerts",
    "incident_action_items",
    "incident_post_mortems",
    "incidents",
    "users",
}


def check_update_dashboard_panel_data_attributes_params_datasets_item_collection(
    value: str | None,
) -> UpdateDashboardPanelDataAttributesParamsDatasetsItemCollection | None:
    if value is None:
        return None
    if value in UPDATE_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_COLLECTION_VALUES:
        return cast(UpdateDashboardPanelDataAttributesParamsDatasetsItemCollection, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_COLLECTION_VALUES!r}"
    )
