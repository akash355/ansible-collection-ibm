#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_compute_vm_instance
short_description: Configure IBM Cloud 'ibm_compute_vm_instance' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_compute_vm_instance' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.7.1
    - Terraform v0.12.20

options:
    file_storage_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    domain:
        description:
            - None
        required: False
        type: str
    cores:
        description:
            - None
        required: False
        type: int
    dedicated_acct_host_only:
        description:
            - None
        required: False
        type: bool
    public_subnet_id:
        description:
            - None
        required: False
        type: int
    ip_address_id:
        description:
            - None
        required: False
        type: int
    ipv6_address:
        description:
            - None
        required: False
        type: str
    os_reference_code:
        description:
            - None
        required: False
        type: str
    datacenter:
        description:
            - None
        required: False
        type: str
    datacenter_choice:
        description:
            - The user provided datacenter options
        required: False
        type: list
        elements: dict
    private_interface_id:
        description:
            - None
        required: False
        type: int
    public_ipv6_subnet:
        description:
            - None
        required: False
        type: str
    notes:
        description:
            - None
        required: False
        type: str
    dedicated_host_name:
        description:
            - None
        required: False
        type: str
    public_subnet:
        description:
            - None
        required: False
        type: str
    evault:
        description:
            - None
        required: False
        type: int
    resource_name:
        description:
            - The name of the resource
        required: False
        type: str
    flavor_key_name:
        description:
            - Flavor key name used to provision vm.
        required: False
        type: str
    ipv6_address_id:
        description:
            - None
        required: False
        type: int
    secondary_ip_addresses:
        description:
            - None
        required: False
        type: list
        elements: str
    wait_time_minutes:
        description:
            - None
        required: False
        type: int
        default: 90
    hostname:
        description:
            - None
        required: False
        type: str
    private_vlan_id:
        description:
            - None
        required: False
        type: int
    public_ipv6_subnet_id:
        description:
            - None
        required: False
        type: str
    block_storage_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    image_id:
        description:
            - None
        required: False
        type: int
    transient:
        description:
            - None
        required: False
        type: bool
    user_metadata:
        description:
            - None
        required: False
        type: str
    local_disk:
        description:
            - None
        required: False
        type: bool
        default: True
    resource_status:
        description:
            - The status of the resource
        required: False
        type: str
    dedicated_host_id:
        description:
            - None
        required: False
        type: int
    private_subnet_id:
        description:
            - None
        required: False
        type: int
    memory:
        description:
            - None
        required: False
        type: int
    network_speed:
        description:
            - None
        required: False
        type: int
        default: 100
    secondary_ip_count:
        description:
            - None
        required: False
        type: int
    bulk_vms:
        description:
            - None
        required: False
        type: list
        elements: dict
    hourly_billing:
        description:
            - None
        required: False
        type: bool
        default: True
    ip_address_id_private:
        description:
            - None
        required: False
        type: int
    ipv6_static_enabled:
        description:
            - None
        required: False
        type: bool
        default: False
    ssh_key_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    public_bandwidth_limited:
        description:
            - None
        required: False
        type: int
    placement_group_id:
        description:
            - The placement group id
        required: False
        type: int
    resource_controller_url:
        description:
            - The URL of the IBM Cloud dashboard that can be used to explore and view details about this instance
        required: False
        type: str
    private_network_only:
        description:
            - None
        required: False
        type: bool
        default: False
    private_security_group_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    ipv4_address_private:
        description:
            - None
        required: False
        type: str
    public_bandwidth_unlimited:
        description:
            - None
        required: False
        type: bool
        default: False
    placement_group_name:
        description:
            - The placement group name
        required: False
        type: str
    public_security_group_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    ipv4_address:
        description:
            - None
        required: False
        type: str
    public_vlan_id:
        description:
            - None
        required: False
        type: int
    private_subnet:
        description:
            - None
        required: False
        type: str
    ipv6_enabled:
        description:
            - None
        required: False
        type: bool
        default: False
    public_interface_id:
        description:
            - None
        required: False
        type: int
    disks:
        description:
            - None
        required: False
        type: list
        elements: int
    post_install_script_uri:
        description:
            - None
        required: False
        type: str
    tags:
        description:
            - None
        required: False
        type: list
        elements: str
    id:
        description:
            - (Required when updating or destroying existing resource) IBM Cloud Resource ID.
        required: False
        type: str
    state:
        description:
            - State of resource
        choices:
            - available
            - absent
        default: available
        required: False
    iaas_classic_username:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure (SoftLayer) user name. This can also be provided
              via the environment variable 'IAAS_CLASSIC_USERNAME'.
        required: False
    iaas_classic_api_key:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure API key. This can also be provided via the
              environment variable 'IAAS_CLASSIC_API_KEY'.
        required: False
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
        required: False
    ibmcloud_api_key:
        description:
            - The IBM Cloud API key to authenticate with the IBM Cloud
              platform. This can also be provided via the environment
              variable 'IC_API_KEY'.
        required: True

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'file_storage_ids',
    'domain',
    'cores',
    'dedicated_acct_host_only',
    'public_subnet_id',
    'ip_address_id',
    'ipv6_address',
    'os_reference_code',
    'datacenter',
    'datacenter_choice',
    'private_interface_id',
    'public_ipv6_subnet',
    'notes',
    'dedicated_host_name',
    'public_subnet',
    'evault',
    'resource_name',
    'flavor_key_name',
    'ipv6_address_id',
    'secondary_ip_addresses',
    'wait_time_minutes',
    'hostname',
    'private_vlan_id',
    'public_ipv6_subnet_id',
    'block_storage_ids',
    'image_id',
    'transient',
    'user_metadata',
    'local_disk',
    'resource_status',
    'dedicated_host_id',
    'private_subnet_id',
    'memory',
    'network_speed',
    'secondary_ip_count',
    'bulk_vms',
    'hourly_billing',
    'ip_address_id_private',
    'ipv6_static_enabled',
    'ssh_key_ids',
    'public_bandwidth_limited',
    'placement_group_id',
    'resource_controller_url',
    'private_network_only',
    'private_security_group_ids',
    'ipv4_address_private',
    'public_bandwidth_unlimited',
    'placement_group_name',
    'public_security_group_ids',
    'ipv4_address',
    'public_vlan_id',
    'private_subnet',
    'ipv6_enabled',
    'public_interface_id',
    'disks',
    'post_install_script_uri',
    'tags',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibmcloud.ibmcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    file_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    domain=dict(
        required=False,
        type='str'),
    cores=dict(
        required=False,
        type='int'),
    dedicated_acct_host_only=dict(
        required=False,
        type='bool'),
    public_subnet_id=dict(
        required=False,
        type='int'),
    ip_address_id=dict(
        required=False,
        type='int'),
    ipv6_address=dict(
        required=False,
        type='str'),
    os_reference_code=dict(
        required=False,
        type='str'),
    datacenter=dict(
        required=False,
        type='str'),
    datacenter_choice=dict(
        required=False,
        elements='',
        type='list'),
    private_interface_id=dict(
        required=False,
        type='int'),
    public_ipv6_subnet=dict(
        required=False,
        type='str'),
    notes=dict(
        required=False,
        type='str'),
    dedicated_host_name=dict(
        required=False,
        type='str'),
    public_subnet=dict(
        required=False,
        type='str'),
    evault=dict(
        required=False,
        type='int'),
    resource_name=dict(
        required=False,
        type='str'),
    flavor_key_name=dict(
        required=False,
        type='str'),
    ipv6_address_id=dict(
        required=False,
        type='int'),
    secondary_ip_addresses=dict(
        required=False,
        elements='',
        type='list'),
    wait_time_minutes=dict(
        default=90,
        type='int'),
    hostname=dict(
        required=False,
        type='str'),
    private_vlan_id=dict(
        required=False,
        type='int'),
    public_ipv6_subnet_id=dict(
        required=False,
        type='str'),
    block_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    image_id=dict(
        required=False,
        type='int'),
    transient=dict(
        required=False,
        type='bool'),
    user_metadata=dict(
        required=False,
        type='str'),
    local_disk=dict(
        default=True,
        type='bool'),
    resource_status=dict(
        required=False,
        type='str'),
    dedicated_host_id=dict(
        required=False,
        type='int'),
    private_subnet_id=dict(
        required=False,
        type='int'),
    memory=dict(
        required=False,
        type='int'),
    network_speed=dict(
        default=100,
        type='int'),
    secondary_ip_count=dict(
        required=False,
        type='int'),
    bulk_vms=dict(
        required=False,
        elements='',
        type='list'),
    hourly_billing=dict(
        default=True,
        type='bool'),
    ip_address_id_private=dict(
        required=False,
        type='int'),
    ipv6_static_enabled=dict(
        default=False,
        type='bool'),
    ssh_key_ids=dict(
        required=False,
        elements='',
        type='list'),
    public_bandwidth_limited=dict(
        required=False,
        type='int'),
    placement_group_id=dict(
        required=False,
        type='int'),
    resource_controller_url=dict(
        required=False,
        type='str'),
    private_network_only=dict(
        default=False,
        type='bool'),
    private_security_group_ids=dict(
        required=False,
        elements='',
        type='list'),
    ipv4_address_private=dict(
        required=False,
        type='str'),
    public_bandwidth_unlimited=dict(
        default=False,
        type='bool'),
    placement_group_name=dict(
        required=False,
        type='str'),
    public_security_group_ids=dict(
        required=False,
        elements='',
        type='list'),
    ipv4_address=dict(
        required=False,
        type='str'),
    public_vlan_id=dict(
        required=False,
        type='int'),
    private_subnet=dict(
        required=False,
        type='str'),
    ipv6_enabled=dict(
        default=False,
        type='bool'),
    public_interface_id=dict(
        required=False,
        type='int'),
    disks=dict(
        required=False,
        elements='',
        type='list'),
    post_install_script_uri=dict(
        required=False,
        type='str'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    id=dict(
        required=False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
    iaas_classic_username=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_USERNAME']),
        required=False),
    iaas_classic_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_API_KEY']),
        required=False),
    region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True)
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # New resource required arguments checks
    missing_args = []
    if module.params['id'] is None:
        for arg, _ in TL_REQUIRED_PARAMETERS:
            if module.params[arg] is None:
                missing_args.append(arg)
        if missing_args:
            module.fail_json(msg=(
                "missing required arguments: " + ", ".join(missing_args)))

    result = ibmcloud_terraform(
        resource_type='ibm_compute_vm_instance',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.7.1',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
