from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_configuration_response import AlertConfigurationResponse
from ...models.errors_list import ErrorsList
from ...models.update_alert_configuration import UpdateAlertConfiguration
from ...types import Response


def _get_kwargs(
    *,
    body: UpdateAlertConfiguration,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/alert_configuration",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlertConfigurationResponse | ErrorsList | None:
    if response.status_code == 200:
        response_200 = AlertConfigurationResponse.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = ErrorsList.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorsList.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ErrorsList.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AlertConfigurationResponse | ErrorsList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateAlertConfiguration,
) -> Response[AlertConfigurationResponse | ErrorsList]:
    """Updates the team's alert configuration

    Args:
        body (UpdateAlertConfiguration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertConfigurationResponse | ErrorsList]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: UpdateAlertConfiguration,
) -> AlertConfigurationResponse | ErrorsList | None:
    """Updates the team's alert configuration

    Args:
        body (UpdateAlertConfiguration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertConfigurationResponse | ErrorsList
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateAlertConfiguration,
) -> Response[AlertConfigurationResponse | ErrorsList]:
    """Updates the team's alert configuration

    Args:
        body (UpdateAlertConfiguration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertConfigurationResponse | ErrorsList]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UpdateAlertConfiguration,
) -> AlertConfigurationResponse | ErrorsList | None:
    """Updates the team's alert configuration

    Args:
        body (UpdateAlertConfiguration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertConfigurationResponse | ErrorsList
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
