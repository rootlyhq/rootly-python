from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_incident_retrospective_step_data_attributes_status import (
    UpdateIncidentRetrospectiveStepDataAttributesStatus,
    check_update_incident_retrospective_step_data_attributes_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateIncidentRetrospectiveStepDataAttributes")


@_attrs_define
class UpdateIncidentRetrospectiveStepDataAttributes:
    """
    Attributes:
        title (Union[Unset, str]): The name of the incident retrospective step
        description (Union[None, Unset, str]): The description of the incident retrospective step
        due_date (Union[None, Unset, str]): Due date
        position (Union[None, Unset, int]): Position of the step
        skippable (Union[Unset, bool]): Is the step skippable?
        status (Union[Unset, UpdateIncidentRetrospectiveStepDataAttributesStatus]): Status of the incident retrospective
            step
    """

    title: Unset | str = UNSET
    description: None | Unset | str = UNSET
    due_date: None | Unset | str = UNSET
    position: None | Unset | int = UNSET
    skippable: Unset | bool = UNSET
    status: Unset | UpdateIncidentRetrospectiveStepDataAttributesStatus = UNSET

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        due_date: None | Unset | str
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        else:
            due_date = self.due_date

        position: None | Unset | int
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        skippable = self.skippable

        status: Unset | str = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if position is not UNSET:
            field_dict["position"] = position
        if skippable is not UNSET:
            field_dict["skippable"] = skippable
        if status is not UNSET:
            field_dict["status"] = status

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

        def _parse_due_date(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        due_date = _parse_due_date(d.pop("due_date", UNSET))

        def _parse_position(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        position = _parse_position(d.pop("position", UNSET))

        skippable = d.pop("skippable", UNSET)

        _status = d.pop("status", UNSET)
        status: Unset | UpdateIncidentRetrospectiveStepDataAttributesStatus
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_update_incident_retrospective_step_data_attributes_status(_status)

        update_incident_retrospective_step_data_attributes = cls(
            title=title,
            description=description,
            due_date=due_date,
            position=position,
            skippable=skippable,
            status=status,
        )

        return update_incident_retrospective_step_data_attributes
