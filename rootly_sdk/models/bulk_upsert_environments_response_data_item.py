from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_upsert_environments_response_data_item_type import (
    BulkUpsertEnvironmentsResponseDataItemType,
    check_bulk_upsert_environments_response_data_item_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.environment import Environment


T = TypeVar("T", bound="BulkUpsertEnvironmentsResponseDataItem")


@_attrs_define
class BulkUpsertEnvironmentsResponseDataItem:
    """
    Attributes:
        id (Union[Unset, str]):
        type_ (Union[Unset, BulkUpsertEnvironmentsResponseDataItemType]):
        attributes (Union[Unset, Environment]):
    """

    id: Union[Unset, str] = UNSET
    type_: Union[Unset, BulkUpsertEnvironmentsResponseDataItemType] = UNSET
    attributes: Union[Unset, "Environment"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        attributes: Union[Unset, dict[str, Any]] = UNSET
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
        from ..models.environment import Environment

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, BulkUpsertEnvironmentsResponseDataItemType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_bulk_upsert_environments_response_data_item_type(_type_)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, Environment]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = Environment.from_dict(_attributes)

        bulk_upsert_environments_response_data_item = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )

        bulk_upsert_environments_response_data_item.additional_properties = d
        return bulk_upsert_environments_response_data_item

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
