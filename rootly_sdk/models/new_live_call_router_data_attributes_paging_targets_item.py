from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_live_call_router_data_attributes_paging_targets_item_type import (
    NewLiveCallRouterDataAttributesPagingTargetsItemType,
    check_new_live_call_router_data_attributes_paging_targets_item_type,
)

T = TypeVar("T", bound="NewLiveCallRouterDataAttributesPagingTargetsItem")


@_attrs_define
class NewLiveCallRouterDataAttributesPagingTargetsItem:
    """
    Attributes:
        id (str): The ID of paging target
        type_ (NewLiveCallRouterDataAttributesPagingTargetsItemType): The type of the paging target. Please contact
            support if you encounter issues using `functionality` as a target type.
        alert_urgency_id (str): This is used in escalation paths to determine who to page
    """

    id: str
    type_: NewLiveCallRouterDataAttributesPagingTargetsItemType
    alert_urgency_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: str = self.type_

        alert_urgency_id = self.alert_urgency_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "alert_urgency_id": alert_urgency_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = check_new_live_call_router_data_attributes_paging_targets_item_type(d.pop("type"))

        alert_urgency_id = d.pop("alert_urgency_id")

        new_live_call_router_data_attributes_paging_targets_item = cls(
            id=id,
            type_=type_,
            alert_urgency_id=alert_urgency_id,
        )

        new_live_call_router_data_attributes_paging_targets_item.additional_properties = d
        return new_live_call_router_data_attributes_paging_targets_item

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
