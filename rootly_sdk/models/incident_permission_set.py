from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_permission_set_private_incident_permissions_item import (
    IncidentPermissionSetPrivateIncidentPermissionsItem,
    check_incident_permission_set_private_incident_permissions_item,
)
from ..models.incident_permission_set_public_incident_permissions_item import (
    IncidentPermissionSetPublicIncidentPermissionsItem,
    check_incident_permission_set_public_incident_permissions_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentPermissionSet")


@_attrs_define
class IncidentPermissionSet:
    """
    Attributes:
        name (str): The incident permission set name.
        created_at (str):
        updated_at (str):
        slug (Union[Unset, str]): The incident permission set slug.
        description (Union[None, Unset, str]): The incident permission set description.
        private_incident_permissions (Union[Unset, list[IncidentPermissionSetPrivateIncidentPermissionsItem]]):
        public_incident_permissions (Union[Unset, list[IncidentPermissionSetPublicIncidentPermissionsItem]]):
    """

    name: str
    created_at: str
    updated_at: str
    slug: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    private_incident_permissions: Union[Unset, list[IncidentPermissionSetPrivateIncidentPermissionsItem]] = UNSET
    public_incident_permissions: Union[Unset, list[IncidentPermissionSetPublicIncidentPermissionsItem]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        created_at = self.created_at

        updated_at = self.updated_at

        slug = self.slug

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        private_incident_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.private_incident_permissions, Unset):
            private_incident_permissions = []
            for private_incident_permissions_item_data in self.private_incident_permissions:
                private_incident_permissions_item: str = private_incident_permissions_item_data
                private_incident_permissions.append(private_incident_permissions_item)

        public_incident_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.public_incident_permissions, Unset):
            public_incident_permissions = []
            for public_incident_permissions_item_data in self.public_incident_permissions:
                public_incident_permissions_item: str = public_incident_permissions_item_data
                public_incident_permissions.append(public_incident_permissions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if description is not UNSET:
            field_dict["description"] = description
        if private_incident_permissions is not UNSET:
            field_dict["private_incident_permissions"] = private_incident_permissions
        if public_incident_permissions is not UNSET:
            field_dict["public_incident_permissions"] = public_incident_permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        slug = d.pop("slug", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        private_incident_permissions = []
        _private_incident_permissions = d.pop("private_incident_permissions", UNSET)
        for private_incident_permissions_item_data in _private_incident_permissions or []:
            private_incident_permissions_item = check_incident_permission_set_private_incident_permissions_item(
                private_incident_permissions_item_data
            )

            private_incident_permissions.append(private_incident_permissions_item)

        public_incident_permissions = []
        _public_incident_permissions = d.pop("public_incident_permissions", UNSET)
        for public_incident_permissions_item_data in _public_incident_permissions or []:
            public_incident_permissions_item = check_incident_permission_set_public_incident_permissions_item(
                public_incident_permissions_item_data
            )

            public_incident_permissions.append(public_incident_permissions_item)

        incident_permission_set = cls(
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            slug=slug,
            description=description,
            private_incident_permissions=private_incident_permissions,
            public_incident_permissions=public_incident_permissions,
        )

        incident_permission_set.additional_properties = d
        return incident_permission_set

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
