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

def create_broker(AutoMinorVersionUpgrade=None, BrokerName=None, Configuration=None, CreatorRequestId=None, DeploymentMode=None, EngineType=None, EngineVersion=None, HostInstanceType=None, Logs=None, MaintenanceWindowStartTime=None, PubliclyAccessible=None, SecurityGroups=None, SubnetIds=None, Tags=None, Users=None):
    """
    Creates a broker. Note: This API is asynchronous.
    See also: AWS API Documentation
    
    
    :example: response = client.create_broker(
        AutoMinorVersionUpgrade=True|False,
        BrokerName='string',
        Configuration={
            'Id': 'string',
            'Revision': 123
        },
        CreatorRequestId='string',
        DeploymentMode='SINGLE_INSTANCE'|'ACTIVE_STANDBY_MULTI_AZ',
        EngineType='ACTIVEMQ',
        EngineVersion='string',
        HostInstanceType='string',
        Logs={
            'Audit': True|False,
            'General': True|False
        },
        MaintenanceWindowStartTime={
            'DayOfWeek': 'MONDAY'|'TUESDAY'|'WEDNESDAY'|'THURSDAY'|'FRIDAY'|'SATURDAY'|'SUNDAY',
            'TimeOfDay': 'string',
            'TimeZone': 'string'
        },
        PubliclyAccessible=True|False,
        SecurityGroups=[
            'string',
        ],
        SubnetIds=[
            'string',
        ],
        Tags={
            'string': 'string'
        },
        Users=[
            {
                'ConsoleAccess': True|False,
                'Groups': [
                    'string',
                ],
                'Password': 'string',
                'Username': 'string'
            },
        ]
    )
    
    
    :type AutoMinorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: Required. Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions. The automatic upgrades occur during the maintenance window of the broker or after a manual broker reboot.

    :type BrokerName: string
    :param BrokerName: Required. The name of the broker. This value must be unique in your AWS account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain whitespaces, brackets, wildcard characters, or special characters.

    :type Configuration: dict
    :param Configuration: A list of information about the configuration.
            Id (string) -- Required. The unique ID that Amazon MQ generates for the configuration.
            Revision (integer) -- The revision number of the configuration.
            

    :type CreatorRequestId: string
    :param CreatorRequestId: The unique ID that the requester receives for the created broker. Amazon MQ passes your ID with the API action. Note: We recommend using a Universally Unique Identifier (UUID) for the creatorRequestId. You may omit the creatorRequestId if your application doesn't require idempotency.This field is autopopulated if not provided.

    :type DeploymentMode: string
    :param DeploymentMode: Required. The deployment mode of the broker.

    :type EngineType: string
    :param EngineType: Required. The type of broker engine. Note: Currently, Amazon MQ supports only ACTIVEMQ.

    :type EngineVersion: string
    :param EngineVersion: Required. The version of the broker engine. For a list of supported engine versions, see https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html

    :type HostInstanceType: string
    :param HostInstanceType: Required. The broker's instance type.

    :type Logs: dict
    :param Logs: Enables Amazon CloudWatch logging for brokers.
            Audit (boolean) -- Enables audit logging. Every user management action made using JMX or the ActiveMQ Web Console is logged.
            General (boolean) -- Enables general logging.
            

    :type MaintenanceWindowStartTime: dict
    :param MaintenanceWindowStartTime: The parameters that determine the WeeklyStartTime.
            DayOfWeek (string) -- Required. The day of the week.
            TimeOfDay (string) -- Required. The time, in 24-hour format.
            TimeZone (string) -- The time zone, UTC by default, in either the Country/City format, or the UTC offset format.
            

    :type PubliclyAccessible: boolean
    :param PubliclyAccessible: Required. Enables connections from applications outside of the VPC that hosts the broker's subnets.

    :type SecurityGroups: list
    :param SecurityGroups: The list of rules (1 minimum, 125 maximum) that authorize connections to brokers.
            (string) --
            

    :type SubnetIds: list
    :param SubnetIds: The list of groups (2 maximum) that define which subnets and IP ranges the broker can use from different Availability Zones. A SINGLE_INSTANCE deployment requires one subnet (for example, the default subnet). An ACTIVE_STANDBY_MULTI_AZ deployment requires two subnets.
            (string) --
            

    :type Tags: dict
    :param Tags: Create tags when creating the broker.
            (string) --
            (string) --
            

    :type Users: list
    :param Users: Required. The list of ActiveMQ users (persons or applications) who can access queues and topics. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.
            (dict) -- An ActiveMQ user associated with the broker.
            ConsoleAccess (boolean) -- Enables access to the the ActiveMQ Web Console for the ActiveMQ user.
            Groups (list) -- The list of groups (20 maximum) to which the ActiveMQ user belongs. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.
            (string) --
            Password (string) -- Required. The password of the ActiveMQ user. This value must be at least 12 characters long, must contain at least 4 unique characters, and must not contain commas.
            Username (string) -- Required. The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.
            

    :rtype: dict
    :return: {
        'BrokerArn': 'string',
        'BrokerId': 'string'
    }
    
    
    :returns: 
    (dict) -- HTTP Status Code 200: OK.
    BrokerArn (string) -- The Amazon Resource Name (ARN) of the broker.
    BrokerId (string) -- The unique ID that Amazon MQ generates for the broker.
    
    
    
    """
    pass

