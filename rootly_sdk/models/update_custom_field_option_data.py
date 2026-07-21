from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_custom_field_option_data_type import check_update_custom_field_option_data_type
from ..models.update_custom_field_option_data_type import UpdateCustomFieldOptionDataType
from typing import cast

if TYPE_CHECKING:
    from ..models.update_custom_field_option_data_attributes import UpdateCustomFieldOptionDataAttributes


T = TypeVar("T", bound="UpdateCustomFieldOptionData")


@_attrs_define
class UpdateCustomFieldOptionData:
    """
    Attributes:
        type_ (UpdateCustomFieldOptionDataType):
        attributes (UpdateCustomFieldOptionDataAttributes):
    """

    type_: UpdateCustomFieldOptionDataType
    attributes: UpdateCustomFieldOptionDataAttributes
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_custom_field_option_data_attributes import UpdateCustomFieldOptionDataAttributes

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
        from ..models.update_custom_field_option_data_attributes import UpdateCustomFieldOptionDataAttributes

        d = dict(src_dict)
        type_ = check_update_custom_field_option_data_type(d.pop("type"))

        attributes = UpdateCustomFieldOptionDataAttributes.from_dict(d.pop("attributes"))

        update_custom_field_option_data = cls(
            type_=type_,
            attributes=attributes,
        )

        update_custom_field_option_data.additional_properties = d
        return update_custom_field_option_data

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
