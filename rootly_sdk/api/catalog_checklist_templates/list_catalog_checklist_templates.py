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
    include: Unset | ListCatalogChecklistTemplatesInclude = UNSET,
    sort: Unset | ListCatalogChecklistTemplatesSort = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtername: Unset | str = UNSET,
    filterslug: Unset | str = UNSET,
    filtercatalog_type: Unset | str = UNSET,
    filterscope_type: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_include: Unset | str = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    json_sort: Unset | str = UNSET
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
    include: Unset | ListCatalogChecklistTemplatesInclude = UNSET,
    sort: Unset | ListCatalogChecklistTemplatesSort = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtername: Unset | str = UNSET,
    filterslug: Unset | str = UNSET,
    filtercatalog_type: Unset | str = UNSET,
    filterscope_type: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
) -> Response[CatalogChecklistTemplateList]:
    """List catalog checklist templates

     List catalog checklist templates

    Args:
        include (Union[Unset, ListCatalogChecklistTemplatesInclude]):
        sort (Union[Unset, ListCatalogChecklistTemplatesSort]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtername (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtercatalog_type (Union[Unset, str]):
        filterscope_type (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):

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
    include: Unset | ListCatalogChecklistTemplatesInclude = UNSET,
    sort: Unset | ListCatalogChecklistTemplatesSort = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtername: Unset | str = UNSET,
    filterslug: Unset | str = UNSET,
    filtercatalog_type: Unset | str = UNSET,
    filterscope_type: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
) -> CatalogChecklistTemplateList | None:
    """List catalog checklist templates

     List catalog checklist templates

    Args:
        include (Union[Unset, ListCatalogChecklistTemplatesInclude]):
        sort (Union[Unset, ListCatalogChecklistTemplatesSort]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtername (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtercatalog_type (Union[Unset, str]):
        filterscope_type (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):

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
    include: Unset | ListCatalogChecklistTemplatesInclude = UNSET,
    sort: Unset | ListCatalogChecklistTemplatesSort = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtername: Unset | str = UNSET,
    filterslug: Unset | str = UNSET,
    filtercatalog_type: Unset | str = UNSET,
    filterscope_type: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
) -> Response[CatalogChecklistTemplateList]:
    """List catalog checklist templates

     List catalog checklist templates

    Args:
        include (Union[Unset, ListCatalogChecklistTemplatesInclude]):
        sort (Union[Unset, ListCatalogChecklistTemplatesSort]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtername (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtercatalog_type (Union[Unset, str]):
        filterscope_type (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):

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
    include: Unset | ListCatalogChecklistTemplatesInclude = UNSET,
    sort: Unset | ListCatalogChecklistTemplatesSort = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtername: Unset | str = UNSET,
    filterslug: Unset | str = UNSET,
    filtercatalog_type: Unset | str = UNSET,
    filterscope_type: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
) -> CatalogChecklistTemplateList | None:
    """List catalog checklist templates

     List catalog checklist templates

    Args:
        include (Union[Unset, ListCatalogChecklistTemplatesInclude]):
        sort (Union[Unset, ListCatalogChecklistTemplatesSort]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtername (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filtercatalog_type (Union[Unset, str]):
        filterscope_type (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):

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
