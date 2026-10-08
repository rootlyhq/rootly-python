from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_webhooks_endpoint_data import NewWebhooksEndpointData


T = TypeVar("T", bound="NewWebhooksEndpoint")


@_attrs_define
class NewWebhooksEndpoint:
    """
    Attributes:
        data (NewWebhooksEndpointData):
    """

    data: NewWebhooksEndpointData

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_webhooks_endpoint_data import NewWebhooksEndpointData

        d = dict(src_dict)
        data = NewWebhooksEndpointData.from_dict(d.pop("data"))

        new_webhooks_endpoint = cls(
            data=data,
        )

        return new_webhooks_endpoint
