from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_retrospective_configuration_data import UpdateRetrospectiveConfigurationData


T = TypeVar("T", bound="UpdateRetrospectiveConfiguration")


@_attrs_define
class UpdateRetrospectiveConfiguration:
    """
    Attributes:
        data (UpdateRetrospectiveConfigurationData):
    """

    data: UpdateRetrospectiveConfigurationData

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
        from ..models.update_retrospective_configuration_data import UpdateRetrospectiveConfigurationData

        d = dict(src_dict)
        data = UpdateRetrospectiveConfigurationData.from_dict(d.pop("data"))

        update_retrospective_configuration = cls(
            data=data,
        )

        return update_retrospective_configuration
