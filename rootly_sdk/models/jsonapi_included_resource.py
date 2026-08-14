from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.jsonapi_included_resource_attributes import JsonapiIncludedResourceAttributes
    from ..models.jsonapi_included_resource_relationships import JsonapiIncludedResourceRelationships


T = TypeVar("T", bound="JsonapiIncludedResource")


@_attrs_define
class JsonapiIncludedResource:
    """
    Attributes:
        id (str):
        type_ (str):
        attributes (Union[Unset, JsonapiIncludedResourceAttributes]):
        relationships (Union[Unset, JsonapiIncludedResourceRelationships]):
    """

    id: str
    type_: str
    attributes: Union[Unset, "JsonapiIncludedResourceAttributes"] = UNSET
    relationships: Union[Unset, "JsonapiIncludedResourceRelationships"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        relationships: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jsonapi_included_resource_attributes import JsonapiIncludedResourceAttributes
        from ..models.jsonapi_included_resource_relationships import JsonapiIncludedResourceRelationships

        d = dict(src_dict)
        id = d.pop("id")

        type_ = d.pop("type")

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, JsonapiIncludedResourceAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = JsonapiIncludedResourceAttributes.from_dict(_attributes)

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, JsonapiIncludedResourceRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = JsonapiIncludedResourceRelationships.from_dict(_relationships)

        jsonapi_included_resource = cls(
            id=id,
            type_=type_,
            attributes=attributes,
            relationships=relationships,
        )

        jsonapi_included_resource.additional_properties = d
        return jsonapi_included_resource

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
