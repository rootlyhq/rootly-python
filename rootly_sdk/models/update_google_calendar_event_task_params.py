from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_google_calendar_event_task_params_conference_solution_key import (
    UpdateGoogleCalendarEventTaskParamsConferenceSolutionKey,
    check_update_google_calendar_event_task_params_conference_solution_key,
)
from ..models.update_google_calendar_event_task_params_task_type import (
    UpdateGoogleCalendarEventTaskParamsTaskType,
    check_update_google_calendar_event_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_google_calendar_event_task_params_post_to_slack_channels_item import (
        UpdateGoogleCalendarEventTaskParamsPostToSlackChannelsItem,
    )


T = TypeVar("T", bound="UpdateGoogleCalendarEventTaskParams")


@_attrs_define
class UpdateGoogleCalendarEventTaskParams:
    """
    Attributes:
        event_id (str): The event ID
        task_type (Union[Unset, UpdateGoogleCalendarEventTaskParamsTaskType]):
        calendar_id (Union[None, Unset, str]):  Default: 'primary'.
        summary (Union[Unset, str]): The event summary
        description (Union[Unset, str]): The event description
        adjustment_days (Union[Unset, int]): Days to adjust meeting by
        time_of_meeting (Union[Unset, str]): Time of meeting in format HH:MM
        meeting_duration (Union[Unset, str]): Meeting duration in format like '1 hour', '30 minutes' Example: 1 hour.
        send_updates (Union[Unset, bool]): Send an email to the attendees notifying them of the event
        can_guests_modify_event (Union[Unset, bool]):
        can_guests_see_other_guests (Union[Unset, bool]):
        can_guests_invite_others (Union[Unset, bool]):
        attendees (Union[Unset, list[str]]): Emails of attendees
        replace_attendees (Union[Unset, bool]):
        conference_solution_key (Union[Unset, UpdateGoogleCalendarEventTaskParamsConferenceSolutionKey]): Sets the video
            conference type attached to the meeting
        post_to_incident_timeline (Union[Unset, bool]):
        post_to_slack_channels (Union[Unset, list['UpdateGoogleCalendarEventTaskParamsPostToSlackChannelsItem']]):
    """

    event_id: str
    task_type: Unset | UpdateGoogleCalendarEventTaskParamsTaskType = UNSET
    calendar_id: None | Unset | str = "primary"
    summary: Unset | str = UNSET
    description: Unset | str = UNSET
    adjustment_days: Unset | int = UNSET
    time_of_meeting: Unset | str = UNSET
    meeting_duration: Unset | str = UNSET
    send_updates: Unset | bool = UNSET
    can_guests_modify_event: Unset | bool = UNSET
    can_guests_see_other_guests: Unset | bool = UNSET
    can_guests_invite_others: Unset | bool = UNSET
    attendees: Unset | list[str] = UNSET
    replace_attendees: Unset | bool = UNSET
    conference_solution_key: Unset | UpdateGoogleCalendarEventTaskParamsConferenceSolutionKey = UNSET
    post_to_incident_timeline: Unset | bool = UNSET
    post_to_slack_channels: Unset | list["UpdateGoogleCalendarEventTaskParamsPostToSlackChannelsItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_id = self.event_id

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        calendar_id: None | Unset | str
        if isinstance(self.calendar_id, Unset):
            calendar_id = UNSET
        else:
            calendar_id = self.calendar_id

        summary = self.summary

        description = self.description

        adjustment_days = self.adjustment_days

        time_of_meeting = self.time_of_meeting

        meeting_duration = self.meeting_duration

        send_updates = self.send_updates

        can_guests_modify_event = self.can_guests_modify_event

        can_guests_see_other_guests = self.can_guests_see_other_guests

        can_guests_invite_others = self.can_guests_invite_others

        attendees: Unset | list[str] = UNSET
        if not isinstance(self.attendees, Unset):
            attendees = self.attendees

        replace_attendees = self.replace_attendees

        conference_solution_key: Unset | str = UNSET
        if not isinstance(self.conference_solution_key, Unset):
            conference_solution_key = self.conference_solution_key

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
                "event_id": event_id,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if calendar_id is not UNSET:
            field_dict["calendar_id"] = calendar_id
        if summary is not UNSET:
            field_dict["summary"] = summary
        if description is not UNSET:
            field_dict["description"] = description
        if adjustment_days is not UNSET:
            field_dict["adjustment_days"] = adjustment_days
        if time_of_meeting is not UNSET:
            field_dict["time_of_meeting"] = time_of_meeting
        if meeting_duration is not UNSET:
            field_dict["meeting_duration"] = meeting_duration
        if send_updates is not UNSET:
            field_dict["send_updates"] = send_updates
        if can_guests_modify_event is not UNSET:
            field_dict["can_guests_modify_event"] = can_guests_modify_event
        if can_guests_see_other_guests is not UNSET:
            field_dict["can_guests_see_other_guests"] = can_guests_see_other_guests
        if can_guests_invite_others is not UNSET:
            field_dict["can_guests_invite_others"] = can_guests_invite_others
        if attendees is not UNSET:
            field_dict["attendees"] = attendees
        if replace_attendees is not UNSET:
            field_dict["replace_attendees"] = replace_attendees
        if conference_solution_key is not UNSET:
            field_dict["conference_solution_key"] = conference_solution_key
        if post_to_incident_timeline is not UNSET:
            field_dict["post_to_incident_timeline"] = post_to_incident_timeline
        if post_to_slack_channels is not UNSET:
            field_dict["post_to_slack_channels"] = post_to_slack_channels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_google_calendar_event_task_params_post_to_slack_channels_item import (
            UpdateGoogleCalendarEventTaskParamsPostToSlackChannelsItem,
        )

        d = dict(src_dict)
        event_id = d.pop("event_id")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | UpdateGoogleCalendarEventTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_google_calendar_event_task_params_task_type(_task_type)

        def _parse_calendar_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        calendar_id = _parse_calendar_id(d.pop("calendar_id", UNSET))

        summary = d.pop("summary", UNSET)

        description = d.pop("description", UNSET)

        adjustment_days = d.pop("adjustment_days", UNSET)

        time_of_meeting = d.pop("time_of_meeting", UNSET)

        meeting_duration = d.pop("meeting_duration", UNSET)

        send_updates = d.pop("send_updates", UNSET)

        can_guests_modify_event = d.pop("can_guests_modify_event", UNSET)

        can_guests_see_other_guests = d.pop("can_guests_see_other_guests", UNSET)

        can_guests_invite_others = d.pop("can_guests_invite_others", UNSET)

        attendees = cast(list[str], d.pop("attendees", UNSET))

        replace_attendees = d.pop("replace_attendees", UNSET)

        _conference_solution_key = d.pop("conference_solution_key", UNSET)
        conference_solution_key: Unset | UpdateGoogleCalendarEventTaskParamsConferenceSolutionKey
        if isinstance(_conference_solution_key, Unset):
            conference_solution_key = UNSET
        else:
            conference_solution_key = check_update_google_calendar_event_task_params_conference_solution_key(
                _conference_solution_key
            )

        post_to_incident_timeline = d.pop("post_to_incident_timeline", UNSET)

        post_to_slack_channels = []
        _post_to_slack_channels = d.pop("post_to_slack_channels", UNSET)
        for post_to_slack_channels_item_data in _post_to_slack_channels or []:
            post_to_slack_channels_item = UpdateGoogleCalendarEventTaskParamsPostToSlackChannelsItem.from_dict(
                post_to_slack_channels_item_data
            )

            post_to_slack_channels.append(post_to_slack_channels_item)

        update_google_calendar_event_task_params = cls(
            event_id=event_id,
            task_type=task_type,
            calendar_id=calendar_id,
            summary=summary,
            description=description,
            adjustment_days=adjustment_days,
            time_of_meeting=time_of_meeting,
            meeting_duration=meeting_duration,
            send_updates=send_updates,
            can_guests_modify_event=can_guests_modify_event,
            can_guests_see_other_guests=can_guests_see_other_guests,
            can_guests_invite_others=can_guests_invite_others,
            attendees=attendees,
            replace_attendees=replace_attendees,
            conference_solution_key=conference_solution_key,
            post_to_incident_timeline=post_to_incident_timeline,
            post_to_slack_channels=post_to_slack_channels,
        )

        update_google_calendar_event_task_params.additional_properties = d
        return update_google_calendar_event_task_params

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
