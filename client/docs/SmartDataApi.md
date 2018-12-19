# swagger_client.SmartDataApi

All URIs are relative to *https://localhost:8080/cs-739/DiskFailurePrediction/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_smart_nvme**](SmartDataApi.md#add_smart_nvme) | **POST** /smart-nvme | Upload NVME disk data
[**add_smart_ssd**](SmartDataApi.md#add_smart_ssd) | **POST** /smart-ssd | Upload ssd disk data
[**get_smart_nvme**](SmartDataApi.md#get_smart_nvme) | **GET** /smart-nvme | Get all NVME disk data
[**get_smart_ssd**](SmartDataApi.md#get_smart_ssd) | **GET** /smart-ssd | Get all ssd disk data


# **add_smart_nvme**
> list[SmartNvme] add_smart_nvme(smart_nvme, uuid=uuid)

Upload NVME disk data

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
api_instance = swagger_client.SmartDataApi(swagger_client.ApiClient(configuration))
smart_nvme = swagger_client.SmartNvme() # SmartNvme | Smartctl --json -x output to be added to dataset
uuid = 'uuid_example' # str | Unique User ID (optional)

try:
    # Upload NVME disk data
    api_response = api_instance.add_smart_nvme(smart_nvme, uuid=uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmartDataApi->add_smart_nvme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_nvme** | [**SmartNvme**](SmartNvme.md)| Smartctl --json -x output to be added to dataset | 
 **uuid** | **str**| Unique User ID | [optional] 

### Return type

[**list[SmartNvme]**](SmartNvme.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_smart_ssd**
> add_smart_ssd(smart_ssd, uuid=uuid)

Upload ssd disk data

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
api_instance = swagger_client.SmartDataApi(swagger_client.ApiClient(configuration))
smart_ssd = swagger_client.SmartSsd() # SmartSsd | Smartctl --json -x output to be added to dataset
uuid = 'uuid_example' # str | Unique User ID (optional)

try:
    # Upload ssd disk data
    api_instance.add_smart_ssd(smart_ssd, uuid=uuid)
except ApiException as e:
    print("Exception when calling SmartDataApi->add_smart_ssd: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_ssd** | [**SmartSsd**](SmartSsd.md)| Smartctl --json -x output to be added to dataset | 
 **uuid** | **str**| Unique User ID | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smart_nvme**
> get_smart_nvme()

Get all NVME disk data

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
api_instance = swagger_client.SmartDataApi(swagger_client.ApiClient(configuration))

try:
    # Get all NVME disk data
    api_instance.get_smart_nvme()
except ApiException as e:
    print("Exception when calling SmartDataApi->get_smart_nvme: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smart_ssd**
> list[SmartSsd] get_smart_ssd()

Get all ssd disk data

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
api_instance = swagger_client.SmartDataApi(swagger_client.ApiClient(configuration))

try:
    # Get all ssd disk data
    api_response = api_instance.get_smart_ssd()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmartDataApi->get_smart_ssd: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SmartSsd]**](SmartSsd.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

