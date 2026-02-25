from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_workflow_group_data_attributes_kind import (
    NewWorkflowGroupDataAttributesKind,
    check_new_workflow_group_data_attributes_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewWorkflowGroupDataAttributes")


@_attrs_define
class NewWorkflowGroupDataAttributes:
    """
    Attributes:
        name (str): The name of the workflow group.
        kind (Union[Unset, NewWorkflowGroupDataAttributesKind]): The kind of the workflow group
        description (Union[None, Unset, str]): A description of the workflow group.
        icon (Union[Unset, str]): An emoji icon displayed next to the workflow group.
        expanded (Union[Unset, bool]): Whether the group is expanded or collapsed.
        position (Union[Unset, int]): The position of the workflow group
    """

    name: str
    kind: Unset | NewWorkflowGroupDataAttributesKind = UNSET
    description: None | Unset | str = UNSET
    icon: Unset | str = UNSET
    expanded: Unset | bool = UNSET
    position: Unset | int = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        kind: Unset | str = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        icon = self.icon

        expanded = self.expanded

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if description is not UNSET:
            field_dict["description"] = description
        if icon is not UNSET:
            field_dict["icon"] = icon
        if expanded is not UNSET:
            field_dict["expanded"] = expanded
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        _kind = d.pop("kind", UNSET)
        kind: Unset | NewWorkflowGroupDataAttributesKind
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_new_workflow_group_data_attributes_kind(_kind)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        icon = d.pop("icon", UNSET)

        expanded = d.pop("expanded", UNSET)

        position = d.pop("position", UNSET)

        new_workflow_group_data_attributes = cls(
            name=name,
            kind=kind,
            description=description,
            icon=icon,
            expanded=expanded,
            position=position,
        )

        new_workflow_group_data_attributes.additional_properties = d
        return new_workflow_group_data_attributes

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
