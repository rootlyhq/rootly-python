from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewRetrospectiveStepDataAttributes")


@_attrs_define
class NewRetrospectiveStepDataAttributes:
    """
    Attributes:
        title (str): The name of the step
        description (None | str | Unset): The description of the step
        due_after_days (int | None | Unset): Due date in days
        incident_role_id (None | str | Unset): Users assigned to the selected incident role will be the default owners
            for this step
        position (int | None | Unset): Position of the step
        skippable (bool | Unset): Is the step skippable?
    """

    title: str
    description: None | str | Unset = UNSET
    due_after_days: int | None | Unset = UNSET
    incident_role_id: None | str | Unset = UNSET
    position: int | None | Unset = UNSET
    skippable: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        due_after_days: int | None | Unset
        if isinstance(self.due_after_days, Unset):
            due_after_days = UNSET
        else:
            due_after_days = self.due_after_days

        incident_role_id: None | str | Unset
        if isinstance(self.incident_role_id, Unset):
            incident_role_id = UNSET
        else:
            incident_role_id = self.incident_role_id

        position: int | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        skippable = self.skippable

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "title": title,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if due_after_days is not UNSET:
            field_dict["due_after_days"] = due_after_days
        if incident_role_id is not UNSET:
            field_dict["incident_role_id"] = incident_role_id
        if position is not UNSET:
            field_dict["position"] = position
        if skippable is not UNSET:
            field_dict["skippable"] = skippable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_due_after_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        due_after_days = _parse_due_after_days(d.pop("due_after_days", UNSET))

        def _parse_incident_role_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        incident_role_id = _parse_incident_role_id(d.pop("incident_role_id", UNSET))

        def _parse_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        skippable = d.pop("skippable", UNSET)

        new_retrospective_step_data_attributes = cls(
            title=title,
            description=description,
            due_after_days=due_after_days,
            incident_role_id=incident_role_id,
            position=position,
            skippable=skippable,
        )

        return new_retrospective_step_data_attributes
