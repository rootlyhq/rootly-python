from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.new_live_call_router_data_attributes_country_code import NewLiveCallRouterDataAttributesCountryCode
from ..models.new_live_call_router_data_attributes_kind import NewLiveCallRouterDataAttributesKind
from ..models.new_live_call_router_data_attributes_phone_type import NewLiveCallRouterDataAttributesPhoneType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_live_call_router_data_attributes_escalation_policy_trigger_params import (
        NewLiveCallRouterDataAttributesEscalationPolicyTriggerParams,
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
        escalation_policy_trigger_params (NewLiveCallRouterDataAttributesEscalationPolicyTriggerParams):
        enabled (Union[Unset, bool]): Whether the live_call_router is enabled
        voicemail_greeting (Union[Unset, str]): The voicemail greeting of the live_call_router
        caller_greeting (Union[Unset, str]): The caller greeting message of the live_call_router
        waiting_music_url (Union[Unset, str]): The waiting music URL of the live_call_router
        sent_to_voicemail_delay (Union[Unset, int]): The delay (seconds) after which the caller in redirected to
            voicemail
        should_redirect_to_voicemail_on_no_answer (Union[Unset, bool]): This prompts the caller to choose voicemail or
            connect live
        escalation_level_delay_in_seconds (Union[Unset, int]): This overrides the delay (seconds) in escalation levels
        should_auto_resolve_alert_on_call_end (Union[Unset, bool]): This overrides the delay (seconds) in escalation
            levels
        alert_urgency_id (Union[Unset, str]): This is used in escalation paths to determine who to page
    """

    kind: NewLiveCallRouterDataAttributesKind
    name: str
    country_code: NewLiveCallRouterDataAttributesCountryCode
    phone_type: NewLiveCallRouterDataAttributesPhoneType
    phone_number: str
    escalation_policy_trigger_params: "NewLiveCallRouterDataAttributesEscalationPolicyTriggerParams"
    enabled: Union[Unset, bool] = UNSET
    voicemail_greeting: Union[Unset, str] = UNSET
    caller_greeting: Union[Unset, str] = UNSET
    waiting_music_url: Union[Unset, str] = UNSET
    sent_to_voicemail_delay: Union[Unset, int] = UNSET
    should_redirect_to_voicemail_on_no_answer: Union[Unset, bool] = UNSET
    escalation_level_delay_in_seconds: Union[Unset, int] = UNSET
    should_auto_resolve_alert_on_call_end: Union[Unset, bool] = UNSET
    alert_urgency_id: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        name = self.name

        country_code = self.country_code.value

        phone_type = self.phone_type.value

        phone_number = self.phone_number

        escalation_policy_trigger_params = self.escalation_policy_trigger_params.to_dict()

        enabled = self.enabled

        voicemail_greeting = self.voicemail_greeting

        caller_greeting = self.caller_greeting

        waiting_music_url = self.waiting_music_url

        sent_to_voicemail_delay = self.sent_to_voicemail_delay

        should_redirect_to_voicemail_on_no_answer = self.should_redirect_to_voicemail_on_no_answer

        escalation_level_delay_in_seconds = self.escalation_level_delay_in_seconds

        should_auto_resolve_alert_on_call_end = self.should_auto_resolve_alert_on_call_end

        alert_urgency_id = self.alert_urgency_id

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "kind": kind,
                "name": name,
                "country_code": country_code,
                "phone_type": phone_type,
                "phone_number": phone_number,
                "escalation_policy_trigger_params": escalation_policy_trigger_params,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if voicemail_greeting is not UNSET:
            field_dict["voicemail_greeting"] = voicemail_greeting
        if caller_greeting is not UNSET:
            field_dict["caller_greeting"] = caller_greeting
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
        if alert_urgency_id is not UNSET:
            field_dict["alert_urgency_id"] = alert_urgency_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.new_live_call_router_data_attributes_escalation_policy_trigger_params import (
            NewLiveCallRouterDataAttributesEscalationPolicyTriggerParams,
        )

        d = src_dict.copy()
        kind = NewLiveCallRouterDataAttributesKind(d.pop("kind"))

        name = d.pop("name")

        country_code = NewLiveCallRouterDataAttributesCountryCode(d.pop("country_code"))

        phone_type = NewLiveCallRouterDataAttributesPhoneType(d.pop("phone_type"))

        phone_number = d.pop("phone_number")

        escalation_policy_trigger_params = NewLiveCallRouterDataAttributesEscalationPolicyTriggerParams.from_dict(
            d.pop("escalation_policy_trigger_params")
        )

        enabled = d.pop("enabled", UNSET)

        voicemail_greeting = d.pop("voicemail_greeting", UNSET)

        caller_greeting = d.pop("caller_greeting", UNSET)

        waiting_music_url = d.pop("waiting_music_url", UNSET)

        sent_to_voicemail_delay = d.pop("sent_to_voicemail_delay", UNSET)

        should_redirect_to_voicemail_on_no_answer = d.pop("should_redirect_to_voicemail_on_no_answer", UNSET)

        escalation_level_delay_in_seconds = d.pop("escalation_level_delay_in_seconds", UNSET)

        should_auto_resolve_alert_on_call_end = d.pop("should_auto_resolve_alert_on_call_end", UNSET)

        alert_urgency_id = d.pop("alert_urgency_id", UNSET)

        new_live_call_router_data_attributes = cls(
            kind=kind,
            name=name,
            country_code=country_code,
            phone_type=phone_type,
            phone_number=phone_number,
            escalation_policy_trigger_params=escalation_policy_trigger_params,
            enabled=enabled,
            voicemail_greeting=voicemail_greeting,
            caller_greeting=caller_greeting,
            waiting_music_url=waiting_music_url,
            sent_to_voicemail_delay=sent_to_voicemail_delay,
            should_redirect_to_voicemail_on_no_answer=should_redirect_to_voicemail_on_no_answer,
            escalation_level_delay_in_seconds=escalation_level_delay_in_seconds,
            should_auto_resolve_alert_on_call_end=should_auto_resolve_alert_on_call_end,
            alert_urgency_id=alert_urgency_id,
        )

        return new_live_call_router_data_attributes
