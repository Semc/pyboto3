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

def create_lifecycle_policy(ExecutionRoleArn=None, Description=None, State=None, PolicyDetails=None):
    """
    Creates a policy to manage the lifecycle of the specified AWS resources. You can create up to 100 lifecycle policies.
    See also: AWS API Documentation
    
    
    :example: response = client.create_lifecycle_policy(
        ExecutionRoleArn='string',
        Description='string',
        State='ENABLED'|'DISABLED',
        PolicyDetails={
            'ResourceTypes': [
                'VOLUME',
            ],
            'TargetTags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'Schedules': [
                {
                    'Name': 'string',
                    'CopyTags': True|False,
                    'TagsToAdd': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'CreateRule': {
                        'Interval': 123,
                        'IntervalUnit': 'HOURS',
                        'Times': [
                            'string',
                        ]
                    },
                    'RetainRule': {
                        'Count': 123
                    }
                },
            ]
        }
    )
    
    
    :type ExecutionRoleArn: string
    :param ExecutionRoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM role used to run the operations specified by the lifecycle policy.
            

    :type Description: string
    :param Description: [REQUIRED]
            A description of the lifecycle policy. The characters ^[0-9A-Za-z _-]+$ are supported.
            

    :type State: string
    :param State: [REQUIRED]
            The desired activation state of the lifecycle policy after creation.
            

    :type PolicyDetails: dict
    :param PolicyDetails: [REQUIRED]
            The configuration details of the lifecycle policy.
            Target tags cannot be re-used across lifecycle policies.
            ResourceTypes (list) --The resource type.
            (string) --
            TargetTags (list) --The single tag that identifies targeted resources for this policy.
            (dict) --Specifies a tag for a resource.
            Key (string) -- [REQUIRED]The tag key.
            Value (string) -- [REQUIRED]The tag value.
            
            Schedules (list) --The schedule of policy-defined actions.
            (dict) --Specifies a schedule.
            Name (string) --The name of the schedule.
            CopyTags (boolean) --
            TagsToAdd (list) --The tags to apply to policy-created resources. These user-defined tags are in addition to the AWS-added lifecycle tags.
            (dict) --Specifies a tag for a resource.
            Key (string) -- [REQUIRED]The tag key.
            Value (string) -- [REQUIRED]The tag value.
            
            CreateRule (dict) --The create rule.
            Interval (integer) -- [REQUIRED]The interval. The supported values are 12 and 24.
            IntervalUnit (string) -- [REQUIRED]The interval unit.
            Times (list) --The time, in UTC, to start the operation.
            The operation occurs within a one-hour window following the specified time.
            (string) --
            
            RetainRule (dict) --The retain rule.
            Count (integer) -- [REQUIRED]The number of snapshots to keep for each volume, up to a maximum of 1000.
            
            
            

    :rtype: dict
    :return: {
        'PolicyId': 'string'
    }
    
    
    """
    pass