def create_configuration(EngineType=None, EngineVersion=None, Name=None, Tags=None):
    """
    Creates a new configuration for the specified configuration name. Amazon MQ uses the default configuration (the engine type and version).
    See also: AWS API Documentation
    
    
    :example: response = client.create_configuration(
        EngineType='ACTIVEMQ',
        EngineVersion='string',
        Name='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type EngineType: string
    :param EngineType: Required. The type of broker engine. Note: Currently, Amazon MQ supports only ACTIVEMQ.

    :type EngineVersion: string
    :param EngineVersion: Required. The version of the broker engine. For a list of supported engine versions, see https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html

    :type Name: string
    :param Name: Required. The name of the configuration. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 1-150 characters long.

    :type Tags: dict
    :param Tags: Create tags when creating the configuration.
            (string) --
            (string) --
            

    :rtype: dict
    :return: {
        'Arn': 'string',
        'Created': datetime(2015, 1, 1),
        'Id': 'string',
        'LatestRevision': {
            'Created': datetime(2015, 1, 1),
            'Description': 'string',
            'Revision': 123
        },
        'Name': 'string'
    }
    
    
    :returns: 
    (dict) -- HTTP Status Code 200: OK.
    Arn (string) -- Required. The Amazon Resource Name (ARN) of the configuration.
    Created (datetime) -- Required. The date and time of the configuration.
    Id (string) -- Required. The unique ID that Amazon MQ generates for the configuration.
    LatestRevision (dict) -- The latest revision of the configuration.
    Created (datetime) -- Required. The date and time of the configuration revision.
    Description (string) -- The description of the configuration revision.
    Revision (integer) -- Required. The revision number of the configuration.
    
    
    Name (string) -- Required. The name of the configuration. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 1-150 characters long.
    
    
    
    """
    pass

def create_tags(ResourceArn=None, Tags=None):
    """
    Add a tag to a resource.
    See also: AWS API Documentation
    
    
    :example: response = client.create_tags(
        ResourceArn='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED] the Amazon Resource Name (ARN)

    :type Tags: dict
    :param Tags: The key-value pair for the resource tag.
            (string) --
            (string) --
            

    """
    pass

def create_user(BrokerId=None, ConsoleAccess=None, Groups=None, Password=None, Username=None):
    """
    Creates an ActiveMQ user.
    See also: AWS API Documentation
    
    
    :example: response = client.create_user(
        BrokerId='string',
        ConsoleAccess=True|False,
        Groups=[
            'string',
        ],
        Password='string',
        Username='string'
    )
    
    
    :type BrokerId: string
    :param BrokerId: [REQUIRED] The unique ID that Amazon MQ generates for the broker.

    :type ConsoleAccess: boolean
    :param ConsoleAccess: Enables access to the the ActiveMQ Web Console for the ActiveMQ user.

    :type Groups: list
    :param Groups: The list of groups (20 maximum) to which the ActiveMQ user belongs. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.
            (string) --
            

    :type Password: string
    :param Password: Required. The password of the user. This value must be at least 12 characters long, must contain at least 4 unique characters, and must not contain commas.

    :type Username: string
    :param Username: [REQUIRED] The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) -- HTTP Status Code 200: OK.
    
    """
    pass

