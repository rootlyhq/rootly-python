from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.restart_incident_data import RestartIncidentData


T = TypeVar("T", bound="RestartIncident")


@_attrs_define
class RestartIncident:
    """
    Attributes:
        data (RestartIncidentData):
    """

    data: RestartIncidentData

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
        from ..models.restart_incident_data import RestartIncidentData

        d = dict(src_dict)
        data = RestartIncidentData.from_dict(d.pop("data"))

        restart_incident = cls(
            data=data,
        )

        return restart_incident
