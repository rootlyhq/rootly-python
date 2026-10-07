from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_alerts_source_data import NewAlertsSourceData


T = TypeVar("T", bound="NewAlertsSource")


@_attrs_define
class NewAlertsSource:
    """
    Attributes:
        data (NewAlertsSourceData):
    """

    data: NewAlertsSourceData

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
        from ..models.new_alerts_source_data import NewAlertsSourceData

        d = dict(src_dict)
        data = NewAlertsSourceData.from_dict(d.pop("data"))

        new_alerts_source = cls(
            data=data,
        )

        return new_alerts_source
