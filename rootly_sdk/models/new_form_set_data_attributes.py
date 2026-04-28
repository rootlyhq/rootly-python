from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

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
            `slack_update_scheduled_incident_form`
    """

    name: str
    forms: list[str]

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        forms = self.forms

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "forms": forms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        forms = cast(list[str], d.pop("forms"))

        new_form_set_data_attributes = cls(
            name=name,
            forms=forms,
        )

        return new_form_set_data_attributes
