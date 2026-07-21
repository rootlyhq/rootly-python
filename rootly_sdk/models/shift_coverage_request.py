from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.schedule_response import ScheduleResponse
    from ..models.shift import Shift
    from ..models.user_response import UserResponse


T = TypeVar("T", bound="ShiftCoverageRequest")


@_attrs_define
class ShiftCoverageRequest:
    """
    Attributes:
        schedule_id (str): ID of schedule
        shift_id (str): ID of the shift being covered
        original_shift_user_id (int): ID of the user whose shift is being covered
        created_by_user_id (int): ID of the user who created the coverage request
        starts_at (str): Start datetime of the coverage request
        ends_at (str): End datetime of the coverage request
        created_at (str | Unset): Date of creation
        updated_at (str | Unset): Date of last update
        schedule (ScheduleResponse | Unset):
        shift (Shift | Unset):
        original_shift_user (UserResponse | Unset):
        created_by_user (UserResponse | Unset):
    """

    schedule_id: str
    shift_id: str
    original_shift_user_id: int
    created_by_user_id: int
    starts_at: str
    ends_at: str
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    schedule: ScheduleResponse | Unset = UNSET
    shift: Shift | Unset = UNSET
    original_shift_user: UserResponse | Unset = UNSET
    created_by_user: UserResponse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_response import UserResponse
        from ..models.shift import Shift
        from ..models.schedule_response import ScheduleResponse

        schedule_id = self.schedule_id

        shift_id = self.shift_id

        original_shift_user_id = self.original_shift_user_id

        created_by_user_id = self.created_by_user_id

        starts_at = self.starts_at

        ends_at = self.ends_at

        created_at = self.created_at

        updated_at = self.updated_at

        schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        shift: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shift, Unset):
            shift = self.shift.to_dict()

        original_shift_user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.original_shift_user, Unset):
            original_shift_user = self.original_shift_user.to_dict()

        created_by_user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by_user, Unset):
            created_by_user = self.created_by_user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedule_id": schedule_id,
                "shift_id": shift_id,
                "original_shift_user_id": original_shift_user_id,
                "created_by_user_id": created_by_user_id,
                "starts_at": starts_at,
                "ends_at": ends_at,
            }
        )
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if shift is not UNSET:
            field_dict["shift"] = shift
        if original_shift_user is not UNSET:
            field_dict["original_shift_user"] = original_shift_user
        if created_by_user is not UNSET:
            field_dict["created_by_user"] = created_by_user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schedule_response import ScheduleResponse
        from ..models.shift import Shift
        from ..models.user_response import UserResponse

        d = dict(src_dict)
        schedule_id = d.pop("schedule_id")

        shift_id = d.pop("shift_id")

        original_shift_user_id = d.pop("original_shift_user_id")

        created_by_user_id = d.pop("created_by_user_id")

        starts_at = d.pop("starts_at")

        ends_at = d.pop("ends_at")

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _schedule = d.pop("schedule", UNSET)
        schedule: ScheduleResponse | Unset
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = ScheduleResponse.from_dict(_schedule)

        _shift = d.pop("shift", UNSET)
        shift: Shift | Unset
        if isinstance(_shift, Unset):
            shift = UNSET
        else:
            shift = Shift.from_dict(_shift)

        _original_shift_user = d.pop("original_shift_user", UNSET)
        original_shift_user: UserResponse | Unset
        if isinstance(_original_shift_user, Unset):
            original_shift_user = UNSET
        else:
            original_shift_user = UserResponse.from_dict(_original_shift_user)

        _created_by_user = d.pop("created_by_user", UNSET)
        created_by_user: UserResponse | Unset
        if isinstance(_created_by_user, Unset):
            created_by_user = UNSET
        else:
            created_by_user = UserResponse.from_dict(_created_by_user)

        shift_coverage_request = cls(
            schedule_id=schedule_id,
            shift_id=shift_id,
            original_shift_user_id=original_shift_user_id,
            created_by_user_id=created_by_user_id,
            starts_at=starts_at,
            ends_at=ends_at,
            created_at=created_at,
            updated_at=updated_at,
            schedule=schedule,
            shift=shift,
            original_shift_user=original_shift_user,
            created_by_user=created_by_user,
        )

        shift_coverage_request.additional_properties = d
        return shift_coverage_request

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
