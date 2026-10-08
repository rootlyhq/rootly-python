from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateFormSetDataAttributes")


@_attrs_define
class UpdateFormSetDataAttributes:
    """
    Attributes:
        slug (None | str | Unset): Deprecated. `slug` is derived from `name`; any submitted value is ignored. This
            property will be removed from the request schema in a future version.
        name (str | Unset): The name of the form set
        forms (list[str] | Unset): The forms included in the form set. Add custom forms using the custom form's `slug`
            field. Or choose a built-in form: `web_new_incident_form`, `web_update_incident_form`,
            `web_incident_post_mortem_form`, `web_incident_mitigation_form`, `web_incident_resolution_form`,
            `web_incident_cancellation_form`, `web_scheduled_incident_form`, `web_update_scheduled_incident_form`,
            `slack_new_incident_form`, `slack_update_incident_form`, `slack_update_incident_status_form`,
            `slack_incident_mitigation_form`, `slack_incident_resolution_form`, `slack_incident_cancellation_form`,
            `slack_scheduled_incident_form`, `slack_update_scheduled_incident_form`, `google_chat_new_incident_form`,
            `google_chat_update_incident_form`, `microsoft_teams_new_incident_form`
    """

    slug: None | str | Unset = UNSET
    name: str | Unset = UNSET
    forms: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        name = self.name

        forms: list[str] | Unset = UNSET
        if not isinstance(self.forms, Unset):
            forms = self.forms

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
        if forms is not UNSET:
            field_dict["forms"] = forms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        name = d.pop("name", UNSET)

        forms = cast(list[str], d.pop("forms", UNSET))

        update_form_set_data_attributes = cls(
            slug=slug,
            name=name,
            forms=forms,
        )

        return update_form_set_data_attributes
