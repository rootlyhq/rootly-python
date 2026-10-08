from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

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
        slug (None | str | Unset): Deprecated. `slug` is derived from `name` and `kind`; any submitted value is ignored.
            This property will be removed from the request schema in a future version.
        kind (NewWorkflowGroupDataAttributesKind | Unset): The kind of the workflow group
        description (None | str | Unset): A description of the workflow group.
        icon (str | Unset): An emoji icon displayed next to the workflow group.
        expanded (bool | Unset): Whether the group is expanded or collapsed.
        position (int | Unset): The position of the workflow group
    """

    name: str
    slug: None | str | Unset = UNSET
    kind: NewWorkflowGroupDataAttributesKind | Unset = UNSET
    description: None | str | Unset = UNSET
    icon: str | Unset = UNSET
    expanded: bool | Unset = UNSET
    position: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        icon = self.icon

        expanded = self.expanded

        position = self.position

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
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

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        _kind = d.pop("kind", UNSET)
        kind: NewWorkflowGroupDataAttributesKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_new_workflow_group_data_attributes_kind(_kind)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        icon = d.pop("icon", UNSET)

        expanded = d.pop("expanded", UNSET)

        position = d.pop("position", UNSET)

        new_workflow_group_data_attributes = cls(
            name=name,
            slug=slug,
            kind=kind,
            description=description,
            icon=icon,
            expanded=expanded,
            position=position,
        )

        return new_workflow_group_data_attributes
