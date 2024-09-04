"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from jsonpath import JSONPath
from polar_sdk import models, utils
from polar_sdk._hooks import HookContext
from polar_sdk.types import BaseModel, OptionalNullable, UNSET
from typing import Any, Dict, Optional, Union, cast

class PolarLicenseKeys(BaseSDK):
    
    
    def list(
        self, *,
        organization_id: OptionalNullable[Union[models.UsersLicenseKeysListQueryParamOrganizationIDFilter, models.UsersLicenseKeysListQueryParamOrganizationIDFilterTypedDict]] = UNSET,
        benefit_id: OptionalNullable[str] = UNSET,
        page: Optional[int] = 1,
        limit: Optional[int] = 10,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> models.UsersLicenseKeysListResponse:
        r"""List License Keys

        :param organization_id: Filter by organization ID.
        :param benefit_id: Filter by a specific benefit
        :param page: Page number, defaults to 1.
        :param limit: Size of a page, defaults to 10. Maximum is 100.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        request = models.UsersLicenseKeysListRequest(
            organization_id=organization_id,
            benefit_id=benefit_id,
            page=page,
            limit=limit,
        )
        
        req = self.build_request(
            method="GET",
            path="/v1/users/license-keys/",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="users:license_keys:list", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["401","404","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        def next_func() -> Optional[models.UsersLicenseKeysListResponse]:
            body = utils.unmarshal_json(http_res.text, Dict[Any, Any])
            page = request.page if not request.page is None else 0
            next_page = page + 1
            
            num_pages = JSONPath("$.pagination.max_page").parse(body)
            if len(num_pages) == 0 or num_pages[0] <= page:
                return None

            if not http_res.text:
                return None
            results = JSONPath("$.items").parse(body)
            if len(results) == 0 or len(results[0]) == 0:
                return None
            limit = request.limit if not request.limit is None else 0
            if len(results[0]) < limit:
                return None

            return self.list(
                organization_id=organization_id,
                benefit_id=benefit_id,
                page=next_page,
                limit=limit,
                retries=retries,
            )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.UsersLicenseKeysListResponse(result=utils.unmarshal_json(http_res.text, Optional[models.ListResourceLicenseKeyRead]), next=next_func)
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.UnauthorizedData)
            raise models.Unauthorized(data=data)
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ResourceNotFoundData)
            raise models.ResourceNotFound(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def list_async(
        self, *,
        organization_id: OptionalNullable[Union[models.UsersLicenseKeysListQueryParamOrganizationIDFilter, models.UsersLicenseKeysListQueryParamOrganizationIDFilterTypedDict]] = UNSET,
        benefit_id: OptionalNullable[str] = UNSET,
        page: Optional[int] = 1,
        limit: Optional[int] = 10,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> models.UsersLicenseKeysListResponse:
        r"""List License Keys

        :param organization_id: Filter by organization ID.
        :param benefit_id: Filter by a specific benefit
        :param page: Page number, defaults to 1.
        :param limit: Size of a page, defaults to 10. Maximum is 100.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        request = models.UsersLicenseKeysListRequest(
            organization_id=organization_id,
            benefit_id=benefit_id,
            page=page,
            limit=limit,
        )
        
        req = self.build_request(
            method="GET",
            path="/v1/users/license-keys/",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="users:license_keys:list", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["401","404","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        def next_func() -> Optional[models.UsersLicenseKeysListResponse]:
            body = utils.unmarshal_json(http_res.text, Dict[Any, Any])
            page = request.page if not request.page is None else 0
            next_page = page + 1
            
            num_pages = JSONPath("$.pagination.max_page").parse(body)
            if len(num_pages) == 0 or num_pages[0] <= page:
                return None

            if not http_res.text:
                return None
            results = JSONPath("$.items").parse(body)
            if len(results) == 0 or len(results[0]) == 0:
                return None
            limit = request.limit if not request.limit is None else 0
            if len(results[0]) < limit:
                return None

            return self.list(
                organization_id=organization_id,
                benefit_id=benefit_id,
                page=next_page,
                limit=limit,
                retries=retries,
            )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.UsersLicenseKeysListResponse(result=utils.unmarshal_json(http_res.text, Optional[models.ListResourceLicenseKeyRead]), next=next_func)
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.UnauthorizedData)
            raise models.Unauthorized(data=data)
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ResourceNotFoundData)
            raise models.ResourceNotFound(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def get(
        self, *,
        id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.LicenseKeyWithActivations]:
        r"""Get License Key

        Get a license key.

        :param id: 
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        request = models.UsersLicenseKeysGetRequest(
            id=id,
        )
        
        req = self.build_request(
            method="GET",
            path="/v1/users/license-keys/{id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="users:license_keys:get", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["401","404","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.LicenseKeyWithActivations])
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.UnauthorizedData)
            raise models.Unauthorized(data=data)
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ResourceNotFoundData)
            raise models.ResourceNotFound(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def get_async(
        self, *,
        id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.LicenseKeyWithActivations]:
        r"""Get License Key

        Get a license key.

        :param id: 
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        request = models.UsersLicenseKeysGetRequest(
            id=id,
        )
        
        req = self.build_request(
            method="GET",
            path="/v1/users/license-keys/{id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="users:license_keys:get", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["401","404","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.LicenseKeyWithActivations])
        if utils.match_response(http_res, "401", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.UnauthorizedData)
            raise models.Unauthorized(data=data)
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ResourceNotFoundData)
            raise models.ResourceNotFound(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def validate(
        self, *,
        request: Union[models.LicenseKeyValidate, models.LicenseKeyValidateTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.ValidatedLicenseKey]:
        r"""Validate License Key

        Validate a license key.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, models.LicenseKeyValidate)
        request = cast(models.LicenseKeyValidate, request)
        
        req = self.build_request(
            method="POST",
            path="/v1/users/license-keys/validate",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, False, "json", models.LicenseKeyValidate),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="users:license_keys:validate", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["404","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.ValidatedLicenseKey])
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ResourceNotFoundData)
            raise models.ResourceNotFound(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def validate_async(
        self, *,
        request: Union[models.LicenseKeyValidate, models.LicenseKeyValidateTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.ValidatedLicenseKey]:
        r"""Validate License Key

        Validate a license key.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, models.LicenseKeyValidate)
        request = cast(models.LicenseKeyValidate, request)
        
        req = self.build_request(
            method="POST",
            path="/v1/users/license-keys/validate",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, False, "json", models.LicenseKeyValidate),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="users:license_keys:validate", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["404","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.ValidatedLicenseKey])
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ResourceNotFoundData)
            raise models.ResourceNotFound(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def activate(
        self, *,
        request: Union[models.LicenseKeyActivate, models.LicenseKeyActivateTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.LicenseKeyActivationRead]:
        r"""Activate License Key

        Activate a license key instance.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, models.LicenseKeyActivate)
        request = cast(models.LicenseKeyActivate, request)
        
        req = self.build_request(
            method="POST",
            path="/v1/users/license-keys/activate",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, False, "json", models.LicenseKeyActivate),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="users:license_keys:activate", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["403","404","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.LicenseKeyActivationRead])
        if utils.match_response(http_res, "403", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.NotPermittedData)
            raise models.NotPermitted(data=data)
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ResourceNotFoundData)
            raise models.ResourceNotFound(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def activate_async(
        self, *,
        request: Union[models.LicenseKeyActivate, models.LicenseKeyActivateTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.LicenseKeyActivationRead]:
        r"""Activate License Key

        Activate a license key instance.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, models.LicenseKeyActivate)
        request = cast(models.LicenseKeyActivate, request)
        
        req = self.build_request(
            method="POST",
            path="/v1/users/license-keys/activate",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, False, "json", models.LicenseKeyActivate),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="users:license_keys:activate", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["403","404","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.LicenseKeyActivationRead])
        if utils.match_response(http_res, "403", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.NotPermittedData)
            raise models.NotPermitted(data=data)
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ResourceNotFoundData)
            raise models.ResourceNotFound(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def deactivate(
        self, *,
        request: Union[models.LicenseKeyDeactivate, models.LicenseKeyDeactivateTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ):
        r"""Deactivate License Key

        Deactivate a license key instance.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, models.LicenseKeyDeactivate)
        request = cast(models.LicenseKeyDeactivate, request)
        
        req = self.build_request(
            method="POST",
            path="/v1/users/license-keys/deactivate",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, False, "json", models.LicenseKeyDeactivate),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="users:license_keys:deactivate", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["404","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "204", "*"):
            return
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ResourceNotFoundData)
            raise models.ResourceNotFound(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def deactivate_async(
        self, *,
        request: Union[models.LicenseKeyDeactivate, models.LicenseKeyDeactivateTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ):
        r"""Deactivate License Key

        Deactivate a license key instance.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, models.LicenseKeyDeactivate)
        request = cast(models.LicenseKeyDeactivate, request)
        
        req = self.build_request(
            method="POST",
            path="/v1/users/license-keys/deactivate",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, False, "json", models.LicenseKeyDeactivate),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="users:license_keys:deactivate", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["404","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "204", "*"):
            return
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ResourceNotFoundData)
            raise models.ResourceNotFound(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
