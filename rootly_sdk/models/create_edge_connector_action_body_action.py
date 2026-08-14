from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_edge_connector_action_body_action_action_type import (
    CreateEdgeConnectorActionBodyActionActionType,
    check_create_edge_connector_action_body_action_action_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_edge_connector_action_body_action_metadata import CreateEdgeConnectorActionBodyActionMetadata


T = TypeVar("T", bound="CreateEdgeConnectorActionBodyAction")


@_attrs_define
class CreateEdgeConnectorActionBodyAction:
    """
    Attributes:
        name (str): Action name
        action_type (CreateEdgeConnectorActionBodyActionActionType): Action type
        metadata (Union[Unset, CreateEdgeConnectorActionBodyActionMetadata]):
    """

    name: str
    action_type: CreateEdgeConnectorActionBodyActionActionType
    metadata: Union[Unset, "CreateEdgeConnectorActionBodyActionMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        action_type: str = self.action_type

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "action_type": action_type,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_edge_connector_action_body_action_metadata import (
            CreateEdgeConnectorActionBodyActionMetadata,
        )

        d = dict(src_dict)
        name = d.pop("name")

        action_type = check_create_edge_connector_action_body_action_action_type(d.pop("action_type"))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, CreateEdgeConnectorActionBodyActionMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateEdgeConnectorActionBodyActionMetadata.from_dict(_metadata)

        create_edge_connector_action_body_action = cls(
            name=name,
            action_type=action_type,
            metadata=metadata,
        )

        create_edge_connector_action_body_action.additional_properties = d
        return create_edge_connector_action_body_action

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
