from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_policy_path_time_restrictions_item_end_day import (
    EscalationPolicyPathTimeRestrictionsItemEndDay,
    check_escalation_policy_path_time_restrictions_item_end_day,
)
from ..models.escalation_policy_path_time_restrictions_item_start_day import (
    EscalationPolicyPathTimeRestrictionsItemStartDay,
    check_escalation_policy_path_time_restrictions_item_start_day,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EscalationPolicyPathTimeRestrictionsItem")


@_attrs_define
class EscalationPolicyPathTimeRestrictionsItem:
    """
    Attributes:
        start_day (Union[Unset, EscalationPolicyPathTimeRestrictionsItemStartDay]):
        start_time (Union[Unset, str]): Formatted as HH:MM
        end_day (Union[Unset, EscalationPolicyPathTimeRestrictionsItemEndDay]):
        end_time (Union[Unset, str]): Formatted as HH:MM
    """

    start_day: Unset | EscalationPolicyPathTimeRestrictionsItemStartDay = UNSET
    start_time: Unset | str = UNSET
    end_day: Unset | EscalationPolicyPathTimeRestrictionsItemEndDay = UNSET
    end_time: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_day: Unset | str = UNSET
        if not isinstance(self.start_day, Unset):
            start_day = self.start_day

        start_time = self.start_time

        end_day: Unset | str = UNSET
        if not isinstance(self.end_day, Unset):
            end_day = self.end_day

        end_time = self.end_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_day is not UNSET:
            field_dict["start_day"] = start_day
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_day is not UNSET:
            field_dict["end_day"] = end_day
        if end_time is not UNSET:
            field_dict["end_time"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _start_day = d.pop("start_day", UNSET)
        start_day: Unset | EscalationPolicyPathTimeRestrictionsItemStartDay
        if isinstance(_start_day, Unset):
            start_day = UNSET
        else:
            start_day = check_escalation_policy_path_time_restrictions_item_start_day(_start_day)

        start_time = d.pop("start_time", UNSET)

        _end_day = d.pop("end_day", UNSET)
        end_day: Unset | EscalationPolicyPathTimeRestrictionsItemEndDay
        if isinstance(_end_day, Unset):
            end_day = UNSET
        else:
            end_day = check_escalation_policy_path_time_restrictions_item_end_day(_end_day)

        end_time = d.pop("end_time", UNSET)

        escalation_policy_path_time_restrictions_item = cls(
            start_day=start_day,
            start_time=start_time,
            end_day=end_day,
            end_time=end_time,
        )

        escalation_policy_path_time_restrictions_item.additional_properties = d
        return escalation_policy_path_time_restrictions_item

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
