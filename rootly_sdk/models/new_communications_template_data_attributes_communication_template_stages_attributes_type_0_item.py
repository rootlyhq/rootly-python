from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewCommunicationsTemplateDataAttributesCommunicationTemplateStagesAttributesType0Item")


@_attrs_define
class NewCommunicationsTemplateDataAttributesCommunicationTemplateStagesAttributesType0Item:
    """
    Attributes:
        communication_stage_id (str | Unset): The communication stage ID
        sms_content (None | str | Unset): SMS content for the stage
        email_subject (None | str | Unset): Email subject for the stage
        email_body (None | str | Unset): Email body for the stage
        slack_content (None | str | Unset): Slack content for the stage
    """

    communication_stage_id: str | Unset = UNSET
    sms_content: None | str | Unset = UNSET
    email_subject: None | str | Unset = UNSET
    email_body: None | str | Unset = UNSET
    slack_content: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        communication_stage_id = self.communication_stage_id

        sms_content: None | str | Unset
        if isinstance(self.sms_content, Unset):
            sms_content = UNSET
        else:
            sms_content = self.sms_content

        email_subject: None | str | Unset
        if isinstance(self.email_subject, Unset):
            email_subject = UNSET
        else:
            email_subject = self.email_subject

        email_body: None | str | Unset
        if isinstance(self.email_body, Unset):
            email_body = UNSET
        else:
            email_body = self.email_body

        slack_content: None | str | Unset
        if isinstance(self.slack_content, Unset):
            slack_content = UNSET
        else:
            slack_content = self.slack_content

        field_dict: dict[str, Any] = {}

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

        def _parse_sms_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sms_content = _parse_sms_content(d.pop("sms_content", UNSET))

        def _parse_email_subject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_subject = _parse_email_subject(d.pop("email_subject", UNSET))

        def _parse_email_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_body = _parse_email_body(d.pop("email_body", UNSET))

        def _parse_slack_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slack_content = _parse_slack_content(d.pop("slack_content", UNSET))

        new_communications_template_data_attributes_communication_template_stages_attributes_type_0_item = cls(
            communication_stage_id=communication_stage_id,
            sms_content=sms_content,
            email_subject=email_subject,
            email_body=email_body,
            slack_content=slack_content,
        )

        return new_communications_template_data_attributes_communication_template_stages_attributes_type_0_item
