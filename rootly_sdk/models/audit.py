from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.audit_item_type import AuditItemType, check_audit_item_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_object_changes_type_0 import AuditObjectChangesType0
    from ..models.audit_object_type_0 import AuditObjectType0


T = TypeVar("T", bound="Audit")


@_attrs_define
class Audit:
    """
    Attributes:
        event (str): Describes the action that was taken.
        created_at (str): Date of creation
        item_type (AuditItemType | Unset): Describes the object in which the action was taken on
        object_ (AuditObjectType0 | None | Unset): The object in which the action was taken on
        object_changes (AuditObjectChangesType0 | None | Unset): The changes that occurred on the object
        user_id (int | None | Unset): The ID of who took action on the object. Together with whodunnit_type can be used
            to find the user
        item_id (None | str | Unset): ID of the affected object
        id (int | None | Unset): ID of audit
    """

    event: str
    created_at: str
    item_type: AuditItemType | Unset = UNSET
    object_: AuditObjectType0 | None | Unset = UNSET
    object_changes: AuditObjectChangesType0 | None | Unset = UNSET
    user_id: int | None | Unset = UNSET
    item_id: None | str | Unset = UNSET
    id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.audit_object_changes_type_0 import AuditObjectChangesType0
        from ..models.audit_object_type_0 import AuditObjectType0

        event = self.event

        created_at = self.created_at

        item_type: str | Unset = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type

        object_: dict[str, Any] | None | Unset
        if isinstance(self.object_, Unset):
            object_ = UNSET
        elif isinstance(self.object_, AuditObjectType0):
            object_ = self.object_.to_dict()
        else:
            object_ = self.object_

        object_changes: dict[str, Any] | None | Unset
        if isinstance(self.object_changes, Unset):
            object_changes = UNSET
        elif isinstance(self.object_changes, AuditObjectChangesType0):
            object_changes = self.object_changes.to_dict()
        else:
            object_changes = self.object_changes

        user_id: int | None | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        item_id: None | str | Unset
        if isinstance(self.item_id, Unset):
            item_id = UNSET
        else:
            item_id = self.item_id

        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event": event,
                "created_at": created_at,
            }
        )
        if item_type is not UNSET:
            field_dict["item_type"] = item_type
        if object_ is not UNSET:
            field_dict["object"] = object_
        if object_changes is not UNSET:
            field_dict["object_changes"] = object_changes
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if item_id is not UNSET:
            field_dict["item_id"] = item_id
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_object_changes_type_0 import AuditObjectChangesType0
        from ..models.audit_object_type_0 import AuditObjectType0

        d = dict(src_dict)
        event = d.pop("event")

        created_at = d.pop("created_at")

        _item_type = d.pop("item_type", UNSET)
        item_type: AuditItemType | Unset
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = check_audit_item_type(_item_type)

        def _parse_object_(data: object) -> AuditObjectType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                object_type_0 = AuditObjectType0.from_dict(data)

                return object_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AuditObjectType0 | None | Unset, data)

        object_ = _parse_object_(d.pop("object", UNSET))

        def _parse_object_changes(data: object) -> AuditObjectChangesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                object_changes_type_0 = AuditObjectChangesType0.from_dict(data)

                return object_changes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AuditObjectChangesType0 | None | Unset, data)

        object_changes = _parse_object_changes(d.pop("object_changes", UNSET))

        def _parse_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_item_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        item_id = _parse_item_id(d.pop("item_id", UNSET))

        def _parse_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        audit = cls(
            event=event,
            created_at=created_at,
            item_type=item_type,
            object_=object_,
            object_changes=object_changes,
            user_id=user_id,
            item_id=item_id,
            id=id,
        )

        audit.additional_properties = d
        return audit

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
