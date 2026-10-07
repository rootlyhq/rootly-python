from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_zoom_meeting_task_params_auto_recording import (
    CreateZoomMeetingTaskParamsAutoRecording,
    check_create_zoom_meeting_task_params_auto_recording,
)
from ..models.create_zoom_meeting_task_params_recording_mode import (
    CreateZoomMeetingTaskParamsRecordingMode,
    check_create_zoom_meeting_task_params_recording_mode,
)
from ..models.create_zoom_meeting_task_params_task_type import (
    CreateZoomMeetingTaskParamsTaskType,
    check_create_zoom_meeting_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_zoom_meeting_task_params_post_to_slack_channels_item import (
        CreateZoomMeetingTaskParamsPostToSlackChannelsItem,
    )


T = TypeVar("T", bound="CreateZoomMeetingTaskParams")


@_attrs_define
class CreateZoomMeetingTaskParams:
    """
    Attributes:
        topic (str): The meeting topic
        task_type (CreateZoomMeetingTaskParamsTaskType | Unset):
        password (str | Unset): The meeting password
        create_as_email (str | Unset): The email to use if creating as email
        alternative_hosts (list[str] | Unset):
        auto_recording (CreateZoomMeetingTaskParamsAutoRecording | Unset):  Default: 'none'.
        record_meeting (bool | Unset): Rootly AI will record the meeting and automatically generate a transcript and
            summary from your meeting
        recording_mode (CreateZoomMeetingTaskParamsRecordingMode | Unset): The video layout for the bot's recording
            (e.g. speaker_view, gallery_view, gallery_view_v2, audio_only)
        enable_zoom_bot_auto_join (bool | Unset): Allow the Rootly bot to start recording without waiting for host
            approval
        post_to_incident_timeline (bool | Unset):
        post_to_slack_channels (list[CreateZoomMeetingTaskParamsPostToSlackChannelsItem] | Unset):
        retry_count (int | Unset): Number of times to retry on rate-limit (HTTP 429) responses (0-4). 0 disables retry.
            Default: 0. Example: 3.
        retry_wait_time (int | Unset): Seconds to wait before each retry (1-15). Retry-After header is honored when
            present and <= 90s, taking the larger of retry_wait_time and the header value. Default: 1. Example: 2.
    """

    topic: str
    task_type: CreateZoomMeetingTaskParamsTaskType | Unset = UNSET
    password: str | Unset = UNSET
    create_as_email: str | Unset = UNSET
    alternative_hosts: list[str] | Unset = UNSET
    auto_recording: CreateZoomMeetingTaskParamsAutoRecording | Unset = "none"
    record_meeting: bool | Unset = UNSET
    recording_mode: CreateZoomMeetingTaskParamsRecordingMode | Unset = UNSET
    enable_zoom_bot_auto_join: bool | Unset = UNSET
    post_to_incident_timeline: bool | Unset = UNSET
    post_to_slack_channels: list[CreateZoomMeetingTaskParamsPostToSlackChannelsItem] | Unset = UNSET
    retry_count: int | Unset = 0
    retry_wait_time: int | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        topic = self.topic

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        password = self.password

        create_as_email = self.create_as_email

        alternative_hosts: list[str] | Unset = UNSET
        if not isinstance(self.alternative_hosts, Unset):
            alternative_hosts = self.alternative_hosts

        auto_recording: str | Unset = UNSET
        if not isinstance(self.auto_recording, Unset):
            auto_recording = self.auto_recording

        record_meeting = self.record_meeting

        recording_mode: str | Unset = UNSET
        if not isinstance(self.recording_mode, Unset):
            recording_mode = self.recording_mode

        enable_zoom_bot_auto_join = self.enable_zoom_bot_auto_join

        post_to_incident_timeline = self.post_to_incident_timeline

        post_to_slack_channels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.post_to_slack_channels, Unset):
            post_to_slack_channels = []
            for post_to_slack_channels_item_data in self.post_to_slack_channels:
                post_to_slack_channels_item = post_to_slack_channels_item_data.to_dict()
                post_to_slack_channels.append(post_to_slack_channels_item)

        retry_count = self.retry_count

        retry_wait_time = self.retry_wait_time

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
        if create_as_email is not UNSET:
            field_dict["create_as_email"] = create_as_email
        if alternative_hosts is not UNSET:
            field_dict["alternative_hosts"] = alternative_hosts
        if auto_recording is not UNSET:
            field_dict["auto_recording"] = auto_recording
        if record_meeting is not UNSET:
            field_dict["record_meeting"] = record_meeting
        if recording_mode is not UNSET:
            field_dict["recording_mode"] = recording_mode
        if enable_zoom_bot_auto_join is not UNSET:
            field_dict["enable_zoom_bot_auto_join"] = enable_zoom_bot_auto_join
        if post_to_incident_timeline is not UNSET:
            field_dict["post_to_incident_timeline"] = post_to_incident_timeline
        if post_to_slack_channels is not UNSET:
            field_dict["post_to_slack_channels"] = post_to_slack_channels
        if retry_count is not UNSET:
            field_dict["retry_count"] = retry_count
        if retry_wait_time is not UNSET:
            field_dict["retry_wait_time"] = retry_wait_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_zoom_meeting_task_params_post_to_slack_channels_item import (
            CreateZoomMeetingTaskParamsPostToSlackChannelsItem,
        )

        d = dict(src_dict)
        topic = d.pop("topic")

        _task_type = d.pop("task_type", UNSET)
        task_type: CreateZoomMeetingTaskParamsTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_zoom_meeting_task_params_task_type(_task_type)

        password = d.pop("password", UNSET)

        create_as_email = d.pop("create_as_email", UNSET)

        alternative_hosts = cast(list[str], d.pop("alternative_hosts", UNSET))

        _auto_recording = d.pop("auto_recording", UNSET)
        auto_recording: CreateZoomMeetingTaskParamsAutoRecording | Unset
        if isinstance(_auto_recording, Unset):
            auto_recording = UNSET
        else:
            auto_recording = check_create_zoom_meeting_task_params_auto_recording(_auto_recording)

        record_meeting = d.pop("record_meeting", UNSET)

        _recording_mode = d.pop("recording_mode", UNSET)
        recording_mode: CreateZoomMeetingTaskParamsRecordingMode | Unset
        if isinstance(_recording_mode, Unset):
            recording_mode = UNSET
        else:
            recording_mode = check_create_zoom_meeting_task_params_recording_mode(_recording_mode)

        enable_zoom_bot_auto_join = d.pop("enable_zoom_bot_auto_join", UNSET)

        post_to_incident_timeline = d.pop("post_to_incident_timeline", UNSET)

        _post_to_slack_channels = d.pop("post_to_slack_channels", UNSET)
        post_to_slack_channels: list[CreateZoomMeetingTaskParamsPostToSlackChannelsItem] | Unset = UNSET
        if _post_to_slack_channels is not UNSET:
            post_to_slack_channels = []
            for post_to_slack_channels_item_data in _post_to_slack_channels:
                post_to_slack_channels_item = CreateZoomMeetingTaskParamsPostToSlackChannelsItem.from_dict(
                    post_to_slack_channels_item_data
                )

                post_to_slack_channels.append(post_to_slack_channels_item)

        retry_count = d.pop("retry_count", UNSET)

        retry_wait_time = d.pop("retry_wait_time", UNSET)

        create_zoom_meeting_task_params = cls(
            topic=topic,
            task_type=task_type,
            password=password,
            create_as_email=create_as_email,
            alternative_hosts=alternative_hosts,
            auto_recording=auto_recording,
            record_meeting=record_meeting,
            recording_mode=recording_mode,
            enable_zoom_bot_auto_join=enable_zoom_bot_auto_join,
            post_to_incident_timeline=post_to_incident_timeline,
            post_to_slack_channels=post_to_slack_channels,
            retry_count=retry_count,
            retry_wait_time=retry_wait_time,
        )

        create_zoom_meeting_task_params.additional_properties = d
        return create_zoom_meeting_task_params

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
