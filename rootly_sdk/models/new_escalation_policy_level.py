from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_escalation_policy_level_data import NewEscalationPolicyLevelData


T = TypeVar("T", bound="NewEscalationPolicyLevel")


@_attrs_define
class NewEscalationPolicyLevel:
    """
    Attributes:
        data (NewEscalationPolicyLevelData):
    """

    data: NewEscalationPolicyLevelData

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_escalation_policy_level_data import NewEscalationPolicyLevelData

        d = dict(src_dict)
        data = NewEscalationPolicyLevelData.from_dict(d.pop("data"))

        new_escalation_policy_level = cls(
            data=data,
        )

        return new_escalation_policy_level
