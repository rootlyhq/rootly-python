from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_upsert_services_response_data_item_type import (
    BulkUpsertServicesResponseDataItemType,
    check_bulk_upsert_services_response_data_item_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service import Service


T = TypeVar("T", bound="BulkUpsertServicesResponseDataItem")


@_attrs_define
class BulkUpsertServicesResponseDataItem:
    """
    Attributes:
        id (str | Unset):
        type_ (BulkUpsertServicesResponseDataItemType | Unset):
        attributes (Service | Unset):
    """

    id: str | Unset = UNSET
    type_: BulkUpsertServicesResponseDataItemType | Unset = UNSET
    attributes: Service | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        id = self.id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        attributes: dict[str, Any] | Unset = UNSET
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
        from ..models.service import Service

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: BulkUpsertServicesResponseDataItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_bulk_upsert_services_response_data_item_type(_type_)

        _attributes = d.pop("attributes", UNSET)
        attributes: Service | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = Service.from_dict(_attributes)

        bulk_upsert_services_response_data_item = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )

        bulk_upsert_services_response_data_item.additional_properties = d
        return bulk_upsert_services_response_data_item

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
