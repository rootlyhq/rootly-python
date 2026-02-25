from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dashboard_panel_response import DashboardPanelResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    range_: Unset | str = UNSET,
    period: Unset | str = UNSET,
    time_zone: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["range"] = range_

    params["period"] = period

    params["time_zone"] = time_zone

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/dashboard_panels/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DashboardPanelResponse | None:
    if response.status_code == 200:
        response_200 = DashboardPanelResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DashboardPanelResponse]:
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
    range_: Unset | str = UNSET,
    period: Unset | str = UNSET,
    time_zone: Unset | str = UNSET,
) -> Response[DashboardPanelResponse]:
    """Retrieves a dashboard panel

     Retrieves a specific dashboard panel by id

    Args:
        id (str):
        range_ (Union[Unset, str]):
        period (Union[Unset, str]):
        time_zone (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DashboardPanelResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        range_=range_,
        period=period,
        time_zone=time_zone,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    range_: Unset | str = UNSET,
    period: Unset | str = UNSET,
    time_zone: Unset | str = UNSET,
) -> DashboardPanelResponse | None:
    """Retrieves a dashboard panel

     Retrieves a specific dashboard panel by id

    Args:
        id (str):
        range_ (Union[Unset, str]):
        period (Union[Unset, str]):
        time_zone (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DashboardPanelResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        range_=range_,
        period=period,
        time_zone=time_zone,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    range_: Unset | str = UNSET,
    period: Unset | str = UNSET,
    time_zone: Unset | str = UNSET,
) -> Response[DashboardPanelResponse]:
    """Retrieves a dashboard panel

     Retrieves a specific dashboard panel by id

    Args:
        id (str):
        range_ (Union[Unset, str]):
        period (Union[Unset, str]):
        time_zone (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DashboardPanelResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        range_=range_,
        period=period,
        time_zone=time_zone,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    range_: Unset | str = UNSET,
    period: Unset | str = UNSET,
    time_zone: Unset | str = UNSET,
) -> DashboardPanelResponse | None:
    """Retrieves a dashboard panel

     Retrieves a specific dashboard panel by id

    Args:
        id (str):
        range_ (Union[Unset, str]):
        period (Union[Unset, str]):
        time_zone (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DashboardPanelResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            range_=range_,
            period=period,
            time_zone=time_zone,
        )
    ).parsed
