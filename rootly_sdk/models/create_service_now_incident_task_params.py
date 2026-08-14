from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_service_now_incident_task_params_task_type import (
    CreateServiceNowIncidentTaskParamsTaskType,
    check_create_service_now_incident_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_service_now_incident_task_params_completion import CreateServiceNowIncidentTaskParamsCompletion
    from ..models.create_service_now_incident_task_params_priority import CreateServiceNowIncidentTaskParamsPriority


T = TypeVar("T", bound="CreateServiceNowIncidentTaskParams")


@_attrs_define
class CreateServiceNowIncidentTaskParams:
    """
    Attributes:
        title (str): The incident title
        task_type (Union[Unset, CreateServiceNowIncidentTaskParamsTaskType]):
        description (Union[Unset, str]): The incident description
        priority (Union[Unset, CreateServiceNowIncidentTaskParamsPriority]): The priority id and display name
        completion (Union[Unset, CreateServiceNowIncidentTaskParamsCompletion]): The completion id and display name
        custom_fields_mapping (Union[None, Unset, str]): Custom field mappings. Can contain liquid markup and need to be
            valid JSON
    """

    title: str
    task_type: Unset | CreateServiceNowIncidentTaskParamsTaskType = UNSET
    description: Unset | str = UNSET
    priority: Union[Unset, "CreateServiceNowIncidentTaskParamsPriority"] = UNSET
    completion: Union[Unset, "CreateServiceNowIncidentTaskParamsCompletion"] = UNSET
    custom_fields_mapping: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

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
                "title": title,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
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
        from ..models.create_service_now_incident_task_params_completion import (
            CreateServiceNowIncidentTaskParamsCompletion,
        )
        from ..models.create_service_now_incident_task_params_priority import CreateServiceNowIncidentTaskParamsPriority

        d = dict(src_dict)
        title = d.pop("title")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | CreateServiceNowIncidentTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_service_now_incident_task_params_task_type(_task_type)

        description = d.pop("description", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Unset | CreateServiceNowIncidentTaskParamsPriority
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = CreateServiceNowIncidentTaskParamsPriority.from_dict(_priority)

        _completion = d.pop("completion", UNSET)
        completion: Unset | CreateServiceNowIncidentTaskParamsCompletion
        if isinstance(_completion, Unset):
            completion = UNSET
        else:
            completion = CreateServiceNowIncidentTaskParamsCompletion.from_dict(_completion)

        def _parse_custom_fields_mapping(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        custom_fields_mapping = _parse_custom_fields_mapping(d.pop("custom_fields_mapping", UNSET))

        create_service_now_incident_task_params = cls(
            title=title,
            task_type=task_type,
            description=description,
            priority=priority,
            completion=completion,
            custom_fields_mapping=custom_fields_mapping,
        )

        create_service_now_incident_task_params.additional_properties = d
        return create_service_now_incident_task_params

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
