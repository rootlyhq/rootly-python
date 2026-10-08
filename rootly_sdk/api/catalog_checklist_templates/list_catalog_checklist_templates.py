from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_checklist_template_list import CatalogChecklistTemplateList
from ...models.list_catalog_checklist_templates_include import (
    ListCatalogChecklistTemplatesInclude,
)
from ...models.list_catalog_checklist_templates_sort import (
    ListCatalogChecklistTemplatesSort,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: ListCatalogChecklistTemplatesInclude | Unset = UNSET,
    sort: ListCatalogChecklistTemplatesSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterslug: str | Unset = UNSET,
    filtercatalog_type: str | Unset = UNSET,
    filterscope_type: str | Unset = UNSET,
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

    params["filter[name]"] = filtername

    params["filter[slug]"] = filterslug

    params["filter[catalog_type]"] = filtercatalog_type

    params["filter[scope_type]"] = filterscope_type

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/catalog_checklist_templates",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CatalogChecklistTemplateList | None:
    if response.status_code == 200:
        response_200 = CatalogChecklistTemplateList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CatalogChecklistTemplateList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include: ListCatalogChecklistTemplatesInclude | Unset = UNSET,
    sort: ListCatalogChecklistTemplatesSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterslug: str | Unset = UNSET,
    filtercatalog_type: str | Unset = UNSET,
    filterscope_type: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
) -> Response[CatalogChecklistTemplateList]:
    """List catalog checklist templates

     List catalog checklist templates

    Args:
        include (ListCatalogChecklistTemplatesInclude | Unset):
        sort (ListCatalogChecklistTemplatesSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtername (str | Unset):
        filterslug (str | Unset):
        filtercatalog_type (str | Unset):
        filterscope_type (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogChecklistTemplateList]
    """

    kwargs = _get_kwargs(
        include=include,
        sort=sort,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtername=filtername,
        filterslug=filterslug,
        filtercatalog_type=filtercatalog_type,
        filterscope_type=filterscope_type,
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
    include: ListCatalogChecklistTemplatesInclude | Unset = UNSET,
    sort: ListCatalogChecklistTemplatesSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterslug: str | Unset = UNSET,
    filtercatalog_type: str | Unset = UNSET,
    filterscope_type: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
) -> CatalogChecklistTemplateList | None:
    """List catalog checklist templates

     List catalog checklist templates

    Args:
        include (ListCatalogChecklistTemplatesInclude | Unset):
        sort (ListCatalogChecklistTemplatesSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtername (str | Unset):
        filterslug (str | Unset):
        filtercatalog_type (str | Unset):
        filterscope_type (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogChecklistTemplateList
    """

    return sync_detailed(
        client=client,
        include=include,
        sort=sort,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtername=filtername,
        filterslug=filterslug,
        filtercatalog_type=filtercatalog_type,
        filterscope_type=filterscope_type,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: ListCatalogChecklistTemplatesInclude | Unset = UNSET,
    sort: ListCatalogChecklistTemplatesSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterslug: str | Unset = UNSET,
    filtercatalog_type: str | Unset = UNSET,
    filterscope_type: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
) -> Response[CatalogChecklistTemplateList]:
    """List catalog checklist templates

     List catalog checklist templates

    Args:
        include (ListCatalogChecklistTemplatesInclude | Unset):
        sort (ListCatalogChecklistTemplatesSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtername (str | Unset):
        filterslug (str | Unset):
        filtercatalog_type (str | Unset):
        filterscope_type (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogChecklistTemplateList]
    """

    kwargs = _get_kwargs(
        include=include,
        sort=sort,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtername=filtername,
        filterslug=filterslug,
        filtercatalog_type=filtercatalog_type,
        filterscope_type=filterscope_type,
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
    include: ListCatalogChecklistTemplatesInclude | Unset = UNSET,
    sort: ListCatalogChecklistTemplatesSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterslug: str | Unset = UNSET,
    filtercatalog_type: str | Unset = UNSET,
    filterscope_type: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
) -> CatalogChecklistTemplateList | None:
    """List catalog checklist templates

     List catalog checklist templates

    Args:
        include (ListCatalogChecklistTemplatesInclude | Unset):
        sort (ListCatalogChecklistTemplatesSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtername (str | Unset):
        filterslug (str | Unset):
        filtercatalog_type (str | Unset):
        filterscope_type (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogChecklistTemplateList
    """

    return (
        await asyncio_detailed(
            client=client,
            include=include,
            sort=sort,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filtername=filtername,
            filterslug=filterslug,
            filtercatalog_type=filtercatalog_type,
            filterscope_type=filterscope_type,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
        )
    ).parsed
