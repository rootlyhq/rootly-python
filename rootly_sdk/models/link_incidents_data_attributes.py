from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkIncidentsDataAttributes")


@_attrs_define
class LinkIncidentsDataAttributes:
    """
    Attributes:
        incident_id (str | Unset): ID of a single incident to link
        incident_ids (list[str] | Unset): IDs of incidents to link
    """

    incident_id: str | Unset = UNSET
    incident_ids: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        incident_id = self.incident_id

        incident_ids: list[str] | Unset = UNSET
        if not isinstance(self.incident_ids, Unset):
            incident_ids = self.incident_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if incident_id is not UNSET:
            field_dict["incident_id"] = incident_id
        if incident_ids is not UNSET:
            field_dict["incident_ids"] = incident_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        incident_id = d.pop("incident_id", UNSET)

        incident_ids = cast(list[str], d.pop("incident_ids", UNSET))

        link_incidents_data_attributes = cls(
            incident_id=incident_id,
            incident_ids=incident_ids,
        )

        return link_incidents_data_attributes
