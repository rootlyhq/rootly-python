from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.escalation_policy_level import EscalationPolicyLevel


T = TypeVar("T", bound="EscalationPolicyLevelListDataItem")


@_attrs_define
class EscalationPolicyLevelListDataItem:
    """
    Attributes:
        id (str): Unique ID of the escalation policy level
        attributes (EscalationPolicyLevel):
    """

    id: str
    attributes: "EscalationPolicyLevel"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.escalation_policy_level import EscalationPolicyLevel

        d = src_dict.copy()
        id = d.pop("id")

        attributes = EscalationPolicyLevel.from_dict(d.pop("attributes"))

        escalation_policy_level_list_data_item = cls(
            id=id,
            attributes=attributes,
        )

        escalation_policy_level_list_data_item.additional_properties = d
        return escalation_policy_level_list_data_item

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
