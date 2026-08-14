from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_incident_task_params_attribute_to_query_by import (
    UpdateIncidentTaskParamsAttributeToQueryBy,
    check_update_incident_task_params_attribute_to_query_by,
)
from ..models.update_incident_task_params_task_type import (
    UpdateIncidentTaskParamsTaskType,
    check_update_incident_task_params_task_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateIncidentTaskParams")


@_attrs_define
class UpdateIncidentTaskParams:
    """
    Attributes:
        incident_id (str): The incident id to update or id of any attribute on the incident
        task_type (Union[Unset, UpdateIncidentTaskParamsTaskType]):
        attribute_to_query_by (Union[Unset, UpdateIncidentTaskParamsAttributeToQueryBy]):  Default: 'id'.
        title (Union[None, Unset, str]): The incident title
        summary (Union[None, Unset, str]): The incident summary
        status (Union[None, Unset, str]):
        severity_id (Union[None, Unset, str]):
        incident_type_ids (Union[None, Unset, list[str]]):
        service_ids (Union[None, Unset, list[str]]): Array of service UUIDs
        functionality_ids (Union[None, Unset, list[str]]): Array of functionality UUIDs
        environment_ids (Union[None, Unset, list[str]]):
        group_ids (Union[None, Unset, list[str]]): Array of group/team UUIDs
        started_at (Union[None, Unset, str]):
        detected_at (Union[None, Unset, str]):
        acknowledged_at (Union[None, Unset, str]):
        mitigated_at (Union[None, Unset, str]):
        resolved_at (Union[None, Unset, str]):
        private (Union[Unset, bool]):
        custom_fields_mapping (Union[None, Unset, str]): Custom field mappings. Can contain liquid markup and need to be
            valid JSON. Use 'services', 'functionalities', or 'groups' keys with arrays of names/slugs for name/slug lookup
    """

    incident_id: str
    task_type: Union[Unset, UpdateIncidentTaskParamsTaskType] = UNSET
    attribute_to_query_by: Union[Unset, UpdateIncidentTaskParamsAttributeToQueryBy] = "id"
    title: Union[None, Unset, str] = UNSET
    summary: Union[None, Unset, str] = UNSET
    status: Union[None, Unset, str] = UNSET
    severity_id: Union[None, Unset, str] = UNSET
    incident_type_ids: Union[None, Unset, list[str]] = UNSET
    service_ids: Union[None, Unset, list[str]] = UNSET
    functionality_ids: Union[None, Unset, list[str]] = UNSET
    environment_ids: Union[None, Unset, list[str]] = UNSET
    group_ids: Union[None, Unset, list[str]] = UNSET
    started_at: Union[None, Unset, str] = UNSET
    detected_at: Union[None, Unset, str] = UNSET
    acknowledged_at: Union[None, Unset, str] = UNSET
    mitigated_at: Union[None, Unset, str] = UNSET
    resolved_at: Union[None, Unset, str] = UNSET
    private: Union[Unset, bool] = UNSET
    custom_fields_mapping: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_id = self.incident_id

        task_type: Union[Unset, str] = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        attribute_to_query_by: Union[Unset, str] = UNSET
        if not isinstance(self.attribute_to_query_by, Unset):
            attribute_to_query_by = self.attribute_to_query_by

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        summary: Union[None, Unset, str]
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        severity_id: Union[None, Unset, str]
        if isinstance(self.severity_id, Unset):
            severity_id = UNSET
        else:
            severity_id = self.severity_id

        incident_type_ids: Union[None, Unset, list[str]]
        if isinstance(self.incident_type_ids, Unset):
            incident_type_ids = UNSET
        elif isinstance(self.incident_type_ids, list):
            incident_type_ids = self.incident_type_ids

        else:
            incident_type_ids = self.incident_type_ids

        service_ids: Union[None, Unset, list[str]]
        if isinstance(self.service_ids, Unset):
            service_ids = UNSET
        elif isinstance(self.service_ids, list):
            service_ids = self.service_ids

        else:
            service_ids = self.service_ids

        functionality_ids: Union[None, Unset, list[str]]
        if isinstance(self.functionality_ids, Unset):
            functionality_ids = UNSET
        elif isinstance(self.functionality_ids, list):
            functionality_ids = self.functionality_ids

        else:
            functionality_ids = self.functionality_ids

        environment_ids: Union[None, Unset, list[str]]
        if isinstance(self.environment_ids, Unset):
            environment_ids = UNSET
        elif isinstance(self.environment_ids, list):
            environment_ids = self.environment_ids

        else:
            environment_ids = self.environment_ids

        group_ids: Union[None, Unset, list[str]]
        if isinstance(self.group_ids, Unset):
            group_ids = UNSET
        elif isinstance(self.group_ids, list):
            group_ids = self.group_ids

        else:
            group_ids = self.group_ids

        started_at: Union[None, Unset, str]
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        else:
            started_at = self.started_at

        detected_at: Union[None, Unset, str]
        if isinstance(self.detected_at, Unset):
            detected_at = UNSET
        else:
            detected_at = self.detected_at

        acknowledged_at: Union[None, Unset, str]
        if isinstance(self.acknowledged_at, Unset):
            acknowledged_at = UNSET
        else:
            acknowledged_at = self.acknowledged_at

        mitigated_at: Union[None, Unset, str]
        if isinstance(self.mitigated_at, Unset):
            mitigated_at = UNSET
        else:
            mitigated_at = self.mitigated_at

        resolved_at: Union[None, Unset, str]
        if isinstance(self.resolved_at, Unset):
            resolved_at = UNSET
        else:
            resolved_at = self.resolved_at

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
                "incident_id": incident_id,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if attribute_to_query_by is not UNSET:
            field_dict["attribute_to_query_by"] = attribute_to_query_by
        if title is not UNSET:
            field_dict["title"] = title
        if summary is not UNSET:
            field_dict["summary"] = summary
        if status is not UNSET:
            field_dict["status"] = status
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
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if detected_at is not UNSET:
            field_dict["detected_at"] = detected_at
        if acknowledged_at is not UNSET:
            field_dict["acknowledged_at"] = acknowledged_at
        if mitigated_at is not UNSET:
            field_dict["mitigated_at"] = mitigated_at
        if resolved_at is not UNSET:
            field_dict["resolved_at"] = resolved_at
        if private is not UNSET:
            field_dict["private"] = private
        if custom_fields_mapping is not UNSET:
            field_dict["custom_fields_mapping"] = custom_fields_mapping

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        incident_id = d.pop("incident_id")

        _task_type = d.pop("task_type", UNSET)
        task_type: Union[Unset, UpdateIncidentTaskParamsTaskType]
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_incident_task_params_task_type(_task_type)

        _attribute_to_query_by = d.pop("attribute_to_query_by", UNSET)
        attribute_to_query_by: Union[Unset, UpdateIncidentTaskParamsAttributeToQueryBy]
        if isinstance(_attribute_to_query_by, Unset):
            attribute_to_query_by = UNSET
        else:
            attribute_to_query_by = check_update_incident_task_params_attribute_to_query_by(_attribute_to_query_by)

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_summary(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        summary = _parse_summary(d.pop("summary", UNSET))

        def _parse_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_severity_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        severity_id = _parse_severity_id(d.pop("severity_id", UNSET))

        def _parse_incident_type_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                incident_type_ids_type_0 = cast(list[str], data)

                return incident_type_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        incident_type_ids = _parse_incident_type_ids(d.pop("incident_type_ids", UNSET))

        def _parse_service_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                service_ids_type_0 = cast(list[str], data)

                return service_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        service_ids = _parse_service_ids(d.pop("service_ids", UNSET))

        def _parse_functionality_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                functionality_ids_type_0 = cast(list[str], data)

                return functionality_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        functionality_ids = _parse_functionality_ids(d.pop("functionality_ids", UNSET))

        def _parse_environment_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                environment_ids_type_0 = cast(list[str], data)

                return environment_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        environment_ids = _parse_environment_ids(d.pop("environment_ids", UNSET))

        def _parse_group_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                group_ids_type_0 = cast(list[str], data)

                return group_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        group_ids = _parse_group_ids(d.pop("group_ids", UNSET))

        def _parse_started_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_detected_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        detected_at = _parse_detected_at(d.pop("detected_at", UNSET))

        def _parse_acknowledged_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        acknowledged_at = _parse_acknowledged_at(d.pop("acknowledged_at", UNSET))

        def _parse_mitigated_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mitigated_at = _parse_mitigated_at(d.pop("mitigated_at", UNSET))

        def _parse_resolved_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        resolved_at = _parse_resolved_at(d.pop("resolved_at", UNSET))

        private = d.pop("private", UNSET)

        def _parse_custom_fields_mapping(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        custom_fields_mapping = _parse_custom_fields_mapping(d.pop("custom_fields_mapping", UNSET))

        update_incident_task_params = cls(
            incident_id=incident_id,
            task_type=task_type,
            attribute_to_query_by=attribute_to_query_by,
            title=title,
            summary=summary,
            status=status,
            severity_id=severity_id,
            incident_type_ids=incident_type_ids,
            service_ids=service_ids,
            functionality_ids=functionality_ids,
            environment_ids=environment_ids,
            group_ids=group_ids,
            started_at=started_at,
            detected_at=detected_at,
            acknowledged_at=acknowledged_at,
            mitigated_at=mitigated_at,
            resolved_at=resolved_at,
            private=private,
            custom_fields_mapping=custom_fields_mapping,
        )

        update_incident_task_params.additional_properties = d
        return update_incident_task_params

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