def delete_broker(BrokerId=None):
    """
    Deletes a broker. Note: This API is asynchronous.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_broker(
        BrokerId='string'
    )
    
    
    :type BrokerId: string
    :param BrokerId: [REQUIRED] The name of the broker. This value must be unique in your AWS account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain whitespaces, brackets, wildcard characters, or special characters.

    :rtype: dict
    :return: {
        'BrokerId': 'string'
    }
    
    
    """
    pass

def delete_tags(ResourceArn=None, TagKeys=None):
    """
    Remove a tag from a resource.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_tags(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED] the Amazon Resource Name (ARN)

    :type TagKeys: list
    :param TagKeys: [REQUIRED] An array of tag keys to delete
            (string) --
            

    """
    pass

def delete_user(BrokerId=None, Username=None):
    """
    Deletes an ActiveMQ user.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_user(
        BrokerId='string',
        Username='string'
    )
    
    
    :type BrokerId: string
    :param BrokerId: [REQUIRED] The unique ID that Amazon MQ generates for the broker.

    :type Username: string
    :param Username: [REQUIRED] The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) -- HTTP Status Code 200: OK.
    
    """
    pass

def describe_broker(BrokerId=None):
    """
    Returns information about the specified broker.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_broker(
        BrokerId='string'
    )
    
    
    :type BrokerId: string
    :param BrokerId: [REQUIRED] The name of the broker. This value must be unique in your AWS account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain whitespaces, brackets, wildcard characters, or special characters.

    :rtype: dict
    :return: {
        'AutoMinorVersionUpgrade': True|False,
        'BrokerArn': 'string',
        'BrokerId': 'string',
        'BrokerInstances': [
            {
                'ConsoleURL': 'string',
                'Endpoints': [
                    'string',
                ],
                'IpAddress': 'string'
            },
        ],
        'BrokerName': 'string',
        'BrokerState': 'CREATION_IN_PROGRESS'|'CREATION_FAILED'|'DELETION_IN_PROGRESS'|'RUNNING'|'REBOOT_IN_PROGRESS',
        'Configurations': {
            'Current': {
                'Id': 'string',
                'Revision': 123
            },
            'History': [
                {
                    'Id': 'string',
                    'Revision': 123
                },
            ],
            'Pending': {
                'Id': 'string',
                'Revision': 123
            }
        },
        'Created': datetime(2015, 1, 1),
        'DeploymentMode': 'SINGLE_INSTANCE'|'ACTIVE_STANDBY_MULTI_AZ',
        'EngineType': 'ACTIVEMQ',
        'EngineVersion': 'string',
        'HostInstanceType': 'string',
        'Logs': {
            'Audit': True|False,
            'AuditLogGroup': 'string',
            'General': True|False,
            'GeneralLogGroup': 'string',
            'Pending': {
                'Audit': True|False,
                'General': True|False
            }
        },
        'MaintenanceWindowStartTime': {
            'DayOfWeek': 'MONDAY'|'TUESDAY'|'WEDNESDAY'|'THURSDAY'|'FRIDAY'|'SATURDAY'|'SUNDAY',
            'TimeOfDay': 'string',
            'TimeZone': 'string'
        },
        'PendingEngineVersion': 'string',
        'PubliclyAccessible': True|False,
        'SecurityGroups': [
            'string',
        ],
        'SubnetIds': [
            'string',
        ],
        'Tags': {
            'string': 'string'
        },
        'Users': [
            {
                'PendingChange': 'CREATE'|'UPDATE'|'DELETE',
                'Username': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_configuration(ConfigurationId=None):
    """
    Returns information about the specified configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_configuration(
        ConfigurationId='string'
    )
    
    
    :type ConfigurationId: string
    :param ConfigurationId: [REQUIRED] The unique ID that Amazon MQ generates for the configuration.

    :rtype: dict
    :return: {
        'Arn': 'string',
        'Created': datetime(2015, 1, 1),
        'Description': 'string',
        'EngineType': 'ACTIVEMQ',
        'EngineVersion': 'string',
        'Id': 'string',
        'LatestRevision': {
            'Created': datetime(2015, 1, 1),
            'Description': 'string',
            'Revision': 123
        },
        'Name': 'string',
        'Tags': {
            'string': 'string'
        }
    }
    
    
    """
    pass

def describe_configuration_revision(ConfigurationId=None, ConfigurationRevision=None):
    """
    Returns the specified configuration revision for the specified configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_configuration_revision(
        ConfigurationId='string',
        ConfigurationRevision='string'
    )
    
    
    :type ConfigurationId: string
    :param ConfigurationId: [REQUIRED] The unique ID that Amazon MQ generates for the configuration.

    :type ConfigurationRevision: string
    :param ConfigurationRevision: [REQUIRED] The revision of the configuration.

    :rtype: dict
    :return: {
        'ConfigurationId': 'string',
        'Created': datetime(2015, 1, 1),
        'Data': 'string',
        'Description': 'string'
    }
    
    
    :returns: 
    (dict) -- HTTP Status Code 200: OK.
    ConfigurationId (string) -- Required. The unique ID that Amazon MQ generates for the configuration.
    Created (datetime) -- Required. The date and time of the configuration.
    Data (string) -- Required. The base64-encoded XML configuration.
    Description (string) -- The description of the configuration.
    
    
    
    """
    pass

def describe_user(BrokerId=None, Username=None):
    """
    Returns information about an ActiveMQ user.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_user(
        BrokerId='string',
        Username='string'
    )
    
    
    :type BrokerId: string
    :param BrokerId: [REQUIRED] The unique ID that Amazon MQ generates for the broker.

    :type Username: string
    :param Username: [REQUIRED] The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.

    :rtype: dict
    :return: {
        'BrokerId': 'string',
        'ConsoleAccess': True|False,
        'Groups': [
            'string',
        ],
        'Pending': {
            'ConsoleAccess': True|False,
            'Groups': [
                'string',
            ],
            'PendingChange': 'CREATE'|'UPDATE'|'DELETE'
        },
        'Username': 'string'
    }
    
    
    :returns: 
    (dict) -- HTTP Status Code 200: OK.
    BrokerId (string) -- Required. The unique ID that Amazon MQ generates for the broker.
    ConsoleAccess (boolean) -- Enables access to the the ActiveMQ Web Console for the ActiveMQ user.
    Groups (list) -- The list of groups (20 maximum) to which the ActiveMQ user belongs. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.
    (string) --
    
    
    Pending (dict) -- The status of the changes pending for the ActiveMQ user.
    ConsoleAccess (boolean) -- Enables access to the the ActiveMQ Web Console for the ActiveMQ user.
    Groups (list) -- The list of groups (20 maximum) to which the ActiveMQ user belongs. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.
    (string) --
    
    
    PendingChange (string) -- Required. The type of change pending for the ActiveMQ user.
    
    
    Username (string) -- Required. The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.
    
    
    
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

