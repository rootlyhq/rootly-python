from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_schedule_rotation_user_data import NewScheduleRotationUserData


T = TypeVar("T", bound="NewScheduleRotationUser")


@_attrs_define
class NewScheduleRotationUser:
    """
    Attributes:
        data (NewScheduleRotationUserData | Unset):
    """

    data: NewScheduleRotationUserData | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_schedule_rotation_user_data import NewScheduleRotationUserData

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: NewScheduleRotationUserData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = NewScheduleRotationUserData.from_dict(_data)

        new_schedule_rotation_user = cls(
            data=data,
        )

        return new_schedule_rotation_user
