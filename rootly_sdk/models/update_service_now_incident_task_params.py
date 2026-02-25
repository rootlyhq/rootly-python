from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_service_now_incident_task_params_task_type import (
    UpdateServiceNowIncidentTaskParamsTaskType,
    check_update_service_now_incident_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_service_now_incident_task_params_completion import UpdateServiceNowIncidentTaskParamsCompletion
    from ..models.update_service_now_incident_task_params_priority import UpdateServiceNowIncidentTaskParamsPriority


T = TypeVar("T", bound="UpdateServiceNowIncidentTaskParams")


@_attrs_define
class UpdateServiceNowIncidentTaskParams:
    """
    Attributes:
        incident_id (str): The incident id
        task_type (Union[Unset, UpdateServiceNowIncidentTaskParamsTaskType]):
        title (Union[Unset, str]): The incident title
        description (Union[Unset, str]): The incident description
        priority (Union[Unset, UpdateServiceNowIncidentTaskParamsPriority]): The priority id and display name
        completion (Union[Unset, UpdateServiceNowIncidentTaskParamsCompletion]): The completion id and display name
        custom_fields_mapping (Union[None, Unset, str]): Custom field mappings. Can contain liquid markup and need to be
            valid JSON
    """

    incident_id: str
    task_type: Unset | UpdateServiceNowIncidentTaskParamsTaskType = UNSET
    title: Unset | str = UNSET
    description: Unset | str = UNSET
    priority: Union[Unset, "UpdateServiceNowIncidentTaskParamsPriority"] = UNSET
    completion: Union[Unset, "UpdateServiceNowIncidentTaskParamsCompletion"] = UNSET
    custom_fields_mapping: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_id = self.incident_id

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        title = self.title

        description = self.description

        priority: Unset | dict[str, Any] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.to_dict()

        completion: Unset | dict[str, Any] = UNSET
        if not isinstance(self.completion, Unset):
            completion = self.completion.to_dict()

        custom_fields_mapping: None | Unset | str
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
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if priority is not UNSET:
            field_dict["priority"] = priority
        if completion is not UNSET:
            field_dict["completion"] = completion
        if custom_fields_mapping is not UNSET:
            field_dict["custom_fields_mapping"] = custom_fields_mapping

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_service_now_incident_task_params_completion import (
            UpdateServiceNowIncidentTaskParamsCompletion,
        )
        from ..models.update_service_now_incident_task_params_priority import UpdateServiceNowIncidentTaskParamsPriority

        d = dict(src_dict)
        incident_id = d.pop("incident_id")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | UpdateServiceNowIncidentTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_service_now_incident_task_params_task_type(_task_type)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Unset | UpdateServiceNowIncidentTaskParamsPriority
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = UpdateServiceNowIncidentTaskParamsPriority.from_dict(_priority)

        _completion = d.pop("completion", UNSET)
        completion: Unset | UpdateServiceNowIncidentTaskParamsCompletion
        if isinstance(_completion, Unset):
            completion = UNSET
        else:
            completion = UpdateServiceNowIncidentTaskParamsCompletion.from_dict(_completion)

        def _parse_custom_fields_mapping(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        custom_fields_mapping = _parse_custom_fields_mapping(d.pop("custom_fields_mapping", UNSET))

        update_service_now_incident_task_params = cls(
            incident_id=incident_id,
            task_type=task_type,
            title=title,
            description=description,
            priority=priority,
            completion=completion,
            custom_fields_mapping=custom_fields_mapping,
        )

        update_service_now_incident_task_params.additional_properties = d
        return update_service_now_incident_task_params

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
