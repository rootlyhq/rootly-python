from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.new_edge_connector_action_action import NewEdgeConnectorActionAction


T = TypeVar("T", bound="NewEdgeConnectorAction")


@_attrs_define
class NewEdgeConnectorAction:
    """
    Attributes:
        action (NewEdgeConnectorActionAction):
    """

    action: "NewEdgeConnectorActionAction"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_edge_connector_action_action import NewEdgeConnectorActionAction

        d = dict(src_dict)
        action = NewEdgeConnectorActionAction.from_dict(d.pop("action"))

        new_edge_connector_action = cls(
            action=action,
        )

        new_edge_connector_action.additional_properties = d
        return new_edge_connector_action

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
