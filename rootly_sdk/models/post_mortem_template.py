from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_mortem_template_format import PostMortemTemplateFormat, check_post_mortem_template_format
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_mortem_template_content_json_type_0 import PostMortemTemplateContentJsonType0


T = TypeVar("T", bound="PostMortemTemplate")


@_attrs_define
class PostMortemTemplate:
    """
    Attributes:
        name (str): The name of the postmortem template
        created_at (str): Date of creation
        updated_at (str): Date of last update
        slug (Union[Unset, str]): The slugified name of the postmortem template
        default (Union[None, Unset, bool]): Default selected template when editing a postmortem
        content (Union[Unset, str]): The postmortem template. Liquid syntax and markdown are supported
        content_html (Union[None, Unset, str]): The postmortem template in HTML format with TipTap blocks support.
            Supports followup and timeline components. Liquid syntax is supported.
        content_json (Union['PostMortemTemplateContentJsonType0', None, Unset]): The postmortem template in TipTap JSON
            format
        format_ (Union[Unset, PostMortemTemplateFormat]): The format of the input
    """

    name: str
    created_at: str
    updated_at: str
    slug: Unset | str = UNSET
    default: None | Unset | bool = UNSET
    content: Unset | str = UNSET
    content_html: None | Unset | str = UNSET
    content_json: Union["PostMortemTemplateContentJsonType0", None, Unset] = UNSET
    format_: Unset | PostMortemTemplateFormat = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.post_mortem_template_content_json_type_0 import PostMortemTemplateContentJsonType0

        name = self.name

        created_at = self.created_at

        updated_at = self.updated_at

        slug = self.slug

        default: None | Unset | bool
        if isinstance(self.default, Unset):
            default = UNSET
        else:
            default = self.default

        content = self.content

        content_html: None | Unset | str
        if isinstance(self.content_html, Unset):
            content_html = UNSET
        else:
            content_html = self.content_html

        content_json: None | Unset | dict[str, Any]
        if isinstance(self.content_json, Unset):
            content_json = UNSET
        elif isinstance(self.content_json, PostMortemTemplateContentJsonType0):
            content_json = self.content_json.to_dict()
        else:
            content_json = self.content_json

        format_: Unset | str = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if default is not UNSET:
            field_dict["default"] = default
        if content is not UNSET:
            field_dict["content"] = content
        if content_html is not UNSET:
            field_dict["content_html"] = content_html
        if content_json is not UNSET:
            field_dict["content_json"] = content_json
        if format_ is not UNSET:
            field_dict["format"] = format_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_mortem_template_content_json_type_0 import PostMortemTemplateContentJsonType0

        d = dict(src_dict)
        name = d.pop("name")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        slug = d.pop("slug", UNSET)

        def _parse_default(data: object) -> None | Unset | bool:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | bool, data)

        default = _parse_default(d.pop("default", UNSET))

        content = d.pop("content", UNSET)

        def _parse_content_html(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        content_html = _parse_content_html(d.pop("content_html", UNSET))

        def _parse_content_json(data: object) -> Union["PostMortemTemplateContentJsonType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_json_type_0 = PostMortemTemplateContentJsonType0.from_dict(data)

                return content_json_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PostMortemTemplateContentJsonType0", None, Unset], data)

        content_json = _parse_content_json(d.pop("content_json", UNSET))

        _format_ = d.pop("format", UNSET)
        format_: Unset | PostMortemTemplateFormat
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = check_post_mortem_template_format(_format_)

        post_mortem_template = cls(
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            slug=slug,
            default=default,
            content=content,
            content_html=content_html,
            content_json=content_json,
            format_=format_,
        )

        post_mortem_template.additional_properties = d
        return post_mortem_template

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
