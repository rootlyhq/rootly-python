from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.new_environment_data_type import NewEnvironmentDataType, check_new_environment_data_type

if TYPE_CHECKING:
    from ..models.new_environment_data_attributes import NewEnvironmentDataAttributes


T = TypeVar("T", bound="NewEnvironmentData")


@_attrs_define
class NewEnvironmentData:
    """
    Attributes:
        type_ (NewEnvironmentDataType):
        attributes (NewEnvironmentDataAttributes):
    """

    type_: NewEnvironmentDataType
    attributes: NewEnvironmentDataAttributes

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
        from ..models.new_environment_data_attributes import NewEnvironmentDataAttributes

        d = dict(src_dict)
        type_ = check_new_environment_data_type(d.pop("type"))

        attributes = NewEnvironmentDataAttributes.from_dict(d.pop("attributes"))

        new_environment_data = cls(
            type_=type_,
            attributes=attributes,
        )

        return new_environment_data
