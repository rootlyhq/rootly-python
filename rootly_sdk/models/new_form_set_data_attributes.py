from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewFormSetDataAttributes")


@_attrs_define
class NewFormSetDataAttributes:
    """
    Attributes:
        name (str): The name of the form set
        forms (list[str]): The forms included in the form set. Add custom forms using the custom form's `slug` field. Or
            choose a built-in form: `web_new_incident_form`, `web_update_incident_form`, `web_incident_post_mortem_form`,
            `web_incident_mitigation_form`, `web_incident_resolution_form`, `web_incident_cancellation_form`,
            `web_scheduled_incident_form`, `web_update_scheduled_incident_form`, `slack_new_incident_form`,
            `slack_update_incident_form`, `slack_update_incident_status_form`, `slack_incident_mitigation_form`,
            `slack_incident_resolution_form`, `slack_incident_cancellation_form`, `slack_scheduled_incident_form`,
            `slack_update_scheduled_incident_form`, `google_chat_new_incident_form`, `google_chat_update_incident_form`,
            `microsoft_teams_new_incident_form`
        slug (Union[None, Unset, str]): Deprecated. `slug` is derived from `name`; any submitted value is ignored. This
            property will be removed from the request schema in a future version.
    """

    name: str
    forms: list[str]
    slug: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        forms = self.forms

        slug: None | Unset | str
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "forms": forms,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        forms = cast(list[str], d.pop("forms"))

        def _parse_slug(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        new_form_set_data_attributes = cls(
            name=name,
            forms=forms,
            slug=slug,
        )

        return new_form_set_data_attributes
