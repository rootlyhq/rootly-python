from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.custom_field_response_data import CustomFieldResponseData
    from ..models.jsonapi_included_resource import JsonapiIncludedResource


T = TypeVar("T", bound="CustomFieldResponse")


@_attrs_define
class CustomFieldResponse:
    """
    Attributes:
        data (CustomFieldResponseData):
        included (list[JsonapiIncludedResource] | Unset):
    """

    data: CustomFieldResponseData
    included: list[JsonapiIncludedResource] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_field_response_data import CustomFieldResponseData
        from ..models.jsonapi_included_resource import JsonapiIncludedResource

        data = self.data.to_dict()

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
            }
        )
        if included is not UNSET:
            field_dict["included"] = included

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_field_response_data import CustomFieldResponseData
        from ..models.jsonapi_included_resource import JsonapiIncludedResource

        d = dict(src_dict)
        data = CustomFieldResponseData.from_dict(d.pop("data"))

        _included = d.pop("included", UNSET)
        included: list[JsonapiIncludedResource] | Unset = UNSET
        if _included is not UNSET:
            included = []
            for included_item_data in _included:
                included_item = JsonapiIncludedResource.from_dict(included_item_data)

                included.append(included_item)

        custom_field_response = cls(
            data=data,
            included=included,
        )

        custom_field_response.additional_properties = d
        return custom_field_response

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
