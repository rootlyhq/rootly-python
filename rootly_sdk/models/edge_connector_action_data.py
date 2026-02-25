from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edge_connector_action_data_type import EdgeConnectorActionDataType, check_edge_connector_action_data_type

if TYPE_CHECKING:
    from ..models.edge_connector_action_data_attributes import EdgeConnectorActionDataAttributes


T = TypeVar("T", bound="EdgeConnectorActionData")


@_attrs_define
class EdgeConnectorActionData:
    """
    Attributes:
        type_ (EdgeConnectorActionDataType):
        id (UUID):
        attributes (EdgeConnectorActionDataAttributes):
    """

    type_: EdgeConnectorActionDataType
    id: UUID
    attributes: "EdgeConnectorActionDataAttributes"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        id = str(self.id)

        attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.edge_connector_action_data_attributes import EdgeConnectorActionDataAttributes

        d = dict(src_dict)
        type_ = check_edge_connector_action_data_type(d.pop("type"))

        id = UUID(d.pop("id"))

        attributes = EdgeConnectorActionDataAttributes.from_dict(d.pop("attributes"))

        edge_connector_action_data = cls(
            type_=type_,
            id=id,
            attributes=attributes,
        )

        edge_connector_action_data.additional_properties = d
        return edge_connector_action_data

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
