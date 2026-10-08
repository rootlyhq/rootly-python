from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_problem_action_item_data import UpdateProblemActionItemData


T = TypeVar("T", bound="UpdateProblemActionItem")


@_attrs_define
class UpdateProblemActionItem:
    """
    Attributes:
        data (UpdateProblemActionItemData):
    """

    data: UpdateProblemActionItemData

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
        from ..models.update_problem_action_item_data import UpdateProblemActionItemData

        d = dict(src_dict)
        data = UpdateProblemActionItemData.from_dict(d.pop("data"))

        update_problem_action_item = cls(
            data=data,
        )

        return update_problem_action_item
