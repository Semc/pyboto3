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

def add_layer_version_permission(LayerName=None, VersionNumber=None, StatementId=None, Action=None, Principal=None, OrganizationId=None, RevisionId=None):
    """
    Adds permissions to the resource-based policy of a version of a function layer. Use this action to grant layer usage permission to other accounts. You can grant permission to a single account, all AWS accounts, or all accounts in an organization.
    To revoke permission, call  RemoveLayerVersionPermission with the statement ID that you specified when you added it.
    See also: AWS API Documentation
    
    
    :example: response = client.add_layer_version_permission(
        LayerName='string',
        VersionNumber=123,
        StatementId='string',
        Action='string',
        Principal='string',
        OrganizationId='string',
        RevisionId='string'
    )
    
    
    :type LayerName: string
    :param LayerName: [REQUIRED]
            The name of the layer.
            

    :type VersionNumber: integer
    :param VersionNumber: [REQUIRED]
            The version number.
            

    :type StatementId: string
    :param StatementId: [REQUIRED]
            An identifier that distinguishes the policy from others on the same layer version.
            

    :type Action: string
    :param Action: [REQUIRED]
            The API action that grants access to the layer. For example, lambda:GetLayerVersion .
            

    :type Principal: string
    :param Principal: [REQUIRED]
            An account ID, or * to grant permission to all AWS accounts.
            

    :type OrganizationId: string
    :param OrganizationId: With the principal set to * , grant permission to all accounts in the specified organization.

    :type RevisionId: string
    :param RevisionId: Only update the policy if the revision ID matches the ID specified. Use this option to avoid modifying a policy that has changed since you last read it.

    :rtype: dict
    :return: {
        'Statement': 'string',
        'RevisionId': 'string'
    }
    
    
    """
    pass

