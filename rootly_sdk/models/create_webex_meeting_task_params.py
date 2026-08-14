from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_webex_meeting_task_params_recording_mode import (
    CreateWebexMeetingTaskParamsRecordingMode,
    check_create_webex_meeting_task_params_recording_mode,
)
from ..models.create_webex_meeting_task_params_task_type import (
    CreateWebexMeetingTaskParamsTaskType,
    check_create_webex_meeting_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_webex_meeting_task_params_post_to_slack_channels_item import (
        CreateWebexMeetingTaskParamsPostToSlackChannelsItem,
    )


T = TypeVar("T", bound="CreateWebexMeetingTaskParams")


@_attrs_define
class CreateWebexMeetingTaskParams:
    """
    Attributes:
        topic (str): The meeting topic
        task_type (Union[Unset, CreateWebexMeetingTaskParamsTaskType]):
        password (Union[Unset, str]): The meeting password
        record_meeting (Union[Unset, bool]): Rootly AI will record the meeting and automatically generate a transcript
            and summary from your meeting
        recording_mode (Union[Unset, CreateWebexMeetingTaskParamsRecordingMode]): The video layout for the bot's
            recording (e.g. speaker_view, gallery_view, gallery_view_v2, audio_only)
        post_to_incident_timeline (Union[Unset, bool]):
        post_to_slack_channels (Union[Unset, list['CreateWebexMeetingTaskParamsPostToSlackChannelsItem']]):
    """

    topic: str
    task_type: Union[Unset, CreateWebexMeetingTaskParamsTaskType] = UNSET
    password: Union[Unset, str] = UNSET
    record_meeting: Union[Unset, bool] = UNSET
    recording_mode: Union[Unset, CreateWebexMeetingTaskParamsRecordingMode] = UNSET
    post_to_incident_timeline: Union[Unset, bool] = UNSET
    post_to_slack_channels: Union[Unset, list["CreateWebexMeetingTaskParamsPostToSlackChannelsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        topic = self.topic

        task_type: Union[Unset, str] = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        password = self.password

        record_meeting = self.record_meeting

        recording_mode: Union[Unset, str] = UNSET
        if not isinstance(self.recording_mode, Unset):
            recording_mode = self.recording_mode

        post_to_incident_timeline = self.post_to_incident_timeline

        post_to_slack_channels: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.post_to_slack_channels, Unset):
            post_to_slack_channels = []
            for post_to_slack_channels_item_data in self.post_to_slack_channels:
                post_to_slack_channels_item = post_to_slack_channels_item_data.to_dict()
                post_to_slack_channels.append(post_to_slack_channels_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "topic": topic,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if password is not UNSET:
            field_dict["password"] = password
        if record_meeting is not UNSET:
            field_dict["record_meeting"] = record_meeting
        if recording_mode is not UNSET:
            field_dict["recording_mode"] = recording_mode
        if post_to_incident_timeline is not UNSET:
            field_dict["post_to_incident_timeline"] = post_to_incident_timeline
        if post_to_slack_channels is not UNSET:
            field_dict["post_to_slack_channels"] = post_to_slack_channels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_webex_meeting_task_params_post_to_slack_channels_item import (
            CreateWebexMeetingTaskParamsPostToSlackChannelsItem,
        )

        d = dict(src_dict)
        topic = d.pop("topic")

        _task_type = d.pop("task_type", UNSET)
        task_type: Union[Unset, CreateWebexMeetingTaskParamsTaskType]
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_webex_meeting_task_params_task_type(_task_type)

        password = d.pop("password", UNSET)

        record_meeting = d.pop("record_meeting", UNSET)

        _recording_mode = d.pop("recording_mode", UNSET)
        recording_mode: Union[Unset, CreateWebexMeetingTaskParamsRecordingMode]
        if isinstance(_recording_mode, Unset):
            recording_mode = UNSET
        else:
            recording_mode = check_create_webex_meeting_task_params_recording_mode(_recording_mode)

        post_to_incident_timeline = d.pop("post_to_incident_timeline", UNSET)

        post_to_slack_channels = []
        _post_to_slack_channels = d.pop("post_to_slack_channels", UNSET)
        for post_to_slack_channels_item_data in _post_to_slack_channels or []:
            post_to_slack_channels_item = CreateWebexMeetingTaskParamsPostToSlackChannelsItem.from_dict(
                post_to_slack_channels_item_data
            )

            post_to_slack_channels.append(post_to_slack_channels_item)

        create_webex_meeting_task_params = cls(
            topic=topic,
            task_type=task_type,
            password=password,
            record_meeting=record_meeting,
            recording_mode=recording_mode,
            post_to_incident_timeline=post_to_incident_timeline,
            post_to_slack_channels=post_to_slack_channels,
        )

        create_webex_meeting_task_params.additional_properties = d
        return create_webex_meeting_task_params

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
