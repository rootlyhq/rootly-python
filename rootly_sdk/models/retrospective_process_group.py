from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RetrospectiveProcessGroup")


@_attrs_define
class RetrospectiveProcessGroup:
    """
    Attributes:
        retrospective_process_id (str):
        sub_status_id (str):
        position (int):
    """

    retrospective_process_id: str
    sub_status_id: str
    position: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        retrospective_process_id = self.retrospective_process_id

        sub_status_id = self.sub_status_id

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "retrospective_process_id": retrospective_process_id,
                "sub_status_id": sub_status_id,
                "position": position,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        retrospective_process_id = d.pop("retrospective_process_id")

        sub_status_id = d.pop("sub_status_id")

        position = d.pop("position")

        retrospective_process_group = cls(
            retrospective_process_id=retrospective_process_id,
            sub_status_id=sub_status_id,
            position=position,
        )

        retrospective_process_group.additional_properties = d
        return retrospective_process_group

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
