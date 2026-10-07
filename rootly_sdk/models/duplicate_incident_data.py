from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.duplicate_incident_data_type import DuplicateIncidentDataType, check_duplicate_incident_data_type

if TYPE_CHECKING:
    from ..models.duplicate_incident_data_attributes import DuplicateIncidentDataAttributes


T = TypeVar("T", bound="DuplicateIncidentData")


@_attrs_define
class DuplicateIncidentData:
    """
    Attributes:
        type_ (DuplicateIncidentDataType):
        attributes (DuplicateIncidentDataAttributes):
    """

    type_: DuplicateIncidentDataType
    attributes: DuplicateIncidentDataAttributes

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.duplicate_incident_data_attributes import DuplicateIncidentDataAttributes

        d = dict(src_dict)
        type_ = check_duplicate_incident_data_type(d.pop("type"))

        attributes = DuplicateIncidentDataAttributes.from_dict(d.pop("attributes"))

        duplicate_incident_data = cls(
            type_=type_,
            attributes=attributes,
        )

        return duplicate_incident_data
