"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from jsonpath import JSONPath
from polar_sdk import models, utils
from polar_sdk._hooks import HookContext
from polar_sdk.types import OptionalNullable, UNSET
from typing import Any, Dict, List, Mapping, Optional, Union


class PolarOrders(BaseSDK):
    def list(
        self,
        *,
        security: Union[
            models.CustomerPortalOrdersListSecurity,
            models.CustomerPortalOrdersListSecurityTypedDict,
        ],
        organization_id: OptionalNullable[
            Union[
                models.CustomerPortalOrdersListQueryParamOrganizationIDFilter,
                models.CustomerPortalOrdersListQueryParamOrganizationIDFilterTypedDict,
            ]
        ] = UNSET,
        product_id: OptionalNullable[
            Union[
                models.CustomerPortalOrdersListQueryParamProductIDFilter,
                models.CustomerPortalOrdersListQueryParamProductIDFilterTypedDict,
            ]
        ] = UNSET,
        product_billing_type: OptionalNullable[
            Union[
                models.CustomerPortalOrdersListQueryParamProductBillingTypeFilter,
                models.CustomerPortalOrdersListQueryParamProductBillingTypeFilterTypedDict,
            ]
        ] = UNSET,
        subscription_id: OptionalNullable[
            Union[
                models.CustomerPortalOrdersListQueryParamSubscriptionIDFilter,
                models.CustomerPortalOrdersListQueryParamSubscriptionIDFilterTypedDict,
            ]
        ] = UNSET,
        query: OptionalNullable[str] = UNSET,
        page: Optional[int] = 1,
        limit: Optional[int] = 10,
        sorting: OptionalNullable[List[models.CustomerOrderSortProperty]] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Optional[models.CustomerPortalOrdersListResponse]:
        r"""List Orders

        List orders of the authenticated customer.

        **Scopes**: `customer_portal:read` `customer_portal:write`

        :param security:
        :param organization_id: Filter by organization ID.
        :param product_id: Filter by product ID.
        :param product_billing_type: Filter by product billing type. `recurring` will filter data corresponding to subscriptions creations or renewals. `one_time` will filter data corresponding to one-time purchases.
        :param subscription_id: Filter by subscription ID.
        :param query: Search by product or organization name.
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
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.CustomerPortalOrdersListRequest(
            organization_id=organization_id,
            product_id=product_id,
            product_billing_type=product_billing_type,
            subscription_id=subscription_id,
            query=query,
            page=page,
            limit=limit,
            sorting=sorting,
        )

        req = self._build_request(
            method="GET",
            path="/v1/customer-portal/orders/",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=utils.get_pydantic_model(
                security, models.CustomerPortalOrdersListSecurity
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
                base_url=base_url or "",
                operation_id="customer_portal:orders:list",
                oauth2_scopes=None,
                security_source=security,
            ),
            request=req,
            error_status_codes=["422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        def next_func() -> Optional[models.CustomerPortalOrdersListResponse]:
            body = utils.unmarshal_json(http_res.text, Union[Dict[Any, Any], List[Any]])
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
                security=security,
                organization_id=organization_id,
                product_id=product_id,
                product_billing_type=product_billing_type,
                subscription_id=subscription_id,
                query=query,
                page=next_page,
                limit=limit,
                sorting=sorting,
                retries=retries,
            )

        response_data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.CustomerPortalOrdersListResponse(
                result=utils.unmarshal_json(
                    http_res.text, models.ListResourceCustomerOrder
                ),
                next=next_func,
            )
        if utils.match_response(http_res, "422", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.HTTPValidationErrorData
            )
            raise models.HTTPValidationError(data=response_data)
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
        security: Union[
            models.CustomerPortalOrdersListSecurity,
            models.CustomerPortalOrdersListSecurityTypedDict,
        ],
        organization_id: OptionalNullable[
            Union[
                models.CustomerPortalOrdersListQueryParamOrganizationIDFilter,
                models.CustomerPortalOrdersListQueryParamOrganizationIDFilterTypedDict,
            ]
        ] = UNSET,
        product_id: OptionalNullable[
            Union[
                models.CustomerPortalOrdersListQueryParamProductIDFilter,
                models.CustomerPortalOrdersListQueryParamProductIDFilterTypedDict,
            ]
        ] = UNSET,
        product_billing_type: OptionalNullable[
            Union[
                models.CustomerPortalOrdersListQueryParamProductBillingTypeFilter,
                models.CustomerPortalOrdersListQueryParamProductBillingTypeFilterTypedDict,
            ]
        ] = UNSET,
        subscription_id: OptionalNullable[
            Union[
                models.CustomerPortalOrdersListQueryParamSubscriptionIDFilter,
                models.CustomerPortalOrdersListQueryParamSubscriptionIDFilterTypedDict,
            ]
        ] = UNSET,
        query: OptionalNullable[str] = UNSET,
        page: Optional[int] = 1,
        limit: Optional[int] = 10,
        sorting: OptionalNullable[List[models.CustomerOrderSortProperty]] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Optional[models.CustomerPortalOrdersListResponse]:
        r"""List Orders

        List orders of the authenticated customer.

        **Scopes**: `customer_portal:read` `customer_portal:write`

        :param security:
        :param organization_id: Filter by organization ID.
        :param product_id: Filter by product ID.
        :param product_billing_type: Filter by product billing type. `recurring` will filter data corresponding to subscriptions creations or renewals. `one_time` will filter data corresponding to one-time purchases.
        :param subscription_id: Filter by subscription ID.
        :param query: Search by product or organization name.
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
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.CustomerPortalOrdersListRequest(
            organization_id=organization_id,
            product_id=product_id,
            product_billing_type=product_billing_type,
            subscription_id=subscription_id,
            query=query,
            page=page,
            limit=limit,
            sorting=sorting,
        )

        req = self._build_request_async(
            method="GET",
            path="/v1/customer-portal/orders/",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=utils.get_pydantic_model(
                security, models.CustomerPortalOrdersListSecurity
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
                base_url=base_url or "",
                operation_id="customer_portal:orders:list",
                oauth2_scopes=None,
                security_source=security,
            ),
            request=req,
            error_status_codes=["422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        def next_func() -> Optional[models.CustomerPortalOrdersListResponse]:
            body = utils.unmarshal_json(http_res.text, Union[Dict[Any, Any], List[Any]])
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
                security=security,
                organization_id=organization_id,
                product_id=product_id,
                product_billing_type=product_billing_type,
                subscription_id=subscription_id,
                query=query,
                page=next_page,
                limit=limit,
                sorting=sorting,
                retries=retries,
            )

        response_data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.CustomerPortalOrdersListResponse(
                result=utils.unmarshal_json(
                    http_res.text, models.ListResourceCustomerOrder
                ),
                next=next_func,
            )
        if utils.match_response(http_res, "422", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.HTTPValidationErrorData
            )
            raise models.HTTPValidationError(data=response_data)
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

    def get(
        self,
        *,
        security: Union[
            models.CustomerPortalOrdersGetSecurity,
            models.CustomerPortalOrdersGetSecurityTypedDict,
        ],
        id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.CustomerOrder:
        r"""Get Order

        Get an order by ID for the authenticated customer.

        **Scopes**: `customer_portal:read` `customer_portal:write`

        :param security:
        :param id: The order ID.
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
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.CustomerPortalOrdersGetRequest(
            id=id,
        )

        req = self._build_request(
            method="GET",
            path="/v1/customer-portal/orders/{id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=utils.get_pydantic_model(
                security, models.CustomerPortalOrdersGetSecurity
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
                base_url=base_url or "",
                operation_id="customer_portal:orders:get",
                oauth2_scopes=None,
                security_source=security,
            ),
            request=req,
            error_status_codes=["404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.CustomerOrder)
        if utils.match_response(http_res, "404", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.ResourceNotFoundData
            )
            raise models.ResourceNotFound(data=response_data)
        if utils.match_response(http_res, "422", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.HTTPValidationErrorData
            )
            raise models.HTTPValidationError(data=response_data)
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

    async def get_async(
        self,
        *,
        security: Union[
            models.CustomerPortalOrdersGetSecurity,
            models.CustomerPortalOrdersGetSecurityTypedDict,
        ],
        id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.CustomerOrder:
        r"""Get Order

        Get an order by ID for the authenticated customer.

        **Scopes**: `customer_portal:read` `customer_portal:write`

        :param security:
        :param id: The order ID.
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
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.CustomerPortalOrdersGetRequest(
            id=id,
        )

        req = self._build_request_async(
            method="GET",
            path="/v1/customer-portal/orders/{id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=utils.get_pydantic_model(
                security, models.CustomerPortalOrdersGetSecurity
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
                base_url=base_url or "",
                operation_id="customer_portal:orders:get",
                oauth2_scopes=None,
                security_source=security,
            ),
            request=req,
            error_status_codes=["404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.CustomerOrder)
        if utils.match_response(http_res, "404", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.ResourceNotFoundData
            )
            raise models.ResourceNotFound(data=response_data)
        if utils.match_response(http_res, "422", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.HTTPValidationErrorData
            )
            raise models.HTTPValidationError(data=response_data)
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

    def invoice(
        self,
        *,
        security: Union[
            models.CustomerPortalOrdersInvoiceSecurity,
            models.CustomerPortalOrdersInvoiceSecurityTypedDict,
        ],
        id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.CustomerOrderInvoice:
        r"""Get Order Invoice

        Get an order's invoice data.

        **Scopes**: `customer_portal:read` `customer_portal:write`

        :param security:
        :param id: The order ID.
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
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.CustomerPortalOrdersInvoiceRequest(
            id=id,
        )

        req = self._build_request(
            method="GET",
            path="/v1/customer-portal/orders/{id}/invoice",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=utils.get_pydantic_model(
                security, models.CustomerPortalOrdersInvoiceSecurity
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
                base_url=base_url or "",
                operation_id="customer_portal:orders:invoice",
                oauth2_scopes=None,
                security_source=security,
            ),
            request=req,
            error_status_codes=["404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.CustomerOrderInvoice)
        if utils.match_response(http_res, "404", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.ResourceNotFoundData
            )
            raise models.ResourceNotFound(data=response_data)
        if utils.match_response(http_res, "422", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.HTTPValidationErrorData
            )
            raise models.HTTPValidationError(data=response_data)
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

    async def invoice_async(
        self,
        *,
        security: Union[
            models.CustomerPortalOrdersInvoiceSecurity,
            models.CustomerPortalOrdersInvoiceSecurityTypedDict,
        ],
        id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.CustomerOrderInvoice:
        r"""Get Order Invoice

        Get an order's invoice data.

        **Scopes**: `customer_portal:read` `customer_portal:write`

        :param security:
        :param id: The order ID.
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
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.CustomerPortalOrdersInvoiceRequest(
            id=id,
        )

        req = self._build_request_async(
            method="GET",
            path="/v1/customer-portal/orders/{id}/invoice",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=utils.get_pydantic_model(
                security, models.CustomerPortalOrdersInvoiceSecurity
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
                base_url=base_url or "",
                operation_id="customer_portal:orders:invoice",
                oauth2_scopes=None,
                security_source=security,
            ),
            request=req,
            error_status_codes=["404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.CustomerOrderInvoice)
        if utils.match_response(http_res, "404", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.ResourceNotFoundData
            )
            raise models.ResourceNotFound(data=response_data)
        if utils.match_response(http_res, "422", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.HTTPValidationErrorData
            )
            raise models.HTTPValidationError(data=response_data)
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
