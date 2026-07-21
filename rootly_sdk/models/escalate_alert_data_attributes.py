from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="EscalateAlertDataAttributes")


@_attrs_define
class EscalateAlertDataAttributes:
    """
    Attributes:
        escalation_policy_id (str | Unset): The ID of the escalation policy to escalate to. If omitted, uses the alert's
            current escalation policy from metadata. Required for resolved alerts whose metadata may have been cleared.
        escalation_policy_level (int | Unset): The escalation policy level to escalate to. If omitted, defaults to the
            next level (same EP) or level 1 (different EP).
    """

    escalation_policy_id: str | Unset = UNSET
    escalation_policy_level: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        escalation_policy_id = self.escalation_policy_id

        escalation_policy_level = self.escalation_policy_level

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if escalation_policy_id is not UNSET:
            field_dict["escalation_policy_id"] = escalation_policy_id
        if escalation_policy_level is not UNSET:
            field_dict["escalation_policy_level"] = escalation_policy_level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        escalation_policy_id = d.pop("escalation_policy_id", UNSET)

        escalation_policy_level = d.pop("escalation_policy_level", UNSET)

        escalate_alert_data_attributes = cls(
            escalation_policy_id=escalation_policy_id,
            escalation_policy_level=escalation_policy_level,
        )

        return escalate_alert_data_attributes
