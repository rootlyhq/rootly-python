from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.on_call_pay_report_pay_type import OnCallPayReportPayType, check_on_call_pay_report_pay_type
from ..models.on_call_pay_report_status import OnCallPayReportStatus, check_on_call_pay_report_status
from ..types import UNSET, Unset

T = TypeVar("T", bound="OnCallPayReport")


@_attrs_define
class OnCallPayReport:
    """
    Attributes:
        status (OnCallPayReportStatus): The current status of the report.
        start_date (datetime.date): The start date of the report period.
        end_date (datetime.date): The end date of the report period.
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        total_duration (int | Unset): Total on-call duration in seconds.
        users_count (int | Unset): Number of users included in the report.
        currency (str | Unset): The currency code for monetary values.
        pay_type (OnCallPayReportPayType | Unset): The pay calculation type.
        hourly_rate_cents (int | Unset): Hourly pay rate in cents.
        daily_rate_cents (int | Unset): Daily pay rate in cents.
        total_pay_cents (int | Unset): Total pay amount in cents.
        include_shadow (bool | Unset): Whether shadow shifts are included.
        show_individual_shift_data (bool | Unset): Whether individual shift data is shown.
        has_single_rate (bool | Unset): Whether a single rate is applied to all users.
        enabled_granular_time_breakdown (bool | Unset): Whether granular time breakdown is enabled.
        last_generated_at (datetime.datetime | None | Unset): When the report was last generated.
    """

    status: OnCallPayReportStatus
    start_date: datetime.date
    end_date: datetime.date
    created_at: datetime.datetime
    updated_at: datetime.datetime
    total_duration: int | Unset = UNSET
    users_count: int | Unset = UNSET
    currency: str | Unset = UNSET
    pay_type: OnCallPayReportPayType | Unset = UNSET
    hourly_rate_cents: int | Unset = UNSET
    daily_rate_cents: int | Unset = UNSET
    total_pay_cents: int | Unset = UNSET
    include_shadow: bool | Unset = UNSET
    show_individual_shift_data: bool | Unset = UNSET
    has_single_rate: bool | Unset = UNSET
    enabled_granular_time_breakdown: bool | Unset = UNSET
    last_generated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str = self.status

        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        total_duration = self.total_duration

        users_count = self.users_count

        currency = self.currency

        pay_type: str | Unset = UNSET
        if not isinstance(self.pay_type, Unset):
            pay_type = self.pay_type

        hourly_rate_cents = self.hourly_rate_cents

        daily_rate_cents = self.daily_rate_cents

        total_pay_cents = self.total_pay_cents

        include_shadow = self.include_shadow

        show_individual_shift_data = self.show_individual_shift_data

        has_single_rate = self.has_single_rate

        enabled_granular_time_breakdown = self.enabled_granular_time_breakdown

        last_generated_at: None | str | Unset
        if isinstance(self.last_generated_at, Unset):
            last_generated_at = UNSET
        elif isinstance(self.last_generated_at, datetime.datetime):
            last_generated_at = self.last_generated_at.isoformat()
        else:
            last_generated_at = self.last_generated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "start_date": start_date,
                "end_date": end_date,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if total_duration is not UNSET:
            field_dict["total_duration"] = total_duration
        if users_count is not UNSET:
            field_dict["users_count"] = users_count
        if currency is not UNSET:
            field_dict["currency"] = currency
        if pay_type is not UNSET:
            field_dict["pay_type"] = pay_type
        if hourly_rate_cents is not UNSET:
            field_dict["hourly_rate_cents"] = hourly_rate_cents
        if daily_rate_cents is not UNSET:
            field_dict["daily_rate_cents"] = daily_rate_cents
        if total_pay_cents is not UNSET:
            field_dict["total_pay_cents"] = total_pay_cents
        if include_shadow is not UNSET:
            field_dict["include_shadow"] = include_shadow
        if show_individual_shift_data is not UNSET:
            field_dict["show_individual_shift_data"] = show_individual_shift_data
        if has_single_rate is not UNSET:
            field_dict["has_single_rate"] = has_single_rate
        if enabled_granular_time_breakdown is not UNSET:
            field_dict["enabled_granular_time_breakdown"] = enabled_granular_time_breakdown
        if last_generated_at is not UNSET:
            field_dict["last_generated_at"] = last_generated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = check_on_call_pay_report_status(d.pop("status"))

        start_date = isoparse(d.pop("start_date")).date()

        end_date = isoparse(d.pop("end_date")).date()

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        total_duration = d.pop("total_duration", UNSET)

        users_count = d.pop("users_count", UNSET)

        currency = d.pop("currency", UNSET)

        _pay_type = d.pop("pay_type", UNSET)
        pay_type: OnCallPayReportPayType | Unset
        if isinstance(_pay_type, Unset):
            pay_type = UNSET
        else:
            pay_type = check_on_call_pay_report_pay_type(_pay_type)

        hourly_rate_cents = d.pop("hourly_rate_cents", UNSET)

        daily_rate_cents = d.pop("daily_rate_cents", UNSET)

        total_pay_cents = d.pop("total_pay_cents", UNSET)

        include_shadow = d.pop("include_shadow", UNSET)

        show_individual_shift_data = d.pop("show_individual_shift_data", UNSET)

        has_single_rate = d.pop("has_single_rate", UNSET)

        enabled_granular_time_breakdown = d.pop("enabled_granular_time_breakdown", UNSET)

        def _parse_last_generated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_generated_at_type_0 = isoparse(data)

                return last_generated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_generated_at = _parse_last_generated_at(d.pop("last_generated_at", UNSET))

        on_call_pay_report = cls(
            status=status,
            start_date=start_date,
            end_date=end_date,
            created_at=created_at,
            updated_at=updated_at,
            total_duration=total_duration,
            users_count=users_count,
            currency=currency,
            pay_type=pay_type,
            hourly_rate_cents=hourly_rate_cents,
            daily_rate_cents=daily_rate_cents,
            total_pay_cents=total_pay_cents,
            include_shadow=include_shadow,
            show_individual_shift_data=show_individual_shift_data,
            has_single_rate=has_single_rate,
            enabled_granular_time_breakdown=enabled_granular_time_breakdown,
            last_generated_at=last_generated_at,
        )

        on_call_pay_report.additional_properties = d
        return on_call_pay_report

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
