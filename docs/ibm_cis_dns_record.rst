
ibm_cis_dns_record -- Configure IBM Cloud 'ibm_cis_dns_record' resource
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cis_dns_record' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.7.1
- Terraform v0.12.20



Parameters
----------

  domain_id (False, str, None)
    (Required for new resource) Associated CIS domain


  name (False, str, None)
    DNS record name


  content (False, str, None)
    DNS record content


  priority (False, int, None)
    Priority Value


  proxiable (False, bool, None)
    None


  cis_id (False, str, None)
    (Required for new resource) CIS object id


  data (False, dict, None)
    None


  proxied (False, bool, False)
    Boolean value true if proxied else flase


  ttl (False, int, 1)
    TTL value


  created_on (False, str, None)
    None


  modified_on (False, str, None)
    None


  record_id (False, str, None)
    None


  type (False, str, None)
    (Required for new resource) Record type


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

