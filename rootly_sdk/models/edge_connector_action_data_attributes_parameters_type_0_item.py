from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edge_connector_action_data_attributes_parameters_type_0_item_type import (
    EdgeConnectorActionDataAttributesParametersType0ItemType,
    check_edge_connector_action_data_attributes_parameters_type_0_item_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EdgeConnectorActionDataAttributesParametersType0Item")


@_attrs_define
class EdgeConnectorActionDataAttributesParametersType0Item:
    """
    Attributes:
        name (Union[Unset, str]):
        type_ (Union[Unset, EdgeConnectorActionDataAttributesParametersType0ItemType]):
        required (Union[Unset, bool]):
        description (Union[None, Unset, str]):
        default (Union[None, Unset, str]): Default value (any type)
        options (Union[None, Unset, list[str]]):
    """

    name: Union[Unset, str] = UNSET
    type_: Union[Unset, EdgeConnectorActionDataAttributesParametersType0ItemType] = UNSET
    required: Union[Unset, bool] = UNSET
    description: Union[None, Unset, str] = UNSET
    default: Union[None, Unset, str] = UNSET
    options: Union[None, Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        required = self.required

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        default: Union[None, Unset, str]
        if isinstance(self.default, Unset):
            default = UNSET
        else:
            default = self.default

        options: Union[None, Unset, list[str]]
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, list):
            options = self.options

        else:
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
        if default is not UNSET:
            field_dict["default"] = default
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, EdgeConnectorActionDataAttributesParametersType0ItemType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_edge_connector_action_data_attributes_parameters_type_0_item_type(_type_)

        required = d.pop("required", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_default(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        default = _parse_default(d.pop("default", UNSET))

        def _parse_options(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                options_type_0 = cast(list[str], data)

                return options_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        options = _parse_options(d.pop("options", UNSET))

        edge_connector_action_data_attributes_parameters_type_0_item = cls(
            name=name,
            type_=type_,
            required=required,
            description=description,
            default=default,
            options=options,
        )

        edge_connector_action_data_attributes_parameters_type_0_item.additional_properties = d
        return edge_connector_action_data_attributes_parameters_type_0_item

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
