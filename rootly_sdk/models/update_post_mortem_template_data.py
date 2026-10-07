from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.update_post_mortem_template_data_type import (
    UpdatePostMortemTemplateDataType,
    check_update_post_mortem_template_data_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_post_mortem_template_data_attributes import UpdatePostMortemTemplateDataAttributes


T = TypeVar("T", bound="UpdatePostMortemTemplateData")


@_attrs_define
class UpdatePostMortemTemplateData:
    """
    Attributes:
        type_ (UpdatePostMortemTemplateDataType):
        attributes (UpdatePostMortemTemplateDataAttributes):
        id (str | Unset): Accepted for JSON:API client compatibility, but ignored. The resource to update is identified
            by the id in the path.
    """

    type_: UpdatePostMortemTemplateDataType
    attributes: UpdatePostMortemTemplateDataAttributes
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
        from ..models.update_post_mortem_template_data_attributes import UpdatePostMortemTemplateDataAttributes

        d = dict(src_dict)
        type_ = check_update_post_mortem_template_data_type(d.pop("type"))

        attributes = UpdatePostMortemTemplateDataAttributes.from_dict(d.pop("attributes"))

        id = d.pop("id", UNSET)

        update_post_mortem_template_data = cls(
            type_=type_,
            attributes=attributes,
            id=id,
        )

        return update_post_mortem_template_data
