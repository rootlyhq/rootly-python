from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.alert_list import AlertList
from ...models.list_alerts_include import check_list_alerts_include
from ...models.list_alerts_include import ListAlertsInclude
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    include: ListAlertsInclude | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filtersource: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filtergroups: str | Unset = UNSET,
    filterlabels: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filterended_atgt: str | Unset = UNSET,
    filterended_atgte: str | Unset = UNSET,
    filterended_atlt: str | Unset = UNSET,
    filterended_atlte: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterupdated_atgt: str | Unset = UNSET,
    filterupdated_atgte: str | Unset = UNSET,
    filterupdated_atlt: str | Unset = UNSET,
    filterupdated_atlte: str | Unset = UNSET,
    filterstatuseq: str | Unset = UNSET,
    filterstatusnot_eq: str | Unset = UNSET,
    filterstatusin: str | Unset = UNSET,
    filterstatusnot_in: str | Unset = UNSET,
    filtersourceeq: str | Unset = UNSET,
    filtersourcenot_eq: str | Unset = UNSET,
    filtersourcein: str | Unset = UNSET,
    filtersourcenot_in: str | Unset = UNSET,
    filterserviceseq: str | Unset = UNSET,
    filterservicesnot_eq: str | Unset = UNSET,
    filterservicesin: str | Unset = UNSET,
    filterservicesnot_in: str | Unset = UNSET,
    filtergroupseq: str | Unset = UNSET,
    filtergroupsnot_eq: str | Unset = UNSET,
    filtergroupsin: str | Unset = UNSET,
    filtergroupsnot_in: str | Unset = UNSET,
    filterenvironmentseq: str | Unset = UNSET,
    filterenvironmentsnot_eq: str | Unset = UNSET,
    filterenvironmentsin: str | Unset = UNSET,
    filterenvironmentsnot_in: str | Unset = UNSET,
    filterlabelseq: str | Unset = UNSET,
    filterlabelsnot_eq: str | Unset = UNSET,
    filterlabelsin: str | Unset = UNSET,
    filterlabelsnot_in: str | Unset = UNSET,
    pageafter: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_include: str | Unset = UNSET
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



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AlertList | None:
    if response.status_code == 200:
        response_200 = AlertList.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AlertList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include: ListAlertsInclude | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filtersource: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filtergroups: str | Unset = UNSET,
    filterlabels: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filterended_atgt: str | Unset = UNSET,
    filterended_atgte: str | Unset = UNSET,
    filterended_atlt: str | Unset = UNSET,
    filterended_atlte: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterupdated_atgt: str | Unset = UNSET,
    filterupdated_atgte: str | Unset = UNSET,
    filterupdated_atlt: str | Unset = UNSET,
    filterupdated_atlte: str | Unset = UNSET,
    filterstatuseq: str | Unset = UNSET,
    filterstatusnot_eq: str | Unset = UNSET,
    filterstatusin: str | Unset = UNSET,
    filterstatusnot_in: str | Unset = UNSET,
    filtersourceeq: str | Unset = UNSET,
    filtersourcenot_eq: str | Unset = UNSET,
    filtersourcein: str | Unset = UNSET,
    filtersourcenot_in: str | Unset = UNSET,
    filterserviceseq: str | Unset = UNSET,
    filterservicesnot_eq: str | Unset = UNSET,
    filterservicesin: str | Unset = UNSET,
    filterservicesnot_in: str | Unset = UNSET,
    filtergroupseq: str | Unset = UNSET,
    filtergroupsnot_eq: str | Unset = UNSET,
    filtergroupsin: str | Unset = UNSET,
    filtergroupsnot_in: str | Unset = UNSET,
    filterenvironmentseq: str | Unset = UNSET,
    filterenvironmentsnot_eq: str | Unset = UNSET,
    filterenvironmentsin: str | Unset = UNSET,
    filterenvironmentsnot_in: str | Unset = UNSET,
    filterlabelseq: str | Unset = UNSET,
    filterlabelsnot_eq: str | Unset = UNSET,
    filterlabelsin: str | Unset = UNSET,
    filterlabelsnot_in: str | Unset = UNSET,
    pageafter: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,

) -> Response[AlertList]:
    """ List alerts

     List alerts

    Args:
        include (ListAlertsInclude | Unset):
        filterstatus (str | Unset):
        filtersource (str | Unset):
        filterservices (str | Unset):
        filterenvironments (str | Unset):
        filtergroups (str | Unset):
        filterlabels (str | Unset):
        filterstarted_atgt (str | Unset):
        filterstarted_atgte (str | Unset):
        filterstarted_atlt (str | Unset):
        filterstarted_atlte (str | Unset):
        filterended_atgt (str | Unset):
        filterended_atgte (str | Unset):
        filterended_atlt (str | Unset):
        filterended_atlte (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterupdated_atgt (str | Unset):
        filterupdated_atgte (str | Unset):
        filterupdated_atlt (str | Unset):
        filterupdated_atlte (str | Unset):
        filterstatuseq (str | Unset):
        filterstatusnot_eq (str | Unset):
        filterstatusin (str | Unset):
        filterstatusnot_in (str | Unset):
        filtersourceeq (str | Unset):
        filtersourcenot_eq (str | Unset):
        filtersourcein (str | Unset):
        filtersourcenot_in (str | Unset):
        filterserviceseq (str | Unset):
        filterservicesnot_eq (str | Unset):
        filterservicesin (str | Unset):
        filterservicesnot_in (str | Unset):
        filtergroupseq (str | Unset):
        filtergroupsnot_eq (str | Unset):
        filtergroupsin (str | Unset):
        filtergroupsnot_in (str | Unset):
        filterenvironmentseq (str | Unset):
        filterenvironmentsnot_eq (str | Unset):
        filterenvironmentsin (str | Unset):
        filterenvironmentsnot_in (str | Unset):
        filterlabelseq (str | Unset):
        filterlabelsnot_eq (str | Unset):
        filterlabelsin (str | Unset):
        filterlabelsnot_in (str | Unset):
        pageafter (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

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
    include: ListAlertsInclude | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filtersource: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filtergroups: str | Unset = UNSET,
    filterlabels: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filterended_atgt: str | Unset = UNSET,
    filterended_atgte: str | Unset = UNSET,
    filterended_atlt: str | Unset = UNSET,
    filterended_atlte: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterupdated_atgt: str | Unset = UNSET,
    filterupdated_atgte: str | Unset = UNSET,
    filterupdated_atlt: str | Unset = UNSET,
    filterupdated_atlte: str | Unset = UNSET,
    filterstatuseq: str | Unset = UNSET,
    filterstatusnot_eq: str | Unset = UNSET,
    filterstatusin: str | Unset = UNSET,
    filterstatusnot_in: str | Unset = UNSET,
    filtersourceeq: str | Unset = UNSET,
    filtersourcenot_eq: str | Unset = UNSET,
    filtersourcein: str | Unset = UNSET,
    filtersourcenot_in: str | Unset = UNSET,
    filterserviceseq: str | Unset = UNSET,
    filterservicesnot_eq: str | Unset = UNSET,
    filterservicesin: str | Unset = UNSET,
    filterservicesnot_in: str | Unset = UNSET,
    filtergroupseq: str | Unset = UNSET,
    filtergroupsnot_eq: str | Unset = UNSET,
    filtergroupsin: str | Unset = UNSET,
    filtergroupsnot_in: str | Unset = UNSET,
    filterenvironmentseq: str | Unset = UNSET,
    filterenvironmentsnot_eq: str | Unset = UNSET,
    filterenvironmentsin: str | Unset = UNSET,
    filterenvironmentsnot_in: str | Unset = UNSET,
    filterlabelseq: str | Unset = UNSET,
    filterlabelsnot_eq: str | Unset = UNSET,
    filterlabelsin: str | Unset = UNSET,
    filterlabelsnot_in: str | Unset = UNSET,
    pageafter: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,

) -> AlertList | None:
    """ List alerts

     List alerts

    Args:
        include (ListAlertsInclude | Unset):
        filterstatus (str | Unset):
        filtersource (str | Unset):
        filterservices (str | Unset):
        filterenvironments (str | Unset):
        filtergroups (str | Unset):
        filterlabels (str | Unset):
        filterstarted_atgt (str | Unset):
        filterstarted_atgte (str | Unset):
        filterstarted_atlt (str | Unset):
        filterstarted_atlte (str | Unset):
        filterended_atgt (str | Unset):
        filterended_atgte (str | Unset):
        filterended_atlt (str | Unset):
        filterended_atlte (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterupdated_atgt (str | Unset):
        filterupdated_atgte (str | Unset):
        filterupdated_atlt (str | Unset):
        filterupdated_atlte (str | Unset):
        filterstatuseq (str | Unset):
        filterstatusnot_eq (str | Unset):
        filterstatusin (str | Unset):
        filterstatusnot_in (str | Unset):
        filtersourceeq (str | Unset):
        filtersourcenot_eq (str | Unset):
        filtersourcein (str | Unset):
        filtersourcenot_in (str | Unset):
        filterserviceseq (str | Unset):
        filterservicesnot_eq (str | Unset):
        filterservicesin (str | Unset):
        filterservicesnot_in (str | Unset):
        filtergroupseq (str | Unset):
        filtergroupsnot_eq (str | Unset):
        filtergroupsin (str | Unset):
        filtergroupsnot_in (str | Unset):
        filterenvironmentseq (str | Unset):
        filterenvironmentsnot_eq (str | Unset):
        filterenvironmentsin (str | Unset):
        filterenvironmentsnot_in (str | Unset):
        filterlabelseq (str | Unset):
        filterlabelsnot_eq (str | Unset):
        filterlabelsin (str | Unset):
        filterlabelsnot_in (str | Unset):
        pageafter (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

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
    include: ListAlertsInclude | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filtersource: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filtergroups: str | Unset = UNSET,
    filterlabels: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filterended_atgt: str | Unset = UNSET,
    filterended_atgte: str | Unset = UNSET,
    filterended_atlt: str | Unset = UNSET,
    filterended_atlte: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterupdated_atgt: str | Unset = UNSET,
    filterupdated_atgte: str | Unset = UNSET,
    filterupdated_atlt: str | Unset = UNSET,
    filterupdated_atlte: str | Unset = UNSET,
    filterstatuseq: str | Unset = UNSET,
    filterstatusnot_eq: str | Unset = UNSET,
    filterstatusin: str | Unset = UNSET,
    filterstatusnot_in: str | Unset = UNSET,
    filtersourceeq: str | Unset = UNSET,
    filtersourcenot_eq: str | Unset = UNSET,
    filtersourcein: str | Unset = UNSET,
    filtersourcenot_in: str | Unset = UNSET,
    filterserviceseq: str | Unset = UNSET,
    filterservicesnot_eq: str | Unset = UNSET,
    filterservicesin: str | Unset = UNSET,
    filterservicesnot_in: str | Unset = UNSET,
    filtergroupseq: str | Unset = UNSET,
    filtergroupsnot_eq: str | Unset = UNSET,
    filtergroupsin: str | Unset = UNSET,
    filtergroupsnot_in: str | Unset = UNSET,
    filterenvironmentseq: str | Unset = UNSET,
    filterenvironmentsnot_eq: str | Unset = UNSET,
    filterenvironmentsin: str | Unset = UNSET,
    filterenvironmentsnot_in: str | Unset = UNSET,
    filterlabelseq: str | Unset = UNSET,
    filterlabelsnot_eq: str | Unset = UNSET,
    filterlabelsin: str | Unset = UNSET,
    filterlabelsnot_in: str | Unset = UNSET,
    pageafter: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,

) -> Response[AlertList]:
    """ List alerts

     List alerts

    Args:
        include (ListAlertsInclude | Unset):
        filterstatus (str | Unset):
        filtersource (str | Unset):
        filterservices (str | Unset):
        filterenvironments (str | Unset):
        filtergroups (str | Unset):
        filterlabels (str | Unset):
        filterstarted_atgt (str | Unset):
        filterstarted_atgte (str | Unset):
        filterstarted_atlt (str | Unset):
        filterstarted_atlte (str | Unset):
        filterended_atgt (str | Unset):
        filterended_atgte (str | Unset):
        filterended_atlt (str | Unset):
        filterended_atlte (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterupdated_atgt (str | Unset):
        filterupdated_atgte (str | Unset):
        filterupdated_atlt (str | Unset):
        filterupdated_atlte (str | Unset):
        filterstatuseq (str | Unset):
        filterstatusnot_eq (str | Unset):
        filterstatusin (str | Unset):
        filterstatusnot_in (str | Unset):
        filtersourceeq (str | Unset):
        filtersourcenot_eq (str | Unset):
        filtersourcein (str | Unset):
        filtersourcenot_in (str | Unset):
        filterserviceseq (str | Unset):
        filterservicesnot_eq (str | Unset):
        filterservicesin (str | Unset):
        filterservicesnot_in (str | Unset):
        filtergroupseq (str | Unset):
        filtergroupsnot_eq (str | Unset):
        filtergroupsin (str | Unset):
        filtergroupsnot_in (str | Unset):
        filterenvironmentseq (str | Unset):
        filterenvironmentsnot_eq (str | Unset):
        filterenvironmentsin (str | Unset):
        filterenvironmentsnot_in (str | Unset):
        filterlabelseq (str | Unset):
        filterlabelsnot_eq (str | Unset):
        filterlabelsin (str | Unset):
        filterlabelsnot_in (str | Unset):
        pageafter (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

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

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    include: ListAlertsInclude | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filtersource: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filtergroups: str | Unset = UNSET,
    filterlabels: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filterended_atgt: str | Unset = UNSET,
    filterended_atgte: str | Unset = UNSET,
    filterended_atlt: str | Unset = UNSET,
    filterended_atlte: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterupdated_atgt: str | Unset = UNSET,
    filterupdated_atgte: str | Unset = UNSET,
    filterupdated_atlt: str | Unset = UNSET,
    filterupdated_atlte: str | Unset = UNSET,
    filterstatuseq: str | Unset = UNSET,
    filterstatusnot_eq: str | Unset = UNSET,
    filterstatusin: str | Unset = UNSET,
    filterstatusnot_in: str | Unset = UNSET,
    filtersourceeq: str | Unset = UNSET,
    filtersourcenot_eq: str | Unset = UNSET,
    filtersourcein: str | Unset = UNSET,
    filtersourcenot_in: str | Unset = UNSET,
    filterserviceseq: str | Unset = UNSET,
    filterservicesnot_eq: str | Unset = UNSET,
    filterservicesin: str | Unset = UNSET,
    filterservicesnot_in: str | Unset = UNSET,
    filtergroupseq: str | Unset = UNSET,
    filtergroupsnot_eq: str | Unset = UNSET,
    filtergroupsin: str | Unset = UNSET,
    filtergroupsnot_in: str | Unset = UNSET,
    filterenvironmentseq: str | Unset = UNSET,
    filterenvironmentsnot_eq: str | Unset = UNSET,
    filterenvironmentsin: str | Unset = UNSET,
    filterenvironmentsnot_in: str | Unset = UNSET,
    filterlabelseq: str | Unset = UNSET,
    filterlabelsnot_eq: str | Unset = UNSET,
    filterlabelsin: str | Unset = UNSET,
    filterlabelsnot_in: str | Unset = UNSET,
    pageafter: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,

) -> AlertList | None:
    """ List alerts

     List alerts

    Args:
        include (ListAlertsInclude | Unset):
        filterstatus (str | Unset):
        filtersource (str | Unset):
        filterservices (str | Unset):
        filterenvironments (str | Unset):
        filtergroups (str | Unset):
        filterlabels (str | Unset):
        filterstarted_atgt (str | Unset):
        filterstarted_atgte (str | Unset):
        filterstarted_atlt (str | Unset):
        filterstarted_atlte (str | Unset):
        filterended_atgt (str | Unset):
        filterended_atgte (str | Unset):
        filterended_atlt (str | Unset):
        filterended_atlte (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterupdated_atgt (str | Unset):
        filterupdated_atgte (str | Unset):
        filterupdated_atlt (str | Unset):
        filterupdated_atlte (str | Unset):
        filterstatuseq (str | Unset):
        filterstatusnot_eq (str | Unset):
        filterstatusin (str | Unset):
        filterstatusnot_in (str | Unset):
        filtersourceeq (str | Unset):
        filtersourcenot_eq (str | Unset):
        filtersourcein (str | Unset):
        filtersourcenot_in (str | Unset):
        filterserviceseq (str | Unset):
        filterservicesnot_eq (str | Unset):
        filterservicesin (str | Unset):
        filterservicesnot_in (str | Unset):
        filtergroupseq (str | Unset):
        filtergroupsnot_eq (str | Unset):
        filtergroupsin (str | Unset):
        filtergroupsnot_in (str | Unset):
        filterenvironmentseq (str | Unset):
        filterenvironmentsnot_eq (str | Unset):
        filterenvironmentsin (str | Unset):
        filterenvironmentsnot_in (str | Unset):
        filterlabelseq (str | Unset):
        filterlabelsnot_eq (str | Unset):
        filterlabelsin (str | Unset):
        filterlabelsnot_in (str | Unset):
        pageafter (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertList
     """


    return (await asyncio_detailed(
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

    )).parsed
