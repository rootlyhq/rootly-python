from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_shift_report_day_of_week import (
    ScheduleShiftReportDayOfWeek,
    check_schedule_shift_report_day_of_week,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_slack_channel_type_0 import ScheduleSlackChannelType0
    from ..models.schedule_slack_user_group_type_0 import ScheduleSlackUserGroupType0


T = TypeVar("T", bound="Schedule")


@_attrs_define
class Schedule:
    """
    Attributes:
        name (str): The name of the schedule
        owner_user_id (int): ID of user assigned as owner of the schedule
        created_at (str): Date of creation
        updated_at (str): Date of last update
        description (Union[None, Unset, str]): The description of the schedule
        all_time_coverage (Union[None, Unset, bool]): 24/7 coverage of the schedule
        slack_user_group (Union['ScheduleSlackUserGroupType0', None, Unset]): Synced slack group of the schedule
        slack_channel (Union['ScheduleSlackChannelType0', None, Unset]): Synced slack channel of the schedule
        owner_group_ids (Union[Unset, list[str]]): Owning teams.
        sync_linear_enabled (Union[Unset, bool]): Whether the schedule is synced with Linear
        include_shadows_in_slack_notifications (Union[Unset, bool]): Whether shadow users are included in Slack
            notifications and user group syncing. Requires `slack_channel` to be set; otherwise this value is forced to
            false on save.
        shift_start_notifications_enabled (Union[Unset, bool]): Whether shift-start notifications are enabled. Requires
            `slack_channel` to be set; otherwise this value is forced to false on save.
        shift_update_notifications_enabled (Union[Unset, bool]): Whether shift-update notifications are enabled.
            Requires `slack_channel` to be set; otherwise this value is forced to false on save.
        shift_report_enabled (Union[Unset, bool]): Whether the weekly shift summary report is enabled. Requires
            `slack_channel` to be set; otherwise this value is forced to false on save.
        shift_report_day_of_week (Union[Unset, ScheduleShiftReportDayOfWeek]): Day of week the weekly shift summary is
            sent
        shift_report_time_of_day (Union[Unset, str]): Time of day the weekly shift summary is sent, in HH:MM 24-hour
            format
        shift_report_time_zone (Union[Unset, str]): IANA time zone used for the weekly shift summary
    """

    name: str
    owner_user_id: int
    created_at: str
    updated_at: str
    description: Union[None, Unset, str] = UNSET
    all_time_coverage: Union[None, Unset, bool] = UNSET
    slack_user_group: Union["ScheduleSlackUserGroupType0", None, Unset] = UNSET
    slack_channel: Union["ScheduleSlackChannelType0", None, Unset] = UNSET
    owner_group_ids: Union[Unset, list[str]] = UNSET
    sync_linear_enabled: Union[Unset, bool] = UNSET
    include_shadows_in_slack_notifications: Union[Unset, bool] = UNSET
    shift_start_notifications_enabled: Union[Unset, bool] = UNSET
    shift_update_notifications_enabled: Union[Unset, bool] = UNSET
    shift_report_enabled: Union[Unset, bool] = UNSET
    shift_report_day_of_week: Union[Unset, ScheduleShiftReportDayOfWeek] = UNSET
    shift_report_time_of_day: Union[Unset, str] = UNSET
    shift_report_time_zone: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.schedule_slack_channel_type_0 import ScheduleSlackChannelType0
        from ..models.schedule_slack_user_group_type_0 import ScheduleSlackUserGroupType0

        name = self.name

        owner_user_id = self.owner_user_id

        created_at = self.created_at

        updated_at = self.updated_at

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        all_time_coverage: Union[None, Unset, bool]
        if isinstance(self.all_time_coverage, Unset):
            all_time_coverage = UNSET
        else:
            all_time_coverage = self.all_time_coverage

        slack_user_group: Union[None, Unset, dict[str, Any]]
        if isinstance(self.slack_user_group, Unset):
            slack_user_group = UNSET
        elif isinstance(self.slack_user_group, ScheduleSlackUserGroupType0):
            slack_user_group = self.slack_user_group.to_dict()
        else:
            slack_user_group = self.slack_user_group

        slack_channel: Union[None, Unset, dict[str, Any]]
        if isinstance(self.slack_channel, Unset):
            slack_channel = UNSET
        elif isinstance(self.slack_channel, ScheduleSlackChannelType0):
            slack_channel = self.slack_channel.to_dict()
        else:
            slack_channel = self.slack_channel

        owner_group_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.owner_group_ids, Unset):
            owner_group_ids = self.owner_group_ids

        sync_linear_enabled = self.sync_linear_enabled

        include_shadows_in_slack_notifications = self.include_shadows_in_slack_notifications

        shift_start_notifications_enabled = self.shift_start_notifications_enabled

        shift_update_notifications_enabled = self.shift_update_notifications_enabled

        shift_report_enabled = self.shift_report_enabled

        shift_report_day_of_week: Union[Unset, str] = UNSET
        if not isinstance(self.shift_report_day_of_week, Unset):
            shift_report_day_of_week = self.shift_report_day_of_week

        shift_report_time_of_day = self.shift_report_time_of_day

        shift_report_time_zone = self.shift_report_time_zone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "owner_user_id": owner_user_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if all_time_coverage is not UNSET:
            field_dict["all_time_coverage"] = all_time_coverage
        if slack_user_group is not UNSET:
            field_dict["slack_user_group"] = slack_user_group
        if slack_channel is not UNSET:
            field_dict["slack_channel"] = slack_channel
        if owner_group_ids is not UNSET:
            field_dict["owner_group_ids"] = owner_group_ids
        if sync_linear_enabled is not UNSET:
            field_dict["sync_linear_enabled"] = sync_linear_enabled
        if include_shadows_in_slack_notifications is not UNSET:
            field_dict["include_shadows_in_slack_notifications"] = include_shadows_in_slack_notifications
        if shift_start_notifications_enabled is not UNSET:
            field_dict["shift_start_notifications_enabled"] = shift_start_notifications_enabled
        if shift_update_notifications_enabled is not UNSET:
            field_dict["shift_update_notifications_enabled"] = shift_update_notifications_enabled
        if shift_report_enabled is not UNSET:
            field_dict["shift_report_enabled"] = shift_report_enabled
        if shift_report_day_of_week is not UNSET:
            field_dict["shift_report_day_of_week"] = shift_report_day_of_week
        if shift_report_time_of_day is not UNSET:
            field_dict["shift_report_time_of_day"] = shift_report_time_of_day
        if shift_report_time_zone is not UNSET:
            field_dict["shift_report_time_zone"] = shift_report_time_zone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schedule_slack_channel_type_0 import ScheduleSlackChannelType0
        from ..models.schedule_slack_user_group_type_0 import ScheduleSlackUserGroupType0

        d = dict(src_dict)
        name = d.pop("name")

        owner_user_id = d.pop("owner_user_id")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_all_time_coverage(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        all_time_coverage = _parse_all_time_coverage(d.pop("all_time_coverage", UNSET))

        def _parse_slack_user_group(data: object) -> Union["ScheduleSlackUserGroupType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                slack_user_group_type_0 = ScheduleSlackUserGroupType0.from_dict(data)

                return slack_user_group_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ScheduleSlackUserGroupType0", None, Unset], data)

        slack_user_group = _parse_slack_user_group(d.pop("slack_user_group", UNSET))

        def _parse_slack_channel(data: object) -> Union["ScheduleSlackChannelType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                slack_channel_type_0 = ScheduleSlackChannelType0.from_dict(data)

                return slack_channel_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ScheduleSlackChannelType0", None, Unset], data)

        slack_channel = _parse_slack_channel(d.pop("slack_channel", UNSET))

        owner_group_ids = cast(list[str], d.pop("owner_group_ids", UNSET))

        sync_linear_enabled = d.pop("sync_linear_enabled", UNSET)

        include_shadows_in_slack_notifications = d.pop("include_shadows_in_slack_notifications", UNSET)

        shift_start_notifications_enabled = d.pop("shift_start_notifications_enabled", UNSET)

        shift_update_notifications_enabled = d.pop("shift_update_notifications_enabled", UNSET)

        shift_report_enabled = d.pop("shift_report_enabled", UNSET)

        _shift_report_day_of_week = d.pop("shift_report_day_of_week", UNSET)
        shift_report_day_of_week: Union[Unset, ScheduleShiftReportDayOfWeek]
        if isinstance(_shift_report_day_of_week, Unset):
            shift_report_day_of_week = UNSET
        else:
            shift_report_day_of_week = check_schedule_shift_report_day_of_week(_shift_report_day_of_week)

        shift_report_time_of_day = d.pop("shift_report_time_of_day", UNSET)

        shift_report_time_zone = d.pop("shift_report_time_zone", UNSET)

        schedule = cls(
            name=name,
            owner_user_id=owner_user_id,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            all_time_coverage=all_time_coverage,
            slack_user_group=slack_user_group,
            slack_channel=slack_channel,
            owner_group_ids=owner_group_ids,
            sync_linear_enabled=sync_linear_enabled,
            include_shadows_in_slack_notifications=include_shadows_in_slack_notifications,
            shift_start_notifications_enabled=shift_start_notifications_enabled,
            shift_update_notifications_enabled=shift_update_notifications_enabled,
            shift_report_enabled=shift_report_enabled,
            shift_report_day_of_week=shift_report_day_of_week,
            shift_report_time_of_day=shift_report_time_of_day,
            shift_report_time_zone=shift_report_time_zone,
        )

        schedule.additional_properties = d
        return schedule

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
