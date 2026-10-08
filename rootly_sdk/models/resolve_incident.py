from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.resolve_incident_data import ResolveIncidentData


T = TypeVar("T", bound="ResolveIncident")


@_attrs_define
class ResolveIncident:
    """
    Attributes:
        data (ResolveIncidentData):
    """

    data: ResolveIncidentData

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
        from ..models.resolve_incident_data import ResolveIncidentData

        d = dict(src_dict)
        data = ResolveIncidentData.from_dict(d.pop("data"))

        resolve_incident = cls(
            data=data,
        )

        return resolve_incident
