from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="NewWorkflowDataAttributesFailureNotificationChannelsItem")


@_attrs_define
class NewWorkflowDataAttributesFailureNotificationChannelsItem:
    """
    Attributes:
        id (str): Slack channel ID. Liquid is allowed, for example `{{ incident.slack_channel_id }}` for the incident
            channel.
        name (str): Slack channel name
    """

    id: str
    name: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        new_workflow_data_attributes_failure_notification_channels_item = cls(
            id=id,
            name=name,
        )

        return new_workflow_data_attributes_failure_notification_channels_item
