from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_dashboard_panel_data_attributes_params_datasets_item_group_by_type_1_type_0_key import (
    UpdateDashboardPanelDataAttributesParamsDatasetsItemGroupByType1Type0Key,
    check_update_dashboard_panel_data_attributes_params_datasets_item_group_by_type_1_type_0_key,
)

T = TypeVar("T", bound="UpdateDashboardPanelDataAttributesParamsDatasetsItemGroupByType1Type0")


@_attrs_define
class UpdateDashboardPanelDataAttributesParamsDatasetsItemGroupByType1Type0:
    """
    Attributes:
        key (UpdateDashboardPanelDataAttributesParamsDatasetsItemGroupByType1Type0Key):
        value (str):
    """

    key: UpdateDashboardPanelDataAttributesParamsDatasetsItemGroupByType1Type0Key
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key: str = self.key

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = check_update_dashboard_panel_data_attributes_params_datasets_item_group_by_type_1_type_0_key(d.pop("key"))

        value = d.pop("value")

        update_dashboard_panel_data_attributes_params_datasets_item_group_by_type_1_type_0 = cls(
            key=key,
            value=value,
        )

        update_dashboard_panel_data_attributes_params_datasets_item_group_by_type_1_type_0.additional_properties = d
        return update_dashboard_panel_data_attributes_params_datasets_item_group_by_type_1_type_0

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
