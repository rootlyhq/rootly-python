from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.update_incident_permission_set_data_attributes_private_incident_permissions_item import (
    UpdateIncidentPermissionSetDataAttributesPrivateIncidentPermissionsItem,
    check_update_incident_permission_set_data_attributes_private_incident_permissions_item,
)
from ..models.update_incident_permission_set_data_attributes_public_incident_permissions_item import (
    UpdateIncidentPermissionSetDataAttributesPublicIncidentPermissionsItem,
    check_update_incident_permission_set_data_attributes_public_incident_permissions_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateIncidentPermissionSetDataAttributes")


@_attrs_define
class UpdateIncidentPermissionSetDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The incident permission set name.
        description (Union[None, Unset, str]): The incident permission set description.
        private_incident_permissions (Union[Unset,
            list[UpdateIncidentPermissionSetDataAttributesPrivateIncidentPermissionsItem]]):
        public_incident_permissions (Union[Unset,
            list[UpdateIncidentPermissionSetDataAttributesPublicIncidentPermissionsItem]]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    private_incident_permissions: Union[
        Unset, list[UpdateIncidentPermissionSetDataAttributesPrivateIncidentPermissionsItem]
    ] = UNSET
    public_incident_permissions: Union[
        Unset, list[UpdateIncidentPermissionSetDataAttributesPublicIncidentPermissionsItem]
    ] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

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

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
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
        name = d.pop("name", UNSET)

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
            private_incident_permissions_item = (
                check_update_incident_permission_set_data_attributes_private_incident_permissions_item(
                    private_incident_permissions_item_data
                )
            )

            private_incident_permissions.append(private_incident_permissions_item)

        public_incident_permissions = []
        _public_incident_permissions = d.pop("public_incident_permissions", UNSET)
        for public_incident_permissions_item_data in _public_incident_permissions or []:
            public_incident_permissions_item = (
                check_update_incident_permission_set_data_attributes_public_incident_permissions_item(
                    public_incident_permissions_item_data
                )
            )

            public_incident_permissions.append(public_incident_permissions_item)

        update_incident_permission_set_data_attributes = cls(
            name=name,
            description=description,
            private_incident_permissions=private_incident_permissions,
            public_incident_permissions=public_incident_permissions,
        )

        return update_incident_permission_set_data_attributes
