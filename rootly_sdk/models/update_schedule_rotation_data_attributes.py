from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

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
        name (Union[Unset, str]): The name of the schedule rotation
        position (Union[Unset, int]): Position of the schedule rotation
        active_all_week (Union[Unset, bool]): Schedule rotation active all week? Default: True.
        active_days (Union[Unset, list[UpdateScheduleRotationDataAttributesActiveDaysItem]]):
        active_time_type (Union[Unset, str]):
        active_time_attributes (Union[Unset, list['UpdateScheduleRotationDataAttributesActiveTimeAttributesItem']]):
            Schedule rotation's active times
        time_zone (Union[Unset, str]): A valid IANA time zone name. Default: 'Etc/UTC'.
        schedule_rotationable_attributes
            (Union['UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType0',
            'UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType1',
            'UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType2',
            'UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType3', Unset]):
        start_time (Union[None, Unset, str]): ISO8601 date and time when rotation starts. Shifts will only be created
            after this time.
        end_time (Union[None, Unset, str]): ISO8601 date and time when rotation ends. Shifts will only be created before
            this time.
        schedule_rotation_members (Union[None, Unset,
            list['UpdateScheduleRotationDataAttributesScheduleRotationMembersType0Item']]): You can only update schedule
            rotation members if your account has schedule nesting feature enabled
    """

    schedule_rotationable_type: UpdateScheduleRotationDataAttributesScheduleRotationableType
    name: Unset | str = UNSET
    position: Unset | int = UNSET
    active_all_week: Unset | bool = True
    active_days: Unset | list[UpdateScheduleRotationDataAttributesActiveDaysItem] = UNSET
    active_time_type: Unset | str = UNSET
    active_time_attributes: Unset | list["UpdateScheduleRotationDataAttributesActiveTimeAttributesItem"] = UNSET
    time_zone: Unset | str = "Etc/UTC"
    schedule_rotationable_attributes: Union[
        "UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType0",
        "UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType1",
        "UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType2",
        "UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType3",
        Unset,
    ] = UNSET
    start_time: None | Unset | str = UNSET
    end_time: None | Unset | str = UNSET
    schedule_rotation_members: (
        None | Unset | list["UpdateScheduleRotationDataAttributesScheduleRotationMembersType0Item"]
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

        active_days: Unset | list[str] = UNSET
        if not isinstance(self.active_days, Unset):
            active_days = []
            for active_days_item_data in self.active_days:
                active_days_item: str = active_days_item_data
                active_days.append(active_days_item)

        active_time_type = self.active_time_type

        active_time_attributes: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.active_time_attributes, Unset):
            active_time_attributes = []
            for active_time_attributes_item_data in self.active_time_attributes:
                active_time_attributes_item = active_time_attributes_item_data.to_dict()
                active_time_attributes.append(active_time_attributes_item)

        time_zone = self.time_zone

        schedule_rotationable_attributes: Unset | dict[str, Any]
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

        start_time: None | Unset | str
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        else:
            start_time = self.start_time

        end_time: None | Unset | str
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        else:
            end_time = self.end_time

        schedule_rotation_members: None | Unset | list[dict[str, Any]]
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

        active_days = []
        _active_days = d.pop("active_days", UNSET)
        for active_days_item_data in _active_days or []:
            active_days_item = check_update_schedule_rotation_data_attributes_active_days_item(active_days_item_data)

            active_days.append(active_days_item)

        active_time_type = d.pop("active_time_type", UNSET)

        active_time_attributes = []
        _active_time_attributes = d.pop("active_time_attributes", UNSET)
        for active_time_attributes_item_data in _active_time_attributes or []:
            active_time_attributes_item = UpdateScheduleRotationDataAttributesActiveTimeAttributesItem.from_dict(
                active_time_attributes_item_data
            )

            active_time_attributes.append(active_time_attributes_item)

        time_zone = d.pop("time_zone", UNSET)

        def _parse_schedule_rotationable_attributes(
            data: object,
        ) -> Union[
            "UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType0",
            "UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType1",
            "UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType2",
            "UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType3",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schedule_rotationable_attributes_type_0 = (
                    UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType0.from_dict(data)
                )

                return schedule_rotationable_attributes_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schedule_rotationable_attributes_type_1 = (
                    UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType1.from_dict(data)
                )

                return schedule_rotationable_attributes_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schedule_rotationable_attributes_type_2 = (
                    UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType2.from_dict(data)
                )

                return schedule_rotationable_attributes_type_2
            except:  # noqa: E722
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

        def _parse_start_time(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        start_time = _parse_start_time(d.pop("start_time", UNSET))

        def _parse_end_time(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        end_time = _parse_end_time(d.pop("end_time", UNSET))

        def _parse_schedule_rotation_members(
            data: object,
        ) -> None | Unset | list["UpdateScheduleRotationDataAttributesScheduleRotationMembersType0Item"]:
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
            except:  # noqa: E722
                pass
            return cast(
                None | Unset | list["UpdateScheduleRotationDataAttributesScheduleRotationMembersType0Item"], data
            )

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
