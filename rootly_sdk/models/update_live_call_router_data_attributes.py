from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.update_live_call_router_data_attributes_country_code import UpdateLiveCallRouterDataAttributesCountryCode
from ..models.update_live_call_router_data_attributes_kind import UpdateLiveCallRouterDataAttributesKind
from ..models.update_live_call_router_data_attributes_phone_type import UpdateLiveCallRouterDataAttributesPhoneType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_live_call_router_data_attributes_escalation_policy_trigger_params_type_0 import (
        UpdateLiveCallRouterDataAttributesEscalationPolicyTriggerParamsType0,
    )


T = TypeVar("T", bound="UpdateLiveCallRouterDataAttributes")


@_attrs_define
class UpdateLiveCallRouterDataAttributes:
    """
    Attributes:
        kind (Union[Unset, UpdateLiveCallRouterDataAttributesKind]): The kind of the live_call_router
        enabled (Union[Unset, bool]): Whether the live_call_router is enabled
        name (Union[Unset, str]): The name of the live_call_router
        country_code (Union[Unset, UpdateLiveCallRouterDataAttributesCountryCode]): The country code of the
            live_call_router
        phone_type (Union[Unset, UpdateLiveCallRouterDataAttributesPhoneType]): The phone type of the live_call_router
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
        escalation_policy_trigger_params (Union['UpdateLiveCallRouterDataAttributesEscalationPolicyTriggerParamsType0',
            None, Unset]):
    """

    kind: Union[Unset, UpdateLiveCallRouterDataAttributesKind] = UNSET
    enabled: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    country_code: Union[Unset, UpdateLiveCallRouterDataAttributesCountryCode] = UNSET
    phone_type: Union[Unset, UpdateLiveCallRouterDataAttributesPhoneType] = UNSET
    voicemail_greeting: Union[Unset, str] = UNSET
    caller_greeting: Union[Unset, str] = UNSET
    waiting_music_url: Union[Unset, str] = UNSET
    sent_to_voicemail_delay: Union[Unset, int] = UNSET
    should_redirect_to_voicemail_on_no_answer: Union[Unset, bool] = UNSET
    escalation_level_delay_in_seconds: Union[Unset, int] = UNSET
    should_auto_resolve_alert_on_call_end: Union[Unset, bool] = UNSET
    alert_urgency_id: Union[Unset, str] = UNSET
    escalation_policy_trigger_params: Union[
        "UpdateLiveCallRouterDataAttributesEscalationPolicyTriggerParamsType0", None, Unset
    ] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_live_call_router_data_attributes_escalation_policy_trigger_params_type_0 import (
            UpdateLiveCallRouterDataAttributesEscalationPolicyTriggerParamsType0,
        )

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        enabled = self.enabled

        name = self.name

        country_code: Union[Unset, str] = UNSET
        if not isinstance(self.country_code, Unset):
            country_code = self.country_code.value

        phone_type: Union[Unset, str] = UNSET
        if not isinstance(self.phone_type, Unset):
            phone_type = self.phone_type.value

        voicemail_greeting = self.voicemail_greeting

        caller_greeting = self.caller_greeting

        waiting_music_url = self.waiting_music_url

        sent_to_voicemail_delay = self.sent_to_voicemail_delay

        should_redirect_to_voicemail_on_no_answer = self.should_redirect_to_voicemail_on_no_answer

        escalation_level_delay_in_seconds = self.escalation_level_delay_in_seconds

        should_auto_resolve_alert_on_call_end = self.should_auto_resolve_alert_on_call_end

        alert_urgency_id = self.alert_urgency_id

        escalation_policy_trigger_params: Union[None, Unset, dict[str, Any]]
        if isinstance(self.escalation_policy_trigger_params, Unset):
            escalation_policy_trigger_params = UNSET
        elif isinstance(
            self.escalation_policy_trigger_params, UpdateLiveCallRouterDataAttributesEscalationPolicyTriggerParamsType0
        ):
            escalation_policy_trigger_params = self.escalation_policy_trigger_params.to_dict()
        else:
            escalation_policy_trigger_params = self.escalation_policy_trigger_params

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if name is not UNSET:
            field_dict["name"] = name
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if phone_type is not UNSET:
            field_dict["phone_type"] = phone_type
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
        if escalation_policy_trigger_params is not UNSET:
            field_dict["escalation_policy_trigger_params"] = escalation_policy_trigger_params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.update_live_call_router_data_attributes_escalation_policy_trigger_params_type_0 import (
            UpdateLiveCallRouterDataAttributesEscalationPolicyTriggerParamsType0,
        )

        d = src_dict.copy()
        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, UpdateLiveCallRouterDataAttributesKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = UpdateLiveCallRouterDataAttributesKind(_kind)

        enabled = d.pop("enabled", UNSET)

        name = d.pop("name", UNSET)

        _country_code = d.pop("country_code", UNSET)
        country_code: Union[Unset, UpdateLiveCallRouterDataAttributesCountryCode]
        if isinstance(_country_code, Unset):
            country_code = UNSET
        else:
            country_code = UpdateLiveCallRouterDataAttributesCountryCode(_country_code)

        _phone_type = d.pop("phone_type", UNSET)
        phone_type: Union[Unset, UpdateLiveCallRouterDataAttributesPhoneType]
        if isinstance(_phone_type, Unset):
            phone_type = UNSET
        else:
            phone_type = UpdateLiveCallRouterDataAttributesPhoneType(_phone_type)

        voicemail_greeting = d.pop("voicemail_greeting", UNSET)

        caller_greeting = d.pop("caller_greeting", UNSET)

        waiting_music_url = d.pop("waiting_music_url", UNSET)

        sent_to_voicemail_delay = d.pop("sent_to_voicemail_delay", UNSET)

        should_redirect_to_voicemail_on_no_answer = d.pop("should_redirect_to_voicemail_on_no_answer", UNSET)

        escalation_level_delay_in_seconds = d.pop("escalation_level_delay_in_seconds", UNSET)

        should_auto_resolve_alert_on_call_end = d.pop("should_auto_resolve_alert_on_call_end", UNSET)

        alert_urgency_id = d.pop("alert_urgency_id", UNSET)

        def _parse_escalation_policy_trigger_params(
            data: object,
        ) -> Union["UpdateLiveCallRouterDataAttributesEscalationPolicyTriggerParamsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                escalation_policy_trigger_params_type_0 = (
                    UpdateLiveCallRouterDataAttributesEscalationPolicyTriggerParamsType0.from_dict(data)
                )

                return escalation_policy_trigger_params_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["UpdateLiveCallRouterDataAttributesEscalationPolicyTriggerParamsType0", None, Unset], data
            )

        escalation_policy_trigger_params = _parse_escalation_policy_trigger_params(
            d.pop("escalation_policy_trigger_params", UNSET)
        )

        update_live_call_router_data_attributes = cls(
            kind=kind,
            enabled=enabled,
            name=name,
            country_code=country_code,
            phone_type=phone_type,
            voicemail_greeting=voicemail_greeting,
            caller_greeting=caller_greeting,
            waiting_music_url=waiting_music_url,
            sent_to_voicemail_delay=sent_to_voicemail_delay,
            should_redirect_to_voicemail_on_no_answer=should_redirect_to_voicemail_on_no_answer,
            escalation_level_delay_in_seconds=escalation_level_delay_in_seconds,
            should_auto_resolve_alert_on_call_end=should_auto_resolve_alert_on_call_end,
            alert_urgency_id=alert_urgency_id,
            escalation_policy_trigger_params=escalation_policy_trigger_params,
        )

        return update_live_call_router_data_attributes
