from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_escalation_policy_data_attributes_business_hours_type_0 import (
        NewEscalationPolicyDataAttributesBusinessHoursType0,
    )


T = TypeVar("T", bound="NewEscalationPolicyDataAttributes")


@_attrs_define
class NewEscalationPolicyDataAttributes:
    """
    Attributes:
        name (str): The name of the escalation policy
        description (None | str | Unset): The description of the escalation policy
        repeat_count (int | Unset): The number of times this policy will be executed until someone acknowledges the
            alert
        group_ids (list[str] | Unset): Associated groups (alerting the group will trigger escalation policy)
        service_ids (list[str] | Unset): Associated services (alerting the service will trigger escalation policy)
        business_hours (NewEscalationPolicyDataAttributesBusinessHoursType0 | None | Unset):
    """

    name: str
    description: None | str | Unset = UNSET
    repeat_count: int | Unset = UNSET
    group_ids: list[str] | Unset = UNSET
    service_ids: list[str] | Unset = UNSET
    business_hours: NewEscalationPolicyDataAttributesBusinessHoursType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.new_escalation_policy_data_attributes_business_hours_type_0 import (
            NewEscalationPolicyDataAttributesBusinessHoursType0,
        )

        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        repeat_count = self.repeat_count

        group_ids: list[str] | Unset = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        service_ids: list[str] | Unset = UNSET
        if not isinstance(self.service_ids, Unset):
            service_ids = self.service_ids

        business_hours: dict[str, Any] | None | Unset
        if isinstance(self.business_hours, Unset):
            business_hours = UNSET
        elif isinstance(self.business_hours, NewEscalationPolicyDataAttributesBusinessHoursType0):
            business_hours = self.business_hours.to_dict()
        else:
            business_hours = self.business_hours

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if repeat_count is not UNSET:
            field_dict["repeat_count"] = repeat_count
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if service_ids is not UNSET:
            field_dict["service_ids"] = service_ids
        if business_hours is not UNSET:
            field_dict["business_hours"] = business_hours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_escalation_policy_data_attributes_business_hours_type_0 import (
            NewEscalationPolicyDataAttributesBusinessHoursType0,
        )

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        repeat_count = d.pop("repeat_count", UNSET)

        group_ids = cast(list[str], d.pop("group_ids", UNSET))

        service_ids = cast(list[str], d.pop("service_ids", UNSET))

        def _parse_business_hours(data: object) -> NewEscalationPolicyDataAttributesBusinessHoursType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                business_hours_type_0 = NewEscalationPolicyDataAttributesBusinessHoursType0.from_dict(data)

                return business_hours_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewEscalationPolicyDataAttributesBusinessHoursType0 | None | Unset, data)

        business_hours = _parse_business_hours(d.pop("business_hours", UNSET))

        new_escalation_policy_data_attributes = cls(
            name=name,
            description=description,
            repeat_count=repeat_count,
            group_ids=group_ids,
            service_ids=service_ids,
            business_hours=business_hours,
        )

        return new_escalation_policy_data_attributes
