from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.authorization_authorizable_type import (
    AuthorizationAuthorizableType,
    check_authorization_authorizable_type,
)
from ..models.authorization_grantee_type import AuthorizationGranteeType, check_authorization_grantee_type
from ..models.authorization_permissions_item import AuthorizationPermissionsItem, check_authorization_permissions_item

T = TypeVar("T", bound="Authorization")


@_attrs_define
class Authorization:
    """
    Attributes:
        authorizable_id (str): The id of the resource being accessed.
        authorizable_type (AuthorizationAuthorizableType): The type of resource being accessed.
        grantee_id (str): The resource id granted access.
        grantee_type (AuthorizationGranteeType): The type of resource granted access.
        permissions (list[AuthorizationPermissionsItem]):
        created_at (str):
        updated_at (str):
    """

    authorizable_id: str
    authorizable_type: AuthorizationAuthorizableType
    grantee_id: str
    grantee_type: AuthorizationGranteeType
    permissions: list[AuthorizationPermissionsItem]
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authorizable_id = self.authorizable_id

        authorizable_type: str = self.authorizable_type

        grantee_id = self.grantee_id

        grantee_type: str = self.grantee_type

        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item: str = permissions_item_data
            permissions.append(permissions_item)

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authorizable_id": authorizable_id,
                "authorizable_type": authorizable_type,
                "grantee_id": grantee_id,
                "grantee_type": grantee_type,
                "permissions": permissions,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        authorizable_id = d.pop("authorizable_id")

        authorizable_type = check_authorization_authorizable_type(d.pop("authorizable_type"))

        grantee_id = d.pop("grantee_id")

        grantee_type = check_authorization_grantee_type(d.pop("grantee_type"))

        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in _permissions:
            permissions_item = check_authorization_permissions_item(permissions_item_data)

            permissions.append(permissions_item)

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        authorization = cls(
            authorizable_id=authorizable_id,
            authorizable_type=authorizable_type,
            grantee_id=grantee_id,
            grantee_type=grantee_type,
            permissions=permissions,
            created_at=created_at,
            updated_at=updated_at,
        )

        authorization.additional_properties = d
        return authorization

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
