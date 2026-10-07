from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.link_incidents_data_type import LinkIncidentsDataType, check_link_incidents_data_type

if TYPE_CHECKING:
    from ..models.link_incidents_data_attributes import LinkIncidentsDataAttributes


T = TypeVar("T", bound="LinkIncidentsData")


@_attrs_define
class LinkIncidentsData:
    """
    Attributes:
        type_ (LinkIncidentsDataType):
        attributes (LinkIncidentsDataAttributes):
    """

    type_: LinkIncidentsDataType
    attributes: LinkIncidentsDataAttributes

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
        from ..models.link_incidents_data_attributes import LinkIncidentsDataAttributes

        d = dict(src_dict)
        type_ = check_link_incidents_data_type(d.pop("type"))

        attributes = LinkIncidentsDataAttributes.from_dict(d.pop("attributes"))

        link_incidents_data = cls(
            type_=type_,
            attributes=attributes,
        )

        return link_incidents_data
