from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewRetrospectiveStepDataAttributes")


@_attrs_define
class NewRetrospectiveStepDataAttributes:
    """
    Attributes:
        title (str): The name of the step
        description (Union[None, Unset, str]): The description of the step
        due_after_days (Union[None, Unset, int]): Due date in days
        incident_role_id (Union[None, Unset, str]): Users assigned to the selected incident role will be the default
            owners for this step
        position (Union[None, Unset, int]): Position of the step
        skippable (Union[Unset, bool]): Is the step skippable?
    """

    title: str
    description: Union[None, Unset, str] = UNSET
    due_after_days: Union[None, Unset, int] = UNSET
    incident_role_id: Union[None, Unset, str] = UNSET
    position: Union[None, Unset, int] = UNSET
    skippable: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        due_after_days: Union[None, Unset, int]
        if isinstance(self.due_after_days, Unset):
            due_after_days = UNSET
        else:
            due_after_days = self.due_after_days

        incident_role_id: Union[None, Unset, str]
        if isinstance(self.incident_role_id, Unset):
            incident_role_id = UNSET
        else:
            incident_role_id = self.incident_role_id

        position: Union[None, Unset, int]
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_due_after_days(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        due_after_days = _parse_due_after_days(d.pop("due_after_days", UNSET))

        def _parse_incident_role_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        incident_role_id = _parse_incident_role_id(d.pop("incident_role_id", UNSET))

        def _parse_position(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

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
