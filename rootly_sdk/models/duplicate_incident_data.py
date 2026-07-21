from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.duplicate_incident_data_type import check_duplicate_incident_data_type
from ..models.duplicate_incident_data_type import DuplicateIncidentDataType
from typing import cast

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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.duplicate_incident_data_attributes import DuplicateIncidentDataAttributes

        type_: str = self.type_

        attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        duplicate_incident_data.additional_properties = d
        return duplicate_incident_data

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
