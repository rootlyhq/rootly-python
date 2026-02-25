from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.page_pagerduty_on_call_responders_task_params_task_type import (
    PagePagerdutyOnCallRespondersTaskParamsTaskType,
    check_page_pagerduty_on_call_responders_task_params_task_type,
)
from ..models.page_pagerduty_on_call_responders_task_params_urgency import (
    PagePagerdutyOnCallRespondersTaskParamsUrgency,
    check_page_pagerduty_on_call_responders_task_params_urgency,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.page_pagerduty_on_call_responders_task_params_escalation_policies_item import (
        PagePagerdutyOnCallRespondersTaskParamsEscalationPoliciesItem,
    )
    from ..models.page_pagerduty_on_call_responders_task_params_service import (
        PagePagerdutyOnCallRespondersTaskParamsService,
    )
    from ..models.page_pagerduty_on_call_responders_task_params_users_item import (
        PagePagerdutyOnCallRespondersTaskParamsUsersItem,
    )


T = TypeVar("T", bound="PagePagerdutyOnCallRespondersTaskParams")


@_attrs_define
class PagePagerdutyOnCallRespondersTaskParams:
    """
    Attributes:
        service (PagePagerdutyOnCallRespondersTaskParamsService):
        task_type (Union[Unset, PagePagerdutyOnCallRespondersTaskParamsTaskType]):
        escalation_policies (Union[Unset, list['PagePagerdutyOnCallRespondersTaskParamsEscalationPoliciesItem']]):
        users (Union[Unset, list['PagePagerdutyOnCallRespondersTaskParamsUsersItem']]):
        title (Union[None, Unset, str]): Incident title.
        message (Union[Unset, str]):
        urgency (Union[Unset, PagePagerdutyOnCallRespondersTaskParamsUrgency]):  Default: 'high'.
        priority (Union[Unset, str]): PagerDuty incident priority, selecting auto will let Rootly auto map our incident
            severity
        create_new_incident_on_conflict (Union[Unset, bool]): Rootly only supports linking to a single PagerDuty
            incident. If this feature is disabled Rootly will add responders from any additional pages to the existing
            PagerDuty incident that is linked to the Rootly incident. If enabled, Rootly will create a new PagerDuty
            incident that is not linked to any Rootly incidents Default: False.
    """

    service: "PagePagerdutyOnCallRespondersTaskParamsService"
    task_type: Unset | PagePagerdutyOnCallRespondersTaskParamsTaskType = UNSET
    escalation_policies: Unset | list["PagePagerdutyOnCallRespondersTaskParamsEscalationPoliciesItem"] = UNSET
    users: Unset | list["PagePagerdutyOnCallRespondersTaskParamsUsersItem"] = UNSET
    title: None | Unset | str = UNSET
    message: Unset | str = UNSET
    urgency: Unset | PagePagerdutyOnCallRespondersTaskParamsUrgency = "high"
    priority: Unset | str = UNSET
    create_new_incident_on_conflict: Unset | bool = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service = self.service.to_dict()

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        escalation_policies: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.escalation_policies, Unset):
            escalation_policies = []
            for escalation_policies_item_data in self.escalation_policies:
                escalation_policies_item = escalation_policies_item_data.to_dict()
                escalation_policies.append(escalation_policies_item)

        users: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        title: None | Unset | str
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        message = self.message

        urgency: Unset | str = UNSET
        if not isinstance(self.urgency, Unset):
            urgency = self.urgency

        priority = self.priority

        create_new_incident_on_conflict = self.create_new_incident_on_conflict

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "service": service,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if escalation_policies is not UNSET:
            field_dict["escalation_policies"] = escalation_policies
        if users is not UNSET:
            field_dict["users"] = users
        if title is not UNSET:
            field_dict["title"] = title
        if message is not UNSET:
            field_dict["message"] = message
        if urgency is not UNSET:
            field_dict["urgency"] = urgency
        if priority is not UNSET:
            field_dict["priority"] = priority
        if create_new_incident_on_conflict is not UNSET:
            field_dict["create_new_incident_on_conflict"] = create_new_incident_on_conflict

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.page_pagerduty_on_call_responders_task_params_escalation_policies_item import (
            PagePagerdutyOnCallRespondersTaskParamsEscalationPoliciesItem,
        )
        from ..models.page_pagerduty_on_call_responders_task_params_service import (
            PagePagerdutyOnCallRespondersTaskParamsService,
        )
        from ..models.page_pagerduty_on_call_responders_task_params_users_item import (
            PagePagerdutyOnCallRespondersTaskParamsUsersItem,
        )

        d = dict(src_dict)
        service = PagePagerdutyOnCallRespondersTaskParamsService.from_dict(d.pop("service"))

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | PagePagerdutyOnCallRespondersTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_page_pagerduty_on_call_responders_task_params_task_type(_task_type)

        escalation_policies = []
        _escalation_policies = d.pop("escalation_policies", UNSET)
        for escalation_policies_item_data in _escalation_policies or []:
            escalation_policies_item = PagePagerdutyOnCallRespondersTaskParamsEscalationPoliciesItem.from_dict(
                escalation_policies_item_data
            )

            escalation_policies.append(escalation_policies_item)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = PagePagerdutyOnCallRespondersTaskParamsUsersItem.from_dict(users_item_data)

            users.append(users_item)

        def _parse_title(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        title = _parse_title(d.pop("title", UNSET))

        message = d.pop("message", UNSET)

        _urgency = d.pop("urgency", UNSET)
        urgency: Unset | PagePagerdutyOnCallRespondersTaskParamsUrgency
        if isinstance(_urgency, Unset):
            urgency = UNSET
        else:
            urgency = check_page_pagerduty_on_call_responders_task_params_urgency(_urgency)

        priority = d.pop("priority", UNSET)

        create_new_incident_on_conflict = d.pop("create_new_incident_on_conflict", UNSET)

        page_pagerduty_on_call_responders_task_params = cls(
            service=service,
            task_type=task_type,
            escalation_policies=escalation_policies,
            users=users,
            title=title,
            message=message,
            urgency=urgency,
            priority=priority,
            create_new_incident_on_conflict=create_new_incident_on_conflict,
        )

        page_pagerduty_on_call_responders_task_params.additional_properties = d
        return page_pagerduty_on_call_responders_task_params

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
