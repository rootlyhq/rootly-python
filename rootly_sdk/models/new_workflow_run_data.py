from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_workflow_run_data_type import NewWorkflowRunDataType, check_new_workflow_run_data_type

if TYPE_CHECKING:
    from ..models.new_workflow_run_data_attributes_type_0 import NewWorkflowRunDataAttributesType0
    from ..models.new_workflow_run_data_attributes_type_1 import NewWorkflowRunDataAttributesType1
    from ..models.new_workflow_run_data_attributes_type_2 import NewWorkflowRunDataAttributesType2
    from ..models.new_workflow_run_data_attributes_type_3 import NewWorkflowRunDataAttributesType3
    from ..models.new_workflow_run_data_attributes_type_4 import NewWorkflowRunDataAttributesType4
    from ..models.new_workflow_run_data_attributes_type_5 import NewWorkflowRunDataAttributesType5


T = TypeVar("T", bound="NewWorkflowRunData")


@_attrs_define
class NewWorkflowRunData:
    """
    Attributes:
        type_ (NewWorkflowRunDataType):
        attributes (Union['NewWorkflowRunDataAttributesType0', 'NewWorkflowRunDataAttributesType1',
            'NewWorkflowRunDataAttributesType2', 'NewWorkflowRunDataAttributesType3', 'NewWorkflowRunDataAttributesType4',
            'NewWorkflowRunDataAttributesType5']):
    """

    type_: NewWorkflowRunDataType
    attributes: Union[
        "NewWorkflowRunDataAttributesType0",
        "NewWorkflowRunDataAttributesType1",
        "NewWorkflowRunDataAttributesType2",
        "NewWorkflowRunDataAttributesType3",
        "NewWorkflowRunDataAttributesType4",
        "NewWorkflowRunDataAttributesType5",
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.new_workflow_run_data_attributes_type_0 import NewWorkflowRunDataAttributesType0
        from ..models.new_workflow_run_data_attributes_type_1 import NewWorkflowRunDataAttributesType1
        from ..models.new_workflow_run_data_attributes_type_2 import NewWorkflowRunDataAttributesType2
        from ..models.new_workflow_run_data_attributes_type_3 import NewWorkflowRunDataAttributesType3
        from ..models.new_workflow_run_data_attributes_type_4 import NewWorkflowRunDataAttributesType4

        type_: str = self.type_

        attributes: dict[str, Any]
        if isinstance(self.attributes, NewWorkflowRunDataAttributesType0):
            attributes = self.attributes.to_dict()
        elif isinstance(self.attributes, NewWorkflowRunDataAttributesType1):
            attributes = self.attributes.to_dict()
        elif isinstance(self.attributes, NewWorkflowRunDataAttributesType2):
            attributes = self.attributes.to_dict()
        elif isinstance(self.attributes, NewWorkflowRunDataAttributesType3):
            attributes = self.attributes.to_dict()
        elif isinstance(self.attributes, NewWorkflowRunDataAttributesType4):
            attributes = self.attributes.to_dict()
        else:
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_workflow_run_data_attributes_type_0 import NewWorkflowRunDataAttributesType0
        from ..models.new_workflow_run_data_attributes_type_1 import NewWorkflowRunDataAttributesType1
        from ..models.new_workflow_run_data_attributes_type_2 import NewWorkflowRunDataAttributesType2
        from ..models.new_workflow_run_data_attributes_type_3 import NewWorkflowRunDataAttributesType3
        from ..models.new_workflow_run_data_attributes_type_4 import NewWorkflowRunDataAttributesType4
        from ..models.new_workflow_run_data_attributes_type_5 import NewWorkflowRunDataAttributesType5

        d = dict(src_dict)
        type_ = check_new_workflow_run_data_type(d.pop("type"))

        def _parse_attributes(
            data: object,
        ) -> Union[
            "NewWorkflowRunDataAttributesType0",
            "NewWorkflowRunDataAttributesType1",
            "NewWorkflowRunDataAttributesType2",
            "NewWorkflowRunDataAttributesType3",
            "NewWorkflowRunDataAttributesType4",
            "NewWorkflowRunDataAttributesType5",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_0 = NewWorkflowRunDataAttributesType0.from_dict(data)

                return attributes_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_1 = NewWorkflowRunDataAttributesType1.from_dict(data)

                return attributes_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_2 = NewWorkflowRunDataAttributesType2.from_dict(data)

                return attributes_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_3 = NewWorkflowRunDataAttributesType3.from_dict(data)

                return attributes_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_4 = NewWorkflowRunDataAttributesType4.from_dict(data)

                return attributes_type_4
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            attributes_type_5 = NewWorkflowRunDataAttributesType5.from_dict(data)

            return attributes_type_5

        attributes = _parse_attributes(d.pop("attributes"))

        new_workflow_run_data = cls(
            type_=type_,
            attributes=attributes,
        )

        new_workflow_run_data.additional_properties = d
        return new_workflow_run_data

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
