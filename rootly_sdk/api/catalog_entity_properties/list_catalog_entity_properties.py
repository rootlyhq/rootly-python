from http import HTTPStatus
from typing import Any
from urllib.parse import quote

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
    include: ListCatalogEntityPropertiesInclude | Unset = UNSET,
    sort: ListCatalogEntityPropertiesSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtercatalog_field_id: str | Unset = UNSET,
    filterkey: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_include: str | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    json_sort: str | Unset = UNSET
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
        "url": "/v1/catalog_entities/{catalog_entity_id}/properties".format(
            catalog_entity_id=quote(str(catalog_entity_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CatalogEntityPropertyList | None:
    if response.status_code == 200:
        response_200 = CatalogEntityPropertyList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
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
    include: ListCatalogEntityPropertiesInclude | Unset = UNSET,
    sort: ListCatalogEntityPropertiesSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtercatalog_field_id: str | Unset = UNSET,
    filterkey: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
) -> Response[CatalogEntityPropertyList]:
    """List catalog properties

     **Deprecated:** This endpoint is deprecated, please use `include=fields` on catalog entities or
    native catalog endpoints (teams, services, functionalities, incident_types, causes, environments) to
    retrieve field values instead.

    List Catalog Entity Properties.

    Args:
        catalog_entity_id (str):
        include (ListCatalogEntityPropertiesInclude | Unset):
        sort (ListCatalogEntityPropertiesSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtercatalog_field_id (str | Unset):
        filterkey (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):

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
    include: ListCatalogEntityPropertiesInclude | Unset = UNSET,
    sort: ListCatalogEntityPropertiesSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtercatalog_field_id: str | Unset = UNSET,
    filterkey: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
) -> CatalogEntityPropertyList | None:
    """List catalog properties

     **Deprecated:** This endpoint is deprecated, please use `include=fields` on catalog entities or
    native catalog endpoints (teams, services, functionalities, incident_types, causes, environments) to
    retrieve field values instead.

    List Catalog Entity Properties.

    Args:
        catalog_entity_id (str):
        include (ListCatalogEntityPropertiesInclude | Unset):
        sort (ListCatalogEntityPropertiesSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtercatalog_field_id (str | Unset):
        filterkey (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):

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
    include: ListCatalogEntityPropertiesInclude | Unset = UNSET,
    sort: ListCatalogEntityPropertiesSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtercatalog_field_id: str | Unset = UNSET,
    filterkey: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
) -> Response[CatalogEntityPropertyList]:
    """List catalog properties

     **Deprecated:** This endpoint is deprecated, please use `include=fields` on catalog entities or
    native catalog endpoints (teams, services, functionalities, incident_types, causes, environments) to
    retrieve field values instead.

    List Catalog Entity Properties.

    Args:
        catalog_entity_id (str):
        include (ListCatalogEntityPropertiesInclude | Unset):
        sort (ListCatalogEntityPropertiesSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtercatalog_field_id (str | Unset):
        filterkey (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):

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
    include: ListCatalogEntityPropertiesInclude | Unset = UNSET,
    sort: ListCatalogEntityPropertiesSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtercatalog_field_id: str | Unset = UNSET,
    filterkey: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
) -> CatalogEntityPropertyList | None:
    """List catalog properties

     **Deprecated:** This endpoint is deprecated, please use `include=fields` on catalog entities or
    native catalog endpoints (teams, services, functionalities, incident_types, causes, environments) to
    retrieve field values instead.

    List Catalog Entity Properties.

    Args:
        catalog_entity_id (str):
        include (ListCatalogEntityPropertiesInclude | Unset):
        sort (ListCatalogEntityPropertiesSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtercatalog_field_id (str | Unset):
        filterkey (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):

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
