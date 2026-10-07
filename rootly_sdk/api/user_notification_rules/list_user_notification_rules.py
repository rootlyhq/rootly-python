from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_notification_rule_list import UserNotificationRuleList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include"] = include

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/users/{user_id}/notification_rules".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UserNotificationRuleList | None:
    if response.status_code == 200:
        response_200 = UserNotificationRuleList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UserNotificationRuleList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[UserNotificationRuleList]:
    """List user notification rules

     List user notification rules

    Args:
        user_id (str):
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserNotificationRuleList]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> UserNotificationRuleList | None:
    """List user notification rules

     List user notification rules

    Args:
        user_id (str):
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserNotificationRuleList
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[UserNotificationRuleList]:
    """List user notification rules

     List user notification rules

    Args:
        user_id (str):
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserNotificationRuleList]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> UserNotificationRuleList | None:
    """List user notification rules

     List user notification rules

    Args:
        user_id (str):
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserNotificationRuleList
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            include=include,
            pagenumber=pagenumber,
            pagesize=pagesize,
            sort=sort,
        )
    ).parsed
