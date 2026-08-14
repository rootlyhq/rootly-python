from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateEscalationPolicyPathDataAttributesRulesItemType9Type5TimeBlocksItem")


@_attrs_define
class UpdateEscalationPolicyPathDataAttributesRulesItemType9Type5TimeBlocksItem:
    """
    Attributes:
        monday (Union[Unset, bool]):  Default: False.
        tuesday (Union[Unset, bool]):  Default: False.
        wednesday (Union[Unset, bool]):  Default: False.
        thursday (Union[Unset, bool]):  Default: False.
        friday (Union[Unset, bool]):  Default: False.
        saturday (Union[Unset, bool]):  Default: False.
        sunday (Union[Unset, bool]):  Default: False.
        start_time (Union[Unset, str]): Formatted as HH:MM
        end_time (Union[Unset, str]): Formatted as HH:MM
        all_day (Union[Unset, bool]):  Default: False.
        position (Union[None, Unset, int]):
    """

    monday: Unset | bool = False
    tuesday: Unset | bool = False
    wednesday: Unset | bool = False
    thursday: Unset | bool = False
    friday: Unset | bool = False
    saturday: Unset | bool = False
    sunday: Unset | bool = False
    start_time: Unset | str = UNSET
    end_time: Unset | str = UNSET
    all_day: Unset | bool = False
    position: None | Unset | int = UNSET
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

        position: None | Unset | int
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

        def _parse_position(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        position = _parse_position(d.pop("position", UNSET))

        update_escalation_policy_path_data_attributes_rules_item_type_9_type_5_time_blocks_item = cls(
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

        update_escalation_policy_path_data_attributes_rules_item_type_9_type_5_time_blocks_item.additional_properties = d
        return update_escalation_policy_path_data_attributes_rules_item_type_9_type_5_time_blocks_item

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
