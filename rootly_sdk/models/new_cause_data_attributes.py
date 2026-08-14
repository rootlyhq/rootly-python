from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_cause_data_attributes_properties_item import NewCauseDataAttributesPropertiesItem


T = TypeVar("T", bound="NewCauseDataAttributes")


@_attrs_define
class NewCauseDataAttributes:
    """
    Attributes:
        name (str): The name of the cause
        slug (Union[None, Unset, str]): Deprecated. `slug` is derived from `name`; any submitted value is ignored. This
            property will be removed from the request schema in a future version.
        description (Union[None, Unset, str]): The description of the cause
        public_description (Union[None, Unset, str]): The status page description of the cause
        position (Union[None, Unset, int]): Position of the cause
        properties (Union[Unset, list['NewCauseDataAttributesPropertiesItem']]): Array of property values for this
            cause.
    """

    name: str
    slug: None | Unset | str = UNSET
    description: None | Unset | str = UNSET
    public_description: None | Unset | str = UNSET
    position: None | Unset | int = UNSET
    properties: Unset | list["NewCauseDataAttributesPropertiesItem"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug: None | Unset | str
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

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

        position: None | Unset | int
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        properties: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if description is not UNSET:
            field_dict["description"] = description
        if public_description is not UNSET:
            field_dict["public_description"] = public_description
        if position is not UNSET:
            field_dict["position"] = position
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_cause_data_attributes_properties_item import NewCauseDataAttributesPropertiesItem

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_slug(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        slug = _parse_slug(d.pop("slug", UNSET))

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

        def _parse_position(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        position = _parse_position(d.pop("position", UNSET))

        properties = []
        _properties = d.pop("properties", UNSET)
        for properties_item_data in _properties or []:
            properties_item = NewCauseDataAttributesPropertiesItem.from_dict(properties_item_data)

            properties.append(properties_item)

        new_cause_data_attributes = cls(
            name=name,
            slug=slug,
            description=description,
            public_description=public_description,
            position=position,
            properties=properties,
        )

        return new_cause_data_attributes
