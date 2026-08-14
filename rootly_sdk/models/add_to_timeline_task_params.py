from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.add_to_timeline_task_params_task_type import (
    AddToTimelineTaskParamsTaskType,
    check_add_to_timeline_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_to_timeline_task_params_post_to_slack_channels_item import (
        AddToTimelineTaskParamsPostToSlackChannelsItem,
    )


T = TypeVar("T", bound="AddToTimelineTaskParams")


@_attrs_define
class AddToTimelineTaskParams:
    """
    Attributes:
        event (str): The timeline event description
        task_type (Union[Unset, AddToTimelineTaskParamsTaskType]):
        url (Union[Unset, str]): A URL for the timeline event
        post_to_slack_channels (Union[Unset, list['AddToTimelineTaskParamsPostToSlackChannelsItem']]):
    """

    event: str
    task_type: Unset | AddToTimelineTaskParamsTaskType = UNSET
    url: Unset | str = UNSET
    post_to_slack_channels: Unset | list["AddToTimelineTaskParamsPostToSlackChannelsItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event = self.event

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        url = self.url

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
                "event": event,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if url is not UNSET:
            field_dict["url"] = url
        if post_to_slack_channels is not UNSET:
            field_dict["post_to_slack_channels"] = post_to_slack_channels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_to_timeline_task_params_post_to_slack_channels_item import (
            AddToTimelineTaskParamsPostToSlackChannelsItem,
        )

        d = dict(src_dict)
        event = d.pop("event")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | AddToTimelineTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_add_to_timeline_task_params_task_type(_task_type)

        url = d.pop("url", UNSET)

        post_to_slack_channels = []
        _post_to_slack_channels = d.pop("post_to_slack_channels", UNSET)
        for post_to_slack_channels_item_data in _post_to_slack_channels or []:
            post_to_slack_channels_item = AddToTimelineTaskParamsPostToSlackChannelsItem.from_dict(
                post_to_slack_channels_item_data
            )

            post_to_slack_channels.append(post_to_slack_channels_item)

        add_to_timeline_task_params = cls(
            event=event,
            task_type=task_type,
            url=url,
            post_to_slack_channels=post_to_slack_channels,
        )

        add_to_timeline_task_params.additional_properties = d
        return add_to_timeline_task_params

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
