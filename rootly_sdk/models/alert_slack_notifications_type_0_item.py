from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlertSlackNotificationsType0Item")


@_attrs_define
class AlertSlackNotificationsType0Item:
    """
    Attributes:
        channel_id (str): Slack channel ID
        thread_ts (str): Slack ts of the root announcement message
    """

    channel_id: str
    thread_ts: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        thread_ts = self.thread_ts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel_id": channel_id,
                "thread_ts": thread_ts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel_id = d.pop("channel_id")

        thread_ts = d.pop("thread_ts")

        alert_slack_notifications_type_0_item = cls(
            channel_id=channel_id,
            thread_ts=thread_ts,
        )

        alert_slack_notifications_type_0_item.additional_properties = d
        return alert_slack_notifications_type_0_item

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
