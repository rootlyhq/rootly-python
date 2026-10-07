from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_retrospective_step_data import NewRetrospectiveStepData


T = TypeVar("T", bound="NewRetrospectiveStep")


@_attrs_define
class NewRetrospectiveStep:
    """
    Attributes:
        data (NewRetrospectiveStepData):
    """

    data: NewRetrospectiveStepData

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
        from ..models.new_retrospective_step_data import NewRetrospectiveStepData

        d = dict(src_dict)
        data = NewRetrospectiveStepData.from_dict(d.pop("data"))

        new_retrospective_step = cls(
            data=data,
        )

        return new_retrospective_step
