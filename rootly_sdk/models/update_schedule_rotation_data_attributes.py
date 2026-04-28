from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_schedule_rotation_data_attributes_active_days_item import (
    UpdateScheduleRotationDataAttributesActiveDaysItem,
    check_update_schedule_rotation_data_attributes_active_days_item,
)
from ..models.update_schedule_rotation_data_attributes_schedule_rotationable_type import (
    UpdateScheduleRotationDataAttributesScheduleRotationableType,
    check_update_schedule_rotation_data_attributes_schedule_rotationable_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_schedule_rotation_data_attributes_active_time_attributes_item import (
        UpdateScheduleRotationDataAttributesActiveTimeAttributesItem,
    )
    from ..models.update_schedule_rotation_data_attributes_schedule_rotation_members_type_0_item import (
        UpdateScheduleRotationDataAttributesScheduleRotationMembersType0Item,
    )
    from ..models.update_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_0 import (
        UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType0,
    )
    from ..models.update_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_1 import (
        UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType1,
    )
    from ..models.update_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_2 import (
        UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType2,
    )
    from ..models.update_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_3 import (
        UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType3,
    )


T = TypeVar("T", bound="UpdateScheduleRotationDataAttributes")


@_attrs_define
class UpdateScheduleRotationDataAttributes:
    """
    Attributes:
        schedule_rotationable_type (UpdateScheduleRotationDataAttributesScheduleRotationableType): Schedule rotation
            type
        name (str | Unset): The name of the schedule rotation
        position (int | Unset): Position of the schedule rotation
        active_all_week (bool | Unset): Schedule rotation active all week? Default: True.
        active_days (list[UpdateScheduleRotationDataAttributesActiveDaysItem] | Unset):
        active_time_type (str | Unset):
        active_time_attributes (list[UpdateScheduleRotationDataAttributesActiveTimeAttributesItem] | Unset): Schedule
            rotation's active times
        time_zone (str | Unset): A valid IANA time zone name. Default: 'Etc/UTC'.
        schedule_rotationable_attributes (Unset |
            UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType0 |
            UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType1 |
            UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType2 |
            UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType3):
        start_time (None | str | Unset): ISO8601 date and time when rotation starts. Shifts will only be created after
            this time.
        end_time (None | str | Unset): ISO8601 date and time when rotation ends. Shifts will only be created before this
            time.
        schedule_rotation_members (list[UpdateScheduleRotationDataAttributesScheduleRotationMembersType0Item] | None |
            Unset): You can only update schedule rotation members if your account has schedule nesting feature enabled
    """

    schedule_rotationable_type: UpdateScheduleRotationDataAttributesScheduleRotationableType
    name: str | Unset = UNSET
    position: int | Unset = UNSET
    active_all_week: bool | Unset = True
    active_days: list[UpdateScheduleRotationDataAttributesActiveDaysItem] | Unset = UNSET
    active_time_type: str | Unset = UNSET
    active_time_attributes: list[UpdateScheduleRotationDataAttributesActiveTimeAttributesItem] | Unset = UNSET
    time_zone: str | Unset = "Etc/UTC"
    schedule_rotationable_attributes: (
        Unset
        | UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType0
        | UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType1
        | UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType2
        | UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType3
    ) = UNSET
    start_time: None | str | Unset = UNSET
    end_time: None | str | Unset = UNSET
    schedule_rotation_members: (
        list[UpdateScheduleRotationDataAttributesScheduleRotationMembersType0Item] | None | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_0 import (
            UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType0,
        )
        from ..models.update_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_1 import (
            UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType1,
        )
        from ..models.update_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_2 import (
            UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType2,
        )

        schedule_rotationable_type: str = self.schedule_rotationable_type

        name = self.name

        position = self.position

        active_all_week = self.active_all_week

        active_days: list[str] | Unset = UNSET
        if not isinstance(self.active_days, Unset):
            active_days = []
            for active_days_item_data in self.active_days:
                active_days_item: str = active_days_item_data
                active_days.append(active_days_item)

        active_time_type = self.active_time_type

        active_time_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.active_time_attributes, Unset):
            active_time_attributes = []
            for active_time_attributes_item_data in self.active_time_attributes:
                active_time_attributes_item = active_time_attributes_item_data.to_dict()
                active_time_attributes.append(active_time_attributes_item)

        time_zone = self.time_zone

        schedule_rotationable_attributes: dict[str, Any] | Unset
        if isinstance(self.schedule_rotationable_attributes, Unset):
            schedule_rotationable_attributes = UNSET
        elif isinstance(
            self.schedule_rotationable_attributes,
            UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType0,
        ):
            schedule_rotationable_attributes = self.schedule_rotationable_attributes.to_dict()
        elif isinstance(
            self.schedule_rotationable_attributes,
            UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType1,
        ):
            schedule_rotationable_attributes = self.schedule_rotationable_attributes.to_dict()
        elif isinstance(
            self.schedule_rotationable_attributes,
            UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType2,
        ):
            schedule_rotationable_attributes = self.schedule_rotationable_attributes.to_dict()
        else:
            schedule_rotationable_attributes = self.schedule_rotationable_attributes.to_dict()

        start_time: None | str | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        else:
            start_time = self.start_time

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        else:
            end_time = self.end_time

        schedule_rotation_members: list[dict[str, Any]] | None | Unset
        if isinstance(self.schedule_rotation_members, Unset):
            schedule_rotation_members = UNSET
        elif isinstance(self.schedule_rotation_members, list):
            schedule_rotation_members = []
            for schedule_rotation_members_type_0_item_data in self.schedule_rotation_members:
                schedule_rotation_members_type_0_item = schedule_rotation_members_type_0_item_data.to_dict()
                schedule_rotation_members.append(schedule_rotation_members_type_0_item)

        else:
            schedule_rotation_members = self.schedule_rotation_members

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "schedule_rotationable_type": schedule_rotationable_type,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if position is not UNSET:
            field_dict["position"] = position
        if active_all_week is not UNSET:
            field_dict["active_all_week"] = active_all_week
        if active_days is not UNSET:
            field_dict["active_days"] = active_days
        if active_time_type is not UNSET:
            field_dict["active_time_type"] = active_time_type
        if active_time_attributes is not UNSET:
            field_dict["active_time_attributes"] = active_time_attributes
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone
        if schedule_rotationable_attributes is not UNSET:
            field_dict["schedule_rotationable_attributes"] = schedule_rotationable_attributes
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if schedule_rotation_members is not UNSET:
            field_dict["schedule_rotation_members"] = schedule_rotation_members

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_schedule_rotation_data_attributes_active_time_attributes_item import (
            UpdateScheduleRotationDataAttributesActiveTimeAttributesItem,
        )
        from ..models.update_schedule_rotation_data_attributes_schedule_rotation_members_type_0_item import (
            UpdateScheduleRotationDataAttributesScheduleRotationMembersType0Item,
        )
        from ..models.update_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_0 import (
            UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType0,
        )
        from ..models.update_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_1 import (
            UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType1,
        )
        from ..models.update_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_2 import (
            UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType2,
        )
        from ..models.update_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_3 import (
            UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType3,
        )

        d = dict(src_dict)
        schedule_rotationable_type = check_update_schedule_rotation_data_attributes_schedule_rotationable_type(
            d.pop("schedule_rotationable_type")
        )

        name = d.pop("name", UNSET)

        position = d.pop("position", UNSET)

        active_all_week = d.pop("active_all_week", UNSET)

        _active_days = d.pop("active_days", UNSET)
        active_days: list[UpdateScheduleRotationDataAttributesActiveDaysItem] | Unset = UNSET
        if _active_days is not UNSET:
            active_days = []
            for active_days_item_data in _active_days:
                active_days_item = check_update_schedule_rotation_data_attributes_active_days_item(
                    active_days_item_data
                )

                active_days.append(active_days_item)

        active_time_type = d.pop("active_time_type", UNSET)

        _active_time_attributes = d.pop("active_time_attributes", UNSET)
        active_time_attributes: list[UpdateScheduleRotationDataAttributesActiveTimeAttributesItem] | Unset = UNSET
        if _active_time_attributes is not UNSET:
            active_time_attributes = []
            for active_time_attributes_item_data in _active_time_attributes:
                active_time_attributes_item = UpdateScheduleRotationDataAttributesActiveTimeAttributesItem.from_dict(
                    active_time_attributes_item_data
                )

                active_time_attributes.append(active_time_attributes_item)

        time_zone = d.pop("time_zone", UNSET)

        def _parse_schedule_rotationable_attributes(
            data: object,
        ) -> (
            Unset
            | UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType0
            | UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType1
            | UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType2
            | UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType3
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schedule_rotationable_attributes_type_0 = (
                    UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType0.from_dict(data)
                )

                return schedule_rotationable_attributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schedule_rotationable_attributes_type_1 = (
                    UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType1.from_dict(data)
                )

                return schedule_rotationable_attributes_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schedule_rotationable_attributes_type_2 = (
                    UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType2.from_dict(data)
                )

                return schedule_rotationable_attributes_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            schedule_rotationable_attributes_type_3 = (
                UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType3.from_dict(data)
            )

            return schedule_rotationable_attributes_type_3

        schedule_rotationable_attributes = _parse_schedule_rotationable_attributes(
            d.pop("schedule_rotationable_attributes", UNSET)
        )

        def _parse_start_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_time = _parse_start_time(d.pop("start_time", UNSET))

        def _parse_end_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_time = _parse_end_time(d.pop("end_time", UNSET))

        def _parse_schedule_rotation_members(
            data: object,
        ) -> list[UpdateScheduleRotationDataAttributesScheduleRotationMembersType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                schedule_rotation_members_type_0 = []
                _schedule_rotation_members_type_0 = data
                for schedule_rotation_members_type_0_item_data in _schedule_rotation_members_type_0:
                    schedule_rotation_members_type_0_item = (
                        UpdateScheduleRotationDataAttributesScheduleRotationMembersType0Item.from_dict(
                            schedule_rotation_members_type_0_item_data
                        )
                    )

                    schedule_rotation_members_type_0.append(schedule_rotation_members_type_0_item)

                return schedule_rotation_members_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UpdateScheduleRotationDataAttributesScheduleRotationMembersType0Item] | None | Unset, data)

        schedule_rotation_members = _parse_schedule_rotation_members(d.pop("schedule_rotation_members", UNSET))

        update_schedule_rotation_data_attributes = cls(
            schedule_rotationable_type=schedule_rotationable_type,
            name=name,
            position=position,
            active_all_week=active_all_week,
            active_days=active_days,
            active_time_type=active_time_type,
            active_time_attributes=active_time_attributes,
            time_zone=time_zone,
            schedule_rotationable_attributes=schedule_rotationable_attributes,
            start_time=start_time,
            end_time=end_time,
            schedule_rotation_members=schedule_rotation_members,
        )

        return update_schedule_rotation_data_attributes
