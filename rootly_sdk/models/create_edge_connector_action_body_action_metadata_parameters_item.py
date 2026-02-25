from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_edge_connector_action_body_action_metadata_parameters_item_type import (
    CreateEdgeConnectorActionBodyActionMetadataParametersItemType,
    check_create_edge_connector_action_body_action_metadata_parameters_item_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateEdgeConnectorActionBodyActionMetadataParametersItem")


@_attrs_define
class CreateEdgeConnectorActionBodyActionMetadataParametersItem:
    """
    Attributes:
        name (Union[Unset, str]):
        type_ (Union[Unset, CreateEdgeConnectorActionBodyActionMetadataParametersItemType]):
        required (Union[Unset, bool]):
        description (Union[Unset, str]):
        options (Union[Unset, list[str]]):
    """

    name: Union[Unset, str] = UNSET
    type_: Union[Unset, CreateEdgeConnectorActionBodyActionMetadataParametersItemType] = UNSET
    required: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    options: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        required = self.required

        description = self.description

        options: Union[Unset, list[str]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if required is not UNSET:
            field_dict["required"] = required
        if description is not UNSET:
            field_dict["description"] = description
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, CreateEdgeConnectorActionBodyActionMetadataParametersItemType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_create_edge_connector_action_body_action_metadata_parameters_item_type(_type_)

        required = d.pop("required", UNSET)

        description = d.pop("description", UNSET)

        options = cast(list[str], d.pop("options", UNSET))

        create_edge_connector_action_body_action_metadata_parameters_item = cls(
            name=name,
            type_=type_,
            required=required,
            description=description,
            options=options,
        )

        create_edge_connector_action_body_action_metadata_parameters_item.additional_properties = d
        return create_edge_connector_action_body_action_metadata_parameters_item

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
