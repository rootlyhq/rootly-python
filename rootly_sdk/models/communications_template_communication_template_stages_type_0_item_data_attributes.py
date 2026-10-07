from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.communications_template_communication_template_stages_type_0_item_data_attributes_communication_stage import (
        CommunicationsTemplateCommunicationTemplateStagesType0ItemDataAttributesCommunicationStage,
    )
    from ..models.communications_template_communication_template_stages_type_0_item_data_attributes_communication_template import (
        CommunicationsTemplateCommunicationTemplateStagesType0ItemDataAttributesCommunicationTemplate,
    )


T = TypeVar("T", bound="CommunicationsTemplateCommunicationTemplateStagesType0ItemDataAttributes")


@_attrs_define
class CommunicationsTemplateCommunicationTemplateStagesType0ItemDataAttributes:
    """
    Attributes:
        email_body (None | str | Unset): Email body for the stage
        email_subject (None | str | Unset): Email subject for the stage
        slack_content (None | str | Unset): Slack content for the stage
        sms_content (None | str | Unset): SMS content for the stage
        created_at (str | Unset): Date of creation
        updated_at (str | Unset): Date of last update
        communication_stage (CommunicationsTemplateCommunicationTemplateStagesType0ItemDataAttributesCommunicationStage
            | Unset):
        communication_template
            (CommunicationsTemplateCommunicationTemplateStagesType0ItemDataAttributesCommunicationTemplate | Unset):
    """

    email_body: None | str | Unset = UNSET
    email_subject: None | str | Unset = UNSET
    slack_content: None | str | Unset = UNSET
    sms_content: None | str | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    communication_stage: (
        CommunicationsTemplateCommunicationTemplateStagesType0ItemDataAttributesCommunicationStage | Unset
    ) = UNSET
    communication_template: (
        CommunicationsTemplateCommunicationTemplateStagesType0ItemDataAttributesCommunicationTemplate | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email_body: None | str | Unset
        if isinstance(self.email_body, Unset):
            email_body = UNSET
        else:
            email_body = self.email_body

        email_subject: None | str | Unset
        if isinstance(self.email_subject, Unset):
            email_subject = UNSET
        else:
            email_subject = self.email_subject

        slack_content: None | str | Unset
        if isinstance(self.slack_content, Unset):
            slack_content = UNSET
        else:
            slack_content = self.slack_content

        sms_content: None | str | Unset
        if isinstance(self.sms_content, Unset):
            sms_content = UNSET
        else:
            sms_content = self.sms_content

        created_at = self.created_at

        updated_at = self.updated_at

        communication_stage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.communication_stage, Unset):
            communication_stage = self.communication_stage.to_dict()

        communication_template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.communication_template, Unset):
            communication_template = self.communication_template.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email_body is not UNSET:
            field_dict["email_body"] = email_body
        if email_subject is not UNSET:
            field_dict["email_subject"] = email_subject
        if slack_content is not UNSET:
            field_dict["slack_content"] = slack_content
        if sms_content is not UNSET:
            field_dict["sms_content"] = sms_content
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if communication_stage is not UNSET:
            field_dict["communication_stage"] = communication_stage
        if communication_template is not UNSET:
            field_dict["communication_template"] = communication_template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.communications_template_communication_template_stages_type_0_item_data_attributes_communication_stage import (
            CommunicationsTemplateCommunicationTemplateStagesType0ItemDataAttributesCommunicationStage,
        )
        from ..models.communications_template_communication_template_stages_type_0_item_data_attributes_communication_template import (
            CommunicationsTemplateCommunicationTemplateStagesType0ItemDataAttributesCommunicationTemplate,
        )

        d = dict(src_dict)

        def _parse_email_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_body = _parse_email_body(d.pop("email_body", UNSET))

        def _parse_email_subject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_subject = _parse_email_subject(d.pop("email_subject", UNSET))

        def _parse_slack_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slack_content = _parse_slack_content(d.pop("slack_content", UNSET))

        def _parse_sms_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sms_content = _parse_sms_content(d.pop("sms_content", UNSET))

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _communication_stage = d.pop("communication_stage", UNSET)
        communication_stage: (
            CommunicationsTemplateCommunicationTemplateStagesType0ItemDataAttributesCommunicationStage | Unset
        )
        if isinstance(_communication_stage, Unset):
            communication_stage = UNSET
        else:
            communication_stage = (
                CommunicationsTemplateCommunicationTemplateStagesType0ItemDataAttributesCommunicationStage.from_dict(
                    _communication_stage
                )
            )

        _communication_template = d.pop("communication_template", UNSET)
        communication_template: (
            CommunicationsTemplateCommunicationTemplateStagesType0ItemDataAttributesCommunicationTemplate | Unset
        )
        if isinstance(_communication_template, Unset):
            communication_template = UNSET
        else:
            communication_template = (
                CommunicationsTemplateCommunicationTemplateStagesType0ItemDataAttributesCommunicationTemplate.from_dict(
                    _communication_template
                )
            )

        communications_template_communication_template_stages_type_0_item_data_attributes = cls(
            email_body=email_body,
            email_subject=email_subject,
            slack_content=slack_content,
            sms_content=sms_content,
            created_at=created_at,
            updated_at=updated_at,
            communication_stage=communication_stage,
            communication_template=communication_template,
        )

        communications_template_communication_template_stages_type_0_item_data_attributes.additional_properties = d
        return communications_template_communication_template_stages_type_0_item_data_attributes

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
