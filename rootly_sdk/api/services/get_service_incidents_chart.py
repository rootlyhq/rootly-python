from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.incidents_chart_response import IncidentsChartResponse
from ...types import UNSET, Response


def _get_kwargs(
    id: UUID | str,
    *,
    period: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["period"] = period

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/services/{id}/incidents_chart",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | IncidentsChartResponse | None:
    if response.status_code == 200:
        response_200 = IncidentsChartResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorsList.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorsList | IncidentsChartResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID | str,
    *,
    client: AuthenticatedClient,
    period: str,
) -> Response[ErrorsList | IncidentsChartResponse]:
    """Get service incidents chart

     Get service incidents chart

    Args:
        id (Union[UUID, str]):
        period (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, IncidentsChartResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        period=period,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID | str,
    *,
    client: AuthenticatedClient,
    period: str,
) -> ErrorsList | IncidentsChartResponse | None:
    """Get service incidents chart

     Get service incidents chart

    Args:
        id (Union[UUID, str]):
        period (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, IncidentsChartResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        period=period,
    ).parsed


async def asyncio_detailed(
    id: UUID | str,
    *,
    client: AuthenticatedClient,
    period: str,
) -> Response[ErrorsList | IncidentsChartResponse]:
    """Get service incidents chart

     Get service incidents chart

    Args:
        id (Union[UUID, str]):
        period (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, IncidentsChartResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        period=period,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID | str,
    *,
    client: AuthenticatedClient,
    period: str,
) -> ErrorsList | IncidentsChartResponse | None:
    """Get service incidents chart

     Get service incidents chart

    Args:
        id (Union[UUID, str]):
        period (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, IncidentsChartResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            period=period,
        )
    ).parsed
