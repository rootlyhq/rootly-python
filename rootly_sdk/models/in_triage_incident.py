from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.in_triage_incident_data import InTriageIncidentData


T = TypeVar("T", bound="InTriageIncident")


@_attrs_define
class InTriageIncident:
    """
    Attributes:
        data (InTriageIncidentData):
    """

    data: InTriageIncidentData

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
        from ..models.in_triage_incident_data import InTriageIncidentData

        d = dict(src_dict)
        data = InTriageIncidentData.from_dict(d.pop("data"))

        in_triage_incident = cls(
            data=data,
        )

        return in_triage_incident
