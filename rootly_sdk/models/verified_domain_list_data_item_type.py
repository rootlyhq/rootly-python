from typing import Literal, cast

VerifiedDomainListDataItemType = Literal["verified_domains"]

VERIFIED_DOMAIN_LIST_DATA_ITEM_TYPE_VALUES: set[VerifiedDomainListDataItemType] = {
    "verified_domains",
}


def check_verified_domain_list_data_item_type(value: str | None) -> VerifiedDomainListDataItemType | None:
    if value is None:
        return None
    if value in VERIFIED_DOMAIN_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(VerifiedDomainListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VERIFIED_DOMAIN_LIST_DATA_ITEM_TYPE_VALUES!r}")
