from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.send_email_task_params_task_type import (
    SendEmailTaskParamsTaskType,
    check_send_email_task_params_task_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SendEmailTaskParams")


@_attrs_define
class SendEmailTaskParams:
    """
    Attributes:
        to (list[str]):
        subject (str): The subject
        body (None | str): The email body
        task_type (SendEmailTaskParamsTaskType | Unset):
        from_ (str | Unset): The from email address. Need to use SMTP integration if different than rootly.com Default:
            'Rootly <workflows@rootly.com>'.
        cc (list[str] | Unset):
        bcc (list[str] | Unset):
        preheader (None | str | Unset): The preheader
        include_header (bool | Unset):
        include_footer (bool | Unset):
        custom_logo_url (None | str | Unset): URL to your custom email logo
    """

    to: list[str]
    subject: str
    body: None | str
    task_type: SendEmailTaskParamsTaskType | Unset = UNSET
    from_: str | Unset = "Rootly <workflows@rootly.com>"
    cc: list[str] | Unset = UNSET
    bcc: list[str] | Unset = UNSET
    preheader: None | str | Unset = UNSET
    include_header: bool | Unset = UNSET
    include_footer: bool | Unset = UNSET
    custom_logo_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        to = self.to

        subject = self.subject

        body: None | str
        body = self.body

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        from_ = self.from_

        cc: list[str] | Unset = UNSET
        if not isinstance(self.cc, Unset):
            cc = self.cc

        bcc: list[str] | Unset = UNSET
        if not isinstance(self.bcc, Unset):
            bcc = self.bcc

        preheader: None | str | Unset
        if isinstance(self.preheader, Unset):
            preheader = UNSET
        else:
            preheader = self.preheader

        include_header = self.include_header

        include_footer = self.include_footer

        custom_logo_url: None | str | Unset
        if isinstance(self.custom_logo_url, Unset):
            custom_logo_url = UNSET
        else:
            custom_logo_url = self.custom_logo_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "to": to,
                "subject": subject,
                "body": body,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if from_ is not UNSET:
            field_dict["from"] = from_
        if cc is not UNSET:
            field_dict["cc"] = cc
        if bcc is not UNSET:
            field_dict["bcc"] = bcc
        if preheader is not UNSET:
            field_dict["preheader"] = preheader
        if include_header is not UNSET:
            field_dict["include_header"] = include_header
        if include_footer is not UNSET:
            field_dict["include_footer"] = include_footer
        if custom_logo_url is not UNSET:
            field_dict["custom_logo_url"] = custom_logo_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        to = cast(list[str], d.pop("to"))

        subject = d.pop("subject")

        def _parse_body(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        body = _parse_body(d.pop("body"))

        _task_type = d.pop("task_type", UNSET)
        task_type: SendEmailTaskParamsTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_send_email_task_params_task_type(_task_type)

        from_ = d.pop("from", UNSET)

        cc = cast(list[str], d.pop("cc", UNSET))

        bcc = cast(list[str], d.pop("bcc", UNSET))

        def _parse_preheader(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preheader = _parse_preheader(d.pop("preheader", UNSET))

        include_header = d.pop("include_header", UNSET)

        include_footer = d.pop("include_footer", UNSET)

        def _parse_custom_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_logo_url = _parse_custom_logo_url(d.pop("custom_logo_url", UNSET))

        send_email_task_params = cls(
            to=to,
            subject=subject,
            body=body,
            task_type=task_type,
            from_=from_,
            cc=cc,
            bcc=bcc,
            preheader=preheader,
            include_header=include_header,
            include_footer=include_footer,
            custom_logo_url=custom_logo_url,
        )

        send_email_task_params.additional_properties = d
        return send_email_task_params

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
