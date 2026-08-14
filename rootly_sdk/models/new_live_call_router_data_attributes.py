from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.new_live_call_router_data_attributes_country_code import (
    NewLiveCallRouterDataAttributesCountryCode,
    check_new_live_call_router_data_attributes_country_code,
)
from ..models.new_live_call_router_data_attributes_kind import (
    NewLiveCallRouterDataAttributesKind,
    check_new_live_call_router_data_attributes_kind,
)
from ..models.new_live_call_router_data_attributes_phone_type import (
    NewLiveCallRouterDataAttributesPhoneType,
    check_new_live_call_router_data_attributes_phone_type,
)
from ..models.new_live_call_router_data_attributes_waiting_music_url import (
    NewLiveCallRouterDataAttributesWaitingMusicUrl,
    check_new_live_call_router_data_attributes_waiting_music_url,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_live_call_router_data_attributes_escalation_policy_trigger_params import (
        NewLiveCallRouterDataAttributesEscalationPolicyTriggerParams,
    )
    from ..models.new_live_call_router_data_attributes_paging_targets_item import (
        NewLiveCallRouterDataAttributesPagingTargetsItem,
    )


T = TypeVar("T", bound="NewLiveCallRouterDataAttributes")


@_attrs_define
class NewLiveCallRouterDataAttributes:
    """
    Attributes:
        kind (NewLiveCallRouterDataAttributesKind): The kind of the live_call_router
        name (str): The name of the live_call_router
        country_code (NewLiveCallRouterDataAttributesCountryCode): The country code of the live_call_router
        phone_type (NewLiveCallRouterDataAttributesPhoneType): The phone type of the live_call_router
        phone_number (str): You can select a phone number using
            [generate_phone_number](#//api/v1/live_call_routers/generate_phone_number) API and pass that phone number here
            to register
        voicemail_greeting (str): The voicemail greeting of the live_call_router
        paging_targets (list['NewLiveCallRouterDataAttributesPagingTargetsItem']): Paging targets that callers can
            select from when this live call router is configured as a phone tree.
        enabled (Union[Unset, bool]): Whether the live_call_router is enabled
        caller_greeting (Union[Unset, str]): The caller greeting message of the live_call_router
        unavailable_responder_message (Union[None, Unset, str]): The message played to the caller when a responder
            doesn't answer and the call moves on to the next person in the escalation. Leave blank to use the default
            message.
        waiting_music_url (Union[Unset, NewLiveCallRouterDataAttributesWaitingMusicUrl]): The waiting music URL of the
            live_call_router
        sent_to_voicemail_delay (Union[Unset, int]): The delay (seconds) after which the caller in redirected to
            voicemail
        should_redirect_to_voicemail_on_no_answer (Union[Unset, bool]): This prompts the caller to choose voicemail or
            connect live
        escalation_level_delay_in_seconds (Union[Unset, int]): This overrides the delay (seconds) in escalation levels
        should_auto_resolve_alert_on_call_end (Union[Unset, bool]): This overrides the delay (seconds) in escalation
            levels
        notify_via_sms (Union[Unset, bool]): Whether responders are also notified via SMS when this router pages them
        notify_via_push_notification (Union[Unset, bool]): Whether responders are also notified via push notification
            when this router pages them
        informational_notification_message (Union[None, Unset, str]): Optional message included in the SMS/push
            notification. Supports variables such as {{ alert.url }}, {{ alert.data.* }}, and {{ alert.alert_urgency.name
            }}.
        alert_urgency_id (Union[Unset, str]): This is used in escalation paths to determine who to page
        calling_tree_enabled (Union[Unset, bool]): Whether the live call router is configured as a phone tree, requiring
            callers to press a key before being connected
        calling_tree_prompt (Union[Unset, str]): The audio instructions callers will hear when they call this number,
            prompting them to select from available options to route their call
        escalation_policy_trigger_params (Union[Unset, NewLiveCallRouterDataAttributesEscalationPolicyTriggerParams]):
    """

    kind: NewLiveCallRouterDataAttributesKind
    name: str
    country_code: NewLiveCallRouterDataAttributesCountryCode
    phone_type: NewLiveCallRouterDataAttributesPhoneType
    phone_number: str
    voicemail_greeting: str
    paging_targets: list["NewLiveCallRouterDataAttributesPagingTargetsItem"]
    enabled: Union[Unset, bool] = UNSET
    caller_greeting: Union[Unset, str] = UNSET
    unavailable_responder_message: Union[None, Unset, str] = UNSET
    waiting_music_url: Union[Unset, NewLiveCallRouterDataAttributesWaitingMusicUrl] = UNSET
    sent_to_voicemail_delay: Union[Unset, int] = UNSET
    should_redirect_to_voicemail_on_no_answer: Union[Unset, bool] = UNSET
    escalation_level_delay_in_seconds: Union[Unset, int] = UNSET
    should_auto_resolve_alert_on_call_end: Union[Unset, bool] = UNSET
    notify_via_sms: Union[Unset, bool] = UNSET
    notify_via_push_notification: Union[Unset, bool] = UNSET
    informational_notification_message: Union[None, Unset, str] = UNSET
    alert_urgency_id: Union[Unset, str] = UNSET
    calling_tree_enabled: Union[Unset, bool] = UNSET
    calling_tree_prompt: Union[Unset, str] = UNSET
    escalation_policy_trigger_params: Union[Unset, "NewLiveCallRouterDataAttributesEscalationPolicyTriggerParams"] = (
        UNSET
    )

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        name = self.name

        country_code: str = self.country_code

        phone_type: str = self.phone_type

        phone_number = self.phone_number

        voicemail_greeting = self.voicemail_greeting

        paging_targets = []
        for paging_targets_item_data in self.paging_targets:
            paging_targets_item = paging_targets_item_data.to_dict()
            paging_targets.append(paging_targets_item)

        enabled = self.enabled

        caller_greeting = self.caller_greeting

        unavailable_responder_message: Union[None, Unset, str]
        if isinstance(self.unavailable_responder_message, Unset):
            unavailable_responder_message = UNSET
        else:
            unavailable_responder_message = self.unavailable_responder_message

        waiting_music_url: Union[Unset, str] = UNSET
        if not isinstance(self.waiting_music_url, Unset):
            waiting_music_url = self.waiting_music_url

        sent_to_voicemail_delay = self.sent_to_voicemail_delay

        should_redirect_to_voicemail_on_no_answer = self.should_redirect_to_voicemail_on_no_answer

        escalation_level_delay_in_seconds = self.escalation_level_delay_in_seconds

        should_auto_resolve_alert_on_call_end = self.should_auto_resolve_alert_on_call_end

        notify_via_sms = self.notify_via_sms

        notify_via_push_notification = self.notify_via_push_notification

        informational_notification_message: Union[None, Unset, str]
        if isinstance(self.informational_notification_message, Unset):
            informational_notification_message = UNSET
        else:
            informational_notification_message = self.informational_notification_message

        alert_urgency_id = self.alert_urgency_id

        calling_tree_enabled = self.calling_tree_enabled

        calling_tree_prompt = self.calling_tree_prompt

        escalation_policy_trigger_params: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.escalation_policy_trigger_params, Unset):
            escalation_policy_trigger_params = self.escalation_policy_trigger_params.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "name": name,
                "country_code": country_code,
                "phone_type": phone_type,
                "phone_number": phone_number,
                "voicemail_greeting": voicemail_greeting,
                "paging_targets": paging_targets,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if caller_greeting is not UNSET:
            field_dict["caller_greeting"] = caller_greeting
        if unavailable_responder_message is not UNSET:
            field_dict["unavailable_responder_message"] = unavailable_responder_message
        if waiting_music_url is not UNSET:
            field_dict["waiting_music_url"] = waiting_music_url
        if sent_to_voicemail_delay is not UNSET:
            field_dict["sent_to_voicemail_delay"] = sent_to_voicemail_delay
        if should_redirect_to_voicemail_on_no_answer is not UNSET:
            field_dict["should_redirect_to_voicemail_on_no_answer"] = should_redirect_to_voicemail_on_no_answer
        if escalation_level_delay_in_seconds is not UNSET:
            field_dict["escalation_level_delay_in_seconds"] = escalation_level_delay_in_seconds
        if should_auto_resolve_alert_on_call_end is not UNSET:
            field_dict["should_auto_resolve_alert_on_call_end"] = should_auto_resolve_alert_on_call_end
        if notify_via_sms is not UNSET:
            field_dict["notify_via_sms"] = notify_via_sms
        if notify_via_push_notification is not UNSET:
            field_dict["notify_via_push_notification"] = notify_via_push_notification
        if informational_notification_message is not UNSET:
            field_dict["informational_notification_message"] = informational_notification_message
        if alert_urgency_id is not UNSET:
            field_dict["alert_urgency_id"] = alert_urgency_id
        if calling_tree_enabled is not UNSET:
            field_dict["calling_tree_enabled"] = calling_tree_enabled
        if calling_tree_prompt is not UNSET:
            field_dict["calling_tree_prompt"] = calling_tree_prompt
        if escalation_policy_trigger_params is not UNSET:
            field_dict["escalation_policy_trigger_params"] = escalation_policy_trigger_params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_live_call_router_data_attributes_escalation_policy_trigger_params import (
            NewLiveCallRouterDataAttributesEscalationPolicyTriggerParams,
        )
        from ..models.new_live_call_router_data_attributes_paging_targets_item import (
            NewLiveCallRouterDataAttributesPagingTargetsItem,
        )

        d = dict(src_dict)
        kind = check_new_live_call_router_data_attributes_kind(d.pop("kind"))

        name = d.pop("name")

        country_code = check_new_live_call_router_data_attributes_country_code(d.pop("country_code"))

        phone_type = check_new_live_call_router_data_attributes_phone_type(d.pop("phone_type"))

        phone_number = d.pop("phone_number")

        voicemail_greeting = d.pop("voicemail_greeting")

        paging_targets = []
        _paging_targets = d.pop("paging_targets")
        for paging_targets_item_data in _paging_targets:
            paging_targets_item = NewLiveCallRouterDataAttributesPagingTargetsItem.from_dict(paging_targets_item_data)

            paging_targets.append(paging_targets_item)

        enabled = d.pop("enabled", UNSET)

        caller_greeting = d.pop("caller_greeting", UNSET)

        def _parse_unavailable_responder_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        unavailable_responder_message = _parse_unavailable_responder_message(
            d.pop("unavailable_responder_message", UNSET)
        )

        _waiting_music_url = d.pop("waiting_music_url", UNSET)
        waiting_music_url: Union[Unset, NewLiveCallRouterDataAttributesWaitingMusicUrl]
        if isinstance(_waiting_music_url, Unset):
            waiting_music_url = UNSET
        else:
            waiting_music_url = check_new_live_call_router_data_attributes_waiting_music_url(_waiting_music_url)

        sent_to_voicemail_delay = d.pop("sent_to_voicemail_delay", UNSET)

        should_redirect_to_voicemail_on_no_answer = d.pop("should_redirect_to_voicemail_on_no_answer", UNSET)

        escalation_level_delay_in_seconds = d.pop("escalation_level_delay_in_seconds", UNSET)

        should_auto_resolve_alert_on_call_end = d.pop("should_auto_resolve_alert_on_call_end", UNSET)

        notify_via_sms = d.pop("notify_via_sms", UNSET)

        notify_via_push_notification = d.pop("notify_via_push_notification", UNSET)

        def _parse_informational_notification_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        informational_notification_message = _parse_informational_notification_message(
            d.pop("informational_notification_message", UNSET)
        )

        alert_urgency_id = d.pop("alert_urgency_id", UNSET)

        calling_tree_enabled = d.pop("calling_tree_enabled", UNSET)

        calling_tree_prompt = d.pop("calling_tree_prompt", UNSET)

        _escalation_policy_trigger_params = d.pop("escalation_policy_trigger_params", UNSET)
        escalation_policy_trigger_params: Union[Unset, NewLiveCallRouterDataAttributesEscalationPolicyTriggerParams]
        if isinstance(_escalation_policy_trigger_params, Unset):
            escalation_policy_trigger_params = UNSET
        else:
            escalation_policy_trigger_params = NewLiveCallRouterDataAttributesEscalationPolicyTriggerParams.from_dict(
                _escalation_policy_trigger_params
            )

        new_live_call_router_data_attributes = cls(
            kind=kind,
            name=name,
            country_code=country_code,
            phone_type=phone_type,
            phone_number=phone_number,
            voicemail_greeting=voicemail_greeting,
            paging_targets=paging_targets,
            enabled=enabled,
            caller_greeting=caller_greeting,
            unavailable_responder_message=unavailable_responder_message,
            waiting_music_url=waiting_music_url,
            sent_to_voicemail_delay=sent_to_voicemail_delay,
            should_redirect_to_voicemail_on_no_answer=should_redirect_to_voicemail_on_no_answer,
            escalation_level_delay_in_seconds=escalation_level_delay_in_seconds,
            should_auto_resolve_alert_on_call_end=should_auto_resolve_alert_on_call_end,
            notify_via_sms=notify_via_sms,
            notify_via_push_notification=notify_via_push_notification,
            informational_notification_message=informational_notification_message,
            alert_urgency_id=alert_urgency_id,
            calling_tree_enabled=calling_tree_enabled,
            calling_tree_prompt=calling_tree_prompt,
            escalation_policy_trigger_params=escalation_policy_trigger_params,
        )

        return new_live_call_router_data_attributes
