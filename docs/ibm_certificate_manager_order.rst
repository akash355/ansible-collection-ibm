
ibm_certificate_manager_order -- Configure IBM Cloud 'ibm_certificate_manager_order' resource
=============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_certificate_manager_order' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.7.1
- Terraform v0.12.20



Parameters
----------

  domains (False, list, None)
    (Required for new resource) List of domain names


  dns_provider_instance_crn (False, str, None)
    DNS provider instance CRN


  issuer (False, str, None)
    Certificate issuer info


  key_algorithm (False, str, rsaEncryption 2048 bit)
    Keyalgorithm info


  begins_on (False, int, None)
    Cerificate validity from date


  expires_on (False, int, None)
    Certificaet expairy date


  certificate_manager_instance_id (False, str, None)
    (Required for new resource) Certificate manager instance ID


  status (False, str, None)
    Status  of the certificate


  has_previous (False, str, None)
    Has Previous


  imported (False, bool, None)
    set to true if certificate is imported


  issuance_info (False, dict, None)
    None


  algorithm (False, str, None)
    Algorithm info


  rotate_keys (False, bool, False)
    Keys are sorated if set to true


  description (False, str, None)
    Certicate description


  domain_validation_method (False, str, dns-01)
    Domain validation methods


  name (False, str, None)
    (Required for new resource) Certificate name


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

