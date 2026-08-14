from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_entity_property_list import CatalogEntityPropertyList
from ...models.list_catalog_entity_properties_include import (
    ListCatalogEntityPropertiesInclude,
)
from ...models.list_catalog_entity_properties_sort import (
    ListCatalogEntityPropertiesSort,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    catalog_entity_id: str,
    *,
    include: Union[Unset, ListCatalogEntityPropertiesInclude] = UNSET,
    sort: Union[Unset, ListCatalogEntityPropertiesSort] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtercatalog_field_id: Union[Unset, str] = UNSET,
    filterkey: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_include: Union[Unset, str] = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[catalog_field_id]"] = filtercatalog_field_id

    params["filter[key]"] = filterkey

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/catalog_entities/{catalog_entity_id}/properties",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CatalogEntityPropertyList]:
    if response.status_code == 200:
        response_200 = CatalogEntityPropertyList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CatalogEntityPropertyList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    catalog_entity_id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, ListCatalogEntityPropertiesInclude] = UNSET,
    sort: Union[Unset, ListCatalogEntityPropertiesSort] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtercatalog_field_id: Union[Unset, str] = UNSET,
    filterkey: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
) -> Response[CatalogEntityPropertyList]:
    """List catalog properties

     **Deprecated:** This endpoint is deprecated, please use `include=fields` on catalog entities or
    native catalog endpoints (teams, services, functionalities, incident_types, causes, environments) to
    retrieve field values instead.

    List Catalog Entity Properties.

    Args:
        catalog_entity_id (str):
        include (Union[Unset, ListCatalogEntityPropertiesInclude]):
        sort (Union[Unset, ListCatalogEntityPropertiesSort]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtercatalog_field_id (Union[Unset, str]):
        filterkey (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogEntityPropertyList]
    """

    kwargs = _get_kwargs(
        catalog_entity_id=catalog_entity_id,
        include=include,
        sort=sort,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtercatalog_field_id=filtercatalog_field_id,
        filterkey=filterkey,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    catalog_entity_id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, ListCatalogEntityPropertiesInclude] = UNSET,
    sort: Union[Unset, ListCatalogEntityPropertiesSort] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtercatalog_field_id: Union[Unset, str] = UNSET,
    filterkey: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
) -> Optional[CatalogEntityPropertyList]:
    """List catalog properties

     **Deprecated:** This endpoint is deprecated, please use `include=fields` on catalog entities or
    native catalog endpoints (teams, services, functionalities, incident_types, causes, environments) to
    retrieve field values instead.

    List Catalog Entity Properties.

    Args:
        catalog_entity_id (str):
        include (Union[Unset, ListCatalogEntityPropertiesInclude]):
        sort (Union[Unset, ListCatalogEntityPropertiesSort]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtercatalog_field_id (Union[Unset, str]):
        filterkey (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogEntityPropertyList
    """

    return sync_detailed(
        catalog_entity_id=catalog_entity_id,
        client=client,
        include=include,
        sort=sort,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtercatalog_field_id=filtercatalog_field_id,
        filterkey=filterkey,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
    ).parsed


async def asyncio_detailed(
    catalog_entity_id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, ListCatalogEntityPropertiesInclude] = UNSET,
    sort: Union[Unset, ListCatalogEntityPropertiesSort] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtercatalog_field_id: Union[Unset, str] = UNSET,
    filterkey: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
) -> Response[CatalogEntityPropertyList]:
    """List catalog properties

     **Deprecated:** This endpoint is deprecated, please use `include=fields` on catalog entities or
    native catalog endpoints (teams, services, functionalities, incident_types, causes, environments) to
    retrieve field values instead.

    List Catalog Entity Properties.

    Args:
        catalog_entity_id (str):
        include (Union[Unset, ListCatalogEntityPropertiesInclude]):
        sort (Union[Unset, ListCatalogEntityPropertiesSort]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtercatalog_field_id (Union[Unset, str]):
        filterkey (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogEntityPropertyList]
    """

    kwargs = _get_kwargs(
        catalog_entity_id=catalog_entity_id,
        include=include,
        sort=sort,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtercatalog_field_id=filtercatalog_field_id,
        filterkey=filterkey,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    catalog_entity_id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, ListCatalogEntityPropertiesInclude] = UNSET,
    sort: Union[Unset, ListCatalogEntityPropertiesSort] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtercatalog_field_id: Union[Unset, str] = UNSET,
    filterkey: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
) -> Optional[CatalogEntityPropertyList]:
    """List catalog properties

     **Deprecated:** This endpoint is deprecated, please use `include=fields` on catalog entities or
    native catalog endpoints (teams, services, functionalities, incident_types, causes, environments) to
    retrieve field values instead.

    List Catalog Entity Properties.

    Args:
        catalog_entity_id (str):
        include (Union[Unset, ListCatalogEntityPropertiesInclude]):
        sort (Union[Unset, ListCatalogEntityPropertiesSort]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtercatalog_field_id (Union[Unset, str]):
        filterkey (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogEntityPropertyList
    """

    return (
        await asyncio_detailed(
            catalog_entity_id=catalog_entity_id,
            client=client,
            include=include,
            sort=sort,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filtercatalog_field_id=filtercatalog_field_id,
            filterkey=filterkey,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
        )
    ).parsed
