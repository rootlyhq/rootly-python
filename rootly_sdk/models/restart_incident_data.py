from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.restart_incident_data_type import RestartIncidentDataType, check_restart_incident_data_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.restart_incident_data_attributes import RestartIncidentDataAttributes


T = TypeVar("T", bound="RestartIncidentData")


@_attrs_define
class RestartIncidentData:
    """
    Attributes:
        type_ (RestartIncidentDataType):
        id (str | Unset): Accepted for JSON:API client compatibility, but ignored. The resource to update is identified
            by the id in the path.
        attributes (RestartIncidentDataAttributes | Unset):
    """

    type_: RestartIncidentDataType
    id: str | Unset = UNSET
    attributes: RestartIncidentDataAttributes | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        id = self.id

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.restart_incident_data_attributes import RestartIncidentDataAttributes

        d = dict(src_dict)
        type_ = check_restart_incident_data_type(d.pop("type"))

        id = d.pop("id", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: RestartIncidentDataAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = RestartIncidentDataAttributes.from_dict(_attributes)

        restart_incident_data = cls(
            type_=type_,
            id=id,
            attributes=attributes,
        )

        return restart_incident_data
