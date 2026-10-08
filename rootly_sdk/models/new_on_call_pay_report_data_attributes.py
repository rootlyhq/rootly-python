from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewOnCallPayReportDataAttributes")


@_attrs_define
class NewOnCallPayReportDataAttributes:
    """
    Attributes:
        start_date (datetime.date): The start date for the report period.
        end_date (datetime.date): The end date for the report period.
        schedule_ids (list[str] | Unset): List of schedule UUIDs to scope the report.
        time_zone (str | Unset): IANA timezone used to compute day and weekend boundaries. Defaults to the team's
            timezone.
        use_responders_time_zone (bool | Unset): When true, day and weekend boundaries are computed in each responder's
            personal timezone instead of the report-wide timezone.
    """

    start_date: datetime.date
    end_date: datetime.date
    schedule_ids: list[str] | Unset = UNSET
    time_zone: str | Unset = UNSET
    use_responders_time_zone: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        schedule_ids: list[str] | Unset = UNSET
        if not isinstance(self.schedule_ids, Unset):
            schedule_ids = self.schedule_ids

        time_zone = self.time_zone

        use_responders_time_zone = self.use_responders_time_zone

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "start_date": start_date,
                "end_date": end_date,
            }
        )
        if schedule_ids is not UNSET:
            field_dict["schedule_ids"] = schedule_ids
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone
        if use_responders_time_zone is not UNSET:
            field_dict["use_responders_time_zone"] = use_responders_time_zone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_date = datetime.date.fromisoformat(d.pop("start_date"))

        end_date = datetime.date.fromisoformat(d.pop("end_date"))

        schedule_ids = cast(list[str], d.pop("schedule_ids", UNSET))

        time_zone = d.pop("time_zone", UNSET)

        use_responders_time_zone = d.pop("use_responders_time_zone", UNSET)

        new_on_call_pay_report_data_attributes = cls(
            start_date=start_date,
            end_date=end_date,
            schedule_ids=schedule_ids,
            time_zone=time_zone,
            use_responders_time_zone=use_responders_time_zone,
        )

        return new_on_call_pay_report_data_attributes
