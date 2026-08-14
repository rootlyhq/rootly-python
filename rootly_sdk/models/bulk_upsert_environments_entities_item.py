from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_upsert_environments_entities_item_fields_item import BulkUpsertEnvironmentsEntitiesItemFieldsItem


T = TypeVar("T", bound="BulkUpsertEnvironmentsEntitiesItem")


@_attrs_define
class BulkUpsertEnvironmentsEntitiesItem:
    """
    Attributes:
        external_id (str): External identifier used as the upsert key. Unique per team.
        name (Union[Unset, str]): Required for new records. Optional for updates.
        description (Union[None, Unset, str]):
        public_description (Union[None, Unset, str]):
        color (Union[None, Unset, str]):
        position (Union[None, Unset, int]):
        notify_emails (Union[None, Unset, list[str]]):
        fields (Union[Unset, list['BulkUpsertEnvironmentsEntitiesItemFieldsItem']]): Catalog property values (merge
            semantics: only mentioned fields written).
    """

    external_id: str
    name: Unset | str = UNSET
    description: None | Unset | str = UNSET
    public_description: None | Unset | str = UNSET
    color: None | Unset | str = UNSET
    position: None | Unset | int = UNSET
    notify_emails: None | Unset | list[str] = UNSET
    fields: Unset | list["BulkUpsertEnvironmentsEntitiesItemFieldsItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        name = self.name

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        public_description: None | Unset | str
        if isinstance(self.public_description, Unset):
            public_description = UNSET
        else:
            public_description = self.public_description

        color: None | Unset | str
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        position: None | Unset | int
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        notify_emails: None | Unset | list[str]
        if isinstance(self.notify_emails, Unset):
            notify_emails = UNSET
        elif isinstance(self.notify_emails, list):
            notify_emails = self.notify_emails

        else:
            notify_emails = self.notify_emails

        fields: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_id": external_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if public_description is not UNSET:
            field_dict["public_description"] = public_description
        if color is not UNSET:
            field_dict["color"] = color
        if position is not UNSET:
            field_dict["position"] = position
        if notify_emails is not UNSET:
            field_dict["notify_emails"] = notify_emails
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_upsert_environments_entities_item_fields_item import (
            BulkUpsertEnvironmentsEntitiesItemFieldsItem,
        )

        d = dict(src_dict)
        external_id = d.pop("external_id")

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_public_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        public_description = _parse_public_description(d.pop("public_description", UNSET))

        def _parse_color(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_position(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        position = _parse_position(d.pop("position", UNSET))

        def _parse_notify_emails(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                notify_emails_type_0 = cast(list[str], data)

                return notify_emails_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        notify_emails = _parse_notify_emails(d.pop("notify_emails", UNSET))

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = BulkUpsertEnvironmentsEntitiesItemFieldsItem.from_dict(fields_item_data)

            fields.append(fields_item)

        bulk_upsert_environments_entities_item = cls(
            external_id=external_id,
            name=name,
            description=description,
            public_description=public_description,
            color=color,
            position=position,
            notify_emails=notify_emails,
            fields=fields,
        )

        bulk_upsert_environments_entities_item.additional_properties = d
        return bulk_upsert_environments_entities_item

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
