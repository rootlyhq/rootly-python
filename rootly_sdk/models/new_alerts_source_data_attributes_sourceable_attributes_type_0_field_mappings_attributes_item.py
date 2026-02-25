from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_alerts_source_data_attributes_sourceable_attributes_type_0_field_mappings_attributes_item_field import (
    NewAlertsSourceDataAttributesSourceableAttributesType0FieldMappingsAttributesItemField,
    check_new_alerts_source_data_attributes_sourceable_attributes_type_0_field_mappings_attributes_item_field,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewAlertsSourceDataAttributesSourceableAttributesType0FieldMappingsAttributesItem")


@_attrs_define
class NewAlertsSourceDataAttributesSourceableAttributesType0FieldMappingsAttributesItem:
    """
    Attributes:
        field (Union[Unset, NewAlertsSourceDataAttributesSourceableAttributesType0FieldMappingsAttributesItemField]):
            Select the field on which the condition to be evaluated
        json_path (Union[Unset, str]): JSON path expression to extract a specific value from the alert's payload for
            evaluation
    """

    field: Unset | NewAlertsSourceDataAttributesSourceableAttributesType0FieldMappingsAttributesItemField = UNSET
    json_path: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field: Unset | str = UNSET
        if not isinstance(self.field, Unset):
            field = self.field

        json_path = self.json_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        field: Unset | NewAlertsSourceDataAttributesSourceableAttributesType0FieldMappingsAttributesItemField
        if isinstance(_field, Unset):
            field = UNSET
        else:
            field = check_new_alerts_source_data_attributes_sourceable_attributes_type_0_field_mappings_attributes_item_field(
                _field
            )

        json_path = d.pop("json_path", UNSET)

        new_alerts_source_data_attributes_sourceable_attributes_type_0_field_mappings_attributes_item = cls(
            field=field,
            json_path=json_path,
        )

        new_alerts_source_data_attributes_sourceable_attributes_type_0_field_mappings_attributes_item.additional_properties = d
        return new_alerts_source_data_attributes_sourceable_attributes_type_0_field_mappings_attributes_item

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
