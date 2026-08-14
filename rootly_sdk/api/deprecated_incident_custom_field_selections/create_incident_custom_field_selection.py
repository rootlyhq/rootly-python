from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.incident_custom_field_selection_response import IncidentCustomFieldSelectionResponse
from ...models.new_incident_custom_field_selection import NewIncidentCustomFieldSelection
from ...types import Response


def _get_kwargs(
    incident_id: str,
    *,
    body: NewIncidentCustomFieldSelection,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/incidents/{incident_id}/custom_field_selections",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | IncidentCustomFieldSelectionResponse | None:
    if response.status_code == 201:
        response_201 = IncidentCustomFieldSelectionResponse.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = ErrorsList.from_dict(response.json())

        return response_401

    if response.status_code == 422:
        response_422 = ErrorsList.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorsList | IncidentCustomFieldSelectionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    incident_id: str,
    *,
    client: AuthenticatedClient,
    body: NewIncidentCustomFieldSelection,
) -> Response[ErrorsList | IncidentCustomFieldSelectionResponse]:
    """[DEPRECATED] Creates an incident custom field selection

     [DEPRECATED] Use form field endpoints instead. Creates a new incident custom field selection from
    provided data

    Args:
        incident_id (str):
        body (NewIncidentCustomFieldSelection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, IncidentCustomFieldSelectionResponse]]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    incident_id: str,
    *,
    client: AuthenticatedClient,
    body: NewIncidentCustomFieldSelection,
) -> ErrorsList | IncidentCustomFieldSelectionResponse | None:
    """[DEPRECATED] Creates an incident custom field selection

     [DEPRECATED] Use form field endpoints instead. Creates a new incident custom field selection from
    provided data

    Args:
        incident_id (str):
        body (NewIncidentCustomFieldSelection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, IncidentCustomFieldSelectionResponse]
    """

    return sync_detailed(
        incident_id=incident_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    incident_id: str,
    *,
    client: AuthenticatedClient,
    body: NewIncidentCustomFieldSelection,
) -> Response[ErrorsList | IncidentCustomFieldSelectionResponse]:
    """[DEPRECATED] Creates an incident custom field selection

     [DEPRECATED] Use form field endpoints instead. Creates a new incident custom field selection from
    provided data

    Args:
        incident_id (str):
        body (NewIncidentCustomFieldSelection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, IncidentCustomFieldSelectionResponse]]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    incident_id: str,
    *,
    client: AuthenticatedClient,
    body: NewIncidentCustomFieldSelection,
) -> ErrorsList | IncidentCustomFieldSelectionResponse | None:
    """[DEPRECATED] Creates an incident custom field selection

     [DEPRECATED] Use form field endpoints instead. Creates a new incident custom field selection from
    provided data

    Args:
        incident_id (str):
        body (NewIncidentCustomFieldSelection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, IncidentCustomFieldSelectionResponse]
    """

    return (
        await asyncio_detailed(
            incident_id=incident_id,
            client=client,
            body=body,
        )
    ).parsed
