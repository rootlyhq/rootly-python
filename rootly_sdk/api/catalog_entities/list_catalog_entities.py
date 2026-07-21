from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.catalog_entity_list import CatalogEntityList
from ...models.list_catalog_entities_include import check_list_catalog_entities_include
from ...models.list_catalog_entities_include import ListCatalogEntitiesInclude
from ...models.list_catalog_entities_sort import check_list_catalog_entities_sort
from ...models.list_catalog_entities_sort import ListCatalogEntitiesSort
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    catalog_id: str,
    *,
    include: ListCatalogEntitiesInclude | Unset = UNSET,
    sort: ListCatalogEntitiesSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterslug: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterbackstage_id: str | Unset = UNSET,
    filterexternal_id: str | Unset = UNSET,
    filtermanaged_by: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterslugeq: str | Unset = UNSET,
    filterslugnot_eq: str | Unset = UNSET,
    filterslugin: str | Unset = UNSET,
    filterslugnot_in: str | Unset = UNSET,
    filternameeq: str | Unset = UNSET,
    filternamenot_eq: str | Unset = UNSET,
    filternamein: str | Unset = UNSET,
    filternamenot_in: str | Unset = UNSET,
    filtermanaged_byeq: str | Unset = UNSET,
    filtermanaged_bynot_eq: str | Unset = UNSET,
    filtermanaged_byin: str | Unset = UNSET,
    filtermanaged_bynot_in: str | Unset = UNSET,

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

    params["filter[search]"] = filtersearch

    params["filter[slug]"] = filterslug

    params["filter[name]"] = filtername

    params["filter[backstage_id]"] = filterbackstage_id

    params["filter[external_id]"] = filterexternal_id

    params["filter[managed_by]"] = filtermanaged_by

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params["filter[slug][eq]"] = filterslugeq

    params["filter[slug][not_eq]"] = filterslugnot_eq

    params["filter[slug][in]"] = filterslugin

    params["filter[slug][not_in]"] = filterslugnot_in

    params["filter[name][eq]"] = filternameeq

    params["filter[name][not_eq]"] = filternamenot_eq

    params["filter[name][in]"] = filternamein

    params["filter[name][not_in]"] = filternamenot_in

    params["filter[managed_by][eq]"] = filtermanaged_byeq

    params["filter[managed_by][not_eq]"] = filtermanaged_bynot_eq

    params["filter[managed_by][in]"] = filtermanaged_byin

    params["filter[managed_by][not_in]"] = filtermanaged_bynot_in


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/catalogs/{catalog_id}/entities".format(catalog_id=quote(str(catalog_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CatalogEntityList | None:
    if response.status_code == 200:
        response_200 = CatalogEntityList.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CatalogEntityList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    catalog_id: str,
    *,
    client: AuthenticatedClient,
    include: ListCatalogEntitiesInclude | Unset = UNSET,
    sort: ListCatalogEntitiesSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterslug: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterbackstage_id: str | Unset = UNSET,
    filterexternal_id: str | Unset = UNSET,
    filtermanaged_by: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterslugeq: str | Unset = UNSET,
    filterslugnot_eq: str | Unset = UNSET,
    filterslugin: str | Unset = UNSET,
    filterslugnot_in: str | Unset = UNSET,
    filternameeq: str | Unset = UNSET,
    filternamenot_eq: str | Unset = UNSET,
    filternamein: str | Unset = UNSET,
    filternamenot_in: str | Unset = UNSET,
    filtermanaged_byeq: str | Unset = UNSET,
    filtermanaged_bynot_eq: str | Unset = UNSET,
    filtermanaged_byin: str | Unset = UNSET,
    filtermanaged_bynot_in: str | Unset = UNSET,

) -> Response[CatalogEntityList]:
    """ List Catalog Entities

     List Catalog Entities

    Args:
        catalog_id (str):
        include (ListCatalogEntitiesInclude | Unset):
        sort (ListCatalogEntitiesSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filterslug (str | Unset):
        filtername (str | Unset):
        filterbackstage_id (str | Unset):
        filterexternal_id (str | Unset):
        filtermanaged_by (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterslugeq (str | Unset):
        filterslugnot_eq (str | Unset):
        filterslugin (str | Unset):
        filterslugnot_in (str | Unset):
        filternameeq (str | Unset):
        filternamenot_eq (str | Unset):
        filternamein (str | Unset):
        filternamenot_in (str | Unset):
        filtermanaged_byeq (str | Unset):
        filtermanaged_bynot_eq (str | Unset):
        filtermanaged_byin (str | Unset):
        filtermanaged_bynot_in (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogEntityList]
     """


    kwargs = _get_kwargs(
        catalog_id=catalog_id,
include=include,
sort=sort,
pagenumber=pagenumber,
pagesize=pagesize,
filtersearch=filtersearch,
filterslug=filterslug,
filtername=filtername,
filterbackstage_id=filterbackstage_id,
filterexternal_id=filterexternal_id,
filtermanaged_by=filtermanaged_by,
filtercreated_atgt=filtercreated_atgt,
filtercreated_atgte=filtercreated_atgte,
filtercreated_atlt=filtercreated_atlt,
filtercreated_atlte=filtercreated_atlte,
filterslugeq=filterslugeq,
filterslugnot_eq=filterslugnot_eq,
filterslugin=filterslugin,
filterslugnot_in=filterslugnot_in,
filternameeq=filternameeq,
filternamenot_eq=filternamenot_eq,
filternamein=filternamein,
filternamenot_in=filternamenot_in,
filtermanaged_byeq=filtermanaged_byeq,
filtermanaged_bynot_eq=filtermanaged_bynot_eq,
filtermanaged_byin=filtermanaged_byin,
filtermanaged_bynot_in=filtermanaged_bynot_in,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    catalog_id: str,
    *,
    client: AuthenticatedClient,
    include: ListCatalogEntitiesInclude | Unset = UNSET,
    sort: ListCatalogEntitiesSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterslug: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterbackstage_id: str | Unset = UNSET,
    filterexternal_id: str | Unset = UNSET,
    filtermanaged_by: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterslugeq: str | Unset = UNSET,
    filterslugnot_eq: str | Unset = UNSET,
    filterslugin: str | Unset = UNSET,
    filterslugnot_in: str | Unset = UNSET,
    filternameeq: str | Unset = UNSET,
    filternamenot_eq: str | Unset = UNSET,
    filternamein: str | Unset = UNSET,
    filternamenot_in: str | Unset = UNSET,
    filtermanaged_byeq: str | Unset = UNSET,
    filtermanaged_bynot_eq: str | Unset = UNSET,
    filtermanaged_byin: str | Unset = UNSET,
    filtermanaged_bynot_in: str | Unset = UNSET,

) -> CatalogEntityList | None:
    """ List Catalog Entities

     List Catalog Entities

    Args:
        catalog_id (str):
        include (ListCatalogEntitiesInclude | Unset):
        sort (ListCatalogEntitiesSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filterslug (str | Unset):
        filtername (str | Unset):
        filterbackstage_id (str | Unset):
        filterexternal_id (str | Unset):
        filtermanaged_by (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterslugeq (str | Unset):
        filterslugnot_eq (str | Unset):
        filterslugin (str | Unset):
        filterslugnot_in (str | Unset):
        filternameeq (str | Unset):
        filternamenot_eq (str | Unset):
        filternamein (str | Unset):
        filternamenot_in (str | Unset):
        filtermanaged_byeq (str | Unset):
        filtermanaged_bynot_eq (str | Unset):
        filtermanaged_byin (str | Unset):
        filtermanaged_bynot_in (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogEntityList
     """


    return sync_detailed(
        catalog_id=catalog_id,
client=client,
include=include,
sort=sort,
pagenumber=pagenumber,
pagesize=pagesize,
filtersearch=filtersearch,
filterslug=filterslug,
filtername=filtername,
filterbackstage_id=filterbackstage_id,
filterexternal_id=filterexternal_id,
filtermanaged_by=filtermanaged_by,
filtercreated_atgt=filtercreated_atgt,
filtercreated_atgte=filtercreated_atgte,
filtercreated_atlt=filtercreated_atlt,
filtercreated_atlte=filtercreated_atlte,
filterslugeq=filterslugeq,
filterslugnot_eq=filterslugnot_eq,
filterslugin=filterslugin,
filterslugnot_in=filterslugnot_in,
filternameeq=filternameeq,
filternamenot_eq=filternamenot_eq,
filternamein=filternamein,
filternamenot_in=filternamenot_in,
filtermanaged_byeq=filtermanaged_byeq,
filtermanaged_bynot_eq=filtermanaged_bynot_eq,
filtermanaged_byin=filtermanaged_byin,
filtermanaged_bynot_in=filtermanaged_bynot_in,

    ).parsed

