from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateRetrospectiveProcessGroupDataAttributes")


@_attrs_define
class UpdateRetrospectiveProcessGroupDataAttributes:
    """
    Attributes:
        sub_status_id (Union[Unset, str]):
        position (Union[Unset, int]):
    """

    sub_status_id: Unset | str = UNSET
    position: Unset | int = UNSET

    def to_dict(self) -> dict[str, Any]:
        sub_status_id = self.sub_status_id

        position = self.position

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if sub_status_id is not UNSET:
            field_dict["sub_status_id"] = sub_status_id
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sub_status_id = d.pop("sub_status_id", UNSET)

        position = d.pop("position", UNSET)

        update_retrospective_process_group_data_attributes = cls(
            sub_status_id=sub_status_id,
            position=position,
        )

        return update_retrospective_process_group_data_attributes
