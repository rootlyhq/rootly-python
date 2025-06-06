from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_policy_path_response_data_type import EscalationPolicyPathResponseDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.escalation_policy_path import EscalationPolicyPath


T = TypeVar("T", bound="EscalationPolicyPathResponseData")


@_attrs_define
class EscalationPolicyPathResponseData:
    """
    Attributes:
        id (str): Unique ID of the escalation policy path
        attributes (EscalationPolicyPath):
        type_ (Union[Unset, EscalationPolicyPathResponseDataType]):
    """

    id: str
    attributes: "EscalationPolicyPath"
    type_: Union[Unset, EscalationPolicyPathResponseDataType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        attributes = self.attributes.to_dict()

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "attributes": attributes,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.escalation_policy_path import EscalationPolicyPath

        d = src_dict.copy()
        id = d.pop("id")

        attributes = EscalationPolicyPath.from_dict(d.pop("attributes"))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, EscalationPolicyPathResponseDataType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = EscalationPolicyPathResponseDataType(_type_)

        escalation_policy_path_response_data = cls(
            id=id,
            attributes=attributes,
            type_=type_,
        )

        escalation_policy_path_response_data.additional_properties = d
        return escalation_policy_path_response_data

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