def delete_lifecycle_policy(PolicyId=None):
    """
    Deletes the specified lifecycle policy and halts the automated operations that the policy specified.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_lifecycle_policy(
        PolicyId='string'
    )
    
    
    :type PolicyId: string
    :param PolicyId: [REQUIRED]
            The identifier of the lifecycle policy.
            

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

def get_lifecycle_policies(PolicyIds=None, State=None, ResourceTypes=None, TargetTags=None, TagsToAdd=None):
    """
    Gets summary information about all or the specified data lifecycle policies.
    To get complete information about a policy, use  GetLifecyclePolicy .
    See also: AWS API Documentation
    
    
    :example: response = client.get_lifecycle_policies(
        PolicyIds=[
            'string',
        ],
        State='ENABLED'|'DISABLED'|'ERROR',
        ResourceTypes=[
            'VOLUME',
        ],
        TargetTags=[
            'string',
        ],
        TagsToAdd=[
            'string',
        ]
    )
    
    
    :type PolicyIds: list
    :param PolicyIds: The identifiers of the data lifecycle policies.
            (string) --
            

    :type State: string
    :param State: The activation state.

    :type ResourceTypes: list
    :param ResourceTypes: The resource type.
            (string) --
            

    :type TargetTags: list
    :param TargetTags: The target tag for a policy.
            Tags are strings in the format key=value .
            (string) --
            

    :type TagsToAdd: list
    :param TagsToAdd: The tags to add to objects created by the policy.
            Tags are strings in the format key=value .
            These user-defined tags are added in addition to the AWS-added lifecycle tags.
            (string) --
            

    :rtype: dict
    :return: {
        'Policies': [
            {
                'PolicyId': 'string',
                'Description': 'string',
                'State': 'ENABLED'|'DISABLED'|'ERROR'
            },
        ]
    }
    
    
    """
    pass

def get_lifecycle_policy(PolicyId=None):
    """
    Gets detailed information about the specified lifecycle policy.
    See also: AWS API Documentation
    
    
    :example: response = client.get_lifecycle_policy(
        PolicyId='string'
    )
    
    
    :type PolicyId: string
    :param PolicyId: [REQUIRED]
            The identifier of the lifecycle policy.
            

    :rtype: dict
    :return: {
        'Policy': {
            'PolicyId': 'string',
            'Description': 'string',
            'State': 'ENABLED'|'DISABLED'|'ERROR',
            'ExecutionRoleArn': 'string',
            'DateCreated': datetime(2015, 1, 1),
            'DateModified': datetime(2015, 1, 1),
            'PolicyDetails': {
                'ResourceTypes': [
                    'VOLUME',
                ],
                'TargetTags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'Schedules': [
                    {
                        'Name': 'string',
                        'CopyTags': True|False,
                        'TagsToAdd': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'CreateRule': {
                            'Interval': 123,
                            'IntervalUnit': 'HOURS',
                            'Times': [
                                'string',
                            ]
                        },
                        'RetainRule': {
                            'Count': 123
                        }
                    },
                ]
            }
        }
    }
    
    
    :returns: 
    (string) --
    
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

def update_lifecycle_policy(PolicyId=None, ExecutionRoleArn=None, State=None, Description=None, PolicyDetails=None):
    """
    Updates the specified lifecycle policy.
    See also: AWS API Documentation
    
    
    :example: response = client.update_lifecycle_policy(
        PolicyId='string',
        ExecutionRoleArn='string',
        State='ENABLED'|'DISABLED',
        Description='string',
        PolicyDetails={
            'ResourceTypes': [
                'VOLUME',
            ],
            'TargetTags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'Schedules': [
                {
                    'Name': 'string',
                    'CopyTags': True|False,
                    'TagsToAdd': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'CreateRule': {
                        'Interval': 123,
                        'IntervalUnit': 'HOURS',
                        'Times': [
                            'string',
                        ]
                    },
                    'RetainRule': {
                        'Count': 123
                    }
                },
            ]
        }
    )
    
    
    :type PolicyId: string
    :param PolicyId: [REQUIRED]
            The identifier of the lifecycle policy.
            

    :type ExecutionRoleArn: string
    :param ExecutionRoleArn: The Amazon Resource Name (ARN) of the IAM role used to run the operations specified by the lifecycle policy.

    :type State: string
    :param State: The desired activation state of the lifecycle policy after creation.

    :type Description: string
    :param Description: A description of the lifecycle policy.

    :type PolicyDetails: dict
    :param PolicyDetails: The configuration of the lifecycle policy.
            Target tags cannot be re-used across policies.
            ResourceTypes (list) --The resource type.
            (string) --
            TargetTags (list) --The single tag that identifies targeted resources for this policy.
            (dict) --Specifies a tag for a resource.
            Key (string) -- [REQUIRED]The tag key.
            Value (string) -- [REQUIRED]The tag value.
            
            Schedules (list) --The schedule of policy-defined actions.
            (dict) --Specifies a schedule.
            Name (string) --The name of the schedule.
            CopyTags (boolean) --
            TagsToAdd (list) --The tags to apply to policy-created resources. These user-defined tags are in addition to the AWS-added lifecycle tags.
            (dict) --Specifies a tag for a resource.
            Key (string) -- [REQUIRED]The tag key.
            Value (string) -- [REQUIRED]The tag value.
            
            CreateRule (dict) --The create rule.
            Interval (integer) -- [REQUIRED]The interval. The supported values are 12 and 24.
            IntervalUnit (string) -- [REQUIRED]The interval unit.
            Times (list) --The time, in UTC, to start the operation.
            The operation occurs within a one-hour window following the specified time.
            (string) --
            
            RetainRule (dict) --The retain rule.
            Count (integer) -- [REQUIRED]The number of snapshots to keep for each volume, up to a maximum of 1000.
            
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

