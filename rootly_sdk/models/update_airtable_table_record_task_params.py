from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_airtable_table_record_task_params_task_type import (
    UpdateAirtableTableRecordTaskParamsTaskType,
    check_update_airtable_table_record_task_params_task_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAirtableTableRecordTaskParams")


@_attrs_define
class UpdateAirtableTableRecordTaskParams:
    """
    Attributes:
        base_key (str): The base key
        table_name (str): The table name
        record_id (str): The record id
        task_type (Union[Unset, UpdateAirtableTableRecordTaskParamsTaskType]):
        custom_fields_mapping (Union[None, Unset, str]): Custom field mappings. Can contain liquid markup and need to be
            valid JSON
    """

    base_key: str
    table_name: str
    record_id: str
    task_type: Unset | UpdateAirtableTableRecordTaskParamsTaskType = UNSET
    custom_fields_mapping: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_key = self.base_key

        table_name = self.table_name

        record_id = self.record_id

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        custom_fields_mapping: None | Unset | str
        if isinstance(self.custom_fields_mapping, Unset):
            custom_fields_mapping = UNSET
        else:
            custom_fields_mapping = self.custom_fields_mapping

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "base_key": base_key,
                "table_name": table_name,
                "record_id": record_id,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if custom_fields_mapping is not UNSET:
            field_dict["custom_fields_mapping"] = custom_fields_mapping

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_key = d.pop("base_key")

        table_name = d.pop("table_name")

        record_id = d.pop("record_id")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | UpdateAirtableTableRecordTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_airtable_table_record_task_params_task_type(_task_type)

        def _parse_custom_fields_mapping(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        custom_fields_mapping = _parse_custom_fields_mapping(d.pop("custom_fields_mapping", UNSET))

        update_airtable_table_record_task_params = cls(
            base_key=base_key,
            table_name=table_name,
            record_id=record_id,
            task_type=task_type,
            custom_fields_mapping=custom_fields_mapping,
        )

        update_airtable_table_record_task_params.additional_properties = d
        return update_airtable_table_record_task_params

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
