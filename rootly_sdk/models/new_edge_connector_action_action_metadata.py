from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_edge_connector_action_action_metadata_icon import (
    NewEdgeConnectorActionActionMetadataIcon,
    check_new_edge_connector_action_action_metadata_icon,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_edge_connector_action_action_metadata_parameters_type_0_item import (
        NewEdgeConnectorActionActionMetadataParametersType0Item,
    )


T = TypeVar("T", bound="NewEdgeConnectorActionActionMetadata")


@_attrs_define
class NewEdgeConnectorActionActionMetadata:
    """
    Attributes:
        description (Union[None, Unset, str]):
        timeout (Union[None, Unset, int]):
        icon (Union[Unset, NewEdgeConnectorActionActionMetadataIcon]):
        parameters (Union[None, Unset, list['NewEdgeConnectorActionActionMetadataParametersType0Item']]):
    """

    description: Union[None, Unset, str] = UNSET
    timeout: Union[None, Unset, int] = UNSET
    icon: Union[Unset, NewEdgeConnectorActionActionMetadataIcon] = UNSET
    parameters: Union[None, Unset, list["NewEdgeConnectorActionActionMetadataParametersType0Item"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        timeout: Union[None, Unset, int]
        if isinstance(self.timeout, Unset):
            timeout = UNSET
        else:
            timeout = self.timeout

        icon: Union[Unset, str] = UNSET
        if not isinstance(self.icon, Unset):
            icon = self.icon

        parameters: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.parameters, Unset):
            parameters = UNSET
        elif isinstance(self.parameters, list):
            parameters = []
            for parameters_type_0_item_data in self.parameters:
                parameters_type_0_item = parameters_type_0_item_data.to_dict()
                parameters.append(parameters_type_0_item)

        else:
            parameters = self.parameters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if icon is not UNSET:
            field_dict["icon"] = icon
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_edge_connector_action_action_metadata_parameters_type_0_item import (
            NewEdgeConnectorActionActionMetadataParametersType0Item,
        )

        d = dict(src_dict)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_timeout(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        timeout = _parse_timeout(d.pop("timeout", UNSET))

        _icon = d.pop("icon", UNSET)
        icon: Union[Unset, NewEdgeConnectorActionActionMetadataIcon]
        if isinstance(_icon, Unset):
            icon = UNSET
        else:
            icon = check_new_edge_connector_action_action_metadata_icon(_icon)

        def _parse_parameters(
            data: object,
        ) -> Union[None, Unset, list["NewEdgeConnectorActionActionMetadataParametersType0Item"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                parameters_type_0 = []
                _parameters_type_0 = data
                for parameters_type_0_item_data in _parameters_type_0:
                    parameters_type_0_item = NewEdgeConnectorActionActionMetadataParametersType0Item.from_dict(
                        parameters_type_0_item_data
                    )

                    parameters_type_0.append(parameters_type_0_item)

                return parameters_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NewEdgeConnectorActionActionMetadataParametersType0Item"]], data)

        parameters = _parse_parameters(d.pop("parameters", UNSET))

        new_edge_connector_action_action_metadata = cls(
            description=description,
            timeout=timeout,
            icon=icon,
            parameters=parameters,
        )

        new_edge_connector_action_action_metadata.additional_properties = d
        return new_edge_connector_action_action_metadata

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
