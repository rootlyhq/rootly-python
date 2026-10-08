from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.add_subscribers_data_type import AddSubscribersDataType, check_add_subscribers_data_type

if TYPE_CHECKING:
    from ..models.add_subscribers_data_attributes import AddSubscribersDataAttributes


T = TypeVar("T", bound="AddSubscribersData")


@_attrs_define
class AddSubscribersData:
    """
    Attributes:
        type_ (AddSubscribersDataType):
        attributes (AddSubscribersDataAttributes):
    """

    type_: AddSubscribersDataType
    attributes: AddSubscribersDataAttributes

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_subscribers_data_attributes import AddSubscribersDataAttributes

        d = dict(src_dict)
        type_ = check_add_subscribers_data_type(d.pop("type"))

        attributes = AddSubscribersDataAttributes.from_dict(d.pop("attributes"))

        add_subscribers_data = cls(
            type_=type_,
            attributes=attributes,
        )

        return add_subscribers_data
