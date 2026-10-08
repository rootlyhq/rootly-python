from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateSlackCanvasTaskParamsChannel")


@_attrs_define
class CreateSlackCanvasTaskParamsChannel:
    """Slack channel containing the canvas. Channel IDs support Liquid variables.

    Attributes:
        id (str): Slack channel ID. Example: {{ incident.slack_channel_id }}.
        name (str): Channel display name. Example: incident-channel.
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

        create_slack_canvas_task_params_channel = cls(
            id=id,
            name=name,
        )

        return create_slack_canvas_task_params_channel
