from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_slack_canvas_task_params_operation import (
    UpdateSlackCanvasTaskParamsOperation,
    check_update_slack_canvas_task_params_operation,
)
from ..models.update_slack_canvas_task_params_task_type import (
    UpdateSlackCanvasTaskParamsTaskType,
    check_update_slack_canvas_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_slack_canvas_task_params_channel import UpdateSlackCanvasTaskParamsChannel


T = TypeVar("T", bound="UpdateSlackCanvasTaskParams")


@_attrs_define
class UpdateSlackCanvasTaskParams:
    """Update the selected channel canvas using Markdown. The connected Slack app must have Canvas permissions.

    Attributes:
        channel (UpdateSlackCanvasTaskParamsChannel): Slack channel containing the canvas. Channel IDs support Liquid
            variables.
        content (str): The canvas content in Markdown. Supports Liquid variables.
        task_type (UpdateSlackCanvasTaskParamsTaskType | Unset):
        operation (UpdateSlackCanvasTaskParamsOperation | Unset): Append content or replace the selected table or entire
            canvas. Default: 'insert_at_end'.
        section_name (None | str | Unset): With replace, target the single table containing this label. Include the
            label in the replacement table. Blank replaces the entire canvas. Supports Liquid.
        retry_count (int | Unset): Number of times to retry on rate-limit (HTTP 429) responses (0-4). 0 disables retry.
            Default: 0. Example: 3.
        retry_wait_time (int | Unset): Seconds to wait before each retry (1-15). Retry-After header is honored when
            present and <= 90s, taking the larger of retry_wait_time and the header value. Default: 1. Example: 2.
    """

    channel: UpdateSlackCanvasTaskParamsChannel
    content: str
    task_type: UpdateSlackCanvasTaskParamsTaskType | Unset = UNSET
    operation: UpdateSlackCanvasTaskParamsOperation | Unset = "insert_at_end"
    section_name: None | str | Unset = UNSET
    retry_count: int | Unset = 0
    retry_wait_time: int | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel = self.channel.to_dict()

        content = self.content

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        operation: str | Unset = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation

        section_name: None | str | Unset
        if isinstance(self.section_name, Unset):
            section_name = UNSET
        else:
            section_name = self.section_name

        retry_count = self.retry_count

        retry_wait_time = self.retry_wait_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel": channel,
                "content": content,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if operation is not UNSET:
            field_dict["operation"] = operation
        if section_name is not UNSET:
            field_dict["section_name"] = section_name
        if retry_count is not UNSET:
            field_dict["retry_count"] = retry_count
        if retry_wait_time is not UNSET:
            field_dict["retry_wait_time"] = retry_wait_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_slack_canvas_task_params_channel import UpdateSlackCanvasTaskParamsChannel

        d = dict(src_dict)
        channel = UpdateSlackCanvasTaskParamsChannel.from_dict(d.pop("channel"))

        content = d.pop("content")

        _task_type = d.pop("task_type", UNSET)
        task_type: UpdateSlackCanvasTaskParamsTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_slack_canvas_task_params_task_type(_task_type)

        _operation = d.pop("operation", UNSET)
        operation: UpdateSlackCanvasTaskParamsOperation | Unset
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = check_update_slack_canvas_task_params_operation(_operation)

        def _parse_section_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        section_name = _parse_section_name(d.pop("section_name", UNSET))

        retry_count = d.pop("retry_count", UNSET)

        retry_wait_time = d.pop("retry_wait_time", UNSET)

        update_slack_canvas_task_params = cls(
            channel=channel,
            content=content,
            task_type=task_type,
            operation=operation,
            section_name=section_name,
            retry_count=retry_count,
            retry_wait_time=retry_wait_time,
        )

        update_slack_canvas_task_params.additional_properties = d
        return update_slack_canvas_task_params

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
