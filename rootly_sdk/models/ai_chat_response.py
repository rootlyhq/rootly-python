from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_chat_response_data import AiChatResponseData
    from ..models.jsonapi_included_resource import JsonapiIncludedResource


T = TypeVar("T", bound="AiChatResponse")


@_attrs_define
class AiChatResponse:
    """
    Attributes:
        data (AiChatResponseData):
        included (list[JsonapiIncludedResource] | Unset):
    """

    data: AiChatResponseData
    included: list[JsonapiIncludedResource] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

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
        from ..models.ai_chat_response_data import AiChatResponseData
        from ..models.jsonapi_included_resource import JsonapiIncludedResource

        d = dict(src_dict)
        data = AiChatResponseData.from_dict(d.pop("data"))

        _included = d.pop("included", UNSET)
        included: list[JsonapiIncludedResource] | Unset = UNSET
        if _included is not UNSET:
            included = []
            for included_item_data in _included:
                included_item = JsonapiIncludedResource.from_dict(included_item_data)

                included.append(included_item)

        ai_chat_response = cls(
            data=data,
            included=included,
        )

        ai_chat_response.additional_properties = d
        return ai_chat_response

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
