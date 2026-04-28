from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewIncidentFormFieldSelectionDataAttributes")


@_attrs_define
class NewIncidentFormFieldSelectionDataAttributes:
    """
    Attributes:
        incident_id (str):
        form_field_id (str): The custom field for this selection
        value (None | str | Unset): The selected value for text kind custom fields
        selected_catalog_entity_ids (list[str] | Unset):
        selected_group_ids (list[str] | Unset):
        selected_option_ids (list[str] | Unset):
        selected_service_ids (list[str] | Unset):
        selected_functionality_ids (list[str] | Unset):
        selected_user_ids (list[int] | Unset):
        selected_environment_ids (list[str] | Unset):
        selected_cause_ids (list[str] | Unset):
        selected_incident_type_ids (list[str] | Unset):
    """

    incident_id: str
    form_field_id: str
    value: None | str | Unset = UNSET
    selected_catalog_entity_ids: list[str] | Unset = UNSET
    selected_group_ids: list[str] | Unset = UNSET
    selected_option_ids: list[str] | Unset = UNSET
    selected_service_ids: list[str] | Unset = UNSET
    selected_functionality_ids: list[str] | Unset = UNSET
    selected_user_ids: list[int] | Unset = UNSET
    selected_environment_ids: list[str] | Unset = UNSET
    selected_cause_ids: list[str] | Unset = UNSET
    selected_incident_type_ids: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        incident_id = self.incident_id

        form_field_id = self.form_field_id

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        selected_catalog_entity_ids: list[str] | Unset = UNSET
        if not isinstance(self.selected_catalog_entity_ids, Unset):
            selected_catalog_entity_ids = self.selected_catalog_entity_ids

        selected_group_ids: list[str] | Unset = UNSET
        if not isinstance(self.selected_group_ids, Unset):
            selected_group_ids = self.selected_group_ids

        selected_option_ids: list[str] | Unset = UNSET
        if not isinstance(self.selected_option_ids, Unset):
            selected_option_ids = self.selected_option_ids

        selected_service_ids: list[str] | Unset = UNSET
        if not isinstance(self.selected_service_ids, Unset):
            selected_service_ids = self.selected_service_ids

        selected_functionality_ids: list[str] | Unset = UNSET
        if not isinstance(self.selected_functionality_ids, Unset):
            selected_functionality_ids = self.selected_functionality_ids

        selected_user_ids: list[int] | Unset = UNSET
        if not isinstance(self.selected_user_ids, Unset):
            selected_user_ids = self.selected_user_ids

        selected_environment_ids: list[str] | Unset = UNSET
        if not isinstance(self.selected_environment_ids, Unset):
            selected_environment_ids = self.selected_environment_ids

        selected_cause_ids: list[str] | Unset = UNSET
        if not isinstance(self.selected_cause_ids, Unset):
            selected_cause_ids = self.selected_cause_ids

        selected_incident_type_ids: list[str] | Unset = UNSET
        if not isinstance(self.selected_incident_type_ids, Unset):
            selected_incident_type_ids = self.selected_incident_type_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "incident_id": incident_id,
                "form_field_id": form_field_id,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if selected_catalog_entity_ids is not UNSET:
            field_dict["selected_catalog_entity_ids"] = selected_catalog_entity_ids
        if selected_group_ids is not UNSET:
            field_dict["selected_group_ids"] = selected_group_ids
        if selected_option_ids is not UNSET:
            field_dict["selected_option_ids"] = selected_option_ids
        if selected_service_ids is not UNSET:
            field_dict["selected_service_ids"] = selected_service_ids
        if selected_functionality_ids is not UNSET:
            field_dict["selected_functionality_ids"] = selected_functionality_ids
        if selected_user_ids is not UNSET:
            field_dict["selected_user_ids"] = selected_user_ids
        if selected_environment_ids is not UNSET:
            field_dict["selected_environment_ids"] = selected_environment_ids
        if selected_cause_ids is not UNSET:
            field_dict["selected_cause_ids"] = selected_cause_ids
        if selected_incident_type_ids is not UNSET:
            field_dict["selected_incident_type_ids"] = selected_incident_type_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        incident_id = d.pop("incident_id")

        form_field_id = d.pop("form_field_id")

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        selected_catalog_entity_ids = cast(list[str], d.pop("selected_catalog_entity_ids", UNSET))

        selected_group_ids = cast(list[str], d.pop("selected_group_ids", UNSET))

        selected_option_ids = cast(list[str], d.pop("selected_option_ids", UNSET))

        selected_service_ids = cast(list[str], d.pop("selected_service_ids", UNSET))

        selected_functionality_ids = cast(list[str], d.pop("selected_functionality_ids", UNSET))

        selected_user_ids = cast(list[int], d.pop("selected_user_ids", UNSET))

        selected_environment_ids = cast(list[str], d.pop("selected_environment_ids", UNSET))

        selected_cause_ids = cast(list[str], d.pop("selected_cause_ids", UNSET))

        selected_incident_type_ids = cast(list[str], d.pop("selected_incident_type_ids", UNSET))

        new_incident_form_field_selection_data_attributes = cls(
            incident_id=incident_id,
            form_field_id=form_field_id,
            value=value,
            selected_catalog_entity_ids=selected_catalog_entity_ids,
            selected_group_ids=selected_group_ids,
            selected_option_ids=selected_option_ids,
            selected_service_ids=selected_service_ids,
            selected_functionality_ids=selected_functionality_ids,
            selected_user_ids=selected_user_ids,
            selected_environment_ids=selected_environment_ids,
            selected_cause_ids=selected_cause_ids,
            selected_incident_type_ids=selected_incident_type_ids,
        )

        return new_incident_form_field_selection_data_attributes
