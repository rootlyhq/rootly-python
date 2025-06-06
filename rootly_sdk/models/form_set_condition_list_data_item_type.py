from enum import Enum


class FormSetConditionListDataItemType(str, Enum):
    FORM_SET_CONDITIONS = "form_set_conditions"

    def __str__(self) -> str:
        return str(self.value)
