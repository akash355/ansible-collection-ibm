
ibm_container_worker_pool -- Configure IBM Cloud 'ibm_container_worker_pool' resource
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_worker_pool' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.7.1
- Terraform v0.12.20



Parameters
----------

  state_ (False, str, None)
    worker pool state


  labels (False, dict, None)
    list of labels to worker pool


  resource_group_id (False, str, None)
    ID of the resource group.


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster


  machine_type (False, str, None)
    (Required for new resource) worker nodes machine type


  entitlement (False, str, None)
    Entitlement option reduces additional OCP Licence cost in Openshift Clusters


  hardware (False, str, shared)
    Hardware type


  disk_encryption (False, bool, True)
    worker node disk encrypted if set to true


  region (False, str, None)
    The worker pool region


  cluster (False, str, None)
    (Required for new resource) Cluster name


  worker_pool_name (False, str, None)
    (Required for new resource) worker pool name


  size_per_zone (False, int, None)
    (Required for new resource) Number of nodes per zone


  zones (False, list, None)
    None


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

