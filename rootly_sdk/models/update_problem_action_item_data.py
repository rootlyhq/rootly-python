from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.update_problem_action_item_data_type import (
    UpdateProblemActionItemDataType,
    check_update_problem_action_item_data_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_problem_action_item_data_attributes import UpdateProblemActionItemDataAttributes


T = TypeVar("T", bound="UpdateProblemActionItemData")


@_attrs_define
class UpdateProblemActionItemData:
    """
    Attributes:
        type_ (UpdateProblemActionItemDataType):
        attributes (UpdateProblemActionItemDataAttributes):
        id (str | Unset): Accepted for JSON:API client compatibility, but ignored. The resource to update is identified
            by the id in the path.
    """

    type_: UpdateProblemActionItemDataType
    attributes: UpdateProblemActionItemDataAttributes
    id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        attributes = self.attributes.to_dict()

        id = self.id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "attributes": attributes,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_problem_action_item_data_attributes import UpdateProblemActionItemDataAttributes

        d = dict(src_dict)
        type_ = check_update_problem_action_item_data_type(d.pop("type"))

        attributes = UpdateProblemActionItemDataAttributes.from_dict(d.pop("attributes"))

        id = d.pop("id", UNSET)

        update_problem_action_item_data = cls(
            type_=type_,
            attributes=attributes,
            id=id,
        )

        return update_problem_action_item_data
