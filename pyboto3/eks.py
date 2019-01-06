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

def create_cluster(name=None, version=None, roleArn=None, resourcesVpcConfig=None, clientRequestToken=None):
    """
    Creates an Amazon EKS control plane.
    The Amazon EKS control plane consists of control plane instances that run the Kubernetes software, like etcd and the API server. The control plane runs in an account managed by AWS, and the Kubernetes API is exposed via the Amazon EKS API server endpoint.
    Amazon EKS worker nodes run in your AWS account and connect to your cluster's control plane via the Kubernetes API server endpoint and a certificate file that is created for your cluster.
    The cluster control plane is provisioned across multiple Availability Zones and fronted by an Elastic Load Balancing Network Load Balancer. Amazon EKS also provisions elastic network interfaces in your VPC subnets to provide connectivity from the control plane instances to the worker nodes (for example, to support kubectl exec , logs , and proxy data flows).
    After you create an Amazon EKS cluster, you must configure your Kubernetes tooling to communicate with the API server and launch worker nodes into your cluster. For more information, see Managing Cluster Authentication and Launching Amazon EKS Worker Nodes in the Amazon EKS User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_cluster(
        name='string',
        version='string',
        roleArn='string',
        resourcesVpcConfig={
            'subnetIds': [
                'string',
            ],
            'securityGroupIds': [
                'string',
            ]
        },
        clientRequestToken='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The unique name to give to your cluster.
            

    :type version: string
    :param version: The desired Kubernetes version for your cluster. If you do not specify a value here, the latest version available in Amazon EKS is used.

    :type roleArn: string
    :param roleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM role that provides permissions for Amazon EKS to make calls to other AWS API operations on your behalf. For more information, see Amazon EKS Service IAM Role in the * Amazon EKS User Guide * .
            

    :type resourcesVpcConfig: dict
    :param resourcesVpcConfig: [REQUIRED]
            The VPC subnets and security groups used by the cluster control plane. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see Cluster VPC Considerations and Cluster Security Group Considerations in the Amazon EKS User Guide . You must specify at least two subnets. You may specify up to five security groups, but we recommend that you use a dedicated security group for your cluster control plane.
            subnetIds (list) -- [REQUIRED]Specify subnets for your Amazon EKS worker nodes. Amazon EKS creates cross-account elastic network interfaces in these subnets to allow communication between your worker nodes and the Kubernetes control plane.
            (string) --
            securityGroupIds (list) --Specify one or more security groups for the cross-account elastic network interfaces that Amazon EKS creates to use to allow communication between your worker nodes and the Kubernetes control plane. If you do not specify a security group, the default security group for your VPC is used.
            (string) --
            

    :type clientRequestToken: string
    :param clientRequestToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'cluster': {
            'name': 'string',
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'version': 'string',
            'endpoint': 'string',
            'roleArn': 'string',
            'resourcesVpcConfig': {
                'subnetIds': [
                    'string',
                ],
                'securityGroupIds': [
                    'string',
                ],
                'vpcId': 'string'
            },
            'status': 'CREATING'|'ACTIVE'|'DELETING'|'FAILED',
            'certificateAuthority': {
                'data': 'string'
            },
            'clientRequestToken': 'string',
            'platformVersion': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_cluster(name=None):
    """
    Deletes the Amazon EKS cluster control plane.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_cluster(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the cluster to delete.
            

    :rtype: dict
    :return: {
        'cluster': {
            'name': 'string',
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'version': 'string',
            'endpoint': 'string',
            'roleArn': 'string',
            'resourcesVpcConfig': {
                'subnetIds': [
                    'string',
                ],
                'securityGroupIds': [
                    'string',
                ],
                'vpcId': 'string'
            },
            'status': 'CREATING'|'ACTIVE'|'DELETING'|'FAILED',
            'certificateAuthority': {
                'data': 'string'
            },
            'clientRequestToken': 'string',
            'platformVersion': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_cluster(name=None):
    """
    Returns descriptive information about an Amazon EKS cluster.
    The API server endpoint and certificate authority data returned by this operation are required for kubelet and kubectl to communicate with your Kubernetes API server. For more information, see Create a kubeconfig for Amazon EKS .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_cluster(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the cluster to describe.
            

    :rtype: dict
    :return: {
        'cluster': {
            'name': 'string',
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'version': 'string',
            'endpoint': 'string',
            'roleArn': 'string',
            'resourcesVpcConfig': {
                'subnetIds': [
                    'string',
                ],
                'securityGroupIds': [
                    'string',
                ],
                'vpcId': 'string'
            },
            'status': 'CREATING'|'ACTIVE'|'DELETING'|'FAILED',
            'certificateAuthority': {
                'data': 'string'
            },
            'clientRequestToken': 'string',
            'platformVersion': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_update(name=None, updateId=None):
    """
    Returns descriptive information about an update against your Amazon EKS cluster.
    When the status of the update is Succeeded , the update is complete. If an update fails, the status is Failed , and an error detail explains the reason for the failure.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_update(
        name='string',
        updateId='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the Amazon EKS cluster to update.
            

    :type updateId: string
    :param updateId: [REQUIRED]
            The ID of the update to describe.
            

    :rtype: dict
    :return: {
        'update': {
            'id': 'string',
            'status': 'InProgress'|'Failed'|'Cancelled'|'Successful',
            'type': 'VersionUpdate',
            'params': [
                {
                    'type': 'Version'|'PlatformVersion',
                    'value': 'string'
                },
            ],
            'createdAt': datetime(2015, 1, 1),
            'errors': [
                {
                    'errorCode': 'SubnetNotFound'|'SecurityGroupNotFound'|'EniLimitReached'|'IpNotAvailable'|'AccessDenied'|'OperationNotPermitted'|'VpcIdNotFound'|'Unknown',
                    'errorMessage': 'string',
                    'resourceIds': [
                        'string',
                    ]
                },
            ]
        }
    }
    
    
    :returns: 
    SubnetNotFound : One of the subnets associated with the cluster could not be found.
    SecurityGroupNotFound : One of the security groups associated with the cluster could not be found.
    EniLimitReached : You have reached the elastic network interface limit for your account.
    IpNotAvailable : A subnet associated with the cluster does not have any free IP addresses.
    AccessDenied : You do not have permissions to perform the specified operation.
    OperationNotPermitted : The service role associated with the cluster does not have the required access permissions for Amazon EKS.
    VpcIdNotFound : The VPC associated with the cluster could not be found.
    
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

def list_clusters(maxResults=None, nextToken=None):
    """
    Lists the Amazon EKS clusters in your AWS account in the specified Region.
    See also: AWS API Documentation
    
    
    :example: response = client.list_clusters(
        maxResults=123,
        nextToken='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: The maximum number of cluster results returned by ListClusters in paginated output. When this parameter is used, ListClusters only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListClusters request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListClusters returns up to 100 results and a nextToken value if applicable.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListClusters request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            

    :rtype: dict
    :return: {
        'clusters': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_updates(name=None, nextToken=None, maxResults=None):
    """
    Lists the updates associated with an Amazon EKS cluster in your AWS account, in the specified Region.
    See also: AWS API Documentation
    
    
    :example: response = client.list_updates(
        name='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the Amazon EKS cluster for which to list updates.
            

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListUpdates request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.

    :type maxResults: integer
    :param maxResults: The maximum number of update results returned by ListUpdates in paginated output. When this parameter is used, ListUpdates only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListUpdates request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListUpdates returns up to 100 results and a nextToken value if applicable.

    :rtype: dict
    :return: {
        'updateIds': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_cluster_version(name=None, version=None, clientRequestToken=None):
    """
    Updates an Amazon EKS cluster to the specified Kubernetes version. Your cluster continues to function during the update. The response output includes an update ID that you can use to track the status of your cluster update with the  DescribeUpdate API operation.
    Cluster updates are asynchronous, and they should finish within a few minutes. During an update, the cluster status moves to UPDATING (this status transition is eventually consistent). When the update is complete (either Failed or Successful ), the cluster status moves to Active .
    See also: AWS API Documentation
    
    
    :example: response = client.update_cluster_version(
        name='string',
        version='string',
        clientRequestToken='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the Amazon EKS cluster to update.
            

    :type version: string
    :param version: [REQUIRED]
            The desired Kubernetes version following a successful update.
            

    :type clientRequestToken: string
    :param clientRequestToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'update': {
            'id': 'string',
            'status': 'InProgress'|'Failed'|'Cancelled'|'Successful',
            'type': 'VersionUpdate',
            'params': [
                {
                    'type': 'Version'|'PlatformVersion',
                    'value': 'string'
                },
            ],
            'createdAt': datetime(2015, 1, 1),
            'errors': [
                {
                    'errorCode': 'SubnetNotFound'|'SecurityGroupNotFound'|'EniLimitReached'|'IpNotAvailable'|'AccessDenied'|'OperationNotPermitted'|'VpcIdNotFound'|'Unknown',
                    'errorMessage': 'string',
                    'resourceIds': [
                        'string',
                    ]
                },
            ]
        }
    }
    
    
    :returns: 
    SubnetNotFound : One of the subnets associated with the cluster could not be found.
    SecurityGroupNotFound : One of the security groups associated with the cluster could not be found.
    EniLimitReached : You have reached the elastic network interface limit for your account.
    IpNotAvailable : A subnet associated with the cluster does not have any free IP addresses.
    AccessDenied : You do not have permissions to perform the specified operation.
    OperationNotPermitted : The service role associated with the cluster does not have the required access permissions for Amazon EKS.
    VpcIdNotFound : The VPC associated with the cluster could not be found.
    
    """
    pass

