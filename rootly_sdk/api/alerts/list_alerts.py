from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_list import AlertList
from ...models.list_alerts_include import ListAlertsInclude
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: Union[Unset, ListAlertsInclude] = UNSET,
    filterstatus: Union[Unset, str] = UNSET,
    filtersource: Union[Unset, str] = UNSET,
    filterservices: Union[Unset, str] = UNSET,
    filterenvironments: Union[Unset, str] = UNSET,
    filtergroups: Union[Unset, str] = UNSET,
    filterlabels: Union[Unset, str] = UNSET,
    filterstarted_atgt: Union[Unset, str] = UNSET,
    filterstarted_atgte: Union[Unset, str] = UNSET,
    filterstarted_atlt: Union[Unset, str] = UNSET,
    filterstarted_atlte: Union[Unset, str] = UNSET,
    filterended_atgt: Union[Unset, str] = UNSET,
    filterended_atgte: Union[Unset, str] = UNSET,
    filterended_atlt: Union[Unset, str] = UNSET,
    filterended_atlte: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterupdated_atgt: Union[Unset, str] = UNSET,
    filterupdated_atgte: Union[Unset, str] = UNSET,
    filterupdated_atlt: Union[Unset, str] = UNSET,
    filterupdated_atlte: Union[Unset, str] = UNSET,
    filterstatuseq: Union[Unset, str] = UNSET,
    filterstatusnot_eq: Union[Unset, str] = UNSET,
    filterstatusin: Union[Unset, str] = UNSET,
    filterstatusnot_in: Union[Unset, str] = UNSET,
    filtersourceeq: Union[Unset, str] = UNSET,
    filtersourcenot_eq: Union[Unset, str] = UNSET,
    filtersourcein: Union[Unset, str] = UNSET,
    filtersourcenot_in: Union[Unset, str] = UNSET,
    filterserviceseq: Union[Unset, str] = UNSET,
    filterservicesnot_eq: Union[Unset, str] = UNSET,
    filterservicesin: Union[Unset, str] = UNSET,
    filterservicesnot_in: Union[Unset, str] = UNSET,
    filtergroupseq: Union[Unset, str] = UNSET,
    filtergroupsnot_eq: Union[Unset, str] = UNSET,
    filtergroupsin: Union[Unset, str] = UNSET,
    filtergroupsnot_in: Union[Unset, str] = UNSET,
    filterenvironmentseq: Union[Unset, str] = UNSET,
    filterenvironmentsnot_eq: Union[Unset, str] = UNSET,
    filterenvironmentsin: Union[Unset, str] = UNSET,
    filterenvironmentsnot_in: Union[Unset, str] = UNSET,
    filterlabelseq: Union[Unset, str] = UNSET,
    filterlabelsnot_eq: Union[Unset, str] = UNSET,
    filterlabelsin: Union[Unset, str] = UNSET,
    filterlabelsnot_in: Union[Unset, str] = UNSET,
    pageafter: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_include: Union[Unset, str] = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    params["filter[status]"] = filterstatus

    params["filter[source]"] = filtersource

    params["filter[services]"] = filterservices

    params["filter[environments]"] = filterenvironments

    params["filter[groups]"] = filtergroups

    params["filter[labels]"] = filterlabels

    params["filter[started_at][gt]"] = filterstarted_atgt

    params["filter[started_at][gte]"] = filterstarted_atgte

    params["filter[started_at][lt]"] = filterstarted_atlt

    params["filter[started_at][lte]"] = filterstarted_atlte

    params["filter[ended_at][gt]"] = filterended_atgt

    params["filter[ended_at][gte]"] = filterended_atgte

    params["filter[ended_at][lt]"] = filterended_atlt

    params["filter[ended_at][lte]"] = filterended_atlte

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params["filter[updated_at][gt]"] = filterupdated_atgt

    params["filter[updated_at][gte]"] = filterupdated_atgte

    params["filter[updated_at][lt]"] = filterupdated_atlt

    params["filter[updated_at][lte]"] = filterupdated_atlte

    params["filter[status][eq]"] = filterstatuseq

    params["filter[status][not_eq]"] = filterstatusnot_eq

    params["filter[status][in]"] = filterstatusin

    params["filter[status][not_in]"] = filterstatusnot_in

    params["filter[source][eq]"] = filtersourceeq

    params["filter[source][not_eq]"] = filtersourcenot_eq

    params["filter[source][in]"] = filtersourcein

    params["filter[source][not_in]"] = filtersourcenot_in

    params["filter[services][eq]"] = filterserviceseq

    params["filter[services][not_eq]"] = filterservicesnot_eq

    params["filter[services][in]"] = filterservicesin

    params["filter[services][not_in]"] = filterservicesnot_in

    params["filter[groups][eq]"] = filtergroupseq

    params["filter[groups][not_eq]"] = filtergroupsnot_eq

    params["filter[groups][in]"] = filtergroupsin

    params["filter[groups][not_in]"] = filtergroupsnot_in

    params["filter[environments][eq]"] = filterenvironmentseq

    params["filter[environments][not_eq]"] = filterenvironmentsnot_eq

    params["filter[environments][in]"] = filterenvironmentsin

    params["filter[environments][not_in]"] = filterenvironmentsnot_in

    params["filter[labels][eq]"] = filterlabelseq

    params["filter[labels][not_eq]"] = filterlabelsnot_eq

    params["filter[labels][in]"] = filterlabelsin

    params["filter[labels][not_in]"] = filterlabelsnot_in

    params["page[after]"] = pageafter

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/alerts",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[AlertList]:
    if response.status_code == 200:
        response_200 = AlertList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[AlertList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, ListAlertsInclude] = UNSET,
    filterstatus: Union[Unset, str] = UNSET,
    filtersource: Union[Unset, str] = UNSET,
    filterservices: Union[Unset, str] = UNSET,
    filterenvironments: Union[Unset, str] = UNSET,
    filtergroups: Union[Unset, str] = UNSET,
    filterlabels: Union[Unset, str] = UNSET,
    filterstarted_atgt: Union[Unset, str] = UNSET,
    filterstarted_atgte: Union[Unset, str] = UNSET,
    filterstarted_atlt: Union[Unset, str] = UNSET,
    filterstarted_atlte: Union[Unset, str] = UNSET,
    filterended_atgt: Union[Unset, str] = UNSET,
    filterended_atgte: Union[Unset, str] = UNSET,
    filterended_atlt: Union[Unset, str] = UNSET,
    filterended_atlte: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterupdated_atgt: Union[Unset, str] = UNSET,
    filterupdated_atgte: Union[Unset, str] = UNSET,
    filterupdated_atlt: Union[Unset, str] = UNSET,
    filterupdated_atlte: Union[Unset, str] = UNSET,
    filterstatuseq: Union[Unset, str] = UNSET,
    filterstatusnot_eq: Union[Unset, str] = UNSET,
    filterstatusin: Union[Unset, str] = UNSET,
    filterstatusnot_in: Union[Unset, str] = UNSET,
    filtersourceeq: Union[Unset, str] = UNSET,
    filtersourcenot_eq: Union[Unset, str] = UNSET,
    filtersourcein: Union[Unset, str] = UNSET,
    filtersourcenot_in: Union[Unset, str] = UNSET,
    filterserviceseq: Union[Unset, str] = UNSET,
    filterservicesnot_eq: Union[Unset, str] = UNSET,
    filterservicesin: Union[Unset, str] = UNSET,
    filterservicesnot_in: Union[Unset, str] = UNSET,
    filtergroupseq: Union[Unset, str] = UNSET,
    filtergroupsnot_eq: Union[Unset, str] = UNSET,
    filtergroupsin: Union[Unset, str] = UNSET,
    filtergroupsnot_in: Union[Unset, str] = UNSET,
    filterenvironmentseq: Union[Unset, str] = UNSET,
    filterenvironmentsnot_eq: Union[Unset, str] = UNSET,
    filterenvironmentsin: Union[Unset, str] = UNSET,
    filterenvironmentsnot_in: Union[Unset, str] = UNSET,
    filterlabelseq: Union[Unset, str] = UNSET,
    filterlabelsnot_eq: Union[Unset, str] = UNSET,
    filterlabelsin: Union[Unset, str] = UNSET,
    filterlabelsnot_in: Union[Unset, str] = UNSET,
    pageafter: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Response[AlertList]:
    """List alerts

     List alerts

    Args:
        include (Union[Unset, ListAlertsInclude]):
        filterstatus (Union[Unset, str]):
        filtersource (Union[Unset, str]):
        filterservices (Union[Unset, str]):
        filterenvironments (Union[Unset, str]):
        filtergroups (Union[Unset, str]):
        filterlabels (Union[Unset, str]):
        filterstarted_atgt (Union[Unset, str]):
        filterstarted_atgte (Union[Unset, str]):
        filterstarted_atlt (Union[Unset, str]):
        filterstarted_atlte (Union[Unset, str]):
        filterended_atgt (Union[Unset, str]):
        filterended_atgte (Union[Unset, str]):
        filterended_atlt (Union[Unset, str]):
        filterended_atlte (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterupdated_atgt (Union[Unset, str]):
        filterupdated_atgte (Union[Unset, str]):
        filterupdated_atlt (Union[Unset, str]):
        filterupdated_atlte (Union[Unset, str]):
        filterstatuseq (Union[Unset, str]):
        filterstatusnot_eq (Union[Unset, str]):
        filterstatusin (Union[Unset, str]):
        filterstatusnot_in (Union[Unset, str]):
        filtersourceeq (Union[Unset, str]):
        filtersourcenot_eq (Union[Unset, str]):
        filtersourcein (Union[Unset, str]):
        filtersourcenot_in (Union[Unset, str]):
        filterserviceseq (Union[Unset, str]):
        filterservicesnot_eq (Union[Unset, str]):
        filterservicesin (Union[Unset, str]):
        filterservicesnot_in (Union[Unset, str]):
        filtergroupseq (Union[Unset, str]):
        filtergroupsnot_eq (Union[Unset, str]):
        filtergroupsin (Union[Unset, str]):
        filtergroupsnot_in (Union[Unset, str]):
        filterenvironmentseq (Union[Unset, str]):
        filterenvironmentsnot_eq (Union[Unset, str]):
        filterenvironmentsin (Union[Unset, str]):
        filterenvironmentsnot_in (Union[Unset, str]):
        filterlabelseq (Union[Unset, str]):
        filterlabelsnot_eq (Union[Unset, str]):
        filterlabelsin (Union[Unset, str]):
        filterlabelsnot_in (Union[Unset, str]):
        pageafter (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertList]
    """

    kwargs = _get_kwargs(
        include=include,
        filterstatus=filterstatus,
        filtersource=filtersource,
        filterservices=filterservices,
        filterenvironments=filterenvironments,
        filtergroups=filtergroups,
        filterlabels=filterlabels,
        filterstarted_atgt=filterstarted_atgt,
        filterstarted_atgte=filterstarted_atgte,
        filterstarted_atlt=filterstarted_atlt,
        filterstarted_atlte=filterstarted_atlte,
        filterended_atgt=filterended_atgt,
        filterended_atgte=filterended_atgte,
        filterended_atlt=filterended_atlt,
        filterended_atlte=filterended_atlte,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterupdated_atgt=filterupdated_atgt,
        filterupdated_atgte=filterupdated_atgte,
        filterupdated_atlt=filterupdated_atlt,
        filterupdated_atlte=filterupdated_atlte,
        filterstatuseq=filterstatuseq,
        filterstatusnot_eq=filterstatusnot_eq,
        filterstatusin=filterstatusin,
        filterstatusnot_in=filterstatusnot_in,
        filtersourceeq=filtersourceeq,
        filtersourcenot_eq=filtersourcenot_eq,
        filtersourcein=filtersourcein,
        filtersourcenot_in=filtersourcenot_in,
        filterserviceseq=filterserviceseq,
        filterservicesnot_eq=filterservicesnot_eq,
        filterservicesin=filterservicesin,
        filterservicesnot_in=filterservicesnot_in,
        filtergroupseq=filtergroupseq,
        filtergroupsnot_eq=filtergroupsnot_eq,
        filtergroupsin=filtergroupsin,
        filtergroupsnot_in=filtergroupsnot_in,
        filterenvironmentseq=filterenvironmentseq,
        filterenvironmentsnot_eq=filterenvironmentsnot_eq,
        filterenvironmentsin=filterenvironmentsin,
        filterenvironmentsnot_in=filterenvironmentsnot_in,
        filterlabelseq=filterlabelseq,
        filterlabelsnot_eq=filterlabelsnot_eq,
        filterlabelsin=filterlabelsin,
        filterlabelsnot_in=filterlabelsnot_in,
        pageafter=pageafter,
        pagenumber=pagenumber,
        pagesize=pagesize,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, ListAlertsInclude] = UNSET,
    filterstatus: Union[Unset, str] = UNSET,
    filtersource: Union[Unset, str] = UNSET,
    filterservices: Union[Unset, str] = UNSET,
    filterenvironments: Union[Unset, str] = UNSET,
    filtergroups: Union[Unset, str] = UNSET,
    filterlabels: Union[Unset, str] = UNSET,
    filterstarted_atgt: Union[Unset, str] = UNSET,
    filterstarted_atgte: Union[Unset, str] = UNSET,
    filterstarted_atlt: Union[Unset, str] = UNSET,
    filterstarted_atlte: Union[Unset, str] = UNSET,
    filterended_atgt: Union[Unset, str] = UNSET,
    filterended_atgte: Union[Unset, str] = UNSET,
    filterended_atlt: Union[Unset, str] = UNSET,
    filterended_atlte: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterupdated_atgt: Union[Unset, str] = UNSET,
    filterupdated_atgte: Union[Unset, str] = UNSET,
    filterupdated_atlt: Union[Unset, str] = UNSET,
    filterupdated_atlte: Union[Unset, str] = UNSET,
    filterstatuseq: Union[Unset, str] = UNSET,
    filterstatusnot_eq: Union[Unset, str] = UNSET,
    filterstatusin: Union[Unset, str] = UNSET,
    filterstatusnot_in: Union[Unset, str] = UNSET,
    filtersourceeq: Union[Unset, str] = UNSET,
    filtersourcenot_eq: Union[Unset, str] = UNSET,
    filtersourcein: Union[Unset, str] = UNSET,
    filtersourcenot_in: Union[Unset, str] = UNSET,
    filterserviceseq: Union[Unset, str] = UNSET,
    filterservicesnot_eq: Union[Unset, str] = UNSET,
    filterservicesin: Union[Unset, str] = UNSET,
    filterservicesnot_in: Union[Unset, str] = UNSET,
    filtergroupseq: Union[Unset, str] = UNSET,
    filtergroupsnot_eq: Union[Unset, str] = UNSET,
    filtergroupsin: Union[Unset, str] = UNSET,
    filtergroupsnot_in: Union[Unset, str] = UNSET,
    filterenvironmentseq: Union[Unset, str] = UNSET,
    filterenvironmentsnot_eq: Union[Unset, str] = UNSET,
    filterenvironmentsin: Union[Unset, str] = UNSET,
    filterenvironmentsnot_in: Union[Unset, str] = UNSET,
    filterlabelseq: Union[Unset, str] = UNSET,
    filterlabelsnot_eq: Union[Unset, str] = UNSET,
    filterlabelsin: Union[Unset, str] = UNSET,
    filterlabelsnot_in: Union[Unset, str] = UNSET,
    pageafter: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Optional[AlertList]:
    """List alerts

     List alerts

    Args:
        include (Union[Unset, ListAlertsInclude]):
        filterstatus (Union[Unset, str]):
        filtersource (Union[Unset, str]):
        filterservices (Union[Unset, str]):
        filterenvironments (Union[Unset, str]):
        filtergroups (Union[Unset, str]):
        filterlabels (Union[Unset, str]):
        filterstarted_atgt (Union[Unset, str]):
        filterstarted_atgte (Union[Unset, str]):
        filterstarted_atlt (Union[Unset, str]):
        filterstarted_atlte (Union[Unset, str]):
        filterended_atgt (Union[Unset, str]):
        filterended_atgte (Union[Unset, str]):
        filterended_atlt (Union[Unset, str]):
        filterended_atlte (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterupdated_atgt (Union[Unset, str]):
        filterupdated_atgte (Union[Unset, str]):
        filterupdated_atlt (Union[Unset, str]):
        filterupdated_atlte (Union[Unset, str]):
        filterstatuseq (Union[Unset, str]):
        filterstatusnot_eq (Union[Unset, str]):
        filterstatusin (Union[Unset, str]):
        filterstatusnot_in (Union[Unset, str]):
        filtersourceeq (Union[Unset, str]):
        filtersourcenot_eq (Union[Unset, str]):
        filtersourcein (Union[Unset, str]):
        filtersourcenot_in (Union[Unset, str]):
        filterserviceseq (Union[Unset, str]):
        filterservicesnot_eq (Union[Unset, str]):
        filterservicesin (Union[Unset, str]):
        filterservicesnot_in (Union[Unset, str]):
        filtergroupseq (Union[Unset, str]):
        filtergroupsnot_eq (Union[Unset, str]):
        filtergroupsin (Union[Unset, str]):
        filtergroupsnot_in (Union[Unset, str]):
        filterenvironmentseq (Union[Unset, str]):
        filterenvironmentsnot_eq (Union[Unset, str]):
        filterenvironmentsin (Union[Unset, str]):
        filterenvironmentsnot_in (Union[Unset, str]):
        filterlabelseq (Union[Unset, str]):
        filterlabelsnot_eq (Union[Unset, str]):
        filterlabelsin (Union[Unset, str]):
        filterlabelsnot_in (Union[Unset, str]):
        pageafter (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertList
    """

    return sync_detailed(
        client=client,
        include=include,
        filterstatus=filterstatus,
        filtersource=filtersource,
        filterservices=filterservices,
        filterenvironments=filterenvironments,
        filtergroups=filtergroups,
        filterlabels=filterlabels,
        filterstarted_atgt=filterstarted_atgt,
        filterstarted_atgte=filterstarted_atgte,
        filterstarted_atlt=filterstarted_atlt,
        filterstarted_atlte=filterstarted_atlte,
        filterended_atgt=filterended_atgt,
        filterended_atgte=filterended_atgte,
        filterended_atlt=filterended_atlt,
        filterended_atlte=filterended_atlte,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterupdated_atgt=filterupdated_atgt,
        filterupdated_atgte=filterupdated_atgte,
        filterupdated_atlt=filterupdated_atlt,
        filterupdated_atlte=filterupdated_atlte,
        filterstatuseq=filterstatuseq,
        filterstatusnot_eq=filterstatusnot_eq,
        filterstatusin=filterstatusin,
        filterstatusnot_in=filterstatusnot_in,
        filtersourceeq=filtersourceeq,
        filtersourcenot_eq=filtersourcenot_eq,
        filtersourcein=filtersourcein,
        filtersourcenot_in=filtersourcenot_in,
        filterserviceseq=filterserviceseq,
        filterservicesnot_eq=filterservicesnot_eq,
        filterservicesin=filterservicesin,
        filterservicesnot_in=filterservicesnot_in,
        filtergroupseq=filtergroupseq,
        filtergroupsnot_eq=filtergroupsnot_eq,
        filtergroupsin=filtergroupsin,
        filtergroupsnot_in=filtergroupsnot_in,
        filterenvironmentseq=filterenvironmentseq,
        filterenvironmentsnot_eq=filterenvironmentsnot_eq,
        filterenvironmentsin=filterenvironmentsin,
        filterenvironmentsnot_in=filterenvironmentsnot_in,
        filterlabelseq=filterlabelseq,
        filterlabelsnot_eq=filterlabelsnot_eq,
        filterlabelsin=filterlabelsin,
        filterlabelsnot_in=filterlabelsnot_in,
        pageafter=pageafter,
        pagenumber=pagenumber,
        pagesize=pagesize,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, ListAlertsInclude] = UNSET,
    filterstatus: Union[Unset, str] = UNSET,
    filtersource: Union[Unset, str] = UNSET,
    filterservices: Union[Unset, str] = UNSET,
    filterenvironments: Union[Unset, str] = UNSET,
    filtergroups: Union[Unset, str] = UNSET,
    filterlabels: Union[Unset, str] = UNSET,
    filterstarted_atgt: Union[Unset, str] = UNSET,
    filterstarted_atgte: Union[Unset, str] = UNSET,
    filterstarted_atlt: Union[Unset, str] = UNSET,
    filterstarted_atlte: Union[Unset, str] = UNSET,
    filterended_atgt: Union[Unset, str] = UNSET,
    filterended_atgte: Union[Unset, str] = UNSET,
    filterended_atlt: Union[Unset, str] = UNSET,
    filterended_atlte: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterupdated_atgt: Union[Unset, str] = UNSET,
    filterupdated_atgte: Union[Unset, str] = UNSET,
    filterupdated_atlt: Union[Unset, str] = UNSET,
    filterupdated_atlte: Union[Unset, str] = UNSET,
    filterstatuseq: Union[Unset, str] = UNSET,
    filterstatusnot_eq: Union[Unset, str] = UNSET,
    filterstatusin: Union[Unset, str] = UNSET,
    filterstatusnot_in: Union[Unset, str] = UNSET,
    filtersourceeq: Union[Unset, str] = UNSET,
    filtersourcenot_eq: Union[Unset, str] = UNSET,
    filtersourcein: Union[Unset, str] = UNSET,
    filtersourcenot_in: Union[Unset, str] = UNSET,
    filterserviceseq: Union[Unset, str] = UNSET,
    filterservicesnot_eq: Union[Unset, str] = UNSET,
    filterservicesin: Union[Unset, str] = UNSET,
    filterservicesnot_in: Union[Unset, str] = UNSET,
    filtergroupseq: Union[Unset, str] = UNSET,
    filtergroupsnot_eq: Union[Unset, str] = UNSET,
    filtergroupsin: Union[Unset, str] = UNSET,
    filtergroupsnot_in: Union[Unset, str] = UNSET,
    filterenvironmentseq: Union[Unset, str] = UNSET,
    filterenvironmentsnot_eq: Union[Unset, str] = UNSET,
    filterenvironmentsin: Union[Unset, str] = UNSET,
    filterenvironmentsnot_in: Union[Unset, str] = UNSET,
    filterlabelseq: Union[Unset, str] = UNSET,
    filterlabelsnot_eq: Union[Unset, str] = UNSET,
    filterlabelsin: Union[Unset, str] = UNSET,
    filterlabelsnot_in: Union[Unset, str] = UNSET,
    pageafter: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Response[AlertList]:
    """List alerts

     List alerts

    Args:
        include (Union[Unset, ListAlertsInclude]):
        filterstatus (Union[Unset, str]):
        filtersource (Union[Unset, str]):
        filterservices (Union[Unset, str]):
        filterenvironments (Union[Unset, str]):
        filtergroups (Union[Unset, str]):
        filterlabels (Union[Unset, str]):
        filterstarted_atgt (Union[Unset, str]):
        filterstarted_atgte (Union[Unset, str]):
        filterstarted_atlt (Union[Unset, str]):
        filterstarted_atlte (Union[Unset, str]):
        filterended_atgt (Union[Unset, str]):
        filterended_atgte (Union[Unset, str]):
        filterended_atlt (Union[Unset, str]):
        filterended_atlte (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterupdated_atgt (Union[Unset, str]):
        filterupdated_atgte (Union[Unset, str]):
        filterupdated_atlt (Union[Unset, str]):
        filterupdated_atlte (Union[Unset, str]):
        filterstatuseq (Union[Unset, str]):
        filterstatusnot_eq (Union[Unset, str]):
        filterstatusin (Union[Unset, str]):
        filterstatusnot_in (Union[Unset, str]):
        filtersourceeq (Union[Unset, str]):
        filtersourcenot_eq (Union[Unset, str]):
        filtersourcein (Union[Unset, str]):
        filtersourcenot_in (Union[Unset, str]):
        filterserviceseq (Union[Unset, str]):
        filterservicesnot_eq (Union[Unset, str]):
        filterservicesin (Union[Unset, str]):
        filterservicesnot_in (Union[Unset, str]):
        filtergroupseq (Union[Unset, str]):
        filtergroupsnot_eq (Union[Unset, str]):
        filtergroupsin (Union[Unset, str]):
        filtergroupsnot_in (Union[Unset, str]):
        filterenvironmentseq (Union[Unset, str]):
        filterenvironmentsnot_eq (Union[Unset, str]):
        filterenvironmentsin (Union[Unset, str]):
        filterenvironmentsnot_in (Union[Unset, str]):
        filterlabelseq (Union[Unset, str]):
        filterlabelsnot_eq (Union[Unset, str]):
        filterlabelsin (Union[Unset, str]):
        filterlabelsnot_in (Union[Unset, str]):
        pageafter (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertList]
    """

    kwargs = _get_kwargs(
        include=include,
        filterstatus=filterstatus,
        filtersource=filtersource,
        filterservices=filterservices,
        filterenvironments=filterenvironments,
        filtergroups=filtergroups,
        filterlabels=filterlabels,
        filterstarted_atgt=filterstarted_atgt,
        filterstarted_atgte=filterstarted_atgte,
        filterstarted_atlt=filterstarted_atlt,
        filterstarted_atlte=filterstarted_atlte,
        filterended_atgt=filterended_atgt,
        filterended_atgte=filterended_atgte,
        filterended_atlt=filterended_atlt,
        filterended_atlte=filterended_atlte,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterupdated_atgt=filterupdated_atgt,
        filterupdated_atgte=filterupdated_atgte,
        filterupdated_atlt=filterupdated_atlt,
        filterupdated_atlte=filterupdated_atlte,
        filterstatuseq=filterstatuseq,
        filterstatusnot_eq=filterstatusnot_eq,
        filterstatusin=filterstatusin,
        filterstatusnot_in=filterstatusnot_in,
        filtersourceeq=filtersourceeq,
        filtersourcenot_eq=filtersourcenot_eq,
        filtersourcein=filtersourcein,
        filtersourcenot_in=filtersourcenot_in,
        filterserviceseq=filterserviceseq,
        filterservicesnot_eq=filterservicesnot_eq,
        filterservicesin=filterservicesin,
        filterservicesnot_in=filterservicesnot_in,
        filtergroupseq=filtergroupseq,
        filtergroupsnot_eq=filtergroupsnot_eq,
        filtergroupsin=filtergroupsin,
        filtergroupsnot_in=filtergroupsnot_in,
        filterenvironmentseq=filterenvironmentseq,
        filterenvironmentsnot_eq=filterenvironmentsnot_eq,
        filterenvironmentsin=filterenvironmentsin,
        filterenvironmentsnot_in=filterenvironmentsnot_in,
        filterlabelseq=filterlabelseq,
        filterlabelsnot_eq=filterlabelsnot_eq,
        filterlabelsin=filterlabelsin,
        filterlabelsnot_in=filterlabelsnot_in,
        pageafter=pageafter,
        pagenumber=pagenumber,
        pagesize=pagesize,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, ListAlertsInclude] = UNSET,
    filterstatus: Union[Unset, str] = UNSET,
    filtersource: Union[Unset, str] = UNSET,
    filterservices: Union[Unset, str] = UNSET,
    filterenvironments: Union[Unset, str] = UNSET,
    filtergroups: Union[Unset, str] = UNSET,
    filterlabels: Union[Unset, str] = UNSET,
    filterstarted_atgt: Union[Unset, str] = UNSET,
    filterstarted_atgte: Union[Unset, str] = UNSET,
    filterstarted_atlt: Union[Unset, str] = UNSET,
    filterstarted_atlte: Union[Unset, str] = UNSET,
    filterended_atgt: Union[Unset, str] = UNSET,
    filterended_atgte: Union[Unset, str] = UNSET,
    filterended_atlt: Union[Unset, str] = UNSET,
    filterended_atlte: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filterupdated_atgt: Union[Unset, str] = UNSET,
    filterupdated_atgte: Union[Unset, str] = UNSET,
    filterupdated_atlt: Union[Unset, str] = UNSET,
    filterupdated_atlte: Union[Unset, str] = UNSET,
    filterstatuseq: Union[Unset, str] = UNSET,
    filterstatusnot_eq: Union[Unset, str] = UNSET,
    filterstatusin: Union[Unset, str] = UNSET,
    filterstatusnot_in: Union[Unset, str] = UNSET,
    filtersourceeq: Union[Unset, str] = UNSET,
    filtersourcenot_eq: Union[Unset, str] = UNSET,
    filtersourcein: Union[Unset, str] = UNSET,
    filtersourcenot_in: Union[Unset, str] = UNSET,
    filterserviceseq: Union[Unset, str] = UNSET,
    filterservicesnot_eq: Union[Unset, str] = UNSET,
    filterservicesin: Union[Unset, str] = UNSET,
    filterservicesnot_in: Union[Unset, str] = UNSET,
    filtergroupseq: Union[Unset, str] = UNSET,
    filtergroupsnot_eq: Union[Unset, str] = UNSET,
    filtergroupsin: Union[Unset, str] = UNSET,
    filtergroupsnot_in: Union[Unset, str] = UNSET,
    filterenvironmentseq: Union[Unset, str] = UNSET,
    filterenvironmentsnot_eq: Union[Unset, str] = UNSET,
    filterenvironmentsin: Union[Unset, str] = UNSET,
    filterenvironmentsnot_in: Union[Unset, str] = UNSET,
    filterlabelseq: Union[Unset, str] = UNSET,
    filterlabelsnot_eq: Union[Unset, str] = UNSET,
    filterlabelsin: Union[Unset, str] = UNSET,
    filterlabelsnot_in: Union[Unset, str] = UNSET,
    pageafter: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Optional[AlertList]:
    """List alerts

     List alerts

    Args:
        include (Union[Unset, ListAlertsInclude]):
        filterstatus (Union[Unset, str]):
        filtersource (Union[Unset, str]):
        filterservices (Union[Unset, str]):
        filterenvironments (Union[Unset, str]):
        filtergroups (Union[Unset, str]):
        filterlabels (Union[Unset, str]):
        filterstarted_atgt (Union[Unset, str]):
        filterstarted_atgte (Union[Unset, str]):
        filterstarted_atlt (Union[Unset, str]):
        filterstarted_atlte (Union[Unset, str]):
        filterended_atgt (Union[Unset, str]):
        filterended_atgte (Union[Unset, str]):
        filterended_atlt (Union[Unset, str]):
        filterended_atlte (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterupdated_atgt (Union[Unset, str]):
        filterupdated_atgte (Union[Unset, str]):
        filterupdated_atlt (Union[Unset, str]):
        filterupdated_atlte (Union[Unset, str]):
        filterstatuseq (Union[Unset, str]):
        filterstatusnot_eq (Union[Unset, str]):
        filterstatusin (Union[Unset, str]):
        filterstatusnot_in (Union[Unset, str]):
        filtersourceeq (Union[Unset, str]):
        filtersourcenot_eq (Union[Unset, str]):
        filtersourcein (Union[Unset, str]):
        filtersourcenot_in (Union[Unset, str]):
        filterserviceseq (Union[Unset, str]):
        filterservicesnot_eq (Union[Unset, str]):
        filterservicesin (Union[Unset, str]):
        filterservicesnot_in (Union[Unset, str]):
        filtergroupseq (Union[Unset, str]):
        filtergroupsnot_eq (Union[Unset, str]):
        filtergroupsin (Union[Unset, str]):
        filtergroupsnot_in (Union[Unset, str]):
        filterenvironmentseq (Union[Unset, str]):
        filterenvironmentsnot_eq (Union[Unset, str]):
        filterenvironmentsin (Union[Unset, str]):
        filterenvironmentsnot_in (Union[Unset, str]):
        filterlabelseq (Union[Unset, str]):
        filterlabelsnot_eq (Union[Unset, str]):
        filterlabelsin (Union[Unset, str]):
        filterlabelsnot_in (Union[Unset, str]):
        pageafter (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertList
    """

    return (
        await asyncio_detailed(
            client=client,
            include=include,
            filterstatus=filterstatus,
            filtersource=filtersource,
            filterservices=filterservices,
            filterenvironments=filterenvironments,
            filtergroups=filtergroups,
            filterlabels=filterlabels,
            filterstarted_atgt=filterstarted_atgt,
            filterstarted_atgte=filterstarted_atgte,
            filterstarted_atlt=filterstarted_atlt,
            filterstarted_atlte=filterstarted_atlte,
            filterended_atgt=filterended_atgt,
            filterended_atgte=filterended_atgte,
            filterended_atlt=filterended_atlt,
            filterended_atlte=filterended_atlte,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
            filterupdated_atgt=filterupdated_atgt,
            filterupdated_atgte=filterupdated_atgte,
            filterupdated_atlt=filterupdated_atlt,
            filterupdated_atlte=filterupdated_atlte,
            filterstatuseq=filterstatuseq,
            filterstatusnot_eq=filterstatusnot_eq,
            filterstatusin=filterstatusin,
            filterstatusnot_in=filterstatusnot_in,
            filtersourceeq=filtersourceeq,
            filtersourcenot_eq=filtersourcenot_eq,
            filtersourcein=filtersourcein,
            filtersourcenot_in=filtersourcenot_in,
            filterserviceseq=filterserviceseq,
            filterservicesnot_eq=filterservicesnot_eq,
            filterservicesin=filterservicesin,
            filterservicesnot_in=filterservicesnot_in,
            filtergroupseq=filtergroupseq,
            filtergroupsnot_eq=filtergroupsnot_eq,
            filtergroupsin=filtergroupsin,
            filtergroupsnot_in=filtergroupsnot_in,
            filterenvironmentseq=filterenvironmentseq,
            filterenvironmentsnot_eq=filterenvironmentsnot_eq,
            filterenvironmentsin=filterenvironmentsin,
            filterenvironmentsnot_in=filterenvironmentsnot_in,
            filterlabelseq=filterlabelseq,
            filterlabelsnot_eq=filterlabelsnot_eq,
            filterlabelsin=filterlabelsin,
            filterlabelsnot_in=filterlabelsnot_in,
            pageafter=pageafter,
            pagenumber=pagenumber,
            pagesize=pagesize,
        )
    ).parsed
