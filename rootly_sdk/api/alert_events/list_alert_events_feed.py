from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_event_feed_list import AlertEventFeedList
from ...models.list_alert_events_feed_filteraction import (
    ListAlertEventsFeedFilteraction,
)
from ...models.list_alert_events_feed_filterkind import (
    ListAlertEventsFeedFilterkind,
)
from ...models.list_alert_events_feed_sort import ListAlertEventsFeedSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: str | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    pageafter: str | Unset = UNSET,
    sort: ListAlertEventsFeedSort | Unset = UNSET,
    filterkind: ListAlertEventsFeedFilterkind | Unset = UNSET,
    filteraction: ListAlertEventsFeedFilteraction | Unset = UNSET,
    filteralert_id: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["include"] = include

    params["page[size]"] = pagesize

    params["page[after]"] = pageafter

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    json_filterkind: str | Unset = UNSET
    if not isinstance(filterkind, Unset):
        json_filterkind = filterkind

    params["filter[kind]"] = json_filterkind

    json_filteraction: str | Unset = UNSET
    if not isinstance(filteraction, Unset):
        json_filteraction = filteraction

    params["filter[action]"] = json_filteraction

    params["filter[alert_id]"] = filteralert_id

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/alert_events",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AlertEventFeedList | None:
    if response.status_code == 200:
        response_200 = AlertEventFeedList.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AlertEventFeedList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    pageafter: str | Unset = UNSET,
    sort: ListAlertEventsFeedSort | Unset = UNSET,
    filterkind: ListAlertEventsFeedFilterkind | Unset = UNSET,
    filteraction: ListAlertEventsFeedFilteraction | Unset = UNSET,
    filteralert_id: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,

) -> Response[AlertEventFeedList]:
    """ List alert events across alerts

     Returns a flat list of alert events across all alerts the requester can access. Designed for
    periodic polling: use `page[after]` with the `next_cursor` returned in the previous response to
    stream forward.

    Args:
        include (str | Unset):
        pagesize (int | Unset):
        pageafter (str | Unset):
        sort (ListAlertEventsFeedSort | Unset):
        filterkind (ListAlertEventsFeedFilterkind | Unset):
        filteraction (ListAlertEventsFeedFilteraction | Unset):
        filteralert_id (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertEventFeedList]
     """


    kwargs = _get_kwargs(
        include=include,
pagesize=pagesize,
pageafter=pageafter,
sort=sort,
filterkind=filterkind,
filteraction=filteraction,
filteralert_id=filteralert_id,
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
    include: str | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    pageafter: str | Unset = UNSET,
    sort: ListAlertEventsFeedSort | Unset = UNSET,
    filterkind: ListAlertEventsFeedFilterkind | Unset = UNSET,
    filteraction: ListAlertEventsFeedFilteraction | Unset = UNSET,
    filteralert_id: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,

) -> AlertEventFeedList | None:
    """ List alert events across alerts

     Returns a flat list of alert events across all alerts the requester can access. Designed for
    periodic polling: use `page[after]` with the `next_cursor` returned in the previous response to
    stream forward.

    Args:
        include (str | Unset):
        pagesize (int | Unset):
        pageafter (str | Unset):
        sort (ListAlertEventsFeedSort | Unset):
        filterkind (ListAlertEventsFeedFilterkind | Unset):
        filteraction (ListAlertEventsFeedFilteraction | Unset):
        filteralert_id (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertEventFeedList
     """


    return sync_detailed(
        client=client,
include=include,
pagesize=pagesize,
pageafter=pageafter,
sort=sort,
filterkind=filterkind,
filteraction=filteraction,
filteralert_id=filteralert_id,
filtercreated_atgt=filtercreated_atgt,
filtercreated_atgte=filtercreated_atgte,
filtercreated_atlt=filtercreated_atlt,
filtercreated_atlte=filtercreated_atlte,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    pageafter: str | Unset = UNSET,
    sort: ListAlertEventsFeedSort | Unset = UNSET,
    filterkind: ListAlertEventsFeedFilterkind | Unset = UNSET,
    filteraction: ListAlertEventsFeedFilteraction | Unset = UNSET,
    filteralert_id: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,

) -> Response[AlertEventFeedList]:
    """ List alert events across alerts

     Returns a flat list of alert events across all alerts the requester can access. Designed for
    periodic polling: use `page[after]` with the `next_cursor` returned in the previous response to
    stream forward.

    Args:
        include (str | Unset):
        pagesize (int | Unset):
        pageafter (str | Unset):
        sort (ListAlertEventsFeedSort | Unset):
        filterkind (ListAlertEventsFeedFilterkind | Unset):
        filteraction (ListAlertEventsFeedFilteraction | Unset):
        filteralert_id (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertEventFeedList]
     """


    kwargs = _get_kwargs(
        include=include,
pagesize=pagesize,
pageafter=pageafter,
sort=sort,
filterkind=filterkind,
filteraction=filteraction,
filteralert_id=filteralert_id,
filtercreated_atgt=filtercreated_atgt,
filtercreated_atgte=filtercreated_atgte,
filtercreated_atlt=filtercreated_atlt,
filtercreated_atlte=filtercreated_atlte,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    pageafter: str | Unset = UNSET,
    sort: ListAlertEventsFeedSort | Unset = UNSET,
    filterkind: ListAlertEventsFeedFilterkind | Unset = UNSET,
    filteraction: ListAlertEventsFeedFilteraction | Unset = UNSET,
    filteralert_id: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,

) -> AlertEventFeedList | None:
    """ List alert events across alerts

     Returns a flat list of alert events across all alerts the requester can access. Designed for
    periodic polling: use `page[after]` with the `next_cursor` returned in the previous response to
    stream forward.

    Args:
        include (str | Unset):
        pagesize (int | Unset):
        pageafter (str | Unset):
        sort (ListAlertEventsFeedSort | Unset):
        filterkind (ListAlertEventsFeedFilterkind | Unset):
        filteraction (ListAlertEventsFeedFilteraction | Unset):
        filteralert_id (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertEventFeedList
     """


    return (await asyncio_detailed(
        client=client,
include=include,
pagesize=pagesize,
pageafter=pageafter,
sort=sort,
filterkind=filterkind,
filteraction=filteraction,
filteralert_id=filteralert_id,
filtercreated_atgt=filtercreated_atgt,
filtercreated_atgte=filtercreated_atgte,
filtercreated_atlt=filtercreated_atlt,
filtercreated_atlte=filtercreated_atlte,

    )).parsed
