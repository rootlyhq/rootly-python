from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dashboard_panel_params_datasets_item_filter_item_rules_item_condition import (
    DashboardPanelParamsDatasetsItemFilterItemRulesItemCondition,
    check_dashboard_panel_params_datasets_item_filter_item_rules_item_condition,
)
from ..models.dashboard_panel_params_datasets_item_filter_item_rules_item_operation import (
    DashboardPanelParamsDatasetsItemFilterItemRulesItemOperation,
    check_dashboard_panel_params_datasets_item_filter_item_rules_item_operation,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardPanelParamsDatasetsItemFilterItemRulesItem")


@_attrs_define
class DashboardPanelParamsDatasetsItemFilterItemRulesItem:
    """
    Attributes:
        operation (Union[Unset, DashboardPanelParamsDatasetsItemFilterItemRulesItemOperation]):
        condition (Union[Unset, DashboardPanelParamsDatasetsItemFilterItemRulesItemCondition]):
        key (Union[Unset, str]):
        value (Union[Unset, str]):
    """

    operation: Unset | DashboardPanelParamsDatasetsItemFilterItemRulesItemOperation = UNSET
    condition: Unset | DashboardPanelParamsDatasetsItemFilterItemRulesItemCondition = UNSET
    key: Unset | str = UNSET
    value: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation: Unset | str = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation

        condition: Unset | str = UNSET
        if not isinstance(self.condition, Unset):
            condition = self.condition

        key = self.key

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if operation is not UNSET:
            field_dict["operation"] = operation
        if condition is not UNSET:
            field_dict["condition"] = condition
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _operation = d.pop("operation", UNSET)
        operation: Unset | DashboardPanelParamsDatasetsItemFilterItemRulesItemOperation
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = check_dashboard_panel_params_datasets_item_filter_item_rules_item_operation(_operation)

        _condition = d.pop("condition", UNSET)
        condition: Unset | DashboardPanelParamsDatasetsItemFilterItemRulesItemCondition
        if isinstance(_condition, Unset):
            condition = UNSET
        else:
            condition = check_dashboard_panel_params_datasets_item_filter_item_rules_item_condition(_condition)

        key = d.pop("key", UNSET)

        value = d.pop("value", UNSET)

        dashboard_panel_params_datasets_item_filter_item_rules_item = cls(
            operation=operation,
            condition=condition,
            key=key,
            value=value,
        )

        dashboard_panel_params_datasets_item_filter_item_rules_item.additional_properties = d
        return dashboard_panel_params_datasets_item_filter_item_rules_item

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
