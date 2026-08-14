from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_custom_field_selection_list import IncidentCustomFieldSelectionList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    incident_id: str,
    *,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include"] = include

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/incidents/{incident_id}/custom_field_selections",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IncidentCustomFieldSelectionList | None:
    if response.status_code == 200:
        response_200 = IncidentCustomFieldSelectionList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IncidentCustomFieldSelectionList]:
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
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
) -> Response[IncidentCustomFieldSelectionList]:
    """[DEPRECATED] List incident custom field selections

     [DEPRECATED] Use form field endpoints instead. List incident custom field selections

    Args:
        incident_id (str):
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentCustomFieldSelectionList]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    incident_id: str,
    *,
    client: AuthenticatedClient,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
) -> IncidentCustomFieldSelectionList | None:
    """[DEPRECATED] List incident custom field selections

     [DEPRECATED] Use form field endpoints instead. List incident custom field selections

    Args:
        incident_id (str):
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentCustomFieldSelectionList
    """

    return sync_detailed(
        incident_id=incident_id,
        client=client,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
    ).parsed


async def asyncio_detailed(
    incident_id: str,
    *,
    client: AuthenticatedClient,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
) -> Response[IncidentCustomFieldSelectionList]:
    """[DEPRECATED] List incident custom field selections

     [DEPRECATED] Use form field endpoints instead. List incident custom field selections

    Args:
        incident_id (str):
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentCustomFieldSelectionList]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    incident_id: str,
    *,
    client: AuthenticatedClient,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
) -> IncidentCustomFieldSelectionList | None:
    """[DEPRECATED] List incident custom field selections

     [DEPRECATED] Use form field endpoints instead. List incident custom field selections

    Args:
        incident_id (str):
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentCustomFieldSelectionList
    """

    return (
        await asyncio_detailed(
            incident_id=incident_id,
            client=client,
            include=include,
            pagenumber=pagenumber,
            pagesize=pagesize,
        )
    ).parsed
