from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.new_verified_domain_data_type import NewVerifiedDomainDataType, check_new_verified_domain_data_type

if TYPE_CHECKING:
    from ..models.new_verified_domain_data_attributes import NewVerifiedDomainDataAttributes


T = TypeVar("T", bound="NewVerifiedDomainData")


@_attrs_define
class NewVerifiedDomainData:
    """
    Attributes:
        type_ (NewVerifiedDomainDataType):
        attributes (NewVerifiedDomainDataAttributes):
    """

    type_: NewVerifiedDomainDataType
    attributes: NewVerifiedDomainDataAttributes

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
        from ..models.new_verified_domain_data_attributes import NewVerifiedDomainDataAttributes

        d = dict(src_dict)
        type_ = check_new_verified_domain_data_type(d.pop("type"))

        attributes = NewVerifiedDomainDataAttributes.from_dict(d.pop("attributes"))

        new_verified_domain_data = cls(
            type_=type_,
            attributes=attributes,
        )

        return new_verified_domain_data
