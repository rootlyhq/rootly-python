from typing import Literal

RetrospectiveConfigurationKind = Literal["mandatory", "skip"]

RETROSPECTIVE_CONFIGURATION_KIND_VALUES: set[RetrospectiveConfigurationKind] = {
    "mandatory",
    "skip",
}


def check_retrospective_configuration_kind(value: str | None) -> RetrospectiveConfigurationKind | None:
    if value is None:
        return None
    if value in RETROSPECTIVE_CONFIGURATION_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RETROSPECTIVE_CONFIGURATION_KIND_VALUES!r}")