def list_brokers(MaxResults=None, NextToken=None):
    """
    Returns a list of all brokers.
    See also: AWS API Documentation
    
    
    :example: response = client.list_brokers(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.

    :type NextToken: string
    :param NextToken: The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.

    :rtype: dict
    :return: {
        'BrokerSummaries': [
            {
                'BrokerArn': 'string',
                'BrokerId': 'string',
                'BrokerName': 'string',
                'BrokerState': 'CREATION_IN_PROGRESS'|'CREATION_FAILED'|'DELETION_IN_PROGRESS'|'RUNNING'|'REBOOT_IN_PROGRESS',
                'Created': datetime(2015, 1, 1),
                'DeploymentMode': 'SINGLE_INSTANCE'|'ACTIVE_STANDBY_MULTI_AZ',
                'HostInstanceType': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (dict) -- HTTP Status Code 200: OK.
    BrokerSummaries (list) -- A list of information about all brokers.
    (dict) -- The Amazon Resource Name (ARN) of the broker.
    BrokerArn (string) -- The Amazon Resource Name (ARN) of the broker.
    BrokerId (string) -- The unique ID that Amazon MQ generates for the broker.
    BrokerName (string) -- The name of the broker. This value must be unique in your AWS account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain whitespaces, brackets, wildcard characters, or special characters.
    BrokerState (string) -- The status of the broker.
    Created (datetime) -- The time when the broker was created.
    DeploymentMode (string) -- Required. The deployment mode of the broker.
    HostInstanceType (string) -- The broker's instance type.
    
    
    
    
    NextToken (string) -- The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.
    
    
    
    """
    pass

