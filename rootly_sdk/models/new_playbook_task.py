from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_playbook_task_data import NewPlaybookTaskData


T = TypeVar("T", bound="NewPlaybookTask")


@_attrs_define
class NewPlaybookTask:
    """
    Attributes:
        data (NewPlaybookTaskData):
    """

    data: NewPlaybookTaskData

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
        from ..models.new_playbook_task_data import NewPlaybookTaskData

        d = dict(src_dict)
        data = NewPlaybookTaskData.from_dict(d.pop("data"))

        new_playbook_task = cls(
            data=data,
        )

        return new_playbook_task
