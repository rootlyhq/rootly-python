from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_field_option_response import CustomFieldOptionResponse
from ...models.errors_list import ErrorsList
from ...models.update_custom_field_option import UpdateCustomFieldOption
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateCustomFieldOption,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/v1/custom_field_options/{id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CustomFieldOptionResponse | ErrorsList | None:
    if response.status_code == 200:
        response_200 = CustomFieldOptionResponse.from_dict(response.json())

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
) -> Response[CustomFieldOptionResponse | ErrorsList]:
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
    body: UpdateCustomFieldOption,
) -> Response[CustomFieldOptionResponse | ErrorsList]:
    """[DEPRECATED] Update a custom field option

     [DEPRECATED] Use form field endpoints instead. Update a specific custom field option by id

    Args:
        id (str):
        body (UpdateCustomFieldOption):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomFieldOptionResponse, ErrorsList]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCustomFieldOption,
) -> CustomFieldOptionResponse | ErrorsList | None:
    """[DEPRECATED] Update a custom field option

     [DEPRECATED] Use form field endpoints instead. Update a specific custom field option by id

    Args:
        id (str):
        body (UpdateCustomFieldOption):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CustomFieldOptionResponse, ErrorsList]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCustomFieldOption,
) -> Response[CustomFieldOptionResponse | ErrorsList]:
    """[DEPRECATED] Update a custom field option

     [DEPRECATED] Use form field endpoints instead. Update a specific custom field option by id

    Args:
        id (str):
        body (UpdateCustomFieldOption):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomFieldOptionResponse, ErrorsList]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCustomFieldOption,
) -> CustomFieldOptionResponse | ErrorsList | None:
    """[DEPRECATED] Update a custom field option

     [DEPRECATED] Use form field endpoints instead. Update a specific custom field option by id

    Args:
        id (str):
        body (UpdateCustomFieldOption):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CustomFieldOptionResponse, ErrorsList]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
