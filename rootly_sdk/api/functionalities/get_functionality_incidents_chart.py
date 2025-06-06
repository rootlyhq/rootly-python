from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.incidents_chart_response import IncidentsChartResponse
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    *,
    period: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["period"] = period

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/functionalities/{id}/incidents_chart",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorsList, IncidentsChartResponse]]:
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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorsList, IncidentsChartResponse]]:
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
    period: str,
) -> Response[Union[ErrorsList, IncidentsChartResponse]]:
    """Get functionality incidents chart

     Get functionality incidents chart

    Args:
        id (str):
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
    id: str,
    *,
    client: AuthenticatedClient,
    period: str,
) -> Optional[Union[ErrorsList, IncidentsChartResponse]]:
    """Get functionality incidents chart

     Get functionality incidents chart

    Args:
        id (str):
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
    id: str,
    *,
    client: AuthenticatedClient,
    period: str,
) -> Response[Union[ErrorsList, IncidentsChartResponse]]:
    """Get functionality incidents chart

     Get functionality incidents chart

    Args:
        id (str):
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
    id: str,
    *,
    client: AuthenticatedClient,
    period: str,
) -> Optional[Union[ErrorsList, IncidentsChartResponse]]:
    """Get functionality incidents chart

     Get functionality incidents chart

    Args:
        id (str):
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
