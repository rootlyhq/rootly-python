from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_edge_connector_action_body_action_metadata_parameters_item import (
        CreateEdgeConnectorActionBodyActionMetadataParametersItem,
    )


T = TypeVar("T", bound="CreateEdgeConnectorActionBodyActionMetadata")


@_attrs_define
class CreateEdgeConnectorActionBodyActionMetadata:
    """
    Attributes:
        description (Union[Unset, str]):
        timeout (Union[Unset, int]):
        parameters (Union[Unset, list['CreateEdgeConnectorActionBodyActionMetadataParametersItem']]):
    """

    description: Unset | str = UNSET
    timeout: Unset | int = UNSET
    parameters: Unset | list["CreateEdgeConnectorActionBodyActionMetadataParametersItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        timeout = self.timeout

        parameters: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_edge_connector_action_body_action_metadata_parameters_item import (
            CreateEdgeConnectorActionBodyActionMetadataParametersItem,
        )

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        timeout = d.pop("timeout", UNSET)

        parameters = []
        _parameters = d.pop("parameters", UNSET)
        for parameters_item_data in _parameters or []:
            parameters_item = CreateEdgeConnectorActionBodyActionMetadataParametersItem.from_dict(parameters_item_data)

            parameters.append(parameters_item)

        create_edge_connector_action_body_action_metadata = cls(
            description=description,
            timeout=timeout,
            parameters=parameters,
        )

        create_edge_connector_action_body_action_metadata.additional_properties = d
        return create_edge_connector_action_body_action_metadata

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
