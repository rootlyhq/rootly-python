from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="NewWebhooksEndpointDataAttributesCustomHeadersItem")


@_attrs_define
class NewWebhooksEndpointDataAttributesCustomHeadersItem:
    """
    Attributes:
        name (str):
        value (str):
    """

    name: str
    value: str

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        value = d.pop("value")

        new_webhooks_endpoint_data_attributes_custom_headers_item = cls(
            name=name,
            value=value,
        )

        return new_webhooks_endpoint_data_attributes_custom_headers_item
