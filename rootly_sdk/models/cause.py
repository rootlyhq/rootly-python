from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cause_fields_item import CauseFieldsItem


T = TypeVar("T", bound="Cause")


@_attrs_define
class Cause:
    """
    Attributes:
        name (str): The name of the cause
        created_at (str): Date of creation
        updated_at (str): Date of last update
        slug (Union[Unset, str]): The slug of the cause
        description (Union[None, Unset, str]): The description of the cause
        position (Union[None, Unset, int]): Position of the cause
        fields (Union[Unset, list['CauseFieldsItem']]): Array of field values for this cause.
    """

    name: str
    created_at: str
    updated_at: str
    slug: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    position: Union[None, Unset, int] = UNSET
    fields: Union[Unset, list["CauseFieldsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        created_at = self.created_at

        updated_at = self.updated_at

        slug = self.slug

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        position: Union[None, Unset, int]
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if description is not UNSET:
            field_dict["description"] = description
        if position is not UNSET:
            field_dict["position"] = position
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cause_fields_item import CauseFieldsItem

        d = dict(src_dict)
        name = d.pop("name")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        slug = d.pop("slug", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_position(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        position = _parse_position(d.pop("position", UNSET))

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = CauseFieldsItem.from_dict(fields_item_data)

            fields.append(fields_item)

        cause = cls(
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            slug=slug,
            description=description,
            position=position,
            fields=fields,
        )

        cause.additional_properties = d
        return cause

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
