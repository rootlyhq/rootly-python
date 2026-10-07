from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_incident_role_data import NewIncidentRoleData


T = TypeVar("T", bound="NewIncidentRole")


@_attrs_define
class NewIncidentRole:
    """
    Attributes:
        data (NewIncidentRoleData):
    """

    data: NewIncidentRoleData

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
        from ..models.new_incident_role_data import NewIncidentRoleData

        d = dict(src_dict)
        data = NewIncidentRoleData.from_dict(d.pop("data"))

        new_incident_role = cls(
            data=data,
        )

        return new_incident_role
