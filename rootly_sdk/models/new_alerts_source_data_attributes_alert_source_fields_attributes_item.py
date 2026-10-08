from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewAlertsSourceDataAttributesAlertSourceFieldsAttributesItem")


@_attrs_define
class NewAlertsSourceDataAttributesAlertSourceFieldsAttributesItem:
    """
    Attributes:
        alert_field_id (str | Unset): The ID of the alert field
        template_body (None | str | Unset): Liquid expression to extract a specific value from the alert's payload for
            evaluation
    """

    alert_field_id: str | Unset = UNSET
    template_body: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        alert_field_id = self.alert_field_id

        template_body: None | str | Unset
        if isinstance(self.template_body, Unset):
            template_body = UNSET
        else:
            template_body = self.template_body

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if alert_field_id is not UNSET:
            field_dict["alert_field_id"] = alert_field_id
        if template_body is not UNSET:
            field_dict["template_body"] = template_body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        alert_field_id = d.pop("alert_field_id", UNSET)

        def _parse_template_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template_body = _parse_template_body(d.pop("template_body", UNSET))

        new_alerts_source_data_attributes_alert_source_fields_attributes_item = cls(
            alert_field_id=alert_field_id,
            template_body=template_body,
        )

        return new_alerts_source_data_attributes_alert_source_fields_attributes_item
