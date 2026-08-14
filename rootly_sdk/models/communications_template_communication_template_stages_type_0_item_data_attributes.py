from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

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
        email_body (Union[None, Unset, str]): Email body for the stage
        email_subject (Union[None, Unset, str]): Email subject for the stage
        slack_content (Union[None, Unset, str]): Slack content for the stage
        sms_content (Union[None, Unset, str]): SMS content for the stage
        created_at (Union[Unset, str]): Date of creation
        updated_at (Union[Unset, str]): Date of last update
        communication_stage (Union[Unset,
            CommunicationsTemplateCommunicationTemplateStagesType0ItemDataAttributesCommunicationStage]):
        communication_template (Union[Unset,
            CommunicationsTemplateCommunicationTemplateStagesType0ItemDataAttributesCommunicationTemplate]):
    """

    email_body: Union[None, Unset, str] = UNSET
    email_subject: Union[None, Unset, str] = UNSET
    slack_content: Union[None, Unset, str] = UNSET
    sms_content: Union[None, Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    communication_stage: Union[
        Unset, "CommunicationsTemplateCommunicationTemplateStagesType0ItemDataAttributesCommunicationStage"
    ] = UNSET
    communication_template: Union[
        Unset, "CommunicationsTemplateCommunicationTemplateStagesType0ItemDataAttributesCommunicationTemplate"
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email_body: Union[None, Unset, str]
        if isinstance(self.email_body, Unset):
            email_body = UNSET
        else:
            email_body = self.email_body

        email_subject: Union[None, Unset, str]
        if isinstance(self.email_subject, Unset):
            email_subject = UNSET
        else:
            email_subject = self.email_subject

        slack_content: Union[None, Unset, str]
        if isinstance(self.slack_content, Unset):
            slack_content = UNSET
        else:
            slack_content = self.slack_content

        sms_content: Union[None, Unset, str]
        if isinstance(self.sms_content, Unset):
            sms_content = UNSET
        else:
            sms_content = self.sms_content

        created_at = self.created_at

        updated_at = self.updated_at

        communication_stage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.communication_stage, Unset):
            communication_stage = self.communication_stage.to_dict()

        communication_template: Union[Unset, dict[str, Any]] = UNSET
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

        def _parse_email_body(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email_body = _parse_email_body(d.pop("email_body", UNSET))

        def _parse_email_subject(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email_subject = _parse_email_subject(d.pop("email_subject", UNSET))

        def _parse_slack_content(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        slack_content = _parse_slack_content(d.pop("slack_content", UNSET))

        def _parse_sms_content(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sms_content = _parse_sms_content(d.pop("sms_content", UNSET))

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _communication_stage = d.pop("communication_stage", UNSET)
        communication_stage: Union[
            Unset, CommunicationsTemplateCommunicationTemplateStagesType0ItemDataAttributesCommunicationStage
        ]
        if isinstance(_communication_stage, Unset):
            communication_stage = UNSET
        else:
            communication_stage = (
                CommunicationsTemplateCommunicationTemplateStagesType0ItemDataAttributesCommunicationStage.from_dict(
                    _communication_stage
                )
            )

        _communication_template = d.pop("communication_template", UNSET)
        communication_template: Union[
            Unset, CommunicationsTemplateCommunicationTemplateStagesType0ItemDataAttributesCommunicationTemplate
        ]
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
