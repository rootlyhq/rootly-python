from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
        description (None | str | Unset):
        timeout (int | None | Unset):
        icon (NewEdgeConnectorActionActionMetadataIcon | Unset):
        parameters (list[NewEdgeConnectorActionActionMetadataParametersType0Item] | None | Unset):
    """

    description: None | str | Unset = UNSET
    timeout: int | None | Unset = UNSET
    icon: NewEdgeConnectorActionActionMetadataIcon | Unset = UNSET
    parameters: list[NewEdgeConnectorActionActionMetadataParametersType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        timeout: int | None | Unset
        if isinstance(self.timeout, Unset):
            timeout = UNSET
        else:
            timeout = self.timeout

        icon: str | Unset = UNSET
        if not isinstance(self.icon, Unset):
            icon = self.icon

        parameters: list[dict[str, Any]] | None | Unset
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

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_timeout(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        timeout = _parse_timeout(d.pop("timeout", UNSET))

        _icon = d.pop("icon", UNSET)
        icon: NewEdgeConnectorActionActionMetadataIcon | Unset
        if isinstance(_icon, Unset):
            icon = UNSET
        else:
            icon = check_new_edge_connector_action_action_metadata_icon(_icon)

        def _parse_parameters(
            data: object,
        ) -> list[NewEdgeConnectorActionActionMetadataParametersType0Item] | None | Unset:
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
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[NewEdgeConnectorActionActionMetadataParametersType0Item] | None | Unset, data)

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