def list_configuration_revisions(ConfigurationId=None, MaxResults=None, NextToken=None):
    """
    Returns a list of all revisions for the specified configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.list_configuration_revisions(
        ConfigurationId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ConfigurationId: string
    :param ConfigurationId: [REQUIRED] The unique ID that Amazon MQ generates for the configuration.

    :type MaxResults: integer
    :param MaxResults: The maximum number of configurations that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.

    :type NextToken: string
    :param NextToken: The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.

    :rtype: dict
    :return: {
        'ConfigurationId': 'string',
        'MaxResults': 123,
        'NextToken': 'string',
        'Revisions': [
            {
                'Created': datetime(2015, 1, 1),
                'Description': 'string',
                'Revision': 123
            },
        ]
    }
    
    
    :returns: 
    (dict) -- HTTP Status Code 200: OK.
    ConfigurationId (string) -- The unique ID that Amazon MQ generates for the configuration.
    MaxResults (integer) -- The maximum number of configuration revisions that can be returned per page (20 by default). This value must be an integer from 5 to 100.
    NextToken (string) -- The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.
    Revisions (list) -- The list of all revisions for the specified configuration.
    (dict) -- Returns information about the specified configuration revision.
    Created (datetime) -- Required. The date and time of the configuration revision.
    Description (string) -- The description of the configuration revision.
    Revision (integer) -- Required. The revision number of the configuration.
    
    
    
    
    
    
    
    """
    pass

def list_configurations(MaxResults=None, NextToken=None):
    """
    Returns a list of all configurations.
    See also: AWS API Documentation
    
    
    :example: response = client.list_configurations(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of configurations that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.

    :type NextToken: string
    :param NextToken: The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.

    :rtype: dict
    :return: {
        'Configurations': [
            {
                'Arn': 'string',
                'Created': datetime(2015, 1, 1),
                'Description': 'string',
                'EngineType': 'ACTIVEMQ',
                'EngineVersion': 'string',
                'Id': 'string',
                'LatestRevision': {
                    'Created': datetime(2015, 1, 1),
                    'Description': 'string',
                    'Revision': 123
                },
                'Name': 'string',
                'Tags': {
                    'string': 'string'
                }
            },
        ],
        'MaxResults': 123,
        'NextToken': 'string'
    }
    
    
    :returns: 
    (dict) -- HTTP Status Code 200: OK.
    Configurations (list) -- The list of all revisions for the specified configuration.
    (dict) -- Returns information about all configurations.
    Arn (string) -- Required. The ARN of the configuration.
    Created (datetime) -- Required. The date and time of the configuration revision.
    Description (string) -- Required. The description of the configuration.
    EngineType (string) -- Required. The type of broker engine. Note: Currently, Amazon MQ supports only ACTIVEMQ.
    EngineVersion (string) -- Required. The version of the broker engine. For a list of supported engine versions, see https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html
    Id (string) -- Required. The unique ID that Amazon MQ generates for the configuration.
    LatestRevision (dict) -- Required. The latest revision of the configuration.
    Created (datetime) -- Required. The date and time of the configuration revision.
    Description (string) -- The description of the configuration revision.
    Revision (integer) -- Required. The revision number of the configuration.
    
    
    Name (string) -- Required. The name of the configuration. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 1-150 characters long.
    Tags (dict) -- The list of all tags associated with this configuration.
    (string) --
    (string) --
    
    
    
    
    
    
    
    
    MaxResults (integer) -- The maximum number of configurations that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.
    NextToken (string) -- The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.
    
    
    
    """
    pass

