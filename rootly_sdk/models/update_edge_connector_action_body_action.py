from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_edge_connector_action_body_action_action_type import (
    UpdateEdgeConnectorActionBodyActionActionType,
    check_update_edge_connector_action_body_action_action_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_edge_connector_action_body_action_metadata import UpdateEdgeConnectorActionBodyActionMetadata


T = TypeVar("T", bound="UpdateEdgeConnectorActionBodyAction")


@_attrs_define
class UpdateEdgeConnectorActionBodyAction:
    """
    Attributes:
        name (Union[Unset, str]):
        action_type (Union[Unset, UpdateEdgeConnectorActionBodyActionActionType]):
        metadata (Union[Unset, UpdateEdgeConnectorActionBodyActionMetadata]):
    """

    name: Union[Unset, str] = UNSET
    action_type: Union[Unset, UpdateEdgeConnectorActionBodyActionActionType] = UNSET
    metadata: Union[Unset, "UpdateEdgeConnectorActionBodyActionMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        action_type: Union[Unset, str] = UNSET
        if not isinstance(self.action_type, Unset):
            action_type = self.action_type

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if action_type is not UNSET:
            field_dict["action_type"] = action_type
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_edge_connector_action_body_action_metadata import (
            UpdateEdgeConnectorActionBodyActionMetadata,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _action_type = d.pop("action_type", UNSET)
        action_type: Union[Unset, UpdateEdgeConnectorActionBodyActionActionType]
        if isinstance(_action_type, Unset):
            action_type = UNSET
        else:
            action_type = check_update_edge_connector_action_body_action_action_type(_action_type)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, UpdateEdgeConnectorActionBodyActionMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = UpdateEdgeConnectorActionBodyActionMetadata.from_dict(_metadata)

        update_edge_connector_action_body_action = cls(
            name=name,
            action_type=action_type,
            metadata=metadata,
        )

        update_edge_connector_action_body_action.additional_properties = d
        return update_edge_connector_action_body_action

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
