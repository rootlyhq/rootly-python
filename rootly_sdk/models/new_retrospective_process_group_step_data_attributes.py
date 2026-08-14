from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewRetrospectiveProcessGroupStepDataAttributes")


@_attrs_define
class NewRetrospectiveProcessGroupStepDataAttributes:
    """
    Attributes:
        retrospective_step_id (str):
        position (Union[Unset, int]):
    """

    retrospective_step_id: str
    position: Unset | int = UNSET

    def to_dict(self) -> dict[str, Any]:
        retrospective_step_id = self.retrospective_step_id

        position = self.position

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "retrospective_step_id": retrospective_step_id,
            }
        )
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        retrospective_step_id = d.pop("retrospective_step_id")

        position = d.pop("position", UNSET)

        new_retrospective_process_group_step_data_attributes = cls(
            retrospective_step_id=retrospective_step_id,
            position=position,
        )

        return new_retrospective_process_group_step_data_attributes
