from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_list import AlertList
from ...models.list_alerts_include import ListAlertsInclude
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: ListAlertsInclude | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filtersource: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filtergroups: str | Unset = UNSET,
    filterlabels: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filterended_atgt: str | Unset = UNSET,
    filterended_atgte: str | Unset = UNSET,
    filterended_atlt: str | Unset = UNSET,
    filterended_atlte: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    pageafter: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_include: str | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    params["filter[status]"] = filterstatus

    params["filter[source]"] = filtersource

    params["filter[services]"] = filterservices

    params["filter[environments]"] = filterenvironments

    params["filter[groups]"] = filtergroups

    params["filter[labels]"] = filterlabels

    params["filter[started_at][gt]"] = filterstarted_atgt

    params["filter[started_at][gte]"] = filterstarted_atgte

    params["filter[started_at][lt]"] = filterstarted_atlt

    params["filter[started_at][lte]"] = filterstarted_atlte

    params["filter[ended_at][gt]"] = filterended_atgt

    params["filter[ended_at][gte]"] = filterended_atgte

    params["filter[ended_at][lt]"] = filterended_atlt

    params["filter[ended_at][lte]"] = filterended_atlte

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params["page[after]"] = pageafter

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/alerts",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AlertList | None:
    if response.status_code == 200:
        response_200 = AlertList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AlertList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include: ListAlertsInclude | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filtersource: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filtergroups: str | Unset = UNSET,
    filterlabels: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filterended_atgt: str | Unset = UNSET,
    filterended_atgte: str | Unset = UNSET,
    filterended_atlt: str | Unset = UNSET,
    filterended_atlte: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    pageafter: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Response[AlertList]:
    """List alerts

     List alerts

    Args:
        include (ListAlertsInclude | Unset):
        filterstatus (str | Unset):
        filtersource (str | Unset):
        filterservices (str | Unset):
        filterenvironments (str | Unset):
        filtergroups (str | Unset):
        filterlabels (str | Unset):
        filterstarted_atgt (str | Unset):
        filterstarted_atgte (str | Unset):
        filterstarted_atlt (str | Unset):
        filterstarted_atlte (str | Unset):
        filterended_atgt (str | Unset):
        filterended_atgte (str | Unset):
        filterended_atlt (str | Unset):
        filterended_atlte (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        pageafter (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertList]
    """

    kwargs = _get_kwargs(
        include=include,
        filterstatus=filterstatus,
        filtersource=filtersource,
        filterservices=filterservices,
        filterenvironments=filterenvironments,
        filtergroups=filtergroups,
        filterlabels=filterlabels,
        filterstarted_atgt=filterstarted_atgt,
        filterstarted_atgte=filterstarted_atgte,
        filterstarted_atlt=filterstarted_atlt,
        filterstarted_atlte=filterstarted_atlte,
        filterended_atgt=filterended_atgt,
        filterended_atgte=filterended_atgte,
        filterended_atlt=filterended_atlt,
        filterended_atlte=filterended_atlte,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        pageafter=pageafter,
        pagenumber=pagenumber,
        pagesize=pagesize,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    include: ListAlertsInclude | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filtersource: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filtergroups: str | Unset = UNSET,
    filterlabels: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filterended_atgt: str | Unset = UNSET,
    filterended_atgte: str | Unset = UNSET,
    filterended_atlt: str | Unset = UNSET,
    filterended_atlte: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    pageafter: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> AlertList | None:
    """List alerts

     List alerts

    Args:
        include (ListAlertsInclude | Unset):
        filterstatus (str | Unset):
        filtersource (str | Unset):
        filterservices (str | Unset):
        filterenvironments (str | Unset):
        filtergroups (str | Unset):
        filterlabels (str | Unset):
        filterstarted_atgt (str | Unset):
        filterstarted_atgte (str | Unset):
        filterstarted_atlt (str | Unset):
        filterstarted_atlte (str | Unset):
        filterended_atgt (str | Unset):
        filterended_atgte (str | Unset):
        filterended_atlt (str | Unset):
        filterended_atlte (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        pageafter (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertList
    """

    return sync_detailed(
        client=client,
        include=include,
        filterstatus=filterstatus,
        filtersource=filtersource,
        filterservices=filterservices,
        filterenvironments=filterenvironments,
        filtergroups=filtergroups,
        filterlabels=filterlabels,
        filterstarted_atgt=filterstarted_atgt,
        filterstarted_atgte=filterstarted_atgte,
        filterstarted_atlt=filterstarted_atlt,
        filterstarted_atlte=filterstarted_atlte,
        filterended_atgt=filterended_atgt,
        filterended_atgte=filterended_atgte,
        filterended_atlt=filterended_atlt,
        filterended_atlte=filterended_atlte,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        pageafter=pageafter,
        pagenumber=pagenumber,
        pagesize=pagesize,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: ListAlertsInclude | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filtersource: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filtergroups: str | Unset = UNSET,
    filterlabels: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filterended_atgt: str | Unset = UNSET,
    filterended_atgte: str | Unset = UNSET,
    filterended_atlt: str | Unset = UNSET,
    filterended_atlte: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    pageafter: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Response[AlertList]:
    """List alerts

     List alerts

    Args:
        include (ListAlertsInclude | Unset):
        filterstatus (str | Unset):
        filtersource (str | Unset):
        filterservices (str | Unset):
        filterenvironments (str | Unset):
        filtergroups (str | Unset):
        filterlabels (str | Unset):
        filterstarted_atgt (str | Unset):
        filterstarted_atgte (str | Unset):
        filterstarted_atlt (str | Unset):
        filterstarted_atlte (str | Unset):
        filterended_atgt (str | Unset):
        filterended_atgte (str | Unset):
        filterended_atlt (str | Unset):
        filterended_atlte (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        pageafter (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertList]
    """

    kwargs = _get_kwargs(
        include=include,
        filterstatus=filterstatus,
        filtersource=filtersource,
        filterservices=filterservices,
        filterenvironments=filterenvironments,
        filtergroups=filtergroups,
        filterlabels=filterlabels,
        filterstarted_atgt=filterstarted_atgt,
        filterstarted_atgte=filterstarted_atgte,
        filterstarted_atlt=filterstarted_atlt,
        filterstarted_atlte=filterstarted_atlte,
        filterended_atgt=filterended_atgt,
        filterended_atgte=filterended_atgte,
        filterended_atlt=filterended_atlt,
        filterended_atlte=filterended_atlte,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        pageafter=pageafter,
        pagenumber=pagenumber,
        pagesize=pagesize,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include: ListAlertsInclude | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filtersource: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filtergroups: str | Unset = UNSET,
    filterlabels: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filterended_atgt: str | Unset = UNSET,
    filterended_atgte: str | Unset = UNSET,
    filterended_atlt: str | Unset = UNSET,
    filterended_atlte: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    pageafter: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> AlertList | None:
    """List alerts

     List alerts

    Args:
        include (ListAlertsInclude | Unset):
        filterstatus (str | Unset):
        filtersource (str | Unset):
        filterservices (str | Unset):
        filterenvironments (str | Unset):
        filtergroups (str | Unset):
        filterlabels (str | Unset):
        filterstarted_atgt (str | Unset):
        filterstarted_atgte (str | Unset):
        filterstarted_atlt (str | Unset):
        filterstarted_atlte (str | Unset):
        filterended_atgt (str | Unset):
        filterended_atgte (str | Unset):
        filterended_atlt (str | Unset):
        filterended_atlte (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        pageafter (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertList
    """

    return (
        await asyncio_detailed(
            client=client,
            include=include,
            filterstatus=filterstatus,
            filtersource=filtersource,
            filterservices=filterservices,
            filterenvironments=filterenvironments,
            filtergroups=filtergroups,
            filterlabels=filterlabels,
            filterstarted_atgt=filterstarted_atgt,
            filterstarted_atgte=filterstarted_atgte,
            filterstarted_atlt=filterstarted_atlt,
            filterstarted_atlte=filterstarted_atlte,
            filterended_atgt=filterended_atgt,
            filterended_atgte=filterended_atgte,
            filterended_atlt=filterended_atlt,
            filterended_atlte=filterended_atlte,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
            pageafter=pageafter,
            pagenumber=pagenumber,
            pagesize=pagesize,
        )
    ).parsed
