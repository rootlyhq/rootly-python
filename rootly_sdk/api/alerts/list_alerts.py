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
    include: Unset | ListAlertsInclude = UNSET,
    filterstatus: Unset | str = UNSET,
    filtersource: Unset | str = UNSET,
    filterservices: Unset | str = UNSET,
    filterenvironments: Unset | str = UNSET,
    filtergroups: Unset | str = UNSET,
    filterlabels: Unset | str = UNSET,
    filterstarted_atgt: Unset | str = UNSET,
    filterstarted_atgte: Unset | str = UNSET,
    filterstarted_atlt: Unset | str = UNSET,
    filterstarted_atlte: Unset | str = UNSET,
    filterended_atgt: Unset | str = UNSET,
    filterended_atgte: Unset | str = UNSET,
    filterended_atlt: Unset | str = UNSET,
    filterended_atlte: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_include: Unset | str = UNSET
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
    include: Unset | ListAlertsInclude = UNSET,
    filterstatus: Unset | str = UNSET,
    filtersource: Unset | str = UNSET,
    filterservices: Unset | str = UNSET,
    filterenvironments: Unset | str = UNSET,
    filtergroups: Unset | str = UNSET,
    filterlabels: Unset | str = UNSET,
    filterstarted_atgt: Unset | str = UNSET,
    filterstarted_atgte: Unset | str = UNSET,
    filterstarted_atlt: Unset | str = UNSET,
    filterstarted_atlte: Unset | str = UNSET,
    filterended_atgt: Unset | str = UNSET,
    filterended_atgte: Unset | str = UNSET,
    filterended_atlt: Unset | str = UNSET,
    filterended_atlte: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
) -> Response[AlertList]:
    """List alerts

     List alerts

    Args:
        include (Union[Unset, ListAlertsInclude]):
        filterstatus (Union[Unset, str]):
        filtersource (Union[Unset, str]):
        filterservices (Union[Unset, str]):
        filterenvironments (Union[Unset, str]):
        filtergroups (Union[Unset, str]):
        filterlabels (Union[Unset, str]):
        filterstarted_atgt (Union[Unset, str]):
        filterstarted_atgte (Union[Unset, str]):
        filterstarted_atlt (Union[Unset, str]):
        filterstarted_atlte (Union[Unset, str]):
        filterended_atgt (Union[Unset, str]):
        filterended_atgte (Union[Unset, str]):
        filterended_atlt (Union[Unset, str]):
        filterended_atlte (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

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
    include: Unset | ListAlertsInclude = UNSET,
    filterstatus: Unset | str = UNSET,
    filtersource: Unset | str = UNSET,
    filterservices: Unset | str = UNSET,
    filterenvironments: Unset | str = UNSET,
    filtergroups: Unset | str = UNSET,
    filterlabels: Unset | str = UNSET,
    filterstarted_atgt: Unset | str = UNSET,
    filterstarted_atgte: Unset | str = UNSET,
    filterstarted_atlt: Unset | str = UNSET,
    filterstarted_atlte: Unset | str = UNSET,
    filterended_atgt: Unset | str = UNSET,
    filterended_atgte: Unset | str = UNSET,
    filterended_atlt: Unset | str = UNSET,
    filterended_atlte: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
) -> AlertList | None:
    """List alerts

     List alerts

    Args:
        include (Union[Unset, ListAlertsInclude]):
        filterstatus (Union[Unset, str]):
        filtersource (Union[Unset, str]):
        filterservices (Union[Unset, str]):
        filterenvironments (Union[Unset, str]):
        filtergroups (Union[Unset, str]):
        filterlabels (Union[Unset, str]):
        filterstarted_atgt (Union[Unset, str]):
        filterstarted_atgte (Union[Unset, str]):
        filterstarted_atlt (Union[Unset, str]):
        filterstarted_atlte (Union[Unset, str]):
        filterended_atgt (Union[Unset, str]):
        filterended_atgte (Union[Unset, str]):
        filterended_atlt (Union[Unset, str]):
        filterended_atlte (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

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
        pagenumber=pagenumber,
        pagesize=pagesize,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: Unset | ListAlertsInclude = UNSET,
    filterstatus: Unset | str = UNSET,
    filtersource: Unset | str = UNSET,
    filterservices: Unset | str = UNSET,
    filterenvironments: Unset | str = UNSET,
    filtergroups: Unset | str = UNSET,
    filterlabels: Unset | str = UNSET,
    filterstarted_atgt: Unset | str = UNSET,
    filterstarted_atgte: Unset | str = UNSET,
    filterstarted_atlt: Unset | str = UNSET,
    filterstarted_atlte: Unset | str = UNSET,
    filterended_atgt: Unset | str = UNSET,
    filterended_atgte: Unset | str = UNSET,
    filterended_atlt: Unset | str = UNSET,
    filterended_atlte: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
) -> Response[AlertList]:
    """List alerts

     List alerts

    Args:
        include (Union[Unset, ListAlertsInclude]):
        filterstatus (Union[Unset, str]):
        filtersource (Union[Unset, str]):
        filterservices (Union[Unset, str]):
        filterenvironments (Union[Unset, str]):
        filtergroups (Union[Unset, str]):
        filterlabels (Union[Unset, str]):
        filterstarted_atgt (Union[Unset, str]):
        filterstarted_atgte (Union[Unset, str]):
        filterstarted_atlt (Union[Unset, str]):
        filterstarted_atlte (Union[Unset, str]):
        filterended_atgt (Union[Unset, str]):
        filterended_atgte (Union[Unset, str]):
        filterended_atlt (Union[Unset, str]):
        filterended_atlte (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

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
        pagenumber=pagenumber,
        pagesize=pagesize,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include: Unset | ListAlertsInclude = UNSET,
    filterstatus: Unset | str = UNSET,
    filtersource: Unset | str = UNSET,
    filterservices: Unset | str = UNSET,
    filterenvironments: Unset | str = UNSET,
    filtergroups: Unset | str = UNSET,
    filterlabels: Unset | str = UNSET,
    filterstarted_atgt: Unset | str = UNSET,
    filterstarted_atgte: Unset | str = UNSET,
    filterstarted_atlt: Unset | str = UNSET,
    filterstarted_atlte: Unset | str = UNSET,
    filterended_atgt: Unset | str = UNSET,
    filterended_atgte: Unset | str = UNSET,
    filterended_atlt: Unset | str = UNSET,
    filterended_atlte: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
) -> AlertList | None:
    """List alerts

     List alerts

    Args:
        include (Union[Unset, ListAlertsInclude]):
        filterstatus (Union[Unset, str]):
        filtersource (Union[Unset, str]):
        filterservices (Union[Unset, str]):
        filterenvironments (Union[Unset, str]):
        filtergroups (Union[Unset, str]):
        filterlabels (Union[Unset, str]):
        filterstarted_atgt (Union[Unset, str]):
        filterstarted_atgte (Union[Unset, str]):
        filterstarted_atlt (Union[Unset, str]):
        filterstarted_atlte (Union[Unset, str]):
        filterended_atgt (Union[Unset, str]):
        filterended_atgte (Union[Unset, str]):
        filterended_atlt (Union[Unset, str]):
        filterended_atlte (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

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
            pagenumber=pagenumber,
            pagesize=pagesize,
        )
    ).parsed
