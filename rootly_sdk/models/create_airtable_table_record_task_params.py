from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_airtable_table_record_task_params_task_type import (
    CreateAirtableTableRecordTaskParamsTaskType,
    check_create_airtable_table_record_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_airtable_table_record_task_params_base import CreateAirtableTableRecordTaskParamsBase
    from ..models.create_airtable_table_record_task_params_table import CreateAirtableTableRecordTaskParamsTable


T = TypeVar("T", bound="CreateAirtableTableRecordTaskParams")


@_attrs_define
class CreateAirtableTableRecordTaskParams:
    """
    Attributes:
        base (CreateAirtableTableRecordTaskParamsBase):
        table (CreateAirtableTableRecordTaskParamsTable):
        task_type (Union[Unset, CreateAirtableTableRecordTaskParamsTaskType]):
        custom_fields_mapping (Union[None, Unset, str]): Custom field mappings. Can contain liquid markup and need to be
            valid JSON
    """

    base: "CreateAirtableTableRecordTaskParamsBase"
    table: "CreateAirtableTableRecordTaskParamsTable"
    task_type: Unset | CreateAirtableTableRecordTaskParamsTaskType = UNSET
    custom_fields_mapping: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base = self.base.to_dict()

        table = self.table.to_dict()

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
                "base": base,
                "table": table,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if custom_fields_mapping is not UNSET:
            field_dict["custom_fields_mapping"] = custom_fields_mapping

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_airtable_table_record_task_params_base import CreateAirtableTableRecordTaskParamsBase
        from ..models.create_airtable_table_record_task_params_table import CreateAirtableTableRecordTaskParamsTable

        d = dict(src_dict)
        base = CreateAirtableTableRecordTaskParamsBase.from_dict(d.pop("base"))

        table = CreateAirtableTableRecordTaskParamsTable.from_dict(d.pop("table"))

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | CreateAirtableTableRecordTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_airtable_table_record_task_params_task_type(_task_type)

        def _parse_custom_fields_mapping(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        custom_fields_mapping = _parse_custom_fields_mapping(d.pop("custom_fields_mapping", UNSET))

        create_airtable_table_record_task_params = cls(
            base=base,
            table=table,
            task_type=task_type,
            custom_fields_mapping=custom_fields_mapping,
        )

        create_airtable_table_record_task_params.additional_properties = d
        return create_airtable_table_record_task_params

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
