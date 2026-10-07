from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_incident_role_data import UpdateIncidentRoleData


T = TypeVar("T", bound="UpdateIncidentRole")


@_attrs_define
class UpdateIncidentRole:
    """
    Attributes:
        data (UpdateIncidentRoleData):
    """

    data: UpdateIncidentRoleData

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
        from ..models.update_incident_role_data import UpdateIncidentRoleData

        d = dict(src_dict)
        data = UpdateIncidentRoleData.from_dict(d.pop("data"))

        update_incident_role = cls(
            data=data,
        )

        return update_incident_role
