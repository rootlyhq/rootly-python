from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_response_data_type import ServiceResponseDataType, check_service_response_data_type

if TYPE_CHECKING:
    from ..models.service import Service


T = TypeVar("T", bound="ServiceResponseData")


@_attrs_define
class ServiceResponseData:
    """
    Attributes:
        id (str): Unique ID of the service
        type_ (ServiceResponseDataType):
        attributes (Service):
    """

    id: str
    type_: ServiceResponseDataType
    attributes: "Service"
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
        from ..models.service import Service

        d = dict(src_dict)
        id = d.pop("id")

        type_ = check_service_response_data_type(d.pop("type"))

        attributes = Service.from_dict(d.pop("attributes"))

        service_response_data = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )

        service_response_data.additional_properties = d
        return service_response_data

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
