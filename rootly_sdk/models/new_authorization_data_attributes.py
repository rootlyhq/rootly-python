from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.new_authorization_data_attributes_authorizable_type import (
    check_new_authorization_data_attributes_authorizable_type,
)
from ..models.new_authorization_data_attributes_authorizable_type import NewAuthorizationDataAttributesAuthorizableType
from ..models.new_authorization_data_attributes_grantee_type import check_new_authorization_data_attributes_grantee_type
from ..models.new_authorization_data_attributes_grantee_type import NewAuthorizationDataAttributesGranteeType
from ..models.new_authorization_data_attributes_permissions_item import (
    check_new_authorization_data_attributes_permissions_item,
)
from ..models.new_authorization_data_attributes_permissions_item import NewAuthorizationDataAttributesPermissionsItem
from typing import cast


T = TypeVar("T", bound="NewAuthorizationDataAttributes")


@_attrs_define
class NewAuthorizationDataAttributes:
    """
    Attributes:
        authorizable_id (str): The id of the resource being accessed.
        authorizable_type (NewAuthorizationDataAttributesAuthorizableType): The type of resource being accessed.
        grantee_id (str): The resource id granted access.
        grantee_type (NewAuthorizationDataAttributesGranteeType): The type of resource granted access.
        permissions (list[NewAuthorizationDataAttributesPermissionsItem]):
    """

    authorizable_id: str
    authorizable_type: NewAuthorizationDataAttributesAuthorizableType
    grantee_id: str
    grantee_type: NewAuthorizationDataAttributesGranteeType
    permissions: list[NewAuthorizationDataAttributesPermissionsItem]

    def to_dict(self) -> dict[str, Any]:
        authorizable_id = self.authorizable_id

        authorizable_type: str = self.authorizable_type

        grantee_id = self.grantee_id

        grantee_type: str = self.grantee_type

        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item: str = permissions_item_data
            permissions.append(permissions_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "authorizable_id": authorizable_id,
                "authorizable_type": authorizable_type,
                "grantee_id": grantee_id,
                "grantee_type": grantee_type,
                "permissions": permissions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        authorizable_id = d.pop("authorizable_id")

        authorizable_type = check_new_authorization_data_attributes_authorizable_type(d.pop("authorizable_type"))

        grantee_id = d.pop("grantee_id")

        grantee_type = check_new_authorization_data_attributes_grantee_type(d.pop("grantee_type"))

        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in _permissions:
            permissions_item = check_new_authorization_data_attributes_permissions_item(permissions_item_data)

            permissions.append(permissions_item)

        new_authorization_data_attributes = cls(
            authorizable_id=authorizable_id,
            authorizable_type=authorizable_type,
            grantee_id=grantee_id,
            grantee_type=grantee_type,
            permissions=permissions,
        )

        return new_authorization_data_attributes
