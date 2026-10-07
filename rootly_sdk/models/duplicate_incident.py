from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.duplicate_incident_data import DuplicateIncidentData


T = TypeVar("T", bound="DuplicateIncident")


@_attrs_define
class DuplicateIncident:
    """
    Attributes:
        data (DuplicateIncidentData):
    """

    data: DuplicateIncidentData

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
        from ..models.duplicate_incident_data import DuplicateIncidentData

        d = dict(src_dict)
        data = DuplicateIncidentData.from_dict(d.pop("data"))

        duplicate_incident = cls(
            data=data,
        )

        return duplicate_incident
