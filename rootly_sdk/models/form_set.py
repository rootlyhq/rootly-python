from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FormSet")


@_attrs_define
class FormSet:
    """
    Attributes:
        name (str): The name of the form set
        is_default (bool): Whether the form set is default
        forms (list[str]): The forms included in the form set. Add custom forms using the custom form's `slug` field. Or
            choose a built-in form: `web_new_incident_form`, `web_update_incident_form`, `web_incident_post_mortem_form`,
            `web_incident_mitigation_form`, `web_incident_resolution_form`, `web_incident_cancellation_form`,
            `web_scheduled_incident_form`, `web_update_scheduled_incident_form`, `slack_new_incident_form`,
            `slack_update_incident_form`, `slack_update_incident_status_form`, `slack_incident_mitigation_form`,
            `slack_incident_resolution_form`, `slack_incident_cancellation_form`, `slack_scheduled_incident_form`,
            `slack_update_scheduled_incident_form`
        created_at (str): Date of creation
        updated_at (str): Date of last update
        slug (Union[Unset, str]): The slug of the form set
    """

    name: str
    is_default: bool
    forms: list[str]
    created_at: str
    updated_at: str
    slug: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        is_default = self.is_default

        forms = self.forms

        created_at = self.created_at

        updated_at = self.updated_at

        slug = self.slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "is_default": is_default,
                "forms": forms,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        is_default = d.pop("is_default")

        forms = cast(list[str], d.pop("forms"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        slug = d.pop("slug", UNSET)

        form_set = cls(
            name=name,
            is_default=is_default,
            forms=forms,
            created_at=created_at,
            updated_at=updated_at,
            slug=slug,
        )

        form_set.additional_properties = d
        return form_set

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
