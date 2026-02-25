from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhooks_endpoint_event_types_item import (
    WebhooksEndpointEventTypesItem,
    check_webhooks_endpoint_event_types_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhooksEndpoint")


@_attrs_define
class WebhooksEndpoint:
    """
    Attributes:
        name (str): The name of the endpoint
        url (str): The URL of the endpoint.
        event_types (list[WebhooksEndpointEventTypesItem]):
        secret (str): The webhook signing secret used to verify webhook requests.
        enabled (bool):
        created_at (str): Date of creation
        updated_at (str): Date of last update
        slug (Union[Unset, str]): The slug of the endpoint
    """

    name: str
    url: str
    event_types: list[WebhooksEndpointEventTypesItem]
    secret: str
    enabled: bool
    created_at: str
    updated_at: str
    slug: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        url = self.url

        event_types = []
        for event_types_item_data in self.event_types:
            event_types_item: str = event_types_item_data
            event_types.append(event_types_item)

        secret = self.secret

        enabled = self.enabled

        created_at = self.created_at

        updated_at = self.updated_at

        slug = self.slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "url": url,
                "event_types": event_types,
                "secret": secret,
                "enabled": enabled,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        url = d.pop("url")

        event_types = []
        _event_types = d.pop("event_types")
        for event_types_item_data in _event_types:
            event_types_item = check_webhooks_endpoint_event_types_item(event_types_item_data)

            event_types.append(event_types_item)

        secret = d.pop("secret")

        enabled = d.pop("enabled")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        slug = d.pop("slug", UNSET)

        webhooks_endpoint = cls(
            name=name,
            url=url,
            event_types=event_types,
            secret=secret,
            enabled=enabled,
            created_at=created_at,
            updated_at=updated_at,
            slug=slug,
        )

        webhooks_endpoint.additional_properties = d
        return webhooks_endpoint

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
