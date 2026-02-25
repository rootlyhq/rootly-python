from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_permission_set_resource_kind import (
    IncidentPermissionSetResourceKind,
    check_incident_permission_set_resource_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentPermissionSetResource")


@_attrs_define
class IncidentPermissionSetResource:
    """
    Attributes:
        incident_permission_set_id (str):
        kind (IncidentPermissionSetResourceKind):
        created_at (str):
        updated_at (str):
        private (Union[Unset, bool]):
        resource_id (Union[Unset, str]):
        resource_type (Union[Unset, str]):
    """

    incident_permission_set_id: str
    kind: IncidentPermissionSetResourceKind
    created_at: str
    updated_at: str
    private: Unset | bool = UNSET
    resource_id: Unset | str = UNSET
    resource_type: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_permission_set_id = self.incident_permission_set_id

        kind: str = self.kind

        created_at = self.created_at

        updated_at = self.updated_at

        private = self.private

        resource_id = self.resource_id

        resource_type = self.resource_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_permission_set_id": incident_permission_set_id,
                "kind": kind,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if private is not UNSET:
            field_dict["private"] = private
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
        if resource_type is not UNSET:
            field_dict["resource_type"] = resource_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        incident_permission_set_id = d.pop("incident_permission_set_id")

        kind = check_incident_permission_set_resource_kind(d.pop("kind"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        private = d.pop("private", UNSET)

        resource_id = d.pop("resource_id", UNSET)

        resource_type = d.pop("resource_type", UNSET)

        incident_permission_set_resource = cls(
            incident_permission_set_id=incident_permission_set_id,
            kind=kind,
            created_at=created_at,
            updated_at=updated_at,
            private=private,
            resource_id=resource_id,
            resource_type=resource_type,
        )

        incident_permission_set_resource.additional_properties = d
        return incident_permission_set_resource

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
