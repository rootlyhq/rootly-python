from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.new_on_call_shadow_data_type import NewOnCallShadowDataType, check_new_on_call_shadow_data_type

if TYPE_CHECKING:
    from ..models.new_on_call_shadow_data_attributes import NewOnCallShadowDataAttributes


T = TypeVar("T", bound="NewOnCallShadowData")


@_attrs_define
class NewOnCallShadowData:
    """
    Attributes:
        type_ (NewOnCallShadowDataType):
        attributes (NewOnCallShadowDataAttributes):
    """

    type_: NewOnCallShadowDataType
    attributes: NewOnCallShadowDataAttributes

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
        from ..models.new_on_call_shadow_data_attributes import NewOnCallShadowDataAttributes

        d = dict(src_dict)
        type_ = check_new_on_call_shadow_data_type(d.pop("type"))

        attributes = NewOnCallShadowDataAttributes.from_dict(d.pop("attributes"))

        new_on_call_shadow_data = cls(
            type_=type_,
            attributes=attributes,
        )

        return new_on_call_shadow_data
