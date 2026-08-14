from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    message: str,
    session_id: Unset | UUID = UNSET,
    incident_id: Unset | UUID = UNSET,
    alert_id: Unset | UUID = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["message"] = message

    json_session_id: Unset | str = UNSET
    if not isinstance(session_id, Unset):
        json_session_id = str(session_id)
    params["session_id"] = json_session_id

    json_incident_id: Unset | str = UNSET
    if not isinstance(incident_id, Unset):
        json_incident_id = str(incident_id)
    params["incident_id"] = json_incident_id

    json_alert_id: Unset | str = UNSET
    if not isinstance(alert_id, Unset):
        json_alert_id = str(alert_id)
    params["alert_id"] = json_alert_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/ai/chat/stream",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 403:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    message: str,
    session_id: Unset | UUID = UNSET,
    incident_id: Unset | UUID = UNSET,
    alert_id: Unset | UUID = UNSET,
) -> Response[Any]:
    """Stream AI chat response (SSE)

     Send a message and receive the AI response as a Server-Sent Events stream. Optionally bind to an
    incident or alert for context. Events: `session_id` (initial), `text` (content chunks),
    `task_update` (tool progress), `error`, `done` (terminal with status). Requires `ai.chat:write`
    OAuth scope or an API key.

    Args:
        message (str):
        session_id (Union[Unset, UUID]):
        incident_id (Union[Unset, UUID]):
        alert_id (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        message=message,
        session_id=session_id,
        incident_id=incident_id,
        alert_id=alert_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    message: str,
    session_id: Unset | UUID = UNSET,
    incident_id: Unset | UUID = UNSET,
    alert_id: Unset | UUID = UNSET,
) -> Response[Any]:
    """Stream AI chat response (SSE)

     Send a message and receive the AI response as a Server-Sent Events stream. Optionally bind to an
    incident or alert for context. Events: `session_id` (initial), `text` (content chunks),
    `task_update` (tool progress), `error`, `done` (terminal with status). Requires `ai.chat:write`
    OAuth scope or an API key.

    Args:
        message (str):
        session_id (Union[Unset, UUID]):
        incident_id (Union[Unset, UUID]):
        alert_id (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        message=message,
        session_id=session_id,
        incident_id=incident_id,
        alert_id=alert_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
