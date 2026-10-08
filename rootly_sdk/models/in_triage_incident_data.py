from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.in_triage_incident_data_type import InTriageIncidentDataType, check_in_triage_incident_data_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="InTriageIncidentData")


@_attrs_define
class InTriageIncidentData:
    """
    Attributes:
        type_ (InTriageIncidentDataType):
        id (str | Unset): Accepted for JSON:API client compatibility, but ignored. The resource to update is identified
            by the id in the path.
    """

    type_: InTriageIncidentDataType
    id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        id = self.id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = check_in_triage_incident_data_type(d.pop("type"))

        id = d.pop("id", UNSET)

        in_triage_incident_data = cls(
            type_=type_,
            id=id,
        )

        return in_triage_incident_data
