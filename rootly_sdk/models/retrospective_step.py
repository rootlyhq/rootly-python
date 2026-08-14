from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RetrospectiveStep")


@_attrs_define
class RetrospectiveStep:
    """
    Attributes:
        retrospective_process_id (str):
        title (str): The name of the step
        created_at (str): Date of creation
        updated_at (str): Date of last update
        slug (Union[Unset, str]): The slug of the step
        description (Union[None, Unset, str]): The description of the step
        incident_role_id (Union[None, Unset, str]): Users assigned to the selected incident role will be the default
            owners for this step
        due_after_days (Union[None, Unset, int]): Due date in days
        position (Union[Unset, int]): Position of the step
        skippable (Union[Unset, bool]): Is the step skippable?
    """

    retrospective_process_id: str
    title: str
    created_at: str
    updated_at: str
    slug: Unset | str = UNSET
    description: None | Unset | str = UNSET
    incident_role_id: None | Unset | str = UNSET
    due_after_days: None | Unset | int = UNSET
    position: Unset | int = UNSET
    skippable: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        retrospective_process_id = self.retrospective_process_id

        title = self.title

        created_at = self.created_at

        updated_at = self.updated_at

        slug = self.slug

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        incident_role_id: None | Unset | str
        if isinstance(self.incident_role_id, Unset):
            incident_role_id = UNSET
        else:
            incident_role_id = self.incident_role_id

        due_after_days: None | Unset | int
        if isinstance(self.due_after_days, Unset):
            due_after_days = UNSET
        else:
            due_after_days = self.due_after_days

        position = self.position

        skippable = self.skippable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "retrospective_process_id": retrospective_process_id,
                "title": title,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if description is not UNSET:
            field_dict["description"] = description
        if incident_role_id is not UNSET:
            field_dict["incident_role_id"] = incident_role_id
        if due_after_days is not UNSET:
            field_dict["due_after_days"] = due_after_days
        if position is not UNSET:
            field_dict["position"] = position
        if skippable is not UNSET:
            field_dict["skippable"] = skippable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        retrospective_process_id = d.pop("retrospective_process_id")

        title = d.pop("title")

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

        def _parse_incident_role_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        incident_role_id = _parse_incident_role_id(d.pop("incident_role_id", UNSET))

        def _parse_due_after_days(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        due_after_days = _parse_due_after_days(d.pop("due_after_days", UNSET))

        position = d.pop("position", UNSET)

        skippable = d.pop("skippable", UNSET)

        retrospective_step = cls(
            retrospective_process_id=retrospective_process_id,
            title=title,
            created_at=created_at,
            updated_at=updated_at,
            slug=slug,
            description=description,
            incident_role_id=incident_role_id,
            due_after_days=due_after_days,
            position=position,
            skippable=skippable,
        )

        retrospective_step.additional_properties = d
        return retrospective_step

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
