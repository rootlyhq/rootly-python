from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewRetrospectiveProcessGroupDataAttributes")


@_attrs_define
class NewRetrospectiveProcessGroupDataAttributes:
    """
    Attributes:
        sub_status_id (str):
        position (Union[Unset, int]):
    """

    sub_status_id: str
    position: Unset | int = UNSET

    def to_dict(self) -> dict[str, Any]:
        sub_status_id = self.sub_status_id

        position = self.position

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sub_status_id": sub_status_id,
            }
        )
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sub_status_id = d.pop("sub_status_id")

        position = d.pop("position", UNSET)

        new_retrospective_process_group_data_attributes = cls(
            sub_status_id=sub_status_id,
            position=position,
        )

        return new_retrospective_process_group_data_attributes
