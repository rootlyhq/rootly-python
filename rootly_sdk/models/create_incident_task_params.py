from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_incident_task_params_task_type import (
    CreateIncidentTaskParamsTaskType,
    check_create_incident_task_params_task_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateIncidentTaskParams")


@_attrs_define
class CreateIncidentTaskParams:
    """
    Attributes:
        title (str): The incident title
        task_type (Union[Unset, CreateIncidentTaskParamsTaskType]):
        summary (Union[Unset, str]): The incident summary
        severity_id (Union[Unset, str]):
        incident_type_ids (Union[Unset, list[str]]):
        service_ids (Union[Unset, list[str]]): Array of service UUIDs
        functionality_ids (Union[Unset, list[str]]): Array of functionality UUIDs
        environment_ids (Union[Unset, list[str]]):
        group_ids (Union[Unset, list[str]]): Array of group/team UUIDs
        private (Union[Unset, bool]):
        custom_fields_mapping (Union[None, Unset, str]): Custom field mappings. Can contain liquid markup and need to be
            valid JSON. Use 'services', 'functionalities', or 'groups' keys with arrays of names/slugs for name/slug lookup
    """

    title: str
    task_type: Union[Unset, CreateIncidentTaskParamsTaskType] = UNSET
    summary: Union[Unset, str] = UNSET
    severity_id: Union[Unset, str] = UNSET
    incident_type_ids: Union[Unset, list[str]] = UNSET
    service_ids: Union[Unset, list[str]] = UNSET
    functionality_ids: Union[Unset, list[str]] = UNSET
    environment_ids: Union[Unset, list[str]] = UNSET
    group_ids: Union[Unset, list[str]] = UNSET
    private: Union[Unset, bool] = UNSET
    custom_fields_mapping: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        task_type: Union[Unset, str] = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        summary = self.summary

        severity_id = self.severity_id

        incident_type_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.incident_type_ids, Unset):
            incident_type_ids = self.incident_type_ids

        service_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.service_ids, Unset):
            service_ids = self.service_ids

        functionality_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.functionality_ids, Unset):
            functionality_ids = self.functionality_ids

        environment_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.environment_ids, Unset):
            environment_ids = self.environment_ids

        group_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        private = self.private

        custom_fields_mapping: Union[None, Unset, str]
        if isinstance(self.custom_fields_mapping, Unset):
            custom_fields_mapping = UNSET
        else:
            custom_fields_mapping = self.custom_fields_mapping

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if summary is not UNSET:
            field_dict["summary"] = summary
        if severity_id is not UNSET:
            field_dict["severity_id"] = severity_id
        if incident_type_ids is not UNSET:
            field_dict["incident_type_ids"] = incident_type_ids
        if service_ids is not UNSET:
            field_dict["service_ids"] = service_ids
        if functionality_ids is not UNSET:
            field_dict["functionality_ids"] = functionality_ids
        if environment_ids is not UNSET:
            field_dict["environment_ids"] = environment_ids
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if private is not UNSET:
            field_dict["private"] = private
        if custom_fields_mapping is not UNSET:
            field_dict["custom_fields_mapping"] = custom_fields_mapping

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        _task_type = d.pop("task_type", UNSET)
        task_type: Union[Unset, CreateIncidentTaskParamsTaskType]
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_incident_task_params_task_type(_task_type)

        summary = d.pop("summary", UNSET)

        severity_id = d.pop("severity_id", UNSET)

        incident_type_ids = cast(list[str], d.pop("incident_type_ids", UNSET))

        service_ids = cast(list[str], d.pop("service_ids", UNSET))

        functionality_ids = cast(list[str], d.pop("functionality_ids", UNSET))

        environment_ids = cast(list[str], d.pop("environment_ids", UNSET))

        group_ids = cast(list[str], d.pop("group_ids", UNSET))

        private = d.pop("private", UNSET)

        def _parse_custom_fields_mapping(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        custom_fields_mapping = _parse_custom_fields_mapping(d.pop("custom_fields_mapping", UNSET))

        create_incident_task_params = cls(
            title=title,
            task_type=task_type,
            summary=summary,
            severity_id=severity_id,
            incident_type_ids=incident_type_ids,
            service_ids=service_ids,
            functionality_ids=functionality_ids,
            environment_ids=environment_ids,
            group_ids=group_ids,
            private=private,
            custom_fields_mapping=custom_fields_mapping,
        )

        create_incident_task_params.additional_properties = d
        return create_incident_task_params

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