def list_tags(ResourceArn=None):
    """
    Lists tags for a resource.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED] the Amazon Resource Name (ARN)

    :rtype: dict
    :return: {
        'Tags': {
            'string': 'string'
        }
    }
    
    
    """
    pass

def list_users(BrokerId=None, MaxResults=None, NextToken=None):
    """
    Returns a list of all ActiveMQ users.
    See also: AWS API Documentation
    
    
    :example: response = client.list_users(
        BrokerId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type BrokerId: string
    :param BrokerId: [REQUIRED] The unique ID that Amazon MQ generates for the broker.

    :type MaxResults: integer
    :param MaxResults: The maximum number of ActiveMQ users that can be returned per page (20 by default). This value must be an integer from 5 to 100.

    :type NextToken: string
    :param NextToken: The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.

    :rtype: dict
    :return: {
        'BrokerId': 'string',
        'MaxResults': 123,
        'NextToken': 'string',
        'Users': [
            {
                'PendingChange': 'CREATE'|'UPDATE'|'DELETE',
                'Username': 'string'
            },
        ]
    }
    
    
    :returns: 
    (dict) -- HTTP Status Code 200: OK.
    BrokerId (string) -- Required. The unique ID that Amazon MQ generates for the broker.
    MaxResults (integer) -- Required. The maximum number of ActiveMQ users that can be returned per page (20 by default). This value must be an integer from 5 to 100.
    NextToken (string) -- The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.
    Users (list) -- Required. The list of all ActiveMQ usernames for the specified broker.
    (dict) -- Returns a list of all ActiveMQ users.
    PendingChange (string) -- The type of change pending for the ActiveMQ user.
    Username (string) -- Required. The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.
    
    
    
    
    
    
    
    """
    pass

