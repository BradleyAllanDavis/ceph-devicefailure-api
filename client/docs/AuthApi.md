# swagger_client.AuthApi

All URIs are relative to *https://localhost:8080/cs-739/DiskFailurePrediction/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_auth**](AuthApi.md#get_auth) | **POST** /auth | Generate new UUID and API Key


# **get_auth**
> InlineResponse200 get_auth(uuid=uuid)

Generate new UUID and API Key

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
uuid = 'uuid_example' # str | Unique User ID (optional)

try:
    # Generate new UUID and API Key
    api_response = api_instance.get_auth(uuid=uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Unique User ID | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

