from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewAlertGroupDataAttributesAttributesItem")


@_attrs_define
class NewAlertGroupDataAttributesAttributesItem:
    """
    Attributes:
        json_path (Union[Unset, str]): The JSON path to the value to group by.
    """

    json_path: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        json_path = self.json_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if json_path is not UNSET:
            field_dict["json_path"] = json_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        json_path = d.pop("json_path", UNSET)

        new_alert_group_data_attributes_attributes_item = cls(
            json_path=json_path,
        )

        new_alert_group_data_attributes_attributes_item.additional_properties = d
        return new_alert_group_data_attributes_attributes_item

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
