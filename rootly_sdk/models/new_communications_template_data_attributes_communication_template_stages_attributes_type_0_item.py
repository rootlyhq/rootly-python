from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewCommunicationsTemplateDataAttributesCommunicationTemplateStagesAttributesType0Item")


@_attrs_define
class NewCommunicationsTemplateDataAttributesCommunicationTemplateStagesAttributesType0Item:
    """
    Attributes:
        communication_stage_id (Union[Unset, str]): The communication stage ID
        sms_content (Union[None, Unset, str]): SMS content for the stage
        email_subject (Union[None, Unset, str]): Email subject for the stage
        email_body (Union[None, Unset, str]): Email body for the stage
        slack_content (Union[None, Unset, str]): Slack content for the stage
    """

    communication_stage_id: Unset | str = UNSET
    sms_content: None | Unset | str = UNSET
    email_subject: None | Unset | str = UNSET
    email_body: None | Unset | str = UNSET
    slack_content: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        communication_stage_id = self.communication_stage_id

        sms_content: None | Unset | str
        if isinstance(self.sms_content, Unset):
            sms_content = UNSET
        else:
            sms_content = self.sms_content

        email_subject: None | Unset | str
        if isinstance(self.email_subject, Unset):
            email_subject = UNSET
        else:
            email_subject = self.email_subject

        email_body: None | Unset | str
        if isinstance(self.email_body, Unset):
            email_body = UNSET
        else:
            email_body = self.email_body

        slack_content: None | Unset | str
        if isinstance(self.slack_content, Unset):
            slack_content = UNSET
        else:
            slack_content = self.slack_content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if communication_stage_id is not UNSET:
            field_dict["communication_stage_id"] = communication_stage_id
        if sms_content is not UNSET:
            field_dict["sms_content"] = sms_content
        if email_subject is not UNSET:
            field_dict["email_subject"] = email_subject
        if email_body is not UNSET:
            field_dict["email_body"] = email_body
        if slack_content is not UNSET:
            field_dict["slack_content"] = slack_content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        communication_stage_id = d.pop("communication_stage_id", UNSET)

        def _parse_sms_content(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        sms_content = _parse_sms_content(d.pop("sms_content", UNSET))

        def _parse_email_subject(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        email_subject = _parse_email_subject(d.pop("email_subject", UNSET))

        def _parse_email_body(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        email_body = _parse_email_body(d.pop("email_body", UNSET))

        def _parse_slack_content(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        slack_content = _parse_slack_content(d.pop("slack_content", UNSET))

        new_communications_template_data_attributes_communication_template_stages_attributes_type_0_item = cls(
            communication_stage_id=communication_stage_id,
            sms_content=sms_content,
            email_subject=email_subject,
            email_body=email_body,
            slack_content=slack_content,
        )

        new_communications_template_data_attributes_communication_template_stages_attributes_type_0_item.additional_properties = d
        return new_communications_template_data_attributes_communication_template_stages_attributes_type_0_item

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
