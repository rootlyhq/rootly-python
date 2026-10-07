from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.rotate_api_key_data import RotateApiKeyData


T = TypeVar("T", bound="RotateApiKey")


@_attrs_define
class RotateApiKey:
    """
    Attributes:
        data (RotateApiKeyData):
    """

    data: RotateApiKeyData

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
        from ..models.rotate_api_key_data import RotateApiKeyData

        d = dict(src_dict)
        data = RotateApiKeyData.from_dict(d.pop("data"))

        rotate_api_key = cls(
            data=data,
        )

        return rotate_api_key
