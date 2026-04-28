from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.schedule_rotation_active_days_item import (
    ScheduleRotationActiveDaysItem,
    check_schedule_rotation_active_days_item,
)
from ..models.schedule_rotation_schedule_rotationable_type import (
    ScheduleRotationScheduleRotationableType,
    check_schedule_rotation_schedule_rotationable_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_rotation_active_time_attributes_item import ScheduleRotationActiveTimeAttributesItem
    from ..models.schedule_rotation_schedule_rotationable_attributes_type_0 import (
        ScheduleRotationScheduleRotationableAttributesType0,
    )
    from ..models.schedule_rotation_schedule_rotationable_attributes_type_1 import (
        ScheduleRotationScheduleRotationableAttributesType1,
    )
    from ..models.schedule_rotation_schedule_rotationable_attributes_type_2 import (
        ScheduleRotationScheduleRotationableAttributesType2,
    )
    from ..models.schedule_rotation_schedule_rotationable_attributes_type_3 import (
        ScheduleRotationScheduleRotationableAttributesType3,
    )


T = TypeVar("T", bound="ScheduleRotation")


@_attrs_define
class ScheduleRotation:
    """
    Attributes:
        schedule_id (str): The ID of parent schedule
        name (str): The name of the schedule rotation
        schedule_rotationable_type (ScheduleRotationScheduleRotationableType): Schedule rotation type
        schedule_rotationable_attributes (ScheduleRotationScheduleRotationableAttributesType0 |
            ScheduleRotationScheduleRotationableAttributesType1 | ScheduleRotationScheduleRotationableAttributesType2 |
            ScheduleRotationScheduleRotationableAttributesType3):
        position (int | Unset): Position of the schedule rotation
        active_all_week (bool | Unset): Schedule rotation active all week? Default: True.
        active_days (list[ScheduleRotationActiveDaysItem] | Unset):
        active_time_type (str | Unset):
        active_time_attributes (list[ScheduleRotationActiveTimeAttributesItem] | Unset): Schedule rotation's active
            times
        time_zone (str | Unset): A valid IANA time zone name. Default: 'Etc/UTC'.
        start_time (datetime.date | None | Unset): ISO8601 date and time when rotation starts. Shifts will only be
            created after this time.
        end_time (datetime.date | None | Unset): ISO8601 date and time when rotation ends. Shifts will only be created
            before this time.
    """

    schedule_id: str
    name: str
    schedule_rotationable_type: ScheduleRotationScheduleRotationableType
    schedule_rotationable_attributes: (
        ScheduleRotationScheduleRotationableAttributesType0
        | ScheduleRotationScheduleRotationableAttributesType1
        | ScheduleRotationScheduleRotationableAttributesType2
        | ScheduleRotationScheduleRotationableAttributesType3
    )
    position: int | Unset = UNSET
    active_all_week: bool | Unset = True
    active_days: list[ScheduleRotationActiveDaysItem] | Unset = UNSET
    active_time_type: str | Unset = UNSET
    active_time_attributes: list[ScheduleRotationActiveTimeAttributesItem] | Unset = UNSET
    time_zone: str | Unset = "Etc/UTC"
    start_time: datetime.date | None | Unset = UNSET
    end_time: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.schedule_rotation_schedule_rotationable_attributes_type_0 import (
            ScheduleRotationScheduleRotationableAttributesType0,
        )
        from ..models.schedule_rotation_schedule_rotationable_attributes_type_1 import (
            ScheduleRotationScheduleRotationableAttributesType1,
        )
        from ..models.schedule_rotation_schedule_rotationable_attributes_type_2 import (
            ScheduleRotationScheduleRotationableAttributesType2,
        )

        schedule_id = self.schedule_id

        name = self.name

        schedule_rotationable_type: str = self.schedule_rotationable_type

        schedule_rotationable_attributes: dict[str, Any]
        if isinstance(self.schedule_rotationable_attributes, ScheduleRotationScheduleRotationableAttributesType0):
            schedule_rotationable_attributes = self.schedule_rotationable_attributes.to_dict()
        elif isinstance(self.schedule_rotationable_attributes, ScheduleRotationScheduleRotationableAttributesType1):
            schedule_rotationable_attributes = self.schedule_rotationable_attributes.to_dict()
        elif isinstance(self.schedule_rotationable_attributes, ScheduleRotationScheduleRotationableAttributesType2):
            schedule_rotationable_attributes = self.schedule_rotationable_attributes.to_dict()
        else:
            schedule_rotationable_attributes = self.schedule_rotationable_attributes.to_dict()

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

        start_time: None | str | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        elif isinstance(self.start_time, datetime.date):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.date):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedule_id": schedule_id,
                "name": name,
                "schedule_rotationable_type": schedule_rotationable_type,
                "schedule_rotationable_attributes": schedule_rotationable_attributes,
            }
        )
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
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schedule_rotation_active_time_attributes_item import ScheduleRotationActiveTimeAttributesItem
        from ..models.schedule_rotation_schedule_rotationable_attributes_type_0 import (
            ScheduleRotationScheduleRotationableAttributesType0,
        )
        from ..models.schedule_rotation_schedule_rotationable_attributes_type_1 import (
            ScheduleRotationScheduleRotationableAttributesType1,
        )
        from ..models.schedule_rotation_schedule_rotationable_attributes_type_2 import (
            ScheduleRotationScheduleRotationableAttributesType2,
        )
        from ..models.schedule_rotation_schedule_rotationable_attributes_type_3 import (
            ScheduleRotationScheduleRotationableAttributesType3,
        )

        d = dict(src_dict)
        schedule_id = d.pop("schedule_id")

        name = d.pop("name")

        schedule_rotationable_type = check_schedule_rotation_schedule_rotationable_type(
            d.pop("schedule_rotationable_type")
        )

        def _parse_schedule_rotationable_attributes(
            data: object,
        ) -> (
            ScheduleRotationScheduleRotationableAttributesType0
            | ScheduleRotationScheduleRotationableAttributesType1
            | ScheduleRotationScheduleRotationableAttributesType2
            | ScheduleRotationScheduleRotationableAttributesType3
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schedule_rotationable_attributes_type_0 = ScheduleRotationScheduleRotationableAttributesType0.from_dict(
                    data
                )

                return schedule_rotationable_attributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schedule_rotationable_attributes_type_1 = ScheduleRotationScheduleRotationableAttributesType1.from_dict(
                    data
                )

                return schedule_rotationable_attributes_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schedule_rotationable_attributes_type_2 = ScheduleRotationScheduleRotationableAttributesType2.from_dict(
                    data
                )

                return schedule_rotationable_attributes_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            schedule_rotationable_attributes_type_3 = ScheduleRotationScheduleRotationableAttributesType3.from_dict(
                data
            )

            return schedule_rotationable_attributes_type_3

        schedule_rotationable_attributes = _parse_schedule_rotationable_attributes(
            d.pop("schedule_rotationable_attributes")
        )

        position = d.pop("position", UNSET)

        active_all_week = d.pop("active_all_week", UNSET)

        _active_days = d.pop("active_days", UNSET)
        active_days: list[ScheduleRotationActiveDaysItem] | Unset = UNSET
        if _active_days is not UNSET:
            active_days = []
            for active_days_item_data in _active_days:
                active_days_item = check_schedule_rotation_active_days_item(active_days_item_data)

                active_days.append(active_days_item)

        active_time_type = d.pop("active_time_type", UNSET)

        _active_time_attributes = d.pop("active_time_attributes", UNSET)
        active_time_attributes: list[ScheduleRotationActiveTimeAttributesItem] | Unset = UNSET
        if _active_time_attributes is not UNSET:
            active_time_attributes = []
            for active_time_attributes_item_data in _active_time_attributes:
                active_time_attributes_item = ScheduleRotationActiveTimeAttributesItem.from_dict(
                    active_time_attributes_item_data
                )

                active_time_attributes.append(active_time_attributes_item)

        time_zone = d.pop("time_zone", UNSET)

        def _parse_start_time(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_type_0 = isoparse(data).date()

                return start_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        start_time = _parse_start_time(d.pop("start_time", UNSET))

        def _parse_end_time(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = isoparse(data).date()

                return end_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        end_time = _parse_end_time(d.pop("end_time", UNSET))

        schedule_rotation = cls(
            schedule_id=schedule_id,
            name=name,
            schedule_rotationable_type=schedule_rotationable_type,
            schedule_rotationable_attributes=schedule_rotationable_attributes,
            position=position,
            active_all_week=active_all_week,
            active_days=active_days,
            active_time_type=active_time_type,
            active_time_attributes=active_time_attributes,
            time_zone=time_zone,
            start_time=start_time,
            end_time=end_time,
        )

        schedule_rotation.additional_properties = d
        return schedule_rotation

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
