from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.update_status_page_data_type import UpdateStatusPageDataType, check_update_status_page_data_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_status_page_data_attributes import UpdateStatusPageDataAttributes


T = TypeVar("T", bound="UpdateStatusPageData")


@_attrs_define
class UpdateStatusPageData:
    """
    Attributes:
        type_ (UpdateStatusPageDataType):
        attributes (UpdateStatusPageDataAttributes):
        id (str | Unset): Accepted for JSON:API client compatibility, but ignored. The resource to update is identified
            by the id in the path.
    """

    type_: UpdateStatusPageDataType
    attributes: UpdateStatusPageDataAttributes
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
        from ..models.update_status_page_data_attributes import UpdateStatusPageDataAttributes

        d = dict(src_dict)
        type_ = check_update_status_page_data_type(d.pop("type"))

        attributes = UpdateStatusPageDataAttributes.from_dict(d.pop("attributes"))

        id = d.pop("id", UNSET)

        update_status_page_data = cls(
            type_=type_,
            attributes=attributes,
            id=id,
        )

        return update_status_page_data
