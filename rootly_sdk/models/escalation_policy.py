from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.escalation_policy_business_hours_type_0 import EscalationPolicyBusinessHoursType0


T = TypeVar("T", bound="EscalationPolicy")


@_attrs_define
class EscalationPolicy:
    """
    Attributes:
        name (str): The name of the escalation policy
        repeat_count (int): The number of times this policy will be executed until someone acknowledges the alert
        created_by_user_id (int): User who created the escalation policy
        description (Union[None, Unset, str]): The description of the escalation policy
        last_updated_by_user_id (Union[Unset, int]): User who updated the escalation policy
        group_ids (Union[Unset, list[str]]): Associated groups (alerting the group will trigger escalation policy)
        service_ids (Union[Unset, list[str]]): Associated services (alerting the service will trigger escalation policy)
        business_hours (Union['EscalationPolicyBusinessHoursType0', None, Unset]):
        created_at (Union[Unset, str]): Date of creation
        updated_at (Union[Unset, str]): Date of last update
    """

    name: str
    repeat_count: int
    created_by_user_id: int
    description: None | Unset | str = UNSET
    last_updated_by_user_id: Unset | int = UNSET
    group_ids: Unset | list[str] = UNSET
    service_ids: Unset | list[str] = UNSET
    business_hours: Union["EscalationPolicyBusinessHoursType0", None, Unset] = UNSET
    created_at: Unset | str = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.escalation_policy_business_hours_type_0 import EscalationPolicyBusinessHoursType0

        name = self.name

        repeat_count = self.repeat_count

        created_by_user_id = self.created_by_user_id

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        last_updated_by_user_id = self.last_updated_by_user_id

        group_ids: Unset | list[str] = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        service_ids: Unset | list[str] = UNSET
        if not isinstance(self.service_ids, Unset):
            service_ids = self.service_ids

        business_hours: None | Unset | dict[str, Any]
        if isinstance(self.business_hours, Unset):
            business_hours = UNSET
        elif isinstance(self.business_hours, EscalationPolicyBusinessHoursType0):
            business_hours = self.business_hours.to_dict()
        else:
            business_hours = self.business_hours

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "repeat_count": repeat_count,
                "created_by_user_id": created_by_user_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if last_updated_by_user_id is not UNSET:
            field_dict["last_updated_by_user_id"] = last_updated_by_user_id
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if service_ids is not UNSET:
            field_dict["service_ids"] = service_ids
        if business_hours is not UNSET:
            field_dict["business_hours"] = business_hours
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.escalation_policy_business_hours_type_0 import EscalationPolicyBusinessHoursType0

        d = dict(src_dict)
        name = d.pop("name")

        repeat_count = d.pop("repeat_count")

        created_by_user_id = d.pop("created_by_user_id")

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        last_updated_by_user_id = d.pop("last_updated_by_user_id", UNSET)

        group_ids = cast(list[str], d.pop("group_ids", UNSET))

        service_ids = cast(list[str], d.pop("service_ids", UNSET))

        def _parse_business_hours(data: object) -> Union["EscalationPolicyBusinessHoursType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                business_hours_type_0 = EscalationPolicyBusinessHoursType0.from_dict(data)

                return business_hours_type_0
            except:  # noqa: E722
                pass
            return cast(Union["EscalationPolicyBusinessHoursType0", None, Unset], data)

        business_hours = _parse_business_hours(d.pop("business_hours", UNSET))

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        escalation_policy = cls(
            name=name,
            repeat_count=repeat_count,
            created_by_user_id=created_by_user_id,
            description=description,
            last_updated_by_user_id=last_updated_by_user_id,
            group_ids=group_ids,
            service_ids=service_ids,
            business_hours=business_hours,
            created_at=created_at,
            updated_at=updated_at,
        )

        escalation_policy.additional_properties = d
        return escalation_policy

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
