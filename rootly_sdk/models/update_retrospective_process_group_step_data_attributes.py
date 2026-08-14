from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateRetrospectiveProcessGroupStepDataAttributes")


@_attrs_define
class UpdateRetrospectiveProcessGroupStepDataAttributes:
    """
    Attributes:
        position (Union[Unset, int]):
    """

    position: Unset | int = UNSET

    def to_dict(self) -> dict[str, Any]:
        position = self.position

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        position = d.pop("position", UNSET)

        update_retrospective_process_group_step_data_attributes = cls(
            position=position,
        )

        return update_retrospective_process_group_step_data_attributes
