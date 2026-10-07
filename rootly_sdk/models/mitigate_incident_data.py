from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.mitigate_incident_data_type import MitigateIncidentDataType, check_mitigate_incident_data_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mitigate_incident_data_attributes import MitigateIncidentDataAttributes


T = TypeVar("T", bound="MitigateIncidentData")


@_attrs_define
class MitigateIncidentData:
    """
    Attributes:
        type_ (MitigateIncidentDataType):
        attributes (MitigateIncidentDataAttributes):
        id (str | Unset): Accepted for JSON:API client compatibility, but ignored. The resource to update is identified
            by the id in the path.
    """

    type_: MitigateIncidentDataType
    attributes: MitigateIncidentDataAttributes
    id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        attributes = self.attributes.to_dict()

        id = self.id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "attributes": attributes,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mitigate_incident_data_attributes import MitigateIncidentDataAttributes

        d = dict(src_dict)
        type_ = check_mitigate_incident_data_type(d.pop("type"))

        attributes = MitigateIncidentDataAttributes.from_dict(d.pop("attributes"))

        id = d.pop("id", UNSET)

        mitigate_incident_data = cls(
            type_=type_,
            attributes=attributes,
            id=id,
        )

        return mitigate_incident_data
