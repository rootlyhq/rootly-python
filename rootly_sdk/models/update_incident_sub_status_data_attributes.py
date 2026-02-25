from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateIncidentSubStatusDataAttributes")


@_attrs_define
class UpdateIncidentSubStatusDataAttributes:
    """
    Attributes:
        sub_status_id (Union[Unset, str]): Note: To change an incident's sub-status, use the PATCH /incidents/:id
            endpoint and set the sub_status_id attribute. This endpoint is for modifying the timestamp of when an incident's
            sub-status was assigned.
        assigned_at (Union[Unset, str]):
        assigned_by_user_id (Union[None, Unset, int]):
    """

    sub_status_id: Unset | str = UNSET
    assigned_at: Unset | str = UNSET
    assigned_by_user_id: None | Unset | int = UNSET

    def to_dict(self) -> dict[str, Any]:
        sub_status_id = self.sub_status_id

        assigned_at = self.assigned_at

        assigned_by_user_id: None | Unset | int
        if isinstance(self.assigned_by_user_id, Unset):
            assigned_by_user_id = UNSET
        else:
            assigned_by_user_id = self.assigned_by_user_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if sub_status_id is not UNSET:
            field_dict["sub_status_id"] = sub_status_id
        if assigned_at is not UNSET:
            field_dict["assigned_at"] = assigned_at
        if assigned_by_user_id is not UNSET:
            field_dict["assigned_by_user_id"] = assigned_by_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sub_status_id = d.pop("sub_status_id", UNSET)

        assigned_at = d.pop("assigned_at", UNSET)

        def _parse_assigned_by_user_id(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        assigned_by_user_id = _parse_assigned_by_user_id(d.pop("assigned_by_user_id", UNSET))

        update_incident_sub_status_data_attributes = cls(
            sub_status_id=sub_status_id,
            assigned_at=assigned_at,
            assigned_by_user_id=assigned_by_user_id,
        )

        return update_incident_sub_status_data_attributes
