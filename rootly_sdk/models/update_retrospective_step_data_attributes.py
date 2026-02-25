from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateRetrospectiveStepDataAttributes")


@_attrs_define
class UpdateRetrospectiveStepDataAttributes:
    """
    Attributes:
        title (Union[Unset, str]): The name of the step
        description (Union[None, Unset, str]): The description of the step
        incident_role_id (Union[None, Unset, str]): Users assigned to the selected incident role will be the default
            owners for this step
        due_after_days (Union[None, Unset, int]): Due date in days
        position (Union[None, Unset, int]): Position of the step
        skippable (Union[Unset, bool]): Is the step skippable?
    """

    title: Unset | str = UNSET
    description: None | Unset | str = UNSET
    incident_role_id: None | Unset | str = UNSET
    due_after_days: None | Unset | int = UNSET
    position: None | Unset | int = UNSET
    skippable: Unset | bool = UNSET

    def to_dict(self) -> dict[str, Any]:
        title = self.title

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

        position: None | Unset | int
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        skippable = self.skippable

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
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
        title = d.pop("title", UNSET)

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

        def _parse_position(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        position = _parse_position(d.pop("position", UNSET))

        skippable = d.pop("skippable", UNSET)

        update_retrospective_step_data_attributes = cls(
            title=title,
            description=description,
            incident_role_id=incident_role_id,
            due_after_days=due_after_days,
            position=position,
            skippable=skippable,
        )

        return update_retrospective_step_data_attributes
