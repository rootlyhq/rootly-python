from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

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
        name (str | Unset): The name of the schedule
        description (None | str | Unset): The description of the schedule
        all_time_coverage (bool | None | Unset): 24/7 coverage of the schedule
        slack_user_group (UpdateScheduleDataAttributesSlackUserGroup | Unset):
        slack_channel (None | Unset | UpdateScheduleDataAttributesSlackChannelType0):
        owner_group_ids (list[str] | Unset): Owning teams.
        owner_user_id (int | None | Unset): ID of the owner of the schedule
    """

    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    all_time_coverage: bool | None | Unset = UNSET
    slack_user_group: UpdateScheduleDataAttributesSlackUserGroup | Unset = UNSET
    slack_channel: None | Unset | UpdateScheduleDataAttributesSlackChannelType0 = UNSET
    owner_group_ids: list[str] | Unset = UNSET
    owner_user_id: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_schedule_data_attributes_slack_channel_type_0 import (
            UpdateScheduleDataAttributesSlackChannelType0,
        )

        name = self.name

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
        elif isinstance(self.slack_channel, UpdateScheduleDataAttributesSlackChannelType0):
            slack_channel = self.slack_channel.to_dict()
        else:
            slack_channel = self.slack_channel

        owner_group_ids: list[str] | Unset = UNSET
        if not isinstance(self.owner_group_ids, Unset):
            owner_group_ids = self.owner_group_ids

        owner_user_id: int | None | Unset
        if isinstance(self.owner_user_id, Unset):
            owner_user_id = UNSET
        else:
            owner_user_id = self.owner_user_id

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_schedule_data_attributes_slack_channel_type_0 import (
            UpdateScheduleDataAttributesSlackChannelType0,
        )
        from ..models.update_schedule_data_attributes_slack_user_group import UpdateScheduleDataAttributesSlackUserGroup

        d = dict(src_dict)
        name = d.pop("name", UNSET)

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
        slack_user_group: UpdateScheduleDataAttributesSlackUserGroup | Unset
        if isinstance(_slack_user_group, Unset):
            slack_user_group = UNSET
        else:
            slack_user_group = UpdateScheduleDataAttributesSlackUserGroup.from_dict(_slack_user_group)

        def _parse_slack_channel(data: object) -> None | Unset | UpdateScheduleDataAttributesSlackChannelType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                slack_channel_type_0 = UpdateScheduleDataAttributesSlackChannelType0.from_dict(data)

                return slack_channel_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateScheduleDataAttributesSlackChannelType0, data)

        slack_channel = _parse_slack_channel(d.pop("slack_channel", UNSET))

        owner_group_ids = cast(list[str], d.pop("owner_group_ids", UNSET))

        def _parse_owner_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        owner_user_id = _parse_owner_user_id(d.pop("owner_user_id", UNSET))

        update_schedule_data_attributes = cls(
            name=name,
            description=description,
            all_time_coverage=all_time_coverage,
            slack_user_group=slack_user_group,
            slack_channel=slack_channel,
            owner_group_ids=owner_group_ids,
            owner_user_id=owner_user_id,
        )

        return update_schedule_data_attributes
