from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_dashboard_panel_data_attributes_params_datasets_item_filter_item_operation import (
    NewDashboardPanelDataAttributesParamsDatasetsItemFilterItemOperation,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_dashboard_panel_data_attributes_params_datasets_item_filter_item_rules_item import (
        NewDashboardPanelDataAttributesParamsDatasetsItemFilterItemRulesItem,
    )


T = TypeVar("T", bound="NewDashboardPanelDataAttributesParamsDatasetsItemFilterItem")


@_attrs_define
class NewDashboardPanelDataAttributesParamsDatasetsItemFilterItem:
    """
    Attributes:
        operation (Union[Unset, NewDashboardPanelDataAttributesParamsDatasetsItemFilterItemOperation]):
        rules (Union[Unset, list['NewDashboardPanelDataAttributesParamsDatasetsItemFilterItemRulesItem']]):
    """

    operation: Union[Unset, NewDashboardPanelDataAttributesParamsDatasetsItemFilterItemOperation] = UNSET
    rules: Union[Unset, list["NewDashboardPanelDataAttributesParamsDatasetsItemFilterItemRulesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation: Union[Unset, str] = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.value

        rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()
                rules.append(rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if operation is not UNSET:
            field_dict["operation"] = operation
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.new_dashboard_panel_data_attributes_params_datasets_item_filter_item_rules_item import (
            NewDashboardPanelDataAttributesParamsDatasetsItemFilterItemRulesItem,
        )

        d = src_dict.copy()
        _operation = d.pop("operation", UNSET)
        operation: Union[Unset, NewDashboardPanelDataAttributesParamsDatasetsItemFilterItemOperation]
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = NewDashboardPanelDataAttributesParamsDatasetsItemFilterItemOperation(_operation)

        rules = []
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:
            rules_item = NewDashboardPanelDataAttributesParamsDatasetsItemFilterItemRulesItem.from_dict(rules_item_data)

            rules.append(rules_item)

        new_dashboard_panel_data_attributes_params_datasets_item_filter_item = cls(
            operation=operation,
            rules=rules,
        )

        new_dashboard_panel_data_attributes_params_datasets_item_filter_item.additional_properties = d
        return new_dashboard_panel_data_attributes_params_datasets_item_filter_item

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