def add_permission(FunctionName=None, StatementId=None, Action=None, Principal=None, SourceArn=None, SourceAccount=None, EventSourceToken=None, Qualifier=None, RevisionId=None):
    """
    Adds a permission to the resource policy associated with the specified AWS Lambda function. You use resource policies to grant permissions to event sources that use the push model. In a push model, event sources (such as Amazon S3 and custom applications) invoke your Lambda function. Each permission you add to the resource policy allows an event source permission to invoke the Lambda function.
    Permissions apply to the Amazon Resource Name (ARN) used to invoke the function, which can be unqualified (the unpublished version of the function), or include a version or alias. If a client uses a version or alias to invoke a function, use the Qualifier parameter to apply permissions to that ARN. For more information about versioning, see AWS Lambda Function Versioning and Aliases .
    This operation requires permission for the lambda:AddPermission action.
    See also: AWS API Documentation
    
    Examples
    This example adds a permission for an S3 bucket to invoke a Lambda function.
    Expected Output:
    
    :example: response = client.add_permission(
        FunctionName='string',
        StatementId='string',
        Action='string',
        Principal='string',
        SourceArn='string',
        SourceAccount='string',
        EventSourceToken='string',
        Qualifier='string',
        RevisionId='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]
            The name of the Lambda function.
            Name formats
            Function name - MyFunction .
            Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
            Partial ARN - 123456789012:function:MyFunction .
            The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
            

    :type StatementId: string
    :param StatementId: [REQUIRED]
            A unique statement identifier.
            

    :type Action: string
    :param Action: [REQUIRED]
            The AWS Lambda action you want to allow in this statement. Each Lambda action is a string starting with lambda: followed by the API name . For example, lambda:CreateFunction . You can use wildcard (lambda:* ) to grant permission for all AWS Lambda actions.
            

    :type Principal: string
    :param Principal: [REQUIRED]
            The principal who is getting this permission. The principal can be an AWS service (e.g. s3.amazonaws.com or sns.amazonaws.com ) for service triggers, or an account ID for cross-account access. If you specify a service as a principal, use the SourceArn parameter to limit who can invoke the function through that service.
            

    :type SourceArn: string
    :param SourceArn: The Amazon Resource Name of the invoker.
            Warning
            If you add a permission to a service principal without providing the source ARN, any AWS account that creates a mapping to your function ARN can invoke your Lambda function.
            

    :type SourceAccount: string
    :param SourceAccount: This parameter is used for S3 and SES. The AWS account ID (without a hyphen) of the source owner. For example, if the SourceArn identifies a bucket, then this is the bucket owner's account ID. You can use this additional condition to ensure the bucket you specify is owned by a specific account (it is possible the bucket owner deleted the bucket and some other AWS account created the bucket). You can also use this condition to specify all sources (that is, you don't specify the SourceArn ) owned by a specific account.

    :type EventSourceToken: string
    :param EventSourceToken: A unique token that must be supplied by the principal invoking the function. This is currently only used for Alexa Smart Home functions.

    :type Qualifier: string
    :param Qualifier: Specify a version or alias to add permissions to a published version of the function.

    :type RevisionId: string
    :param RevisionId: An optional value you can use to ensure you are updating the latest update of the function version or alias. If the RevisionID you pass doesn't match the latest RevisionId of the function or alias, it will fail with an error message, advising you to retrieve the latest function version or alias RevisionID using either GetFunction or GetAlias

    :rtype: dict
    :return: {
        'Statement': 'string'
    }
    
    
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

def create_alias(FunctionName=None, Name=None, FunctionVersion=None, Description=None, RoutingConfig=None):
    """
    Creates an alias that points to the specified Lambda function version. For more information, see Introduction to AWS Lambda Aliases .
    Alias names are unique for a given function. This requires permission for the lambda:CreateAlias action.
    See also: AWS API Documentation
    
    
    :example: response = client.create_alias(
        FunctionName='string',
        Name='string',
        FunctionVersion='string',
        Description='string',
        RoutingConfig={
            'AdditionalVersionWeights': {
                'string': 123.0
            }
        }
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]
            The name of the lambda function.
            Name formats
            Function name - MyFunction .
            Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
            Partial ARN - 123456789012:function:MyFunction .
            The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
            

    :type Name: string
    :param Name: [REQUIRED]
            Name for the alias you are creating.
            

    :type FunctionVersion: string
    :param FunctionVersion: [REQUIRED]
            Lambda function version for which you are creating the alias.
            

    :type Description: string
    :param Description: Description of the alias.

    :type RoutingConfig: dict
    :param RoutingConfig: Specifies an additional version your alias can point to, allowing you to dictate what percentage of traffic will invoke each version. For more information, see Traffic Shifting Using Aliases .
            AdditionalVersionWeights (dict) --The name of the second alias, and the percentage of traffic that is routed to it.
            (string) --
            (float) --
            
            

    :rtype: dict
    :return: {
        'AliasArn': 'string',
        'Name': 'string',
        'FunctionVersion': 'string',
        'Description': 'string',
        'RoutingConfig': {
            'AdditionalVersionWeights': {
                'string': 123.0
            }
        },
        'RevisionId': 'string'
    }
    
    
    :returns: 
    (string) --
    (float) --
    
    
    
    """
    pass

def create_event_source_mapping(EventSourceArn=None, FunctionName=None, Enabled=None, BatchSize=None, StartingPosition=None, StartingPositionTimestamp=None):
    """
    Creates a mapping between an event source and an AWS Lambda function. Lambda reads items from the event source and triggers the function.
    For details about each event source type, see the following topics.
    See also: AWS API Documentation
    
    
    :example: response = client.create_event_source_mapping(
        EventSourceArn='string',
        FunctionName='string',
        Enabled=True|False,
        BatchSize=123,
        StartingPosition='TRIM_HORIZON'|'LATEST'|'AT_TIMESTAMP',
        StartingPositionTimestamp=datetime(2015, 1, 1)
    )
    
    
    :type EventSourceArn: string
    :param EventSourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the event source.
            Amazon Kinesis - The ARN of the data stream or a stream consumer.
            Amazon DynamoDB Streams - The ARN of the stream.
            Amazon Simple Queue Service - The ARN of the queue.
            

    :type FunctionName: string
    :param FunctionName: [REQUIRED]
            The name of the Lambda function.
            Name formats
            Function name - MyFunction .
            Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
            Version or Alias ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD .
            Partial ARN - 123456789012:function:MyFunction .
            The length constraint applies only to the full ARN. If you specify only the function name, it's limited to 64 characters in length.
            

    :type Enabled: boolean
    :param Enabled: Disables the event source mapping to pause polling and invocation.

    :type BatchSize: integer
    :param BatchSize: The maximum number of items to retrieve in a single batch.
            Amazon Kinesis - Default 100. Max 10,000.
            Amazon DynamoDB Streams - Default 100. Max 1,000.
            Amazon Simple Queue Service - Default 10. Max 10.
            

    :type StartingPosition: string
    :param StartingPosition: The position in a stream from which to start reading. Required for Amazon Kinesis and Amazon DynamoDB Streams sources. AT_TIMESTAMP is only supported for Amazon Kinesis streams.

    :type StartingPositionTimestamp: datetime
    :param StartingPositionTimestamp: With StartingPosition set to AT_TIMESTAMP , the Unix time in seconds from which to start reading.

    :rtype: dict
    :return: {
        'UUID': 'string',
        'BatchSize': 123,
        'EventSourceArn': 'string',
        'FunctionArn': 'string',
        'LastModified': datetime(2015, 1, 1),
        'LastProcessingResult': 'string',
        'State': 'string',
        'StateTransitionReason': 'string'
    }
    
    
    :returns: 
    EventSourceArn (string) -- [REQUIRED]
    The Amazon Resource Name (ARN) of the event source.
    
    Amazon Kinesis - The ARN of the data stream or a stream consumer.
    Amazon DynamoDB Streams - The ARN of the stream.
    Amazon Simple Queue Service - The ARN of the queue.
    
    
    FunctionName (string) -- [REQUIRED]
    The name of the Lambda function.
    
    Name formats
    
    Function name - MyFunction .
    Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
    Version or Alias ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD .
    Partial ARN - 123456789012:function:MyFunction .
    
    The length constraint applies only to the full ARN. If you specify only the function name, it's limited to 64 characters in length.
    
    Enabled (boolean) -- Disables the event source mapping to pause polling and invocation.
    BatchSize (integer) -- The maximum number of items to retrieve in a single batch.
    
    Amazon Kinesis - Default 100. Max 10,000.
    Amazon DynamoDB Streams - Default 100. Max 1,000.
    Amazon Simple Queue Service - Default 10. Max 10.
    
    
    StartingPosition (string) -- The position in a stream from which to start reading. Required for Amazon Kinesis and Amazon DynamoDB Streams sources. AT_TIMESTAMP is only supported for Amazon Kinesis streams.
    StartingPositionTimestamp (datetime) -- With StartingPosition set to AT_TIMESTAMP , the Unix time in seconds from which to start reading.
    
    """
    pass

def create_function(FunctionName=None, Runtime=None, Role=None, Handler=None, Code=None, Description=None, Timeout=None, MemorySize=None, Publish=None, VpcConfig=None, DeadLetterConfig=None, Environment=None, KMSKeyArn=None, TracingConfig=None, Tags=None, Layers=None):
    """
    Creates a new Lambda function. The function configuration is created from the request parameters, and the code for the function is provided by a .zip file. The function name is case-sensitive.
    This operation requires permission for the lambda:CreateFunction action.
    See also: AWS API Documentation
    
    Examples
    This example creates a Lambda function.
    Expected Output:
    
    :example: response = client.create_function(
        FunctionName='string',
        Runtime='nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'java8'|'python2.7'|'python3.6'|'python3.7'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
        Role='string',
        Handler='string',
        Code={
            'ZipFile': b'bytes',
            'S3Bucket': 'string',
            'S3Key': 'string',
            'S3ObjectVersion': 'string'
        },
        Description='string',
        Timeout=123,
        MemorySize=123,
        Publish=True|False,
        VpcConfig={
            'SubnetIds': [
                'string',
            ],
            'SecurityGroupIds': [
                'string',
            ]
        },
        DeadLetterConfig={
            'TargetArn': 'string'
        },
        Environment={
            'Variables': {
                'string': 'string'
            }
        },
        KMSKeyArn='string',
        TracingConfig={
            'Mode': 'Active'|'PassThrough'
        },
        Tags={
            'string': 'string'
        },
        Layers=[
            'string',
        ]
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]
            The name of the Lambda function.
            Name formats
            Function name - MyFunction .
            Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
            Partial ARN - 123456789012:function:MyFunction .
            The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
            

    :type Runtime: string
    :param Runtime: [REQUIRED]
            The runtime version for the function.
            

    :type Role: string
    :param Role: [REQUIRED]
            The Amazon Resource Name (ARN) of the function's execution role .
            

    :type Handler: string
    :param Handler: [REQUIRED]
            The name of the method within your code that Lambda calls to execute your function. For more information, see Programming Model .
            

    :type Code: dict
    :param Code: [REQUIRED]
            The code for the function.
            ZipFile (bytes) --The base64-encoded contents of your zip file containing your deployment package. AWS SDK and AWS CLI clients handle the encoding for you.
            S3Bucket (string) --An Amazon S3 bucket in the same region as your function.
            S3Key (string) --The Amazon S3 key of the deployment package.
            S3ObjectVersion (string) --For versioned objects, the version of the deployment package object to use.
            

    :type Description: string
    :param Description: A description of the function.

    :type Timeout: integer
    :param Timeout: The amount of time that Lambda allows a function to run before terminating it. The default is 3 seconds. The maximum allowed value is 900 seconds.

    :type MemorySize: integer
    :param MemorySize: The amount of memory that your function has access to. Increasing the function's memory also increases it's CPU allocation. The default value is 128 MB. The value must be a multiple of 64 MB.

    :type Publish: boolean
    :param Publish: Set to true to publish the first version of the function during creation.

    :type VpcConfig: dict
    :param VpcConfig: If your Lambda function accesses resources in a VPC, you provide this parameter identifying the list of security group IDs and subnet IDs. These must belong to the same VPC. You must provide at least one security group and one subnet ID.
            SubnetIds (list) --A list of VPC subnet IDs.
            (string) --
            SecurityGroupIds (list) --A list of VPC security groups IDs.
            (string) --
            

    :type DeadLetterConfig: dict
    :param DeadLetterConfig: A dead letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing. For more information, see Dead Letter Queues .
            TargetArn (string) --The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.
            

    :type Environment: dict
    :param Environment: Environment variables that are accessible from function code during execution.
            Variables (dict) --Environment variable key-value pairs.
            (string) --
            (string) --
            
            

    :type KMSKeyArn: string
    :param KMSKeyArn: The ARN of the KMS key used to encrypt your function's environment variables. If not provided, AWS Lambda will use a default service key.

    :type TracingConfig: dict
    :param TracingConfig: Set Mode to Active to sample and trace a subset of incoming requests with AWS X-Ray.
            Mode (string) --The tracing mode.
            

    :type Tags: dict
    :param Tags: The list of tags (key-value pairs) assigned to the new function. For more information, see Tagging Lambda Functions in the AWS Lambda Developer Guide .
            (string) --
            (string) --
            

    :type Layers: list
    :param Layers: A list of function layers to add to the function's execution environment.
            (string) --
            

    :rtype: dict
    :return: {
        'FunctionName': 'string',
        'FunctionArn': 'string',
        'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'java8'|'python2.7'|'python3.6'|'python3.7'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
        'Role': 'string',
        'Handler': 'string',
        'CodeSize': 123,
        'Description': 'string',
        'Timeout': 123,
        'MemorySize': 123,
        'LastModified': 'string',
        'CodeSha256': 'string',
        'Version': 'string',
        'VpcConfig': {
            'SubnetIds': [
                'string',
            ],
            'SecurityGroupIds': [
                'string',
            ],
            'VpcId': 'string'
        },
        'DeadLetterConfig': {
            'TargetArn': 'string'
        },
        'Environment': {
            'Variables': {
                'string': 'string'
            },
            'Error': {
                'ErrorCode': 'string',
                'Message': 'string'
            }
        },
        'KMSKeyArn': 'string',
        'TracingConfig': {
            'Mode': 'Active'|'PassThrough'
        },
        'MasterArn': 'string',
        'RevisionId': 'string',
        'Layers': [
            {
                'Arn': 'string',
                'CodeSize': 123
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_alias(FunctionName=None, Name=None):
    """
    Deletes the specified Lambda function alias. For more information, see Introduction to AWS Lambda Aliases .
    This requires permission for the lambda:DeleteAlias action.
    See also: AWS API Documentation
    
    Examples
    This operation deletes a Lambda function alias
    Expected Output:
    
    :example: response = client.delete_alias(
        FunctionName='string',
        Name='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]
            The name of the lambda function.
            Name formats
            Function name - MyFunction .
            Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
            Partial ARN - 123456789012:function:MyFunction .
            The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
            

    :type Name: string
    :param Name: [REQUIRED]
            Name of the alias to delete.
            

    :return: response = client.delete_alias(
        FunctionName='myFunction',
        Name='alias',
    )
    
    print(response)
    
    
    """
    pass

def delete_event_source_mapping(UUID=None):
    """
    Deletes an event source mapping.
    See also: AWS API Documentation
    
    Examples
    This operation deletes a Lambda function event source mapping
    Expected Output:
    
    :example: response = client.delete_event_source_mapping(
        UUID='string'
    )
    
    
    :type UUID: string
    :param UUID: [REQUIRED]
            The identifier of the event source mapping.
            

    :rtype: dict
    :return: {
        'UUID': 'string',
        'BatchSize': 123,
        'EventSourceArn': 'string',
        'FunctionArn': 'string',
        'LastModified': datetime(2015, 1, 1),
        'LastProcessingResult': 'string',
        'State': 'string',
        'StateTransitionReason': 'string'
    }
    
    
    """
    pass

def delete_function(FunctionName=None, Qualifier=None):
    """
    Deletes a Lambda function. To delete a specific function version, use the Qualifier parameter. Otherwise, all versions and aliases are deleted. Event source mappings are not deleted.
    This operation requires permission for the lambda:DeleteFunction action.
    See also: AWS API Documentation
    
    Examples
    This operation deletes a Lambda function
    Expected Output:
    
    :example: response = client.delete_function(
        FunctionName='string',
        Qualifier='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]
            The name of the Lambda function.
            Name formats
            Function name - MyFunction .
            Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
            Partial ARN - 123456789012:function:MyFunction .
            The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
            

    :type Qualifier: string
    :param Qualifier: Specify a version to delete. You cannot delete a version that is referenced by an alias.

    :return: response = client.delete_function(
        FunctionName='myFunction',
        Qualifier='1',
    )
    
    print(response)
    
    
    """
    pass

def delete_function_concurrency(FunctionName=None):
    """
    Removes concurrent execution limits from this function. For more information, see Managing Concurrency .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_function_concurrency(
        FunctionName='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]
            The name of the Lambda function.
            Name formats
            Function name - MyFunction .
            Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
            Partial ARN - 123456789012:function:MyFunction .
            The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
            

    """
    pass

def delete_layer_version(LayerName=None, VersionNumber=None):
    """
    Deletes a version of a function layer. Deleted versions can no longer be viewed or added to functions. However, a copy of the version remains in Lambda until no functions refer to it.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_layer_version(
        LayerName='string',
        VersionNumber=123
    )
    
    
    :type LayerName: string
    :param LayerName: [REQUIRED]
            The name of the layer.
            

    :type VersionNumber: integer
    :param VersionNumber: [REQUIRED]
            The version number.
            

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

def get_account_settings():
    """
    Retrieves details about your account's limits and usage in a region.
    See also: AWS API Documentation
    
    Examples
    This operation retrieves a Lambda customer's account settings
    Expected Output:
    
    :example: response = client.get_account_settings()
    
    
    :rtype: dict
    :return: {
        'AccountLimit': {
            'TotalCodeSize': 123,
            'CodeSizeUnzipped': 123,
            'CodeSizeZipped': 123,
            'ConcurrentExecutions': 123,
            'UnreservedConcurrentExecutions': 123
        },
        'AccountUsage': {
            'TotalCodeSize': 123,
            'FunctionCount': 123
        }
    }
    
    
    """
    pass

def get_alias(FunctionName=None, Name=None):
    """
    Returns the specified alias information such as the alias ARN, description, and function version it is pointing to. For more information, see Introduction to AWS Lambda Aliases .
    This requires permission for the lambda:GetAlias action.
    See also: AWS API Documentation
    
    Examples
    This operation retrieves a Lambda function alias
    Expected Output:
    
    :example: response = client.get_alias(
        FunctionName='string',
        Name='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]
            The name of the lambda function.
            Name formats
            Function name - MyFunction .
            Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
            Partial ARN - 123456789012:function:MyFunction .
            The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
            

    :type Name: string
    :param Name: [REQUIRED]
            Name of the alias for which you want to retrieve information.
            

    :rtype: dict
    :return: {
        'AliasArn': 'string',
        'Name': 'string',
        'FunctionVersion': 'string',
        'Description': 'string',
        'RoutingConfig': {
            'AdditionalVersionWeights': {
                'string': 123.0
            }
        },
        'RevisionId': 'string'
    }
    
    
    :returns: 
    (string) --
    (float) --
    
    
    
    """
    pass

def get_event_source_mapping(UUID=None):
    """
    Returns details about an event source mapping.
    See also: AWS API Documentation
    
    Examples
    This operation retrieves a Lambda function's event source mapping
    Expected Output:
    
    :example: response = client.get_event_source_mapping(
        UUID='string'
    )
    
    
    :type UUID: string
    :param UUID: [REQUIRED]
            The identifier of the event source mapping.
            

    :rtype: dict
    :return: {
        'UUID': 'string',
        'BatchSize': 123,
        'EventSourceArn': 'string',
        'FunctionArn': 'string',
        'LastModified': datetime(2015, 1, 1),
        'LastProcessingResult': 'string',
        'State': 'string',
        'StateTransitionReason': 'string'
    }
    
    
    """
    pass

def get_function(FunctionName=None, Qualifier=None):
    """
    Returns the configuration information of the Lambda function and a presigned URL link to the .zip file you uploaded with  CreateFunction so you can download the .zip file. Note that the URL is valid for up to 10 minutes. The configuration information is the same information you provided as parameters when uploading the function.
    Use the Qualifier parameter to retrieve a published version of the function. Otherwise, returns the unpublished version ($LATEST ). For more information, see AWS Lambda Function Versioning and Aliases .
    This operation requires permission for the lambda:GetFunction action.
    See also: AWS API Documentation
    
    Examples
    This operation retrieves a Lambda function's event source mapping
    Expected Output:
    
    :example: response = client.get_function(
        FunctionName='string',
        Qualifier='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]
            The name of the Lambda function.
            Name formats
            Function name - MyFunction .
            Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
            Partial ARN - 123456789012:function:MyFunction .
            The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
            

    :type Qualifier: string
    :param Qualifier: Specify a version or alias to get details about a published version of the function.

    :rtype: dict
    :return: {
        'Configuration': {
            'FunctionName': 'string',
            'FunctionArn': 'string',
            'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'java8'|'python2.7'|'python3.6'|'python3.7'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
            'Role': 'string',
            'Handler': 'string',
            'CodeSize': 123,
            'Description': 'string',
            'Timeout': 123,
            'MemorySize': 123,
            'LastModified': 'string',
            'CodeSha256': 'string',
            'Version': 'string',
            'VpcConfig': {
                'SubnetIds': [
                    'string',
                ],
                'SecurityGroupIds': [
                    'string',
                ],
                'VpcId': 'string'
            },
            'DeadLetterConfig': {
                'TargetArn': 'string'
            },
            'Environment': {
                'Variables': {
                    'string': 'string'
                },
                'Error': {
                    'ErrorCode': 'string',
                    'Message': 'string'
                }
            },
            'KMSKeyArn': 'string',
            'TracingConfig': {
                'Mode': 'Active'|'PassThrough'
            },
            'MasterArn': 'string',
            'RevisionId': 'string',
            'Layers': [
                {
                    'Arn': 'string',
                    'CodeSize': 123
                },
            ]
        },
        'Code': {
            'RepositoryType': 'string',
            'Location': 'string'
        },
        'Tags': {
            'string': 'string'
        },
        'Concurrency': {
            'ReservedConcurrentExecutions': 123
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_function_configuration(FunctionName=None, Qualifier=None):
    """
    Returns the configuration information of the Lambda function. This the same information you provided as parameters when uploading the function by using  CreateFunction .
    If you are using the versioning feature, you can retrieve this information for a specific function version by using the optional Qualifier parameter and specifying the function version or alias that points to it. If you don't provide it, the API returns information about the $LATEST version of the function. For more information about versioning, see AWS Lambda Function Versioning and Aliases .
    This operation requires permission for the lambda:GetFunctionConfiguration operation.
    See also: AWS API Documentation
    
    Examples
    This operation retrieves a Lambda function's event source mapping
    Expected Output:
    
    :example: response = client.get_function_configuration(
        FunctionName='string',
        Qualifier='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]
            The name of the Lambda function.
            Name formats
            Function name - MyFunction .
            Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
            Partial ARN - 123456789012:function:MyFunction .
            The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
            

    :type Qualifier: string
    :param Qualifier: Specify a version or alias to get details about a published version of the function.

    :rtype: dict
    :return: {
        'FunctionName': 'string',
        'FunctionArn': 'string',
        'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'java8'|'python2.7'|'python3.6'|'python3.7'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
        'Role': 'string',
        'Handler': 'string',
        'CodeSize': 123,
        'Description': 'string',
        'Timeout': 123,
        'MemorySize': 123,
        'LastModified': 'string',
        'CodeSha256': 'string',
        'Version': 'string',
        'VpcConfig': {
            'SubnetIds': [
                'string',
            ],
            'SecurityGroupIds': [
                'string',
            ],
            'VpcId': 'string'
        },
        'DeadLetterConfig': {
            'TargetArn': 'string'
        },
        'Environment': {
            'Variables': {
                'string': 'string'
            },
            'Error': {
                'ErrorCode': 'string',
                'Message': 'string'
            }
        },
        'KMSKeyArn': 'string',
        'TracingConfig': {
            'Mode': 'Active'|'PassThrough'
        },
        'MasterArn': 'string',
        'RevisionId': 'string',
        'Layers': [
            {
                'Arn': 'string',
                'CodeSize': 123
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_layer_version(LayerName=None, VersionNumber=None):
    """
    Returns information about a version of a function layer, with a link to download the layer archive that's valid for 10 minutes.
    See also: AWS API Documentation
    
    
    :example: response = client.get_layer_version(
        LayerName='string',
        VersionNumber=123
    )
    
    
    :type LayerName: string
    :param LayerName: [REQUIRED]
            The name of the layer.
            

    :type VersionNumber: integer
    :param VersionNumber: [REQUIRED]
            The version number.
            

    :rtype: dict
    :return: {
        'Content': {
            'Location': 'string',
            'CodeSha256': 'string',
            'CodeSize': 123
        },
        'LayerArn': 'string',
        'LayerVersionArn': 'string',
        'Description': 'string',
        'CreatedDate': 'string',
        'Version': 123,
        'CompatibleRuntimes': [
            'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'java8'|'python2.7'|'python3.6'|'python3.7'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
        ],
        'LicenseInfo': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_layer_version_policy(LayerName=None, VersionNumber=None):
    """
    Returns the permission policy for a layer version. For more information, see  AddLayerVersionPermission .
    See also: AWS API Documentation
    
    
    :example: response = client.get_layer_version_policy(
        LayerName='string',
        VersionNumber=123
    )
    
    
    :type LayerName: string
    :param LayerName: [REQUIRED]
            The name of the layer.
            

    :type VersionNumber: integer
    :param VersionNumber: [REQUIRED]
            The version number.
            

    :rtype: dict
    :return: {
        'Policy': 'string',
        'RevisionId': 'string'
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

def get_policy(FunctionName=None, Qualifier=None):
    """
    Returns the resource policy associated with the specified Lambda function.
    This action requires permission for the lambda:GetPolicy action.
    See also: AWS API Documentation
    
    Examples
    This operation retrieves a Lambda function policy
    Expected Output:
    
    :example: response = client.get_policy(
        FunctionName='string',
        Qualifier='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]
            The name of the lambda function.
            Name formats
            Function name - MyFunction .
            Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
            Partial ARN - 123456789012:function:MyFunction .
            The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
            

    :type Qualifier: string
    :param Qualifier: You can specify this optional query parameter to specify a function version or an alias name in which case this API will return all permissions associated with the specific qualified ARN. If you don't provide this parameter, the API will return permissions that apply to the unqualified function ARN.

    :rtype: dict
    :return: {
        'Policy': 'string',
        'RevisionId': 'string'
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

def invoke(FunctionName=None, InvocationType=None, LogType=None, ClientContext=None, Payload=None, Qualifier=None):
    """
    Invokes a Lambda function. For an example, see Create the Lambda Function and Test It Manually .
    Specify just a function name to invoke the latest version of the function. To invoke a published version, use the Qualifier parameter to specify a version or alias .
    If you use the RequestResponse (synchronous) invocation option, the function will be invoked only once. If you use the Event (asynchronous) invocation option, the function will be invoked at least once in response to an event and the function must be idempotent to handle this.
    For functions with a long timeout, your client may be disconnected during synchronous invocation while it waits for a response. Configure your HTTP client, SDK, firewall, proxy, or operating system to allow for long connections with timeout or keep-alive settings.
    This operation requires permission for the lambda:InvokeFunction action.
    The TooManyRequestsException noted below will return the following: ConcurrentInvocationLimitExceeded will be returned if you have no functions with reserved concurrency and have exceeded your account concurrent limit or if a function without reserved concurrency exceeds the account's unreserved concurrency limit. ReservedFunctionConcurrentInvocationLimitExceeded will be returned when a function with reserved concurrency exceeds its configured concurrency limit.
    See also: AWS API Documentation
    
    Examples
    This operation invokes a Lambda function
    Expected Output:
    
    :example: response = client.invoke(
        FunctionName='string',
        InvocationType='Event'|'RequestResponse'|'DryRun',
        LogType='None'|'Tail',
        ClientContext='string',
        Payload=b'bytes'|file,
        Qualifier='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]
            The name of the Lambda function.
            Name formats
            Function name - MyFunction .
            Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
            Partial ARN - 123456789012:function:MyFunction .
            The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
            

    :type InvocationType: string
    :param InvocationType: Choose from the following options.
            RequestResponse (default) - Invoke the function synchronously. Keep the connection open until the function returns a response or times out.
            Event - Invoke the function asynchronously. Send events that fail multiple times to the function's dead-letter queue (if configured).
            DryRun - Validate parameter values and verify that the user or role has permission to invoke the function.
            

    :type LogType: string
    :param LogType: You can set this optional parameter to Tail in the request only if you specify the InvocationType parameter with value RequestResponse . In this case, AWS Lambda returns the base64-encoded last 4 KB of log data produced by your Lambda function in the x-amz-log-result header.

    :type ClientContext: string
    :param ClientContext: Using the ClientContext you can pass client-specific information to the Lambda function you are invoking. You can then process the client information in your Lambda function as you choose through the context variable. For an example of a ClientContext JSON, see PutEvents in the Amazon Mobile Analytics API Reference and User Guide .
            The ClientContext JSON must be base64-encoded and has a maximum size of 3583 bytes.
            Note
            ClientContext information is returned only if you use the synchronous (RequestResponse ) invocation type.
            

    :type Payload: bytes or seekable file-like object
    :param Payload: JSON that you want to provide to your Lambda function as input.

    :type Qualifier: string
    :param Qualifier: Specify a version or alias to invoke a published version of the function.

    :rtype: dict
    :return: {
        'StatusCode': 123,
        'FunctionError': 'string',
        'LogResult': 'string',
        'Payload': StreamingBody(),
        'ExecutedVersion': 'string'
    }
    
    
    """
    pass

def invoke_async(FunctionName=None, InvokeArgs=None):
    """
    Submits an invocation request to AWS Lambda. Upon receiving the request, Lambda executes the specified function asynchronously. To see the logs generated by the Lambda function execution, see the CloudWatch Logs console.
    This operation requires permission for the lambda:InvokeFunction action.
    See also: AWS API Documentation
    
    Examples
    This operation invokes a Lambda function asynchronously
    Expected Output:
    
    :example: response = client.invoke_async(
        FunctionName='string',
        InvokeArgs=b'bytes'|file
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]
            The name of the Lambda function.
            Name formats
            Function name - MyFunction .
            Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
            Partial ARN - 123456789012:function:MyFunction .
            The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
            

    :type InvokeArgs: bytes or seekable file-like object
    :param InvokeArgs: [REQUIRED]
            JSON that you want to provide to your Lambda function as input.
            

    :rtype: dict
    :return: {
        'Status': 123
    }
    
    
    """
    pass

def list_aliases(FunctionName=None, FunctionVersion=None, Marker=None, MaxItems=None):
    """
    Returns list of aliases created for a Lambda function. For each alias, the response includes information such as the alias ARN, description, alias name, and the function version to which it points. For more information, see Introduction to AWS Lambda Aliases .
    This requires permission for the lambda:ListAliases action.
    See also: AWS API Documentation
    
    Examples
    This operation retrieves a Lambda function's aliases
    Expected Output:
    
    :example: response = client.list_aliases(
        FunctionName='string',
        FunctionVersion='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]
            The name of the lambda function.
            Name formats
            Function name - MyFunction .
            Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
            Partial ARN - 123456789012:function:MyFunction .
            The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
            

    :type FunctionVersion: string
    :param FunctionVersion: If you specify this optional parameter, the API returns only the aliases that are pointing to the specific Lambda function version, otherwise the API returns all of the aliases created for the Lambda function.

    :type Marker: string
    :param Marker: Optional string. An opaque pagination token returned from a previous ListAliases operation. If present, indicates where to continue the listing.

    :type MaxItems: integer
    :param MaxItems: Optional integer. Specifies the maximum number of aliases to return in response. This parameter value must be greater than 0.

    :rtype: dict
    :return: {
        'NextMarker': 'string',
        'Aliases': [
            {
                'AliasArn': 'string',
                'Name': 'string',
                'FunctionVersion': 'string',
                'Description': 'string',
                'RoutingConfig': {
                    'AdditionalVersionWeights': {
                        'string': 123.0
                    }
                },
                'RevisionId': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    (float) --
    
    
    
    """
    pass

def list_event_source_mappings(EventSourceArn=None, FunctionName=None, Marker=None, MaxItems=None):
    """
    Lists event source mappings. Specify an EventSourceArn to only show event source mappings for a single event source.
    See also: AWS API Documentation
    
    
    :example: response = client.list_event_source_mappings(
        EventSourceArn='string',
        FunctionName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type EventSourceArn: string
    :param EventSourceArn: The Amazon Resource Name (ARN) of the event source.
            Amazon Kinesis - The ARN of the data stream or a stream consumer.
            Amazon DynamoDB Streams - The ARN of the stream.
            Amazon Simple Queue Service - The ARN of the queue.
            

    :type FunctionName: string
    :param FunctionName: The name of the Lambda function.
            Name formats
            Function name - MyFunction .
            Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
            Version or Alias ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD .
            Partial ARN - 123456789012:function:MyFunction .
            The length constraint applies only to the full ARN. If you specify only the function name, it's limited to 64 characters in length.
            

    :type Marker: string
    :param Marker: A pagination token returned by a previous call.

    :type MaxItems: integer
    :param MaxItems: The maximum number of event source mappings to return.

    :rtype: dict
    :return: {
        'NextMarker': 'string',
        'EventSourceMappings': [
            {
                'UUID': 'string',
                'BatchSize': 123,
                'EventSourceArn': 'string',
                'FunctionArn': 'string',
                'LastModified': datetime(2015, 1, 1),
                'LastProcessingResult': 'string',
                'State': 'string',
                'StateTransitionReason': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_functions(MasterRegion=None, FunctionVersion=None, Marker=None, MaxItems=None):
    """
    Returns a list of your Lambda functions. For each function, the response includes the function configuration information. You must use  GetFunction to retrieve the code for your function.
    This operation requires permission for the lambda:ListFunctions action.
    If you are using the versioning feature, you can list all of your functions or only $LATEST versions. For information about the versioning feature, see AWS Lambda Function Versioning and Aliases .
    See also: AWS API Documentation
    
    Examples
    This operation retrieves a Lambda functions
    Expected Output:
    
    :example: response = client.list_functions(
        MasterRegion='string',
        FunctionVersion='ALL',
        Marker='string',
        MaxItems=123
    )
    
    
    :type MasterRegion: string
    :param MasterRegion: Specify a region (e.g. us-east-2 ) to only list functions that were created in that region, or ALL to include functions replicated from any region. If specified, you also must specify the FunctionVersion .

    :type FunctionVersion: string
    :param FunctionVersion: Set to ALL to list all published versions. If not specified, only the latest unpublished version ARN is returned.

    :type Marker: string
    :param Marker: Optional string. An opaque pagination token returned from a previous ListFunctions operation. If present, indicates where to continue the listing.

    :type MaxItems: integer
    :param MaxItems: Optional integer. Specifies the maximum number of AWS Lambda functions to return in response. This parameter value must be greater than 0. The absolute maximum of AWS Lambda functions that can be returned is 50.

    :rtype: dict
    :return: {
        'NextMarker': 'string',
        'Functions': [
            {
                'FunctionName': 'string',
                'FunctionArn': 'string',
                'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'java8'|'python2.7'|'python3.6'|'python3.7'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
                'Role': 'string',
                'Handler': 'string',
                'CodeSize': 123,
                'Description': 'string',
                'Timeout': 123,
                'MemorySize': 123,
                'LastModified': 'string',
                'CodeSha256': 'string',
                'Version': 'string',
                'VpcConfig': {
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ],
                    'VpcId': 'string'
                },
                'DeadLetterConfig': {
                    'TargetArn': 'string'
                },
                'Environment': {
                    'Variables': {
                        'string': 'string'
                    },
                    'Error': {
                        'ErrorCode': 'string',
                        'Message': 'string'
                    }
                },
                'KMSKeyArn': 'string',
                'TracingConfig': {
                    'Mode': 'Active'|'PassThrough'
                },
                'MasterArn': 'string',
                'RevisionId': 'string',
                'Layers': [
                    {
                        'Arn': 'string',
                        'CodeSize': 123
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_layer_versions(CompatibleRuntime=None, LayerName=None, Marker=None, MaxItems=None):
    """
    Lists the versions of a function layer. Versions that have been deleted aren't listed. Specify a runtime identifier to list only versions that indicate that they're compatible with that runtime.
    See also: AWS API Documentation
    
    
    :example: response = client.list_layer_versions(
        CompatibleRuntime='nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'java8'|'python2.7'|'python3.6'|'python3.7'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
        LayerName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type CompatibleRuntime: string
    :param CompatibleRuntime: A runtime identifier. For example, go1.x .

    :type LayerName: string
    :param LayerName: [REQUIRED]
            The name of the layer.
            

    :type Marker: string
    :param Marker: A pagination token returned by a previous call.

    :type MaxItems: integer
    :param MaxItems: The maximum number of versions to return.

    :rtype: dict
    :return: {
        'NextMarker': 'string',
        'LayerVersions': [
            {
                'LayerVersionArn': 'string',
                'Version': 123,
                'Description': 'string',
                'CreatedDate': 'string',
                'CompatibleRuntimes': [
                    'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'java8'|'python2.7'|'python3.6'|'python3.7'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
                ],
                'LicenseInfo': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_layers(CompatibleRuntime=None, Marker=None, MaxItems=None):
    """
    Lists function layers and shows information about the latest version of each. Specify a runtime identifier to list only layers that indicate that they're compatible with that runtime.
    See also: AWS API Documentation
    
    
    :example: response = client.list_layers(
        CompatibleRuntime='nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'java8'|'python2.7'|'python3.6'|'python3.7'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
        Marker='string',
        MaxItems=123
    )
    
    
    :type CompatibleRuntime: string
    :param CompatibleRuntime: A runtime identifier. For example, go1.x .

    :type Marker: string
    :param Marker: A pagination token returned by a previous call.

    :type MaxItems: integer
    :param MaxItems: The maximum number of layers to return.

    :rtype: dict
    :return: {
        'NextMarker': 'string',
        'Layers': [
            {
                'LayerName': 'string',
                'LayerArn': 'string',
                'LatestMatchingVersion': {
                    'LayerVersionArn': 'string',
                    'Version': 123,
                    'Description': 'string',
                    'CreatedDate': 'string',
                    'CompatibleRuntimes': [
                        'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'java8'|'python2.7'|'python3.6'|'python3.7'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
                    ],
                    'LicenseInfo': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tags(Resource=None):
    """
    Returns a list of tags assigned to a function when supplied the function ARN (Amazon Resource Name). For more information on Tagging, see Tagging Lambda Functions in the AWS Lambda Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags(
        Resource='string'
    )
    
    
    :type Resource: string
    :param Resource: [REQUIRED]
            The ARN (Amazon Resource Name) of the function. For more information, see Tagging Lambda Functions in the AWS Lambda Developer Guide .
            

    :rtype: dict
    :return: {
        'Tags': {
            'string': 'string'
        }
    }
    
    
    """
    pass

def list_versions_by_function(FunctionName=None, Marker=None, MaxItems=None):
    """
    Lists all versions of a function. For information about versioning, see AWS Lambda Function Versioning and Aliases .
    See also: AWS API Documentation
    
    Examples
    This operation retrieves a Lambda function versions
    Expected Output:
    
    :example: response = client.list_versions_by_function(
        FunctionName='string',
        Marker='string',
        MaxItems=123
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]
            The name of the lambda function.
            Name formats
            Function name - MyFunction .
            Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
            Partial ARN - 123456789012:function:MyFunction .
            The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
            

    :type Marker: string
    :param Marker: Optional string. An opaque pagination token returned from a previous ListVersionsByFunction operation. If present, indicates where to continue the listing.

    :type MaxItems: integer
    :param MaxItems: Optional integer. Specifies the maximum number of AWS Lambda function versions to return in response. This parameter value must be greater than 0.

    :rtype: dict
    :return: {
        'NextMarker': 'string',
        'Versions': [
            {
                'FunctionName': 'string',
                'FunctionArn': 'string',
                'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'java8'|'python2.7'|'python3.6'|'python3.7'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
                'Role': 'string',
                'Handler': 'string',
                'CodeSize': 123,
                'Description': 'string',
                'Timeout': 123,
                'MemorySize': 123,
                'LastModified': 'string',
                'CodeSha256': 'string',
                'Version': 'string',
                'VpcConfig': {
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ],
                    'VpcId': 'string'
                },
                'DeadLetterConfig': {
                    'TargetArn': 'string'
                },
                'Environment': {
                    'Variables': {
                        'string': 'string'
                    },
                    'Error': {
                        'ErrorCode': 'string',
                        'Message': 'string'
                    }
                },
                'KMSKeyArn': 'string',
                'TracingConfig': {
                    'Mode': 'Active'|'PassThrough'
                },
                'MasterArn': 'string',
                'RevisionId': 'string',
                'Layers': [
                    {
                        'Arn': 'string',
                        'CodeSize': 123
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def publish_layer_version(LayerName=None, Description=None, Content=None, CompatibleRuntimes=None, LicenseInfo=None):
    """
    Creates a function layer from a ZIP archive. Each time you call PublishLayerVersion with the same version name, a new version is created.
    Add layers to your function with  CreateFunction or  UpdateFunctionConfiguration .
    See also: AWS API Documentation
    
    
    :example: response = client.publish_layer_version(
        LayerName='string',
        Description='string',
        Content={
            'S3Bucket': 'string',
            'S3Key': 'string',
            'S3ObjectVersion': 'string',
            'ZipFile': b'bytes'
        },
        CompatibleRuntimes=[
            'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'java8'|'python2.7'|'python3.6'|'python3.7'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
        ],
        LicenseInfo='string'
    )
    
    
    :type LayerName: string
    :param LayerName: [REQUIRED]
            The name of the layer.
            

    :type Description: string
    :param Description: The description of the version.

    :type Content: dict
    :param Content: [REQUIRED]
            The function layer archive.
            S3Bucket (string) --The Amazon S3 bucket of the layer archive.
            S3Key (string) --The Amazon S3 key of the layer archive.
            S3ObjectVersion (string) --For versioned objects, the version of the layer archive object to use.
            ZipFile (bytes) --The base64-encoded contents of the layer archive. AWS SDK and AWS CLI clients handle the encoding for you.
            

    :type CompatibleRuntimes: list
    :param CompatibleRuntimes: A list of compatible function runtimes . Used for filtering with ListLayers and ListLayerVersions .
            (string) --
            

    :type LicenseInfo: string
    :param LicenseInfo: The layer's software license. It can be any of the following:
            An SPDX license identifier . For example, MIT .
            The URL of a license hosted on the internet. For example, https://opensource.org/licenses/MIT .
            The full text of the license.
            

    :rtype: dict
    :return: {
        'Content': {
            'Location': 'string',
            'CodeSha256': 'string',
            'CodeSize': 123
        },
        'LayerArn': 'string',
        'LayerVersionArn': 'string',
        'Description': 'string',
        'CreatedDate': 'string',
        'Version': 123,
        'CompatibleRuntimes': [
            'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'java8'|'python2.7'|'python3.6'|'python3.7'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
        ],
        'LicenseInfo': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def publish_version(FunctionName=None, CodeSha256=None, Description=None, RevisionId=None):
    """
    Publishes a version of your function from the current snapshot of $LATEST. That is, AWS Lambda takes a snapshot of the function code and configuration information from $LATEST and publishes a new version. The code and configuration cannot be modified after publication. For information about the versioning feature, see AWS Lambda Function Versioning and Aliases .
    See also: AWS API Documentation
    
    Examples
    This operation publishes a version of a Lambda function
    Expected Output:
    
    :example: response = client.publish_version(
        FunctionName='string',
        CodeSha256='string',
        Description='string',
        RevisionId='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]
            The name of the lambda function.
            Name formats
            Function name - MyFunction .
            Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
            Partial ARN - 123456789012:function:MyFunction .
            The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
            

    :type CodeSha256: string
    :param CodeSha256: The SHA256 hash of the deployment package you want to publish. This provides validation on the code you are publishing. If you provide this parameter, the value must match the SHA256 of the $LATEST version for the publication to succeed. You can use the DryRun parameter of UpdateFunctionCode to verify the hash value that will be returned before publishing your new version.

    :type Description: string
    :param Description: The description for the version you are publishing. If not provided, AWS Lambda copies the description from the $LATEST version.

    :type RevisionId: string
    :param RevisionId: An optional value you can use to ensure you are updating the latest update of the function version or alias. If the RevisionID you pass doesn't match the latest RevisionId of the function or alias, it will fail with an error message, advising you retrieve the latest function version or alias RevisionID using either GetFunction or GetAlias .

    :rtype: dict
    :return: {
        'FunctionName': 'string',
        'FunctionArn': 'string',
        'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'java8'|'python2.7'|'python3.6'|'python3.7'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
        'Role': 'string',
        'Handler': 'string',
        'CodeSize': 123,
        'Description': 'string',
        'Timeout': 123,
        'MemorySize': 123,
        'LastModified': 'string',
        'CodeSha256': 'string',
        'Version': 'string',
        'VpcConfig': {
            'SubnetIds': [
                'string',
            ],
            'SecurityGroupIds': [
                'string',
            ],
            'VpcId': 'string'
        },
        'DeadLetterConfig': {
            'TargetArn': 'string'
        },
        'Environment': {
            'Variables': {
                'string': 'string'
            },
            'Error': {
                'ErrorCode': 'string',
                'Message': 'string'
            }
        },
        'KMSKeyArn': 'string',
        'TracingConfig': {
            'Mode': 'Active'|'PassThrough'
        },
        'MasterArn': 'string',
        'RevisionId': 'string',
        'Layers': [
            {
                'Arn': 'string',
                'CodeSize': 123
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def put_function_concurrency(FunctionName=None, ReservedConcurrentExecutions=None):
    """
    Sets a limit on the number of concurrent executions available to this function. It is a subset of your account's total concurrent execution limit per region. Note that Lambda automatically reserves a buffer of 100 concurrent executions for functions without any reserved concurrency limit. This means if your account limit is 1000, you have a total of 900 available to allocate to individual functions. For more information, see Managing Concurrency .
    See also: AWS API Documentation
    
    
    :example: response = client.put_function_concurrency(
        FunctionName='string',
        ReservedConcurrentExecutions=123
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]
            The name of the Lambda function.
            Name formats
            Function name - MyFunction .
            Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
            Partial ARN - 123456789012:function:MyFunction .
            The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
            

    :type ReservedConcurrentExecutions: integer
    :param ReservedConcurrentExecutions: [REQUIRED]
            The concurrent execution limit reserved for this function.
            

    :rtype: dict
    :return: {
        'ReservedConcurrentExecutions': 123
    }
    
    
    """
    pass

def remove_layer_version_permission(LayerName=None, VersionNumber=None, StatementId=None, RevisionId=None):
    """
    Removes a statement from the permissions policy for a layer version. For more information, see  AddLayerVersionPermission .
    See also: AWS API Documentation
    
    
    :example: response = client.remove_layer_version_permission(
        LayerName='string',
        VersionNumber=123,
        StatementId='string',
        RevisionId='string'
    )
    
    
    :type LayerName: string
    :param LayerName: [REQUIRED]
            The name of the layer.
            

    :type VersionNumber: integer
    :param VersionNumber: [REQUIRED]
            The version number.
            

    :type StatementId: string
    :param StatementId: [REQUIRED]
            The identifier that was specified when the statement was added.
            

    :type RevisionId: string
    :param RevisionId: Only update the policy if the revision ID matches the ID specified. Use this option to avoid modifying a policy that has changed since you last read it.

    """
    pass

def remove_permission(FunctionName=None, StatementId=None, Qualifier=None, RevisionId=None):
    """
    Removes permissions from a function. You can remove individual permissions from an resource policy associated with a Lambda function by providing a statement ID that you provided when you added the permission. When you remove permissions, disable the event source mapping or trigger configuration first to avoid errors.
    Permissions apply to the Amazon Resource Name (ARN) used to invoke the function, which can be unqualified (the unpublished version of the function), or include a version or alias. If a client uses a version or alias to invoke a function, use the Qualifier parameter to apply permissions to that ARN. For more information about versioning, see AWS Lambda Function Versioning and Aliases .
    You need permission for the lambda:RemovePermission action.
    See also: AWS API Documentation
    
    Examples
    This operation removes a Lambda function's permissions
    Expected Output:
    
    :example: response = client.remove_permission(
        FunctionName='string',
        StatementId='string',
        Qualifier='string',
        RevisionId='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]
            The name of the Lambda function.
            Name formats
            Function name - MyFunction .
            Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
            Partial ARN - 123456789012:function:MyFunction .
            The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
            

    :type StatementId: string
    :param StatementId: [REQUIRED]
            Statement ID of the permission to remove.
            

    :type Qualifier: string
    :param Qualifier: Specify a version or alias to remove permissions from a published version of the function.

    :type RevisionId: string
    :param RevisionId: An optional value you can use to ensure you are updating the latest update of the function version or alias. If the RevisionID you pass doesn't match the latest RevisionId of the function or alias, it will fail with an error message, advising you to retrieve the latest function version or alias RevisionID using either GetFunction or GetAlias .

    :return: response = client.remove_permission(
        FunctionName='myFunction',
        Qualifier='1',
        StatementId='role-statement-id',
    )
    
    print(response)
    
    
    """
    pass

def tag_resource(Resource=None, Tags=None):
    """
    Creates a list of tags (key-value pairs) on the Lambda function. Requires the Lambda function ARN (Amazon Resource Name). If a key is specified without a value, Lambda creates a tag with the specified key and a value of null. For more information, see Tagging Lambda Functions in the AWS Lambda Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.tag_resource(
        Resource='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type Resource: string
    :param Resource: [REQUIRED]
            The ARN (Amazon Resource Name) of the Lambda function. For more information, see Tagging Lambda Functions in the AWS Lambda Developer Guide .
            

    :type Tags: dict
    :param Tags: [REQUIRED]
            The list of tags (key-value pairs) you are assigning to the Lambda function. For more information, see Tagging Lambda Functions in the AWS Lambda Developer Guide .
            (string) --
            (string) --
            

    """
    pass

def untag_resource(Resource=None, TagKeys=None):
    """
    Removes tags from a Lambda function. Requires the function ARN (Amazon Resource Name). For more information, see Tagging Lambda Functions in the AWS Lambda Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.untag_resource(
        Resource='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type Resource: string
    :param Resource: [REQUIRED]
            The ARN (Amazon Resource Name) of the function. For more information, see Tagging Lambda Functions in the AWS Lambda Developer Guide .
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            The list of tag keys to be deleted from the function. For more information, see Tagging Lambda Functions in the AWS Lambda Developer Guide .
            (string) --
            

    """
    pass

def update_alias(FunctionName=None, Name=None, FunctionVersion=None, Description=None, RoutingConfig=None, RevisionId=None):
    """
    Using this API you can update the function version to which the alias points and the alias description. For more information, see Introduction to AWS Lambda Aliases .
    This requires permission for the lambda:UpdateAlias action.
    See also: AWS API Documentation
    
    Examples
    This operation updates a Lambda function alias
    Expected Output:
    
    :example: response = client.update_alias(
        FunctionName='string',
        Name='string',
        FunctionVersion='string',
        Description='string',
        RoutingConfig={
            'AdditionalVersionWeights': {
                'string': 123.0
            }
        },
        RevisionId='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]
            The name of the lambda function.
            Name formats
            Function name - MyFunction .
            Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
            Partial ARN - 123456789012:function:MyFunction .
            The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
            

    :type Name: string
    :param Name: [REQUIRED]
            The alias name.
            

    :type FunctionVersion: string
    :param FunctionVersion: Using this parameter you can change the Lambda function version to which the alias points.

    :type Description: string
    :param Description: You can change the description of the alias using this parameter.

    :type RoutingConfig: dict
    :param RoutingConfig: Specifies an additional version your alias can point to, allowing you to dictate what percentage of traffic will invoke each version. For more information, see Traffic Shifting Using Aliases .
            AdditionalVersionWeights (dict) --The name of the second alias, and the percentage of traffic that is routed to it.
            (string) --
            (float) --
            
            

    :type RevisionId: string
    :param RevisionId: An optional value you can use to ensure you are updating the latest update of the function version or alias. If the RevisionID you pass doesn't match the latest RevisionId of the function or alias, it will fail with an error message, advising you retrieve the latest function version or alias RevisionID using either GetFunction or GetAlias .

    :rtype: dict
    :return: {
        'AliasArn': 'string',
        'Name': 'string',
        'FunctionVersion': 'string',
        'Description': 'string',
        'RoutingConfig': {
            'AdditionalVersionWeights': {
                'string': 123.0
            }
        },
        'RevisionId': 'string'
    }
    
    
    :returns: 
    (string) --
    (float) --
    
    
    
    """
    pass

def update_event_source_mapping(UUID=None, FunctionName=None, Enabled=None, BatchSize=None):
    """
    Updates an event source mapping. You can change the function that AWS Lambda invokes, or pause invocation and resume later from the same location.
    See also: AWS API Documentation
    
    Examples
    This operation updates a Lambda function event source mapping
    Expected Output:
    
    :example: response = client.update_event_source_mapping(
        UUID='string',
        FunctionName='string',
        Enabled=True|False,
        BatchSize=123
    )
    
    
    :type UUID: string
    :param UUID: [REQUIRED]
            The identifier of the event source mapping.
            

    :type FunctionName: string
    :param FunctionName: The name of the Lambda function.
            Name formats
            Function name - MyFunction .
            Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
            Version or Alias ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD .
            Partial ARN - 123456789012:function:MyFunction .
            The length constraint applies only to the full ARN. If you specify only the function name, it's limited to 64 characters in length.
            

    :type Enabled: boolean
    :param Enabled: Disables the event source mapping to pause polling and invocation.

    :type BatchSize: integer
    :param BatchSize: The maximum number of items to retrieve in a single batch.
            Amazon Kinesis - Default 100. Max 10,000.
            Amazon DynamoDB Streams - Default 100. Max 1,000.
            Amazon Simple Queue Service - Default 10. Max 10.
            

    :rtype: dict
    :return: {
        'UUID': 'string',
        'BatchSize': 123,
        'EventSourceArn': 'string',
        'FunctionArn': 'string',
        'LastModified': datetime(2015, 1, 1),
        'LastProcessingResult': 'string',
        'State': 'string',
        'StateTransitionReason': 'string'
    }
    
    
    """
    pass

def update_function_code(FunctionName=None, ZipFile=None, S3Bucket=None, S3Key=None, S3ObjectVersion=None, Publish=None, DryRun=None, RevisionId=None):
    """
    Updates the code for the specified Lambda function. This operation must only be used on an existing Lambda function and cannot be used to update the function configuration.
    If you are using the versioning feature, note this API will always update the $LATEST version of your Lambda function. For information about the versioning feature, see AWS Lambda Function Versioning and Aliases .
    This operation requires permission for the lambda:UpdateFunctionCode action.
    See also: AWS API Documentation
    
    Examples
    This operation updates a Lambda function's code
    Expected Output:
    
    :example: response = client.update_function_code(
        FunctionName='string',
        ZipFile=b'bytes',
        S3Bucket='string',
        S3Key='string',
        S3ObjectVersion='string',
        Publish=True|False,
        DryRun=True|False,
        RevisionId='string'
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]
            The name of the Lambda function.
            Name formats
            Function name - MyFunction .
            Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
            Partial ARN - 123456789012:function:MyFunction .
            The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
            

    :type ZipFile: bytes
    :param ZipFile: The contents of your zip file containing your deployment package. If you are using the web API directly, the contents of the zip file must be base64-encoded. If you are using the AWS SDKs or the AWS CLI, the SDKs or CLI will do the encoding for you. For more information about creating a .zip file, see Execution Permissions .
            This value will be base64 encoded automatically. Do not base64 encode this value prior to performing the operation.
            

    :type S3Bucket: string
    :param S3Bucket: Amazon S3 bucket name where the .zip file containing your deployment package is stored. This bucket must reside in the same AWS Region where you are creating the Lambda function.

    :type S3Key: string
    :param S3Key: The Amazon S3 object (the deployment package) key name you want to upload.

    :type S3ObjectVersion: string
    :param S3ObjectVersion: The Amazon S3 object (the deployment package) version you want to upload.

    :type Publish: boolean
    :param Publish: This boolean parameter can be used to request AWS Lambda to update the Lambda function and publish a version as an atomic operation.

    :type DryRun: boolean
    :param DryRun: This boolean parameter can be used to test your request to AWS Lambda to update the Lambda function and publish a version as an atomic operation. It will do all necessary computation and validation of your code but will not upload it or a publish a version. Each time this operation is invoked, the CodeSha256 hash value of the provided code will also be computed and returned in the response.

    :type RevisionId: string
    :param RevisionId: An optional value you can use to ensure you are updating the latest update of the function version or alias. If the RevisionID you pass doesn't match the latest RevisionId of the function or alias, it will fail with an error message, advising you to retrieve the latest function version or alias RevisionID using either using using either GetFunction or GetAlias .

    :rtype: dict
    :return: {
        'FunctionName': 'string',
        'FunctionArn': 'string',
        'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'java8'|'python2.7'|'python3.6'|'python3.7'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
        'Role': 'string',
        'Handler': 'string',
        'CodeSize': 123,
        'Description': 'string',
        'Timeout': 123,
        'MemorySize': 123,
        'LastModified': 'string',
        'CodeSha256': 'string',
        'Version': 'string',
        'VpcConfig': {
            'SubnetIds': [
                'string',
            ],
            'SecurityGroupIds': [
                'string',
            ],
            'VpcId': 'string'
        },
        'DeadLetterConfig': {
            'TargetArn': 'string'
        },
        'Environment': {
            'Variables': {
                'string': 'string'
            },
            'Error': {
                'ErrorCode': 'string',
                'Message': 'string'
            }
        },
        'KMSKeyArn': 'string',
        'TracingConfig': {
            'Mode': 'Active'|'PassThrough'
        },
        'MasterArn': 'string',
        'RevisionId': 'string',
        'Layers': [
            {
                'Arn': 'string',
                'CodeSize': 123
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_function_configuration(FunctionName=None, Role=None, Handler=None, Description=None, Timeout=None, MemorySize=None, VpcConfig=None, Environment=None, Runtime=None, DeadLetterConfig=None, KMSKeyArn=None, TracingConfig=None, RevisionId=None, Layers=None):
    """
    Updates the configuration parameters for the specified Lambda function by using the values provided in the request. You provide only the parameters you want to change. This operation must only be used on an existing Lambda function and cannot be used to update the function's code.
    If you are using the versioning feature, note this API will always update the $LATEST version of your Lambda function. For information about the versioning feature, see AWS Lambda Function Versioning and Aliases .
    This operation requires permission for the lambda:UpdateFunctionConfiguration action.
    See also: AWS API Documentation
    
    Examples
    This operation updates a Lambda function's configuration
    Expected Output:
    
    :example: response = client.update_function_configuration(
        FunctionName='string',
        Role='string',
        Handler='string',
        Description='string',
        Timeout=123,
        MemorySize=123,
        VpcConfig={
            'SubnetIds': [
                'string',
            ],
            'SecurityGroupIds': [
                'string',
            ]
        },
        Environment={
            'Variables': {
                'string': 'string'
            }
        },
        Runtime='nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'java8'|'python2.7'|'python3.6'|'python3.7'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
        DeadLetterConfig={
            'TargetArn': 'string'
        },
        KMSKeyArn='string',
        TracingConfig={
            'Mode': 'Active'|'PassThrough'
        },
        RevisionId='string',
        Layers=[
            'string',
        ]
    )
    
    
    :type FunctionName: string
    :param FunctionName: [REQUIRED]
            The name of the Lambda function.
            Name formats
            Function name - MyFunction .
            Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction .
            Partial ARN - 123456789012:function:MyFunction .
            The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
            

    :type Role: string
    :param Role: The Amazon Resource Name (ARN) of the IAM role that Lambda will assume when it executes your function.

    :type Handler: string
    :param Handler: The function that Lambda calls to begin executing your function. For Node.js, it is the module-name.export value in your function.

    :type Description: string
    :param Description: A short user-defined function description. AWS Lambda does not use this value. Assign a meaningful description as you see fit.

    :type Timeout: integer
    :param Timeout: The amount of time that Lambda allows a function to run before terminating it. The default is 3 seconds. The maximum allowed value is 900 seconds.

    :type MemorySize: integer
    :param MemorySize: The amount of memory, in MB, your Lambda function is given. AWS Lambda uses this memory size to infer the amount of CPU allocated to your function. Your function use-case determines your CPU and memory requirements. For example, a database operation might need less memory compared to an image processing function. The default value is 128 MB. The value must be a multiple of 64 MB.

    :type VpcConfig: dict
    :param VpcConfig: Specify security groups and subnets in a VPC to which your Lambda function needs access.
            SubnetIds (list) --A list of VPC subnet IDs.
            (string) --
            SecurityGroupIds (list) --A list of VPC security groups IDs.
            (string) --
            

    :type Environment: dict
    :param Environment: The parent object that contains your environment's configuration settings.
            Variables (dict) --Environment variable key-value pairs.
            (string) --
            (string) --
            
            

    :type Runtime: string
    :param Runtime: The runtime version for the function.

    :type DeadLetterConfig: dict
    :param DeadLetterConfig: A dead letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing. For more information, see Dead Letter Queues .
            TargetArn (string) --The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.
            

    :type KMSKeyArn: string
    :param KMSKeyArn: The Amazon Resource Name (ARN) of the KMS key used to encrypt your function's environment variables. If you elect to use the AWS Lambda default service key, pass in an empty string ('') for this parameter.

    :type TracingConfig: dict
    :param TracingConfig: Set Mode to Active to sample and trace a subset of incoming requests with AWS X-Ray.
            Mode (string) --The tracing mode.
            

    :type RevisionId: string
    :param RevisionId: An optional value you can use to ensure you are updating the latest update of the function version or alias. If the RevisionID you pass doesn't match the latest RevisionId of the function or alias, it will fail with an error message, advising you to retrieve the latest function version or alias RevisionID using either GetFunction or GetAlias .

    :type Layers: list
    :param Layers: A list of function layers to add to the function's execution environment.
            (string) --
            

    :rtype: dict
    :return: {
        'FunctionName': 'string',
        'FunctionArn': 'string',
        'Runtime': 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'java8'|'python2.7'|'python3.6'|'python3.7'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
        'Role': 'string',
        'Handler': 'string',
        'CodeSize': 123,
        'Description': 'string',
        'Timeout': 123,
        'MemorySize': 123,
        'LastModified': 'string',
        'CodeSha256': 'string',
        'Version': 'string',
        'VpcConfig': {
            'SubnetIds': [
                'string',
            ],
            'SecurityGroupIds': [
                'string',
            ],
            'VpcId': 'string'
        },
        'DeadLetterConfig': {
            'TargetArn': 'string'
        },
        'Environment': {
            'Variables': {
                'string': 'string'
            },
            'Error': {
                'ErrorCode': 'string',
                'Message': 'string'
            }
        },
        'KMSKeyArn': 'string',
        'TracingConfig': {
            'Mode': 'Active'|'PassThrough'
        },
        'MasterArn': 'string',
        'RevisionId': 'string',
        'Layers': [
            {
                'Arn': 'string',
                'CodeSize': 123
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

