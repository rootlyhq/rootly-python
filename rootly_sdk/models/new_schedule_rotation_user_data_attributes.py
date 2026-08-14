from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewScheduleRotationUserDataAttributes")


@_attrs_define
class NewScheduleRotationUserDataAttributes:
    """
    Attributes:
        user_id (int): Schedule rotation user
        position (Union[Unset, int]): Position of the user inside rotation
    """

    user_id: int
    position: Unset | int = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        position = self.position

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "user_id": user_id,
            }
        )
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("user_id")

        position = d.pop("position", UNSET)

        new_schedule_rotation_user_data_attributes = cls(
            user_id=user_id,
            position=position,
        )

        return new_schedule_rotation_user_data_attributes
