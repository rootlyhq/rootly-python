from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.update_alerts_source_data_attributes_sourceable_attributes_type_0_field_mappings_attributes_item_field import (
    UpdateAlertsSourceDataAttributesSourceableAttributesType0FieldMappingsAttributesItemField,
    check_update_alerts_source_data_attributes_sourceable_attributes_type_0_field_mappings_attributes_item_field,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAlertsSourceDataAttributesSourceableAttributesType0FieldMappingsAttributesItem")


@_attrs_define
class UpdateAlertsSourceDataAttributesSourceableAttributesType0FieldMappingsAttributesItem:
    """
    Attributes:
        field (UpdateAlertsSourceDataAttributesSourceableAttributesType0FieldMappingsAttributesItemField | Unset):
            Select the field on which the condition to be evaluated
        json_path (str | Unset): JSON path expression to extract a specific value from the alert's payload for
            evaluation. For `notification_target_id` only: if your account has opted in to Dynamic Notification Targets,
            this may also be a Liquid template that resolves to a notification target id at routing time.
    """

    field: UpdateAlertsSourceDataAttributesSourceableAttributesType0FieldMappingsAttributesItemField | Unset = UNSET
    json_path: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        field: str | Unset = UNSET
        if not isinstance(self.field, Unset):
            field = self.field

        json_path = self.json_path

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if json_path is not UNSET:
            field_dict["json_path"] = json_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _field = d.pop("field", UNSET)
        field: UpdateAlertsSourceDataAttributesSourceableAttributesType0FieldMappingsAttributesItemField | Unset
        if isinstance(_field, Unset):
            field = UNSET
        else:
            field = check_update_alerts_source_data_attributes_sourceable_attributes_type_0_field_mappings_attributes_item_field(
                _field
            )

        json_path = d.pop("json_path", UNSET)

        update_alerts_source_data_attributes_sourceable_attributes_type_0_field_mappings_attributes_item = cls(
            field=field,
            json_path=json_path,
        )

        return update_alerts_source_data_attributes_sourceable_attributes_type_0_field_mappings_attributes_item
