from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dashboard_panel_params_datasets_item_filter_item_operation import (
    DashboardPanelParamsDatasetsItemFilterItemOperation,
    check_dashboard_panel_params_datasets_item_filter_item_operation,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_panel_params_datasets_item_filter_item_rules_item import (
        DashboardPanelParamsDatasetsItemFilterItemRulesItem,
    )


T = TypeVar("T", bound="DashboardPanelParamsDatasetsItemFilterItem")


@_attrs_define
class DashboardPanelParamsDatasetsItemFilterItem:
    """
    Attributes:
        operation (Union[Unset, DashboardPanelParamsDatasetsItemFilterItemOperation]):
        rules (Union[Unset, list['DashboardPanelParamsDatasetsItemFilterItemRulesItem']]):
    """

    operation: Unset | DashboardPanelParamsDatasetsItemFilterItemOperation = UNSET
    rules: Unset | list["DashboardPanelParamsDatasetsItemFilterItemRulesItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation: Unset | str = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation

        rules: Unset | list[dict[str, Any]] = UNSET
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_panel_params_datasets_item_filter_item_rules_item import (
            DashboardPanelParamsDatasetsItemFilterItemRulesItem,
        )

        d = dict(src_dict)
        _operation = d.pop("operation", UNSET)
        operation: Unset | DashboardPanelParamsDatasetsItemFilterItemOperation
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = check_dashboard_panel_params_datasets_item_filter_item_operation(_operation)

        rules = []
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:
            rules_item = DashboardPanelParamsDatasetsItemFilterItemRulesItem.from_dict(rules_item_data)

            rules.append(rules_item)

        dashboard_panel_params_datasets_item_filter_item = cls(
            operation=operation,
            rules=rules,
        )

        dashboard_panel_params_datasets_item_filter_item.additional_properties = d
        return dashboard_panel_params_datasets_item_filter_item

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
