from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.new_webhooks_endpoint_data_attributes_event_types_item import (
    NewWebhooksEndpointDataAttributesEventTypesItem,
    check_new_webhooks_endpoint_data_attributes_event_types_item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_webhooks_endpoint_data_attributes_custom_headers_item import (
        NewWebhooksEndpointDataAttributesCustomHeadersItem,
    )


T = TypeVar("T", bound="NewWebhooksEndpointDataAttributes")


@_attrs_define
class NewWebhooksEndpointDataAttributes:
    """
    Attributes:
        name (str): The name of the endpoint
        url (str): The URL of the endpoint.
        secret (str | Unset): The webhook signing secret used to verify webhook requests.
        event_types (list[NewWebhooksEndpointDataAttributesEventTypesItem] | Unset):
        enabled (bool | Unset):
        custom_headers (list[NewWebhooksEndpointDataAttributesCustomHeadersItem] | Unset): Custom HTTP headers sent with
            each delivery. Max 10. Reserved names (Content-Type, X-Rootly-Signature, Host, etc.) are rejected.
    """

    name: str
    url: str
    secret: str | Unset = UNSET
    event_types: list[NewWebhooksEndpointDataAttributesEventTypesItem] | Unset = UNSET
    enabled: bool | Unset = UNSET
    custom_headers: list[NewWebhooksEndpointDataAttributesCustomHeadersItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:

        name = self.name

        url = self.url

        secret = self.secret

        event_types: list[str] | Unset = UNSET
        if not isinstance(self.event_types, Unset):
            event_types = []
            for event_types_item_data in self.event_types:
                event_types_item: str = event_types_item_data
                event_types.append(event_types_item)

        enabled = self.enabled

        custom_headers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_headers, Unset):
            custom_headers = []
            for custom_headers_item_data in self.custom_headers:
                custom_headers_item = custom_headers_item_data.to_dict()
                custom_headers.append(custom_headers_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "url": url,
            }
        )
        if secret is not UNSET:
            field_dict["secret"] = secret
        if event_types is not UNSET:
            field_dict["event_types"] = event_types
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if custom_headers is not UNSET:
            field_dict["custom_headers"] = custom_headers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_webhooks_endpoint_data_attributes_custom_headers_item import (
            NewWebhooksEndpointDataAttributesCustomHeadersItem,
        )

        d = dict(src_dict)
        name = d.pop("name")

        url = d.pop("url")

        secret = d.pop("secret", UNSET)

        _event_types = d.pop("event_types", UNSET)
        event_types: list[NewWebhooksEndpointDataAttributesEventTypesItem] | Unset = UNSET
        if _event_types is not UNSET:
            event_types = []
            for event_types_item_data in _event_types:
                event_types_item = check_new_webhooks_endpoint_data_attributes_event_types_item(event_types_item_data)

                event_types.append(event_types_item)

        enabled = d.pop("enabled", UNSET)

        _custom_headers = d.pop("custom_headers", UNSET)
        custom_headers: list[NewWebhooksEndpointDataAttributesCustomHeadersItem] | Unset = UNSET
        if _custom_headers is not UNSET:
            custom_headers = []
            for custom_headers_item_data in _custom_headers:
                custom_headers_item = NewWebhooksEndpointDataAttributesCustomHeadersItem.from_dict(
                    custom_headers_item_data
                )

                custom_headers.append(custom_headers_item)

        new_webhooks_endpoint_data_attributes = cls(
            name=name,
            url=url,
            secret=secret,
            event_types=event_types,
            enabled=enabled,
            custom_headers=custom_headers,
        )

        return new_webhooks_endpoint_data_attributes
