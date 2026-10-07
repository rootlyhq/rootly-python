from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhooks_delivery_status import WebhooksDeliveryStatus, check_webhooks_delivery_status

T = TypeVar("T", bound="WebhooksDelivery")


@_attrs_define
class WebhooksDelivery:
    """
    Attributes:
        endpoint_id (str):
        payload (str):
        status (WebhooksDeliveryStatus): Delivery status
        response_status (int | None): HTTP status code recorded for the delivery attempt. It is null before the first
            attempt. For SSRF and transport failures, Rootly generates this code because no destination response was
            received.
        delivered_at (None | str):
        created_at (str): Date of creation
        updated_at (str): Date of last update
    """

    endpoint_id: str
    payload: str
    status: WebhooksDeliveryStatus
    response_status: int | None
    delivered_at: None | str
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        endpoint_id = self.endpoint_id

        payload = self.payload

        status: str = self.status

        response_status: int | None
        response_status = self.response_status

        delivered_at: None | str
        delivered_at = self.delivered_at

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpoint_id": endpoint_id,
                "payload": payload,
                "status": status,
                "response_status": response_status,
                "delivered_at": delivered_at,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        endpoint_id = d.pop("endpoint_id")

        payload = d.pop("payload")

        status = check_webhooks_delivery_status(d.pop("status"))

        def _parse_response_status(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        response_status = _parse_response_status(d.pop("response_status"))

        def _parse_delivered_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        delivered_at = _parse_delivered_at(d.pop("delivered_at"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        webhooks_delivery = cls(
            endpoint_id=endpoint_id,
            payload=payload,
            status=status,
            response_status=response_status,
            delivered_at=delivered_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        webhooks_delivery.additional_properties = d
        return webhooks_delivery

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
