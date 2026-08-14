from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_escalation_policy_data_attributes_business_hours_type_0 import (
        UpdateEscalationPolicyDataAttributesBusinessHoursType0,
    )


T = TypeVar("T", bound="UpdateEscalationPolicyDataAttributes")


@_attrs_define
class UpdateEscalationPolicyDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The name of the escalation policy
        description (Union[None, Unset, str]): The description of the escalation policy
        repeat_count (Union[Unset, int]): The number of times this policy will be executed until someone acknowledges
            the alert
        group_ids (Union[Unset, list[str]]): Associated groups (alerting the group will trigger escalation policy)
        service_ids (Union[Unset, list[str]]): Associated services (alerting the service will trigger escalation policy)
        business_hours (Union['UpdateEscalationPolicyDataAttributesBusinessHoursType0', None, Unset]):
    """

    name: Unset | str = UNSET
    description: None | Unset | str = UNSET
    repeat_count: Unset | int = UNSET
    group_ids: Unset | list[str] = UNSET
    service_ids: Unset | list[str] = UNSET
    business_hours: Union["UpdateEscalationPolicyDataAttributesBusinessHoursType0", None, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_escalation_policy_data_attributes_business_hours_type_0 import (
            UpdateEscalationPolicyDataAttributesBusinessHoursType0,
        )

        name = self.name

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        repeat_count = self.repeat_count

        group_ids: Unset | list[str] = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        service_ids: Unset | list[str] = UNSET
        if not isinstance(self.service_ids, Unset):
            service_ids = self.service_ids

        business_hours: None | Unset | dict[str, Any]
        if isinstance(self.business_hours, Unset):
            business_hours = UNSET
        elif isinstance(self.business_hours, UpdateEscalationPolicyDataAttributesBusinessHoursType0):
            business_hours = self.business_hours.to_dict()
        else:
            business_hours = self.business_hours

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
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
        from ..models.update_escalation_policy_data_attributes_business_hours_type_0 import (
            UpdateEscalationPolicyDataAttributesBusinessHoursType0,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        repeat_count = d.pop("repeat_count", UNSET)

        group_ids = cast(list[str], d.pop("group_ids", UNSET))

        service_ids = cast(list[str], d.pop("service_ids", UNSET))

        def _parse_business_hours(
            data: object,
        ) -> Union["UpdateEscalationPolicyDataAttributesBusinessHoursType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                business_hours_type_0 = UpdateEscalationPolicyDataAttributesBusinessHoursType0.from_dict(data)

                return business_hours_type_0
            except:  # noqa: E722
                pass
            return cast(Union["UpdateEscalationPolicyDataAttributesBusinessHoursType0", None, Unset], data)

        business_hours = _parse_business_hours(d.pop("business_hours", UNSET))

        update_escalation_policy_data_attributes = cls(
            name=name,
            description=description,
            repeat_count=repeat_count,
            group_ids=group_ids,
            service_ids=service_ids,
            business_hours=business_hours,
        )

        return update_escalation_policy_data_attributes
