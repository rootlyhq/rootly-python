from typing import Literal, cast

NewDashboardPanelDataAttributesParamsDatasetsItemAggregateType0Operation = Literal["average", "count", "sum"]

NEW_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_AGGREGATE_TYPE_0_OPERATION_VALUES: set[
    NewDashboardPanelDataAttributesParamsDatasetsItemAggregateType0Operation
] = {
    "average",
    "count",
    "sum",
}


def check_new_dashboard_panel_data_attributes_params_datasets_item_aggregate_type_0_operation(
    value: str | None,
) -> NewDashboardPanelDataAttributesParamsDatasetsItemAggregateType0Operation | None:
    if value is None:
        return None
    if value in NEW_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_AGGREGATE_TYPE_0_OPERATION_VALUES:
        return cast(NewDashboardPanelDataAttributesParamsDatasetsItemAggregateType0Operation, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_DASHBOARD_PANEL_DATA_ATTRIBUTES_PARAMS_DATASETS_ITEM_AGGREGATE_TYPE_0_OPERATION_VALUES!r}"
    )
