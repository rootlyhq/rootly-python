from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_field_option_response import CustomFieldOptionResponse
from ...models.errors_list import ErrorsList
from ...models.new_custom_field_option import NewCustomFieldOption
from ...types import Response


def _get_kwargs(
    custom_field_id: str,
    *,
    body: NewCustomFieldOption,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/custom_fields/{custom_field_id}/options",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CustomFieldOptionResponse | ErrorsList | None:
    if response.status_code == 201:
        response_201 = CustomFieldOptionResponse.from_dict(response.json())

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
) -> Response[CustomFieldOptionResponse | ErrorsList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    custom_field_id: str,
    *,
    client: AuthenticatedClient,
    body: NewCustomFieldOption,
) -> Response[CustomFieldOptionResponse | ErrorsList]:
    """[DEPRECATED] Creates a custom field option

     [DEPRECATED] Use form field endpoints instead. Creates a new custom field option from provided data

    Args:
        custom_field_id (str):
        body (NewCustomFieldOption):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomFieldOptionResponse, ErrorsList]]
    """

    kwargs = _get_kwargs(
        custom_field_id=custom_field_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    custom_field_id: str,
    *,
    client: AuthenticatedClient,
    body: NewCustomFieldOption,
) -> CustomFieldOptionResponse | ErrorsList | None:
    """[DEPRECATED] Creates a custom field option

     [DEPRECATED] Use form field endpoints instead. Creates a new custom field option from provided data

    Args:
        custom_field_id (str):
        body (NewCustomFieldOption):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CustomFieldOptionResponse, ErrorsList]
    """

    return sync_detailed(
        custom_field_id=custom_field_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    custom_field_id: str,
    *,
    client: AuthenticatedClient,
    body: NewCustomFieldOption,
) -> Response[CustomFieldOptionResponse | ErrorsList]:
    """[DEPRECATED] Creates a custom field option

     [DEPRECATED] Use form field endpoints instead. Creates a new custom field option from provided data

    Args:
        custom_field_id (str):
        body (NewCustomFieldOption):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomFieldOptionResponse, ErrorsList]]
    """

    kwargs = _get_kwargs(
        custom_field_id=custom_field_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    custom_field_id: str,
    *,
    client: AuthenticatedClient,
    body: NewCustomFieldOption,
) -> CustomFieldOptionResponse | ErrorsList | None:
    """[DEPRECATED] Creates a custom field option

     [DEPRECATED] Use form field endpoints instead. Creates a new custom field option from provided data

    Args:
        custom_field_id (str):
        body (NewCustomFieldOption):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CustomFieldOptionResponse, ErrorsList]
    """

    return (
        await asyncio_detailed(
            custom_field_id=custom_field_id,
            client=client,
            body=body,
        )
    ).parsed
