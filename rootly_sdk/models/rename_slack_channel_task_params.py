from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rename_slack_channel_task_params_task_type import (
    RenameSlackChannelTaskParamsTaskType,
    check_rename_slack_channel_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rename_slack_channel_task_params_channel import RenameSlackChannelTaskParamsChannel


T = TypeVar("T", bound="RenameSlackChannelTaskParams")


@_attrs_define
class RenameSlackChannelTaskParams:
    """
    Attributes:
        channel (RenameSlackChannelTaskParamsChannel):
        title (str):
        task_type (RenameSlackChannelTaskParamsTaskType | Unset):
        retry_count (int | Unset): Number of times to retry on rate-limit (HTTP 429) responses (0-4). 0 disables retry.
            Default: 0. Example: 3.
        retry_wait_time (int | Unset): Seconds to wait before each retry (1-15). Retry-After header is honored when
            present and <= 90s, taking the larger of retry_wait_time and the header value. Default: 1. Example: 2.
    """

    channel: RenameSlackChannelTaskParamsChannel
    title: str
    task_type: RenameSlackChannelTaskParamsTaskType | Unset = UNSET
    retry_count: int | Unset = 0
    retry_wait_time: int | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel = self.channel.to_dict()

        title = self.title

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        retry_count = self.retry_count

        retry_wait_time = self.retry_wait_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel": channel,
                "title": title,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if retry_count is not UNSET:
            field_dict["retry_count"] = retry_count
        if retry_wait_time is not UNSET:
            field_dict["retry_wait_time"] = retry_wait_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rename_slack_channel_task_params_channel import RenameSlackChannelTaskParamsChannel

        d = dict(src_dict)
        channel = RenameSlackChannelTaskParamsChannel.from_dict(d.pop("channel"))

        title = d.pop("title")

        _task_type = d.pop("task_type", UNSET)
        task_type: RenameSlackChannelTaskParamsTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_rename_slack_channel_task_params_task_type(_task_type)

        retry_count = d.pop("retry_count", UNSET)

        retry_wait_time = d.pop("retry_wait_time", UNSET)

        rename_slack_channel_task_params = cls(
            channel=channel,
            title=title,
            task_type=task_type,
            retry_count=retry_count,
            retry_wait_time=retry_wait_time,
        )

        rename_slack_channel_task_params.additional_properties = d
        return rename_slack_channel_task_params

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
