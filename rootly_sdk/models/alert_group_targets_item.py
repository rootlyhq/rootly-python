from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_group_targets_item_target_type import AlertGroupTargetsItemTargetType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertGroupTargetsItem")


@_attrs_define
class AlertGroupTargetsItem:
    """
    Attributes:
        target_type (Union[Unset, AlertGroupTargetsItemTargetType]): The type of the target.
        target_id (Union[Unset, UUID]): id for the Group, Service or EscalationPolicy
    """

    target_type: Union[Unset, AlertGroupTargetsItemTargetType] = UNSET
    target_id: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_type: Union[Unset, str] = UNSET
        if not isinstance(self.target_type, Unset):
            target_type = self.target_type.value

        target_id: Union[Unset, str] = UNSET
        if not isinstance(self.target_id, Unset):
            target_id = str(self.target_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target_type is not UNSET:
            field_dict["target_type"] = target_type
        if target_id is not UNSET:
            field_dict["target_id"] = target_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _target_type = d.pop("target_type", UNSET)
        target_type: Union[Unset, AlertGroupTargetsItemTargetType]
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = AlertGroupTargetsItemTargetType(_target_type)

        _target_id = d.pop("target_id", UNSET)
        target_id: Union[Unset, UUID]
        if isinstance(_target_id, Unset):
            target_id = UNSET
        else:
            target_id = UUID(_target_id)

        alert_group_targets_item = cls(
            target_type=target_type,
            target_id=target_id,
        )

        alert_group_targets_item.additional_properties = d
        return alert_group_targets_item

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
