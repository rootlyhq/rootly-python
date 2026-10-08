from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateServiceDataAttributesIncidentBroadcastChannelType0")


@_attrs_define
class UpdateServiceDataAttributesIncidentBroadcastChannelType0:
    """Slack channel to broadcast incidents to

    Attributes:
        id (str): Slack channel ID
        name (str | Unset): Slack channel name
    """

    id: str
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name", UNSET)

        update_service_data_attributes_incident_broadcast_channel_type_0 = cls(
            id=id,
            name=name,
        )

        return update_service_data_attributes_incident_broadcast_channel_type_0
