from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_problem_action_item_data import NewProblemActionItemData


T = TypeVar("T", bound="NewProblemActionItem")


@_attrs_define
class NewProblemActionItem:
    """
    Attributes:
        data (NewProblemActionItemData):
    """

    data: NewProblemActionItemData

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
        from ..models.new_problem_action_item_data import NewProblemActionItemData

        d = dict(src_dict)
        data = NewProblemActionItemData.from_dict(d.pop("data"))

        new_problem_action_item = cls(
            data=data,
        )

        return new_problem_action_item
