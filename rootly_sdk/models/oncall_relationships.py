from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.oncall_relationships_escalation_policy import OncallRelationshipsEscalationPolicy
    from ..models.oncall_relationships_schedule import OncallRelationshipsSchedule
    from ..models.oncall_relationships_user import OncallRelationshipsUser


T = TypeVar("T", bound="OncallRelationships")


@_attrs_define
class OncallRelationships:
    """
    Attributes:
        user (Union[Unset, OncallRelationshipsUser]):
        schedule (Union[Unset, OncallRelationshipsSchedule]):
        escalation_policy (Union[Unset, OncallRelationshipsEscalationPolicy]):
    """

    user: Union[Unset, "OncallRelationshipsUser"] = UNSET
    schedule: Union[Unset, "OncallRelationshipsSchedule"] = UNSET
    escalation_policy: Union[Unset, "OncallRelationshipsEscalationPolicy"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user: Unset | dict[str, Any] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        schedule: Unset | dict[str, Any] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        escalation_policy: Unset | dict[str, Any] = UNSET
        if not isinstance(self.escalation_policy, Unset):
            escalation_policy = self.escalation_policy.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if escalation_policy is not UNSET:
            field_dict["escalation_policy"] = escalation_policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.oncall_relationships_escalation_policy import OncallRelationshipsEscalationPolicy
        from ..models.oncall_relationships_schedule import OncallRelationshipsSchedule
        from ..models.oncall_relationships_user import OncallRelationshipsUser

        d = dict(src_dict)
        _user = d.pop("user", UNSET)
        user: Unset | OncallRelationshipsUser
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = OncallRelationshipsUser.from_dict(_user)

        _schedule = d.pop("schedule", UNSET)
        schedule: Unset | OncallRelationshipsSchedule
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = OncallRelationshipsSchedule.from_dict(_schedule)

        _escalation_policy = d.pop("escalation_policy", UNSET)
        escalation_policy: Unset | OncallRelationshipsEscalationPolicy
        if isinstance(_escalation_policy, Unset):
            escalation_policy = UNSET
        else:
            escalation_policy = OncallRelationshipsEscalationPolicy.from_dict(_escalation_policy)

        oncall_relationships = cls(
            user=user,
            schedule=schedule,
            escalation_policy=escalation_policy,
        )

        oncall_relationships.additional_properties = d
        return oncall_relationships

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
