from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="SlackChannel")


@_attrs_define
class SlackChannel:
    """
    Attributes:
        id (str):
        slack_channel_name (str):
        slack_channel_id (str):
        slack_team_id (str):
        created_at (str):
        updated_at (str):
    """

    id: str
    slack_channel_name: str
    slack_channel_id: str
    slack_team_id: str
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        slack_channel_name = self.slack_channel_name

        slack_channel_id = self.slack_channel_id

        slack_team_id = self.slack_team_id

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "slack_channel_name": slack_channel_name,
                "slack_channel_id": slack_channel_id,
                "slack_team_id": slack_team_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        slack_channel_name = d.pop("slack_channel_name")

        slack_channel_id = d.pop("slack_channel_id")

        slack_team_id = d.pop("slack_team_id")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        slack_channel = cls(
            id=id,
            slack_channel_name=slack_channel_name,
            slack_channel_id=slack_channel_id,
            slack_team_id=slack_team_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        slack_channel.additional_properties = d
        return slack_channel

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
