from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_retrospective_step_status import (
    IncidentRetrospectiveStepStatus,
    check_incident_retrospective_step_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentRetrospectiveStep")


@_attrs_define
class IncidentRetrospectiveStep:
    """
    Attributes:
        retrospective_step_id (str):
        incident_id (str):
        title (str): The name of the step
        created_at (str): Date of creation
        updated_at (str): Date of last update
        description (Union[None, Unset, str]): The description of the step
        status (Union[Unset, IncidentRetrospectiveStepStatus]): Status of the incident retrospective step
        kind (Union[None, Unset, str]): Due date
        due_date (Union[None, Unset, str]): Due date
        position (Union[Unset, int]): Position of the step
        skippable (Union[Unset, bool]): Is the step skippable?
    """

    retrospective_step_id: str
    incident_id: str
    title: str
    created_at: str
    updated_at: str
    description: None | Unset | str = UNSET
    status: Unset | IncidentRetrospectiveStepStatus = UNSET
    kind: None | Unset | str = UNSET
    due_date: None | Unset | str = UNSET
    position: Unset | int = UNSET
    skippable: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        retrospective_step_id = self.retrospective_step_id

        incident_id = self.incident_id

        title = self.title

        created_at = self.created_at

        updated_at = self.updated_at

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        status: Unset | str = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        kind: None | Unset | str
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        due_date: None | Unset | str
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        else:
            due_date = self.due_date

        position = self.position

        skippable = self.skippable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "retrospective_step_id": retrospective_step_id,
                "incident_id": incident_id,
                "title": title,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if kind is not UNSET:
            field_dict["kind"] = kind
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if position is not UNSET:
            field_dict["position"] = position
        if skippable is not UNSET:
            field_dict["skippable"] = skippable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        retrospective_step_id = d.pop("retrospective_step_id")

        incident_id = d.pop("incident_id")

        title = d.pop("title")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        _status = d.pop("status", UNSET)
        status: Unset | IncidentRetrospectiveStepStatus
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_incident_retrospective_step_status(_status)

        def _parse_kind(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        kind = _parse_kind(d.pop("kind", UNSET))

        def _parse_due_date(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        due_date = _parse_due_date(d.pop("due_date", UNSET))

        position = d.pop("position", UNSET)

        skippable = d.pop("skippable", UNSET)

        incident_retrospective_step = cls(
            retrospective_step_id=retrospective_step_id,
            incident_id=incident_id,
            title=title,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            status=status,
            kind=kind,
            due_date=due_date,
            position=position,
            skippable=skippable,
        )

        incident_retrospective_step.additional_properties = d
        return incident_retrospective_step

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
