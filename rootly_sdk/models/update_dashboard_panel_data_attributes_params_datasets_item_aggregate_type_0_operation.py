from typing import Literal, cast

UpdateDashboardPanelDataAttributesParamsDatasetsItemAggregateType0Operation = Literal["average", "count", "sum"]

UPDATE_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_AGGREGATE_TYPE_0_OPERATION_VALUES: set[
    UpdateDashboardPanelDataAttributesParamsDatasetsItemAggregateType0Operation
] = {
    "average",
    "count",
    "sum",
}


def check_update_dashboard_panel_data_attributes_params_datasets_item_aggregate_type_0_operation(
    value: str | None,
) -> UpdateDashboardPanelDataAttributesParamsDatasetsItemAggregateType0Operation | None:
    if value is None:
        return None
    if value in UPDATE_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_AGGREGATE_TYPE_0_OPERATION_VALUES:
        return cast(UpdateDashboardPanelDataAttributesParamsDatasetsItemAggregateType0Operation, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_AGGREGATE_TYPE_0_OPERATION_VALUES!r}"
    )
