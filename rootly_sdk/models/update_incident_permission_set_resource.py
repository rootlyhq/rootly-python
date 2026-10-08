from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_incident_permission_set_resource_data import UpdateIncidentPermissionSetResourceData


T = TypeVar("T", bound="UpdateIncidentPermissionSetResource")


@_attrs_define
class UpdateIncidentPermissionSetResource:
    """
    Attributes:
        data (UpdateIncidentPermissionSetResourceData):
    """

    data: UpdateIncidentPermissionSetResourceData

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_incident_permission_set_resource_data import UpdateIncidentPermissionSetResourceData

        d = dict(src_dict)
        data = UpdateIncidentPermissionSetResourceData.from_dict(d.pop("data"))

        update_incident_permission_set_resource = cls(
            data=data,
        )

        return update_incident_permission_set_resource
