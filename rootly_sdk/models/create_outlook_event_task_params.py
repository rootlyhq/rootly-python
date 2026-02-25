from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_outlook_event_task_params_task_type import (
    CreateOutlookEventTaskParamsTaskType,
    check_create_outlook_event_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_outlook_event_task_params_calendar import CreateOutlookEventTaskParamsCalendar
    from ..models.create_outlook_event_task_params_post_to_slack_channels_item import (
        CreateOutlookEventTaskParamsPostToSlackChannelsItem,
    )


T = TypeVar("T", bound="CreateOutlookEventTaskParams")


@_attrs_define
class CreateOutlookEventTaskParams:
    """
    Attributes:
        calendar (CreateOutlookEventTaskParamsCalendar):
        days_until_meeting (int): The days until meeting
        time_of_meeting (str): Time of meeting in format HH:MM Example: 14:30.
        meeting_duration (str): Meeting duration in format like '1 hour', '30 minutes' Example: 1 hour.
        summary (str): The event summary
        description (str): The event description
        task_type (Union[Unset, CreateOutlookEventTaskParamsTaskType]):
        attendees (Union[Unset, list[str]]): Emails of attendees
        time_zone (Union[None, Unset, str]): A valid IANA time zone name.
        exclude_weekends (Union[Unset, bool]):
        enable_online_meeting (Union[Unset, bool]): Enable Microsoft Teams online meeting
        post_to_incident_timeline (Union[Unset, bool]):
        post_to_slack_channels (Union[Unset, list['CreateOutlookEventTaskParamsPostToSlackChannelsItem']]):
    """

    calendar: "CreateOutlookEventTaskParamsCalendar"
    days_until_meeting: int
    time_of_meeting: str
    meeting_duration: str
    summary: str
    description: str
    task_type: Unset | CreateOutlookEventTaskParamsTaskType = UNSET
    attendees: Unset | list[str] = UNSET
    time_zone: None | Unset | str = UNSET
    exclude_weekends: Unset | bool = UNSET
    enable_online_meeting: Unset | bool = UNSET
    post_to_incident_timeline: Unset | bool = UNSET
    post_to_slack_channels: Unset | list["CreateOutlookEventTaskParamsPostToSlackChannelsItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        calendar = self.calendar.to_dict()

        days_until_meeting = self.days_until_meeting

        time_of_meeting = self.time_of_meeting

        meeting_duration = self.meeting_duration

        summary = self.summary

        description = self.description

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        attendees: Unset | list[str] = UNSET
        if not isinstance(self.attendees, Unset):
            attendees = self.attendees

        time_zone: None | Unset | str
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = self.time_zone

        exclude_weekends = self.exclude_weekends

        enable_online_meeting = self.enable_online_meeting

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
                "calendar": calendar,
                "days_until_meeting": days_until_meeting,
                "time_of_meeting": time_of_meeting,
                "meeting_duration": meeting_duration,
                "summary": summary,
                "description": description,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if attendees is not UNSET:
            field_dict["attendees"] = attendees
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone
        if exclude_weekends is not UNSET:
            field_dict["exclude_weekends"] = exclude_weekends
        if enable_online_meeting is not UNSET:
            field_dict["enable_online_meeting"] = enable_online_meeting
        if post_to_incident_timeline is not UNSET:
            field_dict["post_to_incident_timeline"] = post_to_incident_timeline
        if post_to_slack_channels is not UNSET:
            field_dict["post_to_slack_channels"] = post_to_slack_channels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_outlook_event_task_params_calendar import CreateOutlookEventTaskParamsCalendar
        from ..models.create_outlook_event_task_params_post_to_slack_channels_item import (
            CreateOutlookEventTaskParamsPostToSlackChannelsItem,
        )

        d = dict(src_dict)
        calendar = CreateOutlookEventTaskParamsCalendar.from_dict(d.pop("calendar"))

        days_until_meeting = d.pop("days_until_meeting")

        time_of_meeting = d.pop("time_of_meeting")

        meeting_duration = d.pop("meeting_duration")

        summary = d.pop("summary")

        description = d.pop("description")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | CreateOutlookEventTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_outlook_event_task_params_task_type(_task_type)

        attendees = cast(list[str], d.pop("attendees", UNSET))

        def _parse_time_zone(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        time_zone = _parse_time_zone(d.pop("time_zone", UNSET))

        exclude_weekends = d.pop("exclude_weekends", UNSET)

        enable_online_meeting = d.pop("enable_online_meeting", UNSET)

        post_to_incident_timeline = d.pop("post_to_incident_timeline", UNSET)

        post_to_slack_channels = []
        _post_to_slack_channels = d.pop("post_to_slack_channels", UNSET)
        for post_to_slack_channels_item_data in _post_to_slack_channels or []:
            post_to_slack_channels_item = CreateOutlookEventTaskParamsPostToSlackChannelsItem.from_dict(
                post_to_slack_channels_item_data
            )

            post_to_slack_channels.append(post_to_slack_channels_item)

        create_outlook_event_task_params = cls(
            calendar=calendar,
            days_until_meeting=days_until_meeting,
            time_of_meeting=time_of_meeting,
            meeting_duration=meeting_duration,
            summary=summary,
            description=description,
            task_type=task_type,
            attendees=attendees,
            time_zone=time_zone,
            exclude_weekends=exclude_weekends,
            enable_online_meeting=enable_online_meeting,
            post_to_incident_timeline=post_to_incident_timeline,
            post_to_slack_channels=post_to_slack_channels,
        )

        create_outlook_event_task_params.additional_properties = d
        return create_outlook_event_task_params

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
