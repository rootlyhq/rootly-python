from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentSubStatus")


@_attrs_define
class IncidentSubStatus:
    """
    Attributes:
        incident_id (str):
        sub_status_id (str): Note: To change an incident's sub-status, use the PATCH /incidents/:id endpoint and set the
            sub_status_id attribute. This endpoint is for modifying the timestamp of when an incident's sub-status was
            assigned.
        assigned_at (str):
        assigned_by_user_id (Union[None, Unset, int]):
    """

    incident_id: str
    sub_status_id: str
    assigned_at: str
    assigned_by_user_id: None | Unset | int = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_id = self.incident_id

        sub_status_id = self.sub_status_id

        assigned_at = self.assigned_at

        assigned_by_user_id: None | Unset | int
        if isinstance(self.assigned_by_user_id, Unset):
            assigned_by_user_id = UNSET
        else:
            assigned_by_user_id = self.assigned_by_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_id": incident_id,
                "sub_status_id": sub_status_id,
                "assigned_at": assigned_at,
            }
        )
        if assigned_by_user_id is not UNSET:
            field_dict["assigned_by_user_id"] = assigned_by_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        incident_id = d.pop("incident_id")

        sub_status_id = d.pop("sub_status_id")

        assigned_at = d.pop("assigned_at")

        def _parse_assigned_by_user_id(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        assigned_by_user_id = _parse_assigned_by_user_id(d.pop("assigned_by_user_id", UNSET))

        incident_sub_status = cls(
            incident_id=incident_id,
            sub_status_id=sub_status_id,
            assigned_at=assigned_at,
            assigned_by_user_id=assigned_by_user_id,
        )

        incident_sub_status.additional_properties = d
        return incident_sub_status

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
