from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.add_subscribers_data_type import AddSubscribersDataType, check_add_subscribers_data_type

if TYPE_CHECKING:
    from ..models.add_subscribers_data_attributes import AddSubscribersDataAttributes


T = TypeVar("T", bound="AddSubscribersData")


@_attrs_define
class AddSubscribersData:
    """
    Attributes:
        type_ (AddSubscribersDataType):
        attributes (AddSubscribersDataAttributes):
    """

    type_: AddSubscribersDataType
    attributes: "AddSubscribersDataAttributes"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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
        from ..models.add_subscribers_data_attributes import AddSubscribersDataAttributes

        d = dict(src_dict)
        type_ = check_add_subscribers_data_type(d.pop("type"))

        attributes = AddSubscribersDataAttributes.from_dict(d.pop("attributes"))

        add_subscribers_data = cls(
            type_=type_,
            attributes=attributes,
        )

        add_subscribers_data.additional_properties = d
        return add_subscribers_data

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
