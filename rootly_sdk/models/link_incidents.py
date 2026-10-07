from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.link_incidents_data import LinkIncidentsData


T = TypeVar("T", bound="LinkIncidents")


@_attrs_define
class LinkIncidents:
    """
    Attributes:
        data (LinkIncidentsData):
    """

    data: LinkIncidentsData

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
        from ..models.link_incidents_data import LinkIncidentsData

        d = dict(src_dict)
        data = LinkIncidentsData.from_dict(d.pop("data"))

        link_incidents = cls(
            data=data,
        )

        return link_incidents
