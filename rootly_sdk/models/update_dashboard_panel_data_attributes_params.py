from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_dashboard_panel_data_attributes_params_display import (
    UpdateDashboardPanelDataAttributesParamsDisplay,
    check_update_dashboard_panel_data_attributes_params_display,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_dashboard_panel_data_attributes_params_datalabels import (
        UpdateDashboardPanelDataAttributesParamsDatalabels,
    )
    from ..models.update_dashboard_panel_data_attributes_params_datasets_item import (
        UpdateDashboardPanelDataAttributesParamsDatasetsItem,
    )
    from ..models.update_dashboard_panel_data_attributes_params_legend import (
        UpdateDashboardPanelDataAttributesParamsLegend,
    )


T = TypeVar("T", bound="UpdateDashboardPanelDataAttributesParams")


@_attrs_define
class UpdateDashboardPanelDataAttributesParams:
    """
    Attributes:
        display (UpdateDashboardPanelDataAttributesParamsDisplay | Unset):
        description (str | Unset):
        table_fields (list[str] | Unset):
        legend (UpdateDashboardPanelDataAttributesParamsLegend | Unset):
        datalabels (UpdateDashboardPanelDataAttributesParamsDatalabels | Unset):
        datasets (list[UpdateDashboardPanelDataAttributesParamsDatasetsItem] | Unset):
    """

    display: UpdateDashboardPanelDataAttributesParamsDisplay | Unset = UNSET
    description: str | Unset = UNSET
    table_fields: list[str] | Unset = UNSET
    legend: UpdateDashboardPanelDataAttributesParamsLegend | Unset = UNSET
    datalabels: UpdateDashboardPanelDataAttributesParamsDatalabels | Unset = UNSET
    datasets: list[UpdateDashboardPanelDataAttributesParamsDatasetsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display: str | Unset = UNSET
        if not isinstance(self.display, Unset):
            display = self.display

        description = self.description

        table_fields: list[str] | Unset = UNSET
        if not isinstance(self.table_fields, Unset):
            table_fields = self.table_fields

        legend: dict[str, Any] | Unset = UNSET
        if not isinstance(self.legend, Unset):
            legend = self.legend.to_dict()

        datalabels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.datalabels, Unset):
            datalabels = self.datalabels.to_dict()

        datasets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.datasets, Unset):
            datasets = []
            for datasets_item_data in self.datasets:
                datasets_item = datasets_item_data.to_dict()
                datasets.append(datasets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display is not UNSET:
            field_dict["display"] = display
        if description is not UNSET:
            field_dict["description"] = description
        if table_fields is not UNSET:
            field_dict["table_fields"] = table_fields
        if legend is not UNSET:
            field_dict["legend"] = legend
        if datalabels is not UNSET:
            field_dict["datalabels"] = datalabels
        if datasets is not UNSET:
            field_dict["datasets"] = datasets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_dashboard_panel_data_attributes_params_datalabels import (
            UpdateDashboardPanelDataAttributesParamsDatalabels,
        )
        from ..models.update_dashboard_panel_data_attributes_params_datasets_item import (
            UpdateDashboardPanelDataAttributesParamsDatasetsItem,
        )
        from ..models.update_dashboard_panel_data_attributes_params_legend import (
            UpdateDashboardPanelDataAttributesParamsLegend,
        )

        d = dict(src_dict)
        _display = d.pop("display", UNSET)
        display: UpdateDashboardPanelDataAttributesParamsDisplay | Unset
        if isinstance(_display, Unset):
            display = UNSET
        else:
            display = check_update_dashboard_panel_data_attributes_params_display(_display)

        description = d.pop("description", UNSET)

        table_fields = cast(list[str], d.pop("table_fields", UNSET))

        _legend = d.pop("legend", UNSET)
        legend: UpdateDashboardPanelDataAttributesParamsLegend | Unset
        if isinstance(_legend, Unset):
            legend = UNSET
        else:
            legend = UpdateDashboardPanelDataAttributesParamsLegend.from_dict(_legend)

        _datalabels = d.pop("datalabels", UNSET)
        datalabels: UpdateDashboardPanelDataAttributesParamsDatalabels | Unset
        if isinstance(_datalabels, Unset):
            datalabels = UNSET
        else:
            datalabels = UpdateDashboardPanelDataAttributesParamsDatalabels.from_dict(_datalabels)

        _datasets = d.pop("datasets", UNSET)
        datasets: list[UpdateDashboardPanelDataAttributesParamsDatasetsItem] | Unset = UNSET
        if _datasets is not UNSET:
            datasets = []
            for datasets_item_data in _datasets:
                datasets_item = UpdateDashboardPanelDataAttributesParamsDatasetsItem.from_dict(datasets_item_data)

                datasets.append(datasets_item)

        update_dashboard_panel_data_attributes_params = cls(
            display=display,
            description=description,
            table_fields=table_fields,
            legend=legend,
            datalabels=datalabels,
            datasets=datasets,
        )

        update_dashboard_panel_data_attributes_params.additional_properties = d
        return update_dashboard_panel_data_attributes_params

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
