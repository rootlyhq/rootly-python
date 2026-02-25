from typing import Literal, cast

NewDashboardPanelDataAttributesParamsDatasetsItemCollection = Literal[
    "alerts", "incident_action_items", "incident_post_mortems", "incidents", "users"
]

NEW_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_COLLECTION_VALUES: set[
    NewDashboardPanelDataAttributesParamsDatasetsItemCollection
] = {
    "alerts",
    "incident_action_items",
    "incident_post_mortems",
    "incidents",
    "users",
}


def check_new_dashboard_panel_data_attributes_params_datasets_item_collection(
    value: str | None,
) -> NewDashboardPanelDataAttributesParamsDatasetsItemCollection | None:
    if value is None:
        return None
    if value in NEW_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_COLLECTION_VALUES:
        return cast(NewDashboardPanelDataAttributesParamsDatasetsItemCollection, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_COLLECTION_VALUES!r}"
    )
