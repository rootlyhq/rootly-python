from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_environment_data_type import NewEnvironmentDataType, check_new_environment_data_type

if TYPE_CHECKING:
    from ..models.new_environment_data_attributes import NewEnvironmentDataAttributes


T = TypeVar("T", bound="NewEnvironmentData")


@_attrs_define
class NewEnvironmentData:
    """
    Attributes:
        type_ (NewEnvironmentDataType):
        attributes (NewEnvironmentDataAttributes):
    """

    type_: NewEnvironmentDataType
    attributes: "NewEnvironmentDataAttributes"
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
        from ..models.new_environment_data_attributes import NewEnvironmentDataAttributes

        d = dict(src_dict)
        type_ = check_new_environment_data_type(d.pop("type"))

        attributes = NewEnvironmentDataAttributes.from_dict(d.pop("attributes"))

        new_environment_data = cls(
            type_=type_,
            attributes=attributes,
        )

        new_environment_data.additional_properties = d
        return new_environment_data

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
