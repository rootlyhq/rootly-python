from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_urgency_response_data_type import (
    AlertUrgencyResponseDataType,
    check_alert_urgency_response_data_type,
)

if TYPE_CHECKING:
    from ..models.alert_urgency import AlertUrgency


T = TypeVar("T", bound="AlertUrgencyResponseData")


@_attrs_define
class AlertUrgencyResponseData:
    """
    Attributes:
        id (str): Unique ID of the alert urgency
        type_ (AlertUrgencyResponseDataType):
        attributes (AlertUrgency):
    """

    id: str
    type_: AlertUrgencyResponseDataType
    attributes: "AlertUrgency"
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
        from ..models.alert_urgency import AlertUrgency

        d = dict(src_dict)
        id = d.pop("id")

        type_ = check_alert_urgency_response_data_type(d.pop("type"))

        attributes = AlertUrgency.from_dict(d.pop("attributes"))

        alert_urgency_response_data = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )

        alert_urgency_response_data.additional_properties = d
        return alert_urgency_response_data

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
