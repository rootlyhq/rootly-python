from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.new_post_mortem_template_data_attributes_format import (
    NewPostMortemTemplateDataAttributesFormat,
    check_new_post_mortem_template_data_attributes_format,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewPostMortemTemplateDataAttributes")


@_attrs_define
class NewPostMortemTemplateDataAttributes:
    """
    Attributes:
        name (str): The name of the postmortem template
        slug (None | str | Unset): Deprecated. `slug` is derived from `name`; any submitted value is ignored. This
            property will be removed from the request schema in a future version.
        default (bool | None | Unset): Default selected template when editing a postmortem
        content (str | Unset): The postmortem template. Supports TipTap blocks (followup and timeline components),
            Liquid syntax, and HTML. Will be sanitized and applied to both content and content_html fields.
        format_ (NewPostMortemTemplateDataAttributesFormat | Unset): The format of the input Default: 'html'.
    """

    name: str
    slug: None | str | Unset = UNSET
    default: bool | None | Unset = UNSET
    content: str | Unset = UNSET
    format_: NewPostMortemTemplateDataAttributesFormat | Unset = "html"

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        default: bool | None | Unset
        if isinstance(self.default, Unset):
            default = UNSET
        else:
            default = self.default

        content = self.content

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if default is not UNSET:
            field_dict["default"] = default
        if content is not UNSET:
            field_dict["content"] = content
        if format_ is not UNSET:
            field_dict["format"] = format_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_default(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        default = _parse_default(d.pop("default", UNSET))

        content = d.pop("content", UNSET)

        _format_ = d.pop("format", UNSET)
        format_: NewPostMortemTemplateDataAttributesFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = check_new_post_mortem_template_data_attributes_format(_format_)

        new_post_mortem_template_data_attributes = cls(
            name=name,
            slug=slug,
            default=default,
            content=content,
            format_=format_,
        )

        return new_post_mortem_template_data_attributes
