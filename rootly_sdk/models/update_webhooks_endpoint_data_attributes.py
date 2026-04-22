from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.update_webhooks_endpoint_data_attributes_event_types_item import (
    UpdateWebhooksEndpointDataAttributesEventTypesItem,
    check_update_webhooks_endpoint_data_attributes_event_types_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWebhooksEndpointDataAttributes")


@_attrs_define
class UpdateWebhooksEndpointDataAttributes:
    """
    Attributes:
        name (str | Unset): The name of the endpoint
        event_types (list[UpdateWebhooksEndpointDataAttributesEventTypesItem] | Unset):
        enabled (bool | Unset):
    """

    name: str | Unset = UNSET
    event_types: list[UpdateWebhooksEndpointDataAttributesEventTypesItem] | Unset = UNSET
    enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        event_types: list[str] | Unset = UNSET
        if not isinstance(self.event_types, Unset):
            event_types = []
            for event_types_item_data in self.event_types:
                event_types_item: str = event_types_item_data
                event_types.append(event_types_item)

        enabled = self.enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if event_types is not UNSET:
            field_dict["event_types"] = event_types
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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

        update_webhooks_endpoint_data_attributes = cls(
            name=name,
            event_types=event_types,
            enabled=enabled,
        )

        return update_webhooks_endpoint_data_attributes
