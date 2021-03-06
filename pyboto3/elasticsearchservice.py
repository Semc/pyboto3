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

def add_tags(ARN=None, TagList=None):
    """
    Attaches tags to an existing Elasticsearch domain. Tags are a set of case-sensitive key value pairs. An Elasticsearch domain may have up to 10 tags. See Tagging Amazon Elasticsearch Service Domains for more information.
    See also: AWS API Documentation
    
    
    :example: response = client.add_tags(
        ARN='string',
        TagList=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ARN: string
    :param ARN: [REQUIRED]
            Specify the ARN for which you want to add the tags.
            

    :type TagList: list
    :param TagList: [REQUIRED]
            List of Tag that need to be added for the Elasticsearch domain.
            (dict) --Specifies a key value pair for a resource tag.
            Key (string) -- [REQUIRED]Specifies the TagKey , the name of the tag. Tag keys must be unique for the Elasticsearch domain to which they are attached.
            Value (string) -- [REQUIRED]Specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and do not have to be unique in a tag set. For example, you can have a key value pair in a tag set of project : Trinity and cost-center : Trinity
            
            

    """
    pass

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

def cancel_elasticsearch_service_software_update(DomainName=None):
    """
    Cancels a scheduled service software update for an Amazon ES domain. You can only perform this operation before the AutomatedUpdateDate and when the UpdateStatus is in the PENDING_UPDATE state.
    See also: AWS API Documentation
    
    
    :example: response = client.cancel_elasticsearch_service_software_update(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the domain that you want to stop the latest service software update on.
            

    :rtype: dict
    :return: {
        'ServiceSoftwareOptions': {
            'CurrentVersion': 'string',
            'NewVersion': 'string',
            'UpdateAvailable': True|False,
            'Cancellable': True|False,
            'UpdateStatus': 'PENDING_UPDATE'|'IN_PROGRESS'|'COMPLETED'|'NOT_ELIGIBLE'|'ELIGIBLE',
            'Description': 'string',
            'AutomatedUpdateDate': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def create_elasticsearch_domain(DomainName=None, ElasticsearchVersion=None, ElasticsearchClusterConfig=None, EBSOptions=None, AccessPolicies=None, SnapshotOptions=None, VPCOptions=None, CognitoOptions=None, EncryptionAtRestOptions=None, NodeToNodeEncryptionOptions=None, AdvancedOptions=None, LogPublishingOptions=None):
    """
    Creates a new Elasticsearch domain. For more information, see Creating Elasticsearch Domains in the Amazon Elasticsearch Service Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_elasticsearch_domain(
        DomainName='string',
        ElasticsearchVersion='string',
        ElasticsearchClusterConfig={
            'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
            'InstanceCount': 123,
            'DedicatedMasterEnabled': True|False,
            'ZoneAwarenessEnabled': True|False,
            'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
            'DedicatedMasterCount': 123
        },
        EBSOptions={
            'EBSEnabled': True|False,
            'VolumeType': 'standard'|'gp2'|'io1',
            'VolumeSize': 123,
            'Iops': 123
        },
        AccessPolicies='string',
        SnapshotOptions={
            'AutomatedSnapshotStartHour': 123
        },
        VPCOptions={
            'SubnetIds': [
                'string',
            ],
            'SecurityGroupIds': [
                'string',
            ]
        },
        CognitoOptions={
            'Enabled': True|False,
            'UserPoolId': 'string',
            'IdentityPoolId': 'string',
            'RoleArn': 'string'
        },
        EncryptionAtRestOptions={
            'Enabled': True|False,
            'KmsKeyId': 'string'
        },
        NodeToNodeEncryptionOptions={
            'Enabled': True|False
        },
        AdvancedOptions={
            'string': 'string'
        },
        LogPublishingOptions={
            'string': {
                'CloudWatchLogsLogGroupArn': 'string',
                'Enabled': True|False
            }
        }
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the Elasticsearch domain that you are creating. Domain names are unique across the domains owned by an account within an AWS region. Domain names must start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            

    :type ElasticsearchVersion: string
    :param ElasticsearchVersion: String of format X.Y to specify version for the Elasticsearch domain eg. '1.5' or '2.3'. For more information, see Creating Elasticsearch Domains in the Amazon Elasticsearch Service Developer Guide .

    :type ElasticsearchClusterConfig: dict
    :param ElasticsearchClusterConfig: Configuration options for an Elasticsearch domain. Specifies the instance type and number of instances in the domain cluster.
            InstanceType (string) --The instance type for an Elasticsearch cluster.
            InstanceCount (integer) --The number of instances in the specified domain cluster.
            DedicatedMasterEnabled (boolean) --A boolean value to indicate whether a dedicated master node is enabled. See About Dedicated Master Nodes for more information.
            ZoneAwarenessEnabled (boolean) --A boolean value to indicate whether zone awareness is enabled. See About Zone Awareness for more information.
            DedicatedMasterType (string) --The instance type for a dedicated master node.
            DedicatedMasterCount (integer) --Total number of dedicated master nodes, active and on standby, for the cluster.
            

    :type EBSOptions: dict
    :param EBSOptions: Options to enable, disable and specify the type and size of EBS storage volumes.
            EBSEnabled (boolean) --Specifies whether EBS-based storage is enabled.
            VolumeType (string) --Specifies the volume type for EBS-based storage.
            VolumeSize (integer) --Integer to specify the size of an EBS volume.
            Iops (integer) --Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).
            

    :type AccessPolicies: string
    :param AccessPolicies: IAM access policy as a JSON-formatted string.

    :type SnapshotOptions: dict
    :param SnapshotOptions: Option to set time, in UTC format, of the daily automated snapshot. Default value is 0 hours.
            AutomatedSnapshotStartHour (integer) --Specifies the time, in UTC format, when the service takes a daily automated snapshot of the specified Elasticsearch domain. Default value is 0 hours.
            

    :type VPCOptions: dict
    :param VPCOptions: Options to specify the subnets and security groups for VPC endpoint. For more information, see Creating a VPC in VPC Endpoints for Amazon Elasticsearch Service Domains
            SubnetIds (list) --Specifies the subnets for VPC endpoint.
            (string) --
            SecurityGroupIds (list) --Specifies the security groups for VPC endpoint.
            (string) --
            

    :type CognitoOptions: dict
    :param CognitoOptions: Options to specify the Cognito user and identity pools for Kibana authentication. For more information, see Amazon Cognito Authentication for Kibana .
            Enabled (boolean) --Specifies the option to enable Cognito for Kibana authentication.
            UserPoolId (string) --Specifies the Cognito user pool ID for Kibana authentication.
            IdentityPoolId (string) --Specifies the Cognito identity pool ID for Kibana authentication.
            RoleArn (string) --Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito resources.
            

    :type EncryptionAtRestOptions: dict
    :param EncryptionAtRestOptions: Specifies the Encryption At Rest Options.
            Enabled (boolean) --Specifies the option to enable Encryption At Rest.
            KmsKeyId (string) --Specifies the KMS Key ID for Encryption At Rest options.
            

    :type NodeToNodeEncryptionOptions: dict
    :param NodeToNodeEncryptionOptions: Specifies the NodeToNodeEncryptionOptions.
            Enabled (boolean) --Specify true to enable node-to-node encryption.
            

    :type AdvancedOptions: dict
    :param AdvancedOptions: Option to allow references to indices in an HTTP request body. Must be false when configuring access to individual sub-resources. By default, the value is true . See Configuration Advanced Options for more information.
            (string) --
            (string) --
            

    :type LogPublishingOptions: dict
    :param LogPublishingOptions: Map of LogType and LogPublishingOption , each containing options to publish a given type of Elasticsearch log.
            (string) --Type of Log File, it can be one of the following:
            INDEX_SLOW_LOGS: Index slow logs contain insert requests that took more time than configured index query log threshold to execute.
            SEARCH_SLOW_LOGS: Search slow logs contain search queries that took more time than configured search query log threshold to execute.
            ES_APPLICATION_LOGS: Elasticsearch application logs contain information about errors and warnings raised during the operation of the service and can be useful for troubleshooting.
            (dict) --Log Publishing option that is set for given domain. Attributes and their details:
            CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be published.
            Enabled: Whether the log publishing for given log type is enabled or not
            CloudWatchLogsLogGroupArn (string) --ARN of the Cloudwatch log group to which log needs to be published.
            Enabled (boolean) --Specifies whether given log publishing option is enabled or not.
            
            

    :rtype: dict
    :return: {
        'DomainStatus': {
            'DomainId': 'string',
            'DomainName': 'string',
            'ARN': 'string',
            'Created': True|False,
            'Deleted': True|False,
            'Endpoint': 'string',
            'Endpoints': {
                'string': 'string'
            },
            'Processing': True|False,
            'UpgradeProcessing': True|False,
            'ElasticsearchVersion': 'string',
            'ElasticsearchClusterConfig': {
                'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                'InstanceCount': 123,
                'DedicatedMasterEnabled': True|False,
                'ZoneAwarenessEnabled': True|False,
                'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                'DedicatedMasterCount': 123
            },
            'EBSOptions': {
                'EBSEnabled': True|False,
                'VolumeType': 'standard'|'gp2'|'io1',
                'VolumeSize': 123,
                'Iops': 123
            },
            'AccessPolicies': 'string',
            'SnapshotOptions': {
                'AutomatedSnapshotStartHour': 123
            },
            'VPCOptions': {
                'VPCId': 'string',
                'SubnetIds': [
                    'string',
                ],
                'AvailabilityZones': [
                    'string',
                ],
                'SecurityGroupIds': [
                    'string',
                ]
            },
            'CognitoOptions': {
                'Enabled': True|False,
                'UserPoolId': 'string',
                'IdentityPoolId': 'string',
                'RoleArn': 'string'
            },
            'EncryptionAtRestOptions': {
                'Enabled': True|False,
                'KmsKeyId': 'string'
            },
            'NodeToNodeEncryptionOptions': {
                'Enabled': True|False
            },
            'AdvancedOptions': {
                'string': 'string'
            },
            'LogPublishingOptions': {
                'string': {
                    'CloudWatchLogsLogGroupArn': 'string',
                    'Enabled': True|False
                }
            },
            'ServiceSoftwareOptions': {
                'CurrentVersion': 'string',
                'NewVersion': 'string',
                'UpdateAvailable': True|False,
                'Cancellable': True|False,
                'UpdateStatus': 'PENDING_UPDATE'|'IN_PROGRESS'|'COMPLETED'|'NOT_ELIGIBLE'|'ELIGIBLE',
                'Description': 'string',
                'AutomatedUpdateDate': datetime(2015, 1, 1)
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_elasticsearch_domain(DomainName=None):
    """
    Permanently deletes the specified Elasticsearch domain and all of its data. Once a domain is deleted, it cannot be recovered.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_elasticsearch_domain(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the Elasticsearch domain that you want to permanently delete.
            

    :rtype: dict
    :return: {
        'DomainStatus': {
            'DomainId': 'string',
            'DomainName': 'string',
            'ARN': 'string',
            'Created': True|False,
            'Deleted': True|False,
            'Endpoint': 'string',
            'Endpoints': {
                'string': 'string'
            },
            'Processing': True|False,
            'UpgradeProcessing': True|False,
            'ElasticsearchVersion': 'string',
            'ElasticsearchClusterConfig': {
                'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                'InstanceCount': 123,
                'DedicatedMasterEnabled': True|False,
                'ZoneAwarenessEnabled': True|False,
                'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                'DedicatedMasterCount': 123
            },
            'EBSOptions': {
                'EBSEnabled': True|False,
                'VolumeType': 'standard'|'gp2'|'io1',
                'VolumeSize': 123,
                'Iops': 123
            },
            'AccessPolicies': 'string',
            'SnapshotOptions': {
                'AutomatedSnapshotStartHour': 123
            },
            'VPCOptions': {
                'VPCId': 'string',
                'SubnetIds': [
                    'string',
                ],
                'AvailabilityZones': [
                    'string',
                ],
                'SecurityGroupIds': [
                    'string',
                ]
            },
            'CognitoOptions': {
                'Enabled': True|False,
                'UserPoolId': 'string',
                'IdentityPoolId': 'string',
                'RoleArn': 'string'
            },
            'EncryptionAtRestOptions': {
                'Enabled': True|False,
                'KmsKeyId': 'string'
            },
            'NodeToNodeEncryptionOptions': {
                'Enabled': True|False
            },
            'AdvancedOptions': {
                'string': 'string'
            },
            'LogPublishingOptions': {
                'string': {
                    'CloudWatchLogsLogGroupArn': 'string',
                    'Enabled': True|False
                }
            },
            'ServiceSoftwareOptions': {
                'CurrentVersion': 'string',
                'NewVersion': 'string',
                'UpdateAvailable': True|False,
                'Cancellable': True|False,
                'UpdateStatus': 'PENDING_UPDATE'|'IN_PROGRESS'|'COMPLETED'|'NOT_ELIGIBLE'|'ELIGIBLE',
                'Description': 'string',
                'AutomatedUpdateDate': datetime(2015, 1, 1)
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_elasticsearch_service_role():
    """
    Deletes the service-linked role that Elasticsearch Service uses to manage and maintain VPC domains. Role deletion will fail if any existing VPC domains use the role. You must delete any such Elasticsearch domains before deleting the role. See Deleting Elasticsearch Service Role in VPC Endpoints for Amazon Elasticsearch Service Domains .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_elasticsearch_service_role()
    
    
    """
    pass

def describe_elasticsearch_domain(DomainName=None):
    """
    Returns domain configuration information about the specified Elasticsearch domain, including the domain ID, domain endpoint, and domain ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_elasticsearch_domain(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the Elasticsearch domain for which you want information.
            

    :rtype: dict
    :return: {
        'DomainStatus': {
            'DomainId': 'string',
            'DomainName': 'string',
            'ARN': 'string',
            'Created': True|False,
            'Deleted': True|False,
            'Endpoint': 'string',
            'Endpoints': {
                'string': 'string'
            },
            'Processing': True|False,
            'UpgradeProcessing': True|False,
            'ElasticsearchVersion': 'string',
            'ElasticsearchClusterConfig': {
                'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                'InstanceCount': 123,
                'DedicatedMasterEnabled': True|False,
                'ZoneAwarenessEnabled': True|False,
                'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                'DedicatedMasterCount': 123
            },
            'EBSOptions': {
                'EBSEnabled': True|False,
                'VolumeType': 'standard'|'gp2'|'io1',
                'VolumeSize': 123,
                'Iops': 123
            },
            'AccessPolicies': 'string',
            'SnapshotOptions': {
                'AutomatedSnapshotStartHour': 123
            },
            'VPCOptions': {
                'VPCId': 'string',
                'SubnetIds': [
                    'string',
                ],
                'AvailabilityZones': [
                    'string',
                ],
                'SecurityGroupIds': [
                    'string',
                ]
            },
            'CognitoOptions': {
                'Enabled': True|False,
                'UserPoolId': 'string',
                'IdentityPoolId': 'string',
                'RoleArn': 'string'
            },
            'EncryptionAtRestOptions': {
                'Enabled': True|False,
                'KmsKeyId': 'string'
            },
            'NodeToNodeEncryptionOptions': {
                'Enabled': True|False
            },
            'AdvancedOptions': {
                'string': 'string'
            },
            'LogPublishingOptions': {
                'string': {
                    'CloudWatchLogsLogGroupArn': 'string',
                    'Enabled': True|False
                }
            },
            'ServiceSoftwareOptions': {
                'CurrentVersion': 'string',
                'NewVersion': 'string',
                'UpdateAvailable': True|False,
                'Cancellable': True|False,
                'UpdateStatus': 'PENDING_UPDATE'|'IN_PROGRESS'|'COMPLETED'|'NOT_ELIGIBLE'|'ELIGIBLE',
                'Description': 'string',
                'AutomatedUpdateDate': datetime(2015, 1, 1)
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_elasticsearch_domain_config(DomainName=None):
    """
    Provides cluster configuration information about the specified Elasticsearch domain, such as the state, creation date, update version, and update date for cluster options.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_elasticsearch_domain_config(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The Elasticsearch domain that you want to get information about.
            

    :rtype: dict
    :return: {
        'DomainConfig': {
            'ElasticsearchVersion': {
                'Options': 'string',
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'ElasticsearchClusterConfig': {
                'Options': {
                    'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                    'InstanceCount': 123,
                    'DedicatedMasterEnabled': True|False,
                    'ZoneAwarenessEnabled': True|False,
                    'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                    'DedicatedMasterCount': 123
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'EBSOptions': {
                'Options': {
                    'EBSEnabled': True|False,
                    'VolumeType': 'standard'|'gp2'|'io1',
                    'VolumeSize': 123,
                    'Iops': 123
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'AccessPolicies': {
                'Options': 'string',
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'SnapshotOptions': {
                'Options': {
                    'AutomatedSnapshotStartHour': 123
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'VPCOptions': {
                'Options': {
                    'VPCId': 'string',
                    'SubnetIds': [
                        'string',
                    ],
                    'AvailabilityZones': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ]
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'CognitoOptions': {
                'Options': {
                    'Enabled': True|False,
                    'UserPoolId': 'string',
                    'IdentityPoolId': 'string',
                    'RoleArn': 'string'
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'EncryptionAtRestOptions': {
                'Options': {
                    'Enabled': True|False,
                    'KmsKeyId': 'string'
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'NodeToNodeEncryptionOptions': {
                'Options': {
                    'Enabled': True|False
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'AdvancedOptions': {
                'Options': {
                    'string': 'string'
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'LogPublishingOptions': {
                'Options': {
                    'string': {
                        'CloudWatchLogsLogGroupArn': 'string',
                        'Enabled': True|False
                    }
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_elasticsearch_domains(DomainNames=None):
    """
    Returns domain configuration information about the specified Elasticsearch domains, including the domain ID, domain endpoint, and domain ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_elasticsearch_domains(
        DomainNames=[
            'string',
        ]
    )
    
    
    :type DomainNames: list
    :param DomainNames: [REQUIRED]
            The Elasticsearch domains for which you want information.
            (string) --The name of an Elasticsearch domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            

    :rtype: dict
    :return: {
        'DomainStatusList': [
            {
                'DomainId': 'string',
                'DomainName': 'string',
                'ARN': 'string',
                'Created': True|False,
                'Deleted': True|False,
                'Endpoint': 'string',
                'Endpoints': {
                    'string': 'string'
                },
                'Processing': True|False,
                'UpgradeProcessing': True|False,
                'ElasticsearchVersion': 'string',
                'ElasticsearchClusterConfig': {
                    'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                    'InstanceCount': 123,
                    'DedicatedMasterEnabled': True|False,
                    'ZoneAwarenessEnabled': True|False,
                    'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                    'DedicatedMasterCount': 123
                },
                'EBSOptions': {
                    'EBSEnabled': True|False,
                    'VolumeType': 'standard'|'gp2'|'io1',
                    'VolumeSize': 123,
                    'Iops': 123
                },
                'AccessPolicies': 'string',
                'SnapshotOptions': {
                    'AutomatedSnapshotStartHour': 123
                },
                'VPCOptions': {
                    'VPCId': 'string',
                    'SubnetIds': [
                        'string',
                    ],
                    'AvailabilityZones': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ]
                },
                'CognitoOptions': {
                    'Enabled': True|False,
                    'UserPoolId': 'string',
                    'IdentityPoolId': 'string',
                    'RoleArn': 'string'
                },
                'EncryptionAtRestOptions': {
                    'Enabled': True|False,
                    'KmsKeyId': 'string'
                },
                'NodeToNodeEncryptionOptions': {
                    'Enabled': True|False
                },
                'AdvancedOptions': {
                    'string': 'string'
                },
                'LogPublishingOptions': {
                    'string': {
                        'CloudWatchLogsLogGroupArn': 'string',
                        'Enabled': True|False
                    }
                },
                'ServiceSoftwareOptions': {
                    'CurrentVersion': 'string',
                    'NewVersion': 'string',
                    'UpdateAvailable': True|False,
                    'Cancellable': True|False,
                    'UpdateStatus': 'PENDING_UPDATE'|'IN_PROGRESS'|'COMPLETED'|'NOT_ELIGIBLE'|'ELIGIBLE',
                    'Description': 'string',
                    'AutomatedUpdateDate': datetime(2015, 1, 1)
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_elasticsearch_instance_type_limits(DomainName=None, InstanceType=None, ElasticsearchVersion=None):
    """
    Describe Elasticsearch Limits for a given InstanceType and ElasticsearchVersion. When modifying existing Domain, specify the ``  DomainName `` to know what Limits are supported for modifying.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_elasticsearch_instance_type_limits(
        DomainName='string',
        InstanceType='m3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
        ElasticsearchVersion='string'
    )
    
    
    :type DomainName: string
    :param DomainName: DomainName represents the name of the Domain that we are trying to modify. This should be present only if we are querying for Elasticsearch `` Limits `` for existing domain.

    :type InstanceType: string
    :param InstanceType: [REQUIRED]
            The instance type for an Elasticsearch cluster for which Elasticsearch `` Limits `` are needed.
            

    :type ElasticsearchVersion: string
    :param ElasticsearchVersion: [REQUIRED]
            Version of Elasticsearch for which `` Limits `` are needed.
            

    :rtype: dict
    :return: {
        'LimitsByRole': {
            'string': {
                'StorageTypes': [
                    {
                        'StorageTypeName': 'string',
                        'StorageSubTypeName': 'string',
                        'StorageTypeLimits': [
                            {
                                'LimitName': 'string',
                                'LimitValues': [
                                    'string',
                                ]
                            },
                        ]
                    },
                ],
                'InstanceLimits': {
                    'InstanceCountLimits': {
                        'MinimumInstanceCount': 123,
                        'MaximumInstanceCount': 123
                    }
                },
                'AdditionalLimits': [
                    {
                        'LimitName': 'string',
                        'LimitValues': [
                            'string',
                        ]
                    },
                ]
            }
        }
    }
    
    
    :returns: 
    Data: If the given InstanceType is used as Data node
    Master: If the given InstanceType is used as Master node
    
    """
    pass

def describe_reserved_elasticsearch_instance_offerings(ReservedElasticsearchInstanceOfferingId=None, MaxResults=None, NextToken=None):
    """
    Lists available reserved Elasticsearch instance offerings.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_reserved_elasticsearch_instance_offerings(
        ReservedElasticsearchInstanceOfferingId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ReservedElasticsearchInstanceOfferingId: string
    :param ReservedElasticsearchInstanceOfferingId: The offering identifier filter value. Use this parameter to show only the available offering that matches the specified reservation identifier.

    :type MaxResults: integer
    :param MaxResults: Set this value to limit the number of results returned. If not specified, defaults to 100.

    :type NextToken: string
    :param NextToken: NextToken should be sent in case if earlier API call produced result containing NextToken. It is used for pagination.

    :rtype: dict
    :return: {
        'NextToken': 'string',
        'ReservedElasticsearchInstanceOfferings': [
            {
                'ReservedElasticsearchInstanceOfferingId': 'string',
                'ElasticsearchInstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                'Duration': 123,
                'FixedPrice': 123.0,
                'UsagePrice': 123.0,
                'CurrencyCode': 'string',
                'PaymentOption': 'ALL_UPFRONT'|'PARTIAL_UPFRONT'|'NO_UPFRONT',
                'RecurringCharges': [
                    {
                        'RecurringChargeAmount': 123.0,
                        'RecurringChargeFrequency': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def describe_reserved_elasticsearch_instances(ReservedElasticsearchInstanceId=None, MaxResults=None, NextToken=None):
    """
    Returns information about reserved Elasticsearch instances for this account.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_reserved_elasticsearch_instances(
        ReservedElasticsearchInstanceId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ReservedElasticsearchInstanceId: string
    :param ReservedElasticsearchInstanceId: The reserved instance identifier filter value. Use this parameter to show only the reservation that matches the specified reserved Elasticsearch instance ID.

    :type MaxResults: integer
    :param MaxResults: Set this value to limit the number of results returned. If not specified, defaults to 100.

    :type NextToken: string
    :param NextToken: NextToken should be sent in case if earlier API call produced result containing NextToken. It is used for pagination.

    :rtype: dict
    :return: {
        'NextToken': 'string',
        'ReservedElasticsearchInstances': [
            {
                'ReservationName': 'string',
                'ReservedElasticsearchInstanceId': 'string',
                'ReservedElasticsearchInstanceOfferingId': 'string',
                'ElasticsearchInstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                'StartTime': datetime(2015, 1, 1),
                'Duration': 123,
                'FixedPrice': 123.0,
                'UsagePrice': 123.0,
                'CurrencyCode': 'string',
                'ElasticsearchInstanceCount': 123,
                'State': 'string',
                'PaymentOption': 'ALL_UPFRONT'|'PARTIAL_UPFRONT'|'NO_UPFRONT',
                'RecurringCharges': [
                    {
                        'RecurringChargeAmount': 123.0,
                        'RecurringChargeFrequency': 'string'
                    },
                ]
            },
        ]
    }
    
    
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

def get_compatible_elasticsearch_versions(DomainName=None):
    """
    Returns a list of upgrade compatible Elastisearch versions. You can optionally pass a ``  DomainName `` to get all upgrade compatible Elasticsearch versions for that specific domain.
    See also: AWS API Documentation
    
    
    :example: response = client.get_compatible_elasticsearch_versions(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: The name of an Elasticsearch domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).

    :rtype: dict
    :return: {
        'CompatibleElasticsearchVersions': [
            {
                'SourceVersion': 'string',
                'TargetVersions': [
                    'string',
                ]
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

def get_upgrade_history(DomainName=None, MaxResults=None, NextToken=None):
    """
    Retrieves the complete history of the last 10 upgrades that were performed on the domain.
    See also: AWS API Documentation
    
    
    :example: response = client.get_upgrade_history(
        DomainName='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of an Elasticsearch domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            

    :type MaxResults: integer
    :param MaxResults: Set this value to limit the number of results returned.

    :type NextToken: string
    :param NextToken: Paginated APIs accepts NextToken input to returns next page results and provides a NextToken output in the response which can be used by the client to retrieve more results.

    :rtype: dict
    :return: {
        'UpgradeHistories': [
            {
                'UpgradeName': 'string',
                'StartTimestamp': datetime(2015, 1, 1),
                'UpgradeStatus': 'IN_PROGRESS'|'SUCCEEDED'|'SUCCEEDED_WITH_ISSUES'|'FAILED',
                'StepsList': [
                    {
                        'UpgradeStep': 'PRE_UPGRADE_CHECK'|'SNAPSHOT'|'UPGRADE',
                        'UpgradeStepStatus': 'IN_PROGRESS'|'SUCCEEDED'|'SUCCEEDED_WITH_ISSUES'|'FAILED',
                        'Issues': [
                            'string',
                        ],
                        'ProgressPercent': 123.0
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    In Progress
    Succeeded
    Succeeded with Issues
    Failed
    
    """
    pass

def get_upgrade_status(DomainName=None):
    """
    Retrieves the latest status of the last upgrade or upgrade eligibility check that was performed on the domain.
    See also: AWS API Documentation
    
    
    :example: response = client.get_upgrade_status(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of an Elasticsearch domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            

    :rtype: dict
    :return: {
        'UpgradeStep': 'PRE_UPGRADE_CHECK'|'SNAPSHOT'|'UPGRADE',
        'StepStatus': 'IN_PROGRESS'|'SUCCEEDED'|'SUCCEEDED_WITH_ISSUES'|'FAILED',
        'UpgradeName': 'string'
    }
    
    
    :returns: 
    In Progress
    Succeeded
    Succeeded with Issues
    Failed
    
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

def list_domain_names():
    """
    Returns the name of all Elasticsearch domains owned by the current user's account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_domain_names()
    
    
    :rtype: dict
    :return: {
        'DomainNames': [
            {
                'DomainName': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_elasticsearch_instance_types(ElasticsearchVersion=None, DomainName=None, MaxResults=None, NextToken=None):
    """
    List all Elasticsearch instance types that are supported for given ElasticsearchVersion
    See also: AWS API Documentation
    
    
    :example: response = client.list_elasticsearch_instance_types(
        ElasticsearchVersion='string',
        DomainName='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ElasticsearchVersion: string
    :param ElasticsearchVersion: [REQUIRED]
            Version of Elasticsearch for which list of supported elasticsearch instance types are needed.
            

    :type DomainName: string
    :param DomainName: DomainName represents the name of the Domain that we are trying to modify. This should be present only if we are querying for list of available Elasticsearch instance types when modifying existing domain.

    :type MaxResults: integer
    :param MaxResults: Set this value to limit the number of results returned. Value provided must be greater than 30 else it wont be honored.

    :type NextToken: string
    :param NextToken: NextToken should be sent in case if earlier API call produced result containing NextToken. It is used for pagination.

    :rtype: dict
    :return: {
        'ElasticsearchInstanceTypes': [
            'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_elasticsearch_versions(MaxResults=None, NextToken=None):
    """
    List all supported Elasticsearch versions
    See also: AWS API Documentation
    
    
    :example: response = client.list_elasticsearch_versions(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: Set this value to limit the number of results returned. Value provided must be greater than 10 else it wont be honored.

    :type NextToken: string
    :param NextToken: Paginated APIs accepts NextToken input to returns next page results and provides a NextToken output in the response which can be used by the client to retrieve more results.

    :rtype: dict
    :return: {
        'ElasticsearchVersions': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tags(ARN=None):
    """
    Returns all tags for the given Elasticsearch domain.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags(
        ARN='string'
    )
    
    
    :type ARN: string
    :param ARN: [REQUIRED]
            Specify the ARN for the Elasticsearch domain to which the tags are attached that you want to view.
            

    :rtype: dict
    :return: {
        'TagList': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def purchase_reserved_elasticsearch_instance_offering(ReservedElasticsearchInstanceOfferingId=None, ReservationName=None, InstanceCount=None):
    """
    Allows you to purchase reserved Elasticsearch instances.
    See also: AWS API Documentation
    
    
    :example: response = client.purchase_reserved_elasticsearch_instance_offering(
        ReservedElasticsearchInstanceOfferingId='string',
        ReservationName='string',
        InstanceCount=123
    )
    
    
    :type ReservedElasticsearchInstanceOfferingId: string
    :param ReservedElasticsearchInstanceOfferingId: [REQUIRED]
            The ID of the reserved Elasticsearch instance offering to purchase.
            

    :type ReservationName: string
    :param ReservationName: [REQUIRED]
            A customer-specified identifier to track this reservation.
            

    :type InstanceCount: integer
    :param InstanceCount: The number of Elasticsearch instances to reserve.

    :rtype: dict
    :return: {
        'ReservedElasticsearchInstanceId': 'string',
        'ReservationName': 'string'
    }
    
    
    """
    pass

def remove_tags(ARN=None, TagKeys=None):
    """
    Removes the specified set of tags from the specified Elasticsearch domain.
    See also: AWS API Documentation
    
    
    :example: response = client.remove_tags(
        ARN='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ARN: string
    :param ARN: [REQUIRED]
            Specifies the ARN for the Elasticsearch domain from which you want to delete the specified tags.
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            Specifies the TagKey list which you want to remove from the Elasticsearch domain.
            (string) --
            

    """
    pass

def start_elasticsearch_service_software_update(DomainName=None):
    """
    Schedules a service software update for an Amazon ES domain.
    See also: AWS API Documentation
    
    
    :example: response = client.start_elasticsearch_service_software_update(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the domain that you want to update to the latest service software.
            

    :rtype: dict
    :return: {
        'ServiceSoftwareOptions': {
            'CurrentVersion': 'string',
            'NewVersion': 'string',
            'UpdateAvailable': True|False,
            'Cancellable': True|False,
            'UpdateStatus': 'PENDING_UPDATE'|'IN_PROGRESS'|'COMPLETED'|'NOT_ELIGIBLE'|'ELIGIBLE',
            'Description': 'string',
            'AutomatedUpdateDate': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def update_elasticsearch_domain_config(DomainName=None, ElasticsearchClusterConfig=None, EBSOptions=None, SnapshotOptions=None, VPCOptions=None, CognitoOptions=None, AdvancedOptions=None, AccessPolicies=None, LogPublishingOptions=None):
    """
    Modifies the cluster configuration of the specified Elasticsearch domain, setting as setting the instance type and the number of instances.
    See also: AWS API Documentation
    
    
    :example: response = client.update_elasticsearch_domain_config(
        DomainName='string',
        ElasticsearchClusterConfig={
            'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
            'InstanceCount': 123,
            'DedicatedMasterEnabled': True|False,
            'ZoneAwarenessEnabled': True|False,
            'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
            'DedicatedMasterCount': 123
        },
        EBSOptions={
            'EBSEnabled': True|False,
            'VolumeType': 'standard'|'gp2'|'io1',
            'VolumeSize': 123,
            'Iops': 123
        },
        SnapshotOptions={
            'AutomatedSnapshotStartHour': 123
        },
        VPCOptions={
            'SubnetIds': [
                'string',
            ],
            'SecurityGroupIds': [
                'string',
            ]
        },
        CognitoOptions={
            'Enabled': True|False,
            'UserPoolId': 'string',
            'IdentityPoolId': 'string',
            'RoleArn': 'string'
        },
        AdvancedOptions={
            'string': 'string'
        },
        AccessPolicies='string',
        LogPublishingOptions={
            'string': {
                'CloudWatchLogsLogGroupArn': 'string',
                'Enabled': True|False
            }
        }
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the Elasticsearch domain that you are updating.
            

    :type ElasticsearchClusterConfig: dict
    :param ElasticsearchClusterConfig: The type and number of instances to instantiate for the domain cluster.
            InstanceType (string) --The instance type for an Elasticsearch cluster.
            InstanceCount (integer) --The number of instances in the specified domain cluster.
            DedicatedMasterEnabled (boolean) --A boolean value to indicate whether a dedicated master node is enabled. See About Dedicated Master Nodes for more information.
            ZoneAwarenessEnabled (boolean) --A boolean value to indicate whether zone awareness is enabled. See About Zone Awareness for more information.
            DedicatedMasterType (string) --The instance type for a dedicated master node.
            DedicatedMasterCount (integer) --Total number of dedicated master nodes, active and on standby, for the cluster.
            

    :type EBSOptions: dict
    :param EBSOptions: Specify the type and size of the EBS volume that you want to use.
            EBSEnabled (boolean) --Specifies whether EBS-based storage is enabled.
            VolumeType (string) --Specifies the volume type for EBS-based storage.
            VolumeSize (integer) --Integer to specify the size of an EBS volume.
            Iops (integer) --Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).
            

    :type SnapshotOptions: dict
    :param SnapshotOptions: Option to set the time, in UTC format, for the daily automated snapshot. Default value is 0 hours.
            AutomatedSnapshotStartHour (integer) --Specifies the time, in UTC format, when the service takes a daily automated snapshot of the specified Elasticsearch domain. Default value is 0 hours.
            

    :type VPCOptions: dict
    :param VPCOptions: Options to specify the subnets and security groups for VPC endpoint. For more information, see Creating a VPC in VPC Endpoints for Amazon Elasticsearch Service Domains
            SubnetIds (list) --Specifies the subnets for VPC endpoint.
            (string) --
            SecurityGroupIds (list) --Specifies the security groups for VPC endpoint.
            (string) --
            

    :type CognitoOptions: dict
    :param CognitoOptions: Options to specify the Cognito user and identity pools for Kibana authentication. For more information, see Amazon Cognito Authentication for Kibana .
            Enabled (boolean) --Specifies the option to enable Cognito for Kibana authentication.
            UserPoolId (string) --Specifies the Cognito user pool ID for Kibana authentication.
            IdentityPoolId (string) --Specifies the Cognito identity pool ID for Kibana authentication.
            RoleArn (string) --Specifies the role ARN that provides Elasticsearch permissions for accessing Cognito resources.
            

    :type AdvancedOptions: dict
    :param AdvancedOptions: Modifies the advanced option to allow references to indices in an HTTP request body. Must be false when configuring access to individual sub-resources. By default, the value is true . See Configuration Advanced Options for more information.
            (string) --
            (string) --
            

    :type AccessPolicies: string
    :param AccessPolicies: IAM access policy as a JSON-formatted string.

    :type LogPublishingOptions: dict
    :param LogPublishingOptions: Map of LogType and LogPublishingOption , each containing options to publish a given type of Elasticsearch log.
            (string) --Type of Log File, it can be one of the following:
            INDEX_SLOW_LOGS: Index slow logs contain insert requests that took more time than configured index query log threshold to execute.
            SEARCH_SLOW_LOGS: Search slow logs contain search queries that took more time than configured search query log threshold to execute.
            ES_APPLICATION_LOGS: Elasticsearch application logs contain information about errors and warnings raised during the operation of the service and can be useful for troubleshooting.
            (dict) --Log Publishing option that is set for given domain. Attributes and their details:
            CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be published.
            Enabled: Whether the log publishing for given log type is enabled or not
            CloudWatchLogsLogGroupArn (string) --ARN of the Cloudwatch log group to which log needs to be published.
            Enabled (boolean) --Specifies whether given log publishing option is enabled or not.
            
            

    :rtype: dict
    :return: {
        'DomainConfig': {
            'ElasticsearchVersion': {
                'Options': 'string',
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'ElasticsearchClusterConfig': {
                'Options': {
                    'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                    'InstanceCount': 123,
                    'DedicatedMasterEnabled': True|False,
                    'ZoneAwarenessEnabled': True|False,
                    'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                    'DedicatedMasterCount': 123
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'EBSOptions': {
                'Options': {
                    'EBSEnabled': True|False,
                    'VolumeType': 'standard'|'gp2'|'io1',
                    'VolumeSize': 123,
                    'Iops': 123
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'AccessPolicies': {
                'Options': 'string',
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'SnapshotOptions': {
                'Options': {
                    'AutomatedSnapshotStartHour': 123
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'VPCOptions': {
                'Options': {
                    'VPCId': 'string',
                    'SubnetIds': [
                        'string',
                    ],
                    'AvailabilityZones': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ]
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'CognitoOptions': {
                'Options': {
                    'Enabled': True|False,
                    'UserPoolId': 'string',
                    'IdentityPoolId': 'string',
                    'RoleArn': 'string'
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'EncryptionAtRestOptions': {
                'Options': {
                    'Enabled': True|False,
                    'KmsKeyId': 'string'
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'NodeToNodeEncryptionOptions': {
                'Options': {
                    'Enabled': True|False
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'AdvancedOptions': {
                'Options': {
                    'string': 'string'
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'LogPublishingOptions': {
                'Options': {
                    'string': {
                        'CloudWatchLogsLogGroupArn': 'string',
                        'Enabled': True|False
                    }
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def upgrade_elasticsearch_domain(DomainName=None, TargetVersion=None, PerformCheckOnly=None):
    """
    Allows you to either upgrade your domain or perform an Upgrade eligibility check to a compatible Elasticsearch version.
    See also: AWS API Documentation
    
    
    :example: response = client.upgrade_elasticsearch_domain(
        DomainName='string',
        TargetVersion='string',
        PerformCheckOnly=True|False
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of an Elasticsearch domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            

    :type TargetVersion: string
    :param TargetVersion: [REQUIRED]
            The version of Elasticsearch that you intend to upgrade the domain to.
            

    :type PerformCheckOnly: boolean
    :param PerformCheckOnly: This flag, when set to True, indicates that an Upgrade Eligibility Check needs to be performed. This will not actually perform the Upgrade.

    :rtype: dict
    :return: {
        'DomainName': 'string',
        'TargetVersion': 'string',
        'PerformCheckOnly': True|False
    }
    
    
    """
    pass

