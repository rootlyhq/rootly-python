from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.send_dashboard_report_task_params_task_type import (
    SendDashboardReportTaskParamsTaskType,
    check_send_dashboard_report_task_params_task_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SendDashboardReportTaskParams")


@_attrs_define
class SendDashboardReportTaskParams:
    """
    Attributes:
        dashboard_ids (list[str]):
        to (list[str]):
        subject (str): The subject
        body (Union[None, str]): The email body
        task_type (Union[Unset, SendDashboardReportTaskParamsTaskType]):
        from_ (Union[Unset, str]): The from email address. Need to use SMTP integration if different than rootly.com
            Default: 'Rootly <workflows@rootly.com>'.
        preheader (Union[None, Unset, str]): The preheader
    """

    dashboard_ids: list[str]
    to: list[str]
    subject: str
    body: None | str
    task_type: Unset | SendDashboardReportTaskParamsTaskType = UNSET
    from_: Unset | str = "Rootly <workflows@rootly.com>"
    preheader: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dashboard_ids = self.dashboard_ids

        to = self.to

        subject = self.subject

        body: None | str
        body = self.body

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        from_ = self.from_

        preheader: None | Unset | str
        if isinstance(self.preheader, Unset):
            preheader = UNSET
        else:
            preheader = self.preheader

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dashboard_ids": dashboard_ids,
                "to": to,
                "subject": subject,
                "body": body,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if from_ is not UNSET:
            field_dict["from"] = from_
        if preheader is not UNSET:
            field_dict["preheader"] = preheader

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dashboard_ids = cast(list[str], d.pop("dashboard_ids"))

        to = cast(list[str], d.pop("to"))

        subject = d.pop("subject")

        def _parse_body(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        body = _parse_body(d.pop("body"))

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | SendDashboardReportTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_send_dashboard_report_task_params_task_type(_task_type)

        from_ = d.pop("from", UNSET)

        def _parse_preheader(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        preheader = _parse_preheader(d.pop("preheader", UNSET))

        send_dashboard_report_task_params = cls(
            dashboard_ids=dashboard_ids,
            to=to,
            subject=subject,
            body=body,
            task_type=task_type,
            from_=from_,
            preheader=preheader,
        )

        send_dashboard_report_task_params.additional_properties = d
        return send_dashboard_report_task_params

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
