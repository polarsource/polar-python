"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from polar_sdk import models, utils
from polar_sdk._hooks import HookContext
from polar_sdk.types import OptionalNullable, UNSET
from polar_sdk.utils.unmarshal_json_response import unmarshal_json_response
from typing import Any, Mapping, Optional


class PolarOrganizations(BaseSDK):
    def get(
        self,
        *,
        slug: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.CustomerOrganization:
        r"""Get Organization

        Get a customer portal's organization by slug.

        :param slug: The organization slug.
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

        request = models.CustomerPortalOrganizationsGetRequest(
            slug=slug,
        )

        req = self._build_request(
            method="GET",
            path="/v1/customer-portal/organizations/{slug}",
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
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="customer_portal:organizations:get",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return unmarshal_json_response(models.CustomerOrganization, http_res)
        if utils.match_response(http_res, "404", "application/json"):
            response_data = unmarshal_json_response(
                models.ResourceNotFoundData, http_res
            )
            raise models.ResourceNotFound(response_data, http_res)
        if utils.match_response(http_res, "422", "application/json"):
            response_data = unmarshal_json_response(
                models.HTTPValidationErrorData, http_res
            )
            raise models.HTTPValidationError(response_data, http_res)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.SDKError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.SDKError("API error occurred", http_res, http_res_text)

        raise models.SDKError("Unexpected response received", http_res)

    async def get_async(
        self,
        *,
        slug: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.CustomerOrganization:
        r"""Get Organization

        Get a customer portal's organization by slug.

        :param slug: The organization slug.
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

        request = models.CustomerPortalOrganizationsGetRequest(
            slug=slug,
        )

        req = self._build_request_async(
            method="GET",
            path="/v1/customer-portal/organizations/{slug}",
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
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="customer_portal:organizations:get",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return unmarshal_json_response(models.CustomerOrganization, http_res)
        if utils.match_response(http_res, "404", "application/json"):
            response_data = unmarshal_json_response(
                models.ResourceNotFoundData, http_res
            )
            raise models.ResourceNotFound(response_data, http_res)
        if utils.match_response(http_res, "422", "application/json"):
            response_data = unmarshal_json_response(
                models.HTTPValidationErrorData, http_res
            )
            raise models.HTTPValidationError(response_data, http_res)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.SDKError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.SDKError("API error occurred", http_res, http_res_text)

        raise models.SDKError("Unexpected response received", http_res)
