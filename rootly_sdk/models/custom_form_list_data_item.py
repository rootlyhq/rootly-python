from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.custom_form_list_data_item_type import check_custom_form_list_data_item_type
from ..models.custom_form_list_data_item_type import CustomFormListDataItemType
from typing import cast

if TYPE_CHECKING:
    from ..models.custom_form import CustomForm


T = TypeVar("T", bound="CustomFormListDataItem")


@_attrs_define
class CustomFormListDataItem:
    """
    Attributes:
        id (str): Unique id of the custom form.
        type_ (CustomFormListDataItemType):
        attributes (CustomForm):
    """

    id: str
    type_: CustomFormListDataItemType
    attributes: CustomForm
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_form import CustomForm

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
        from ..models.custom_form import CustomForm

        d = dict(src_dict)
        id = d.pop("id")

        type_ = check_custom_form_list_data_item_type(d.pop("type"))

        attributes = CustomForm.from_dict(d.pop("attributes"))

        custom_form_list_data_item = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )

        custom_form_list_data_item.additional_properties = d
        return custom_form_list_data_item

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
