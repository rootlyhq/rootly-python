from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_zendesk_ticket_task_params_kind import (
    CreateZendeskTicketTaskParamsKind,
    check_create_zendesk_ticket_task_params_kind,
)
from ..models.create_zendesk_ticket_task_params_task_type import (
    CreateZendeskTicketTaskParamsTaskType,
    check_create_zendesk_ticket_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_zendesk_ticket_task_params_completion import CreateZendeskTicketTaskParamsCompletion
    from ..models.create_zendesk_ticket_task_params_priority import CreateZendeskTicketTaskParamsPriority


T = TypeVar("T", bound="CreateZendeskTicketTaskParams")


@_attrs_define
class CreateZendeskTicketTaskParams:
    """
    Attributes:
        kind (CreateZendeskTicketTaskParamsKind):
        subject (str): The ticket subject
        task_type (Union[Unset, CreateZendeskTicketTaskParamsTaskType]):
        comment (Union[Unset, str]): The ticket comment
        tags (Union[Unset, str]): The ticket tags
        priority (Union[Unset, CreateZendeskTicketTaskParamsPriority]): The priority id and display name
        completion (Union[Unset, CreateZendeskTicketTaskParamsCompletion]): The completion id and display name
        custom_fields_mapping (Union[None, Unset, str]): Custom field mappings. Can contain liquid markup and need to be
            valid JSON
        ticket_payload (Union[None, Unset, str]): Additional Zendesk ticket attributes. Will be merged into whatever was
            specified in this tasks current parameters. Can contain liquid markup and need to be valid JSON
    """

    kind: CreateZendeskTicketTaskParamsKind
    subject: str
    task_type: Unset | CreateZendeskTicketTaskParamsTaskType = UNSET
    comment: Unset | str = UNSET
    tags: Unset | str = UNSET
    priority: Union[Unset, "CreateZendeskTicketTaskParamsPriority"] = UNSET
    completion: Union[Unset, "CreateZendeskTicketTaskParamsCompletion"] = UNSET
    custom_fields_mapping: None | Unset | str = UNSET
    ticket_payload: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        subject = self.subject

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        comment = self.comment

        tags = self.tags

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

        ticket_payload: None | Unset | str
        if isinstance(self.ticket_payload, Unset):
            ticket_payload = UNSET
        else:
            ticket_payload = self.ticket_payload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "subject": subject,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if comment is not UNSET:
            field_dict["comment"] = comment
        if tags is not UNSET:
            field_dict["tags"] = tags
        if priority is not UNSET:
            field_dict["priority"] = priority
        if completion is not UNSET:
            field_dict["completion"] = completion
        if custom_fields_mapping is not UNSET:
            field_dict["custom_fields_mapping"] = custom_fields_mapping
        if ticket_payload is not UNSET:
            field_dict["ticket_payload"] = ticket_payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_zendesk_ticket_task_params_completion import CreateZendeskTicketTaskParamsCompletion
        from ..models.create_zendesk_ticket_task_params_priority import CreateZendeskTicketTaskParamsPriority

        d = dict(src_dict)
        kind = check_create_zendesk_ticket_task_params_kind(d.pop("kind"))

        subject = d.pop("subject")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | CreateZendeskTicketTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_zendesk_ticket_task_params_task_type(_task_type)

        comment = d.pop("comment", UNSET)

        tags = d.pop("tags", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Unset | CreateZendeskTicketTaskParamsPriority
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = CreateZendeskTicketTaskParamsPriority.from_dict(_priority)

        _completion = d.pop("completion", UNSET)
        completion: Unset | CreateZendeskTicketTaskParamsCompletion
        if isinstance(_completion, Unset):
            completion = UNSET
        else:
            completion = CreateZendeskTicketTaskParamsCompletion.from_dict(_completion)

        def _parse_custom_fields_mapping(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        custom_fields_mapping = _parse_custom_fields_mapping(d.pop("custom_fields_mapping", UNSET))

        def _parse_ticket_payload(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        ticket_payload = _parse_ticket_payload(d.pop("ticket_payload", UNSET))

        create_zendesk_ticket_task_params = cls(
            kind=kind,
            subject=subject,
            task_type=task_type,
            comment=comment,
            tags=tags,
            priority=priority,
            completion=completion,
            custom_fields_mapping=custom_fields_mapping,
            ticket_payload=ticket_payload,
        )

        create_zendesk_ticket_task_params.additional_properties = d
        return create_zendesk_ticket_task_params

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
