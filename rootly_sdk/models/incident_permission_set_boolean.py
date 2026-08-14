from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_permission_set_boolean_kind import (
    IncidentPermissionSetBooleanKind,
    check_incident_permission_set_boolean_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentPermissionSetBoolean")


@_attrs_define
class IncidentPermissionSetBoolean:
    """
    Attributes:
        kind (IncidentPermissionSetBooleanKind):
        created_at (str):
        updated_at (str):
        incident_permission_set_id (Union[Unset, str]):
        private (Union[Unset, bool]):
        enabled (Union[Unset, bool]):
    """

    kind: IncidentPermissionSetBooleanKind
    created_at: str
    updated_at: str
    incident_permission_set_id: Unset | str = UNSET
    private: Unset | bool = UNSET
    enabled: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        created_at = self.created_at

        updated_at = self.updated_at

        incident_permission_set_id = self.incident_permission_set_id

        private = self.private

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if incident_permission_set_id is not UNSET:
            field_dict["incident_permission_set_id"] = incident_permission_set_id
        if private is not UNSET:
            field_dict["private"] = private
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = check_incident_permission_set_boolean_kind(d.pop("kind"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        incident_permission_set_id = d.pop("incident_permission_set_id", UNSET)

        private = d.pop("private", UNSET)

        enabled = d.pop("enabled", UNSET)

        incident_permission_set_boolean = cls(
            kind=kind,
            created_at=created_at,
            updated_at=updated_at,
            incident_permission_set_id=incident_permission_set_id,
            private=private,
            enabled=enabled,
        )

        incident_permission_set_boolean.additional_properties = d
        return incident_permission_set_boolean

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
