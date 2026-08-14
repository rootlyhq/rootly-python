from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_key_list import ApiKeyList
from ...models.errors_list import ErrorsList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filterkind: Union[Unset, str] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    filteruser_id: Union[Unset, str] = UNSET,
    filtergroup_ids: Union[Unset, str] = UNSET,
    filterrole_id: Union[Unset, str] = UNSET,
    filteractive: Union[Unset, bool] = UNSET,
    filterexpired: Union[Unset, bool] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterexpires_atgt: Union[Unset, str] = UNSET,
    filterexpires_atgte: Union[Unset, str] = UNSET,
    filterexpires_atlt: Union[Unset, str] = UNSET,
    filterexpires_atlte: Union[Unset, str] = UNSET,
    filterlast_used_atgt: Union[Unset, str] = UNSET,
    filterlast_used_atgte: Union[Unset, str] = UNSET,
    filterlast_used_atlt: Union[Unset, str] = UNSET,
    filterlast_used_atlte: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include"] = include

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[kind]"] = filterkind

    params["filter[search]"] = filtersearch

    params["filter[name]"] = filtername

    params["filter[user_id]"] = filteruser_id

    params["filter[group_ids]"] = filtergroup_ids

    params["filter[role_id]"] = filterrole_id

    params["filter[active]"] = filteractive

    params["filter[expired]"] = filterexpired

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params["filter[expires_at][gt]"] = filterexpires_atgt

    params["filter[expires_at][gte]"] = filterexpires_atgte

    params["filter[expires_at][lt]"] = filterexpires_atlt

    params["filter[expires_at][lte]"] = filterexpires_atlte

    params["filter[last_used_at][gt]"] = filterlast_used_atgt

    params["filter[last_used_at][gte]"] = filterlast_used_atgte

    params["filter[last_used_at][lt]"] = filterlast_used_atlt

    params["filter[last_used_at][lte]"] = filterlast_used_atlte

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/api_keys",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiKeyList, ErrorsList]]:
    if response.status_code == 200:
        response_200 = ApiKeyList.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorsList.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiKeyList, ErrorsList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filterkind: Union[Unset, str] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    filteruser_id: Union[Unset, str] = UNSET,
    filtergroup_ids: Union[Unset, str] = UNSET,
    filterrole_id: Union[Unset, str] = UNSET,
    filteractive: Union[Unset, bool] = UNSET,
    filterexpired: Union[Unset, bool] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterexpires_atgt: Union[Unset, str] = UNSET,
    filterexpires_atgte: Union[Unset, str] = UNSET,
    filterexpires_atlt: Union[Unset, str] = UNSET,
    filterexpires_atlte: Union[Unset, str] = UNSET,
    filterlast_used_atgt: Union[Unset, str] = UNSET,
    filterlast_used_atgte: Union[Unset, str] = UNSET,
    filterlast_used_atlt: Union[Unset, str] = UNSET,
    filterlast_used_atlte: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[Union[ApiKeyList, ErrorsList]]:
    """List API keys

     List API keys for the current organization. Returns key metadata including name, kind, expiration,
    and last usage — the secret token value is never included in the response.

    **API key kinds:**
    - `personal` — tied to a specific user, inherits that user's permissions.
    - `team` — scoped to one or more teams (groups), creates a service account with permissions derived
    from group membership.
    - `organization` — organization-wide, creates a service account with a configurable role and on-call
    role.

    **Automated rotation workflow:** Use `filter[expires_at][lt]` to find keys approaching expiration,
    then call the rotate endpoint to issue a new token before the old one expires. Combine with
    `filter[active]=true` to exclude already-expired keys.

    **Sorting:** Use the `sort` parameter with a field name (e.g., `sort=expires_at`). Prefix with `-`
    for descending order (e.g., `sort=-created_at`). Allowed fields: `name`, `kind`, `created_at`,
    `updated_at`, `expires_at`, `last_used_at`.

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterkind (Union[Unset, str]):
        filtersearch (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filteruser_id (Union[Unset, str]):
        filtergroup_ids (Union[Unset, str]):
        filterrole_id (Union[Unset, str]):
        filteractive (Union[Unset, bool]):
        filterexpired (Union[Unset, bool]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterexpires_atgt (Union[Unset, str]):
        filterexpires_atgte (Union[Unset, str]):
        filterexpires_atlt (Union[Unset, str]):
        filterexpires_atlte (Union[Unset, str]):
        filterlast_used_atgt (Union[Unset, str]):
        filterlast_used_atgte (Union[Unset, str]):
        filterlast_used_atlt (Union[Unset, str]):
        filterlast_used_atlte (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiKeyList, ErrorsList]]
    """

    kwargs = _get_kwargs(
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterkind=filterkind,
        filtersearch=filtersearch,
        filtername=filtername,
        filteruser_id=filteruser_id,
        filtergroup_ids=filtergroup_ids,
        filterrole_id=filterrole_id,
        filteractive=filteractive,
        filterexpired=filterexpired,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterexpires_atgt=filterexpires_atgt,
        filterexpires_atgte=filterexpires_atgte,
        filterexpires_atlt=filterexpires_atlt,
        filterexpires_atlte=filterexpires_atlte,
        filterlast_used_atgt=filterlast_used_atgt,
        filterlast_used_atgte=filterlast_used_atgte,
        filterlast_used_atlt=filterlast_used_atlt,
        filterlast_used_atlte=filterlast_used_atlte,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filterkind: Union[Unset, str] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    filteruser_id: Union[Unset, str] = UNSET,
    filtergroup_ids: Union[Unset, str] = UNSET,
    filterrole_id: Union[Unset, str] = UNSET,
    filteractive: Union[Unset, bool] = UNSET,
    filterexpired: Union[Unset, bool] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterexpires_atgt: Union[Unset, str] = UNSET,
    filterexpires_atgte: Union[Unset, str] = UNSET,
    filterexpires_atlt: Union[Unset, str] = UNSET,
    filterexpires_atlte: Union[Unset, str] = UNSET,
    filterlast_used_atgt: Union[Unset, str] = UNSET,
    filterlast_used_atgte: Union[Unset, str] = UNSET,
    filterlast_used_atlt: Union[Unset, str] = UNSET,
    filterlast_used_atlte: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[Union[ApiKeyList, ErrorsList]]:
    """List API keys

     List API keys for the current organization. Returns key metadata including name, kind, expiration,
    and last usage — the secret token value is never included in the response.

    **API key kinds:**
    - `personal` — tied to a specific user, inherits that user's permissions.
    - `team` — scoped to one or more teams (groups), creates a service account with permissions derived
    from group membership.
    - `organization` — organization-wide, creates a service account with a configurable role and on-call
    role.

    **Automated rotation workflow:** Use `filter[expires_at][lt]` to find keys approaching expiration,
    then call the rotate endpoint to issue a new token before the old one expires. Combine with
    `filter[active]=true` to exclude already-expired keys.

    **Sorting:** Use the `sort` parameter with a field name (e.g., `sort=expires_at`). Prefix with `-`
    for descending order (e.g., `sort=-created_at`). Allowed fields: `name`, `kind`, `created_at`,
    `updated_at`, `expires_at`, `last_used_at`.

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterkind (Union[Unset, str]):
        filtersearch (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filteruser_id (Union[Unset, str]):
        filtergroup_ids (Union[Unset, str]):
        filterrole_id (Union[Unset, str]):
        filteractive (Union[Unset, bool]):
        filterexpired (Union[Unset, bool]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterexpires_atgt (Union[Unset, str]):
        filterexpires_atgte (Union[Unset, str]):
        filterexpires_atlt (Union[Unset, str]):
        filterexpires_atlte (Union[Unset, str]):
        filterlast_used_atgt (Union[Unset, str]):
        filterlast_used_atgte (Union[Unset, str]):
        filterlast_used_atlt (Union[Unset, str]):
        filterlast_used_atlte (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiKeyList, ErrorsList]
    """

    return sync_detailed(
        client=client,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterkind=filterkind,
        filtersearch=filtersearch,
        filtername=filtername,
        filteruser_id=filteruser_id,
        filtergroup_ids=filtergroup_ids,
        filterrole_id=filterrole_id,
        filteractive=filteractive,
        filterexpired=filterexpired,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterexpires_atgt=filterexpires_atgt,
        filterexpires_atgte=filterexpires_atgte,
        filterexpires_atlt=filterexpires_atlt,
        filterexpires_atlte=filterexpires_atlte,
        filterlast_used_atgt=filterlast_used_atgt,
        filterlast_used_atgte=filterlast_used_atgte,
        filterlast_used_atlt=filterlast_used_atlt,
        filterlast_used_atlte=filterlast_used_atlte,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filterkind: Union[Unset, str] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    filteruser_id: Union[Unset, str] = UNSET,
    filtergroup_ids: Union[Unset, str] = UNSET,
    filterrole_id: Union[Unset, str] = UNSET,
    filteractive: Union[Unset, bool] = UNSET,
    filterexpired: Union[Unset, bool] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterexpires_atgt: Union[Unset, str] = UNSET,
    filterexpires_atgte: Union[Unset, str] = UNSET,
    filterexpires_atlt: Union[Unset, str] = UNSET,
    filterexpires_atlte: Union[Unset, str] = UNSET,
    filterlast_used_atgt: Union[Unset, str] = UNSET,
    filterlast_used_atgte: Union[Unset, str] = UNSET,
    filterlast_used_atlt: Union[Unset, str] = UNSET,
    filterlast_used_atlte: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Response[Union[ApiKeyList, ErrorsList]]:
    """List API keys

     List API keys for the current organization. Returns key metadata including name, kind, expiration,
    and last usage — the secret token value is never included in the response.

    **API key kinds:**
    - `personal` — tied to a specific user, inherits that user's permissions.
    - `team` — scoped to one or more teams (groups), creates a service account with permissions derived
    from group membership.
    - `organization` — organization-wide, creates a service account with a configurable role and on-call
    role.

    **Automated rotation workflow:** Use `filter[expires_at][lt]` to find keys approaching expiration,
    then call the rotate endpoint to issue a new token before the old one expires. Combine with
    `filter[active]=true` to exclude already-expired keys.

    **Sorting:** Use the `sort` parameter with a field name (e.g., `sort=expires_at`). Prefix with `-`
    for descending order (e.g., `sort=-created_at`). Allowed fields: `name`, `kind`, `created_at`,
    `updated_at`, `expires_at`, `last_used_at`.

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterkind (Union[Unset, str]):
        filtersearch (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filteruser_id (Union[Unset, str]):
        filtergroup_ids (Union[Unset, str]):
        filterrole_id (Union[Unset, str]):
        filteractive (Union[Unset, bool]):
        filterexpired (Union[Unset, bool]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterexpires_atgt (Union[Unset, str]):
        filterexpires_atgte (Union[Unset, str]):
        filterexpires_atlt (Union[Unset, str]):
        filterexpires_atlte (Union[Unset, str]):
        filterlast_used_atgt (Union[Unset, str]):
        filterlast_used_atgte (Union[Unset, str]):
        filterlast_used_atlt (Union[Unset, str]):
        filterlast_used_atlte (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiKeyList, ErrorsList]]
    """

    kwargs = _get_kwargs(
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterkind=filterkind,
        filtersearch=filtersearch,
        filtername=filtername,
        filteruser_id=filteruser_id,
        filtergroup_ids=filtergroup_ids,
        filterrole_id=filterrole_id,
        filteractive=filteractive,
        filterexpired=filterexpired,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterexpires_atgt=filterexpires_atgt,
        filterexpires_atgte=filterexpires_atgte,
        filterexpires_atlt=filterexpires_atlt,
        filterexpires_atlte=filterexpires_atlte,
        filterlast_used_atgt=filterlast_used_atgt,
        filterlast_used_atgte=filterlast_used_atgte,
        filterlast_used_atlt=filterlast_used_atlt,
        filterlast_used_atlte=filterlast_used_atlte,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filterkind: Union[Unset, str] = UNSET,
    filtersearch: Union[Unset, str] = UNSET,
    filtername: Union[Unset, str] = UNSET,
    filteruser_id: Union[Unset, str] = UNSET,
    filtergroup_ids: Union[Unset, str] = UNSET,
    filterrole_id: Union[Unset, str] = UNSET,
    filteractive: Union[Unset, bool] = UNSET,
    filterexpired: Union[Unset, bool] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterexpires_atgt: Union[Unset, str] = UNSET,
    filterexpires_atgte: Union[Unset, str] = UNSET,
    filterexpires_atlt: Union[Unset, str] = UNSET,
    filterexpires_atlte: Union[Unset, str] = UNSET,
    filterlast_used_atgt: Union[Unset, str] = UNSET,
    filterlast_used_atgte: Union[Unset, str] = UNSET,
    filterlast_used_atlt: Union[Unset, str] = UNSET,
    filterlast_used_atlte: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
) -> Optional[Union[ApiKeyList, ErrorsList]]:
    """List API keys

     List API keys for the current organization. Returns key metadata including name, kind, expiration,
    and last usage — the secret token value is never included in the response.

    **API key kinds:**
    - `personal` — tied to a specific user, inherits that user's permissions.
    - `team` — scoped to one or more teams (groups), creates a service account with permissions derived
    from group membership.
    - `organization` — organization-wide, creates a service account with a configurable role and on-call
    role.

    **Automated rotation workflow:** Use `filter[expires_at][lt]` to find keys approaching expiration,
    then call the rotate endpoint to issue a new token before the old one expires. Combine with
    `filter[active]=true` to exclude already-expired keys.

    **Sorting:** Use the `sort` parameter with a field name (e.g., `sort=expires_at`). Prefix with `-`
    for descending order (e.g., `sort=-created_at`). Allowed fields: `name`, `kind`, `created_at`,
    `updated_at`, `expires_at`, `last_used_at`.

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filterkind (Union[Unset, str]):
        filtersearch (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filteruser_id (Union[Unset, str]):
        filtergroup_ids (Union[Unset, str]):
        filterrole_id (Union[Unset, str]):
        filteractive (Union[Unset, bool]):
        filterexpired (Union[Unset, bool]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterexpires_atgt (Union[Unset, str]):
        filterexpires_atgte (Union[Unset, str]):
        filterexpires_atlt (Union[Unset, str]):
        filterexpires_atlte (Union[Unset, str]):
        filterlast_used_atgt (Union[Unset, str]):
        filterlast_used_atgte (Union[Unset, str]):
        filterlast_used_atlt (Union[Unset, str]):
        filterlast_used_atlte (Union[Unset, str]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiKeyList, ErrorsList]
    """

    return (
        await asyncio_detailed(
            client=client,
            include=include,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filterkind=filterkind,
            filtersearch=filtersearch,
            filtername=filtername,
            filteruser_id=filteruser_id,
            filtergroup_ids=filtergroup_ids,
            filterrole_id=filterrole_id,
            filteractive=filteractive,
            filterexpired=filterexpired,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
            filterexpires_atgt=filterexpires_atgt,
            filterexpires_atgte=filterexpires_atgte,
            filterexpires_atlt=filterexpires_atlt,
            filterexpires_atlte=filterexpires_atlte,
            filterlast_used_atgt=filterlast_used_atgt,
            filterlast_used_atgte=filterlast_used_atgte,
            filterlast_used_atlt=filterlast_used_atlt,
            filterlast_used_atlte=filterlast_used_atlte,
            sort=sort,
        )
    ).parsed
