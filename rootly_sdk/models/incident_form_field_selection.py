from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentFormFieldSelection")


@_attrs_define
class IncidentFormFieldSelection:
    """
    Attributes:
        incident_id (str):
        form_field_id (str): The custom field for this selection
        value (Union[None, Unset, str]): The selected value for text kind custom fields
        selected_catalog_entity_ids (Union[Unset, list[str]]):
        selected_group_ids (Union[Unset, list[str]]):
        selected_option_ids (Union[Unset, list[str]]):
        selected_service_ids (Union[Unset, list[str]]):
        selected_functionality_ids (Union[Unset, list[str]]):
        selected_user_ids (Union[Unset, list[int]]):
        selected_environment_ids (Union[Unset, list[str]]):
        selected_cause_ids (Union[Unset, list[str]]):
        selected_incident_type_ids (Union[Unset, list[str]]):
    """

    incident_id: str
    form_field_id: str
    value: Union[None, Unset, str] = UNSET
    selected_catalog_entity_ids: Union[Unset, list[str]] = UNSET
    selected_group_ids: Union[Unset, list[str]] = UNSET
    selected_option_ids: Union[Unset, list[str]] = UNSET
    selected_service_ids: Union[Unset, list[str]] = UNSET
    selected_functionality_ids: Union[Unset, list[str]] = UNSET
    selected_user_ids: Union[Unset, list[int]] = UNSET
    selected_environment_ids: Union[Unset, list[str]] = UNSET
    selected_cause_ids: Union[Unset, list[str]] = UNSET
    selected_incident_type_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_id = self.incident_id

        form_field_id = self.form_field_id

        value: Union[None, Unset, str]
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        selected_catalog_entity_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.selected_catalog_entity_ids, Unset):
            selected_catalog_entity_ids = self.selected_catalog_entity_ids

        selected_group_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.selected_group_ids, Unset):
            selected_group_ids = self.selected_group_ids

        selected_option_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.selected_option_ids, Unset):
            selected_option_ids = self.selected_option_ids

        selected_service_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.selected_service_ids, Unset):
            selected_service_ids = self.selected_service_ids

        selected_functionality_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.selected_functionality_ids, Unset):
            selected_functionality_ids = self.selected_functionality_ids

        selected_user_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.selected_user_ids, Unset):
            selected_user_ids = self.selected_user_ids

        selected_environment_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.selected_environment_ids, Unset):
            selected_environment_ids = self.selected_environment_ids

        selected_cause_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.selected_cause_ids, Unset):
            selected_cause_ids = self.selected_cause_ids

        selected_incident_type_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.selected_incident_type_ids, Unset):
            selected_incident_type_ids = self.selected_incident_type_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        def _parse_value(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

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

        incident_form_field_selection = cls(
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

        incident_form_field_selection.additional_properties = d
        return incident_form_field_selection

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
