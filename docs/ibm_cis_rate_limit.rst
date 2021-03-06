
ibm_cis_rate_limit -- Configure IBM Cloud 'ibm_cis_rate_limit' resource
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cis_rate_limit' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.7.1
- Terraform v0.12.20



Parameters
----------

  threshold (False, int, None)
    (Required for new resource) Rate Limiting Threshold


  disabled (False, bool, False)
    Whether this rate limiting rule is currently disabled.


  description (False, str, None)
    A note that you can use to describe the reason for a rate limiting rule.


  bypass (False, list, None)
    Bypass URL


  period (False, int, None)
    (Required for new resource) Rate Limiting Period


  correlate (False, list, None)
    Ratelimiting Correlate


  action (False, list, None)
    (Required for new resource) Rate Limiting Action


  cis_id (False, str, None)
    (Required for new resource) CIS Intance CRN


  domain_id (False, str, None)
    (Required for new resource) CIS Domain ID


  match (False, list, None)
    Rate Limiting Match


  rule_id (False, str, None)
    Rate Limit rule Id


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

