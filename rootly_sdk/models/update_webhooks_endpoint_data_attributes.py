from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_webhooks_endpoint_data_attributes_event_types_item import (
    UpdateWebhooksEndpointDataAttributesEventTypesItem,
    check_update_webhooks_endpoint_data_attributes_event_types_item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_webhooks_endpoint_data_attributes_custom_headers_item import (
        UpdateWebhooksEndpointDataAttributesCustomHeadersItem,
    )


T = TypeVar("T", bound="UpdateWebhooksEndpointDataAttributes")


@_attrs_define
class UpdateWebhooksEndpointDataAttributes:
    """
    Attributes:
        slug (None | str | Unset): Deprecated. `slug` is derived from `name`; any submitted value is ignored. This
            property will be removed from the request schema in a future version.
        name (str | Unset): The name of the endpoint
        event_types (list[UpdateWebhooksEndpointDataAttributesEventTypesItem] | Unset):
        enabled (bool | Unset):
        custom_headers (list[UpdateWebhooksEndpointDataAttributesCustomHeadersItem] | Unset): Custom HTTP headers sent
            with each delivery. Max 10. Reserved names (Content-Type, X-Rootly-Signature, Host, etc.) are rejected.
    """

    slug: None | str | Unset = UNSET
    name: str | Unset = UNSET
    event_types: list[UpdateWebhooksEndpointDataAttributesEventTypesItem] | Unset = UNSET
    enabled: bool | Unset = UNSET
    custom_headers: list[UpdateWebhooksEndpointDataAttributesCustomHeadersItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        name = self.name

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

        field_dict.update({})
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
        if event_types is not UNSET:
            field_dict["event_types"] = event_types
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if custom_headers is not UNSET:
            field_dict["custom_headers"] = custom_headers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_webhooks_endpoint_data_attributes_custom_headers_item import (
            UpdateWebhooksEndpointDataAttributesCustomHeadersItem,
        )

        d = dict(src_dict)

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        name = d.pop("name", UNSET)

        _event_types = d.pop("event_types", UNSET)
        event_types: list[UpdateWebhooksEndpointDataAttributesEventTypesItem] | Unset = UNSET
        if _event_types is not UNSET:
            event_types = []
            for event_types_item_data in _event_types:
                event_types_item = check_update_webhooks_endpoint_data_attributes_event_types_item(
                    event_types_item_data
                )

                event_types.append(event_types_item)

        enabled = d.pop("enabled", UNSET)

        _custom_headers = d.pop("custom_headers", UNSET)
        custom_headers: list[UpdateWebhooksEndpointDataAttributesCustomHeadersItem] | Unset = UNSET
        if _custom_headers is not UNSET:
            custom_headers = []
            for custom_headers_item_data in _custom_headers:
                custom_headers_item = UpdateWebhooksEndpointDataAttributesCustomHeadersItem.from_dict(
                    custom_headers_item_data
                )

                custom_headers.append(custom_headers_item)

        update_webhooks_endpoint_data_attributes = cls(
            slug=slug,
            name=name,
            event_types=event_types,
            enabled=enabled,
            custom_headers=custom_headers,
        )

        return update_webhooks_endpoint_data_attributes
