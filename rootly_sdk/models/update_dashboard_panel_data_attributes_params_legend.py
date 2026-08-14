from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_dashboard_panel_data_attributes_params_legend_groups import (
    UpdateDashboardPanelDataAttributesParamsLegendGroups,
    check_update_dashboard_panel_data_attributes_params_legend_groups,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateDashboardPanelDataAttributesParamsLegend")


@_attrs_define
class UpdateDashboardPanelDataAttributesParamsLegend:
    """
    Attributes:
        groups (Union[Unset, UpdateDashboardPanelDataAttributesParamsLegendGroups]):  Default: 'all'.
    """

    groups: Unset | UpdateDashboardPanelDataAttributesParamsLegendGroups = "all"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        groups: Unset | str = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _groups = d.pop("groups", UNSET)
        groups: Unset | UpdateDashboardPanelDataAttributesParamsLegendGroups
        if isinstance(_groups, Unset):
            groups = UNSET
        else:
            groups = check_update_dashboard_panel_data_attributes_params_legend_groups(_groups)

        update_dashboard_panel_data_attributes_params_legend = cls(
            groups=groups,
        )

        update_dashboard_panel_data_attributes_params_legend.additional_properties = d
        return update_dashboard_panel_data_attributes_params_legend

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
