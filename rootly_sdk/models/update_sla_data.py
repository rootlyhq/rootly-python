from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_sla_data_type import UpdateSlaDataType, check_update_sla_data_type

if TYPE_CHECKING:
    from ..models.update_sla_data_attributes import UpdateSlaDataAttributes


T = TypeVar("T", bound="UpdateSlaData")


@_attrs_define
class UpdateSlaData:
    """
    Attributes:
        type_ (UpdateSlaDataType):
        attributes (UpdateSlaDataAttributes):
    """

    type_: UpdateSlaDataType
    attributes: UpdateSlaDataAttributes
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_sla_data_attributes import UpdateSlaDataAttributes

        d = dict(src_dict)
        type_ = check_update_sla_data_type(d.pop("type"))

        attributes = UpdateSlaDataAttributes.from_dict(d.pop("attributes"))

        update_sla_data = cls(
            type_=type_,
            attributes=attributes,
        )

        update_sla_data.additional_properties = d
        return update_sla_data

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
