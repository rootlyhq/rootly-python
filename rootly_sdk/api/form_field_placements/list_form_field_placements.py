from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.form_field_placement_list import FormFieldPlacementList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    form_field_id: str,
    *,
    include: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filterform_field_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include"] = include

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[form_field_id]"] = filterform_field_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/form_fields/{form_field_id}/placements",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[FormFieldPlacementList]:
    if response.status_code == 200:
        response_200 = FormFieldPlacementList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[FormFieldPlacementList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    form_field_id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filterform_field_id: Union[Unset, str] = UNSET,
) -> Response[FormFieldPlacementList]:
    """List Form Field Placements

     List form_field_placements

    Args:
        form_field_id (str):
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterform_field_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FormFieldPlacementList]
    """

    kwargs = _get_kwargs(
        form_field_id=form_field_id,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterform_field_id=filterform_field_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    form_field_id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filterform_field_id: Union[Unset, str] = UNSET,
) -> Optional[FormFieldPlacementList]:
    """List Form Field Placements

     List form_field_placements

    Args:
        form_field_id (str):
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterform_field_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FormFieldPlacementList
    """

    return sync_detailed(
        form_field_id=form_field_id,
        client=client,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterform_field_id=filterform_field_id,
    ).parsed


async def asyncio_detailed(
    form_field_id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filterform_field_id: Union[Unset, str] = UNSET,
) -> Response[FormFieldPlacementList]:
    """List Form Field Placements

     List form_field_placements

    Args:
        form_field_id (str):
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterform_field_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FormFieldPlacementList]
    """

    kwargs = _get_kwargs(
        form_field_id=form_field_id,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterform_field_id=filterform_field_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    form_field_id: str,
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filterform_field_id: Union[Unset, str] = UNSET,
) -> Optional[FormFieldPlacementList]:
    """List Form Field Placements

     List form_field_placements

    Args:
        form_field_id (str):
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterform_field_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FormFieldPlacementList
    """

    return (
        await asyncio_detailed(
            form_field_id=form_field_id,
            client=client,
            include=include,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filterform_field_id=filterform_field_id,
        )
    ).parsed
