from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
        created_at (str): Date of creation
        updated_at (str): Date of last update
        description (Union[None, Unset, str]): The description of the schedule
        all_time_coverage (Union[None, Unset, bool]): 24/7 coverage of the schedule
        slack_user_group (Union['ScheduleSlackUserGroupType0', None, Unset]): Synced slack group of the schedule
        slack_channel (Union['ScheduleSlackChannelType0', None, Unset]): Synced slack channel of the schedule
        owner_group_ids (Union[Unset, list[str]]): Owning teams.
        owner_user_id (Union[None, Unset, int]): ID of user assigned as owner of the schedule
    """

    name: str
    created_at: str
    updated_at: str
    description: Union[None, Unset, str] = UNSET
    all_time_coverage: Union[None, Unset, bool] = UNSET
    slack_user_group: Union["ScheduleSlackUserGroupType0", None, Unset] = UNSET
    slack_channel: Union["ScheduleSlackChannelType0", None, Unset] = UNSET
    owner_group_ids: Union[Unset, list[str]] = UNSET
    owner_user_id: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.schedule_slack_channel_type_0 import ScheduleSlackChannelType0
        from ..models.schedule_slack_user_group_type_0 import ScheduleSlackUserGroupType0

        name = self.name

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

        owner_user_id: Union[None, Unset, int]
        if isinstance(self.owner_user_id, Unset):
            owner_user_id = UNSET
        else:
            owner_user_id = self.owner_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
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
        if owner_user_id is not UNSET:
            field_dict["owner_user_id"] = owner_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schedule_slack_channel_type_0 import ScheduleSlackChannelType0
        from ..models.schedule_slack_user_group_type_0 import ScheduleSlackUserGroupType0

        d = dict(src_dict)
        name = d.pop("name")

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

        def _parse_owner_user_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        owner_user_id = _parse_owner_user_id(d.pop("owner_user_id", UNSET))

        schedule = cls(
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            all_time_coverage=all_time_coverage,
            slack_user_group=slack_user_group,
            slack_channel=slack_channel,
            owner_group_ids=owner_group_ids,
            owner_user_id=owner_user_id,
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
