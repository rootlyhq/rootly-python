from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.shift_override_response_data_type import (
    ShiftOverrideResponseDataType,
    check_shift_override_response_data_type,
)

if TYPE_CHECKING:
    from ..models.shift_override import ShiftOverride


T = TypeVar("T", bound="ShiftOverrideResponseData")


@_attrs_define
class ShiftOverrideResponseData:
    """
    Attributes:
        id (str): Unique ID of the shift override
        type_ (ShiftOverrideResponseDataType):
        attributes (ShiftOverride):
    """

    id: str
    type_: ShiftOverrideResponseDataType
    attributes: "ShiftOverride"
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
        from ..models.shift_override import ShiftOverride

        d = dict(src_dict)
        id = d.pop("id")

        type_ = check_shift_override_response_data_type(d.pop("type"))

        attributes = ShiftOverride.from_dict(d.pop("attributes"))

        shift_override_response_data = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )

        shift_override_response_data.additional_properties = d
        return shift_override_response_data

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
