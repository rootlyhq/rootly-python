from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_escalation_policy_path_data_attributes_time_restrictions_item_end_day import (
    NewEscalationPolicyPathDataAttributesTimeRestrictionsItemEndDay,
    check_new_escalation_policy_path_data_attributes_time_restrictions_item_end_day,
)
from ..models.new_escalation_policy_path_data_attributes_time_restrictions_item_start_day import (
    NewEscalationPolicyPathDataAttributesTimeRestrictionsItemStartDay,
    check_new_escalation_policy_path_data_attributes_time_restrictions_item_start_day,
)

T = TypeVar("T", bound="NewEscalationPolicyPathDataAttributesTimeRestrictionsItem")


@_attrs_define
class NewEscalationPolicyPathDataAttributesTimeRestrictionsItem:
    """
    Attributes:
        start_day (NewEscalationPolicyPathDataAttributesTimeRestrictionsItemStartDay):
        start_time (str): Formatted as HH:MM
        end_day (NewEscalationPolicyPathDataAttributesTimeRestrictionsItemEndDay):
        end_time (str): Formatted as HH:MM
    """

    start_day: NewEscalationPolicyPathDataAttributesTimeRestrictionsItemStartDay
    start_time: str
    end_day: NewEscalationPolicyPathDataAttributesTimeRestrictionsItemEndDay
    end_time: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_day: str = self.start_day

        start_time = self.start_time

        end_day: str = self.end_day

        end_time = self.end_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_day": start_day,
                "start_time": start_time,
                "end_day": end_day,
                "end_time": end_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_day = check_new_escalation_policy_path_data_attributes_time_restrictions_item_start_day(
            d.pop("start_day")
        )

        start_time = d.pop("start_time")

        end_day = check_new_escalation_policy_path_data_attributes_time_restrictions_item_end_day(d.pop("end_day"))

        end_time = d.pop("end_time")

        new_escalation_policy_path_data_attributes_time_restrictions_item = cls(
            start_day=start_day,
            start_time=start_time,
            end_day=end_day,
            end_time=end_time,
        )

        new_escalation_policy_path_data_attributes_time_restrictions_item.additional_properties = d
        return new_escalation_policy_path_data_attributes_time_restrictions_item

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
