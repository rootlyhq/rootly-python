from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_feedback_response_data_type import (
    IncidentFeedbackResponseDataType,
    check_incident_feedback_response_data_type,
)

if TYPE_CHECKING:
    from ..models.incident_feedback import IncidentFeedback


T = TypeVar("T", bound="IncidentFeedbackResponseData")


@_attrs_define
class IncidentFeedbackResponseData:
    """
    Attributes:
        id (str): Unique ID of the incident feedback
        type_ (IncidentFeedbackResponseDataType):
        attributes (IncidentFeedback):
    """

    id: str
    type_: IncidentFeedbackResponseDataType
    attributes: "IncidentFeedback"
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
        from ..models.incident_feedback import IncidentFeedback

        d = dict(src_dict)
        id = d.pop("id")

        type_ = check_incident_feedback_response_data_type(d.pop("type"))

        attributes = IncidentFeedback.from_dict(d.pop("attributes"))

        incident_feedback_response_data = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )

        incident_feedback_response_data.additional_properties = d
        return incident_feedback_response_data

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
