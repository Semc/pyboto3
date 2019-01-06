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

def create_cluster(BrokerNodeGroupInfo=None, ClusterName=None, EncryptionInfo=None, EnhancedMonitoring=None, KafkaVersion=None, NumberOfBrokerNodes=None):
    """
    Creates a new MSK cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.create_cluster(
        BrokerNodeGroupInfo={
            'BrokerAZDistribution': 'DEFAULT',
            'ClientSubnets': [
                'string',
            ],
            'InstanceType': 'string',
            'SecurityGroups': [
                'string',
            ],
            'StorageInfo': {
                'EbsStorageInfo': {
                    'VolumeSize': 123
                }
            }
        },
        ClusterName='string',
        EncryptionInfo={
            'EncryptionAtRest': {
                'DataVolumeKMSKeyId': 'string'
            }
        },
        EnhancedMonitoring='DEFAULT'|'PER_BROKER'|'PER_TOPIC_PER_BROKER',
        KafkaVersion='string',
        NumberOfBrokerNodes=123
    )
    
    
    :type BrokerNodeGroupInfo: dict
    :param BrokerNodeGroupInfo: [REQUIRED]
            Information about the broker nodes in the cluster.
            BrokerAZDistribution (string) --The distribution of broker nodes across Availability Zones.
            ClientSubnets (list) -- [REQUIRED]The list of subnets to connect to in the client virtual private cloud (VPC). AWS creates elastic network interfaces inside these subnets. Client applications use elastic network interfaces to produce and consume data. Client subnets can't be in Availability Zone us-east-1e.
            (string) --
            InstanceType (string) -- [REQUIRED]The type of Amazon EC2 instances to use for Kafka brokers. The following instance types are allowed: kafka.m5.large, kafka.m5.xlarge, kafka.m5.2xlarge, kafka.m5.4xlarge, kafka.m5.12xlarge, and kafka.m5.24xlarge.
            SecurityGroups (list) --The AWS security groups to associate with the elastic network interfaces in order to specify who can connect to and communicate with the Amazon MSK cluster.
            (string) --
            StorageInfo (dict) --Contains information about storage volumes attached to MSK broker nodes.
            EbsStorageInfo (dict) --EBS volume information.
            VolumeSize (integer) --The size in GiB of the EBS volume for the data drive on each broker node.
            
            

    :type ClusterName: string
    :param ClusterName: [REQUIRED]
            The name of the cluster.
            

    :type EncryptionInfo: dict
    :param EncryptionInfo: Includes all encryption-related information.
            EncryptionAtRest (dict) --The data volume encryption details.
            DataVolumeKMSKeyId (string) -- [REQUIRED]The AWS KMS key used for data encryption.
            
            

    :type EnhancedMonitoring: string
    :param EnhancedMonitoring: Specifies the level of monitoring for the MSK cluster. The possible values are DEFAULT, PER_BROKER, and PER_TOPIC_PER_BROKER.

    :type KafkaVersion: string
    :param KafkaVersion: [REQUIRED]
            The version of Apache Kafka.
            

    :type NumberOfBrokerNodes: integer
    :param NumberOfBrokerNodes: [REQUIRED]
            The number of Kafka broker nodes in the Amazon MSK cluster.
            

    :rtype: dict
    :return: {
        'ClusterArn': 'string',
        'ClusterName': 'string',
        'State': 'ACTIVE'|'CREATING'|'DELETING'|'FAILED'
    }
    
    
    """
    pass

def delete_cluster(ClusterArn=None, CurrentVersion=None):
    """
    Deletes the MSK cluster specified by the Amazon Resource Name (ARN) in the request.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_cluster(
        ClusterArn='string',
        CurrentVersion='string'
    )
    
    
    :type ClusterArn: string
    :param ClusterArn: [REQUIRED]
            The Amazon Resource Name (ARN) that uniquely identifies the cluster.
            

    :type CurrentVersion: string
    :param CurrentVersion: The current version of the MSK cluster.

    :rtype: dict
    :return: {
        'ClusterArn': 'string',
        'State': 'ACTIVE'|'CREATING'|'DELETING'|'FAILED'
    }
    
    
    """
    pass

