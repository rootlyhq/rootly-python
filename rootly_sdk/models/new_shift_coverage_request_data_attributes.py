from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewShiftCoverageRequestDataAttributes")


@_attrs_define
class NewShiftCoverageRequestDataAttributes:
    """
    Attributes:
        starts_at (datetime.datetime): Start datetime of the time range to request coverage for
        ends_at (datetime.datetime): End datetime of the time range to request coverage for
        user_id (int | Unset): Optional. Restrict coverage to shifts assigned to this user. When omitted, every shift
            overlapping the time range is covered.
        recipient_user_ids (list[int] | Unset): Optional. Notify selected active schedule members for every covered
            shift when targeted-shift-coverage is enabled. Recipients must be eligible for each shift. Omitted, empty, or
            flag-disabled selections broadcast.
    """

    starts_at: datetime.datetime
    ends_at: datetime.datetime
    user_id: int | Unset = UNSET
    recipient_user_ids: list[int] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        starts_at = self.starts_at.isoformat()

        ends_at = self.ends_at.isoformat()

        user_id = self.user_id

        recipient_user_ids: list[int] | Unset = UNSET
        if not isinstance(self.recipient_user_ids, Unset):
            recipient_user_ids = self.recipient_user_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "starts_at": starts_at,
                "ends_at": ends_at,
            }
        )
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if recipient_user_ids is not UNSET:
            field_dict["recipient_user_ids"] = recipient_user_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        starts_at = datetime.datetime.fromisoformat(d.pop("starts_at"))

        ends_at = datetime.datetime.fromisoformat(d.pop("ends_at"))

        user_id = d.pop("user_id", UNSET)

        recipient_user_ids = cast(list[int], d.pop("recipient_user_ids", UNSET))

        new_shift_coverage_request_data_attributes = cls(
            starts_at=starts_at,
            ends_at=ends_at,
            user_id=user_id,
            recipient_user_ids=recipient_user_ids,
        )

        return new_shift_coverage_request_data_attributes
