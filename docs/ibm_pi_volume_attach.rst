
ibm_pi_volume_attach -- Configure IBM Cloud 'ibm_pi_volume_attach' resource
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_volume_attach' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.7.1
- Terraform v0.12.20



Parameters
----------

  status (False, str, None)
    None


  pi_volume_shareable (False, bool, None)
    None


  volumeattachid (False, str, None)
    Volume attachment ID


  pi_cloud_instance_id (False, str, None)
    (Required for new resource) Cloud Instance ID - This is the service_instance_id.


  pi_volume_attach_name (False, str, None)
    (Required for new resource) Name of the volume to attach. Note these  volumes should have been created


  pi_instance_name (False, str, None)
    (Required for new resource) PI Instance name


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  zone (False, str, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environment variable 'IC_ZONE'.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

