from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewIncidentActionItemDataAttributesFormFieldSelectionsType0Item")


@_attrs_define
class NewIncidentActionItemDataAttributesFormFieldSelectionsType0Item:
    """
    Attributes:
        form_field_id (str): ID of the custom field
        id (Union[Unset, str]): ID of an existing selection. Required when updating or removing a field's existing
            value.
        value (Union[None, Unset, list[str], str]): Value for text, textarea, rich text, date, datetime, number,
            checkbox, or tag fields
        selected_option_ids (Union[Unset, list[str]]): IDs of the selected custom field options
        selected_user_ids (Union[Unset, list[int]]): IDs of the selected users
        selected_group_ids (Union[Unset, list[str]]): IDs of the selected teams
        selected_service_ids (Union[Unset, list[str]]): IDs of the selected services
        selected_functionality_ids (Union[Unset, list[str]]): IDs of the selected functionalities
        selected_catalog_entity_ids (Union[Unset, list[str]]): IDs of the selected catalog entities
        selected_environment_ids (Union[Unset, list[str]]): IDs of the selected environments
        selected_cause_ids (Union[Unset, list[str]]): IDs of the selected causes
        selected_incident_type_ids (Union[Unset, list[str]]): IDs of the selected incident types
        field_destroy (Union[None, Unset, bool]): Set to true to remove the field's value from the action item
    """

    form_field_id: str
    id: Union[Unset, str] = UNSET
    value: Union[None, Unset, list[str], str] = UNSET
    selected_option_ids: Union[Unset, list[str]] = UNSET
    selected_user_ids: Union[Unset, list[int]] = UNSET
    selected_group_ids: Union[Unset, list[str]] = UNSET
    selected_service_ids: Union[Unset, list[str]] = UNSET
    selected_functionality_ids: Union[Unset, list[str]] = UNSET
    selected_catalog_entity_ids: Union[Unset, list[str]] = UNSET
    selected_environment_ids: Union[Unset, list[str]] = UNSET
    selected_cause_ids: Union[Unset, list[str]] = UNSET
    selected_incident_type_ids: Union[Unset, list[str]] = UNSET
    field_destroy: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        form_field_id = self.form_field_id

        id = self.id

        value: Union[None, Unset, list[str], str]
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, list):
            value = self.value

        else:
            value = self.value

        selected_option_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.selected_option_ids, Unset):
            selected_option_ids = self.selected_option_ids

        selected_user_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.selected_user_ids, Unset):
            selected_user_ids = self.selected_user_ids

        selected_group_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.selected_group_ids, Unset):
            selected_group_ids = self.selected_group_ids

        selected_service_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.selected_service_ids, Unset):
            selected_service_ids = self.selected_service_ids

        selected_functionality_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.selected_functionality_ids, Unset):
            selected_functionality_ids = self.selected_functionality_ids

        selected_catalog_entity_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.selected_catalog_entity_ids, Unset):
            selected_catalog_entity_ids = self.selected_catalog_entity_ids

        selected_environment_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.selected_environment_ids, Unset):
            selected_environment_ids = self.selected_environment_ids

        selected_cause_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.selected_cause_ids, Unset):
            selected_cause_ids = self.selected_cause_ids

        selected_incident_type_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.selected_incident_type_ids, Unset):
            selected_incident_type_ids = self.selected_incident_type_ids

        field_destroy: Union[None, Unset, bool]
        if isinstance(self.field_destroy, Unset):
            field_destroy = UNSET
        else:
            field_destroy = self.field_destroy

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "form_field_id": form_field_id,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if value is not UNSET:
            field_dict["value"] = value
        if selected_option_ids is not UNSET:
            field_dict["selected_option_ids"] = selected_option_ids
        if selected_user_ids is not UNSET:
            field_dict["selected_user_ids"] = selected_user_ids
        if selected_group_ids is not UNSET:
            field_dict["selected_group_ids"] = selected_group_ids
        if selected_service_ids is not UNSET:
            field_dict["selected_service_ids"] = selected_service_ids
        if selected_functionality_ids is not UNSET:
            field_dict["selected_functionality_ids"] = selected_functionality_ids
        if selected_catalog_entity_ids is not UNSET:
            field_dict["selected_catalog_entity_ids"] = selected_catalog_entity_ids
        if selected_environment_ids is not UNSET:
            field_dict["selected_environment_ids"] = selected_environment_ids
        if selected_cause_ids is not UNSET:
            field_dict["selected_cause_ids"] = selected_cause_ids
        if selected_incident_type_ids is not UNSET:
            field_dict["selected_incident_type_ids"] = selected_incident_type_ids
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        form_field_id = d.pop("form_field_id")

        id = d.pop("id", UNSET)

        def _parse_value(data: object) -> Union[None, Unset, list[str], str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_1 = cast(list[str], data)

                return value_type_1
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str], str], data)

        value = _parse_value(d.pop("value", UNSET))

        selected_option_ids = cast(list[str], d.pop("selected_option_ids", UNSET))

        selected_user_ids = cast(list[int], d.pop("selected_user_ids", UNSET))

        selected_group_ids = cast(list[str], d.pop("selected_group_ids", UNSET))

        selected_service_ids = cast(list[str], d.pop("selected_service_ids", UNSET))

        selected_functionality_ids = cast(list[str], d.pop("selected_functionality_ids", UNSET))

        selected_catalog_entity_ids = cast(list[str], d.pop("selected_catalog_entity_ids", UNSET))

        selected_environment_ids = cast(list[str], d.pop("selected_environment_ids", UNSET))

        selected_cause_ids = cast(list[str], d.pop("selected_cause_ids", UNSET))

        selected_incident_type_ids = cast(list[str], d.pop("selected_incident_type_ids", UNSET))

        def _parse_field_destroy(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        field_destroy = _parse_field_destroy(d.pop("_destroy", UNSET))

        new_incident_action_item_data_attributes_form_field_selections_type_0_item = cls(
            form_field_id=form_field_id,
            id=id,
            value=value,
            selected_option_ids=selected_option_ids,
            selected_user_ids=selected_user_ids,
            selected_group_ids=selected_group_ids,
            selected_service_ids=selected_service_ids,
            selected_functionality_ids=selected_functionality_ids,
            selected_catalog_entity_ids=selected_catalog_entity_ids,
            selected_environment_ids=selected_environment_ids,
            selected_cause_ids=selected_cause_ids,
            selected_incident_type_ids=selected_incident_type_ids,
            field_destroy=field_destroy,
        )

        return new_incident_action_item_data_attributes_form_field_selections_type_0_item
