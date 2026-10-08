from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_incident_event_service_data import UpdateIncidentEventServiceData


T = TypeVar("T", bound="UpdateIncidentEventService")


@_attrs_define
class UpdateIncidentEventService:
    """
    Attributes:
        data (UpdateIncidentEventServiceData):
    """

    data: UpdateIncidentEventServiceData

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
        from ..models.update_incident_event_service_data import UpdateIncidentEventServiceData

        d = dict(src_dict)
        data = UpdateIncidentEventServiceData.from_dict(d.pop("data"))

        update_incident_event_service = cls(
            data=data,
        )

        return update_incident_event_service
