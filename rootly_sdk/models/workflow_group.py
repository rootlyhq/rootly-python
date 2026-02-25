from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_group_kind import WorkflowGroupKind, check_workflow_group_kind
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowGroup")


@_attrs_define
class WorkflowGroup:
    """
    Attributes:
        name (str): The name of the workflow group.
        position (int): The position of the workflow group
        kind (Union[Unset, WorkflowGroupKind]): The kind of the workflow group
        slug (Union[Unset, str]): The slug of the workflow group.
        description (Union[None, Unset, str]): A description of the workflow group.
        icon (Union[Unset, str]): An emoji icon displayed next to the workflow group.
        expanded (Union[Unset, bool]): Whether the group is expanded or collapsed.
    """

    name: str
    position: int
    kind: Unset | WorkflowGroupKind = UNSET
    slug: Unset | str = UNSET
    description: None | Unset | str = UNSET
    icon: Unset | str = UNSET
    expanded: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        position = self.position

        kind: Unset | str = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        slug = self.slug

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        icon = self.icon

        expanded = self.expanded

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "position": position,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if slug is not UNSET:
            field_dict["slug"] = slug
        if description is not UNSET:
            field_dict["description"] = description
        if icon is not UNSET:
            field_dict["icon"] = icon
        if expanded is not UNSET:
            field_dict["expanded"] = expanded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        position = d.pop("position")

        _kind = d.pop("kind", UNSET)
        kind: Unset | WorkflowGroupKind
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_workflow_group_kind(_kind)

        slug = d.pop("slug", UNSET)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        icon = d.pop("icon", UNSET)

        expanded = d.pop("expanded", UNSET)

        workflow_group = cls(
            name=name,
            position=position,
            kind=kind,
            slug=slug,
            description=description,
            icon=icon,
            expanded=expanded,
        )

        workflow_group.additional_properties = d
        return workflow_group

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
