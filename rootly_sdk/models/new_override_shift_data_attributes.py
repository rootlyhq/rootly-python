import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

T = TypeVar("T", bound="NewOverrideShiftDataAttributes")


@_attrs_define
class NewOverrideShiftDataAttributes:
    """
    Attributes:
        starts_at (datetime.datetime): Start datetime of override shift
        ends_at (datetime.datetime): End datetime of override shift
        user_id (int): Override shift user
    """

    starts_at: datetime.datetime
    ends_at: datetime.datetime
    user_id: int

    def to_dict(self) -> dict[str, Any]:
        starts_at = self.starts_at.isoformat()

        ends_at = self.ends_at.isoformat()

        user_id = self.user_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "starts_at": starts_at,
                "ends_at": ends_at,
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        starts_at = isoparse(d.pop("starts_at"))

        ends_at = isoparse(d.pop("ends_at"))

        user_id = d.pop("user_id")

        new_override_shift_data_attributes = cls(
            starts_at=starts_at,
            ends_at=ends_at,
            user_id=user_id,
        )

        return new_override_shift_data_attributes
