from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.mitigate_incident_data import MitigateIncidentData


T = TypeVar("T", bound="MitigateIncident")


@_attrs_define
class MitigateIncident:
    """
    Attributes:
        data (MitigateIncidentData):
    """

    data: MitigateIncidentData

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
        from ..models.mitigate_incident_data import MitigateIncidentData

        d = dict(src_dict)
        data = MitigateIncidentData.from_dict(d.pop("data"))

        mitigate_incident = cls(
            data=data,
        )

        return mitigate_incident
