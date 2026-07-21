from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_property_list import CatalogPropertyList
from ...models.list_incident_type_catalog_properties_include import (
    ListIncidentTypeCatalogPropertiesInclude,
)
from ...models.list_incident_type_catalog_properties_sort import (
    ListIncidentTypeCatalogPropertiesSort,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: ListIncidentTypeCatalogPropertiesInclude | Unset = UNSET,
    sort: ListIncidentTypeCatalogPropertiesSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterslug: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterkind: str | Unset = UNSET,
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

    params["filter[slug]"] = filterslug

    params["filter[name]"] = filtername

    params["filter[kind]"] = filterkind

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/incident_types/properties",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CatalogPropertyList | None:
    if response.status_code == 200:
        response_200 = CatalogPropertyList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CatalogPropertyList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include: ListIncidentTypeCatalogPropertiesInclude | Unset = UNSET,
    sort: ListIncidentTypeCatalogPropertiesSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterslug: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
) -> Response[CatalogPropertyList]:
    """List Catalog Properties

     List IncidentType Catalog Properties

    Args:
        include (ListIncidentTypeCatalogPropertiesInclude | Unset):
        sort (ListIncidentTypeCatalogPropertiesSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterslug (str | Unset):
        filtername (str | Unset):
        filterkind (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogPropertyList]
    """

    kwargs = _get_kwargs(
        include=include,
        sort=sort,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterslug=filterslug,
        filtername=filtername,
        filterkind=filterkind,
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
    *,
    client: AuthenticatedClient,
    include: ListIncidentTypeCatalogPropertiesInclude | Unset = UNSET,
    sort: ListIncidentTypeCatalogPropertiesSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterslug: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
) -> CatalogPropertyList | None:
    """List Catalog Properties

     List IncidentType Catalog Properties

    Args:
        include (ListIncidentTypeCatalogPropertiesInclude | Unset):
        sort (ListIncidentTypeCatalogPropertiesSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterslug (str | Unset):
        filtername (str | Unset):
        filterkind (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogPropertyList
    """

    return sync_detailed(
        client=client,
        include=include,
        sort=sort,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterslug=filterslug,
        filtername=filtername,
        filterkind=filterkind,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: ListIncidentTypeCatalogPropertiesInclude | Unset = UNSET,
    sort: ListIncidentTypeCatalogPropertiesSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterslug: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
) -> Response[CatalogPropertyList]:
    """List Catalog Properties

     List IncidentType Catalog Properties

    Args:
        include (ListIncidentTypeCatalogPropertiesInclude | Unset):
        sort (ListIncidentTypeCatalogPropertiesSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterslug (str | Unset):
        filtername (str | Unset):
        filterkind (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogPropertyList]
    """

    kwargs = _get_kwargs(
        include=include,
        sort=sort,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterslug=filterslug,
        filtername=filtername,
        filterkind=filterkind,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include: ListIncidentTypeCatalogPropertiesInclude | Unset = UNSET,
    sort: ListIncidentTypeCatalogPropertiesSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterslug: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
) -> CatalogPropertyList | None:
    """List Catalog Properties

     List IncidentType Catalog Properties

    Args:
        include (ListIncidentTypeCatalogPropertiesInclude | Unset):
        sort (ListIncidentTypeCatalogPropertiesSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterslug (str | Unset):
        filtername (str | Unset):
        filterkind (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogPropertyList
    """

    return (
        await asyncio_detailed(
            client=client,
            include=include,
            sort=sort,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filterslug=filterslug,
            filtername=filtername,
            filterkind=filterkind,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
        )
    ).parsed
