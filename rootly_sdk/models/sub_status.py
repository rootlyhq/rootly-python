from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sub_status_parent_status import SubStatusParentStatus, check_sub_status_parent_status
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubStatus")


@_attrs_define
class SubStatus:
    """
    Attributes:
        name (str):
        parent_status (SubStatusParentStatus):
        created_at (str):
        updated_at (str):
        slug (Union[Unset, str]):
        description (Union[None, Unset, str]):
        position (Union[None, Unset, int]):
    """

    name: str
    parent_status: SubStatusParentStatus
    created_at: str
    updated_at: str
    slug: Unset | str = UNSET
    description: None | Unset | str = UNSET
    position: None | Unset | int = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        parent_status: str = self.parent_status

        created_at = self.created_at

        updated_at = self.updated_at

        slug = self.slug

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        position: None | Unset | int
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "parent_status": parent_status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if description is not UNSET:
            field_dict["description"] = description
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        parent_status = check_sub_status_parent_status(d.pop("parent_status"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        slug = d.pop("slug", UNSET)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_position(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        position = _parse_position(d.pop("position", UNSET))

        sub_status = cls(
            name=name,
            parent_status=parent_status,
            created_at=created_at,
            updated_at=updated_at,
            slug=slug,
            description=description,
            position=position,
        )

        sub_status.additional_properties = d
        return sub_status

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
