from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.list_oncalls_include import ListOncallsInclude
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: ListOncallsInclude | Unset = UNSET,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    earliest: bool | Unset = UNSET,
    time_zone: str | Unset = UNSET,
    filterescalation_policy_ids: str | Unset = UNSET,
    filterschedule_ids: str | Unset = UNSET,
    filteruser_ids: str | Unset = UNSET,
    filterservice_ids: str | Unset = UNSET,
    filtergroup_ids: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_include: str | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    params["since"] = since

    params["until"] = until

    params["earliest"] = earliest

    params["time_zone"] = time_zone

    params["filter[escalation_policy_ids]"] = filterescalation_policy_ids

    params["filter[schedule_ids]"] = filterschedule_ids

    params["filter[user_ids]"] = filteruser_ids

    params["filter[service_ids]"] = filterservice_ids

    params["filter[group_ids]"] = filtergroup_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/oncalls",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorsList | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 401:
        response_401 = ErrorsList.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorsList.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorsList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include: ListOncallsInclude | Unset = UNSET,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    earliest: bool | Unset = UNSET,
    time_zone: str | Unset = UNSET,
    filterescalation_policy_ids: str | Unset = UNSET,
    filterschedule_ids: str | Unset = UNSET,
    filteruser_ids: str | Unset = UNSET,
    filterservice_ids: str | Unset = UNSET,
    filtergroup_ids: str | Unset = UNSET,
) -> Response[Any | ErrorsList]:
    """List on-calls

     List who is currently on-call, with support for filtering by escalation policy, schedule, and user.
    Returns on-call entries grouped by escalation policy level.

    Args:
        include (ListOncallsInclude | Unset):
        since (str | Unset):
        until (str | Unset):
        earliest (bool | Unset):
        time_zone (str | Unset):
        filterescalation_policy_ids (str | Unset):
        filterschedule_ids (str | Unset):
        filteruser_ids (str | Unset):
        filterservice_ids (str | Unset):
        filtergroup_ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorsList]
    """

    kwargs = _get_kwargs(
        include=include,
        since=since,
        until=until,
        earliest=earliest,
        time_zone=time_zone,
        filterescalation_policy_ids=filterescalation_policy_ids,
        filterschedule_ids=filterschedule_ids,
        filteruser_ids=filteruser_ids,
        filterservice_ids=filterservice_ids,
        filtergroup_ids=filtergroup_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    include: ListOncallsInclude | Unset = UNSET,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    earliest: bool | Unset = UNSET,
    time_zone: str | Unset = UNSET,
    filterescalation_policy_ids: str | Unset = UNSET,
    filterschedule_ids: str | Unset = UNSET,
    filteruser_ids: str | Unset = UNSET,
    filterservice_ids: str | Unset = UNSET,
    filtergroup_ids: str | Unset = UNSET,
) -> Any | ErrorsList | None:
    """List on-calls

     List who is currently on-call, with support for filtering by escalation policy, schedule, and user.
    Returns on-call entries grouped by escalation policy level.

    Args:
        include (ListOncallsInclude | Unset):
        since (str | Unset):
        until (str | Unset):
        earliest (bool | Unset):
        time_zone (str | Unset):
        filterescalation_policy_ids (str | Unset):
        filterschedule_ids (str | Unset):
        filteruser_ids (str | Unset):
        filterservice_ids (str | Unset):
        filtergroup_ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorsList
    """

    return sync_detailed(
        client=client,
        include=include,
        since=since,
        until=until,
        earliest=earliest,
        time_zone=time_zone,
        filterescalation_policy_ids=filterescalation_policy_ids,
        filterschedule_ids=filterschedule_ids,
        filteruser_ids=filteruser_ids,
        filterservice_ids=filterservice_ids,
        filtergroup_ids=filtergroup_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: ListOncallsInclude | Unset = UNSET,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    earliest: bool | Unset = UNSET,
    time_zone: str | Unset = UNSET,
    filterescalation_policy_ids: str | Unset = UNSET,
    filterschedule_ids: str | Unset = UNSET,
    filteruser_ids: str | Unset = UNSET,
    filterservice_ids: str | Unset = UNSET,
    filtergroup_ids: str | Unset = UNSET,
) -> Response[Any | ErrorsList]:
    """List on-calls

     List who is currently on-call, with support for filtering by escalation policy, schedule, and user.
    Returns on-call entries grouped by escalation policy level.

    Args:
        include (ListOncallsInclude | Unset):
        since (str | Unset):
        until (str | Unset):
        earliest (bool | Unset):
        time_zone (str | Unset):
        filterescalation_policy_ids (str | Unset):
        filterschedule_ids (str | Unset):
        filteruser_ids (str | Unset):
        filterservice_ids (str | Unset):
        filtergroup_ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorsList]
    """

    kwargs = _get_kwargs(
        include=include,
        since=since,
        until=until,
        earliest=earliest,
        time_zone=time_zone,
        filterescalation_policy_ids=filterescalation_policy_ids,
        filterschedule_ids=filterschedule_ids,
        filteruser_ids=filteruser_ids,
        filterservice_ids=filterservice_ids,
        filtergroup_ids=filtergroup_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include: ListOncallsInclude | Unset = UNSET,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    earliest: bool | Unset = UNSET,
    time_zone: str | Unset = UNSET,
    filterescalation_policy_ids: str | Unset = UNSET,
    filterschedule_ids: str | Unset = UNSET,
    filteruser_ids: str | Unset = UNSET,
    filterservice_ids: str | Unset = UNSET,
    filtergroup_ids: str | Unset = UNSET,
) -> Any | ErrorsList | None:
    """List on-calls

     List who is currently on-call, with support for filtering by escalation policy, schedule, and user.
    Returns on-call entries grouped by escalation policy level.

    Args:
        include (ListOncallsInclude | Unset):
        since (str | Unset):
        until (str | Unset):
        earliest (bool | Unset):
        time_zone (str | Unset):
        filterescalation_policy_ids (str | Unset):
        filterschedule_ids (str | Unset):
        filteruser_ids (str | Unset):
        filterservice_ids (str | Unset):
        filtergroup_ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorsList
    """

    return (
        await asyncio_detailed(
            client=client,
            include=include,
            since=since,
            until=until,
            earliest=earliest,
            time_zone=time_zone,
            filterescalation_policy_ids=filterescalation_policy_ids,
            filterschedule_ids=filterschedule_ids,
            filteruser_ids=filteruser_ids,
            filterservice_ids=filterservice_ids,
            filtergroup_ids=filtergroup_ids,
        )
    ).parsed