def reboot_broker(BrokerId=None):
    """
    Reboots a broker. Note: This API is asynchronous.
    See also: AWS API Documentation
    
    
    :example: response = client.reboot_broker(
        BrokerId='string'
    )
    
    
    :type BrokerId: string
    :param BrokerId: [REQUIRED] The unique ID that Amazon MQ generates for the broker.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def update_broker(AutoMinorVersionUpgrade=None, BrokerId=None, Configuration=None, EngineVersion=None, Logs=None):
    """
    Adds a pending configuration change to a broker.
    See also: AWS API Documentation
    
    
    :example: response = client.update_broker(
        AutoMinorVersionUpgrade=True|False,
        BrokerId='string',
        Configuration={
            'Id': 'string',
            'Revision': 123
        },
        EngineVersion='string',
        Logs={
            'Audit': True|False,
            'General': True|False
        }
    )
    
    
    :type AutoMinorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions. The automatic upgrades occur during the maintenance window of the broker or after a manual broker reboot.

    :type BrokerId: string
    :param BrokerId: [REQUIRED] The name of the broker. This value must be unique in your AWS account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain whitespaces, brackets, wildcard characters, or special characters.

    :type Configuration: dict
    :param Configuration: A list of information about the configuration.
            Id (string) -- Required. The unique ID that Amazon MQ generates for the configuration.
            Revision (integer) -- The revision number of the configuration.
            

    :type EngineVersion: string
    :param EngineVersion: The version of the broker engine. For a list of supported engine versions, see https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html

    :type Logs: dict
    :param Logs: Enables Amazon CloudWatch logging for brokers.
            Audit (boolean) -- Enables audit logging. Every user management action made using JMX or the ActiveMQ Web Console is logged.
            General (boolean) -- Enables general logging.
            

    :rtype: dict
    :return: {
        'AutoMinorVersionUpgrade': True|False,
        'BrokerId': 'string',
        'Configuration': {
            'Id': 'string',
            'Revision': 123
        },
        'EngineVersion': 'string',
        'Logs': {
            'Audit': True|False,
            'General': True|False
        }
    }
    
    
    :returns: 
    (dict) -- HTTP Status Code 200: OK.
    AutoMinorVersionUpgrade (boolean) -- The new value of automatic upgrades to new minor version for brokers.
    BrokerId (string) -- Required. The unique ID that Amazon MQ generates for the broker.
    Configuration (dict) -- The ID of the updated configuration.
    Id (string) -- Required. The unique ID that Amazon MQ generates for the configuration.
    Revision (integer) -- The revision number of the configuration.
    
    
    EngineVersion (string) -- The version of the broker engine to upgrade to. For a list of supported engine versions, see https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html
    Logs (dict) -- The list of information about logs to be enabled for the specified broker.
    Audit (boolean) -- Enables audit logging. Every user management action made using JMX or the ActiveMQ Web Console is logged.
    General (boolean) -- Enables general logging.
    
    
    
    
    
    """
    pass

def update_configuration(ConfigurationId=None, Data=None, Description=None):
    """
    Updates the specified configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.update_configuration(
        ConfigurationId='string',
        Data='string',
        Description='string'
    )
    
    
    :type ConfigurationId: string
    :param ConfigurationId: [REQUIRED] The unique ID that Amazon MQ generates for the configuration.

    :type Data: string
    :param Data: Required. The base64-encoded XML configuration.

    :type Description: string
    :param Description: The description of the configuration.

    :rtype: dict
    :return: {
        'Arn': 'string',
        'Created': datetime(2015, 1, 1),
        'Id': 'string',
        'LatestRevision': {
            'Created': datetime(2015, 1, 1),
            'Description': 'string',
            'Revision': 123
        },
        'Name': 'string',
        'Warnings': [
            {
                'AttributeName': 'string',
                'ElementName': 'string',
                'Reason': 'DISALLOWED_ELEMENT_REMOVED'|'DISALLOWED_ATTRIBUTE_REMOVED'|'INVALID_ATTRIBUTE_VALUE_REMOVED'
            },
        ]
    }
    
    
    :returns: 
    (dict) -- HTTP Status Code 200: OK.
    Arn (string) -- Required. The Amazon Resource Name (ARN) of the configuration.
    Created (datetime) -- Required. The date and time of the configuration.
    Id (string) -- Required. The unique ID that Amazon MQ generates for the configuration.
    LatestRevision (dict) -- The latest revision of the configuration.
    Created (datetime) -- Required. The date and time of the configuration revision.
    Description (string) -- The description of the configuration revision.
    Revision (integer) -- Required. The revision number of the configuration.
    
    
    Name (string) -- Required. The name of the configuration. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 1-150 characters long.
    Warnings (list) -- The list of the first 20 warnings about the configuration XML elements or attributes that were sanitized.
    (dict) -- Returns information about the XML element or attribute that was sanitized in the configuration.
    AttributeName (string) -- The name of the XML attribute that has been sanitized.
    ElementName (string) -- The name of the XML element that has been sanitized.
    Reason (string) -- Required. The reason for which the XML elements or attributes were sanitized.
    
    
    
    
    
    
    
    """
    pass

def update_user(BrokerId=None, ConsoleAccess=None, Groups=None, Password=None, Username=None):
    """
    Updates the information for an ActiveMQ user.
    See also: AWS API Documentation
    
    
    :example: response = client.update_user(
        BrokerId='string',
        ConsoleAccess=True|False,
        Groups=[
            'string',
        ],
        Password='string',
        Username='string'
    )
    
    
    :type BrokerId: string
    :param BrokerId: [REQUIRED] The unique ID that Amazon MQ generates for the broker.

    :type ConsoleAccess: boolean
    :param ConsoleAccess: Enables access to the the ActiveMQ Web Console for the ActiveMQ user.

    :type Groups: list
    :param Groups: The list of groups (20 maximum) to which the ActiveMQ user belongs. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.
            (string) --
            

    :type Password: string
    :param Password: The password of the user. This value must be at least 12 characters long, must contain at least 4 unique characters, and must not contain commas.

    :type Username: string
    :param Username: [REQUIRED] Required. The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) -- HTTP Status Code 200: OK.
    
    """
    pass

