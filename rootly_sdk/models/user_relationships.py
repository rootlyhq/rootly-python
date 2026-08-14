from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.on_call_role_relationship import OnCallRoleRelationship
    from ..models.role_relationship import RoleRelationship


T = TypeVar("T", bound="UserRelationships")


@_attrs_define
class UserRelationships:
    """
    Attributes:
        role (Union[Unset, RoleRelationship]):
        on_call_role (Union[Unset, OnCallRoleRelationship]):
    """

    role: Union[Unset, "RoleRelationship"] = UNSET
    on_call_role: Union[Unset, "OnCallRoleRelationship"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role: Unset | dict[str, Any] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        on_call_role: Unset | dict[str, Any] = UNSET
        if not isinstance(self.on_call_role, Unset):
            on_call_role = self.on_call_role.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role is not UNSET:
            field_dict["role"] = role
        if on_call_role is not UNSET:
            field_dict["on_call_role"] = on_call_role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.on_call_role_relationship import OnCallRoleRelationship
        from ..models.role_relationship import RoleRelationship

        d = dict(src_dict)
        _role = d.pop("role", UNSET)
        role: Unset | RoleRelationship
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = RoleRelationship.from_dict(_role)

        _on_call_role = d.pop("on_call_role", UNSET)
        on_call_role: Unset | OnCallRoleRelationship
        if isinstance(_on_call_role, Unset):
            on_call_role = UNSET
        else:
            on_call_role = OnCallRoleRelationship.from_dict(_on_call_role)

        user_relationships = cls(
            role=role,
            on_call_role=on_call_role,
        )

        user_relationships.additional_properties = d
        return user_relationships

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
