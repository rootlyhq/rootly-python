from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_slack_channel_topic_task_params_task_type import (
    UpdateSlackChannelTopicTaskParamsTaskType,
    check_update_slack_channel_topic_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_slack_channel_topic_task_params_channel import UpdateSlackChannelTopicTaskParamsChannel


T = TypeVar("T", bound="UpdateSlackChannelTopicTaskParams")


@_attrs_define
class UpdateSlackChannelTopicTaskParams:
    """
    Attributes:
        channel (UpdateSlackChannelTopicTaskParamsChannel):
        topic (str):
        task_type (Union[Unset, UpdateSlackChannelTopicTaskParamsTaskType]):
    """

    channel: "UpdateSlackChannelTopicTaskParamsChannel"
    topic: str
    task_type: Unset | UpdateSlackChannelTopicTaskParamsTaskType = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel = self.channel.to_dict()

        topic = self.topic

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel": channel,
                "topic": topic,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_slack_channel_topic_task_params_channel import UpdateSlackChannelTopicTaskParamsChannel

        d = dict(src_dict)
        channel = UpdateSlackChannelTopicTaskParamsChannel.from_dict(d.pop("channel"))

        topic = d.pop("topic")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | UpdateSlackChannelTopicTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_slack_channel_topic_task_params_task_type(_task_type)

        update_slack_channel_topic_task_params = cls(
            channel=channel,
            topic=topic,
            task_type=task_type,
        )

        update_slack_channel_topic_task_params.additional_properties = d
        return update_slack_channel_topic_task_params

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
