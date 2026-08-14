from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ScheduleRotationUser")


@_attrs_define
class ScheduleRotationUser:
    """
    Attributes:
        schedule_rotation_id (str):
        user_id (int): Schedule rotation user
        position (int): Position of the user inside rotation
        created_at (str): Date of creation
        updated_at (str): Date of last update
    """

    schedule_rotation_id: str
    user_id: int
    position: int
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_rotation_id = self.schedule_rotation_id

        user_id = self.user_id

        position = self.position

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedule_rotation_id": schedule_rotation_id,
                "user_id": user_id,
                "position": position,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        schedule_rotation_id = d.pop("schedule_rotation_id")

        user_id = d.pop("user_id")

        position = d.pop("position")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        schedule_rotation_user = cls(
            schedule_rotation_id=schedule_rotation_id,
            user_id=user_id,
            position=position,
            created_at=created_at,
            updated_at=updated_at,
        )

        schedule_rotation_user.additional_properties = d
        return schedule_rotation_user

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
