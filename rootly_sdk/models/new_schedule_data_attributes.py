from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.new_schedule_data_attributes_shift_report_day_of_week import (
    check_new_schedule_data_attributes_shift_report_day_of_week,
)
from ..models.new_schedule_data_attributes_shift_report_day_of_week import NewScheduleDataAttributesShiftReportDayOfWeek
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.new_schedule_data_attributes_slack_channel_type_0 import NewScheduleDataAttributesSlackChannelType0
    from ..models.new_schedule_data_attributes_slack_user_group import NewScheduleDataAttributesSlackUserGroup


T = TypeVar("T", bound="NewScheduleDataAttributes")


@_attrs_define
class NewScheduleDataAttributes:
    """
    Attributes:
        name (str): The name of the schedule
        owner_user_id (int): ID of the owner of the schedule
        description (None | str | Unset): The description of the schedule
        all_time_coverage (bool | None | Unset): 24/7 coverage of the schedule
        slack_user_group (NewScheduleDataAttributesSlackUserGroup | Unset):
        slack_channel (NewScheduleDataAttributesSlackChannelType0 | None | Unset):
        owner_group_ids (list[str] | Unset): Owning teams.
        sync_linear_enabled (bool | None | Unset): Whether the schedule is synced with Linear
        include_shadows_in_slack_notifications (bool | None | Unset): Whether shadow users are included in Slack
            notifications and user group syncing. Requires `slack_channel` to be set; otherwise this value is forced to
            false on save.
        shift_start_notifications_enabled (bool | None | Unset): Whether shift-start notifications are enabled. Requires
            `slack_channel` to be set; otherwise this value is forced to false on save.
        shift_update_notifications_enabled (bool | None | Unset): Whether shift-update notifications are enabled.
            Requires `slack_channel` to be set; otherwise this value is forced to false on save.
        shift_report_enabled (bool | None | Unset): Whether the weekly shift summary report is enabled. Requires
            `slack_channel` to be set; otherwise this value is forced to false on save.
        shift_report_day_of_week (NewScheduleDataAttributesShiftReportDayOfWeek | Unset): Day of week the weekly shift
            summary is sent
        shift_report_time_of_day (None | str | Unset): Time of day the weekly shift summary is sent, in HH:MM 24-hour
            format
        shift_report_time_zone (None | str | Unset): IANA time zone used for the weekly shift summary
    """

    name: str
    owner_user_id: int
    description: None | str | Unset = UNSET
    all_time_coverage: bool | None | Unset = UNSET
    slack_user_group: NewScheduleDataAttributesSlackUserGroup | Unset = UNSET
    slack_channel: NewScheduleDataAttributesSlackChannelType0 | None | Unset = UNSET
    owner_group_ids: list[str] | Unset = UNSET
    sync_linear_enabled: bool | None | Unset = UNSET
    include_shadows_in_slack_notifications: bool | None | Unset = UNSET
    shift_start_notifications_enabled: bool | None | Unset = UNSET
    shift_update_notifications_enabled: bool | None | Unset = UNSET
    shift_report_enabled: bool | None | Unset = UNSET
    shift_report_day_of_week: NewScheduleDataAttributesShiftReportDayOfWeek | Unset = UNSET
    shift_report_time_of_day: None | str | Unset = UNSET
    shift_report_time_zone: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.new_schedule_data_attributes_slack_user_group import NewScheduleDataAttributesSlackUserGroup
        from ..models.new_schedule_data_attributes_slack_channel_type_0 import (
            NewScheduleDataAttributesSlackChannelType0,
        )

        name = self.name

        owner_user_id = self.owner_user_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        all_time_coverage: bool | None | Unset
        if isinstance(self.all_time_coverage, Unset):
            all_time_coverage = UNSET
        else:
            all_time_coverage = self.all_time_coverage

        slack_user_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.slack_user_group, Unset):
            slack_user_group = self.slack_user_group.to_dict()

        slack_channel: dict[str, Any] | None | Unset
        if isinstance(self.slack_channel, Unset):
            slack_channel = UNSET
        elif isinstance(self.slack_channel, NewScheduleDataAttributesSlackChannelType0):
            slack_channel = self.slack_channel.to_dict()
        else:
            slack_channel = self.slack_channel

        owner_group_ids: list[str] | Unset = UNSET
        if not isinstance(self.owner_group_ids, Unset):
            owner_group_ids = self.owner_group_ids

        sync_linear_enabled: bool | None | Unset
        if isinstance(self.sync_linear_enabled, Unset):
            sync_linear_enabled = UNSET
        else:
            sync_linear_enabled = self.sync_linear_enabled

        include_shadows_in_slack_notifications: bool | None | Unset
        if isinstance(self.include_shadows_in_slack_notifications, Unset):
            include_shadows_in_slack_notifications = UNSET
        else:
            include_shadows_in_slack_notifications = self.include_shadows_in_slack_notifications

        shift_start_notifications_enabled: bool | None | Unset
        if isinstance(self.shift_start_notifications_enabled, Unset):
            shift_start_notifications_enabled = UNSET
        else:
            shift_start_notifications_enabled = self.shift_start_notifications_enabled

        shift_update_notifications_enabled: bool | None | Unset
        if isinstance(self.shift_update_notifications_enabled, Unset):
            shift_update_notifications_enabled = UNSET
        else:
            shift_update_notifications_enabled = self.shift_update_notifications_enabled

        shift_report_enabled: bool | None | Unset
        if isinstance(self.shift_report_enabled, Unset):
            shift_report_enabled = UNSET
        else:
            shift_report_enabled = self.shift_report_enabled

        shift_report_day_of_week: str | Unset = UNSET
        if not isinstance(self.shift_report_day_of_week, Unset):
            shift_report_day_of_week = self.shift_report_day_of_week

        shift_report_time_of_day: None | str | Unset
        if isinstance(self.shift_report_time_of_day, Unset):
            shift_report_time_of_day = UNSET
        else:
            shift_report_time_of_day = self.shift_report_time_of_day

        shift_report_time_zone: None | str | Unset
        if isinstance(self.shift_report_time_zone, Unset):
            shift_report_time_zone = UNSET
        else:
            shift_report_time_zone = self.shift_report_time_zone

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "owner_user_id": owner_user_id,
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
        from ..models.new_schedule_data_attributes_slack_channel_type_0 import (
            NewScheduleDataAttributesSlackChannelType0,
        )
        from ..models.new_schedule_data_attributes_slack_user_group import NewScheduleDataAttributesSlackUserGroup

        d = dict(src_dict)
        name = d.pop("name")

        owner_user_id = d.pop("owner_user_id")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_all_time_coverage(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        all_time_coverage = _parse_all_time_coverage(d.pop("all_time_coverage", UNSET))

        _slack_user_group = d.pop("slack_user_group", UNSET)
        slack_user_group: NewScheduleDataAttributesSlackUserGroup | Unset
        if isinstance(_slack_user_group, Unset):
            slack_user_group = UNSET
        else:
            slack_user_group = NewScheduleDataAttributesSlackUserGroup.from_dict(_slack_user_group)

        def _parse_slack_channel(data: object) -> NewScheduleDataAttributesSlackChannelType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                slack_channel_type_0 = NewScheduleDataAttributesSlackChannelType0.from_dict(data)

                return slack_channel_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewScheduleDataAttributesSlackChannelType0 | None | Unset, data)

        slack_channel = _parse_slack_channel(d.pop("slack_channel", UNSET))

        owner_group_ids = cast(list[str], d.pop("owner_group_ids", UNSET))

        def _parse_sync_linear_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        sync_linear_enabled = _parse_sync_linear_enabled(d.pop("sync_linear_enabled", UNSET))

        def _parse_include_shadows_in_slack_notifications(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_shadows_in_slack_notifications = _parse_include_shadows_in_slack_notifications(
            d.pop("include_shadows_in_slack_notifications", UNSET)
        )

        def _parse_shift_start_notifications_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        shift_start_notifications_enabled = _parse_shift_start_notifications_enabled(
            d.pop("shift_start_notifications_enabled", UNSET)
        )

        def _parse_shift_update_notifications_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        shift_update_notifications_enabled = _parse_shift_update_notifications_enabled(
            d.pop("shift_update_notifications_enabled", UNSET)
        )

        def _parse_shift_report_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        shift_report_enabled = _parse_shift_report_enabled(d.pop("shift_report_enabled", UNSET))

        _shift_report_day_of_week = d.pop("shift_report_day_of_week", UNSET)
        shift_report_day_of_week: NewScheduleDataAttributesShiftReportDayOfWeek | Unset
        if isinstance(_shift_report_day_of_week, Unset):
            shift_report_day_of_week = UNSET
        else:
            shift_report_day_of_week = check_new_schedule_data_attributes_shift_report_day_of_week(
                _shift_report_day_of_week
            )

        def _parse_shift_report_time_of_day(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        shift_report_time_of_day = _parse_shift_report_time_of_day(d.pop("shift_report_time_of_day", UNSET))

        def _parse_shift_report_time_zone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        shift_report_time_zone = _parse_shift_report_time_zone(d.pop("shift_report_time_zone", UNSET))

        new_schedule_data_attributes = cls(
            name=name,
            owner_user_id=owner_user_id,
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

        return new_schedule_data_attributes
