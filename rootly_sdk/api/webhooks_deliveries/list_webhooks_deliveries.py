import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.webhooks_delivery_list import WebhooksDeliveryList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    endpoint_id: str,
    *,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filtercreated_atgt: datetime.datetime | Unset = UNSET,
    filtercreated_atgte: datetime.datetime | Unset = UNSET,
    filtercreated_atlt: datetime.datetime | Unset = UNSET,
    filtercreated_atlte: datetime.datetime | Unset = UNSET,
    filterdelivered_atgt: datetime.datetime | Unset = UNSET,
    filterdelivered_atgte: datetime.datetime | Unset = UNSET,
    filterdelivered_atlt: datetime.datetime | Unset = UNSET,
    filterdelivered_atlte: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include"] = include

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[status]"] = filterstatus

    json_filtercreated_atgt: str | Unset = UNSET
    if not isinstance(filtercreated_atgt, Unset):
        json_filtercreated_atgt = filtercreated_atgt.isoformat()
    params["filter[created_at][gt]"] = json_filtercreated_atgt

    json_filtercreated_atgte: str | Unset = UNSET
    if not isinstance(filtercreated_atgte, Unset):
        json_filtercreated_atgte = filtercreated_atgte.isoformat()
    params["filter[created_at][gte]"] = json_filtercreated_atgte

    json_filtercreated_atlt: str | Unset = UNSET
    if not isinstance(filtercreated_atlt, Unset):
        json_filtercreated_atlt = filtercreated_atlt.isoformat()
    params["filter[created_at][lt]"] = json_filtercreated_atlt

    json_filtercreated_atlte: str | Unset = UNSET
    if not isinstance(filtercreated_atlte, Unset):
        json_filtercreated_atlte = filtercreated_atlte.isoformat()
    params["filter[created_at][lte]"] = json_filtercreated_atlte

    json_filterdelivered_atgt: str | Unset = UNSET
    if not isinstance(filterdelivered_atgt, Unset):
        json_filterdelivered_atgt = filterdelivered_atgt.isoformat()
    params["filter[delivered_at][gt]"] = json_filterdelivered_atgt

    json_filterdelivered_atgte: str | Unset = UNSET
    if not isinstance(filterdelivered_atgte, Unset):
        json_filterdelivered_atgte = filterdelivered_atgte.isoformat()
    params["filter[delivered_at][gte]"] = json_filterdelivered_atgte

    json_filterdelivered_atlt: str | Unset = UNSET
    if not isinstance(filterdelivered_atlt, Unset):
        json_filterdelivered_atlt = filterdelivered_atlt.isoformat()
    params["filter[delivered_at][lt]"] = json_filterdelivered_atlt

    json_filterdelivered_atlte: str | Unset = UNSET
    if not isinstance(filterdelivered_atlte, Unset):
        json_filterdelivered_atlte = filterdelivered_atlte.isoformat()
    params["filter[delivered_at][lte]"] = json_filterdelivered_atlte

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/webhooks/endpoints/{endpoint_id}/deliveries".format(
            endpoint_id=quote(str(endpoint_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | WebhooksDeliveryList | None:
    if response.status_code == 200:
        response_200 = WebhooksDeliveryList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorsList.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorsList | WebhooksDeliveryList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    endpoint_id: str,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filtercreated_atgt: datetime.datetime | Unset = UNSET,
    filtercreated_atgte: datetime.datetime | Unset = UNSET,
    filtercreated_atlt: datetime.datetime | Unset = UNSET,
    filtercreated_atlte: datetime.datetime | Unset = UNSET,
    filterdelivered_atgt: datetime.datetime | Unset = UNSET,
    filterdelivered_atgte: datetime.datetime | Unset = UNSET,
    filterdelivered_atlt: datetime.datetime | Unset = UNSET,
    filterdelivered_atlte: datetime.datetime | Unset = UNSET,
) -> Response[ErrorsList | WebhooksDeliveryList]:
    """List webhook deliveries

     List webhook deliveries for given endpoint

    Args:
        endpoint_id (str):
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterstatus (str | Unset):
        filtercreated_atgt (datetime.datetime | Unset):
        filtercreated_atgte (datetime.datetime | Unset):
        filtercreated_atlt (datetime.datetime | Unset):
        filtercreated_atlte (datetime.datetime | Unset):
        filterdelivered_atgt (datetime.datetime | Unset):
        filterdelivered_atgte (datetime.datetime | Unset):
        filterdelivered_atlt (datetime.datetime | Unset):
        filterdelivered_atlte (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorsList | WebhooksDeliveryList]
    """

    kwargs = _get_kwargs(
        endpoint_id=endpoint_id,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterstatus=filterstatus,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterdelivered_atgt=filterdelivered_atgt,
        filterdelivered_atgte=filterdelivered_atgte,
        filterdelivered_atlt=filterdelivered_atlt,
        filterdelivered_atlte=filterdelivered_atlte,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    endpoint_id: str,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filtercreated_atgt: datetime.datetime | Unset = UNSET,
    filtercreated_atgte: datetime.datetime | Unset = UNSET,
    filtercreated_atlt: datetime.datetime | Unset = UNSET,
    filtercreated_atlte: datetime.datetime | Unset = UNSET,
    filterdelivered_atgt: datetime.datetime | Unset = UNSET,
    filterdelivered_atgte: datetime.datetime | Unset = UNSET,
    filterdelivered_atlt: datetime.datetime | Unset = UNSET,
    filterdelivered_atlte: datetime.datetime | Unset = UNSET,
) -> ErrorsList | WebhooksDeliveryList | None:
    """List webhook deliveries

     List webhook deliveries for given endpoint

    Args:
        endpoint_id (str):
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterstatus (str | Unset):
        filtercreated_atgt (datetime.datetime | Unset):
        filtercreated_atgte (datetime.datetime | Unset):
        filtercreated_atlt (datetime.datetime | Unset):
        filtercreated_atlte (datetime.datetime | Unset):
        filterdelivered_atgt (datetime.datetime | Unset):
        filterdelivered_atgte (datetime.datetime | Unset):
        filterdelivered_atlt (datetime.datetime | Unset):
        filterdelivered_atlte (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorsList | WebhooksDeliveryList
    """

    return sync_detailed(
        endpoint_id=endpoint_id,
        client=client,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterstatus=filterstatus,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterdelivered_atgt=filterdelivered_atgt,
        filterdelivered_atgte=filterdelivered_atgte,
        filterdelivered_atlt=filterdelivered_atlt,
        filterdelivered_atlte=filterdelivered_atlte,
    ).parsed


async def asyncio_detailed(
    endpoint_id: str,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filtercreated_atgt: datetime.datetime | Unset = UNSET,
    filtercreated_atgte: datetime.datetime | Unset = UNSET,
    filtercreated_atlt: datetime.datetime | Unset = UNSET,
    filtercreated_atlte: datetime.datetime | Unset = UNSET,
    filterdelivered_atgt: datetime.datetime | Unset = UNSET,
    filterdelivered_atgte: datetime.datetime | Unset = UNSET,
    filterdelivered_atlt: datetime.datetime | Unset = UNSET,
    filterdelivered_atlte: datetime.datetime | Unset = UNSET,
) -> Response[ErrorsList | WebhooksDeliveryList]:
    """List webhook deliveries

     List webhook deliveries for given endpoint

    Args:
        endpoint_id (str):
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterstatus (str | Unset):
        filtercreated_atgt (datetime.datetime | Unset):
        filtercreated_atgte (datetime.datetime | Unset):
        filtercreated_atlt (datetime.datetime | Unset):
        filtercreated_atlte (datetime.datetime | Unset):
        filterdelivered_atgt (datetime.datetime | Unset):
        filterdelivered_atgte (datetime.datetime | Unset):
        filterdelivered_atlt (datetime.datetime | Unset):
        filterdelivered_atlte (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorsList | WebhooksDeliveryList]
    """

    kwargs = _get_kwargs(
        endpoint_id=endpoint_id,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterstatus=filterstatus,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterdelivered_atgt=filterdelivered_atgt,
        filterdelivered_atgte=filterdelivered_atgte,
        filterdelivered_atlt=filterdelivered_atlt,
        filterdelivered_atlte=filterdelivered_atlte,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    endpoint_id: str,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filtercreated_atgt: datetime.datetime | Unset = UNSET,
    filtercreated_atgte: datetime.datetime | Unset = UNSET,
    filtercreated_atlt: datetime.datetime | Unset = UNSET,
    filtercreated_atlte: datetime.datetime | Unset = UNSET,
    filterdelivered_atgt: datetime.datetime | Unset = UNSET,
    filterdelivered_atgte: datetime.datetime | Unset = UNSET,
    filterdelivered_atlt: datetime.datetime | Unset = UNSET,
    filterdelivered_atlte: datetime.datetime | Unset = UNSET,
) -> ErrorsList | WebhooksDeliveryList | None:
    """List webhook deliveries

     List webhook deliveries for given endpoint

    Args:
        endpoint_id (str):
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterstatus (str | Unset):
        filtercreated_atgt (datetime.datetime | Unset):
        filtercreated_atgte (datetime.datetime | Unset):
        filtercreated_atlt (datetime.datetime | Unset):
        filtercreated_atlte (datetime.datetime | Unset):
        filterdelivered_atgt (datetime.datetime | Unset):
        filterdelivered_atgte (datetime.datetime | Unset):
        filterdelivered_atlt (datetime.datetime | Unset):
        filterdelivered_atlte (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorsList | WebhooksDeliveryList
    """

    return (
        await asyncio_detailed(
            endpoint_id=endpoint_id,
            client=client,
            include=include,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filterstatus=filterstatus,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
            filterdelivered_atgt=filterdelivered_atgt,
            filterdelivered_atgte=filterdelivered_atgte,
            filterdelivered_atlt=filterdelivered_atlt,
            filterdelivered_atlte=filterdelivered_atlte,
        )
    ).parsed
