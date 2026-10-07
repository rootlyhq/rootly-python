from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_incident_status_page_event_data import NewIncidentStatusPageEventData


T = TypeVar("T", bound="NewIncidentStatusPageEvent")


@_attrs_define
class NewIncidentStatusPageEvent:
    """
    Attributes:
        data (NewIncidentStatusPageEventData):
    """

    data: NewIncidentStatusPageEventData

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
        from ..models.new_incident_status_page_event_data import NewIncidentStatusPageEventData

        d = dict(src_dict)
        data = NewIncidentStatusPageEventData.from_dict(d.pop("data"))

        new_incident_status_page_event = cls(
            data=data,
        )

        return new_incident_status_page_event
