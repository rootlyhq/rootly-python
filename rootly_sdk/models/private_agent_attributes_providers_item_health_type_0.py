from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrivateAgentAttributesProvidersItemHealthType0")


@_attrs_define
class PrivateAgentAttributesProvidersItemHealthType0:
    """Last reported provider health; may be stale when the agent is offline. Invalid or absent fields are omitted.

    Attributes:
        status (str | Unset):
        observed_at (str | Unset):
        message (str | Unset):
    """

    status: str | Unset = UNSET
    observed_at: str | Unset = UNSET
    message: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        observed_at = self.observed_at

        message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if observed_at is not UNSET:
            field_dict["observed_at"] = observed_at
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status", UNSET)

        observed_at = d.pop("observed_at", UNSET)

        message = d.pop("message", UNSET)

        private_agent_attributes_providers_item_health_type_0 = cls(
            status=status,
            observed_at=observed_at,
            message=message,
        )

        return private_agent_attributes_providers_item_health_type_0
