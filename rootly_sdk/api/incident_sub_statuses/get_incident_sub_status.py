from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_incident_sub_status_include import GetIncidentSubStatusInclude
from ...models.incident_sub_status_response import IncidentSubStatusResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    include: Unset | GetIncidentSubStatusInclude = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_include: Unset | str = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/incident_sub_statuses/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IncidentSubStatusResponse | None:
    if response.status_code == 200:
        response_200 = IncidentSubStatusResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IncidentSubStatusResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    include: Unset | GetIncidentSubStatusInclude = UNSET,
) -> Response[IncidentSubStatusResponse]:
    """Retrieves incident_sub_status

     Retrieves a specific incident_sub_status by id

    Args:
        id (str):
        include (Union[Unset, GetIncidentSubStatusInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentSubStatusResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    include: Unset | GetIncidentSubStatusInclude = UNSET,
) -> IncidentSubStatusResponse | None:
    """Retrieves incident_sub_status

     Retrieves a specific incident_sub_status by id

    Args:
        id (str):
        include (Union[Unset, GetIncidentSubStatusInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentSubStatusResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        include=include,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    include: Unset | GetIncidentSubStatusInclude = UNSET,
) -> Response[IncidentSubStatusResponse]:
    """Retrieves incident_sub_status

     Retrieves a specific incident_sub_status by id

    Args:
        id (str):
        include (Union[Unset, GetIncidentSubStatusInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentSubStatusResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    include: Unset | GetIncidentSubStatusInclude = UNSET,
) -> IncidentSubStatusResponse | None:
    """Retrieves incident_sub_status

     Retrieves a specific incident_sub_status by id

    Args:
        id (str):
        include (Union[Unset, GetIncidentSubStatusInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentSubStatusResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            include=include,
        )
    ).parsed
