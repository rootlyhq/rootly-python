from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

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
        display (Union[Unset, UpdateDashboardPanelDataAttributesParamsDisplay]):
        description (Union[Unset, str]):
        table_fields (Union[Unset, list[str]]):
        legend (Union[Unset, UpdateDashboardPanelDataAttributesParamsLegend]):
        datalabels (Union[Unset, UpdateDashboardPanelDataAttributesParamsDatalabels]):
        datasets (Union[Unset, list['UpdateDashboardPanelDataAttributesParamsDatasetsItem']]):
    """

    display: Unset | UpdateDashboardPanelDataAttributesParamsDisplay = UNSET
    description: Unset | str = UNSET
    table_fields: Unset | list[str] = UNSET
    legend: Union[Unset, "UpdateDashboardPanelDataAttributesParamsLegend"] = UNSET
    datalabels: Union[Unset, "UpdateDashboardPanelDataAttributesParamsDatalabels"] = UNSET
    datasets: Unset | list["UpdateDashboardPanelDataAttributesParamsDatasetsItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display: Unset | str = UNSET
        if not isinstance(self.display, Unset):
            display = self.display

        description = self.description

        table_fields: Unset | list[str] = UNSET
        if not isinstance(self.table_fields, Unset):
            table_fields = self.table_fields

        legend: Unset | dict[str, Any] = UNSET
        if not isinstance(self.legend, Unset):
            legend = self.legend.to_dict()

        datalabels: Unset | dict[str, Any] = UNSET
        if not isinstance(self.datalabels, Unset):
            datalabels = self.datalabels.to_dict()

        datasets: Unset | list[dict[str, Any]] = UNSET
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
        display: Unset | UpdateDashboardPanelDataAttributesParamsDisplay
        if isinstance(_display, Unset):
            display = UNSET
        else:
            display = check_update_dashboard_panel_data_attributes_params_display(_display)

        description = d.pop("description", UNSET)

        table_fields = cast(list[str], d.pop("table_fields", UNSET))

        _legend = d.pop("legend", UNSET)
        legend: Unset | UpdateDashboardPanelDataAttributesParamsLegend
        if isinstance(_legend, Unset):
            legend = UNSET
        else:
            legend = UpdateDashboardPanelDataAttributesParamsLegend.from_dict(_legend)

        _datalabels = d.pop("datalabels", UNSET)
        datalabels: Unset | UpdateDashboardPanelDataAttributesParamsDatalabels
        if isinstance(_datalabels, Unset):
            datalabels = UNSET
        else:
            datalabels = UpdateDashboardPanelDataAttributesParamsDatalabels.from_dict(_datalabels)

        datasets = []
        _datasets = d.pop("datasets", UNSET)
        for datasets_item_data in _datasets or []:
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
