from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_escalation_policy_path_data import UpdateEscalationPolicyPathData


T = TypeVar("T", bound="UpdateEscalationPolicyPath")


@_attrs_define
class UpdateEscalationPolicyPath:
    """
    Attributes:
        data (UpdateEscalationPolicyPathData):
    """

    data: UpdateEscalationPolicyPathData

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
        from ..models.update_escalation_policy_path_data import UpdateEscalationPolicyPathData

        d = dict(src_dict)
        data = UpdateEscalationPolicyPathData.from_dict(d.pop("data"))

        update_escalation_policy_path = cls(
            data=data,
        )

        return update_escalation_policy_path
