from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_event_schedule_type_0_escalation_policies_item import (
        AlertEventScheduleType0EscalationPoliciesItem,
    )


T = TypeVar("T", bound="AlertEventScheduleType0")


@_attrs_define
class AlertEventScheduleType0:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        description (None | str | Unset):
        escalation_policies (list[AlertEventScheduleType0EscalationPoliciesItem] | Unset):
        created_at (str | Unset):
        updated_at (str | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    escalation_policies: list[AlertEventScheduleType0EscalationPoliciesItem] | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        id = self.id

        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        escalation_policies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.escalation_policies, Unset):
            escalation_policies = []
            for escalation_policies_item_data in self.escalation_policies:
                escalation_policies_item = escalation_policies_item_data.to_dict()
                escalation_policies.append(escalation_policies_item)

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if escalation_policies is not UNSET:
            field_dict["escalation_policies"] = escalation_policies
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_event_schedule_type_0_escalation_policies_item import (
            AlertEventScheduleType0EscalationPoliciesItem,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _escalation_policies = d.pop("escalation_policies", UNSET)
        escalation_policies: list[AlertEventScheduleType0EscalationPoliciesItem] | Unset = UNSET
        if _escalation_policies is not UNSET:
            escalation_policies = []
            for escalation_policies_item_data in _escalation_policies:
                escalation_policies_item = AlertEventScheduleType0EscalationPoliciesItem.from_dict(
                    escalation_policies_item_data
                )

                escalation_policies.append(escalation_policies_item)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        alert_event_schedule_type_0 = cls(
            id=id,
            name=name,
            description=description,
            escalation_policies=escalation_policies,
            created_at=created_at,
            updated_at=updated_at,
        )

        alert_event_schedule_type_0.additional_properties = d
        return alert_event_schedule_type_0

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
