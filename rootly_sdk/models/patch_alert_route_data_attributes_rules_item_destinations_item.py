from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_alert_route_data_attributes_rules_item_destinations_item_target_type import (
    PatchAlertRouteDataAttributesRulesItemDestinationsItemTargetType,
    check_patch_alert_route_data_attributes_rules_item_destinations_item_target_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchAlertRouteDataAttributesRulesItemDestinationsItem")


@_attrs_define
class PatchAlertRouteDataAttributesRulesItemDestinationsItem:
    """
    Attributes:
        id (UUID | Unset): The ID of the destination. Required for updating or deleting existing destinations.
        field_destroy (bool | Unset): Set to true to delete this destination
        target_type (PatchAlertRouteDataAttributesRulesItemDestinationsItemTargetType | Unset): The type of the target.
            Please contact support if you encounter issues using `Functionality` as a target type.
        target_id (UUID | Unset): The ID of the target
    """

    id: UUID | Unset = UNSET
    field_destroy: bool | Unset = UNSET
    target_type: PatchAlertRouteDataAttributesRulesItemDestinationsItemTargetType | Unset = UNSET
    target_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        field_destroy = self.field_destroy

        target_type: str | Unset = UNSET
        if not isinstance(self.target_type, Unset):
            target_type = self.target_type

        target_id: str | Unset = UNSET
        if not isinstance(self.target_id, Unset):
            target_id = str(self.target_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy
        if target_type is not UNSET:
            field_dict["target_type"] = target_type
        if target_id is not UNSET:
            field_dict["target_id"] = target_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        field_destroy = d.pop("_destroy", UNSET)

        _target_type = d.pop("target_type", UNSET)
        target_type: PatchAlertRouteDataAttributesRulesItemDestinationsItemTargetType | Unset
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = check_patch_alert_route_data_attributes_rules_item_destinations_item_target_type(_target_type)

        _target_id = d.pop("target_id", UNSET)
        target_id: UUID | Unset
        if isinstance(_target_id, Unset):
            target_id = UNSET
        else:
            target_id = UUID(_target_id)

        patch_alert_route_data_attributes_rules_item_destinations_item = cls(
            id=id,
            field_destroy=field_destroy,
            target_type=target_type,
            target_id=target_id,
        )

        patch_alert_route_data_attributes_rules_item_destinations_item.additional_properties = d
        return patch_alert_route_data_attributes_rules_item_destinations_item

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
