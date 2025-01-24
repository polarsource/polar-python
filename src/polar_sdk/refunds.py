"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from jsonpath import JSONPath
from polar_sdk import models, utils
from polar_sdk._hooks import HookContext
from polar_sdk.types import BaseModel, OptionalNullable, UNSET
from typing import Any, Dict, List, Mapping, Optional, Union, cast


class Refunds(BaseSDK):
    def list(
        self,
        *,
        id: OptionalNullable[
            Union[models.RefundIDFilter, models.RefundIDFilterTypedDict]
        ] = UNSET,
        organization_id: OptionalNullable[
            Union[
                models.RefundsListQueryParamOrganizationIDFilter,
                models.RefundsListQueryParamOrganizationIDFilterTypedDict,
            ]
        ] = UNSET,
        order_id: OptionalNullable[
            Union[models.OrderIDFilter, models.OrderIDFilterTypedDict]
        ] = UNSET,
        subscription_id: OptionalNullable[
            Union[models.SubscriptionIDFilter, models.SubscriptionIDFilterTypedDict]
        ] = UNSET,
        customer_id: OptionalNullable[
            Union[
                models.RefundsListQueryParamCustomerIDFilter,
                models.RefundsListQueryParamCustomerIDFilterTypedDict,
            ]
        ] = UNSET,
        succeeded: OptionalNullable[bool] = UNSET,
        page: Optional[int] = 1,
        limit: Optional[int] = 10,
        sorting: OptionalNullable[List[models.RefundSortProperty]] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Optional[models.RefundsListResponse]:
        r"""List Refunds

        List products.

        :param id: Filter by refund ID.
        :param organization_id: Filter by organization ID.
        :param order_id: Filter by order ID.
        :param subscription_id: Filter by subscription ID.
        :param customer_id: Filter by customer ID.
        :param succeeded: Filter by `succeeded`.
        :param page: Page number, defaults to 1.
        :param limit: Size of a page, defaults to 10. Maximum is 100.
        :param sorting: Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.RefundsListRequest(
            id=id,
            organization_id=organization_id,
            order_id=order_id,
            subscription_id=subscription_id,
            customer_id=customer_id,
            succeeded=succeeded,
            page=page,
            limit=limit,
            sorting=sorting,
        )

        req = self._build_request(
            method="GET",
            path="/v1/refunds/",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="refunds:list",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        def next_func() -> Optional[models.RefundsListResponse]:
            body = utils.unmarshal_json(http_res.text, Dict[Any, Any])
            page = request.page if not request.page is None else 1
            next_page = page + 1

            num_pages = JSONPath("$.pagination.max_page").parse(body)
            if len(num_pages) == 0 or num_pages[0] <= page:
                return None

            if not http_res.text:
                return None
            results = JSONPath("$.items").parse(body)
            if len(results) == 0 or len(results[0]) == 0:
                return None
            limit = request.limit if not request.limit is None else 10
            if len(results[0]) < limit:
                return None

            return self.list(
                id=id,
                organization_id=organization_id,
                order_id=order_id,
                subscription_id=subscription_id,
                customer_id=customer_id,
                succeeded=succeeded,
                page=next_page,
                limit=limit,
                sorting=sorting,
                retries=retries,
            )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.RefundsListResponse(
                result=utils.unmarshal_json(http_res.text, models.ListResourceRefund),
                next=next_func,
            )
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def list_async(
        self,
        *,
        id: OptionalNullable[
            Union[models.RefundIDFilter, models.RefundIDFilterTypedDict]
        ] = UNSET,
        organization_id: OptionalNullable[
            Union[
                models.RefundsListQueryParamOrganizationIDFilter,
                models.RefundsListQueryParamOrganizationIDFilterTypedDict,
            ]
        ] = UNSET,
        order_id: OptionalNullable[
            Union[models.OrderIDFilter, models.OrderIDFilterTypedDict]
        ] = UNSET,
        subscription_id: OptionalNullable[
            Union[models.SubscriptionIDFilter, models.SubscriptionIDFilterTypedDict]
        ] = UNSET,
        customer_id: OptionalNullable[
            Union[
                models.RefundsListQueryParamCustomerIDFilter,
                models.RefundsListQueryParamCustomerIDFilterTypedDict,
            ]
        ] = UNSET,
        succeeded: OptionalNullable[bool] = UNSET,
        page: Optional[int] = 1,
        limit: Optional[int] = 10,
        sorting: OptionalNullable[List[models.RefundSortProperty]] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Optional[models.RefundsListResponse]:
        r"""List Refunds

        List products.

        :param id: Filter by refund ID.
        :param organization_id: Filter by organization ID.
        :param order_id: Filter by order ID.
        :param subscription_id: Filter by subscription ID.
        :param customer_id: Filter by customer ID.
        :param succeeded: Filter by `succeeded`.
        :param page: Page number, defaults to 1.
        :param limit: Size of a page, defaults to 10. Maximum is 100.
        :param sorting: Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.RefundsListRequest(
            id=id,
            organization_id=organization_id,
            order_id=order_id,
            subscription_id=subscription_id,
            customer_id=customer_id,
            succeeded=succeeded,
            page=page,
            limit=limit,
            sorting=sorting,
        )

        req = self._build_request_async(
            method="GET",
            path="/v1/refunds/",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="refunds:list",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        def next_func() -> Optional[models.RefundsListResponse]:
            body = utils.unmarshal_json(http_res.text, Dict[Any, Any])
            page = request.page if not request.page is None else 1
            next_page = page + 1

            num_pages = JSONPath("$.pagination.max_page").parse(body)
            if len(num_pages) == 0 or num_pages[0] <= page:
                return None

            if not http_res.text:
                return None
            results = JSONPath("$.items").parse(body)
            if len(results) == 0 or len(results[0]) == 0:
                return None
            limit = request.limit if not request.limit is None else 10
            if len(results[0]) < limit:
                return None

            return self.list(
                id=id,
                organization_id=organization_id,
                order_id=order_id,
                subscription_id=subscription_id,
                customer_id=customer_id,
                succeeded=succeeded,
                page=next_page,
                limit=limit,
                sorting=sorting,
                retries=retries,
            )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.RefundsListResponse(
                result=utils.unmarshal_json(http_res.text, models.ListResourceRefund),
                next=next_func,
            )
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def create(
        self,
        *,
        request: Union[models.RefundCreate, models.RefundCreateTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Optional[models.Refund]:
        r"""Create Refund

        Create a refund.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, models.RefundCreate)
        request = cast(models.RefundCreate, request)

        req = self._build_request(
            method="POST",
            path="/v1/refunds/",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.RefundCreate
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="refunds:create",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["400", "403", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.Refund)
        if utils.match_response(http_res, "201", "*"):
            return None
        if utils.match_response(http_res, "400", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.RefundAmountTooHighData)
            raise models.RefundAmountTooHigh(data=data)
        if utils.match_response(http_res, "403", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.RefundedAlreadyData)
            raise models.RefundedAlready(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def create_async(
        self,
        *,
        request: Union[models.RefundCreate, models.RefundCreateTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Optional[models.Refund]:
        r"""Create Refund

        Create a refund.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, models.RefundCreate)
        request = cast(models.RefundCreate, request)

        req = self._build_request_async(
            method="POST",
            path="/v1/refunds/",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.RefundCreate
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="refunds:create",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["400", "403", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.Refund)
        if utils.match_response(http_res, "201", "*"):
            return None
        if utils.match_response(http_res, "400", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.RefundAmountTooHighData)
            raise models.RefundAmountTooHigh(data=data)
        if utils.match_response(http_res, "403", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.RefundedAlreadyData)
            raise models.RefundedAlready(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )
