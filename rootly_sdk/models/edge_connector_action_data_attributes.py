import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.edge_connector_action_data_attributes_action_type import (
    EdgeConnectorActionDataAttributesActionType,
    check_edge_connector_action_data_attributes_action_type,
)
from ..models.edge_connector_action_data_attributes_icon import (
    EdgeConnectorActionDataAttributesIcon,
    check_edge_connector_action_data_attributes_icon,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edge_connector_action_data_attributes_parameters_type_0_item import (
        EdgeConnectorActionDataAttributesParametersType0Item,
    )


T = TypeVar("T", bound="EdgeConnectorActionDataAttributes")


@_attrs_define
class EdgeConnectorActionDataAttributes:
    """
    Attributes:
        name (str): Action name
        action_type (EdgeConnectorActionDataAttributesActionType): Action type
        slug (Union[Unset, str]): Action slug
        icon (Union[Unset, EdgeConnectorActionDataAttributesIcon]): Action icon
        description (Union[None, Unset, str]): Action description
        timeout (Union[None, Unset, int]): Timeout in seconds
        parameters (Union[None, Unset, list['EdgeConnectorActionDataAttributesParametersType0Item']]): Parameter
            definitions
        last_executed_at (Union[None, Unset, datetime.datetime]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    name: str
    action_type: EdgeConnectorActionDataAttributesActionType
    slug: Unset | str = UNSET
    icon: Unset | EdgeConnectorActionDataAttributesIcon = UNSET
    description: None | Unset | str = UNSET
    timeout: None | Unset | int = UNSET
    parameters: None | Unset | list["EdgeConnectorActionDataAttributesParametersType0Item"] = UNSET
    last_executed_at: None | Unset | datetime.datetime = UNSET
    created_at: Unset | datetime.datetime = UNSET
    updated_at: Unset | datetime.datetime = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        action_type: str = self.action_type

        slug = self.slug

        icon: Unset | str = UNSET
        if not isinstance(self.icon, Unset):
            icon = self.icon

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        timeout: None | Unset | int
        if isinstance(self.timeout, Unset):
            timeout = UNSET
        else:
            timeout = self.timeout

        parameters: None | Unset | list[dict[str, Any]]
        if isinstance(self.parameters, Unset):
            parameters = UNSET
        elif isinstance(self.parameters, list):
            parameters = []
            for parameters_type_0_item_data in self.parameters:
                parameters_type_0_item = parameters_type_0_item_data.to_dict()
                parameters.append(parameters_type_0_item)

        else:
            parameters = self.parameters

        last_executed_at: None | Unset | str
        if isinstance(self.last_executed_at, Unset):
            last_executed_at = UNSET
        elif isinstance(self.last_executed_at, datetime.datetime):
            last_executed_at = self.last_executed_at.isoformat()
        else:
            last_executed_at = self.last_executed_at

        created_at: Unset | str = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Unset | str = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "action_type": action_type,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if icon is not UNSET:
            field_dict["icon"] = icon
        if description is not UNSET:
            field_dict["description"] = description
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if last_executed_at is not UNSET:
            field_dict["last_executed_at"] = last_executed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.edge_connector_action_data_attributes_parameters_type_0_item import (
            EdgeConnectorActionDataAttributesParametersType0Item,
        )

        d = dict(src_dict)
        name = d.pop("name")

        action_type = check_edge_connector_action_data_attributes_action_type(d.pop("action_type"))

        slug = d.pop("slug", UNSET)

        _icon = d.pop("icon", UNSET)
        icon: Unset | EdgeConnectorActionDataAttributesIcon
        if isinstance(_icon, Unset):
            icon = UNSET
        else:
            icon = check_edge_connector_action_data_attributes_icon(_icon)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_timeout(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        timeout = _parse_timeout(d.pop("timeout", UNSET))

        def _parse_parameters(
            data: object,
        ) -> None | Unset | list["EdgeConnectorActionDataAttributesParametersType0Item"]:
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
                    parameters_type_0_item = EdgeConnectorActionDataAttributesParametersType0Item.from_dict(
                        parameters_type_0_item_data
                    )

                    parameters_type_0.append(parameters_type_0_item)

                return parameters_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list["EdgeConnectorActionDataAttributesParametersType0Item"], data)

        parameters = _parse_parameters(d.pop("parameters", UNSET))

        def _parse_last_executed_at(data: object) -> None | Unset | datetime.datetime:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_executed_at_type_0 = isoparse(data)

                return last_executed_at_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | datetime.datetime, data)

        last_executed_at = _parse_last_executed_at(d.pop("last_executed_at", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: Unset | datetime.datetime
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Unset | datetime.datetime
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        edge_connector_action_data_attributes = cls(
            name=name,
            action_type=action_type,
            slug=slug,
            icon=icon,
            description=description,
            timeout=timeout,
            parameters=parameters,
            last_executed_at=last_executed_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        edge_connector_action_data_attributes.additional_properties = d
        return edge_connector_action_data_attributes

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
