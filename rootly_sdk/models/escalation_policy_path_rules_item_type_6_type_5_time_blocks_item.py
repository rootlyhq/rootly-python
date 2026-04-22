from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EscalationPolicyPathRulesItemType6Type5TimeBlocksItem")


@_attrs_define
class EscalationPolicyPathRulesItemType6Type5TimeBlocksItem:
    """
    Attributes:
        monday (bool | None | Unset):
        tuesday (bool | None | Unset):
        wednesday (bool | None | Unset):
        thursday (bool | None | Unset):
        friday (bool | None | Unset):
        saturday (bool | None | Unset):
        sunday (bool | None | Unset):
        start_time (str | Unset): Formatted as HH:MM
        end_time (str | Unset): Formatted as HH:MM
        all_day (bool | None | Unset):
        position (int | None | Unset):
    """

    monday: bool | None | Unset = UNSET
    tuesday: bool | None | Unset = UNSET
    wednesday: bool | None | Unset = UNSET
    thursday: bool | None | Unset = UNSET
    friday: bool | None | Unset = UNSET
    saturday: bool | None | Unset = UNSET
    sunday: bool | None | Unset = UNSET
    start_time: str | Unset = UNSET
    end_time: str | Unset = UNSET
    all_day: bool | None | Unset = UNSET
    position: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monday: bool | None | Unset
        if isinstance(self.monday, Unset):
            monday = UNSET
        else:
            monday = self.monday

        tuesday: bool | None | Unset
        if isinstance(self.tuesday, Unset):
            tuesday = UNSET
        else:
            tuesday = self.tuesday

        wednesday: bool | None | Unset
        if isinstance(self.wednesday, Unset):
            wednesday = UNSET
        else:
            wednesday = self.wednesday

        thursday: bool | None | Unset
        if isinstance(self.thursday, Unset):
            thursday = UNSET
        else:
            thursday = self.thursday

        friday: bool | None | Unset
        if isinstance(self.friday, Unset):
            friday = UNSET
        else:
            friday = self.friday

        saturday: bool | None | Unset
        if isinstance(self.saturday, Unset):
            saturday = UNSET
        else:
            saturday = self.saturday

        sunday: bool | None | Unset
        if isinstance(self.sunday, Unset):
            sunday = UNSET
        else:
            sunday = self.sunday

        start_time = self.start_time

        end_time = self.end_time

        all_day: bool | None | Unset
        if isinstance(self.all_day, Unset):
            all_day = UNSET
        else:
            all_day = self.all_day

        position: int | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if monday is not UNSET:
            field_dict["monday"] = monday
        if tuesday is not UNSET:
            field_dict["tuesday"] = tuesday
        if wednesday is not UNSET:
            field_dict["wednesday"] = wednesday
        if thursday is not UNSET:
            field_dict["thursday"] = thursday
        if friday is not UNSET:
            field_dict["friday"] = friday
        if saturday is not UNSET:
            field_dict["saturday"] = saturday
        if sunday is not UNSET:
            field_dict["sunday"] = sunday
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if all_day is not UNSET:
            field_dict["all_day"] = all_day
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_monday(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        monday = _parse_monday(d.pop("monday", UNSET))

        def _parse_tuesday(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        tuesday = _parse_tuesday(d.pop("tuesday", UNSET))

        def _parse_wednesday(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        wednesday = _parse_wednesday(d.pop("wednesday", UNSET))

        def _parse_thursday(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        thursday = _parse_thursday(d.pop("thursday", UNSET))

        def _parse_friday(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        friday = _parse_friday(d.pop("friday", UNSET))

        def _parse_saturday(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        saturday = _parse_saturday(d.pop("saturday", UNSET))

        def _parse_sunday(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        sunday = _parse_sunday(d.pop("sunday", UNSET))

        start_time = d.pop("start_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        def _parse_all_day(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        all_day = _parse_all_day(d.pop("all_day", UNSET))

        def _parse_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        escalation_policy_path_rules_item_type_6_type_5_time_blocks_item = cls(
            monday=monday,
            tuesday=tuesday,
            wednesday=wednesday,
            thursday=thursday,
            friday=friday,
            saturday=saturday,
            sunday=sunday,
            start_time=start_time,
            end_time=end_time,
            all_day=all_day,
            position=position,
        )

        escalation_policy_path_rules_item_type_6_type_5_time_blocks_item.additional_properties = d
        return escalation_policy_path_rules_item_type_6_type_5_time_blocks_item

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
