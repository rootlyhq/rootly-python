from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewOnCallPayReportDataAttributes")


@_attrs_define
class NewOnCallPayReportDataAttributes:
    """
    Attributes:
        start_date (datetime.date): The start date for the report period.
        end_date (datetime.date): The end date for the report period.
        schedule_ids (list[str] | Unset): List of schedule UUIDs to scope the report.
    """

    start_date: datetime.date
    end_date: datetime.date
    schedule_ids: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        schedule_ids: list[str] | Unset = UNSET
        if not isinstance(self.schedule_ids, Unset):
            schedule_ids = self.schedule_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "start_date": start_date,
                "end_date": end_date,
            }
        )
        if schedule_ids is not UNSET:
            field_dict["schedule_ids"] = schedule_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_date = isoparse(d.pop("start_date")).date()

        end_date = isoparse(d.pop("end_date")).date()

        schedule_ids = cast(list[str], d.pop("schedule_ids", UNSET))

        new_on_call_pay_report_data_attributes = cls(
            start_date=start_date,
            end_date=end_date,
            schedule_ids=schedule_ids,
        )

        return new_on_call_pay_report_data_attributes
