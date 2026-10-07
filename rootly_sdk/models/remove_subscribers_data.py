from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.remove_subscribers_data_type import RemoveSubscribersDataType, check_remove_subscribers_data_type

if TYPE_CHECKING:
    from ..models.remove_subscribers_data_attributes import RemoveSubscribersDataAttributes


T = TypeVar("T", bound="RemoveSubscribersData")


@_attrs_define
class RemoveSubscribersData:
    """
    Attributes:
        type_ (RemoveSubscribersDataType):
        attributes (RemoveSubscribersDataAttributes):
    """

    type_: RemoveSubscribersDataType
    attributes: RemoveSubscribersDataAttributes

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
        from ..models.remove_subscribers_data_attributes import RemoveSubscribersDataAttributes

        d = dict(src_dict)
        type_ = check_remove_subscribers_data_type(d.pop("type"))

        attributes = RemoveSubscribersDataAttributes.from_dict(d.pop("attributes"))

        remove_subscribers_data = cls(
            type_=type_,
            attributes=attributes,
        )

        return remove_subscribers_data
