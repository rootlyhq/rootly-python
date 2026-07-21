from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.new_incident_data_type import check_new_incident_data_type
from ..models.new_incident_data_type import NewIncidentDataType
from typing import cast

if TYPE_CHECKING:
    from ..models.new_incident_data_attributes import NewIncidentDataAttributes


T = TypeVar("T", bound="NewIncidentData")


@_attrs_define
class NewIncidentData:
    """
    Attributes:
        type_ (NewIncidentDataType):
        attributes (NewIncidentDataAttributes):
    """

    type_: NewIncidentDataType
    attributes: NewIncidentDataAttributes
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.new_incident_data_attributes import NewIncidentDataAttributes

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
        from ..models.new_incident_data_attributes import NewIncidentDataAttributes

        d = dict(src_dict)
        type_ = check_new_incident_data_type(d.pop("type"))

        attributes = NewIncidentDataAttributes.from_dict(d.pop("attributes"))

        new_incident_data = cls(
            type_=type_,
            attributes=attributes,
        )

        new_incident_data.additional_properties = d
        return new_incident_data

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
