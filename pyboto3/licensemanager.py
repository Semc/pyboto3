'''

The MIT License (MIT)

Copyright (c) 2016 WavyCloud

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').

    """
    pass

def create_license_configuration(Name=None, Description=None, LicenseCountingType=None, LicenseCount=None, LicenseCountHardLimit=None, LicenseRules=None, Tags=None):
    """
    Creates a new license configuration object. A license configuration is an abstraction of a customer license agreement that can be consumed and enforced by License Manager. Components include specifications for the license type (licensing by instance, socket, CPU, or VCPU), tenancy (shared tenancy, Amazon EC2 Dedicated Instance, Amazon EC2 Dedicated Host, or any of these), host affinity (how long a VM must be associated with a host), the number of licenses purchased and used.
    See also: AWS API Documentation
    
    
    :example: response = client.create_license_configuration(
        Name='string',
        Description='string',
        LicenseCountingType='vCPU'|'Instance'|'Core'|'Socket',
        LicenseCount=123,
        LicenseCountHardLimit=True|False,
        LicenseRules=[
            'string',
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Name of the license configuration.
            

    :type Description: string
    :param Description: Human-friendly description of the license configuration.

    :type LicenseCountingType: string
    :param LicenseCountingType: [REQUIRED]
            Dimension to use to track the license inventory.
            

    :type LicenseCount: integer
    :param LicenseCount: Number of licenses managed by the license configuration.

    :type LicenseCountHardLimit: boolean
    :param LicenseCountHardLimit: Flag indicating whether hard or soft license enforcement is used. Exceeding a hard limit results in the blocked deployment of new instances.

    :type LicenseRules: list
    :param LicenseRules: Array of configured License Manager rules.
            (string) --
            

    :type Tags: list
    :param Tags: The tags to apply to the resources during launch. You can only tag instances and volumes on launch. The specified tags are applied to all instances or volumes that are created during launch. To tag a resource after it has been created, see CreateTags .
            (dict) --Tag for a resource in a key-value format.
            Key (string) --Key for the resource tag.
            Value (string) --Value for the resource tag.
            
            

    :rtype: dict
    :return: {
        'LicenseConfigurationArn': 'string'
    }
    
    
    """
    pass

def delete_license_configuration(LicenseConfigurationArn=None):
    """
    Deletes an existing license configuration. This action fails if the configuration is in use.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_license_configuration(
        LicenseConfigurationArn='string'
    )
    
    
    :type LicenseConfigurationArn: string
    :param LicenseConfigurationArn: [REQUIRED]
            Unique ID of the configuration object to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def generate_presigned_url(ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
    """
    Generate a presigned url given a client, its method, and arguments
    
    :type ClientMethod: string
    :param ClientMethod: The client method to presign for

    :type Params: dict
    :param Params: The parameters normally passed to
            ClientMethod.

    :type ExpiresIn: int
    :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)

    :type HttpMethod: string
    :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.

    """
    pass

def get_license_configuration(LicenseConfigurationArn=None):
    """
    Returns a detailed description of a license configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.get_license_configuration(
        LicenseConfigurationArn='string'
    )
    
    
    :type LicenseConfigurationArn: string
    :param LicenseConfigurationArn: [REQUIRED]
            ARN of the license configuration being requested.
            

    :rtype: dict
    :return: {
        'LicenseConfigurationId': 'string',
        'LicenseConfigurationArn': 'string',
        'Name': 'string',
        'Description': 'string',
        'LicenseCountingType': 'vCPU'|'Instance'|'Core'|'Socket',
        'LicenseRules': [
            'string',
        ],
        'LicenseCount': 123,
        'LicenseCountHardLimit': True|False,
        'ConsumedLicenses': 123,
        'Status': 'string',
        'OwnerAccountId': 'string',
        'ConsumedLicenseSummaryList': [
            {
                'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI',
                'ConsumedLicenses': 123
            },
        ],
        'ManagedResourceSummaryList': [
            {
                'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI',
                'AssociationCount': 123
            },
        ],
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def get_paginator(operation_name=None):
    """
    Create a paginator for an operation.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').

    :rtype: L{botocore.paginate.Paginator}
    """
    pass

def get_service_settings():
    """
    Gets License Manager settings for a region. Exposes the configured S3 bucket, SNS topic, etc., for inspection.
    See also: AWS API Documentation
    
    
    :example: response = client.get_service_settings()
    
    
    :rtype: dict
    :return: {
        'S3BucketArn': 'string',
        'SnsTopicArn': 'string',
        'OrganizationConfiguration': {
            'EnableIntegration': True|False
        },
        'EnableCrossAccountsDiscovery': True|False
    }
    
    
    """
    pass

def get_waiter(waiter_name=None):
    """
    Returns an object that can wait for some condition.
    
    :type waiter_name: str
    :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.

    :rtype: botocore.waiter.Waiter
    """
    pass

def list_associations_for_license_configuration(LicenseConfigurationArn=None, MaxResults=None, NextToken=None):
    """
    Lists the resource associations for a license configuration. Resource associations need not consume licenses from a license configuration. For example, an AMI or a stopped instance may not consume a license (depending on the license rules). Use this operation to find all resources associated with a license configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.list_associations_for_license_configuration(
        LicenseConfigurationArn='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type LicenseConfigurationArn: string
    :param LicenseConfigurationArn: [REQUIRED]
            ARN of a LicenseConfiguration object.
            

    :type MaxResults: integer
    :param MaxResults: Maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value.

    :type NextToken: string
    :param NextToken: Token for the next set of results.

    :rtype: dict
    :return: {
        'LicenseConfigurationAssociations': [
            {
                'ResourceArn': 'string',
                'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI',
                'ResourceOwnerId': 'string',
                'AssociationTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_license_configurations(LicenseConfigurationArns=None, MaxResults=None, NextToken=None, Filters=None):
    """
    Lists license configuration objects for an account, each containing the name, description, license type, and other license terms modeled from a license agreement.
    See also: AWS API Documentation
    
    
    :example: response = client.list_license_configurations(
        LicenseConfigurationArns=[
            'string',
        ],
        MaxResults=123,
        NextToken='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type LicenseConfigurationArns: list
    :param LicenseConfigurationArns: An array of ARNs for the calling account s license configurations.
            (string) --
            

    :type MaxResults: integer
    :param MaxResults: Maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value.

    :type NextToken: string
    :param NextToken: Token for the next set of results.

    :type Filters: list
    :param Filters: One or more filters.
            (dict) --A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a Describe operation are documented with the Describe operation.
            Name (string) --Name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :rtype: dict
    :return: {
        'LicenseConfigurations': [
            {
                'LicenseConfigurationId': 'string',
                'LicenseConfigurationArn': 'string',
                'Name': 'string',
                'Description': 'string',
                'LicenseCountingType': 'vCPU'|'Instance'|'Core'|'Socket',
                'LicenseRules': [
                    'string',
                ],
                'LicenseCount': 123,
                'LicenseCountHardLimit': True|False,
                'ConsumedLicenses': 123,
                'Status': 'string',
                'OwnerAccountId': 'string',
                'ConsumedLicenseSummaryList': [
                    {
                        'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI',
                        'ConsumedLicenses': 123
                    },
                ],
                'ManagedResourceSummaryList': [
                    {
                        'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI',
                        'AssociationCount': 123
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_license_specifications_for_resource(ResourceArn=None, MaxResults=None, NextToken=None):
    """
    Returns the license configuration for a resource.
    See also: AWS API Documentation
    
    
    :example: response = client.list_license_specifications_for_resource(
        ResourceArn='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            ARN of an AMI or Amazon EC2 instance that has an associated license configuration.
            

    :type MaxResults: integer
    :param MaxResults: Maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value.

    :type NextToken: string
    :param NextToken: Token for the next set of results.

    :rtype: dict
    :return: {
        'LicenseSpecifications': [
            {
                'LicenseConfigurationArn': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_resource_inventory(MaxResults=None, NextToken=None, Filters=None):
    """
    Returns a detailed list of resources.
    See also: AWS API Documentation
    
    
    :example: response = client.list_resource_inventory(
        MaxResults=123,
        NextToken='string',
        Filters=[
            {
                'Name': 'string',
                'Condition': 'EQUALS'|'NOT_EQUALS'|'BEGINS_WITH'|'CONTAINS',
                'Value': 'string'
            },
        ]
    )
    
    
    :type MaxResults: integer
    :param MaxResults: Maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value.

    :type NextToken: string
    :param NextToken: Token for the next set of results.

    :type Filters: list
    :param Filters: One or more filters.
            (dict) --An inventory filter object.
            Name (string) -- [REQUIRED]The name of the filter.
            Condition (string) -- [REQUIRED]The condition of the filter.
            Value (string) --Value of the filter.
            
            

    :rtype: dict
    :return: {
        'ResourceInventoryList': [
            {
                'ResourceId': 'string',
                'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI',
                'ResourceArn': 'string',
                'Platform': 'string',
                'PlatformVersion': 'string',
                'ResourceOwningAccountId': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_tags_for_resource(ResourceArn=None):
    """
    Lists tags attached to a resource.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            ARN for the resource.
            

    :rtype: dict
    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_usage_for_license_configuration(LicenseConfigurationArn=None, MaxResults=None, NextToken=None, Filters=None):
    """
    Lists all license usage records for a license configuration, displaying license consumption details by resource at a selected point in time. Use this action to audit the current license consumption for any license inventory and configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.list_usage_for_license_configuration(
        LicenseConfigurationArn='string',
        MaxResults=123,
        NextToken='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type LicenseConfigurationArn: string
    :param LicenseConfigurationArn: [REQUIRED]
            ARN of the targeted LicenseConfiguration object.
            

    :type MaxResults: integer
    :param MaxResults: Maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value.

    :type NextToken: string
    :param NextToken: Token for the next set of results.

    :type Filters: list
    :param Filters: List of filters to apply.
            (dict) --A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a Describe operation are documented with the Describe operation.
            Name (string) --Name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :rtype: dict
    :return: {
        'LicenseConfigurationUsageList': [
            {
                'ResourceArn': 'string',
                'ResourceType': 'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI',
                'ResourceStatus': 'string',
                'ResourceOwnerId': 'string',
                'AssociationTime': datetime(2015, 1, 1),
                'ConsumedLicenses': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Attach one of more tags to any resource.
    See also: AWS API Documentation
    
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            Resource of the ARN to be tagged.
            

    :type Tags: list
    :param Tags: [REQUIRED]
            Names of the tags to attach to the resource.
            (dict) --Tag for a resource in a key-value format.
            Key (string) --Key for the resource tag.
            Value (string) --Value for the resource tag.
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Remove tags from a resource.
    See also: AWS API Documentation
    
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            ARN of the resource.
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            List keys identifying tags to remove.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_license_configuration(LicenseConfigurationArn=None, LicenseConfigurationStatus=None, LicenseRules=None, LicenseCount=None, LicenseCountHardLimit=None, Name=None, Description=None):
    """
    Modifies the attributes of an existing license configuration object. A license configuration is an abstraction of a customer license agreement that can be consumed and enforced by License Manager. Components include specifications for the license type (Instances, cores, sockets, VCPUs), tenancy (shared or Dedicated Host), host affinity (how long a VM is associated with a host), the number of licenses purchased and used.
    See also: AWS API Documentation
    
    
    :example: response = client.update_license_configuration(
        LicenseConfigurationArn='string',
        LicenseConfigurationStatus='AVAILABLE'|'DISABLED',
        LicenseRules=[
            'string',
        ],
        LicenseCount=123,
        LicenseCountHardLimit=True|False,
        Name='string',
        Description='string'
    )
    
    
    :type LicenseConfigurationArn: string
    :param LicenseConfigurationArn: [REQUIRED]
            ARN for a license configuration.
            

    :type LicenseConfigurationStatus: string
    :param LicenseConfigurationStatus: New status of the license configuration (ACTIVE or INACTIVE ).

    :type LicenseRules: list
    :param LicenseRules: List of flexible text strings designating license rules.
            (string) --
            

    :type LicenseCount: integer
    :param LicenseCount: New number of licenses managed by the license configuration.

    :type LicenseCountHardLimit: boolean
    :param LicenseCountHardLimit: Sets the number of available licenses as a hard limit.

    :type Name: string
    :param Name: New name of the license configuration.

    :type Description: string
    :param Description: New human-friendly description of the license configuration.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_license_specifications_for_resource(ResourceArn=None, AddLicenseSpecifications=None, RemoveLicenseSpecifications=None):
    """
    Adds or removes license configurations for a specified AWS resource. This operation currently supports updating the license specifications of AMIs, instances, and hosts. Launch templates and AWS CloudFormation templates are not managed from this operation as those resources send the license configurations directly to a resource creation operation, such as RunInstances .
    See also: AWS API Documentation
    
    
    :example: response = client.update_license_specifications_for_resource(
        ResourceArn='string',
        AddLicenseSpecifications=[
            {
                'LicenseConfigurationArn': 'string'
            },
        ],
        RemoveLicenseSpecifications=[
            {
                'LicenseConfigurationArn': 'string'
            },
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            ARN for an AWS server resource.
            

    :type AddLicenseSpecifications: list
    :param AddLicenseSpecifications: License configuration ARNs to be added to a resource.
            (dict) --Object used for associating a license configuration with a resource.
            LicenseConfigurationArn (string) -- [REQUIRED]ARN of the LicenseConfiguration object.
            
            

    :type RemoveLicenseSpecifications: list
    :param RemoveLicenseSpecifications: License configuration ARNs to be removed from a resource.
            (dict) --Object used for associating a license configuration with a resource.
            LicenseConfigurationArn (string) -- [REQUIRED]ARN of the LicenseConfiguration object.
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_service_settings(S3BucketArn=None, SnsTopicArn=None, OrganizationConfiguration=None, EnableCrossAccountsDiscovery=None):
    """
    Updates License Manager service settings.
    See also: AWS API Documentation
    
    
    :example: response = client.update_service_settings(
        S3BucketArn='string',
        SnsTopicArn='string',
        OrganizationConfiguration={
            'EnableIntegration': True|False
        },
        EnableCrossAccountsDiscovery=True|False
    )
    
    
    :type S3BucketArn: string
    :param S3BucketArn: ARN of the Amazon S3 bucket where License Manager information is stored.

    :type SnsTopicArn: string
    :param SnsTopicArn: ARN of the Amazon SNS topic used for License Manager alerts.

    :type OrganizationConfiguration: dict
    :param OrganizationConfiguration: Integrates AWS Organizations with License Manager for cross-account discovery.
            EnableIntegration (boolean) -- [REQUIRED]Flag to activate AWS Organization integration.
            

    :type EnableCrossAccountsDiscovery: boolean
    :param EnableCrossAccountsDiscovery: Activates cross-account discovery.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

