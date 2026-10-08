from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.update_authorization_data_attributes_permissions_item import (
    UpdateAuthorizationDataAttributesPermissionsItem,
    check_update_authorization_data_attributes_permissions_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAuthorizationDataAttributes")


@_attrs_define
class UpdateAuthorizationDataAttributes:
    """
    Attributes:
        permissions (list[UpdateAuthorizationDataAttributesPermissionsItem] | Unset):
    """

    permissions: list[UpdateAuthorizationDataAttributesPermissionsItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        permissions: list[str] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item: str = permissions_item_data
                permissions.append(permissions_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _permissions = d.pop("permissions", UNSET)
        permissions: list[UpdateAuthorizationDataAttributesPermissionsItem] | Unset = UNSET
        if _permissions is not UNSET:
            permissions = []
            for permissions_item_data in _permissions:
                permissions_item = check_update_authorization_data_attributes_permissions_item(permissions_item_data)

                permissions.append(permissions_item)

        update_authorization_data_attributes = cls(
            permissions=permissions,
        )

        return update_authorization_data_attributes
