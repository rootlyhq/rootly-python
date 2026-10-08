from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.new_cause_data_type import NewCauseDataType, check_new_cause_data_type

if TYPE_CHECKING:
    from ..models.new_cause_data_attributes import NewCauseDataAttributes


T = TypeVar("T", bound="NewCauseData")


@_attrs_define
class NewCauseData:
    """
    Attributes:
        type_ (NewCauseDataType):
        attributes (NewCauseDataAttributes):
    """

    type_: NewCauseDataType
    attributes: NewCauseDataAttributes

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
        from ..models.new_cause_data_attributes import NewCauseDataAttributes

        d = dict(src_dict)
        type_ = check_new_cause_data_type(d.pop("type"))

        attributes = NewCauseDataAttributes.from_dict(d.pop("attributes"))

        new_cause_data = cls(
            type_=type_,
            attributes=attributes,
        )

        return new_cause_data
