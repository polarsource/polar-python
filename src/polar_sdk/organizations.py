"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from jsonpath import JSONPath
from polar_sdk import models, utils
from polar_sdk._hooks import HookContext
from polar_sdk.types import BaseModel, OptionalNullable, UNSET
from typing import Any, Dict, List, Mapping, Optional, Union, cast


class Organizations(BaseSDK):
    def list(
        self,
        *,
        slug: OptionalNullable[str] = UNSET,
        page: Optional[int] = 1,
        limit: Optional[int] = 10,
        sorting: OptionalNullable[List[models.OrganizationSortProperty]] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Optional[models.OrganizationsListResponse]:
        r"""List Organizations

        List organizations.

        :param slug: Filter by slug.
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

        request = models.OrganizationsListRequest(
            slug=slug,
            page=page,
            limit=limit,
            sorting=sorting,
        )

        req = self._build_request(
            method="GET",
            path="/v1/organizations/",
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
                operation_id="organizations:list",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        def next_func() -> Optional[models.OrganizationsListResponse]:
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
                slug=slug,
                page=next_page,
                limit=limit,
                sorting=sorting,
                retries=retries,
            )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.OrganizationsListResponse(
                result=utils.unmarshal_json(
                    http_res.text, models.ListResourceOrganization
                ),
                next=next_func,
            )
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
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
        slug: OptionalNullable[str] = UNSET,
        page: Optional[int] = 1,
        limit: Optional[int] = 10,
        sorting: OptionalNullable[List[models.OrganizationSortProperty]] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Optional[models.OrganizationsListResponse]:
        r"""List Organizations

        List organizations.

        :param slug: Filter by slug.
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

        request = models.OrganizationsListRequest(
            slug=slug,
            page=page,
            limit=limit,
            sorting=sorting,
        )

        req = self._build_request_async(
            method="GET",
            path="/v1/organizations/",
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
                operation_id="organizations:list",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        def next_func() -> Optional[models.OrganizationsListResponse]:
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
                slug=slug,
                page=next_page,
                limit=limit,
                sorting=sorting,
                retries=retries,
            )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.OrganizationsListResponse(
                result=utils.unmarshal_json(
                    http_res.text, models.ListResourceOrganization
                ),
                next=next_func,
            )
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
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
        request: Union[models.OrganizationCreate, models.OrganizationCreateTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.Organization:
        r"""Create Organization

        Create an organization.

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
            request = utils.unmarshal(request, models.OrganizationCreate)
        request = cast(models.OrganizationCreate, request)

        req = self._build_request(
            method="POST",
            path="/v1/organizations/",
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
                request, False, False, "json", models.OrganizationCreate
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
                operation_id="organizations:create",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "201", "application/json"):
            return utils.unmarshal_json(http_res.text, models.Organization)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
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
        request: Union[models.OrganizationCreate, models.OrganizationCreateTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.Organization:
        r"""Create Organization

        Create an organization.

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
            request = utils.unmarshal(request, models.OrganizationCreate)
        request = cast(models.OrganizationCreate, request)

        req = self._build_request_async(
            method="POST",
            path="/v1/organizations/",
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
                request, False, False, "json", models.OrganizationCreate
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
                operation_id="organizations:create",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "201", "application/json"):
            return utils.unmarshal_json(http_res.text, models.Organization)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
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
        id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.Organization:
        r"""Get Organization

        Get an organization by ID.

        :param id:
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

        request = models.OrganizationsGetRequest(
            id=id,
        )

        req = self._build_request(
            method="GET",
            path="/v1/organizations/{id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
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
                operation_id="organizations:get",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.Organization)
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ResourceNotFoundData)
            raise models.ResourceNotFound(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
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
        id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.Organization:
        r"""Get Organization

        Get an organization by ID.

        :param id:
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

        request = models.OrganizationsGetRequest(
            id=id,
        )

        req = self._build_request_async(
            method="GET",
            path="/v1/organizations/{id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
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
                operation_id="organizations:get",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.Organization)
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ResourceNotFoundData)
            raise models.ResourceNotFound(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
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

    def update(
        self,
        *,
        id: str,
        organization_update: Union[
            models.OrganizationUpdate, models.OrganizationUpdateTypedDict
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.Organization:
        r"""Update Organization

        Update an organization.

        :param id:
        :param organization_update:
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

        request = models.OrganizationsUpdateRequest(
            id=id,
            organization_update=utils.get_pydantic_model(
                organization_update, models.OrganizationUpdate
            ),
        )

        req = self._build_request(
            method="PATCH",
            path="/v1/organizations/{id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.organization_update,
                False,
                False,
                "json",
                models.OrganizationUpdate,
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
                operation_id="organizations:update",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["403", "404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.Organization)
        if utils.match_response(http_res, "403", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.NotPermittedData)
            raise models.NotPermitted(data=data)
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ResourceNotFoundData)
            raise models.ResourceNotFound(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
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

    async def update_async(
        self,
        *,
        id: str,
        organization_update: Union[
            models.OrganizationUpdate, models.OrganizationUpdateTypedDict
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.Organization:
        r"""Update Organization

        Update an organization.

        :param id:
        :param organization_update:
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

        request = models.OrganizationsUpdateRequest(
            id=id,
            organization_update=utils.get_pydantic_model(
                organization_update, models.OrganizationUpdate
            ),
        )

        req = self._build_request_async(
            method="PATCH",
            path="/v1/organizations/{id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.organization_update,
                False,
                False,
                "json",
                models.OrganizationUpdate,
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
                operation_id="organizations:update",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["403", "404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.Organization)
        if utils.match_response(http_res, "403", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.NotPermittedData)
            raise models.NotPermitted(data=data)
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ResourceNotFoundData)
            raise models.ResourceNotFound(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
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
