from __future__ import annotations

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
        name (str | Unset): Required for new records. Optional for updates.
        description (None | str | Unset):
        public_description (None | str | Unset):
        color (None | str | Unset):
        position (int | None | Unset):
        notify_emails (list[str] | None | Unset):
        fields (list[BulkUpsertEnvironmentsEntitiesItemFieldsItem] | Unset): Catalog property values (merge semantics:
            only mentioned fields written).
    """

    external_id: str
    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    public_description: None | str | Unset = UNSET
    color: None | str | Unset = UNSET
    position: int | None | Unset = UNSET
    notify_emails: list[str] | None | Unset = UNSET
    fields: list[BulkUpsertEnvironmentsEntitiesItemFieldsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        public_description: None | str | Unset
        if isinstance(self.public_description, Unset):
            public_description = UNSET
        else:
            public_description = self.public_description

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        position: int | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        notify_emails: list[str] | None | Unset
        if isinstance(self.notify_emails, Unset):
            notify_emails = UNSET
        elif isinstance(self.notify_emails, list):
            notify_emails = self.notify_emails

        else:
            notify_emails = self.notify_emails

        fields: list[dict[str, Any]] | Unset = UNSET
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

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_public_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_description = _parse_public_description(d.pop("public_description", UNSET))

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        def _parse_notify_emails(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                notify_emails_type_0 = cast(list[str], data)

                return notify_emails_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        notify_emails = _parse_notify_emails(d.pop("notify_emails", UNSET))

        _fields = d.pop("fields", UNSET)
        fields: list[BulkUpsertEnvironmentsEntitiesItemFieldsItem] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
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
