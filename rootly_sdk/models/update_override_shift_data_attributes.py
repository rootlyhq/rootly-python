from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="UpdateOverrideShiftDataAttributes")


@_attrs_define
class UpdateOverrideShiftDataAttributes:
    """
    Attributes:
        user_id (int): Override shift user
    """

    user_id: int

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("user_id")

        update_override_shift_data_attributes = cls(
            user_id=user_id,
        )

        return update_override_shift_data_attributes
