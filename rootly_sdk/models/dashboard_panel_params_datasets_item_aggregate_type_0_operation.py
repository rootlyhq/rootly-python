from typing import Literal, cast

DashboardPanelParamsDatasetsItemAggregateType0Operation = Literal["average", "count", "sum"]

DASHBOARD_PANEL_PARAMS_DATASETS_ITEM_AGGREGATE_TYPE_0_OPERATION_VALUES: set[
    DashboardPanelParamsDatasetsItemAggregateType0Operation
] = {
    "average",
    "count",
    "sum",
}


def check_dashboard_panel_params_datasets_item_aggregate_type_0_operation(
    value: str | None,
) -> DashboardPanelParamsDatasetsItemAggregateType0Operation | None:
    if value is None:
        return None
    if value in DASHBOARD_PANEL_PARAMS_DATASETS_ITEM_AGGREGATE_TYPE_0_OPERATION_VALUES:
        return cast(DashboardPanelParamsDatasetsItemAggregateType0Operation, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DASHBOARD_PANEL_PARAMS_DATASETS_ITEM_AGGREGATE_TYPE_0_OPERATION_VALUES!r}"
    )