def describe_cluster(ClusterArn=None):
    """
    Returns a description of the MSK cluster whose Amazon Resource Name (ARN) is specified in the request.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_cluster(
        ClusterArn='string'
    )
    
    
    :type ClusterArn: string
    :param ClusterArn: [REQUIRED]
            The Amazon Resource Name (ARN) that uniquely identifies the cluster.
            

    :rtype: dict
    :return: {
        'ClusterInfo': {
            'BrokerNodeGroupInfo': {
                'BrokerAZDistribution': 'DEFAULT',
                'ClientSubnets': [
                    'string',
                ],
                'InstanceType': 'string',
                'SecurityGroups': [
                    'string',
                ],
                'StorageInfo': {
                    'EbsStorageInfo': {
                        'VolumeSize': 123
                    }
                }
            },
            'ClusterArn': 'string',
            'ClusterName': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'CurrentBrokerSoftwareInfo': {
                'ConfigurationArn': 'string',
                'ConfigurationRevision': 'string',
                'KafkaVersion': 'string'
            },
            'CurrentVersion': 'string',
            'EncryptionInfo': {
                'EncryptionAtRest': {
                    'DataVolumeKMSKeyId': 'string'
                }
            },
            'EnhancedMonitoring': 'DEFAULT'|'PER_BROKER'|'PER_TOPIC_PER_BROKER',
            'NumberOfBrokerNodes': 123,
            'State': 'ACTIVE'|'CREATING'|'DELETING'|'FAILED',
            'ZookeeperConnectString': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
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

def get_bootstrap_brokers(ClusterArn=None):
    """
    A list of brokers that a client application can use to bootstrap.
    See also: AWS API Documentation
    
    
    :example: response = client.get_bootstrap_brokers(
        ClusterArn='string'
    )
    
    
    :type ClusterArn: string
    :param ClusterArn: [REQUIRED]
            The Amazon Resource Name (ARN) that uniquely identifies the cluster.
            

    :rtype: dict
    :return: {
        'BootstrapBrokerString': 'string'
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

def get_waiter(waiter_name=None):
    """
    Returns an object that can wait for some condition.
    
    :type waiter_name: str
    :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.

    :rtype: botocore.waiter.Waiter
    """
    pass

def list_clusters(ClusterNameFilter=None, MaxResults=None, NextToken=None):
    """
    Returns a list of clusters in an account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_clusters(
        ClusterNameFilter='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ClusterNameFilter: string
    :param ClusterNameFilter: Specify a prefix of the name of the clusters that you want to list. The service lists all the clusters whose names start with this prefix.

    :type MaxResults: integer
    :param MaxResults: The maximum number of clusters to return in the response. If there are more clusters, the response includes a NextToken parameter.

    :type NextToken: string
    :param NextToken: The paginated results marker. When the result of a ListClusters operation is truncated, the call returns NextToken in the response. To get another batch of clusters, provide this token in your next request.

    :rtype: dict
    :return: {
        'ClusterInfoList': [
            {
                'BrokerNodeGroupInfo': {
                    'BrokerAZDistribution': 'DEFAULT',
                    'ClientSubnets': [
                        'string',
                    ],
                    'InstanceType': 'string',
                    'SecurityGroups': [
                        'string',
                    ],
                    'StorageInfo': {
                        'EbsStorageInfo': {
                            'VolumeSize': 123
                        }
                    }
                },
                'ClusterArn': 'string',
                'ClusterName': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'CurrentBrokerSoftwareInfo': {
                    'ConfigurationArn': 'string',
                    'ConfigurationRevision': 'string',
                    'KafkaVersion': 'string'
                },
                'CurrentVersion': 'string',
                'EncryptionInfo': {
                    'EncryptionAtRest': {
                        'DataVolumeKMSKeyId': 'string'
                    }
                },
                'EnhancedMonitoring': 'DEFAULT'|'PER_BROKER'|'PER_TOPIC_PER_BROKER',
                'NumberOfBrokerNodes': 123,
                'State': 'ACTIVE'|'CREATING'|'DELETING'|'FAILED',
                'ZookeeperConnectString': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_nodes(ClusterArn=None, MaxResults=None, NextToken=None):
    """
    Returns a list of the broker nodes in the cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.list_nodes(
        ClusterArn='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ClusterArn: string
    :param ClusterArn: [REQUIRED]
            The Amazon Resource Name (ARN) that uniquely identifies the cluster.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of clusters to return in the response. If there are more clusters, the response includes a NextToken parameter.

    :type NextToken: string
    :param NextToken: The paginated results marker. When the result of a ListClusters operation is truncated, the call returns NextToken in the response. To get another batch of clusters, provide this token in your next request.

    :rtype: dict
    :return: {
        'NextToken': 'string',
        'NodeInfoList': [
            {
                'AddedToClusterTime': 'string',
                'BrokerNodeInfo': {
                    'AttachedENIId': 'string',
                    'BrokerId': 123.0,
                    'ClientSubnet': 'string',
                    'ClientVpcIpAddress': 'string',
                    'CurrentBrokerSoftwareInfo': {
                        'ConfigurationArn': 'string',
                        'ConfigurationRevision': 'string',
                        'KafkaVersion': 'string'
                    }
                },
                'InstanceType': 'string',
                'NodeARN': 'string',
                'NodeType': 'BROKER',
                'ZookeeperNodeInfo': {
                    'AttachedENIId': 'string',
                    'ClientVpcIpAddress': 'string',
                    'ZookeeperId': 123.0,
                    'ZookeeperVersion': 'string'
                }
            },
        ]
    }
    
    
    """
    pass

