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

def cancel_job(jobId=None, reason=None):
    """
    Cancels a job in an AWS Batch job queue. Jobs that are in the SUBMITTED , PENDING , or RUNNABLE state are cancelled. Jobs that have progressed to STARTING or RUNNING are not cancelled (but the API operation still succeeds, even if no job is cancelled); these jobs must be terminated with the  TerminateJob operation.
    See also: AWS API Documentation
    
    Examples
    This example cancels a job with the specified job ID.
    Expected Output:
    
    :example: response = client.cancel_job(
        jobId='string',
        reason='string'
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]
            The AWS Batch job ID of the job to cancel.
            

    :type reason: string
    :param reason: [REQUIRED]
            A message to attach to the job that explains the reason for canceling it. This message is returned by future DescribeJobs operations on the job. This message is also recorded in the AWS Batch activity logs.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_compute_environment(computeEnvironmentName=None, type=None, state=None, computeResources=None, serviceRole=None):
    """
    Creates an AWS Batch compute environment. You can create MANAGED or UNMANAGED compute environments.
    In a managed compute environment, AWS Batch manages the capacity and instance types of the compute resources within the environment. This is based on the compute resource specification that you define or the launch template that you specify when you create the compute environment. You can choose to use Amazon EC2 On-Demand Instances or Spot Instances in your managed compute environment. You can optionally set a maximum price so that Spot Instances only launch when the Spot Instance price is below a specified percentage of the On-Demand price.
    In an unmanaged compute environment, you can manage your own compute resources. This provides more compute resource configuration options, such as using a custom AMI, but you must ensure that your AMI meets the Amazon ECS container instance AMI specification. For more information, see Container Instance AMIs in the Amazon Elastic Container Service Developer Guide . After you have created your unmanaged compute environment, you can use the  DescribeComputeEnvironments operation to find the Amazon ECS cluster that is associated with it. Then, manually launch your container instances into that Amazon ECS cluster. For more information, see Launching an Amazon ECS Container Instance in the Amazon Elastic Container Service Developer Guide .
    See also: AWS API Documentation
    
    Examples
    This example creates a managed compute environment with specific C4 instance types that are launched on demand. The compute environment is called C4OnDemand.
    Expected Output:
    This example creates a managed compute environment with the M4 instance type that is launched when the Spot bid price is at or below 20% of the On-Demand price for the instance type. The compute environment is called M4Spot.
    Expected Output:
    
    :example: response = client.create_compute_environment(
        computeEnvironmentName='string',
        type='MANAGED'|'UNMANAGED',
        state='ENABLED'|'DISABLED',
        computeResources={
            'type': 'EC2'|'SPOT',
            'minvCpus': 123,
            'maxvCpus': 123,
            'desiredvCpus': 123,
            'instanceTypes': [
                'string',
            ],
            'imageId': 'string',
            'subnets': [
                'string',
            ],
            'securityGroupIds': [
                'string',
            ],
            'ec2KeyPair': 'string',
            'instanceRole': 'string',
            'tags': {
                'string': 'string'
            },
            'placementGroup': 'string',
            'bidPercentage': 123,
            'spotIamFleetRole': 'string',
            'launchTemplate': {
                'launchTemplateId': 'string',
                'launchTemplateName': 'string',
                'version': 'string'
            }
        },
        serviceRole='string'
    )
    
    
    :type computeEnvironmentName: string
    :param computeEnvironmentName: [REQUIRED]
            The name for your compute environment. Up to 128 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.
            

    :type type: string
    :param type: [REQUIRED]
            The type of the compute environment. For more information, see Compute Environments in the AWS Batch User Guide .
            

    :type state: string
    :param state: The state of the compute environment. If the state is ENABLED , then the compute environment accepts jobs from a queue and can scale out automatically based on queues.

    :type computeResources: dict
    :param computeResources: Details of the compute resources managed by the compute environment. This parameter is required for managed compute environments.
            type (string) -- [REQUIRED]The type of compute environment.
            minvCpus (integer) -- [REQUIRED]The minimum number of EC2 vCPUs that an environment should maintain (even if the compute environment is DISABLED ).
            maxvCpus (integer) -- [REQUIRED]The maximum number of EC2 vCPUs that an environment can reach.
            desiredvCpus (integer) --The desired number of EC2 vCPUS in the compute environment.
            instanceTypes (list) -- [REQUIRED]The instances types that may be launched. You can specify instance families to launch any instance type within those families (for example, c4 or p3 ), or you can specify specific sizes within a family (such as c4.8xlarge ). You can also choose optimal to pick instance types (from the latest C, M, and R instance families) on the fly that match the demand of your job queues.
            (string) --
            imageId (string) --The Amazon Machine Image (AMI) ID used for instances launched in the compute environment.
            subnets (list) -- [REQUIRED]The VPC subnets into which the compute resources are launched.
            (string) --
            securityGroupIds (list) --The EC2 security group that is associated with instances launched in the compute environment.
            (string) --
            ec2KeyPair (string) --The EC2 key pair that is used for instances launched in the compute environment.
            instanceRole (string) -- [REQUIRED]The Amazon ECS instance profile applied to Amazon EC2 instances in a compute environment. You can specify the short name or full Amazon Resource Name (ARN) of an instance profile. For example, ecsInstanceRole or arn:aws:iam::<aws_account_id>:instance-profile/ecsInstanceRole . For more information, see Amazon ECS Instance Role in the AWS Batch User Guide .
            tags (dict) --Key-value pair tags to be applied to resources that are launched in the compute environment.
            (string) --
            (string) --
            
            placementGroup (string) --The Amazon EC2 placement group to associate with your compute resources. If you intend to submit multi-node parallel jobs to your compute environment, you should consider creating a cluster placement group and associate it with your compute resources. This keeps your multi-node parallel job on a logical grouping of instances within a single Availability Zone with high network flow potential. For more information, see Placement Groups in the Amazon EC2 User Guide for Linux Instances .
            bidPercentage (integer) --The maximum percentage that a Spot Instance price can be when compared with the On-Demand price for that instance type before instances are launched. For example, if your maximum percentage is 20%, then the Spot price must be below 20% of the current On-Demand price for that EC2 instance. You always pay the lowest (market) price and never more than your maximum percentage. If you leave this field empty, the default value is 100% of the On-Demand price.
            spotIamFleetRole (string) --The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a SPOT compute environment.
            launchTemplate (dict) --The launch template to use for your compute resources. Any other compute resource parameters that you specify in a CreateComputeEnvironment API operation override the same parameters in the launch template. You must specify either the launch template ID or launch template name in the request, but not both.
            launchTemplateId (string) --The ID of the launch template.
            launchTemplateName (string) --The name of the launch template.
            version (string) --The version number of the launch template.
            Default: The default version of the launch template.
            
            

    :type serviceRole: string
    :param serviceRole: [REQUIRED]
            The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.
            If your specified role has a path other than / , then you must either specify the full role ARN (this is recommended) or prefix the role name with the path.
            Note
            Depending on how you created your AWS Batch service role, its ARN may contain the service-role path prefix. When you only specify the name of the service role, AWS Batch assumes that your ARN does not use the service-role path prefix. Because of this, we recommend that you specify the full ARN of your service role when you create compute environments.
            

    :rtype: dict
    :return: {
        'computeEnvironmentName': 'string',
        'computeEnvironmentArn': 'string'
    }
    
    
    :returns: 
    computeEnvironmentName (string) -- [REQUIRED]
    The name for your compute environment. Up to 128 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.
    
    type (string) -- [REQUIRED]
    The type of the compute environment. For more information, see Compute Environments in the AWS Batch User Guide .
    
    state (string) -- The state of the compute environment. If the state is ENABLED , then the compute environment accepts jobs from a queue and can scale out automatically based on queues.
    computeResources (dict) -- Details of the compute resources managed by the compute environment. This parameter is required for managed compute environments.
    
    type (string) -- [REQUIRED]The type of compute environment.
    
    minvCpus (integer) -- [REQUIRED]The minimum number of EC2 vCPUs that an environment should maintain (even if the compute environment is DISABLED ).
    
    maxvCpus (integer) -- [REQUIRED]The maximum number of EC2 vCPUs that an environment can reach.
    
    desiredvCpus (integer) --The desired number of EC2 vCPUS in the compute environment.
    
    instanceTypes (list) -- [REQUIRED]The instances types that may be launched. You can specify instance families to launch any instance type within those families (for example, c4 or p3 ), or you can specify specific sizes within a family (such as c4.8xlarge ). You can also choose optimal to pick instance types (from the latest C, M, and R instance families) on the fly that match the demand of your job queues.
    
    (string) --
    
    
    imageId (string) --The Amazon Machine Image (AMI) ID used for instances launched in the compute environment.
    
    subnets (list) -- [REQUIRED]The VPC subnets into which the compute resources are launched.
    
    (string) --
    
    
    securityGroupIds (list) --The EC2 security group that is associated with instances launched in the compute environment.
    
    (string) --
    
    
    ec2KeyPair (string) --The EC2 key pair that is used for instances launched in the compute environment.
    
    instanceRole (string) -- [REQUIRED]The Amazon ECS instance profile applied to Amazon EC2 instances in a compute environment. You can specify the short name or full Amazon Resource Name (ARN) of an instance profile. For example, ecsInstanceRole or arn:aws:iam::<aws_account_id>:instance-profile/ecsInstanceRole . For more information, see Amazon ECS Instance Role in the AWS Batch User Guide .
    
    tags (dict) --Key-value pair tags to be applied to resources that are launched in the compute environment.
    
    (string) --
    (string) --
    
    
    
    
    placementGroup (string) --The Amazon EC2 placement group to associate with your compute resources. If you intend to submit multi-node parallel jobs to your compute environment, you should consider creating a cluster placement group and associate it with your compute resources. This keeps your multi-node parallel job on a logical grouping of instances within a single Availability Zone with high network flow potential. For more information, see Placement Groups in the Amazon EC2 User Guide for Linux Instances .
    
    bidPercentage (integer) --The maximum percentage that a Spot Instance price can be when compared with the On-Demand price for that instance type before instances are launched. For example, if your maximum percentage is 20%, then the Spot price must be below 20% of the current On-Demand price for that EC2 instance. You always pay the lowest (market) price and never more than your maximum percentage. If you leave this field empty, the default value is 100% of the On-Demand price.
    
    spotIamFleetRole (string) --The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a SPOT compute environment.
    
    launchTemplate (dict) --The launch template to use for your compute resources. Any other compute resource parameters that you specify in a  CreateComputeEnvironment API operation override the same parameters in the launch template. You must specify either the launch template ID or launch template name in the request, but not both.
    
    launchTemplateId (string) --The ID of the launch template.
    
    launchTemplateName (string) --The name of the launch template.
    
    version (string) --The version number of the launch template.
    Default: The default version of the launch template.
    
    
    
    
    
    serviceRole (string) -- [REQUIRED]
    The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.
    If your specified role has a path other than / , then you must either specify the full role ARN (this is recommended) or prefix the role name with the path.
    
    Note
    Depending on how you created your AWS Batch service role, its ARN may contain the service-role path prefix. When you only specify the name of the service role, AWS Batch assumes that your ARN does not use the service-role path prefix. Because of this, we recommend that you specify the full ARN of your service role when you create compute environments.
    
    
    
    """
    pass

def create_job_queue(jobQueueName=None, state=None, priority=None, computeEnvironmentOrder=None):
    """
    Creates an AWS Batch job queue. When you create a job queue, you associate one or more compute environments to the queue and assign an order of preference for the compute environments.
    You also set a priority to the job queue that determines the order in which the AWS Batch scheduler places jobs onto its associated compute environments. For example, if a compute environment is associated with more than one job queue, the job queue with a higher priority is given preference for scheduling jobs to that compute environment.
    See also: AWS API Documentation
    
    Examples
    This example creates a job queue called LowPriority that uses the M4Spot compute environment.
    Expected Output:
    This example creates a job queue called HighPriority that uses the C4OnDemand compute environment with an order of 1 and the M4Spot compute environment with an order of 2.
    Expected Output:
    
    :example: response = client.create_job_queue(
        jobQueueName='string',
        state='ENABLED'|'DISABLED',
        priority=123,
        computeEnvironmentOrder=[
            {
                'order': 123,
                'computeEnvironment': 'string'
            },
        ]
    )
    
    
    :type jobQueueName: string
    :param jobQueueName: [REQUIRED]
            The name of the job queue.
            

    :type state: string
    :param state: The state of the job queue. If the job queue state is ENABLED , it is able to accept jobs.

    :type priority: integer
    :param priority: [REQUIRED]
            The priority of the job queue. Job queues with a higher priority (or a higher integer value for the priority parameter) are evaluated first when associated with the same compute environment. Priority is determined in descending order, for example, a job queue with a priority value of 10 is given scheduling preference over a job queue with a priority value of 1 .
            

    :type computeEnvironmentOrder: list
    :param computeEnvironmentOrder: [REQUIRED]
            The set of compute environments mapped to a job queue and their order relative to each other. The job scheduler uses this parameter to determine which compute environment should execute a given job. Compute environments must be in the VALID state before you can associate them with a job queue. You can associate up to three compute environments with a job queue.
            (dict) --The order in which compute environments are tried for job placement within a queue. Compute environments are tried in ascending order. For example, if two compute environments are associated with a job queue, the compute environment with a lower order integer value is tried for job placement first.
            order (integer) -- [REQUIRED]The order of the compute environment.
            computeEnvironment (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the compute environment.
            
            

    :rtype: dict
    :return: {
        'jobQueueName': 'string',
        'jobQueueArn': 'string'
    }
    
    
    """
    pass

def delete_compute_environment(computeEnvironment=None):
    """
    Deletes an AWS Batch compute environment.
    Before you can delete a compute environment, you must set its state to DISABLED with the  UpdateComputeEnvironment API operation and disassociate it from any job queues with the  UpdateJobQueue API operation.
    See also: AWS API Documentation
    
    Examples
    This example deletes the P2OnDemand compute environment.
    Expected Output:
    
    :example: response = client.delete_compute_environment(
        computeEnvironment='string'
    )
    
    
    :type computeEnvironment: string
    :param computeEnvironment: [REQUIRED]
            The name or Amazon Resource Name (ARN) of the compute environment to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_job_queue(jobQueue=None):
    """
    Deletes the specified job queue. You must first disable submissions for a queue with the  UpdateJobQueue operation. All jobs in the queue are terminated when you delete a job queue.
    It is not necessary to disassociate compute environments from a queue before submitting a DeleteJobQueue request.
    See also: AWS API Documentation
    
    Examples
    This example deletes the GPGPU job queue.
    Expected Output:
    
    :example: response = client.delete_job_queue(
        jobQueue='string'
    )
    
    
    :type jobQueue: string
    :param jobQueue: [REQUIRED]
            The short name or full Amazon Resource Name (ARN) of the queue to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def deregister_job_definition(jobDefinition=None):
    """
    Deregisters an AWS Batch job definition.
    See also: AWS API Documentation
    
    Examples
    This example deregisters a job definition called sleep10.
    Expected Output:
    
    :example: response = client.deregister_job_definition(
        jobDefinition='string'
    )
    
    
    :type jobDefinition: string
    :param jobDefinition: [REQUIRED]
            The name and revision (name:revision ) or full Amazon Resource Name (ARN) of the job definition to deregister.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_compute_environments(computeEnvironments=None, maxResults=None, nextToken=None):
    """
    Describes one or more of your compute environments.
    If you are using an unmanaged compute environment, you can use the DescribeComputeEnvironment operation to determine the ecsClusterArn that you should launch your Amazon ECS container instances into.
    See also: AWS API Documentation
    
    Examples
    This example describes the P2OnDemand compute environment.
    Expected Output:
    
    :example: response = client.describe_compute_environments(
        computeEnvironments=[
            'string',
        ],
        maxResults=123,
        nextToken='string'
    )
    
    
    :type computeEnvironments: list
    :param computeEnvironments: A list of up to 100 compute environment names or full Amazon Resource Name (ARN) entries.
            (string) --
            

    :type maxResults: integer
    :param maxResults: The maximum number of cluster results returned by DescribeComputeEnvironments in paginated output. When this parameter is used, DescribeComputeEnvironments only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another DescribeComputeEnvironments request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then DescribeComputeEnvironments returns up to 100 results and a nextToken value if applicable.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated DescribeComputeEnvironments request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            

    :rtype: dict
    :return: {
        'computeEnvironments': [
            {
                'computeEnvironmentName': 'string',
                'computeEnvironmentArn': 'string',
                'ecsClusterArn': 'string',
                'type': 'MANAGED'|'UNMANAGED',
                'state': 'ENABLED'|'DISABLED',
                'status': 'CREATING'|'UPDATING'|'DELETING'|'DELETED'|'VALID'|'INVALID',
                'statusReason': 'string',
                'computeResources': {
                    'type': 'EC2'|'SPOT',
                    'minvCpus': 123,
                    'maxvCpus': 123,
                    'desiredvCpus': 123,
                    'instanceTypes': [
                        'string',
                    ],
                    'imageId': 'string',
                    'subnets': [
                        'string',
                    ],
                    'securityGroupIds': [
                        'string',
                    ],
                    'ec2KeyPair': 'string',
                    'instanceRole': 'string',
                    'tags': {
                        'string': 'string'
                    },
                    'placementGroup': 'string',
                    'bidPercentage': 123,
                    'spotIamFleetRole': 'string',
                    'launchTemplate': {
                        'launchTemplateId': 'string',
                        'launchTemplateName': 'string',
                        'version': 'string'
                    }
                },
                'serviceRole': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_job_definitions(jobDefinitions=None, maxResults=None, jobDefinitionName=None, status=None, nextToken=None):
    """
    Describes a list of job definitions. You can specify a status (such as ACTIVE ) to only return job definitions that match that status.
    See also: AWS API Documentation
    
    Examples
    This example describes all of your active job definitions.
    Expected Output:
    
    :example: response = client.describe_job_definitions(
        jobDefinitions=[
            'string',
        ],
        maxResults=123,
        jobDefinitionName='string',
        status='string',
        nextToken='string'
    )
    
    
    :type jobDefinitions: list
    :param jobDefinitions: A space-separated list of up to 100 job definition names or full Amazon Resource Name (ARN) entries.
            (string) --
            

    :type maxResults: integer
    :param maxResults: The maximum number of results returned by DescribeJobDefinitions in paginated output. When this parameter is used, DescribeJobDefinitions only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another DescribeJobDefinitions request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then DescribeJobDefinitions returns up to 100 results and a nextToken value if applicable.

    :type jobDefinitionName: string
    :param jobDefinitionName: The name of the job definition to describe.

    :type status: string
    :param status: The status with which to filter job definitions.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated DescribeJobDefinitions request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            

    :rtype: dict
    :return: {
        'jobDefinitions': [
            {
                'jobDefinitionName': 'string',
                'jobDefinitionArn': 'string',
                'revision': 123,
                'status': 'string',
                'type': 'string',
                'parameters': {
                    'string': 'string'
                },
                'retryStrategy': {
                    'attempts': 123
                },
                'containerProperties': {
                    'image': 'string',
                    'vcpus': 123,
                    'memory': 123,
                    'command': [
                        'string',
                    ],
                    'jobRoleArn': 'string',
                    'volumes': [
                        {
                            'host': {
                                'sourcePath': 'string'
                            },
                            'name': 'string'
                        },
                    ],
                    'environment': [
                        {
                            'name': 'string',
                            'value': 'string'
                        },
                    ],
                    'mountPoints': [
                        {
                            'containerPath': 'string',
                            'readOnly': True|False,
                            'sourceVolume': 'string'
                        },
                    ],
                    'readonlyRootFilesystem': True|False,
                    'privileged': True|False,
                    'ulimits': [
                        {
                            'hardLimit': 123,
                            'name': 'string',
                            'softLimit': 123
                        },
                    ],
                    'user': 'string',
                    'instanceType': 'string'
                },
                'timeout': {
                    'attemptDurationSeconds': 123
                },
                'nodeProperties': {
                    'numNodes': 123,
                    'mainNode': 123,
                    'nodeRangeProperties': [
                        {
                            'targetNodes': 'string',
                            'container': {
                                'image': 'string',
                                'vcpus': 123,
                                'memory': 123,
                                'command': [
                                    'string',
                                ],
                                'jobRoleArn': 'string',
                                'volumes': [
                                    {
                                        'host': {
                                            'sourcePath': 'string'
                                        },
                                        'name': 'string'
                                    },
                                ],
                                'environment': [
                                    {
                                        'name': 'string',
                                        'value': 'string'
                                    },
                                ],
                                'mountPoints': [
                                    {
                                        'containerPath': 'string',
                                        'readOnly': True|False,
                                        'sourceVolume': 'string'
                                    },
                                ],
                                'readonlyRootFilesystem': True|False,
                                'privileged': True|False,
                                'ulimits': [
                                    {
                                        'hardLimit': 123,
                                        'name': 'string',
                                        'softLimit': 123
                                    },
                                ],
                                'user': 'string',
                                'instanceType': 'string'
                            }
                        },
                    ]
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_job_queues(jobQueues=None, maxResults=None, nextToken=None):
    """
    Describes one or more of your job queues.
    See also: AWS API Documentation
    
    Examples
    This example describes the HighPriority job queue.
    Expected Output:
    
    :example: response = client.describe_job_queues(
        jobQueues=[
            'string',
        ],
        maxResults=123,
        nextToken='string'
    )
    
    
    :type jobQueues: list
    :param jobQueues: A list of up to 100 queue names or full queue Amazon Resource Name (ARN) entries.
            (string) --
            

    :type maxResults: integer
    :param maxResults: The maximum number of results returned by DescribeJobQueues in paginated output. When this parameter is used, DescribeJobQueues only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another DescribeJobQueues request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then DescribeJobQueues returns up to 100 results and a nextToken value if applicable.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated DescribeJobQueues request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            

    :rtype: dict
    :return: {
        'jobQueues': [
            {
                'jobQueueName': 'string',
                'jobQueueArn': 'string',
                'state': 'ENABLED'|'DISABLED',
                'status': 'CREATING'|'UPDATING'|'DELETING'|'DELETED'|'VALID'|'INVALID',
                'statusReason': 'string',
                'priority': 123,
                'computeEnvironmentOrder': [
                    {
                        'order': 123,
                        'computeEnvironment': 'string'
                    },
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def describe_jobs(jobs=None):
    """
    Describes a list of AWS Batch jobs.
    See also: AWS API Documentation
    
    Examples
    This example describes a job with the specified job ID.
    Expected Output:
    
    :example: response = client.describe_jobs(
        jobs=[
            'string',
        ]
    )
    
    
    :type jobs: list
    :param jobs: [REQUIRED]
            A space-separated list of up to 100 job IDs.
            (string) --
            

    :rtype: dict
    :return: {
        'jobs': [
            {
                'jobName': 'string',
                'jobId': 'string',
                'jobQueue': 'string',
                'status': 'SUBMITTED'|'PENDING'|'RUNNABLE'|'STARTING'|'RUNNING'|'SUCCEEDED'|'FAILED',
                'attempts': [
                    {
                        'container': {
                            'containerInstanceArn': 'string',
                            'taskArn': 'string',
                            'exitCode': 123,
                            'reason': 'string',
                            'logStreamName': 'string',
                            'networkInterfaces': [
                                {
                                    'attachmentId': 'string',
                                    'ipv6Address': 'string',
                                    'privateIpv4Address': 'string'
                                },
                            ]
                        },
                        'startedAt': 123,
                        'stoppedAt': 123,
                        'statusReason': 'string'
                    },
                ],
                'statusReason': 'string',
                'createdAt': 123,
                'retryStrategy': {
                    'attempts': 123
                },
                'startedAt': 123,
                'stoppedAt': 123,
                'dependsOn': [
                    {
                        'jobId': 'string',
                        'type': 'N_TO_N'|'SEQUENTIAL'
                    },
                ],
                'jobDefinition': 'string',
                'parameters': {
                    'string': 'string'
                },
                'container': {
                    'image': 'string',
                    'vcpus': 123,
                    'memory': 123,
                    'command': [
                        'string',
                    ],
                    'jobRoleArn': 'string',
                    'volumes': [
                        {
                            'host': {
                                'sourcePath': 'string'
                            },
                            'name': 'string'
                        },
                    ],
                    'environment': [
                        {
                            'name': 'string',
                            'value': 'string'
                        },
                    ],
                    'mountPoints': [
                        {
                            'containerPath': 'string',
                            'readOnly': True|False,
                            'sourceVolume': 'string'
                        },
                    ],
                    'readonlyRootFilesystem': True|False,
                    'ulimits': [
                        {
                            'hardLimit': 123,
                            'name': 'string',
                            'softLimit': 123
                        },
                    ],
                    'privileged': True|False,
                    'user': 'string',
                    'exitCode': 123,
                    'reason': 'string',
                    'containerInstanceArn': 'string',
                    'taskArn': 'string',
                    'logStreamName': 'string',
                    'instanceType': 'string',
                    'networkInterfaces': [
                        {
                            'attachmentId': 'string',
                            'ipv6Address': 'string',
                            'privateIpv4Address': 'string'
                        },
                    ]
                },
                'nodeDetails': {
                    'nodeIndex': 123,
                    'isMainNode': True|False
                },
                'nodeProperties': {
                    'numNodes': 123,
                    'mainNode': 123,
                    'nodeRangeProperties': [
                        {
                            'targetNodes': 'string',
                            'container': {
                                'image': 'string',
                                'vcpus': 123,
                                'memory': 123,
                                'command': [
                                    'string',
                                ],
                                'jobRoleArn': 'string',
                                'volumes': [
                                    {
                                        'host': {
                                            'sourcePath': 'string'
                                        },
                                        'name': 'string'
                                    },
                                ],
                                'environment': [
                                    {
                                        'name': 'string',
                                        'value': 'string'
                                    },
                                ],
                                'mountPoints': [
                                    {
                                        'containerPath': 'string',
                                        'readOnly': True|False,
                                        'sourceVolume': 'string'
                                    },
                                ],
                                'readonlyRootFilesystem': True|False,
                                'privileged': True|False,
                                'ulimits': [
                                    {
                                        'hardLimit': 123,
                                        'name': 'string',
                                        'softLimit': 123
                                    },
                                ],
                                'user': 'string',
                                'instanceType': 'string'
                            }
                        },
                    ]
                },
                'arrayProperties': {
                    'statusSummary': {
                        'string': 123
                    },
                    'size': 123,
                    'index': 123
                },
                'timeout': {
                    'attemptDurationSeconds': 123
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
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

def list_jobs(jobQueue=None, arrayJobId=None, multiNodeJobId=None, jobStatus=None, maxResults=None, nextToken=None):
    """
    Returns a list of AWS Batch jobs.
    You must specify only one of the following:
    You can filter the results by job status with the jobStatus parameter. If you do not specify a status, only RUNNING jobs are returned.
    See also: AWS API Documentation
    
    Examples
    This example lists the running jobs in the HighPriority job queue.
    Expected Output:
    This example lists jobs in the HighPriority job queue that are in the SUBMITTED job status.
    Expected Output:
    
    :example: response = client.list_jobs(
        jobQueue='string',
        arrayJobId='string',
        multiNodeJobId='string',
        jobStatus='SUBMITTED'|'PENDING'|'RUNNABLE'|'STARTING'|'RUNNING'|'SUCCEEDED'|'FAILED',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type jobQueue: string
    :param jobQueue: The name or full Amazon Resource Name (ARN) of the job queue with which to list jobs.

    :type arrayJobId: string
    :param arrayJobId: The job ID for an array job. Specifying an array job ID with this parameter lists all child jobs from within the specified array.

    :type multiNodeJobId: string
    :param multiNodeJobId: The job ID for a multi-node parallel job. Specifying a multi-node parallel job ID with this parameter lists all nodes that are associated with the specified job.

    :type jobStatus: string
    :param jobStatus: The job status with which to filter jobs in the specified queue. If you do not specify a status, only RUNNING jobs are returned.

    :type maxResults: integer
    :param maxResults: The maximum number of results returned by ListJobs in paginated output. When this parameter is used, ListJobs only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListJobs request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListJobs returns up to 100 results and a nextToken value if applicable.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListJobs request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            

    :rtype: dict
    :return: {
        'jobSummaryList': [
            {
                'jobId': 'string',
                'jobName': 'string',
                'createdAt': 123,
                'status': 'SUBMITTED'|'PENDING'|'RUNNABLE'|'STARTING'|'RUNNING'|'SUCCEEDED'|'FAILED',
                'statusReason': 'string',
                'startedAt': 123,
                'stoppedAt': 123,
                'container': {
                    'exitCode': 123,
                    'reason': 'string'
                },
                'arrayProperties': {
                    'size': 123,
                    'index': 123
                },
                'nodeProperties': {
                    'isMainNode': True|False,
                    'numNodes': 123,
                    'nodeIndex': 123
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    jobQueue (string) -- The name or full Amazon Resource Name (ARN) of the job queue with which to list jobs.
    arrayJobId (string) -- The job ID for an array job. Specifying an array job ID with this parameter lists all child jobs from within the specified array.
    multiNodeJobId (string) -- The job ID for a multi-node parallel job. Specifying a multi-node parallel job ID with this parameter lists all nodes that are associated with the specified job.
    jobStatus (string) -- The job status with which to filter jobs in the specified queue. If you do not specify a status, only RUNNING jobs are returned.
    maxResults (integer) -- The maximum number of results returned by ListJobs in paginated output. When this parameter is used, ListJobs only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListJobs request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListJobs returns up to 100 results and a nextToken value if applicable.
    nextToken (string) -- The nextToken value returned from a previous paginated ListJobs request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return.
    
    Note
    This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
    
    
    
    """
    pass

def register_job_definition(jobDefinitionName=None, type=None, parameters=None, containerProperties=None, nodeProperties=None, retryStrategy=None, timeout=None):
    """
    Registers an AWS Batch job definition.
    See also: AWS API Documentation
    
    Examples
    This example registers a job definition for a simple container job.
    Expected Output:
    
    :example: response = client.register_job_definition(
        jobDefinitionName='string',
        type='container'|'multinode',
        parameters={
            'string': 'string'
        },
        containerProperties={
            'image': 'string',
            'vcpus': 123,
            'memory': 123,
            'command': [
                'string',
            ],
            'jobRoleArn': 'string',
            'volumes': [
                {
                    'host': {
                        'sourcePath': 'string'
                    },
                    'name': 'string'
                },
            ],
            'environment': [
                {
                    'name': 'string',
                    'value': 'string'
                },
            ],
            'mountPoints': [
                {
                    'containerPath': 'string',
                    'readOnly': True|False,
                    'sourceVolume': 'string'
                },
            ],
            'readonlyRootFilesystem': True|False,
            'privileged': True|False,
            'ulimits': [
                {
                    'hardLimit': 123,
                    'name': 'string',
                    'softLimit': 123
                },
            ],
            'user': 'string',
            'instanceType': 'string'
        },
        nodeProperties={
            'numNodes': 123,
            'mainNode': 123,
            'nodeRangeProperties': [
                {
                    'targetNodes': 'string',
                    'container': {
                        'image': 'string',
                        'vcpus': 123,
                        'memory': 123,
                        'command': [
                            'string',
                        ],
                        'jobRoleArn': 'string',
                        'volumes': [
                            {
                                'host': {
                                    'sourcePath': 'string'
                                },
                                'name': 'string'
                            },
                        ],
                        'environment': [
                            {
                                'name': 'string',
                                'value': 'string'
                            },
                        ],
                        'mountPoints': [
                            {
                                'containerPath': 'string',
                                'readOnly': True|False,
                                'sourceVolume': 'string'
                            },
                        ],
                        'readonlyRootFilesystem': True|False,
                        'privileged': True|False,
                        'ulimits': [
                            {
                                'hardLimit': 123,
                                'name': 'string',
                                'softLimit': 123
                            },
                        ],
                        'user': 'string',
                        'instanceType': 'string'
                    }
                },
            ]
        },
        retryStrategy={
            'attempts': 123
        },
        timeout={
            'attemptDurationSeconds': 123
        }
    )
    
    
    :type jobDefinitionName: string
    :param jobDefinitionName: [REQUIRED]
            The name of the job definition to register. Up to 128 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.
            

    :type type: string
    :param type: [REQUIRED]
            The type of job definition.
            

    :type parameters: dict
    :param parameters: Default parameter substitution placeholders to set in the job definition. Parameters are specified as a key-value pair mapping. Parameters in a SubmitJob request override any corresponding parameter defaults from the job definition.
            (string) --
            (string) --
            

    :type containerProperties: dict
    :param containerProperties: An object with various properties specific to single-node container-based jobs. If the job definition's type parameter is container , then you must specify either containerProperties or nodeProperties .
            image (string) --The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with `` repository-url /image :tag `` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to Image in the Create a container section of the Docker Remote API and the IMAGE parameter of docker run .
            Images in Amazon ECR repositories use the full registry and repository URI (for example, 012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name> ).
            Images in official repositories on Docker Hub use a single name (for example, ubuntu or mongo ).
            Images in other repositories on Docker Hub are qualified with an organization name (for example, amazon/amazon-ecs-agent ).
            Images in other online repositories are qualified further by a domain name (for example, quay.io/assemblyline/ubuntu ).
            vcpus (integer) --The number of vCPUs reserved for the container. This parameter maps to CpuShares in the Create a container section of the Docker Remote API and the --cpu-shares option to docker run . Each vCPU is equivalent to 1,024 CPU shares. You must specify at least one vCPU.
            memory (integer) --The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. This parameter maps to Memory in the Create a container section of the Docker Remote API and the --memory option to docker run . You must specify at least 4 MiB of memory for a job.
            Note
            If you are trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see Memory Management in the AWS Batch User Guide .
            command (list) --The command that is passed to the container. This parameter maps to Cmd in the Create a container section of the Docker Remote API and the COMMAND parameter to docker run . For more information, see https://docs.docker.com/engine/reference/builder/#cmd .
            (string) --
            jobRoleArn (string) --The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS permissions.
            volumes (list) --A list of data volumes used in a job.
            (dict) --A data volume used in a job's container properties.
            host (dict) --The contents of the host parameter determine whether your data volume persists on the host container instance and where it is stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data is not guaranteed to persist after the containers associated with it stop running.
            sourcePath (string) --The path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If the host parameter contains a sourcePath file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the sourcePath value does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.
            name (string) --The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the sourceVolume parameter of container definition mountPoints .
            
            environment (list) --The environment variables to pass to a container. This parameter maps to Env in the Create a container section of the Docker Remote API and the --env option to docker run .
            Warning
            We do not recommend using plaintext environment variables for sensitive information, such as credential data.
            Note
            Environment variables must not start with AWS_BATCH ; this naming convention is reserved for variables that are set by the AWS Batch service.
            (dict) --A key-value pair object.
            name (string) --The name of the key-value pair. For environment variables, this is the name of the environment variable.
            value (string) --The value of the key-value pair. For environment variables, this is the value of the environment variable.
            
            mountPoints (list) --The mount points for data volumes in your container. This parameter maps to Volumes in the Create a container section of the Docker Remote API and the --volume option to docker run .
            (dict) --Details on a Docker volume mount point that is used in a job's container properties.
            containerPath (string) --The path on the container at which to mount the host volume.
            readOnly (boolean) --If this value is true , the container has read-only access to the volume; otherwise, the container can write to the volume. The default value is false .
            sourceVolume (string) --The name of the volume to mount.
            
            readonlyRootFilesystem (boolean) --When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ReadonlyRootfs in the Create a container section of the Docker Remote API and the --read-only option to docker run .
            privileged (boolean) --When this parameter is true, the container is given elevated privileges on the host container instance (similar to the root user). This parameter maps to Privileged in the Create a container section of the Docker Remote API and the --privileged option to docker run .
            ulimits (list) --A list of ulimits to set in the container. This parameter maps to Ulimits in the Create a container section of the Docker Remote API and the --ulimit option to docker run .
            (dict) --The ulimit settings to pass to the container.
            hardLimit (integer) -- [REQUIRED]The hard limit for the ulimit type.
            name (string) -- [REQUIRED]The type of the ulimit .
            softLimit (integer) -- [REQUIRED]The soft limit for the ulimit type.
            
            user (string) --The user name to use inside the container. This parameter maps to User in the Create a container section of the Docker Remote API and the --user option to docker run .
            instanceType (string) --The instance type to use for a multi-node parallel job. Currently all node groups in a multi-node parallel job must use the same instance type. This parameter is not valid for single-node container jobs.
            

    :type nodeProperties: dict
    :param nodeProperties: An object with various properties specific to multi-node parallel jobs. If you specify node properties for a job, it becomes a multi-node parallel job. For more information, see Multi-node Parallel Jobs in the AWS Batch User Guide . If the job definition's type parameter is container , then you must specify either containerProperties or nodeProperties .
            numNodes (integer) -- [REQUIRED]The number of nodes associated with a multi-node parallel job.
            mainNode (integer) -- [REQUIRED]Specifies the node index for the main node of a multi-node parallel job.
            nodeRangeProperties (list) -- [REQUIRED]A list of node ranges and their properties associated with a multi-node parallel job.
            (dict) --An object representing the properties of the node range for a multi-node parallel job.
            targetNodes (string) -- [REQUIRED]The range of nodes, using node index values. A range of 0:3 indicates nodes with index values of 0 through 3 . If the starting range value is omitted (:n ), then 0 is used to start the range. If the ending range value is omitted (n: ), then the highest possible node index is used to end the range. Your accumulative node ranges must account for all nodes (0:n). You may nest node ranges, for example 0:10 and 4:5, in which case the 4:5 range properties override the 0:10 properties.
            container (dict) --The container details for the node range.
            image (string) --The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with `` repository-url /image :tag `` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to Image in the Create a container section of the Docker Remote API and the IMAGE parameter of docker run .
            Images in Amazon ECR repositories use the full registry and repository URI (for example, 012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name> ).
            Images in official repositories on Docker Hub use a single name (for example, ubuntu or mongo ).
            Images in other repositories on Docker Hub are qualified with an organization name (for example, amazon/amazon-ecs-agent ).
            Images in other online repositories are qualified further by a domain name (for example, quay.io/assemblyline/ubuntu ).
            vcpus (integer) --The number of vCPUs reserved for the container. This parameter maps to CpuShares in the Create a container section of the Docker Remote API and the --cpu-shares option to docker run . Each vCPU is equivalent to 1,024 CPU shares. You must specify at least one vCPU.
            memory (integer) --The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. This parameter maps to Memory in the Create a container section of the Docker Remote API and the --memory option to docker run . You must specify at least 4 MiB of memory for a job.
            Note
            If you are trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see Memory Management in the AWS Batch User Guide .
            command (list) --The command that is passed to the container. This parameter maps to Cmd in the Create a container section of the Docker Remote API and the COMMAND parameter to docker run . For more information, see https://docs.docker.com/engine/reference/builder/#cmd .
            (string) --
            jobRoleArn (string) --The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS permissions.
            volumes (list) --A list of data volumes used in a job.
            (dict) --A data volume used in a job's container properties.
            host (dict) --The contents of the host parameter determine whether your data volume persists on the host container instance and where it is stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data is not guaranteed to persist after the containers associated with it stop running.
            sourcePath (string) --The path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If the host parameter contains a sourcePath file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the sourcePath value does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.
            name (string) --The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the sourceVolume parameter of container definition mountPoints .
            
            environment (list) --The environment variables to pass to a container. This parameter maps to Env in the Create a container section of the Docker Remote API and the --env option to docker run .
            Warning
            We do not recommend using plaintext environment variables for sensitive information, such as credential data.
            Note
            Environment variables must not start with AWS_BATCH ; this naming convention is reserved for variables that are set by the AWS Batch service.
            (dict) --A key-value pair object.
            name (string) --The name of the key-value pair. For environment variables, this is the name of the environment variable.
            value (string) --The value of the key-value pair. For environment variables, this is the value of the environment variable.
            
            mountPoints (list) --The mount points for data volumes in your container. This parameter maps to Volumes in the Create a container section of the Docker Remote API and the --volume option to docker run .
            (dict) --Details on a Docker volume mount point that is used in a job's container properties.
            containerPath (string) --The path on the container at which to mount the host volume.
            readOnly (boolean) --If this value is true , the container has read-only access to the volume; otherwise, the container can write to the volume. The default value is false .
            sourceVolume (string) --The name of the volume to mount.
            
            readonlyRootFilesystem (boolean) --When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ReadonlyRootfs in the Create a container section of the Docker Remote API and the --read-only option to docker run .
            privileged (boolean) --When this parameter is true, the container is given elevated privileges on the host container instance (similar to the root user). This parameter maps to Privileged in the Create a container section of the Docker Remote API and the --privileged option to docker run .
            ulimits (list) --A list of ulimits to set in the container. This parameter maps to Ulimits in the Create a container section of the Docker Remote API and the --ulimit option to docker run .
            (dict) --The ulimit settings to pass to the container.
            hardLimit (integer) -- [REQUIRED]The hard limit for the ulimit type.
            name (string) -- [REQUIRED]The type of the ulimit .
            softLimit (integer) -- [REQUIRED]The soft limit for the ulimit type.
            
            user (string) --The user name to use inside the container. This parameter maps to User in the Create a container section of the Docker Remote API and the --user option to docker run .
            instanceType (string) --The instance type to use for a multi-node parallel job. Currently all node groups in a multi-node parallel job must use the same instance type. This parameter is not valid for single-node container jobs.
            
            
            

    :type retryStrategy: dict
    :param retryStrategy: The retry strategy to use for failed jobs that are submitted with this job definition. Any retry strategy that is specified during a SubmitJob operation overrides the retry strategy defined here. If a job is terminated due to a timeout, it is not retried.
            attempts (integer) --The number of times to move a job to the RUNNABLE status. You may specify between 1 and 10 attempts. If the value of attempts is greater than one, the job is retried on failure the same number of attempts as the value.
            

    :type timeout: dict
    :param timeout: The timeout configuration for jobs that are submitted with this job definition, after which AWS Batch terminates your jobs if they have not finished. If a job is terminated due to a timeout, it is not retried. The minimum value for the timeout is 60 seconds. Any timeout configuration that is specified during a SubmitJob operation overrides the timeout configuration defined here. For more information, see Job Timeouts in the Amazon Elastic Container Service Developer Guide .
            attemptDurationSeconds (integer) --The time duration in seconds (measured from the job attempt's startedAt timestamp) after which AWS Batch terminates your jobs if they have not finished.
            

    :rtype: dict
    :return: {
        'jobDefinitionName': 'string',
        'jobDefinitionArn': 'string',
        'revision': 123
    }
    
    
    """
    pass

def submit_job(jobName=None, jobQueue=None, arrayProperties=None, dependsOn=None, jobDefinition=None, parameters=None, containerOverrides=None, nodeOverrides=None, retryStrategy=None, timeout=None):
    """
    Submits an AWS Batch job from a job definition. Parameters specified during  SubmitJob override parameters defined in the job definition.
    See also: AWS API Documentation
    
    Examples
    This example submits a simple container job called example to the HighPriority job queue.
    Expected Output:
    
    :example: response = client.submit_job(
        jobName='string',
        jobQueue='string',
        arrayProperties={
            'size': 123
        },
        dependsOn=[
            {
                'jobId': 'string',
                'type': 'N_TO_N'|'SEQUENTIAL'
            },
        ],
        jobDefinition='string',
        parameters={
            'string': 'string'
        },
        containerOverrides={
            'vcpus': 123,
            'memory': 123,
            'command': [
                'string',
            ],
            'instanceType': 'string',
            'environment': [
                {
                    'name': 'string',
                    'value': 'string'
                },
            ]
        },
        nodeOverrides={
            'nodePropertyOverrides': [
                {
                    'targetNodes': 'string',
                    'containerOverrides': {
                        'vcpus': 123,
                        'memory': 123,
                        'command': [
                            'string',
                        ],
                        'instanceType': 'string',
                        'environment': [
                            {
                                'name': 'string',
                                'value': 'string'
                            },
                        ]
                    }
                },
            ]
        },
        retryStrategy={
            'attempts': 123
        },
        timeout={
            'attemptDurationSeconds': 123
        }
    )
    
    
    :type jobName: string
    :param jobName: [REQUIRED]
            The name of the job. The first character must be alphanumeric, and up to 128 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.
            

    :type jobQueue: string
    :param jobQueue: [REQUIRED]
            The job queue into which the job is submitted. You can specify either the name or the Amazon Resource Name (ARN) of the queue.
            

    :type arrayProperties: dict
    :param arrayProperties: The array properties for the submitted job, such as the size of the array. The array size can be between 2 and 10,000. If you specify array properties for a job, it becomes an array job. For more information, see Array Jobs in the AWS Batch User Guide .
            size (integer) --The size of the array job.
            

    :type dependsOn: list
    :param dependsOn: A list of dependencies for the job. A job can depend upon a maximum of 20 jobs. You can specify a SEQUENTIAL type dependency without specifying a job ID for array jobs so that each child array job completes sequentially, starting at index 0. You can also specify an N_TO_N type dependency with a job ID for array jobs. In that case, each index child of this job must wait for the corresponding index child of each dependency to complete before it can begin.
            (dict) --An object representing an AWS Batch job dependency.
            jobId (string) --The job ID of the AWS Batch job associated with this dependency.
            type (string) --The type of the job dependency.
            
            

    :type jobDefinition: string
    :param jobDefinition: [REQUIRED]
            The job definition used by this job. This value can be either a name:revision or the Amazon Resource Name (ARN) for the job definition.
            

    :type parameters: dict
    :param parameters: Additional parameters passed to the job that replace parameter substitution placeholders that are set in the job definition. Parameters are specified as a key and value pair mapping. Parameters in a SubmitJob request override any corresponding parameter defaults from the job definition.
            (string) --
            (string) --
            

    :type containerOverrides: dict
    :param containerOverrides: A list of container overrides in JSON format that specify the name of a container in the specified job definition and the overrides it should receive. You can override the default command for a container (that is specified in the job definition or the Docker image) with a command override. You can also override existing environment variables (that are specified in the job definition or Docker image) on a container or add new environment variables to it with an environment override.
            vcpus (integer) --The number of vCPUs to reserve for the container. This value overrides the value set in the job definition.
            memory (integer) --The number of MiB of memory reserved for the job. This value overrides the value set in the job definition.
            command (list) --The command to send to the container that overrides the default command from the Docker image or the job definition.
            (string) --
            instanceType (string) --The instance type to use for a multi-node parallel job. This parameter is not valid for single-node container jobs.
            environment (list) --The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the job definition.
            Note
            Environment variables must not start with AWS_BATCH ; this naming convention is reserved for variables that are set by the AWS Batch service.
            (dict) --A key-value pair object.
            name (string) --The name of the key-value pair. For environment variables, this is the name of the environment variable.
            value (string) --The value of the key-value pair. For environment variables, this is the value of the environment variable.
            
            

    :type nodeOverrides: dict
    :param nodeOverrides: A list of node overrides in JSON format that specify the node range to target and the container overrides for that node range.
            nodePropertyOverrides (list) --The node property overrides for the job.
            (dict) --Object representing any node overrides to a job definition that is used in a SubmitJob API operation.
            targetNodes (string) -- [REQUIRED]The range of nodes, using node index values, with which to override. A range of 0:3 indicates nodes with index values of 0 through 3 . If the starting range value is omitted (:n ), then 0 is used to start the range. If the ending range value is omitted (n: ), then the highest possible node index is used to end the range.
            containerOverrides (dict) --The overrides that should be sent to a node range.
            vcpus (integer) --The number of vCPUs to reserve for the container. This value overrides the value set in the job definition.
            memory (integer) --The number of MiB of memory reserved for the job. This value overrides the value set in the job definition.
            command (list) --The command to send to the container that overrides the default command from the Docker image or the job definition.
            (string) --
            instanceType (string) --The instance type to use for a multi-node parallel job. This parameter is not valid for single-node container jobs.
            environment (list) --The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the job definition.
            Note
            Environment variables must not start with AWS_BATCH ; this naming convention is reserved for variables that are set by the AWS Batch service.
            (dict) --A key-value pair object.
            name (string) --The name of the key-value pair. For environment variables, this is the name of the environment variable.
            value (string) --The value of the key-value pair. For environment variables, this is the value of the environment variable.
            
            
            
            

    :type retryStrategy: dict
    :param retryStrategy: The retry strategy to use for failed jobs from this SubmitJob operation. When a retry strategy is specified here, it overrides the retry strategy defined in the job definition.
            attempts (integer) --The number of times to move a job to the RUNNABLE status. You may specify between 1 and 10 attempts. If the value of attempts is greater than one, the job is retried on failure the same number of attempts as the value.
            

    :type timeout: dict
    :param timeout: The timeout configuration for this SubmitJob operation. You can specify a timeout duration after which AWS Batch terminates your jobs if they have not finished. If a job is terminated due to a timeout, it is not retried. The minimum value for the timeout is 60 seconds. This configuration overrides any timeout configuration specified in the job definition. For array jobs, child jobs have the same timeout configuration as the parent job. For more information, see Job Timeouts in the Amazon Elastic Container Service Developer Guide .
            attemptDurationSeconds (integer) --The time duration in seconds (measured from the job attempt's startedAt timestamp) after which AWS Batch terminates your jobs if they have not finished.
            

    :rtype: dict
    :return: {
        'jobName': 'string',
        'jobId': 'string'
    }
    
    
    """
    pass

def terminate_job(jobId=None, reason=None):
    """
    Terminates a job in a job queue. Jobs that are in the STARTING or RUNNING state are terminated, which causes them to transition to FAILED . Jobs that have not progressed to the STARTING state are cancelled.
    See also: AWS API Documentation
    
    Examples
    This example terminates a job with the specified job ID.
    Expected Output:
    
    :example: response = client.terminate_job(
        jobId='string',
        reason='string'
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]
            The AWS Batch job ID of the job to terminate.
            

    :type reason: string
    :param reason: [REQUIRED]
            A message to attach to the job that explains the reason for canceling it. This message is returned by future DescribeJobs operations on the job. This message is also recorded in the AWS Batch activity logs.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_compute_environment(computeEnvironment=None, state=None, computeResources=None, serviceRole=None):
    """
    Updates an AWS Batch compute environment.
    See also: AWS API Documentation
    
    Examples
    This example disables the P2OnDemand compute environment so it can be deleted.
    Expected Output:
    
    :example: response = client.update_compute_environment(
        computeEnvironment='string',
        state='ENABLED'|'DISABLED',
        computeResources={
            'minvCpus': 123,
            'maxvCpus': 123,
            'desiredvCpus': 123
        },
        serviceRole='string'
    )
    
    
    :type computeEnvironment: string
    :param computeEnvironment: [REQUIRED]
            The name or full Amazon Resource Name (ARN) of the compute environment to update.
            

    :type state: string
    :param state: The state of the compute environment. Compute environments in the ENABLED state can accept jobs from a queue and scale in or out automatically based on the workload demand of its associated queues.

    :type computeResources: dict
    :param computeResources: Details of the compute resources managed by the compute environment. Required for a managed compute environment.
            minvCpus (integer) --The minimum number of EC2 vCPUs that an environment should maintain.
            maxvCpus (integer) --The maximum number of EC2 vCPUs that an environment can reach.
            desiredvCpus (integer) --The desired number of EC2 vCPUS in the compute environment.
            

    :type serviceRole: string
    :param serviceRole: The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.
            If your specified role has a path other than / , then you must either specify the full role ARN (this is recommended) or prefix the role name with the path.
            Note
            Depending on how you created your AWS Batch service role, its ARN may contain the service-role path prefix. When you only specify the name of the service role, AWS Batch assumes that your ARN does not use the service-role path prefix. Because of this, we recommend that you specify the full ARN of your service role when you create compute environments.
            

    :rtype: dict
    :return: {
        'computeEnvironmentName': 'string',
        'computeEnvironmentArn': 'string'
    }
    
    
    """
    pass

def update_job_queue(jobQueue=None, state=None, priority=None, computeEnvironmentOrder=None):
    """
    Updates a job queue.
    See also: AWS API Documentation
    
    Examples
    This example disables a job queue so that it can be deleted.
    Expected Output:
    
    :example: response = client.update_job_queue(
        jobQueue='string',
        state='ENABLED'|'DISABLED',
        priority=123,
        computeEnvironmentOrder=[
            {
                'order': 123,
                'computeEnvironment': 'string'
            },
        ]
    )
    
    
    :type jobQueue: string
    :param jobQueue: [REQUIRED]
            The name or the Amazon Resource Name (ARN) of the job queue.
            

    :type state: string
    :param state: Describes the queue's ability to accept new jobs.

    :type priority: integer
    :param priority: The priority of the job queue. Job queues with a higher priority (or a higher integer value for the priority parameter) are evaluated first when associated with the same compute environment. Priority is determined in descending order, for example, a job queue with a priority value of 10 is given scheduling preference over a job queue with a priority value of 1 .

    :type computeEnvironmentOrder: list
    :param computeEnvironmentOrder: Details the set of compute environments mapped to a job queue and their order relative to each other. This is one of the parameters used by the job scheduler to determine which compute environment should execute a given job.
            (dict) --The order in which compute environments are tried for job placement within a queue. Compute environments are tried in ascending order. For example, if two compute environments are associated with a job queue, the compute environment with a lower order integer value is tried for job placement first.
            order (integer) -- [REQUIRED]The order of the compute environment.
            computeEnvironment (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the compute environment.
            
            

    :rtype: dict
    :return: {
        'jobQueueName': 'string',
        'jobQueueArn': 'string'
    }
    
    
    """
    pass

