from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_dashboard_panel_data_attributes_params_datasets_item_aggregate_type_0_operation import (
    UpdateDashboardPanelDataAttributesParamsDatasetsItemAggregateType0Operation,
    check_update_dashboard_panel_data_attributes_params_datasets_item_aggregate_type_0_operation,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateDashboardPanelDataAttributesParamsDatasetsItemAggregateType0")


@_attrs_define
class UpdateDashboardPanelDataAttributesParamsDatasetsItemAggregateType0:
    """
    Attributes:
        operation (Union[Unset, UpdateDashboardPanelDataAttributesParamsDatasetsItemAggregateType0Operation]):
        key (Union[None, Unset, str]):
        cumulative (Union[None, Unset, bool]):
    """

    operation: Unset | UpdateDashboardPanelDataAttributesParamsDatasetsItemAggregateType0Operation = UNSET
    key: None | Unset | str = UNSET
    cumulative: None | Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation: Unset | str = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation

        key: None | Unset | str
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        cumulative: None | Unset | bool
        if isinstance(self.cumulative, Unset):
            cumulative = UNSET
        else:
            cumulative = self.cumulative

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if operation is not UNSET:
            field_dict["operation"] = operation
        if key is not UNSET:
            field_dict["key"] = key
        if cumulative is not UNSET:
            field_dict["cumulative"] = cumulative

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _operation = d.pop("operation", UNSET)
        operation: Unset | UpdateDashboardPanelDataAttributesParamsDatasetsItemAggregateType0Operation
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = check_update_dashboard_panel_data_attributes_params_datasets_item_aggregate_type_0_operation(
                _operation
            )

        def _parse_key(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        key = _parse_key(d.pop("key", UNSET))

        def _parse_cumulative(data: object) -> None | Unset | bool:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | bool, data)

        cumulative = _parse_cumulative(d.pop("cumulative", UNSET))

        update_dashboard_panel_data_attributes_params_datasets_item_aggregate_type_0 = cls(
            operation=operation,
            key=key,
            cumulative=cumulative,
        )

        update_dashboard_panel_data_attributes_params_datasets_item_aggregate_type_0.additional_properties = d
        return update_dashboard_panel_data_attributes_params_datasets_item_aggregate_type_0

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
