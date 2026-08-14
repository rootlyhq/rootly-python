from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.redis_client_task_params_task_type import (
    RedisClientTaskParamsTaskType,
    check_redis_client_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.redis_client_task_params_post_to_slack_channels_item import (
        RedisClientTaskParamsPostToSlackChannelsItem,
    )


T = TypeVar("T", bound="RedisClientTaskParams")


@_attrs_define
class RedisClientTaskParams:
    """
    Attributes:
        url (str):  Example: redis://redis-12345.c1.us-east-1-2.ec2.cloud.redislabs.com:12345.
        commands (str):
        task_type (Union[Unset, RedisClientTaskParamsTaskType]):
        event_url (Union[Unset, str]):
        event_message (Union[Unset, str]):
        post_to_incident_timeline (Union[Unset, bool]):
        post_to_slack_channels (Union[Unset, list['RedisClientTaskParamsPostToSlackChannelsItem']]):
    """

    url: str
    commands: str
    task_type: Unset | RedisClientTaskParamsTaskType = UNSET
    event_url: Unset | str = UNSET
    event_message: Unset | str = UNSET
    post_to_incident_timeline: Unset | bool = UNSET
    post_to_slack_channels: Unset | list["RedisClientTaskParamsPostToSlackChannelsItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        commands = self.commands

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        event_url = self.event_url

        event_message = self.event_message

        post_to_incident_timeline = self.post_to_incident_timeline

        post_to_slack_channels: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.post_to_slack_channels, Unset):
            post_to_slack_channels = []
            for post_to_slack_channels_item_data in self.post_to_slack_channels:
                post_to_slack_channels_item = post_to_slack_channels_item_data.to_dict()
                post_to_slack_channels.append(post_to_slack_channels_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "commands": commands,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if event_url is not UNSET:
            field_dict["event_url"] = event_url
        if event_message is not UNSET:
            field_dict["event_message"] = event_message
        if post_to_incident_timeline is not UNSET:
            field_dict["post_to_incident_timeline"] = post_to_incident_timeline
        if post_to_slack_channels is not UNSET:
            field_dict["post_to_slack_channels"] = post_to_slack_channels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.redis_client_task_params_post_to_slack_channels_item import (
            RedisClientTaskParamsPostToSlackChannelsItem,
        )

        d = dict(src_dict)
        url = d.pop("url")

        commands = d.pop("commands")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | RedisClientTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_redis_client_task_params_task_type(_task_type)

        event_url = d.pop("event_url", UNSET)

        event_message = d.pop("event_message", UNSET)

        post_to_incident_timeline = d.pop("post_to_incident_timeline", UNSET)

        post_to_slack_channels = []
        _post_to_slack_channels = d.pop("post_to_slack_channels", UNSET)
        for post_to_slack_channels_item_data in _post_to_slack_channels or []:
            post_to_slack_channels_item = RedisClientTaskParamsPostToSlackChannelsItem.from_dict(
                post_to_slack_channels_item_data
            )

            post_to_slack_channels.append(post_to_slack_channels_item)

        redis_client_task_params = cls(
            url=url,
            commands=commands,
            task_type=task_type,
            event_url=event_url,
            event_message=event_message,
            post_to_incident_timeline=post_to_incident_timeline,
            post_to_slack_channels=post_to_slack_channels,
        )

        redis_client_task_params.additional_properties = d
        return redis_client_task_params

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
