from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delete_alert_route_response_200_data_attributes import DeleteAlertRouteResponse200DataAttributes


T = TypeVar("T", bound="DeleteAlertRouteResponse200Data")


@_attrs_define
class DeleteAlertRouteResponse200Data:
    """
    Attributes:
        id (Union[Unset, str]):
        type_ (Union[Unset, str]):
        attributes (Union[Unset, DeleteAlertRouteResponse200DataAttributes]):
    """

    id: Unset | str = UNSET
    type_: Unset | str = UNSET
    attributes: Union[Unset, "DeleteAlertRouteResponse200DataAttributes"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        attributes: Unset | dict[str, Any] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delete_alert_route_response_200_data_attributes import DeleteAlertRouteResponse200DataAttributes

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: Unset | DeleteAlertRouteResponse200DataAttributes
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = DeleteAlertRouteResponse200DataAttributes.from_dict(_attributes)

        delete_alert_route_response_200_data = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )

        delete_alert_route_response_200_data.additional_properties = d
        return delete_alert_route_response_200_data

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
