from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.page_rootly_on_call_responders_task_params_task_type import (
    PageRootlyOnCallRespondersTaskParamsTaskType,
    check_page_rootly_on_call_responders_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.page_rootly_on_call_responders_task_params_escalation_policy_target import (
        PageRootlyOnCallRespondersTaskParamsEscalationPolicyTarget,
    )
    from ..models.page_rootly_on_call_responders_task_params_group_target import (
        PageRootlyOnCallRespondersTaskParamsGroupTarget,
    )
    from ..models.page_rootly_on_call_responders_task_params_service_target import (
        PageRootlyOnCallRespondersTaskParamsServiceTarget,
    )
    from ..models.page_rootly_on_call_responders_task_params_user_target import (
        PageRootlyOnCallRespondersTaskParamsUserTarget,
    )


T = TypeVar("T", bound="PageRootlyOnCallRespondersTaskParams")


@_attrs_define
class PageRootlyOnCallRespondersTaskParams:
    """
    Attributes:
        alert_urgency_id (str): Alert urgency ID
        summary (str): Alert title
        task_type (Union[Unset, PageRootlyOnCallRespondersTaskParamsTaskType]):
        escalation_policy_target (Union[Unset, PageRootlyOnCallRespondersTaskParamsEscalationPolicyTarget]):
        service_target (Union[Unset, PageRootlyOnCallRespondersTaskParamsServiceTarget]):
        user_target (Union[Unset, PageRootlyOnCallRespondersTaskParamsUserTarget]):
        group_target (Union[Unset, PageRootlyOnCallRespondersTaskParamsGroupTarget]):
        description (Union[Unset, str]): Alert description
        escalation_note (Union[Unset, str]):
    """

    alert_urgency_id: str
    summary: str
    task_type: Unset | PageRootlyOnCallRespondersTaskParamsTaskType = UNSET
    escalation_policy_target: Union[Unset, "PageRootlyOnCallRespondersTaskParamsEscalationPolicyTarget"] = UNSET
    service_target: Union[Unset, "PageRootlyOnCallRespondersTaskParamsServiceTarget"] = UNSET
    user_target: Union[Unset, "PageRootlyOnCallRespondersTaskParamsUserTarget"] = UNSET
    group_target: Union[Unset, "PageRootlyOnCallRespondersTaskParamsGroupTarget"] = UNSET
    description: Unset | str = UNSET
    escalation_note: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_urgency_id = self.alert_urgency_id

        summary = self.summary

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        escalation_policy_target: Unset | dict[str, Any] = UNSET
        if not isinstance(self.escalation_policy_target, Unset):
            escalation_policy_target = self.escalation_policy_target.to_dict()

        service_target: Unset | dict[str, Any] = UNSET
        if not isinstance(self.service_target, Unset):
            service_target = self.service_target.to_dict()

        user_target: Unset | dict[str, Any] = UNSET
        if not isinstance(self.user_target, Unset):
            user_target = self.user_target.to_dict()

        group_target: Unset | dict[str, Any] = UNSET
        if not isinstance(self.group_target, Unset):
            group_target = self.group_target.to_dict()

        description = self.description

        escalation_note = self.escalation_note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_urgency_id": alert_urgency_id,
                "summary": summary,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if escalation_policy_target is not UNSET:
            field_dict["escalation_policy_target"] = escalation_policy_target
        if service_target is not UNSET:
            field_dict["service_target"] = service_target
        if user_target is not UNSET:
            field_dict["user_target"] = user_target
        if group_target is not UNSET:
            field_dict["group_target"] = group_target
        if description is not UNSET:
            field_dict["description"] = description
        if escalation_note is not UNSET:
            field_dict["escalation_note"] = escalation_note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.page_rootly_on_call_responders_task_params_escalation_policy_target import (
            PageRootlyOnCallRespondersTaskParamsEscalationPolicyTarget,
        )
        from ..models.page_rootly_on_call_responders_task_params_group_target import (
            PageRootlyOnCallRespondersTaskParamsGroupTarget,
        )
        from ..models.page_rootly_on_call_responders_task_params_service_target import (
            PageRootlyOnCallRespondersTaskParamsServiceTarget,
        )
        from ..models.page_rootly_on_call_responders_task_params_user_target import (
            PageRootlyOnCallRespondersTaskParamsUserTarget,
        )

        d = dict(src_dict)
        alert_urgency_id = d.pop("alert_urgency_id")

        summary = d.pop("summary")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | PageRootlyOnCallRespondersTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_page_rootly_on_call_responders_task_params_task_type(_task_type)

        _escalation_policy_target = d.pop("escalation_policy_target", UNSET)
        escalation_policy_target: Unset | PageRootlyOnCallRespondersTaskParamsEscalationPolicyTarget
        if isinstance(_escalation_policy_target, Unset):
            escalation_policy_target = UNSET
        else:
            escalation_policy_target = PageRootlyOnCallRespondersTaskParamsEscalationPolicyTarget.from_dict(
                _escalation_policy_target
            )

        _service_target = d.pop("service_target", UNSET)
        service_target: Unset | PageRootlyOnCallRespondersTaskParamsServiceTarget
        if isinstance(_service_target, Unset):
            service_target = UNSET
        else:
            service_target = PageRootlyOnCallRespondersTaskParamsServiceTarget.from_dict(_service_target)

        _user_target = d.pop("user_target", UNSET)
        user_target: Unset | PageRootlyOnCallRespondersTaskParamsUserTarget
        if isinstance(_user_target, Unset):
            user_target = UNSET
        else:
            user_target = PageRootlyOnCallRespondersTaskParamsUserTarget.from_dict(_user_target)

        _group_target = d.pop("group_target", UNSET)
        group_target: Unset | PageRootlyOnCallRespondersTaskParamsGroupTarget
        if isinstance(_group_target, Unset):
            group_target = UNSET
        else:
            group_target = PageRootlyOnCallRespondersTaskParamsGroupTarget.from_dict(_group_target)

        description = d.pop("description", UNSET)

        escalation_note = d.pop("escalation_note", UNSET)

        page_rootly_on_call_responders_task_params = cls(
            alert_urgency_id=alert_urgency_id,
            summary=summary,
            task_type=task_type,
            escalation_policy_target=escalation_policy_target,
            service_target=service_target,
            user_target=user_target,
            group_target=group_target,
            description=description,
            escalation_note=escalation_note,
        )

        page_rootly_on_call_responders_task_params.additional_properties = d
        return page_rootly_on_call_responders_task_params

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
