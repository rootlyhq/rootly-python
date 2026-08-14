from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.update_schedule_data_attributes_shift_report_day_of_week import (
    UpdateScheduleDataAttributesShiftReportDayOfWeek,
    check_update_schedule_data_attributes_shift_report_day_of_week,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_schedule_data_attributes_slack_channel_type_0 import (
        UpdateScheduleDataAttributesSlackChannelType0,
    )
    from ..models.update_schedule_data_attributes_slack_user_group import UpdateScheduleDataAttributesSlackUserGroup


T = TypeVar("T", bound="UpdateScheduleDataAttributes")


@_attrs_define
class UpdateScheduleDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The name of the schedule
        description (Union[None, Unset, str]): The description of the schedule
        all_time_coverage (Union[None, Unset, bool]): 24/7 coverage of the schedule
        slack_user_group (Union[Unset, UpdateScheduleDataAttributesSlackUserGroup]):
        slack_channel (Union['UpdateScheduleDataAttributesSlackChannelType0', None, Unset]):
        owner_group_ids (Union[Unset, list[str]]): Owning teams.
        owner_user_id (Union[None, Unset, int]): ID of the owner of the schedule
        sync_linear_enabled (Union[None, Unset, bool]): Whether the schedule is synced with Linear
        include_shadows_in_slack_notifications (Union[None, Unset, bool]): Whether shadow users are included in Slack
            notifications and user group syncing. Requires `slack_channel` to be set; otherwise this value is forced to
            false on save.
        shift_start_notifications_enabled (Union[None, Unset, bool]): Whether shift-start notifications are enabled.
            Requires `slack_channel` to be set; otherwise this value is forced to false on save.
        shift_update_notifications_enabled (Union[None, Unset, bool]): Whether shift-update notifications are enabled.
            Requires `slack_channel` to be set; otherwise this value is forced to false on save.
        shift_report_enabled (Union[None, Unset, bool]): Whether the weekly shift summary report is enabled. Requires
            `slack_channel` to be set; otherwise this value is forced to false on save.
        shift_report_day_of_week (Union[Unset, UpdateScheduleDataAttributesShiftReportDayOfWeek]): Day of week the
            weekly shift summary is sent
        shift_report_time_of_day (Union[None, Unset, str]): Time of day the weekly shift summary is sent, in HH:MM
            24-hour format
        shift_report_time_zone (Union[None, Unset, str]): IANA time zone used for the weekly shift summary
    """

    name: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    all_time_coverage: Union[None, Unset, bool] = UNSET
    slack_user_group: Union[Unset, "UpdateScheduleDataAttributesSlackUserGroup"] = UNSET
    slack_channel: Union["UpdateScheduleDataAttributesSlackChannelType0", None, Unset] = UNSET
    owner_group_ids: Union[Unset, list[str]] = UNSET
    owner_user_id: Union[None, Unset, int] = UNSET
    sync_linear_enabled: Union[None, Unset, bool] = UNSET
    include_shadows_in_slack_notifications: Union[None, Unset, bool] = UNSET
    shift_start_notifications_enabled: Union[None, Unset, bool] = UNSET
    shift_update_notifications_enabled: Union[None, Unset, bool] = UNSET
    shift_report_enabled: Union[None, Unset, bool] = UNSET
    shift_report_day_of_week: Union[Unset, UpdateScheduleDataAttributesShiftReportDayOfWeek] = UNSET
    shift_report_time_of_day: Union[None, Unset, str] = UNSET
    shift_report_time_zone: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_schedule_data_attributes_slack_channel_type_0 import (
            UpdateScheduleDataAttributesSlackChannelType0,
        )

        name = self.name

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

        slack_user_group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.slack_user_group, Unset):
            slack_user_group = self.slack_user_group.to_dict()

        slack_channel: Union[None, Unset, dict[str, Any]]
        if isinstance(self.slack_channel, Unset):
            slack_channel = UNSET
        elif isinstance(self.slack_channel, UpdateScheduleDataAttributesSlackChannelType0):
            slack_channel = self.slack_channel.to_dict()
        else:
            slack_channel = self.slack_channel

        owner_group_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.owner_group_ids, Unset):
            owner_group_ids = self.owner_group_ids

        owner_user_id: Union[None, Unset, int]
        if isinstance(self.owner_user_id, Unset):
            owner_user_id = UNSET
        else:
            owner_user_id = self.owner_user_id

        sync_linear_enabled: Union[None, Unset, bool]
        if isinstance(self.sync_linear_enabled, Unset):
            sync_linear_enabled = UNSET
        else:
            sync_linear_enabled = self.sync_linear_enabled

        include_shadows_in_slack_notifications: Union[None, Unset, bool]
        if isinstance(self.include_shadows_in_slack_notifications, Unset):
            include_shadows_in_slack_notifications = UNSET
        else:
            include_shadows_in_slack_notifications = self.include_shadows_in_slack_notifications

        shift_start_notifications_enabled: Union[None, Unset, bool]
        if isinstance(self.shift_start_notifications_enabled, Unset):
            shift_start_notifications_enabled = UNSET
        else:
            shift_start_notifications_enabled = self.shift_start_notifications_enabled

        shift_update_notifications_enabled: Union[None, Unset, bool]
        if isinstance(self.shift_update_notifications_enabled, Unset):
            shift_update_notifications_enabled = UNSET
        else:
            shift_update_notifications_enabled = self.shift_update_notifications_enabled

        shift_report_enabled: Union[None, Unset, bool]
        if isinstance(self.shift_report_enabled, Unset):
            shift_report_enabled = UNSET
        else:
            shift_report_enabled = self.shift_report_enabled

        shift_report_day_of_week: Union[Unset, str] = UNSET
        if not isinstance(self.shift_report_day_of_week, Unset):
            shift_report_day_of_week = self.shift_report_day_of_week

        shift_report_time_of_day: Union[None, Unset, str]
        if isinstance(self.shift_report_time_of_day, Unset):
            shift_report_time_of_day = UNSET
        else:
            shift_report_time_of_day = self.shift_report_time_of_day

        shift_report_time_zone: Union[None, Unset, str]
        if isinstance(self.shift_report_time_zone, Unset):
            shift_report_time_zone = UNSET
        else:
            shift_report_time_zone = self.shift_report_time_zone

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
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
        if owner_user_id is not UNSET:
            field_dict["owner_user_id"] = owner_user_id
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
        from ..models.update_schedule_data_attributes_slack_channel_type_0 import (
            UpdateScheduleDataAttributesSlackChannelType0,
        )
        from ..models.update_schedule_data_attributes_slack_user_group import UpdateScheduleDataAttributesSlackUserGroup

        d = dict(src_dict)
        name = d.pop("name", UNSET)

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

        _slack_user_group = d.pop("slack_user_group", UNSET)
        slack_user_group: Union[Unset, UpdateScheduleDataAttributesSlackUserGroup]
        if isinstance(_slack_user_group, Unset):
            slack_user_group = UNSET
        else:
            slack_user_group = UpdateScheduleDataAttributesSlackUserGroup.from_dict(_slack_user_group)

        def _parse_slack_channel(data: object) -> Union["UpdateScheduleDataAttributesSlackChannelType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                slack_channel_type_0 = UpdateScheduleDataAttributesSlackChannelType0.from_dict(data)

                return slack_channel_type_0
            except:  # noqa: E722
                pass
            return cast(Union["UpdateScheduleDataAttributesSlackChannelType0", None, Unset], data)

        slack_channel = _parse_slack_channel(d.pop("slack_channel", UNSET))

        owner_group_ids = cast(list[str], d.pop("owner_group_ids", UNSET))

        def _parse_owner_user_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        owner_user_id = _parse_owner_user_id(d.pop("owner_user_id", UNSET))

        def _parse_sync_linear_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        sync_linear_enabled = _parse_sync_linear_enabled(d.pop("sync_linear_enabled", UNSET))

        def _parse_include_shadows_in_slack_notifications(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        include_shadows_in_slack_notifications = _parse_include_shadows_in_slack_notifications(
            d.pop("include_shadows_in_slack_notifications", UNSET)
        )

        def _parse_shift_start_notifications_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        shift_start_notifications_enabled = _parse_shift_start_notifications_enabled(
            d.pop("shift_start_notifications_enabled", UNSET)
        )

        def _parse_shift_update_notifications_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        shift_update_notifications_enabled = _parse_shift_update_notifications_enabled(
            d.pop("shift_update_notifications_enabled", UNSET)
        )

        def _parse_shift_report_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        shift_report_enabled = _parse_shift_report_enabled(d.pop("shift_report_enabled", UNSET))

        _shift_report_day_of_week = d.pop("shift_report_day_of_week", UNSET)
        shift_report_day_of_week: Union[Unset, UpdateScheduleDataAttributesShiftReportDayOfWeek]
        if isinstance(_shift_report_day_of_week, Unset):
            shift_report_day_of_week = UNSET
        else:
            shift_report_day_of_week = check_update_schedule_data_attributes_shift_report_day_of_week(
                _shift_report_day_of_week
            )

        def _parse_shift_report_time_of_day(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shift_report_time_of_day = _parse_shift_report_time_of_day(d.pop("shift_report_time_of_day", UNSET))

        def _parse_shift_report_time_zone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shift_report_time_zone = _parse_shift_report_time_zone(d.pop("shift_report_time_zone", UNSET))

        update_schedule_data_attributes = cls(
            name=name,
            description=description,
            all_time_coverage=all_time_coverage,
            slack_user_group=slack_user_group,
            slack_channel=slack_channel,
            owner_group_ids=owner_group_ids,
            owner_user_id=owner_user_id,
            sync_linear_enabled=sync_linear_enabled,
            include_shadows_in_slack_notifications=include_shadows_in_slack_notifications,
            shift_start_notifications_enabled=shift_start_notifications_enabled,
            shift_update_notifications_enabled=shift_update_notifications_enabled,
            shift_report_enabled=shift_report_enabled,
            shift_report_day_of_week=shift_report_day_of_week,
            shift_report_time_of_day=shift_report_time_of_day,
            shift_report_time_zone=shift_report_time_zone,
        )

        return update_schedule_data_attributes
