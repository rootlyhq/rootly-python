from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.new_incident_permission_set_data_attributes_private_incident_permissions_item import (
    NewIncidentPermissionSetDataAttributesPrivateIncidentPermissionsItem,
    check_new_incident_permission_set_data_attributes_private_incident_permissions_item,
)
from ..models.new_incident_permission_set_data_attributes_public_incident_permissions_item import (
    NewIncidentPermissionSetDataAttributesPublicIncidentPermissionsItem,
    check_new_incident_permission_set_data_attributes_public_incident_permissions_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewIncidentPermissionSetDataAttributes")


@_attrs_define
class NewIncidentPermissionSetDataAttributes:
    """
    Attributes:
        name (str): The incident permission set name.
        description (None | str | Unset): The incident permission set description.
        private_incident_permissions (list[NewIncidentPermissionSetDataAttributesPrivateIncidentPermissionsItem] |
            Unset):
        public_incident_permissions (list[NewIncidentPermissionSetDataAttributesPublicIncidentPermissionsItem] | Unset):
    """

    name: str
    description: None | str | Unset = UNSET
    private_incident_permissions: list[NewIncidentPermissionSetDataAttributesPrivateIncidentPermissionsItem] | Unset = (
        UNSET
    )
    public_incident_permissions: list[NewIncidentPermissionSetDataAttributesPublicIncidentPermissionsItem] | Unset = (
        UNSET
    )

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        private_incident_permissions: list[str] | Unset = UNSET
        if not isinstance(self.private_incident_permissions, Unset):
            private_incident_permissions = []
            for private_incident_permissions_item_data in self.private_incident_permissions:
                private_incident_permissions_item: str = private_incident_permissions_item_data
                private_incident_permissions.append(private_incident_permissions_item)

        public_incident_permissions: list[str] | Unset = UNSET
        if not isinstance(self.public_incident_permissions, Unset):
            public_incident_permissions = []
            for public_incident_permissions_item_data in self.public_incident_permissions:
                public_incident_permissions_item: str = public_incident_permissions_item_data
                public_incident_permissions.append(public_incident_permissions_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
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

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _private_incident_permissions = d.pop("private_incident_permissions", UNSET)
        private_incident_permissions: (
            list[NewIncidentPermissionSetDataAttributesPrivateIncidentPermissionsItem] | Unset
        ) = UNSET
        if _private_incident_permissions is not UNSET:
            private_incident_permissions = []
            for private_incident_permissions_item_data in _private_incident_permissions:
                private_incident_permissions_item = (
                    check_new_incident_permission_set_data_attributes_private_incident_permissions_item(
                        private_incident_permissions_item_data
                    )
                )

                private_incident_permissions.append(private_incident_permissions_item)

        _public_incident_permissions = d.pop("public_incident_permissions", UNSET)
        public_incident_permissions: (
            list[NewIncidentPermissionSetDataAttributesPublicIncidentPermissionsItem] | Unset
        ) = UNSET
        if _public_incident_permissions is not UNSET:
            public_incident_permissions = []
            for public_incident_permissions_item_data in _public_incident_permissions:
                public_incident_permissions_item = (
                    check_new_incident_permission_set_data_attributes_public_incident_permissions_item(
                        public_incident_permissions_item_data
                    )
                )

                public_incident_permissions.append(public_incident_permissions_item)

        new_incident_permission_set_data_attributes = cls(
            name=name,
            description=description,
            private_incident_permissions=private_incident_permissions,
            public_incident_permissions=public_incident_permissions,
        )

        return new_incident_permission_set_data_attributes
