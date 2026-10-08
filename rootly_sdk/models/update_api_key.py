from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_api_key_data import UpdateApiKeyData


T = TypeVar("T", bound="UpdateApiKey")


@_attrs_define
class UpdateApiKey:
    """
    Attributes:
        data (UpdateApiKeyData):
    """

    data: UpdateApiKeyData

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
        from ..models.update_api_key_data import UpdateApiKeyData

        d = dict(src_dict)
        data = UpdateApiKeyData.from_dict(d.pop("data"))

        update_api_key = cls(
            data=data,
        )

        return update_api_key
