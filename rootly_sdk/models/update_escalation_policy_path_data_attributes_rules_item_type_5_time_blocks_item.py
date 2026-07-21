from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="UpdateEscalationPolicyPathDataAttributesRulesItemType5TimeBlocksItem")


@_attrs_define
class UpdateEscalationPolicyPathDataAttributesRulesItemType5TimeBlocksItem:
    """
    Attributes:
        monday (bool | Unset):  Default: False.
        tuesday (bool | Unset):  Default: False.
        wednesday (bool | Unset):  Default: False.
        thursday (bool | Unset):  Default: False.
        friday (bool | Unset):  Default: False.
        saturday (bool | Unset):  Default: False.
        sunday (bool | Unset):  Default: False.
        start_time (str | Unset): Formatted as HH:MM
        end_time (str | Unset): Formatted as HH:MM
        all_day (bool | Unset):  Default: False.
        position (int | None | Unset):
    """

    monday: bool | Unset = False
    tuesday: bool | Unset = False
    wednesday: bool | Unset = False
    thursday: bool | Unset = False
    friday: bool | Unset = False
    saturday: bool | Unset = False
    sunday: bool | Unset = False
    start_time: str | Unset = UNSET
    end_time: str | Unset = UNSET
    all_day: bool | Unset = False
    position: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monday = self.monday

        tuesday = self.tuesday

        wednesday = self.wednesday

        thursday = self.thursday

        friday = self.friday

        saturday = self.saturday

        sunday = self.sunday

        start_time = self.start_time

        end_time = self.end_time

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
        monday = d.pop("monday", UNSET)

        tuesday = d.pop("tuesday", UNSET)

        wednesday = d.pop("wednesday", UNSET)

        thursday = d.pop("thursday", UNSET)

        friday = d.pop("friday", UNSET)

        saturday = d.pop("saturday", UNSET)

        sunday = d.pop("sunday", UNSET)

        start_time = d.pop("start_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        all_day = d.pop("all_day", UNSET)

        def _parse_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        update_escalation_policy_path_data_attributes_rules_item_type_5_time_blocks_item = cls(
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

        update_escalation_policy_path_data_attributes_rules_item_type_5_time_blocks_item.additional_properties = d
        return update_escalation_policy_path_data_attributes_rules_item_type_5_time_blocks_item

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
