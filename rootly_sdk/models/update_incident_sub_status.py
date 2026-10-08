from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_incident_sub_status_data import UpdateIncidentSubStatusData


T = TypeVar("T", bound="UpdateIncidentSubStatus")


@_attrs_define
class UpdateIncidentSubStatus:
    """
    Attributes:
        data (UpdateIncidentSubStatusData):
    """

    data: UpdateIncidentSubStatusData

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
        from ..models.update_incident_sub_status_data import UpdateIncidentSubStatusData

        d = dict(src_dict)
        data = UpdateIncidentSubStatusData.from_dict(d.pop("data"))

        update_incident_sub_status = cls(
            data=data,
        )

        return update_incident_sub_status
