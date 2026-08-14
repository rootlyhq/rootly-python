from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_go_to_meeting_task_params_conference_call_info import (
    CreateGoToMeetingTaskParamsConferenceCallInfo,
    check_create_go_to_meeting_task_params_conference_call_info,
)
from ..models.create_go_to_meeting_task_params_task_type import (
    CreateGoToMeetingTaskParamsTaskType,
    check_create_go_to_meeting_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_go_to_meeting_task_params_post_to_slack_channels_item import (
        CreateGoToMeetingTaskParamsPostToSlackChannelsItem,
    )


T = TypeVar("T", bound="CreateGoToMeetingTaskParams")


@_attrs_define
class CreateGoToMeetingTaskParams:
    """
    Attributes:
        subject (str): The meeting subject
        task_type (Union[Unset, CreateGoToMeetingTaskParamsTaskType]):
        conference_call_info (Union[Unset, CreateGoToMeetingTaskParamsConferenceCallInfo]):  Default: 'voip'. Example:
            voip.
        password_required (Union[None, Unset, bool]):
        post_to_incident_timeline (Union[Unset, bool]):
        post_to_slack_channels (Union[Unset, list['CreateGoToMeetingTaskParamsPostToSlackChannelsItem']]):
    """

    subject: str
    task_type: Unset | CreateGoToMeetingTaskParamsTaskType = UNSET
    conference_call_info: Unset | CreateGoToMeetingTaskParamsConferenceCallInfo = "voip"
    password_required: None | Unset | bool = UNSET
    post_to_incident_timeline: Unset | bool = UNSET
    post_to_slack_channels: Unset | list["CreateGoToMeetingTaskParamsPostToSlackChannelsItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subject = self.subject

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        conference_call_info: Unset | str = UNSET
        if not isinstance(self.conference_call_info, Unset):
            conference_call_info = self.conference_call_info

        password_required: None | Unset | bool
        if isinstance(self.password_required, Unset):
            password_required = UNSET
        else:
            password_required = self.password_required

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
                "subject": subject,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if conference_call_info is not UNSET:
            field_dict["conference_call_info"] = conference_call_info
        if password_required is not UNSET:
            field_dict["password_required"] = password_required
        if post_to_incident_timeline is not UNSET:
            field_dict["post_to_incident_timeline"] = post_to_incident_timeline
        if post_to_slack_channels is not UNSET:
            field_dict["post_to_slack_channels"] = post_to_slack_channels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_go_to_meeting_task_params_post_to_slack_channels_item import (
            CreateGoToMeetingTaskParamsPostToSlackChannelsItem,
        )

        d = dict(src_dict)
        subject = d.pop("subject")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | CreateGoToMeetingTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_go_to_meeting_task_params_task_type(_task_type)

        _conference_call_info = d.pop("conference_call_info", UNSET)
        conference_call_info: Unset | CreateGoToMeetingTaskParamsConferenceCallInfo
        if isinstance(_conference_call_info, Unset):
            conference_call_info = UNSET
        else:
            conference_call_info = check_create_go_to_meeting_task_params_conference_call_info(_conference_call_info)

        def _parse_password_required(data: object) -> None | Unset | bool:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | bool, data)

        password_required = _parse_password_required(d.pop("password_required", UNSET))

        post_to_incident_timeline = d.pop("post_to_incident_timeline", UNSET)

        post_to_slack_channels = []
        _post_to_slack_channels = d.pop("post_to_slack_channels", UNSET)
        for post_to_slack_channels_item_data in _post_to_slack_channels or []:
            post_to_slack_channels_item = CreateGoToMeetingTaskParamsPostToSlackChannelsItem.from_dict(
                post_to_slack_channels_item_data
            )

            post_to_slack_channels.append(post_to_slack_channels_item)

        create_go_to_meeting_task_params = cls(
            subject=subject,
            task_type=task_type,
            conference_call_info=conference_call_info,
            password_required=password_required,
            post_to_incident_timeline=post_to_incident_timeline,
            post_to_slack_channels=post_to_slack_channels,
        )

        create_go_to_meeting_task_params.additional_properties = d
        return create_go_to_meeting_task_params

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