async def asyncio_detailed(
    catalog_id: str,
    *,
    client: AuthenticatedClient,
    include: ListCatalogEntitiesInclude | Unset = UNSET,
    sort: ListCatalogEntitiesSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterslug: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterbackstage_id: str | Unset = UNSET,
    filterexternal_id: str | Unset = UNSET,
    filtermanaged_by: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterslugeq: str | Unset = UNSET,
    filterslugnot_eq: str | Unset = UNSET,
    filterslugin: str | Unset = UNSET,
    filterslugnot_in: str | Unset = UNSET,
    filternameeq: str | Unset = UNSET,
    filternamenot_eq: str | Unset = UNSET,
    filternamein: str | Unset = UNSET,
    filternamenot_in: str | Unset = UNSET,
    filtermanaged_byeq: str | Unset = UNSET,
    filtermanaged_bynot_eq: str | Unset = UNSET,
    filtermanaged_byin: str | Unset = UNSET,
    filtermanaged_bynot_in: str | Unset = UNSET,

) -> Response[CatalogEntityList]:
    """ List Catalog Entities

     List Catalog Entities

    Args:
        catalog_id (str):
        include (ListCatalogEntitiesInclude | Unset):
        sort (ListCatalogEntitiesSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filterslug (str | Unset):
        filtername (str | Unset):
        filterbackstage_id (str | Unset):
        filterexternal_id (str | Unset):
        filtermanaged_by (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterslugeq (str | Unset):
        filterslugnot_eq (str | Unset):
        filterslugin (str | Unset):
        filterslugnot_in (str | Unset):
        filternameeq (str | Unset):
        filternamenot_eq (str | Unset):
        filternamein (str | Unset):
        filternamenot_in (str | Unset):
        filtermanaged_byeq (str | Unset):
        filtermanaged_bynot_eq (str | Unset):
        filtermanaged_byin (str | Unset):
        filtermanaged_bynot_in (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogEntityList]
     """


    kwargs = _get_kwargs(
        catalog_id=catalog_id,
include=include,
sort=sort,
pagenumber=pagenumber,
pagesize=pagesize,
filtersearch=filtersearch,
filterslug=filterslug,
filtername=filtername,
filterbackstage_id=filterbackstage_id,
filterexternal_id=filterexternal_id,
filtermanaged_by=filtermanaged_by,
filtercreated_atgt=filtercreated_atgt,
filtercreated_atgte=filtercreated_atgte,
filtercreated_atlt=filtercreated_atlt,
filtercreated_atlte=filtercreated_atlte,
filterslugeq=filterslugeq,
filterslugnot_eq=filterslugnot_eq,
filterslugin=filterslugin,
filterslugnot_in=filterslugnot_in,
filternameeq=filternameeq,
filternamenot_eq=filternamenot_eq,
filternamein=filternamein,
filternamenot_in=filternamenot_in,
filtermanaged_byeq=filtermanaged_byeq,
filtermanaged_bynot_eq=filtermanaged_bynot_eq,
filtermanaged_byin=filtermanaged_byin,
filtermanaged_bynot_in=filtermanaged_bynot_in,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    catalog_id: str,
    *,
    client: AuthenticatedClient,
    include: ListCatalogEntitiesInclude | Unset = UNSET,
    sort: ListCatalogEntitiesSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterslug: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterbackstage_id: str | Unset = UNSET,
    filterexternal_id: str | Unset = UNSET,
    filtermanaged_by: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterslugeq: str | Unset = UNSET,
    filterslugnot_eq: str | Unset = UNSET,
    filterslugin: str | Unset = UNSET,
    filterslugnot_in: str | Unset = UNSET,
    filternameeq: str | Unset = UNSET,
    filternamenot_eq: str | Unset = UNSET,
    filternamein: str | Unset = UNSET,
    filternamenot_in: str | Unset = UNSET,
    filtermanaged_byeq: str | Unset = UNSET,
    filtermanaged_bynot_eq: str | Unset = UNSET,
    filtermanaged_byin: str | Unset = UNSET,
    filtermanaged_bynot_in: str | Unset = UNSET,

) -> CatalogEntityList | None:
    """ List Catalog Entities

     List Catalog Entities

    Args:
        catalog_id (str):
        include (ListCatalogEntitiesInclude | Unset):
        sort (ListCatalogEntitiesSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filterslug (str | Unset):
        filtername (str | Unset):
        filterbackstage_id (str | Unset):
        filterexternal_id (str | Unset):
        filtermanaged_by (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterslugeq (str | Unset):
        filterslugnot_eq (str | Unset):
        filterslugin (str | Unset):
        filterslugnot_in (str | Unset):
        filternameeq (str | Unset):
        filternamenot_eq (str | Unset):
        filternamein (str | Unset):
        filternamenot_in (str | Unset):
        filtermanaged_byeq (str | Unset):
        filtermanaged_bynot_eq (str | Unset):
        filtermanaged_byin (str | Unset):
        filtermanaged_bynot_in (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogEntityList
     """


    return (await asyncio_detailed(
        catalog_id=catalog_id,
client=client,
include=include,
sort=sort,
pagenumber=pagenumber,
pagesize=pagesize,
filtersearch=filtersearch,
filterslug=filterslug,
filtername=filtername,
filterbackstage_id=filterbackstage_id,
filterexternal_id=filterexternal_id,
filtermanaged_by=filtermanaged_by,
filtercreated_atgt=filtercreated_atgt,
filtercreated_atgte=filtercreated_atgte,
filtercreated_atlt=filtercreated_atlt,
filtercreated_atlte=filtercreated_atlte,
filterslugeq=filterslugeq,
filterslugnot_eq=filterslugnot_eq,
filterslugin=filterslugin,
filterslugnot_in=filterslugnot_in,
filternameeq=filternameeq,
filternamenot_eq=filternamenot_eq,
filternamein=filternamein,
filternamenot_in=filternamenot_in,
filtermanaged_byeq=filtermanaged_byeq,
filtermanaged_bynot_eq=filtermanaged_bynot_eq,
filtermanaged_byin=filtermanaged_byin,
filtermanaged_bynot_in=filtermanaged_bynot_in,

    )).parsed
