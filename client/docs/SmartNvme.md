# SmartNvme

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_format_version** | **list[int]** |  | [optional] 
**smartctl** | [**SmartNvmeSmartctl**](SmartNvmeSmartctl.md) |  | [optional] 
**device** | [**SmartNvmeDevice**](SmartNvmeDevice.md) |  | [optional] 
**model_name** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**firmware_version** | **str** |  | [optional] 
**nvme_pci_vendor** | [**SmartNvmeNvmePciVendor**](SmartNvmeNvmePciVendor.md) |  | [optional] 
**nvme_ieee_oui_identifier** | **int** |  | [optional] 
**nvme_controller_id** | **int** |  | [optional] 
**nvme_number_of_namespaces** | **int** |  | [optional] 
**nvme_namespaces** | [**list[SmartNvmeNvmeNamespaces]**](SmartNvmeNvmeNamespaces.md) |  | [optional] 
**user_capacity** | [**SmartNvmeSize**](SmartNvmeSize.md) |  | [optional] 
**logical_block_size** | **int** |  | [optional] 
**local_time** | [**SmartNvmeLocalTime**](SmartNvmeLocalTime.md) |  | [optional] 
**smart_status** | [**SmartNvmeSmartStatus**](SmartNvmeSmartStatus.md) |  | [optional] 
**nvme_smart_health_information_log** | [**SmartNvmeNvmeSmartHealthInformationLog**](SmartNvmeNvmeSmartHealthInformationLog.md) |  | [optional] 
**temperature** | [**SmartNvmeTemperature**](SmartNvmeTemperature.md) |  | [optional] 
**power_cycle_count** | **int** |  | [optional] 
**power_on_time** | [**SmartNvmePowerOnTime**](SmartNvmePowerOnTime.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


