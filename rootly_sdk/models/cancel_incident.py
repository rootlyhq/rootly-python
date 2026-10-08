from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.cancel_incident_data import CancelIncidentData


T = TypeVar("T", bound="CancelIncident")


@_attrs_define
class CancelIncident:
    """
    Attributes:
        data (CancelIncidentData):
    """

    data: CancelIncidentData

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
        from ..models.cancel_incident_data import CancelIncidentData

        d = dict(src_dict)
        data = CancelIncidentData.from_dict(d.pop("data"))

        cancel_incident = cls(
            data=data,
        )

        return cancel_incident
