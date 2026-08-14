from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_list import CatalogList
from ...models.list_catalogs_include import ListCatalogsInclude
from ...models.list_catalogs_sort import ListCatalogsSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: Union[Unset, ListCatalogsInclude] = UNSET,
    sort: Union[Unset, ListCatalogsSort] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filterslug: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    filterexternal_id: Union[Unset, str] = UNSET,
    filtermanaged_by: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterslugeq: Union[Unset, str] = UNSET,
    filterslugnot_eq: Union[Unset, str] = UNSET,
    filterslugin: Union[Unset, str] = UNSET,
    filterslugnot_in: Union[Unset, str] = UNSET,
    filternameeq: Union[Unset, str] = UNSET,
    filternamenot_eq: Union[Unset, str] = UNSET,
    filternamein: Union[Unset, str] = UNSET,
    filternamenot_in: Union[Unset, str] = UNSET,
    filtermanaged_byeq: Union[Unset, str] = UNSET,
    filtermanaged_bynot_eq: Union[Unset, str] = UNSET,
    filtermanaged_byin: Union[Unset, str] = UNSET,
    filtermanaged_bynot_in: Union[Unset, str] = UNSET,
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

    params["filter[search]"] = filtersearch

    params["filter[slug]"] = filterslug

    params["filter[name]"] = filtername

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
        "url": "/v1/catalogs",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[CatalogList]:
    if response.status_code == 200:
        response_200 = CatalogList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[CatalogList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, ListCatalogsInclude] = UNSET,
    sort: Union[Unset, ListCatalogsSort] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filterslug: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    filterexternal_id: Union[Unset, str] = UNSET,
    filtermanaged_by: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterslugeq: Union[Unset, str] = UNSET,
    filterslugnot_eq: Union[Unset, str] = UNSET,
    filterslugin: Union[Unset, str] = UNSET,
    filterslugnot_in: Union[Unset, str] = UNSET,
    filternameeq: Union[Unset, str] = UNSET,
    filternamenot_eq: Union[Unset, str] = UNSET,
    filternamein: Union[Unset, str] = UNSET,
    filternamenot_in: Union[Unset, str] = UNSET,
    filtermanaged_byeq: Union[Unset, str] = UNSET,
    filtermanaged_bynot_eq: Union[Unset, str] = UNSET,
    filtermanaged_byin: Union[Unset, str] = UNSET,
    filtermanaged_bynot_in: Union[Unset, str] = UNSET,
) -> Response[CatalogList]:
    """List catalogs

     List catalogs

    Args:
        include (Union[Unset, ListCatalogsInclude]):
        sort (Union[Unset, ListCatalogsSort]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterexternal_id (Union[Unset, str]):
        filtermanaged_by (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterslugeq (Union[Unset, str]):
        filterslugnot_eq (Union[Unset, str]):
        filterslugin (Union[Unset, str]):
        filterslugnot_in (Union[Unset, str]):
        filternameeq (Union[Unset, str]):
        filternamenot_eq (Union[Unset, str]):
        filternamein (Union[Unset, str]):
        filternamenot_in (Union[Unset, str]):
        filtermanaged_byeq (Union[Unset, str]):
        filtermanaged_bynot_eq (Union[Unset, str]):
        filtermanaged_byin (Union[Unset, str]):
        filtermanaged_bynot_in (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogList]
    """

    kwargs = _get_kwargs(
        include=include,
        sort=sort,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterslug=filterslug,
        filtername=filtername,
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
    *,
    client: AuthenticatedClient,
    include: Union[Unset, ListCatalogsInclude] = UNSET,
    sort: Union[Unset, ListCatalogsSort] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filterslug: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    filterexternal_id: Union[Unset, str] = UNSET,
    filtermanaged_by: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterslugeq: Union[Unset, str] = UNSET,
    filterslugnot_eq: Union[Unset, str] = UNSET,
    filterslugin: Union[Unset, str] = UNSET,
    filterslugnot_in: Union[Unset, str] = UNSET,
    filternameeq: Union[Unset, str] = UNSET,
    filternamenot_eq: Union[Unset, str] = UNSET,
    filternamein: Union[Unset, str] = UNSET,
    filternamenot_in: Union[Unset, str] = UNSET,
    filtermanaged_byeq: Union[Unset, str] = UNSET,
    filtermanaged_bynot_eq: Union[Unset, str] = UNSET,
    filtermanaged_byin: Union[Unset, str] = UNSET,
    filtermanaged_bynot_in: Union[Unset, str] = UNSET,
) -> Optional[CatalogList]:
    """List catalogs

     List catalogs

    Args:
        include (Union[Unset, ListCatalogsInclude]):
        sort (Union[Unset, ListCatalogsSort]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterexternal_id (Union[Unset, str]):
        filtermanaged_by (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterslugeq (Union[Unset, str]):
        filterslugnot_eq (Union[Unset, str]):
        filterslugin (Union[Unset, str]):
        filterslugnot_in (Union[Unset, str]):
        filternameeq (Union[Unset, str]):
        filternamenot_eq (Union[Unset, str]):
        filternamein (Union[Unset, str]):
        filternamenot_in (Union[Unset, str]):
        filtermanaged_byeq (Union[Unset, str]):
        filtermanaged_bynot_eq (Union[Unset, str]):
        filtermanaged_byin (Union[Unset, str]):
        filtermanaged_bynot_in (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogList
    """

    return sync_detailed(
        client=client,
        include=include,
        sort=sort,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterslug=filterslug,
        filtername=filtername,
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
    *,
    client: AuthenticatedClient,
    include: Union[Unset, ListCatalogsInclude] = UNSET,
    sort: Union[Unset, ListCatalogsSort] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filterslug: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    filterexternal_id: Union[Unset, str] = UNSET,
    filtermanaged_by: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterslugeq: Union[Unset, str] = UNSET,
    filterslugnot_eq: Union[Unset, str] = UNSET,
    filterslugin: Union[Unset, str] = UNSET,
    filterslugnot_in: Union[Unset, str] = UNSET,
    filternameeq: Union[Unset, str] = UNSET,
    filternamenot_eq: Union[Unset, str] = UNSET,
    filternamein: Union[Unset, str] = UNSET,
    filternamenot_in: Union[Unset, str] = UNSET,
    filtermanaged_byeq: Union[Unset, str] = UNSET,
    filtermanaged_bynot_eq: Union[Unset, str] = UNSET,
    filtermanaged_byin: Union[Unset, str] = UNSET,
    filtermanaged_bynot_in: Union[Unset, str] = UNSET,
) -> Response[CatalogList]:
    """List catalogs

     List catalogs

    Args:
        include (Union[Unset, ListCatalogsInclude]):
        sort (Union[Unset, ListCatalogsSort]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterexternal_id (Union[Unset, str]):
        filtermanaged_by (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterslugeq (Union[Unset, str]):
        filterslugnot_eq (Union[Unset, str]):
        filterslugin (Union[Unset, str]):
        filterslugnot_in (Union[Unset, str]):
        filternameeq (Union[Unset, str]):
        filternamenot_eq (Union[Unset, str]):
        filternamein (Union[Unset, str]):
        filternamenot_in (Union[Unset, str]):
        filtermanaged_byeq (Union[Unset, str]):
        filtermanaged_bynot_eq (Union[Unset, str]):
        filtermanaged_byin (Union[Unset, str]):
        filtermanaged_bynot_in (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogList]
    """

    kwargs = _get_kwargs(
        include=include,
        sort=sort,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterslug=filterslug,
        filtername=filtername,
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

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, ListCatalogsInclude] = UNSET,
    sort: Union[Unset, ListCatalogsSort] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filterslug: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    filterexternal_id: Union[Unset, str] = UNSET,
    filtermanaged_by: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterslugeq: Union[Unset, str] = UNSET,
    filterslugnot_eq: Union[Unset, str] = UNSET,
    filterslugin: Union[Unset, str] = UNSET,
    filterslugnot_in: Union[Unset, str] = UNSET,
    filternameeq: Union[Unset, str] = UNSET,
    filternamenot_eq: Union[Unset, str] = UNSET,
    filternamein: Union[Unset, str] = UNSET,
    filternamenot_in: Union[Unset, str] = UNSET,
    filtermanaged_byeq: Union[Unset, str] = UNSET,
    filtermanaged_bynot_eq: Union[Unset, str] = UNSET,
    filtermanaged_byin: Union[Unset, str] = UNSET,
    filtermanaged_bynot_in: Union[Unset, str] = UNSET,
) -> Optional[CatalogList]:
    """List catalogs

     List catalogs

    Args:
        include (Union[Unset, ListCatalogsInclude]):
        sort (Union[Unset, ListCatalogsSort]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterexternal_id (Union[Unset, str]):
        filtermanaged_by (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterslugeq (Union[Unset, str]):
        filterslugnot_eq (Union[Unset, str]):
        filterslugin (Union[Unset, str]):
        filterslugnot_in (Union[Unset, str]):
        filternameeq (Union[Unset, str]):
        filternamenot_eq (Union[Unset, str]):
        filternamein (Union[Unset, str]):
        filternamenot_in (Union[Unset, str]):
        filtermanaged_byeq (Union[Unset, str]):
        filtermanaged_bynot_eq (Union[Unset, str]):
        filtermanaged_byin (Union[Unset, str]):
        filtermanaged_bynot_in (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogList
    """

    return (
        await asyncio_detailed(
            client=client,
            include=include,
            sort=sort,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filtersearch=filtersearch,
            filterslug=filterslug,
            filtername=filtername,
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
    ).parsed
