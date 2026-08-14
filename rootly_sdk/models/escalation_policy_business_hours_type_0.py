from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_policy_business_hours_type_0_days_type_0_item import (
    EscalationPolicyBusinessHoursType0DaysType0Item,
    check_escalation_policy_business_hours_type_0_days_type_0_item,
)
from ..models.escalation_policy_business_hours_type_0_time_zone import (
    EscalationPolicyBusinessHoursType0TimeZone,
    check_escalation_policy_business_hours_type_0_time_zone,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EscalationPolicyBusinessHoursType0")


@_attrs_define
class EscalationPolicyBusinessHoursType0:
    """
    Attributes:
        time_zone (Union[Unset, EscalationPolicyBusinessHoursType0TimeZone]): Time zone for business hours
        days (Union[None, Unset, list[EscalationPolicyBusinessHoursType0DaysType0Item]]): Business days
        start_time (Union[None, Unset, str]): Start time for business hours (HH:MM)
        end_time (Union[None, Unset, str]): End time for business hours (HH:MM)
    """

    time_zone: Unset | EscalationPolicyBusinessHoursType0TimeZone = UNSET
    days: None | Unset | list[EscalationPolicyBusinessHoursType0DaysType0Item] = UNSET
    start_time: None | Unset | str = UNSET
    end_time: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_zone: Unset | str = UNSET
        if not isinstance(self.time_zone, Unset):
            time_zone = self.time_zone

        days: None | Unset | list[str]
        if isinstance(self.days, Unset):
            days = UNSET
        elif isinstance(self.days, list):
            days = []
            for days_type_0_item_data in self.days:
                days_type_0_item: str = days_type_0_item_data
                days.append(days_type_0_item)

        else:
            days = self.days

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone
        if days is not UNSET:
            field_dict["days"] = days
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _time_zone = d.pop("time_zone", UNSET)
        time_zone: Unset | EscalationPolicyBusinessHoursType0TimeZone
        if isinstance(_time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = check_escalation_policy_business_hours_type_0_time_zone(_time_zone)

        def _parse_days(data: object) -> None | Unset | list[EscalationPolicyBusinessHoursType0DaysType0Item]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                days_type_0 = []
                _days_type_0 = data
                for days_type_0_item_data in _days_type_0:
                    days_type_0_item = check_escalation_policy_business_hours_type_0_days_type_0_item(
                        days_type_0_item_data
                    )

                    days_type_0.append(days_type_0_item)

                return days_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[EscalationPolicyBusinessHoursType0DaysType0Item], data)

        days = _parse_days(d.pop("days", UNSET))

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

        escalation_policy_business_hours_type_0 = cls(
            time_zone=time_zone,
            days=days,
            start_time=start_time,
            end_time=end_time,
        )

        escalation_policy_business_hours_type_0.additional_properties = d
        return escalation_policy_business_hours_type_0

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
