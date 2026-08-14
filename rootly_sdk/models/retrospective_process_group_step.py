from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RetrospectiveProcessGroupStep")


@_attrs_define
class RetrospectiveProcessGroupStep:
    """
    Attributes:
        retrospective_process_group_id (str):
        retrospective_step_id (str):
        position (int):
    """

    retrospective_process_group_id: str
    retrospective_step_id: str
    position: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        retrospective_process_group_id = self.retrospective_process_group_id

        retrospective_step_id = self.retrospective_step_id

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "retrospective_process_group_id": retrospective_process_group_id,
                "retrospective_step_id": retrospective_step_id,
                "position": position,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        retrospective_process_group_id = d.pop("retrospective_process_group_id")

        retrospective_step_id = d.pop("retrospective_step_id")

        position = d.pop("position")

        retrospective_process_group_step = cls(
            retrospective_process_group_id=retrospective_process_group_id,
            retrospective_step_id=retrospective_step_id,
            position=position,
        )

        retrospective_process_group_step.additional_properties = d
        return retrospective_process_group_step

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
