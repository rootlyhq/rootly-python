from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.escalation_policy_path_response_data import EscalationPolicyPathResponseData


T = TypeVar("T", bound="EscalationPolicyPathResponse")


@_attrs_define
class EscalationPolicyPathResponse:
    """
    Attributes:
        data (EscalationPolicyPathResponseData):
    """

    data: EscalationPolicyPathResponseData
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.escalation_policy_path_response_data import EscalationPolicyPathResponseData

        d = dict(src_dict)
        data = EscalationPolicyPathResponseData.from_dict(d.pop("data"))

        escalation_policy_path_response = cls(
            data=data,
        )

        escalation_policy_path_response.additional_properties = d
        return escalation_policy_path_response

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
