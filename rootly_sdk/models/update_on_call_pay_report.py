from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_on_call_pay_report_data import UpdateOnCallPayReportData


T = TypeVar("T", bound="UpdateOnCallPayReport")


@_attrs_define
class UpdateOnCallPayReport:
    """
    Attributes:
        data (UpdateOnCallPayReportData):
    """

    data: UpdateOnCallPayReportData

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_on_call_pay_report_data import UpdateOnCallPayReportData

        d = dict(src_dict)
        data = UpdateOnCallPayReportData.from_dict(d.pop("data"))

        update_on_call_pay_report = cls(
            data=data,
        )

        return update_on_call_pay_report
