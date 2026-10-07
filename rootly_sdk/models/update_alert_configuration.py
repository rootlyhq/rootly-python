from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_alert_configuration_data import UpdateAlertConfigurationData


T = TypeVar("T", bound="UpdateAlertConfiguration")


@_attrs_define
class UpdateAlertConfiguration:
    """
    Attributes:
        data (UpdateAlertConfigurationData):
    """

    data: UpdateAlertConfigurationData

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
        from ..models.update_alert_configuration_data import UpdateAlertConfigurationData

        d = dict(src_dict)
        data = UpdateAlertConfigurationData.from_dict(d.pop("data"))

        update_alert_configuration = cls(
            data=data,
        )

        return update_alert_configuration
