from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_alerts_source_data import UpdateAlertsSourceData


T = TypeVar("T", bound="UpdateAlertsSource")


@_attrs_define
class UpdateAlertsSource:
    """
    Attributes:
        data (UpdateAlertsSourceData):
    """

    data: UpdateAlertsSourceData

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
        from ..models.update_alerts_source_data import UpdateAlertsSourceData

        d = dict(src_dict)
        data = UpdateAlertsSourceData.from_dict(d.pop("data"))

        update_alerts_source = cls(
            data=data,
        )

        return update_alerts_source
