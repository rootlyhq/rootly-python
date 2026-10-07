from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_workflows_include import ListWorkflowsInclude
from ...models.list_workflows_sort import ListWorkflowsSort
from ...models.workflow_list import WorkflowList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: ListWorkflowsInclude | Unset = UNSET,
    sort: ListWorkflowsSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterslug: str | Unset = UNSET,
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

    params["filter[name]"] = filtername

    params["filter[slug]"] = filterslug

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/workflows",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> WorkflowList | None:
    if response.status_code == 200:
        response_200 = WorkflowList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[WorkflowList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include: ListWorkflowsInclude | Unset = UNSET,
    sort: ListWorkflowsSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterslug: str | Unset = UNSET,
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
) -> Response[WorkflowList]:
    """List workflows

     List workflows

    Args:
        include (ListWorkflowsInclude | Unset):
        sort (ListWorkflowsSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filtername (str | Unset):
        filterslug (str | Unset):
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkflowList]
    """

    kwargs = _get_kwargs(
        include=include,
        sort=sort,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filtername=filtername,
        filterslug=filterslug,
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
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    include: ListWorkflowsInclude | Unset = UNSET,
    sort: ListWorkflowsSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterslug: str | Unset = UNSET,
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
) -> WorkflowList | None:
    """List workflows

     List workflows

    Args:
        include (ListWorkflowsInclude | Unset):
        sort (ListWorkflowsSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filtername (str | Unset):
        filterslug (str | Unset):
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkflowList
    """

    return sync_detailed(
        client=client,
        include=include,
        sort=sort,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filtername=filtername,
        filterslug=filterslug,
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
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: ListWorkflowsInclude | Unset = UNSET,
    sort: ListWorkflowsSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterslug: str | Unset = UNSET,
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
) -> Response[WorkflowList]:
    """List workflows

     List workflows

    Args:
        include (ListWorkflowsInclude | Unset):
        sort (ListWorkflowsSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filtername (str | Unset):
        filterslug (str | Unset):
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkflowList]
    """

    kwargs = _get_kwargs(
        include=include,
        sort=sort,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filtername=filtername,
        filterslug=filterslug,
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
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include: ListWorkflowsInclude | Unset = UNSET,
    sort: ListWorkflowsSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filtername: str | Unset = UNSET,
    filterslug: str | Unset = UNSET,
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
) -> WorkflowList | None:
    """List workflows

     List workflows

    Args:
        include (ListWorkflowsInclude | Unset):
        sort (ListWorkflowsSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filtername (str | Unset):
        filterslug (str | Unset):
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkflowList
    """

    return (
        await asyncio_detailed(
            client=client,
            include=include,
            sort=sort,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filtersearch=filtersearch,
            filtername=filtername,
            filterslug=filterslug,
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
        )
    ).parsed
