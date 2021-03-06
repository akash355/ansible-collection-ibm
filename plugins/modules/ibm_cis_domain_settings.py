#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_cis_domain_settings
short_description: Configure IBM Cloud 'ibm_cis_domain_settings' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_cis_domain_settings' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.7.1
    - Terraform v0.12.20

options:
    always_use_https:
        description:
            - always_use_https setting
        required: False
        type: str
    hotlink_protection:
        description:
            - hotlink_protection setting
        required: False
        type: str
    websockets:
        description:
            - websockets setting
        required: False
        type: str
    script_load_optimization:
        description:
            - script_load_optimization setting
        required: False
        type: str
    browser_check:
        description:
            - browser_check setting
        required: False
        type: str
    image_load_optimization:
        description:
            - image_load_optimization setting
        required: False
        type: str
    pseudo_ipv4:
        description:
            - pseudo_ipv4 setting
        required: False
        type: str
    tls_client_auth:
        description:
            - tls_client_auth setting
        required: False
        type: str
    true_client_ip_header:
        description:
            - true_client_ip_header setting
        required: False
        type: str
    cis_id:
        description:
            - (Required for new resource) CIS instance crn
        required: False
        type: str
    opportunistic_encryption:
        description:
            - opportunistic_encryption setting
        required: False
        type: str
    cname_flattening:
        description:
            - cname_flattening setting
        required: False
        type: str
    image_size_optimization:
        description:
            - image_size_optimization setting
        required: False
        type: str
    response_buffering:
        description:
            - response_buffering setting
        required: False
        type: str
    domain_id:
        description:
            - (Required for new resource) Associated CIS domain
        required: False
        type: str
    ipv6:
        description:
            - ipv6 setting
        required: False
        type: str
    ip_geolocation:
        description:
            - ip_geolocation setting
        required: False
        type: str
    prefetch_preload:
        description:
            - prefetch_preload setting
        required: False
        type: str
    ssl:
        description:
            - SSL/TLS setting
        required: False
        type: str
    min_tls_version:
        description:
            - Minimum version of TLS required
        required: False
        type: str
        default: 1.1
    http2:
        description:
            - http2 setting
        required: False
        type: str
    server_side_exclude:
        description:
            - server_side_exclude setting
        required: False
        type: str
    brotli:
        description:
            - brotli setting
        required: False
        type: str
    waf:
        description:
            - WAF setting
        required: False
        type: str
    certificate_status:
        description:
            - Certificate status
        required: False
        type: str
    automatic_https_rewrites:
        description:
            - automatic_https_rewrites setting
        required: False
        type: str
    origin_error_page_pass_thru:
        description:
            - origin_error_page_pass_thru setting
        required: False
        type: str
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
    ('cis_id', 'str'),
    ('domain_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'always_use_https',
    'hotlink_protection',
    'websockets',
    'script_load_optimization',
    'browser_check',
    'image_load_optimization',
    'pseudo_ipv4',
    'tls_client_auth',
    'true_client_ip_header',
    'cis_id',
    'opportunistic_encryption',
    'cname_flattening',
    'image_size_optimization',
    'response_buffering',
    'domain_id',
    'ipv6',
    'ip_geolocation',
    'prefetch_preload',
    'ssl',
    'min_tls_version',
    'http2',
    'server_side_exclude',
    'brotli',
    'waf',
    'certificate_status',
    'automatic_https_rewrites',
    'origin_error_page_pass_thru',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibmcloud.ibmcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    always_use_https=dict(
        required=False,
        type='str'),
    hotlink_protection=dict(
        required=False,
        type='str'),
    websockets=dict(
        required=False,
        type='str'),
    script_load_optimization=dict(
        required=False,
        type='str'),
    browser_check=dict(
        required=False,
        type='str'),
    image_load_optimization=dict(
        required=False,
        type='str'),
    pseudo_ipv4=dict(
        required=False,
        type='str'),
    tls_client_auth=dict(
        required=False,
        type='str'),
    true_client_ip_header=dict(
        required=False,
        type='str'),
    cis_id=dict(
        required=False,
        type='str'),
    opportunistic_encryption=dict(
        required=False,
        type='str'),
    cname_flattening=dict(
        required=False,
        type='str'),
    image_size_optimization=dict(
        required=False,
        type='str'),
    response_buffering=dict(
        required=False,
        type='str'),
    domain_id=dict(
        required=False,
        type='str'),
    ipv6=dict(
        required=False,
        type='str'),
    ip_geolocation=dict(
        required=False,
        type='str'),
    prefetch_preload=dict(
        required=False,
        type='str'),
    ssl=dict(
        required=False,
        type='str'),
    min_tls_version=dict(
        default='1.1',
        type='str'),
    http2=dict(
        required=False,
        type='str'),
    server_side_exclude=dict(
        required=False,
        type='str'),
    brotli=dict(
        required=False,
        type='str'),
    waf=dict(
        required=False,
        type='str'),
    certificate_status=dict(
        required=False,
        type='str'),
    automatic_https_rewrites=dict(
        required=False,
        type='str'),
    origin_error_page_pass_thru=dict(
        required=False,
        type='str'),
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
        resource_type='ibm_cis_domain_settings',
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
