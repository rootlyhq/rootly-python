from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_workflow_group_data_attributes_kind import (
    UpdateWorkflowGroupDataAttributesKind,
    check_update_workflow_group_data_attributes_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWorkflowGroupDataAttributes")


@_attrs_define
class UpdateWorkflowGroupDataAttributes:
    """
    Attributes:
        slug (Union[None, Unset, str]): Deprecated. `slug` is derived from `name` and `kind`; any submitted value is
            ignored. This property will be removed from the request schema in a future version.
        kind (Union[Unset, UpdateWorkflowGroupDataAttributesKind]): The kind of the workflow group
        name (Union[Unset, str]): The name of the workflow group.
        description (Union[None, Unset, str]): A description of the workflow group.
        icon (Union[Unset, str]): An emoji icon displayed next to the workflow group.
        expanded (Union[Unset, bool]): Whether the group is expanded or collapsed.
        position (Union[Unset, int]): The position of the workflow group
    """

    slug: Union[None, Unset, str] = UNSET
    kind: Union[Unset, UpdateWorkflowGroupDataAttributesKind] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    expanded: Union[Unset, bool] = UNSET
    position: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug: Union[None, Unset, str]
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        icon = self.icon

        expanded = self.expanded

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if slug is not UNSET:
            field_dict["slug"] = slug
        if kind is not UNSET:
            field_dict["kind"] = kind
        if name is not UNSET:
            field_dict["name"] = name
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

        def _parse_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        slug = _parse_slug(d.pop("slug", UNSET))

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, UpdateWorkflowGroupDataAttributesKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_update_workflow_group_data_attributes_kind(_kind)

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        icon = d.pop("icon", UNSET)

        expanded = d.pop("expanded", UNSET)

        position = d.pop("position", UNSET)

        update_workflow_group_data_attributes = cls(
            slug=slug,
            kind=kind,
            name=name,
            description=description,
            icon=icon,
            expanded=expanded,
            position=position,
        )

        update_workflow_group_data_attributes.additional_properties = d
        return update_workflow_group_data_attributes

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
