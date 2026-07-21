from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.jsonapi_included_resource import JsonapiIncludedResource
    from ..models.links import Links
    from ..models.meta import Meta
    from ..models.status_page_list_data_item import StatusPageListDataItem


T = TypeVar("T", bound="StatusPageList")


@_attrs_define
class StatusPageList:
    """
    Attributes:
        data (list[StatusPageListDataItem]):
        links (Links):
        meta (Meta):
        included (list[JsonapiIncludedResource] | Unset):
    """

    data: list[StatusPageListDataItem]
    links: Links
    meta: Meta
    included: list[JsonapiIncludedResource] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.status_page_list_data_item import StatusPageListDataItem
        from ..models.meta import Meta
        from ..models.jsonapi_included_resource import JsonapiIncludedResource
        from ..models.links import Links

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        links = self.links.to_dict()

        meta = self.meta.to_dict()

        included: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.included, Unset):
            included = []
            for included_item_data in self.included:
                included_item = included_item_data.to_dict()
                included.append(included_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "links": links,
                "meta": meta,
            }
        )
        if included is not UNSET:
            field_dict["included"] = included

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jsonapi_included_resource import JsonapiIncludedResource
        from ..models.links import Links
        from ..models.meta import Meta
        from ..models.status_page_list_data_item import StatusPageListDataItem

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = StatusPageListDataItem.from_dict(data_item_data)

            data.append(data_item)

        links = Links.from_dict(d.pop("links"))

        meta = Meta.from_dict(d.pop("meta"))

        _included = d.pop("included", UNSET)
        included: list[JsonapiIncludedResource] | Unset = UNSET
        if _included is not UNSET:
            included = []
            for included_item_data in _included:
                included_item = JsonapiIncludedResource.from_dict(included_item_data)

                included.append(included_item)

        status_page_list = cls(
            data=data,
            links=links,
            meta=meta,
            included=included,
        )

        status_page_list.additional_properties = d
        return status_page_list

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
