from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_custom_field_selection_response_data_type import (
    IncidentCustomFieldSelectionResponseDataType,
    check_incident_custom_field_selection_response_data_type,
)

if TYPE_CHECKING:
    from ..models.incident_custom_field_selection import IncidentCustomFieldSelection


T = TypeVar("T", bound="IncidentCustomFieldSelectionResponseData")


@_attrs_define
class IncidentCustomFieldSelectionResponseData:
    """
    Attributes:
        id (str): Unique ID of the incident_custom_field_selection
        type_ (IncidentCustomFieldSelectionResponseDataType):
        attributes (IncidentCustomFieldSelection):
    """

    id: str
    type_: IncidentCustomFieldSelectionResponseDataType
    attributes: "IncidentCustomFieldSelection"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: str = self.type_

        attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.incident_custom_field_selection import IncidentCustomFieldSelection

        d = dict(src_dict)
        id = d.pop("id")

        type_ = check_incident_custom_field_selection_response_data_type(d.pop("type"))

        attributes = IncidentCustomFieldSelection.from_dict(d.pop("attributes"))

        incident_custom_field_selection_response_data = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )

        incident_custom_field_selection_response_data.additional_properties = d
        return incident_custom_field_selection_response_data

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
