from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.list_oncalls_include import ListOncallsInclude
from ...models.oncall_list import OncallList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: Unset | ListOncallsInclude = UNSET,
    since: Unset | str = UNSET,
    until: Unset | str = UNSET,
    earliest: Unset | bool = UNSET,
    time_zone: Unset | str = UNSET,
    filterescalation_policy_ids: Unset | str = UNSET,
    filterschedule_ids: Unset | str = UNSET,
    filteruser_ids: Unset | str = UNSET,
    filterservice_ids: Unset | str = UNSET,
    filtergroup_ids: Unset | str = UNSET,
    filternotification_types: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_include: Unset | str = UNSET
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

    params["filter[notification_types]"] = filternotification_types

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/oncalls",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | OncallList | None:
    if response.status_code == 200:
        response_200 = OncallList.from_dict(response.json())

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


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorsList | OncallList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include: Unset | ListOncallsInclude = UNSET,
    since: Unset | str = UNSET,
    until: Unset | str = UNSET,
    earliest: Unset | bool = UNSET,
    time_zone: Unset | str = UNSET,
    filterescalation_policy_ids: Unset | str = UNSET,
    filterschedule_ids: Unset | str = UNSET,
    filteruser_ids: Unset | str = UNSET,
    filterservice_ids: Unset | str = UNSET,
    filtergroup_ids: Unset | str = UNSET,
    filternotification_types: Unset | str = UNSET,
) -> Response[ErrorsList | OncallList]:
    """List on-calls

     List who is currently on-call, with support for filtering by escalation policy, schedule, and user.
    Returns on-call entries grouped by escalation policy level.

    Args:
        include (Union[Unset, ListOncallsInclude]):
        since (Union[Unset, str]):
        until (Union[Unset, str]):
        earliest (Union[Unset, bool]):
        time_zone (Union[Unset, str]):
        filterescalation_policy_ids (Union[Unset, str]):
        filterschedule_ids (Union[Unset, str]):
        filteruser_ids (Union[Unset, str]):
        filterservice_ids (Union[Unset, str]):
        filtergroup_ids (Union[Unset, str]):
        filternotification_types (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, OncallList]]
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
        filternotification_types=filternotification_types,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    include: Unset | ListOncallsInclude = UNSET,
    since: Unset | str = UNSET,
    until: Unset | str = UNSET,
    earliest: Unset | bool = UNSET,
    time_zone: Unset | str = UNSET,
    filterescalation_policy_ids: Unset | str = UNSET,
    filterschedule_ids: Unset | str = UNSET,
    filteruser_ids: Unset | str = UNSET,
    filterservice_ids: Unset | str = UNSET,
    filtergroup_ids: Unset | str = UNSET,
    filternotification_types: Unset | str = UNSET,
) -> ErrorsList | OncallList | None:
    """List on-calls

     List who is currently on-call, with support for filtering by escalation policy, schedule, and user.
    Returns on-call entries grouped by escalation policy level.

    Args:
        include (Union[Unset, ListOncallsInclude]):
        since (Union[Unset, str]):
        until (Union[Unset, str]):
        earliest (Union[Unset, bool]):
        time_zone (Union[Unset, str]):
        filterescalation_policy_ids (Union[Unset, str]):
        filterschedule_ids (Union[Unset, str]):
        filteruser_ids (Union[Unset, str]):
        filterservice_ids (Union[Unset, str]):
        filtergroup_ids (Union[Unset, str]):
        filternotification_types (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, OncallList]
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
        filternotification_types=filternotification_types,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: Unset | ListOncallsInclude = UNSET,
    since: Unset | str = UNSET,
    until: Unset | str = UNSET,
    earliest: Unset | bool = UNSET,
    time_zone: Unset | str = UNSET,
    filterescalation_policy_ids: Unset | str = UNSET,
    filterschedule_ids: Unset | str = UNSET,
    filteruser_ids: Unset | str = UNSET,
    filterservice_ids: Unset | str = UNSET,
    filtergroup_ids: Unset | str = UNSET,
    filternotification_types: Unset | str = UNSET,
) -> Response[ErrorsList | OncallList]:
    """List on-calls

     List who is currently on-call, with support for filtering by escalation policy, schedule, and user.
    Returns on-call entries grouped by escalation policy level.

    Args:
        include (Union[Unset, ListOncallsInclude]):
        since (Union[Unset, str]):
        until (Union[Unset, str]):
        earliest (Union[Unset, bool]):
        time_zone (Union[Unset, str]):
        filterescalation_policy_ids (Union[Unset, str]):
        filterschedule_ids (Union[Unset, str]):
        filteruser_ids (Union[Unset, str]):
        filterservice_ids (Union[Unset, str]):
        filtergroup_ids (Union[Unset, str]):
        filternotification_types (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, OncallList]]
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
        filternotification_types=filternotification_types,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include: Unset | ListOncallsInclude = UNSET,
    since: Unset | str = UNSET,
    until: Unset | str = UNSET,
    earliest: Unset | bool = UNSET,
    time_zone: Unset | str = UNSET,
    filterescalation_policy_ids: Unset | str = UNSET,
    filterschedule_ids: Unset | str = UNSET,
    filteruser_ids: Unset | str = UNSET,
    filterservice_ids: Unset | str = UNSET,
    filtergroup_ids: Unset | str = UNSET,
    filternotification_types: Unset | str = UNSET,
) -> ErrorsList | OncallList | None:
    """List on-calls

     List who is currently on-call, with support for filtering by escalation policy, schedule, and user.
    Returns on-call entries grouped by escalation policy level.

    Args:
        include (Union[Unset, ListOncallsInclude]):
        since (Union[Unset, str]):
        until (Union[Unset, str]):
        earliest (Union[Unset, bool]):
        time_zone (Union[Unset, str]):
        filterescalation_policy_ids (Union[Unset, str]):
        filterschedule_ids (Union[Unset, str]):
        filteruser_ids (Union[Unset, str]):
        filterservice_ids (Union[Unset, str]):
        filtergroup_ids (Union[Unset, str]):
        filternotification_types (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, OncallList]
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
            filternotification_types=filternotification_types,
        )
    ).parsed
