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

def add_tags_to_resource(ResourceArn=None, Tags=None):
    """
    Adds metadata tags to an AWS DMS resource, including replication instance, endpoint, security group, and migration task. These tags can also be used with cost allocation reporting to track cost associated with DMS resources, or used in a Condition statement in an IAM policy for DMS.
    See also: AWS API Documentation
    
    
    :example: response = client.add_tags_to_resource(
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
            The Amazon Resource Name (ARN) of the AWS DMS resource the tag is to be added to. AWS DMS resources include a replication instance, endpoint, and a replication task.
            

    :type Tags: list
    :param Tags: [REQUIRED]
            The tag to be assigned to the DMS resource.
            (dict) --
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
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

def create_endpoint(EndpointIdentifier=None, EndpointType=None, EngineName=None, Username=None, Password=None, ServerName=None, Port=None, DatabaseName=None, ExtraConnectionAttributes=None, KmsKeyId=None, Tags=None, CertificateArn=None, SslMode=None, ServiceAccessRoleArn=None, ExternalTableDefinition=None, DynamoDbSettings=None, S3Settings=None, DmsTransferSettings=None, MongoDbSettings=None, KinesisSettings=None, ElasticsearchSettings=None):
    """
    Creates an endpoint using the provided settings.
    See also: AWS API Documentation
    
    
    :example: response = client.create_endpoint(
        EndpointIdentifier='string',
        EndpointType='source'|'target',
        EngineName='string',
        Username='string',
        Password='string',
        ServerName='string',
        Port=123,
        DatabaseName='string',
        ExtraConnectionAttributes='string',
        KmsKeyId='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        CertificateArn='string',
        SslMode='none'|'require'|'verify-ca'|'verify-full',
        ServiceAccessRoleArn='string',
        ExternalTableDefinition='string',
        DynamoDbSettings={
            'ServiceAccessRoleArn': 'string'
        },
        S3Settings={
            'ServiceAccessRoleArn': 'string',
            'ExternalTableDefinition': 'string',
            'CsvRowDelimiter': 'string',
            'CsvDelimiter': 'string',
            'BucketFolder': 'string',
            'BucketName': 'string',
            'CompressionType': 'none'|'gzip'
        },
        DmsTransferSettings={
            'ServiceAccessRoleArn': 'string',
            'BucketName': 'string'
        },
        MongoDbSettings={
            'Username': 'string',
            'Password': 'string',
            'ServerName': 'string',
            'Port': 123,
            'DatabaseName': 'string',
            'AuthType': 'no'|'password',
            'AuthMechanism': 'default'|'mongodb_cr'|'scram_sha_1',
            'NestingLevel': 'none'|'one',
            'ExtractDocId': 'string',
            'DocsToInvestigate': 'string',
            'AuthSource': 'string',
            'KmsKeyId': 'string'
        },
        KinesisSettings={
            'StreamArn': 'string',
            'MessageFormat': 'json',
            'ServiceAccessRoleArn': 'string'
        },
        ElasticsearchSettings={
            'ServiceAccessRoleArn': 'string',
            'EndpointUri': 'string',
            'FullLoadErrorPercentage': 123,
            'ErrorRetryDuration': 123
        }
    )
    
    
    :type EndpointIdentifier: string
    :param EndpointIdentifier: [REQUIRED]
            The database endpoint identifier. Identifiers must begin with a letter; must contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two consecutive hyphens.
            

    :type EndpointType: string
    :param EndpointType: [REQUIRED]
            The type of endpoint.
            

    :type EngineName: string
    :param EngineName: [REQUIRED]
            The type of engine for the endpoint. Valid values, depending on the EndPointType value, include mysql , oracle , postgres , mariadb , aurora , aurora-postgresql , redshift , s3 , db2 , azuredb , sybase , dynamodb , mongodb , and sqlserver .
            

    :type Username: string
    :param Username: The user name to be used to log in to the endpoint database.

    :type Password: string
    :param Password: The password to be used to log in to the endpoint database.

    :type ServerName: string
    :param ServerName: The name of the server where the endpoint database resides.

    :type Port: integer
    :param Port: The port used by the endpoint database.

    :type DatabaseName: string
    :param DatabaseName: The name of the endpoint database.

    :type ExtraConnectionAttributes: string
    :param ExtraConnectionAttributes: Additional attributes associated with the connection.

    :type KmsKeyId: string
    :param KmsKeyId: The AWS KMS key identifier to use to encrypt the connection parameters. If you don't specify a value for the KmsKeyId parameter, then AWS DMS uses your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.

    :type Tags: list
    :param Tags: Tags to be added to the endpoint.
            (dict) --
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            

    :type CertificateArn: string
    :param CertificateArn: The Amazon Resource Name (ARN) for the certificate.

    :type SslMode: string
    :param SslMode: The Secure Sockets Layer (SSL) mode to use for the SSL connection. The SSL mode can be one of four values: none , require , verify-ca , verify-full . The default value is none .

    :type ServiceAccessRoleArn: string
    :param ServiceAccessRoleArn: The Amazon Resource Name (ARN) for the service access role that you want to use to create the endpoint.

    :type ExternalTableDefinition: string
    :param ExternalTableDefinition: The external table definition.

    :type DynamoDbSettings: dict
    :param DynamoDbSettings: Settings in JSON format for the target Amazon DynamoDB endpoint. For more information about the available settings, see Using Object Mapping to Migrate Data to DynamoDB in the AWS Database Migration Service User Guide.
            ServiceAccessRoleArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) used by the service access IAM role.
            

    :type S3Settings: dict
    :param S3Settings: Settings in JSON format for the target Amazon S3 endpoint. For more information about the available settings, see Extra Connection Attributes When Using Amazon S3 as a Target for AWS DMS in the AWS Database Migration Service User Guide.
            ServiceAccessRoleArn (string) --The Amazon Resource Name (ARN) used by the service access IAM role.
            ExternalTableDefinition (string) --The external table definition.
            CsvRowDelimiter (string) --The delimiter used to separate rows in the source files. The default is a carriage return (n).
            CsvDelimiter (string) --The delimiter used to separate columns in the source files. The default is a comma.
            BucketFolder (string) --An optional parameter to set a folder name in the S3 bucket. If provided, tables are created in the path <bucketFolder>/<schema_name>/<table_name>/. If this parameter is not specified, then the path used is <schema_name>/<table_name>/.
            BucketName (string) --The name of the S3 bucket.
            CompressionType (string) --An optional parameter to use GZIP to compress the target files. Set to GZIP to compress the target files. Set to NONE (the default) or do not use to leave the files uncompressed.
            

    :type DmsTransferSettings: dict
    :param DmsTransferSettings: The settings in JSON format for the DMS transfer type of source endpoint.
            Possible attributes include the following:
            serviceAccessRoleArn - The IAM role that has permission to access the Amazon S3 bucket.
            bucketName - The name of the S3 bucket to use.
            compressionType - An optional parameter to use GZIP to compress the target files. To use GZIP, set this value to NONE (the default). To keep the files uncompressed, don't use this value.
            Shorthand syntax for these attributes is as follows: ServiceAccessRoleArn=string,BucketName=string,CompressionType=string
            JSON syntax for these attributes is as follows: { 'ServiceAccessRoleArn': 'string', 'BucketName': 'string', 'CompressionType': 'none'|'gzip' }
            ServiceAccessRoleArn (string) --The IAM role that has permission to access the Amazon S3 bucket.
            BucketName (string) --The name of the S3 bucket to use.
            

    :type MongoDbSettings: dict
    :param MongoDbSettings: Settings in JSON format for the source MongoDB endpoint. For more information about the available settings, see the configuration properties section in Using MongoDB as a Target for AWS Database Migration Service in the AWS Database Migration Service User Guide.
            Username (string) --The user name you use to access the MongoDB source endpoint.
            Password (string) --The password for the user account you use to access the MongoDB source endpoint.
            ServerName (string) --The name of the server on the MongoDB source endpoint.
            Port (integer) --The port value for the MongoDB source endpoint.
            DatabaseName (string) --The database name on the MongoDB source endpoint.
            AuthType (string) --The authentication type you use to access the MongoDB source endpoint.
            Valid values: NO, PASSWORD
            When NO is selected, user name and password parameters are not used and can be empty.
            AuthMechanism (string) --The authentication mechanism you use to access the MongoDB source endpoint.
            Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1
            DEFAULT   For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use SCRAM_SHA_1. This attribute is not used when authType=No.
            NestingLevel (string) --Specifies either document or table mode.
            Valid values: NONE, ONE
            Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.
            ExtractDocId (string) --Specifies the document ID. Use this attribute when NestingLevel is set to NONE.
            Default value is false.
            DocsToInvestigate (string) --Indicates the number of documents to preview to determine the document organization. Use this attribute when NestingLevel is set to ONE.
            Must be a positive value greater than 0. Default value is 1000.
            AuthSource (string) --The MongoDB database name. This attribute is not used when authType=NO .
            The default is admin.
            KmsKeyId (string) --The AWS KMS key identifier that is used to encrypt the content on the replication instance. If you don't specify a value for the KmsKeyId parameter, then AWS DMS uses your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.
            

    :type KinesisSettings: dict
    :param KinesisSettings: Settings in JSON format for the target Amazon Kinesis Data Streams endpoint. For more information about the available settings, see `Using Object Mapping to Migrate Data to a Kinesis Data Stream <http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kinesis.html#CHAP_Target.Kinesis.ObjectMapping >`__ in the AWS Database Migration User Guide.
            StreamArn (string) --The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.
            MessageFormat (string) --The output format for the records created on the endpoint. The message format is JSON .
            ServiceAccessRoleArn (string) --The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Amazon Kinesis data stream.
            

    :type ElasticsearchSettings: dict
    :param ElasticsearchSettings: Settings in JSON format for the target Elasticsearch endpoint. For more information about the available settings, see Extra Connection Attributes When Using Elasticsearch as a Target for AWS DMS in the AWS Database Migration User Guide.
            ServiceAccessRoleArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) used by service to access the IAM role.
            EndpointUri (string) -- [REQUIRED]The endpoint for the ElasticSearch cluster.
            FullLoadErrorPercentage (integer) --The maximum percentage of records that can fail to be written before a full load operation stops.
            ErrorRetryDuration (integer) --The maximum number of seconds that DMS retries failed API requests to the Elasticsearch cluster.
            

    :rtype: dict
    :return: {
        'Endpoint': {
            'EndpointIdentifier': 'string',
            'EndpointType': 'source'|'target',
            'EngineName': 'string',
            'EngineDisplayName': 'string',
            'Username': 'string',
            'ServerName': 'string',
            'Port': 123,
            'DatabaseName': 'string',
            'ExtraConnectionAttributes': 'string',
            'Status': 'string',
            'KmsKeyId': 'string',
            'EndpointArn': 'string',
            'CertificateArn': 'string',
            'SslMode': 'none'|'require'|'verify-ca'|'verify-full',
            'ServiceAccessRoleArn': 'string',
            'ExternalTableDefinition': 'string',
            'ExternalId': 'string',
            'DynamoDbSettings': {
                'ServiceAccessRoleArn': 'string'
            },
            'S3Settings': {
                'ServiceAccessRoleArn': 'string',
                'ExternalTableDefinition': 'string',
                'CsvRowDelimiter': 'string',
                'CsvDelimiter': 'string',
                'BucketFolder': 'string',
                'BucketName': 'string',
                'CompressionType': 'none'|'gzip'
            },
            'DmsTransferSettings': {
                'ServiceAccessRoleArn': 'string',
                'BucketName': 'string'
            },
            'MongoDbSettings': {
                'Username': 'string',
                'Password': 'string',
                'ServerName': 'string',
                'Port': 123,
                'DatabaseName': 'string',
                'AuthType': 'no'|'password',
                'AuthMechanism': 'default'|'mongodb_cr'|'scram_sha_1',
                'NestingLevel': 'none'|'one',
                'ExtractDocId': 'string',
                'DocsToInvestigate': 'string',
                'AuthSource': 'string',
                'KmsKeyId': 'string'
            },
            'KinesisSettings': {
                'StreamArn': 'string',
                'MessageFormat': 'json',
                'ServiceAccessRoleArn': 'string'
            },
            'ElasticsearchSettings': {
                'ServiceAccessRoleArn': 'string',
                'EndpointUri': 'string',
                'FullLoadErrorPercentage': 123,
                'ErrorRetryDuration': 123
            }
        }
    }
    
    
    :returns: 
    serviceAccessRoleArn - The IAM role that has permission to access the Amazon S3 bucket.
    bucketName - The name of the S3 bucket to use.
    compressionType - An optional parameter to use GZIP to compress the target files. To use GZIP, set this value to NONE (the default). To keep the files uncompressed, don't use this value.
    
    """
    pass

def create_event_subscription(SubscriptionName=None, SnsTopicArn=None, SourceType=None, EventCategories=None, SourceIds=None, Enabled=None, Tags=None):
    """
    Creates an AWS DMS event notification subscription.
    You can specify the type of source (SourceType ) you want to be notified of, provide a list of AWS DMS source IDs (SourceIds ) that triggers the events, and provide a list of event categories (EventCategories ) for events you want to be notified of. If you specify both the SourceType and SourceIds , such as SourceType = replication-instance and SourceIdentifier = my-replinstance , you will be notified of all the replication instance events for the specified source. If you specify a SourceType but don't specify a SourceIdentifier , you receive notice of the events for that source type for all your AWS DMS sources. If you don't specify either SourceType nor SourceIdentifier , you will be notified of events generated from all AWS DMS sources belonging to your customer account.
    For more information about AWS DMS events, see Working with Events and Notifications in the AWS Database Migration Service User Guide.
    See also: AWS API Documentation
    
    
    :example: response = client.create_event_subscription(
        SubscriptionName='string',
        SnsTopicArn='string',
        SourceType='string',
        EventCategories=[
            'string',
        ],
        SourceIds=[
            'string',
        ],
        Enabled=True|False,
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type SubscriptionName: string
    :param SubscriptionName: [REQUIRED]
            The name of the AWS DMS event notification subscription.
            Constraints: The name must be less than 255 characters.
            

    :type SnsTopicArn: string
    :param SnsTopicArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the Amazon SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.
            

    :type SourceType: string
    :param SourceType: The type of AWS DMS resource that generates the events. For example, if you want to be notified of events generated by a replication instance, you set this parameter to replication-instance . If this value is not specified, all events are returned.
            Valid values: replication-instance | migration-task
            

    :type EventCategories: list
    :param EventCategories: A list of event categories for a source type that you want to subscribe to. You can see a list of the categories for a given source type by calling the DescribeEventCategories action or in the topic Working with Events and Notifications in the AWS Database Migration Service User Guide.
            (string) --
            

    :type SourceIds: list
    :param SourceIds: The list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens; it cannot end with a hyphen or contain two consecutive hyphens.
            (string) --
            

    :type Enabled: boolean
    :param Enabled: A Boolean value; set to true to activate the subscription, or set to false to create the subscription but not activate it.

    :type Tags: list
    :param Tags: A tag to be attached to the event subscription.
            (dict) --
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            

    :rtype: dict
    :return: {
        'EventSubscription': {
            'CustomerAwsId': 'string',
            'CustSubscriptionId': 'string',
            'SnsTopicArn': 'string',
            'Status': 'string',
            'SubscriptionCreationTime': 'string',
            'SourceType': 'string',
            'SourceIdsList': [
                'string',
            ],
            'EventCategoriesList': [
                'string',
            ],
            'Enabled': True|False
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_replication_instance(ReplicationInstanceIdentifier=None, AllocatedStorage=None, ReplicationInstanceClass=None, VpcSecurityGroupIds=None, AvailabilityZone=None, ReplicationSubnetGroupIdentifier=None, PreferredMaintenanceWindow=None, MultiAZ=None, EngineVersion=None, AutoMinorVersionUpgrade=None, Tags=None, KmsKeyId=None, PubliclyAccessible=None, DnsNameServers=None):
    """
    Creates the replication instance using the specified parameters.
    See also: AWS API Documentation
    
    
    :example: response = client.create_replication_instance(
        ReplicationInstanceIdentifier='string',
        AllocatedStorage=123,
        ReplicationInstanceClass='string',
        VpcSecurityGroupIds=[
            'string',
        ],
        AvailabilityZone='string',
        ReplicationSubnetGroupIdentifier='string',
        PreferredMaintenanceWindow='string',
        MultiAZ=True|False,
        EngineVersion='string',
        AutoMinorVersionUpgrade=True|False,
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        KmsKeyId='string',
        PubliclyAccessible=True|False,
        DnsNameServers='string'
    )
    
    
    :type ReplicationInstanceIdentifier: string
    :param ReplicationInstanceIdentifier: [REQUIRED]
            The replication instance identifier. This parameter is stored as a lowercase string.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Example: myrepinstance
            

    :type AllocatedStorage: integer
    :param AllocatedStorage: The amount of storage (in gigabytes) to be initially allocated for the replication instance.

    :type ReplicationInstanceClass: string
    :param ReplicationInstanceClass: [REQUIRED]
            The compute and memory capacity of the replication instance as specified by the replication instance class.
            Valid Values: dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge
            

    :type VpcSecurityGroupIds: list
    :param VpcSecurityGroupIds: Specifies the VPC security group to be used with the replication instance. The VPC security group must work with the VPC containing the replication instance.
            (string) --
            

    :type AvailabilityZone: string
    :param AvailabilityZone: The EC2 Availability Zone that the replication instance will be created in.
            Default: A random, system-chosen Availability Zone in the endpoint's region.
            Example: us-east-1d
            

    :type ReplicationSubnetGroupIdentifier: string
    :param ReplicationSubnetGroupIdentifier: A subnet group to associate with the replication instance.

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
            Format: ddd:hh24:mi-ddd:hh24:mi
            Default: A 30-minute window selected at random from an 8-hour block of time per region, occurring on a random day of the week.
            Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun
            Constraints: Minimum 30-minute window.
            

    :type MultiAZ: boolean
    :param MultiAZ: Specifies if the replication instance is a Multi-AZ deployment. You cannot set the AvailabilityZone parameter if the Multi-AZ parameter is set to true .

    :type EngineVersion: string
    :param EngineVersion: The engine version number of the replication instance.

    :type AutoMinorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: Indicates that minor engine upgrades will be applied automatically to the replication instance during the maintenance window.
            Default: true
            

    :type Tags: list
    :param Tags: Tags to be associated with the replication instance.
            (dict) --
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            

    :type KmsKeyId: string
    :param KmsKeyId: The AWS KMS key identifier that is used to encrypt the content on the replication instance. If you don't specify a value for the KmsKeyId parameter, then AWS DMS uses your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.

    :type PubliclyAccessible: boolean
    :param PubliclyAccessible: Specifies the accessibility options for the replication instance. A value of true represents an instance with a public IP address. A value of false represents an instance with a private IP address. The default value is true .

    :type DnsNameServers: string
    :param DnsNameServers: A list of DNS name servers supported for the replication instance.

    :rtype: dict
    :return: {
        'ReplicationInstance': {
            'ReplicationInstanceIdentifier': 'string',
            'ReplicationInstanceClass': 'string',
            'ReplicationInstanceStatus': 'string',
            'AllocatedStorage': 123,
            'InstanceCreateTime': datetime(2015, 1, 1),
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'AvailabilityZone': 'string',
            'ReplicationSubnetGroup': {
                'ReplicationSubnetGroupIdentifier': 'string',
                'ReplicationSubnetGroupDescription': 'string',
                'VpcId': 'string',
                'SubnetGroupStatus': 'string',
                'Subnets': [
                    {
                        'SubnetIdentifier': 'string',
                        'SubnetAvailabilityZone': {
                            'Name': 'string'
                        },
                        'SubnetStatus': 'string'
                    },
                ]
            },
            'PreferredMaintenanceWindow': 'string',
            'PendingModifiedValues': {
                'ReplicationInstanceClass': 'string',
                'AllocatedStorage': 123,
                'MultiAZ': True|False,
                'EngineVersion': 'string'
            },
            'MultiAZ': True|False,
            'EngineVersion': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'KmsKeyId': 'string',
            'ReplicationInstanceArn': 'string',
            'ReplicationInstancePublicIpAddress': 'string',
            'ReplicationInstancePrivateIpAddress': 'string',
            'ReplicationInstancePublicIpAddresses': [
                'string',
            ],
            'ReplicationInstancePrivateIpAddresses': [
                'string',
            ],
            'PubliclyAccessible': True|False,
            'SecondaryAvailabilityZone': 'string',
            'FreeUntil': datetime(2015, 1, 1),
            'DnsNameServers': 'string'
        }
    }
    
    
    :returns: 
    Must contain from 1 to 63 alphanumeric characters or hyphens.
    First character must be a letter.
    Cannot end with a hyphen or contain two consecutive hyphens.
    
    """
    pass

def create_replication_subnet_group(ReplicationSubnetGroupIdentifier=None, ReplicationSubnetGroupDescription=None, SubnetIds=None, Tags=None):
    """
    Creates a replication subnet group given a list of the subnet IDs in a VPC.
    See also: AWS API Documentation
    
    
    :example: response = client.create_replication_subnet_group(
        ReplicationSubnetGroupIdentifier='string',
        ReplicationSubnetGroupDescription='string',
        SubnetIds=[
            'string',
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ReplicationSubnetGroupIdentifier: string
    :param ReplicationSubnetGroupIdentifier: [REQUIRED]
            The name for the replication subnet group. This value is stored as a lowercase string.
            Constraints: Must contain no more than 255 alphanumeric characters, periods, spaces, underscores, or hyphens. Must not be 'default'.
            Example: mySubnetgroup
            

    :type ReplicationSubnetGroupDescription: string
    :param ReplicationSubnetGroupDescription: [REQUIRED]
            The description for the subnet group.
            

    :type SubnetIds: list
    :param SubnetIds: [REQUIRED]
            The EC2 subnet IDs for the subnet group.
            (string) --
            

    :type Tags: list
    :param Tags: The tag to be assigned to the subnet group.
            (dict) --
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            

    :rtype: dict
    :return: {
        'ReplicationSubnetGroup': {
            'ReplicationSubnetGroupIdentifier': 'string',
            'ReplicationSubnetGroupDescription': 'string',
            'VpcId': 'string',
            'SubnetGroupStatus': 'string',
            'Subnets': [
                {
                    'SubnetIdentifier': 'string',
                    'SubnetAvailabilityZone': {
                        'Name': 'string'
                    },
                    'SubnetStatus': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def create_replication_task(ReplicationTaskIdentifier=None, SourceEndpointArn=None, TargetEndpointArn=None, ReplicationInstanceArn=None, MigrationType=None, TableMappings=None, ReplicationTaskSettings=None, CdcStartTime=None, CdcStartPosition=None, CdcStopPosition=None, Tags=None):
    """
    Creates a replication task using the specified parameters.
    See also: AWS API Documentation
    
    
    :example: response = client.create_replication_task(
        ReplicationTaskIdentifier='string',
        SourceEndpointArn='string',
        TargetEndpointArn='string',
        ReplicationInstanceArn='string',
        MigrationType='full-load'|'cdc'|'full-load-and-cdc',
        TableMappings='string',
        ReplicationTaskSettings='string',
        CdcStartTime=datetime(2015, 1, 1),
        CdcStartPosition='string',
        CdcStopPosition='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ReplicationTaskIdentifier: string
    :param ReplicationTaskIdentifier: [REQUIRED]
            The replication task identifier.
            Constraints:
            Must contain from 1 to 255 alphanumeric characters or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            

    :type SourceEndpointArn: string
    :param SourceEndpointArn: [REQUIRED]
            The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
            

    :type TargetEndpointArn: string
    :param TargetEndpointArn: [REQUIRED]
            The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
            

    :type ReplicationInstanceArn: string
    :param ReplicationInstanceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the replication instance.
            

    :type MigrationType: string
    :param MigrationType: [REQUIRED]
            The migration type.
            

    :type TableMappings: string
    :param TableMappings: [REQUIRED]
            When using the AWS CLI or boto3, provide the path of the JSON file that contains the table mappings. Precede the path with 'file://'. When working with the DMS API, provide the JSON as the parameter value.
            For example, --table-mappings file://mappingfile.json
            

    :type ReplicationTaskSettings: string
    :param ReplicationTaskSettings: Settings for the task, such as target metadata settings. For a complete list of task settings, see Task Settings for AWS Database Migration Service Tasks in the AWS Database Migration User Guide.

    :type CdcStartTime: datetime
    :param CdcStartTime: Indicates the start time for a change data capture (CDC) operation. Use either CdcStartTime or CdcStartPosition to specify when you want a CDC operation to start. Specifying both values results in an error.
            Timestamp Example: --cdc-start-time  2018-03-08T12:12:12 
            

    :type CdcStartPosition: string
    :param CdcStartPosition: Indicates when you want a change data capture (CDC) operation to start. Use either CdcStartPosition or CdcStartTime to specify when you want a CDC operation to start. Specifying both values results in an error.
            The value can be in date, checkpoint, or LSN/SCN format.
            Date Example: --cdc-start-position  2018-03-08T12:12:12 
            Checkpoint Example: --cdc-start-position 'checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93'
            LSN Example: --cdc-start-position  mysql-bin-changelog.000024:373 
            

    :type CdcStopPosition: string
    :param CdcStopPosition: Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.
            Server time example: --cdc-stop-position  server_time:3018-02-09T12:12:12 
            Commit time example: --cdc-stop-position  commit_time: 3018-02-09T12:12:12  
            

    :type Tags: list
    :param Tags: Tags to be added to the replication instance.
            (dict) --
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            

    :rtype: dict
    :return: {
        'ReplicationTask': {
            'ReplicationTaskIdentifier': 'string',
            'SourceEndpointArn': 'string',
            'TargetEndpointArn': 'string',
            'ReplicationInstanceArn': 'string',
            'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
            'TableMappings': 'string',
            'ReplicationTaskSettings': 'string',
            'Status': 'string',
            'LastFailureMessage': 'string',
            'StopReason': 'string',
            'ReplicationTaskCreationDate': datetime(2015, 1, 1),
            'ReplicationTaskStartDate': datetime(2015, 1, 1),
            'CdcStartPosition': 'string',
            'CdcStopPosition': 'string',
            'RecoveryCheckpoint': 'string',
            'ReplicationTaskArn': 'string',
            'ReplicationTaskStats': {
                'FullLoadProgressPercent': 123,
                'ElapsedTimeMillis': 123,
                'TablesLoaded': 123,
                'TablesLoading': 123,
                'TablesQueued': 123,
                'TablesErrored': 123
            }
        }
    }
    
    
    :returns: 
    Must contain from 1 to 255 alphanumeric characters or hyphens.
    First character must be a letter.
    Cannot end with a hyphen or contain two consecutive hyphens.
    
    """
    pass

def delete_certificate(CertificateArn=None):
    """
    Deletes the specified certificate.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_certificate(
        CertificateArn='string'
    )
    
    
    :type CertificateArn: string
    :param CertificateArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the deleted certificate.
            

    :rtype: dict
    :return: {
        'Certificate': {
            'CertificateIdentifier': 'string',
            'CertificateCreationDate': datetime(2015, 1, 1),
            'CertificatePem': 'string',
            'CertificateWallet': b'bytes',
            'CertificateArn': 'string',
            'CertificateOwner': 'string',
            'ValidFromDate': datetime(2015, 1, 1),
            'ValidToDate': datetime(2015, 1, 1),
            'SigningAlgorithm': 'string',
            'KeyLength': 123
        }
    }
    
    
    """
    pass

def delete_endpoint(EndpointArn=None):
    """
    Deletes the specified endpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_endpoint(
        EndpointArn='string'
    )
    
    
    :type EndpointArn: string
    :param EndpointArn: [REQUIRED]
            The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
            

    :rtype: dict
    :return: {
        'Endpoint': {
            'EndpointIdentifier': 'string',
            'EndpointType': 'source'|'target',
            'EngineName': 'string',
            'EngineDisplayName': 'string',
            'Username': 'string',
            'ServerName': 'string',
            'Port': 123,
            'DatabaseName': 'string',
            'ExtraConnectionAttributes': 'string',
            'Status': 'string',
            'KmsKeyId': 'string',
            'EndpointArn': 'string',
            'CertificateArn': 'string',
            'SslMode': 'none'|'require'|'verify-ca'|'verify-full',
            'ServiceAccessRoleArn': 'string',
            'ExternalTableDefinition': 'string',
            'ExternalId': 'string',
            'DynamoDbSettings': {
                'ServiceAccessRoleArn': 'string'
            },
            'S3Settings': {
                'ServiceAccessRoleArn': 'string',
                'ExternalTableDefinition': 'string',
                'CsvRowDelimiter': 'string',
                'CsvDelimiter': 'string',
                'BucketFolder': 'string',
                'BucketName': 'string',
                'CompressionType': 'none'|'gzip'
            },
            'DmsTransferSettings': {
                'ServiceAccessRoleArn': 'string',
                'BucketName': 'string'
            },
            'MongoDbSettings': {
                'Username': 'string',
                'Password': 'string',
                'ServerName': 'string',
                'Port': 123,
                'DatabaseName': 'string',
                'AuthType': 'no'|'password',
                'AuthMechanism': 'default'|'mongodb_cr'|'scram_sha_1',
                'NestingLevel': 'none'|'one',
                'ExtractDocId': 'string',
                'DocsToInvestigate': 'string',
                'AuthSource': 'string',
                'KmsKeyId': 'string'
            },
            'KinesisSettings': {
                'StreamArn': 'string',
                'MessageFormat': 'json',
                'ServiceAccessRoleArn': 'string'
            },
            'ElasticsearchSettings': {
                'ServiceAccessRoleArn': 'string',
                'EndpointUri': 'string',
                'FullLoadErrorPercentage': 123,
                'ErrorRetryDuration': 123
            }
        }
    }
    
    
    """
    pass

def delete_event_subscription(SubscriptionName=None):
    """
    Deletes an AWS DMS event subscription.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_event_subscription(
        SubscriptionName='string'
    )
    
    
    :type SubscriptionName: string
    :param SubscriptionName: [REQUIRED]
            The name of the DMS event notification subscription to be deleted.
            

    :rtype: dict
    :return: {
        'EventSubscription': {
            'CustomerAwsId': 'string',
            'CustSubscriptionId': 'string',
            'SnsTopicArn': 'string',
            'Status': 'string',
            'SubscriptionCreationTime': 'string',
            'SourceType': 'string',
            'SourceIdsList': [
                'string',
            ],
            'EventCategoriesList': [
                'string',
            ],
            'Enabled': True|False
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_replication_instance(ReplicationInstanceArn=None):
    """
    Deletes the specified replication instance.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_replication_instance(
        ReplicationInstanceArn='string'
    )
    
    
    :type ReplicationInstanceArn: string
    :param ReplicationInstanceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the replication instance to be deleted.
            

    :rtype: dict
    :return: {
        'ReplicationInstance': {
            'ReplicationInstanceIdentifier': 'string',
            'ReplicationInstanceClass': 'string',
            'ReplicationInstanceStatus': 'string',
            'AllocatedStorage': 123,
            'InstanceCreateTime': datetime(2015, 1, 1),
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'AvailabilityZone': 'string',
            'ReplicationSubnetGroup': {
                'ReplicationSubnetGroupIdentifier': 'string',
                'ReplicationSubnetGroupDescription': 'string',
                'VpcId': 'string',
                'SubnetGroupStatus': 'string',
                'Subnets': [
                    {
                        'SubnetIdentifier': 'string',
                        'SubnetAvailabilityZone': {
                            'Name': 'string'
                        },
                        'SubnetStatus': 'string'
                    },
                ]
            },
            'PreferredMaintenanceWindow': 'string',
            'PendingModifiedValues': {
                'ReplicationInstanceClass': 'string',
                'AllocatedStorage': 123,
                'MultiAZ': True|False,
                'EngineVersion': 'string'
            },
            'MultiAZ': True|False,
            'EngineVersion': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'KmsKeyId': 'string',
            'ReplicationInstanceArn': 'string',
            'ReplicationInstancePublicIpAddress': 'string',
            'ReplicationInstancePrivateIpAddress': 'string',
            'ReplicationInstancePublicIpAddresses': [
                'string',
            ],
            'ReplicationInstancePrivateIpAddresses': [
                'string',
            ],
            'PubliclyAccessible': True|False,
            'SecondaryAvailabilityZone': 'string',
            'FreeUntil': datetime(2015, 1, 1),
            'DnsNameServers': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_replication_subnet_group(ReplicationSubnetGroupIdentifier=None):
    """
    Deletes a subnet group.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_replication_subnet_group(
        ReplicationSubnetGroupIdentifier='string'
    )
    
    
    :type ReplicationSubnetGroupIdentifier: string
    :param ReplicationSubnetGroupIdentifier: [REQUIRED]
            The subnet group name of the replication instance.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_replication_task(ReplicationTaskArn=None):
    """
    Deletes the specified replication task.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_replication_task(
        ReplicationTaskArn='string'
    )
    
    
    :type ReplicationTaskArn: string
    :param ReplicationTaskArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the replication task to be deleted.
            

    :rtype: dict
    :return: {
        'ReplicationTask': {
            'ReplicationTaskIdentifier': 'string',
            'SourceEndpointArn': 'string',
            'TargetEndpointArn': 'string',
            'ReplicationInstanceArn': 'string',
            'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
            'TableMappings': 'string',
            'ReplicationTaskSettings': 'string',
            'Status': 'string',
            'LastFailureMessage': 'string',
            'StopReason': 'string',
            'ReplicationTaskCreationDate': datetime(2015, 1, 1),
            'ReplicationTaskStartDate': datetime(2015, 1, 1),
            'CdcStartPosition': 'string',
            'CdcStopPosition': 'string',
            'RecoveryCheckpoint': 'string',
            'ReplicationTaskArn': 'string',
            'ReplicationTaskStats': {
                'FullLoadProgressPercent': 123,
                'ElapsedTimeMillis': 123,
                'TablesLoaded': 123,
                'TablesLoading': 123,
                'TablesQueued': 123,
                'TablesErrored': 123
            }
        }
    }
    
    
    """
    pass

def describe_account_attributes():
    """
    Lists all of the AWS DMS attributes for a customer account. The attributes include AWS DMS quotas for the account, such as the number of replication instances allowed. The description for a quota includes the quota name, current usage toward that quota, and the quota's maximum value.
    This command does not take any parameters.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_account_attributes()
    
    
    :rtype: dict
    :return: {
        'AccountQuotas': [
            {
                'AccountQuotaName': 'string',
                'Used': 123,
                'Max': 123
            },
        ]
    }
    
    
    """
    pass

def describe_certificates(Filters=None, MaxRecords=None, Marker=None):
    """
    Provides a description of the certificate.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_certificates(
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type Filters: list
    :param Filters: Filters applied to the certificate described in the form of key-value pairs.
            (dict) --
            Name (string) -- [REQUIRED]The name of the filter.
            Values (list) -- [REQUIRED]The filter value.
            (string) --
            
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 10
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
    :return: {
        'Marker': 'string',
        'Certificates': [
            {
                'CertificateIdentifier': 'string',
                'CertificateCreationDate': datetime(2015, 1, 1),
                'CertificatePem': 'string',
                'CertificateWallet': b'bytes',
                'CertificateArn': 'string',
                'CertificateOwner': 'string',
                'ValidFromDate': datetime(2015, 1, 1),
                'ValidToDate': datetime(2015, 1, 1),
                'SigningAlgorithm': 'string',
                'KeyLength': 123
            },
        ]
    }
    
    
    """
    pass

def describe_connections(Filters=None, MaxRecords=None, Marker=None):
    """
    Describes the status of the connections that have been made between the replication instance and an endpoint. Connections are created when you test an endpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_connections(
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type Filters: list
    :param Filters: The filters applied to the connection.
            Valid filter names: endpoint-arn | replication-instance-arn
            (dict) --
            Name (string) -- [REQUIRED]The name of the filter.
            Values (list) -- [REQUIRED]The filter value.
            (string) --
            
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
    :return: {
        'Marker': 'string',
        'Connections': [
            {
                'ReplicationInstanceArn': 'string',
                'EndpointArn': 'string',
                'Status': 'string',
                'LastFailureMessage': 'string',
                'EndpointIdentifier': 'string',
                'ReplicationInstanceIdentifier': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_endpoint_types(Filters=None, MaxRecords=None, Marker=None):
    """
    Returns information about the type of endpoints available.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_endpoint_types(
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type Filters: list
    :param Filters: Filters applied to the describe action.
            Valid filter names: engine-name | endpoint-type
            (dict) --
            Name (string) -- [REQUIRED]The name of the filter.
            Values (list) -- [REQUIRED]The filter value.
            (string) --
            
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
    :return: {
        'Marker': 'string',
        'SupportedEndpointTypes': [
            {
                'EngineName': 'string',
                'SupportsCDC': True|False,
                'EndpointType': 'source'|'target',
                'EngineDisplayName': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_endpoints(Filters=None, MaxRecords=None, Marker=None):
    """
    Returns information about the endpoints for your account in the current region.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_endpoints(
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type Filters: list
    :param Filters: Filters applied to the describe action.
            Valid filter names: endpoint-arn | endpoint-type | endpoint-id | engine-name
            (dict) --
            Name (string) -- [REQUIRED]The name of the filter.
            Values (list) -- [REQUIRED]The filter value.
            (string) --
            
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
    :return: {
        'Marker': 'string',
        'Endpoints': [
            {
                'EndpointIdentifier': 'string',
                'EndpointType': 'source'|'target',
                'EngineName': 'string',
                'EngineDisplayName': 'string',
                'Username': 'string',
                'ServerName': 'string',
                'Port': 123,
                'DatabaseName': 'string',
                'ExtraConnectionAttributes': 'string',
                'Status': 'string',
                'KmsKeyId': 'string',
                'EndpointArn': 'string',
                'CertificateArn': 'string',
                'SslMode': 'none'|'require'|'verify-ca'|'verify-full',
                'ServiceAccessRoleArn': 'string',
                'ExternalTableDefinition': 'string',
                'ExternalId': 'string',
                'DynamoDbSettings': {
                    'ServiceAccessRoleArn': 'string'
                },
                'S3Settings': {
                    'ServiceAccessRoleArn': 'string',
                    'ExternalTableDefinition': 'string',
                    'CsvRowDelimiter': 'string',
                    'CsvDelimiter': 'string',
                    'BucketFolder': 'string',
                    'BucketName': 'string',
                    'CompressionType': 'none'|'gzip'
                },
                'DmsTransferSettings': {
                    'ServiceAccessRoleArn': 'string',
                    'BucketName': 'string'
                },
                'MongoDbSettings': {
                    'Username': 'string',
                    'Password': 'string',
                    'ServerName': 'string',
                    'Port': 123,
                    'DatabaseName': 'string',
                    'AuthType': 'no'|'password',
                    'AuthMechanism': 'default'|'mongodb_cr'|'scram_sha_1',
                    'NestingLevel': 'none'|'one',
                    'ExtractDocId': 'string',
                    'DocsToInvestigate': 'string',
                    'AuthSource': 'string',
                    'KmsKeyId': 'string'
                },
                'KinesisSettings': {
                    'StreamArn': 'string',
                    'MessageFormat': 'json',
                    'ServiceAccessRoleArn': 'string'
                },
                'ElasticsearchSettings': {
                    'ServiceAccessRoleArn': 'string',
                    'EndpointUri': 'string',
                    'FullLoadErrorPercentage': 123,
                    'ErrorRetryDuration': 123
                }
            },
        ]
    }
    
    
    :returns: 
    serviceAccessRoleArn - The IAM role that has permission to access the Amazon S3 bucket.
    bucketName - The name of the S3 bucket to use.
    compressionType - An optional parameter to use GZIP to compress the target files. To use GZIP, set this value to NONE (the default). To keep the files uncompressed, don't use this value.
    
    """
    pass

def describe_event_categories(SourceType=None, Filters=None):
    """
    Lists categories for all event source types, or, if specified, for a specified source type. You can see a list of the event categories and source types in Working with Events and Notifications in the AWS Database Migration Service User Guide.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_event_categories(
        SourceType='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type SourceType: string
    :param SourceType: The type of AWS DMS resource that generates events.
            Valid values: replication-instance | migration-task
            

    :type Filters: list
    :param Filters: Filters applied to the action.
            (dict) --
            Name (string) -- [REQUIRED]The name of the filter.
            Values (list) -- [REQUIRED]The filter value.
            (string) --
            
            

    :rtype: dict
    :return: {
        'EventCategoryGroupList': [
            {
                'SourceType': 'string',
                'EventCategories': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_event_subscriptions(SubscriptionName=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Lists all the event subscriptions for a customer account. The description of a subscription includes SubscriptionName , SNSTopicARN , CustomerID , SourceType , SourceID , CreationTime , and Status .
    If you specify SubscriptionName , this action lists the description for that subscription.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_event_subscriptions(
        SubscriptionName='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type SubscriptionName: string
    :param SubscriptionName: The name of the AWS DMS event subscription to be described.

    :type Filters: list
    :param Filters: Filters applied to the action.
            (dict) --
            Name (string) -- [REQUIRED]The name of the filter.
            Values (list) -- [REQUIRED]The filter value.
            (string) --
            
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
    :return: {
        'Marker': 'string',
        'EventSubscriptionsList': [
            {
                'CustomerAwsId': 'string',
                'CustSubscriptionId': 'string',
                'SnsTopicArn': 'string',
                'Status': 'string',
                'SubscriptionCreationTime': 'string',
                'SourceType': 'string',
                'SourceIdsList': [
                    'string',
                ],
                'EventCategoriesList': [
                    'string',
                ],
                'Enabled': True|False
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_events(SourceIdentifier=None, SourceType=None, StartTime=None, EndTime=None, Duration=None, EventCategories=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Lists events for a given source identifier and source type. You can also specify a start and end time. For more information on AWS DMS events, see Working with Events and Notifications in the AWS Database Migration User Guide.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_events(
        SourceIdentifier='string',
        SourceType='replication-instance',
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        Duration=123,
        EventCategories=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type SourceIdentifier: string
    :param SourceIdentifier: The identifier of the event source. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens. It cannot end with a hyphen or contain two consecutive hyphens.

    :type SourceType: string
    :param SourceType: The type of AWS DMS resource that generates events.
            Valid values: replication-instance | migration-task
            

    :type StartTime: datetime
    :param StartTime: The start time for the events to be listed.

    :type EndTime: datetime
    :param EndTime: The end time for the events to be listed.

    :type Duration: integer
    :param Duration: The duration of the events to be listed.

    :type EventCategories: list
    :param EventCategories: A list of event categories for a source type that you want to subscribe to.
            (string) --
            

    :type Filters: list
    :param Filters: Filters applied to the action.
            (dict) --
            Name (string) -- [REQUIRED]The name of the filter.
            Values (list) -- [REQUIRED]The filter value.
            (string) --
            
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
    :return: {
        'Marker': 'string',
        'Events': [
            {
                'SourceIdentifier': 'string',
                'SourceType': 'replication-instance',
                'Message': 'string',
                'EventCategories': [
                    'string',
                ],
                'Date': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_orderable_replication_instances(MaxRecords=None, Marker=None):
    """
    Returns information about the replication instance types that can be created in the specified region.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_orderable_replication_instances(
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
    :return: {
        'OrderableReplicationInstances': [
            {
                'EngineVersion': 'string',
                'ReplicationInstanceClass': 'string',
                'StorageType': 'string',
                'MinAllocatedStorage': 123,
                'MaxAllocatedStorage': 123,
                'DefaultAllocatedStorage': 123,
                'IncludedAllocatedStorage': 123
            },
        ],
        'Marker': 'string'
    }
    
    
    """
    pass

def describe_refresh_schemas_status(EndpointArn=None):
    """
    Returns the status of the RefreshSchemas operation.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_refresh_schemas_status(
        EndpointArn='string'
    )
    
    
    :type EndpointArn: string
    :param EndpointArn: [REQUIRED]
            The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
            

    :rtype: dict
    :return: {
        'RefreshSchemasStatus': {
            'EndpointArn': 'string',
            'ReplicationInstanceArn': 'string',
            'Status': 'successful'|'failed'|'refreshing',
            'LastRefreshDate': datetime(2015, 1, 1),
            'LastFailureMessage': 'string'
        }
    }
    
    
    """
    pass

def describe_replication_instance_task_logs(ReplicationInstanceArn=None, MaxRecords=None, Marker=None):
    """
    Returns information about the task logs for the specified task.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_replication_instance_task_logs(
        ReplicationInstanceArn='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type ReplicationInstanceArn: string
    :param ReplicationInstanceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the replication instance.
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
    :return: {
        'ReplicationInstanceArn': 'string',
        'ReplicationInstanceTaskLogs': [
            {
                'ReplicationTaskName': 'string',
                'ReplicationTaskArn': 'string',
                'ReplicationInstanceTaskLogSize': 123
            },
        ],
        'Marker': 'string'
    }
    
    
    """
    pass

def describe_replication_instances(Filters=None, MaxRecords=None, Marker=None):
    """
    Returns information about replication instances for your account in the current region.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_replication_instances(
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type Filters: list
    :param Filters: Filters applied to the describe action.
            Valid filter names: replication-instance-arn | replication-instance-id | replication-instance-class | engine-version
            (dict) --
            Name (string) -- [REQUIRED]The name of the filter.
            Values (list) -- [REQUIRED]The filter value.
            (string) --
            
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
    :return: {
        'Marker': 'string',
        'ReplicationInstances': [
            {
                'ReplicationInstanceIdentifier': 'string',
                'ReplicationInstanceClass': 'string',
                'ReplicationInstanceStatus': 'string',
                'AllocatedStorage': 123,
                'InstanceCreateTime': datetime(2015, 1, 1),
                'VpcSecurityGroups': [
                    {
                        'VpcSecurityGroupId': 'string',
                        'Status': 'string'
                    },
                ],
                'AvailabilityZone': 'string',
                'ReplicationSubnetGroup': {
                    'ReplicationSubnetGroupIdentifier': 'string',
                    'ReplicationSubnetGroupDescription': 'string',
                    'VpcId': 'string',
                    'SubnetGroupStatus': 'string',
                    'Subnets': [
                        {
                            'SubnetIdentifier': 'string',
                            'SubnetAvailabilityZone': {
                                'Name': 'string'
                            },
                            'SubnetStatus': 'string'
                        },
                    ]
                },
                'PreferredMaintenanceWindow': 'string',
                'PendingModifiedValues': {
                    'ReplicationInstanceClass': 'string',
                    'AllocatedStorage': 123,
                    'MultiAZ': True|False,
                    'EngineVersion': 'string'
                },
                'MultiAZ': True|False,
                'EngineVersion': 'string',
                'AutoMinorVersionUpgrade': True|False,
                'KmsKeyId': 'string',
                'ReplicationInstanceArn': 'string',
                'ReplicationInstancePublicIpAddress': 'string',
                'ReplicationInstancePrivateIpAddress': 'string',
                'ReplicationInstancePublicIpAddresses': [
                    'string',
                ],
                'ReplicationInstancePrivateIpAddresses': [
                    'string',
                ],
                'PubliclyAccessible': True|False,
                'SecondaryAvailabilityZone': 'string',
                'FreeUntil': datetime(2015, 1, 1),
                'DnsNameServers': 'string'
            },
        ]
    }
    
    
    :returns: 
    Must contain from 1 to 63 alphanumeric characters or hyphens.
    First character must be a letter.
    Cannot end with a hyphen or contain two consecutive hyphens.
    
    """
    pass

def describe_replication_subnet_groups(Filters=None, MaxRecords=None, Marker=None):
    """
    Returns information about the replication subnet groups.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_replication_subnet_groups(
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type Filters: list
    :param Filters: Filters applied to the describe action.
            (dict) --
            Name (string) -- [REQUIRED]The name of the filter.
            Values (list) -- [REQUIRED]The filter value.
            (string) --
            
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
    :return: {
        'Marker': 'string',
        'ReplicationSubnetGroups': [
            {
                'ReplicationSubnetGroupIdentifier': 'string',
                'ReplicationSubnetGroupDescription': 'string',
                'VpcId': 'string',
                'SubnetGroupStatus': 'string',
                'Subnets': [
                    {
                        'SubnetIdentifier': 'string',
                        'SubnetAvailabilityZone': {
                            'Name': 'string'
                        },
                        'SubnetStatus': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def describe_replication_task_assessment_results(ReplicationTaskArn=None, MaxRecords=None, Marker=None):
    """
    Returns the task assessment results from Amazon S3. This action always returns the latest results.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_replication_task_assessment_results(
        ReplicationTaskArn='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type ReplicationTaskArn: string
    :param ReplicationTaskArn: 
            The Amazon Resource Name (ARN) string that uniquely identifies the task. When this input parameter is specified the API will return only one result and ignore the values of the max-records and marker parameters.
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
    :return: {
        'Marker': 'string',
        'BucketName': 'string',
        'ReplicationTaskAssessmentResults': [
            {
                'ReplicationTaskIdentifier': 'string',
                'ReplicationTaskArn': 'string',
                'ReplicationTaskLastAssessmentDate': datetime(2015, 1, 1),
                'AssessmentStatus': 'string',
                'AssessmentResultsFile': 'string',
                'AssessmentResults': 'string',
                'S3ObjectUrl': 'string'
            },
        ]
    }
    
    
    :returns: 
    The Amazon S3 bucket where the task assessment report is located.
    
    """
    pass

def describe_replication_tasks(Filters=None, MaxRecords=None, Marker=None):
    """
    Returns information about replication tasks for your account in the current region.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_replication_tasks(
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type Filters: list
    :param Filters: Filters applied to the describe action.
            Valid filter names: replication-task-arn | replication-task-id | migration-type | endpoint-arn | replication-instance-arn
            (dict) --
            Name (string) -- [REQUIRED]The name of the filter.
            Values (list) -- [REQUIRED]The filter value.
            (string) --
            
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
    :return: {
        'Marker': 'string',
        'ReplicationTasks': [
            {
                'ReplicationTaskIdentifier': 'string',
                'SourceEndpointArn': 'string',
                'TargetEndpointArn': 'string',
                'ReplicationInstanceArn': 'string',
                'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
                'TableMappings': 'string',
                'ReplicationTaskSettings': 'string',
                'Status': 'string',
                'LastFailureMessage': 'string',
                'StopReason': 'string',
                'ReplicationTaskCreationDate': datetime(2015, 1, 1),
                'ReplicationTaskStartDate': datetime(2015, 1, 1),
                'CdcStartPosition': 'string',
                'CdcStopPosition': 'string',
                'RecoveryCheckpoint': 'string',
                'ReplicationTaskArn': 'string',
                'ReplicationTaskStats': {
                    'FullLoadProgressPercent': 123,
                    'ElapsedTimeMillis': 123,
                    'TablesLoaded': 123,
                    'TablesLoading': 123,
                    'TablesQueued': 123,
                    'TablesErrored': 123
                }
            },
        ]
    }
    
    
    :returns: 
    Must contain from 1 to 255 alphanumeric characters or hyphens.
    First character must be a letter.
    Cannot end with a hyphen or contain two consecutive hyphens.
    
    """
    pass

def describe_schemas(EndpointArn=None, MaxRecords=None, Marker=None):
    """
    Returns information about the schema for the specified endpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_schemas(
        EndpointArn='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type EndpointArn: string
    :param EndpointArn: [REQUIRED]
            The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
    :return: {
        'Marker': 'string',
        'Schemas': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_table_statistics(ReplicationTaskArn=None, MaxRecords=None, Marker=None, Filters=None):
    """
    Returns table statistics on the database migration task, including table name, rows inserted, rows updated, and rows deleted.
    Note that the "last updated" column the DMS console only indicates the time that AWS DMS last updated the table statistics record for a table. It does not indicate the time of the last update to the table.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_table_statistics(
        ReplicationTaskArn='string',
        MaxRecords=123,
        Marker='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type ReplicationTaskArn: string
    :param ReplicationTaskArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the replication task.
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 500.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :type Filters: list
    :param Filters: Filters applied to the describe table statistics action.
            Valid filter names: schema-name | table-name | table-state
            A combination of filters creates an AND condition where each record matches all specified filters.
            (dict) --
            Name (string) -- [REQUIRED]The name of the filter.
            Values (list) -- [REQUIRED]The filter value.
            (string) --
            
            

    :rtype: dict
    :return: {
        'ReplicationTaskArn': 'string',
        'TableStatistics': [
            {
                'SchemaName': 'string',
                'TableName': 'string',
                'Inserts': 123,
                'Deletes': 123,
                'Updates': 123,
                'Ddls': 123,
                'FullLoadRows': 123,
                'FullLoadCondtnlChkFailedRows': 123,
                'FullLoadErrorRows': 123,
                'LastUpdateTime': datetime(2015, 1, 1),
                'TableState': 'string',
                'ValidationPendingRecords': 123,
                'ValidationFailedRecords': 123,
                'ValidationSuspendedRecords': 123,
                'ValidationState': 'string',
                'ValidationStateDetails': 'string'
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    Not enabledValidation is not enabled for the table in the migration task.
    Pending recordsSome records in the table are waiting for validation.
    Mismatched recordsSome records in the table do not match between the source and target.
    Suspended recordsSome records in the table could not be validated.
    No primary keyThe table could not be validated because it had no primary key.
    Table errorThe table was not validated because it was in an error state and some data was not migrated.
    ValidatedAll rows in the table were validated. If the table is updated, the status can change from Validated.
    ErrorThe table could not be validated because of an unexpected error.
    
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

def import_certificate(CertificateIdentifier=None, CertificatePem=None, CertificateWallet=None, Tags=None):
    """
    Uploads the specified certificate.
    See also: AWS API Documentation
    
    
    :example: response = client.import_certificate(
        CertificateIdentifier='string',
        CertificatePem='string',
        CertificateWallet=b'bytes',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type CertificateIdentifier: string
    :param CertificateIdentifier: [REQUIRED]
            The customer-assigned name of the certificate. Valid characters are A-z and 0-9.
            

    :type CertificatePem: string
    :param CertificatePem: The contents of the .pem X.509 certificate file for the certificate.

    :type CertificateWallet: bytes
    :param CertificateWallet: The location of the imported Oracle Wallet certificate for use with SSL.

    :type Tags: list
    :param Tags: The tags associated with the certificate.
            (dict) --
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            

    :rtype: dict
    :return: {
        'Certificate': {
            'CertificateIdentifier': 'string',
            'CertificateCreationDate': datetime(2015, 1, 1),
            'CertificatePem': 'string',
            'CertificateWallet': b'bytes',
            'CertificateArn': 'string',
            'CertificateOwner': 'string',
            'ValidFromDate': datetime(2015, 1, 1),
            'ValidToDate': datetime(2015, 1, 1),
            'SigningAlgorithm': 'string',
            'KeyLength': 123
        }
    }
    
    
    """
    pass

def list_tags_for_resource(ResourceArn=None):
    """
    Lists all tags for an AWS DMS resource.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) string that uniquely identifies the AWS DMS resource.
            

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

def modify_endpoint(EndpointArn=None, EndpointIdentifier=None, EndpointType=None, EngineName=None, Username=None, Password=None, ServerName=None, Port=None, DatabaseName=None, ExtraConnectionAttributes=None, CertificateArn=None, SslMode=None, ServiceAccessRoleArn=None, ExternalTableDefinition=None, DynamoDbSettings=None, S3Settings=None, DmsTransferSettings=None, MongoDbSettings=None, KinesisSettings=None, ElasticsearchSettings=None):
    """
    Modifies the specified endpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_endpoint(
        EndpointArn='string',
        EndpointIdentifier='string',
        EndpointType='source'|'target',
        EngineName='string',
        Username='string',
        Password='string',
        ServerName='string',
        Port=123,
        DatabaseName='string',
        ExtraConnectionAttributes='string',
        CertificateArn='string',
        SslMode='none'|'require'|'verify-ca'|'verify-full',
        ServiceAccessRoleArn='string',
        ExternalTableDefinition='string',
        DynamoDbSettings={
            'ServiceAccessRoleArn': 'string'
        },
        S3Settings={
            'ServiceAccessRoleArn': 'string',
            'ExternalTableDefinition': 'string',
            'CsvRowDelimiter': 'string',
            'CsvDelimiter': 'string',
            'BucketFolder': 'string',
            'BucketName': 'string',
            'CompressionType': 'none'|'gzip'
        },
        DmsTransferSettings={
            'ServiceAccessRoleArn': 'string',
            'BucketName': 'string'
        },
        MongoDbSettings={
            'Username': 'string',
            'Password': 'string',
            'ServerName': 'string',
            'Port': 123,
            'DatabaseName': 'string',
            'AuthType': 'no'|'password',
            'AuthMechanism': 'default'|'mongodb_cr'|'scram_sha_1',
            'NestingLevel': 'none'|'one',
            'ExtractDocId': 'string',
            'DocsToInvestigate': 'string',
            'AuthSource': 'string',
            'KmsKeyId': 'string'
        },
        KinesisSettings={
            'StreamArn': 'string',
            'MessageFormat': 'json',
            'ServiceAccessRoleArn': 'string'
        },
        ElasticsearchSettings={
            'ServiceAccessRoleArn': 'string',
            'EndpointUri': 'string',
            'FullLoadErrorPercentage': 123,
            'ErrorRetryDuration': 123
        }
    )
    
    
    :type EndpointArn: string
    :param EndpointArn: [REQUIRED]
            The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
            

    :type EndpointIdentifier: string
    :param EndpointIdentifier: The database endpoint identifier. Identifiers must begin with a letter; must contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two consecutive hyphens.

    :type EndpointType: string
    :param EndpointType: The type of endpoint.

    :type EngineName: string
    :param EngineName: The type of engine for the endpoint. Valid values, depending on the EndPointType, include mysql, oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb, sybase, sybase, dynamodb, mongodb, and sqlserver.

    :type Username: string
    :param Username: The user name to be used to login to the endpoint database.

    :type Password: string
    :param Password: The password to be used to login to the endpoint database.

    :type ServerName: string
    :param ServerName: The name of the server where the endpoint database resides.

    :type Port: integer
    :param Port: The port used by the endpoint database.

    :type DatabaseName: string
    :param DatabaseName: The name of the endpoint database.

    :type ExtraConnectionAttributes: string
    :param ExtraConnectionAttributes: Additional attributes associated with the connection. To reset this parameter, pass the empty string ('') as an argument.

    :type CertificateArn: string
    :param CertificateArn: The Amazon Resource Name (ARN) of the certificate used for SSL connection.

    :type SslMode: string
    :param SslMode: The SSL mode to be used.
            SSL mode can be one of four values: none, require, verify-ca, verify-full.
            The default value is none.
            

    :type ServiceAccessRoleArn: string
    :param ServiceAccessRoleArn: The Amazon Resource Name (ARN) for the service access role you want to use to modify the endpoint.

    :type ExternalTableDefinition: string
    :param ExternalTableDefinition: The external table definition.

    :type DynamoDbSettings: dict
    :param DynamoDbSettings: Settings in JSON format for the target Amazon DynamoDB endpoint. For more information about the available settings, see Using Object Mapping to Migrate Data to DynamoDB in the AWS Database Migration Service User Guide.
            ServiceAccessRoleArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) used by the service access IAM role.
            

    :type S3Settings: dict
    :param S3Settings: Settings in JSON format for the target Amazon S3 endpoint. For more information about the available settings, see Extra Connection Attributes When Using Amazon S3 as a Target for AWS DMS in the AWS Database Migration Service User Guide.
            ServiceAccessRoleArn (string) --The Amazon Resource Name (ARN) used by the service access IAM role.
            ExternalTableDefinition (string) --The external table definition.
            CsvRowDelimiter (string) --The delimiter used to separate rows in the source files. The default is a carriage return (n).
            CsvDelimiter (string) --The delimiter used to separate columns in the source files. The default is a comma.
            BucketFolder (string) --An optional parameter to set a folder name in the S3 bucket. If provided, tables are created in the path <bucketFolder>/<schema_name>/<table_name>/. If this parameter is not specified, then the path used is <schema_name>/<table_name>/.
            BucketName (string) --The name of the S3 bucket.
            CompressionType (string) --An optional parameter to use GZIP to compress the target files. Set to GZIP to compress the target files. Set to NONE (the default) or do not use to leave the files uncompressed.
            

    :type DmsTransferSettings: dict
    :param DmsTransferSettings: The settings in JSON format for the DMS transfer type of source endpoint.
            Attributes include the following:
            serviceAccessRoleArn - The IAM role that has permission to access the Amazon S3 bucket.
            BucketName - The name of the S3 bucket to use.
            compressionType - An optional parameter to use GZIP to compress the target files. Set to NONE (the default) or do not use to leave the files uncompressed.
            Shorthand syntax: ServiceAccessRoleArn=string ,BucketName=string,CompressionType=string
            JSON syntax:
            { 'ServiceAccessRoleArn': 'string', 'BucketName': 'string', 'CompressionType': 'none'|'gzip' }
            ServiceAccessRoleArn (string) --The IAM role that has permission to access the Amazon S3 bucket.
            BucketName (string) --The name of the S3 bucket to use.
            

    :type MongoDbSettings: dict
    :param MongoDbSettings: Settings in JSON format for the source MongoDB endpoint. For more information about the available settings, see the configuration properties section in Using MongoDB as a Target for AWS Database Migration Service in the AWS Database Migration Service User Guide.
            Username (string) --The user name you use to access the MongoDB source endpoint.
            Password (string) --The password for the user account you use to access the MongoDB source endpoint.
            ServerName (string) --The name of the server on the MongoDB source endpoint.
            Port (integer) --The port value for the MongoDB source endpoint.
            DatabaseName (string) --The database name on the MongoDB source endpoint.
            AuthType (string) --The authentication type you use to access the MongoDB source endpoint.
            Valid values: NO, PASSWORD
            When NO is selected, user name and password parameters are not used and can be empty.
            AuthMechanism (string) --The authentication mechanism you use to access the MongoDB source endpoint.
            Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1
            DEFAULT   For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use SCRAM_SHA_1. This attribute is not used when authType=No.
            NestingLevel (string) --Specifies either document or table mode.
            Valid values: NONE, ONE
            Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.
            ExtractDocId (string) --Specifies the document ID. Use this attribute when NestingLevel is set to NONE.
            Default value is false.
            DocsToInvestigate (string) --Indicates the number of documents to preview to determine the document organization. Use this attribute when NestingLevel is set to ONE.
            Must be a positive value greater than 0. Default value is 1000.
            AuthSource (string) --The MongoDB database name. This attribute is not used when authType=NO .
            The default is admin.
            KmsKeyId (string) --The AWS KMS key identifier that is used to encrypt the content on the replication instance. If you don't specify a value for the KmsKeyId parameter, then AWS DMS uses your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.
            

    :type KinesisSettings: dict
    :param KinesisSettings: Settings in JSON format for the target Amazon Kinesis Data Streams endpoint. For more information about the available settings, see `Using Object Mapping to Migrate Data to a Kinesis Data Stream <http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kinesis.html#CHAP_Target.Kinesis.ObjectMapping >`__ in the AWS Database Migration User Guide.
            StreamArn (string) --The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.
            MessageFormat (string) --The output format for the records created on the endpoint. The message format is JSON .
            ServiceAccessRoleArn (string) --The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Amazon Kinesis data stream.
            

    :type ElasticsearchSettings: dict
    :param ElasticsearchSettings: Settings in JSON format for the target Elasticsearch endpoint. For more information about the available settings, see Extra Connection Attributes When Using Elasticsearch as a Target for AWS DMS in the AWS Database Migration User Guide.
            ServiceAccessRoleArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) used by service to access the IAM role.
            EndpointUri (string) -- [REQUIRED]The endpoint for the ElasticSearch cluster.
            FullLoadErrorPercentage (integer) --The maximum percentage of records that can fail to be written before a full load operation stops.
            ErrorRetryDuration (integer) --The maximum number of seconds that DMS retries failed API requests to the Elasticsearch cluster.
            

    :rtype: dict
    :return: {
        'Endpoint': {
            'EndpointIdentifier': 'string',
            'EndpointType': 'source'|'target',
            'EngineName': 'string',
            'EngineDisplayName': 'string',
            'Username': 'string',
            'ServerName': 'string',
            'Port': 123,
            'DatabaseName': 'string',
            'ExtraConnectionAttributes': 'string',
            'Status': 'string',
            'KmsKeyId': 'string',
            'EndpointArn': 'string',
            'CertificateArn': 'string',
            'SslMode': 'none'|'require'|'verify-ca'|'verify-full',
            'ServiceAccessRoleArn': 'string',
            'ExternalTableDefinition': 'string',
            'ExternalId': 'string',
            'DynamoDbSettings': {
                'ServiceAccessRoleArn': 'string'
            },
            'S3Settings': {
                'ServiceAccessRoleArn': 'string',
                'ExternalTableDefinition': 'string',
                'CsvRowDelimiter': 'string',
                'CsvDelimiter': 'string',
                'BucketFolder': 'string',
                'BucketName': 'string',
                'CompressionType': 'none'|'gzip'
            },
            'DmsTransferSettings': {
                'ServiceAccessRoleArn': 'string',
                'BucketName': 'string'
            },
            'MongoDbSettings': {
                'Username': 'string',
                'Password': 'string',
                'ServerName': 'string',
                'Port': 123,
                'DatabaseName': 'string',
                'AuthType': 'no'|'password',
                'AuthMechanism': 'default'|'mongodb_cr'|'scram_sha_1',
                'NestingLevel': 'none'|'one',
                'ExtractDocId': 'string',
                'DocsToInvestigate': 'string',
                'AuthSource': 'string',
                'KmsKeyId': 'string'
            },
            'KinesisSettings': {
                'StreamArn': 'string',
                'MessageFormat': 'json',
                'ServiceAccessRoleArn': 'string'
            },
            'ElasticsearchSettings': {
                'ServiceAccessRoleArn': 'string',
                'EndpointUri': 'string',
                'FullLoadErrorPercentage': 123,
                'ErrorRetryDuration': 123
            }
        }
    }
    
    
    :returns: 
    serviceAccessRoleArn - The IAM role that has permission to access the Amazon S3 bucket.
    bucketName - The name of the S3 bucket to use.
    compressionType - An optional parameter to use GZIP to compress the target files. To use GZIP, set this value to NONE (the default). To keep the files uncompressed, don't use this value.
    
    """
    pass

def modify_event_subscription(SubscriptionName=None, SnsTopicArn=None, SourceType=None, EventCategories=None, Enabled=None):
    """
    Modifies an existing AWS DMS event notification subscription.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_event_subscription(
        SubscriptionName='string',
        SnsTopicArn='string',
        SourceType='string',
        EventCategories=[
            'string',
        ],
        Enabled=True|False
    )
    
    
    :type SubscriptionName: string
    :param SubscriptionName: [REQUIRED]
            The name of the AWS DMS event notification subscription to be modified.
            

    :type SnsTopicArn: string
    :param SnsTopicArn: The Amazon Resource Name (ARN) of the Amazon SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.

    :type SourceType: string
    :param SourceType: The type of AWS DMS resource that generates the events you want to subscribe to.
            Valid values: replication-instance | migration-task
            

    :type EventCategories: list
    :param EventCategories: A list of event categories for a source type that you want to subscribe to. Use the DescribeEventCategories action to see a list of event categories.
            (string) --
            

    :type Enabled: boolean
    :param Enabled: A Boolean value; set to true to activate the subscription.

    :rtype: dict
    :return: {
        'EventSubscription': {
            'CustomerAwsId': 'string',
            'CustSubscriptionId': 'string',
            'SnsTopicArn': 'string',
            'Status': 'string',
            'SubscriptionCreationTime': 'string',
            'SourceType': 'string',
            'SourceIdsList': [
                'string',
            ],
            'EventCategoriesList': [
                'string',
            ],
            'Enabled': True|False
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def modify_replication_instance(ReplicationInstanceArn=None, AllocatedStorage=None, ApplyImmediately=None, ReplicationInstanceClass=None, VpcSecurityGroupIds=None, PreferredMaintenanceWindow=None, MultiAZ=None, EngineVersion=None, AllowMajorVersionUpgrade=None, AutoMinorVersionUpgrade=None, ReplicationInstanceIdentifier=None):
    """
    Modifies the replication instance to apply new settings. You can change one or more parameters by specifying these parameters and the new values in the request.
    Some settings are applied during the maintenance window.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_replication_instance(
        ReplicationInstanceArn='string',
        AllocatedStorage=123,
        ApplyImmediately=True|False,
        ReplicationInstanceClass='string',
        VpcSecurityGroupIds=[
            'string',
        ],
        PreferredMaintenanceWindow='string',
        MultiAZ=True|False,
        EngineVersion='string',
        AllowMajorVersionUpgrade=True|False,
        AutoMinorVersionUpgrade=True|False,
        ReplicationInstanceIdentifier='string'
    )
    
    
    :type ReplicationInstanceArn: string
    :param ReplicationInstanceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the replication instance.
            

    :type AllocatedStorage: integer
    :param AllocatedStorage: The amount of storage (in gigabytes) to be allocated for the replication instance.

    :type ApplyImmediately: boolean
    :param ApplyImmediately: Indicates whether the changes should be applied immediately or during the next maintenance window.

    :type ReplicationInstanceClass: string
    :param ReplicationInstanceClass: The compute and memory capacity of the replication instance.
            Valid Values: dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge
            

    :type VpcSecurityGroupIds: list
    :param VpcSecurityGroupIds: Specifies the VPC security group to be used with the replication instance. The VPC security group must work with the VPC containing the replication instance.
            (string) --
            

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: The weekly time range (in UTC) during which system maintenance can occur, which might result in an outage. Changing this parameter does not result in an outage, except in the following situation, and the change is asynchronously applied as soon as possible. If moving this window to the current time, there must be at least 30 minutes between the current time and end of the window to ensure pending changes are applied.
            Default: Uses existing setting
            Format: ddd:hh24:mi-ddd:hh24:mi
            Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun
            Constraints: Must be at least 30 minutes
            

    :type MultiAZ: boolean
    :param MultiAZ: Specifies if the replication instance is a Multi-AZ deployment. You cannot set the AvailabilityZone parameter if the Multi-AZ parameter is set to true .

    :type EngineVersion: string
    :param EngineVersion: The engine version number of the replication instance.

    :type AllowMajorVersionUpgrade: boolean
    :param AllowMajorVersionUpgrade: Indicates that major version upgrades are allowed. Changing this parameter does not result in an outage and the change is asynchronously applied as soon as possible.
            Constraints: This parameter must be set to true when specifying a value for the EngineVersion parameter that is a different major version than the replication instance's current version.
            

    :type AutoMinorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: Indicates that minor version upgrades will be applied automatically to the replication instance during the maintenance window. Changing this parameter does not result in an outage except in the following case and the change is asynchronously applied as soon as possible. An outage will result if this parameter is set to true during the maintenance window, and a newer minor version is available, and AWS DMS has enabled auto patching for that engine version.

    :type ReplicationInstanceIdentifier: string
    :param ReplicationInstanceIdentifier: The replication instance identifier. This parameter is stored as a lowercase string.

    :rtype: dict
    :return: {
        'ReplicationInstance': {
            'ReplicationInstanceIdentifier': 'string',
            'ReplicationInstanceClass': 'string',
            'ReplicationInstanceStatus': 'string',
            'AllocatedStorage': 123,
            'InstanceCreateTime': datetime(2015, 1, 1),
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'AvailabilityZone': 'string',
            'ReplicationSubnetGroup': {
                'ReplicationSubnetGroupIdentifier': 'string',
                'ReplicationSubnetGroupDescription': 'string',
                'VpcId': 'string',
                'SubnetGroupStatus': 'string',
                'Subnets': [
                    {
                        'SubnetIdentifier': 'string',
                        'SubnetAvailabilityZone': {
                            'Name': 'string'
                        },
                        'SubnetStatus': 'string'
                    },
                ]
            },
            'PreferredMaintenanceWindow': 'string',
            'PendingModifiedValues': {
                'ReplicationInstanceClass': 'string',
                'AllocatedStorage': 123,
                'MultiAZ': True|False,
                'EngineVersion': 'string'
            },
            'MultiAZ': True|False,
            'EngineVersion': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'KmsKeyId': 'string',
            'ReplicationInstanceArn': 'string',
            'ReplicationInstancePublicIpAddress': 'string',
            'ReplicationInstancePrivateIpAddress': 'string',
            'ReplicationInstancePublicIpAddresses': [
                'string',
            ],
            'ReplicationInstancePrivateIpAddresses': [
                'string',
            ],
            'PubliclyAccessible': True|False,
            'SecondaryAvailabilityZone': 'string',
            'FreeUntil': datetime(2015, 1, 1),
            'DnsNameServers': 'string'
        }
    }
    
    
    :returns: 
    Must contain from 1 to 63 alphanumeric characters or hyphens.
    First character must be a letter.
    Cannot end with a hyphen or contain two consecutive hyphens.
    
    """
    pass

def modify_replication_subnet_group(ReplicationSubnetGroupIdentifier=None, ReplicationSubnetGroupDescription=None, SubnetIds=None):
    """
    Modifies the settings for the specified replication subnet group.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_replication_subnet_group(
        ReplicationSubnetGroupIdentifier='string',
        ReplicationSubnetGroupDescription='string',
        SubnetIds=[
            'string',
        ]
    )
    
    
    :type ReplicationSubnetGroupIdentifier: string
    :param ReplicationSubnetGroupIdentifier: [REQUIRED]
            The name of the replication instance subnet group.
            

    :type ReplicationSubnetGroupDescription: string
    :param ReplicationSubnetGroupDescription: The description of the replication instance subnet group.

    :type SubnetIds: list
    :param SubnetIds: [REQUIRED]
            A list of subnet IDs.
            (string) --
            

    :rtype: dict
    :return: {
        'ReplicationSubnetGroup': {
            'ReplicationSubnetGroupIdentifier': 'string',
            'ReplicationSubnetGroupDescription': 'string',
            'VpcId': 'string',
            'SubnetGroupStatus': 'string',
            'Subnets': [
                {
                    'SubnetIdentifier': 'string',
                    'SubnetAvailabilityZone': {
                        'Name': 'string'
                    },
                    'SubnetStatus': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def modify_replication_task(ReplicationTaskArn=None, ReplicationTaskIdentifier=None, MigrationType=None, TableMappings=None, ReplicationTaskSettings=None, CdcStartTime=None, CdcStartPosition=None, CdcStopPosition=None):
    """
    Modifies the specified replication task.
    You can't modify the task endpoints. The task must be stopped before you can modify it.
    For more information about AWS DMS tasks, see Working with Migration Tasks in the AWS Database Migration Service User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.modify_replication_task(
        ReplicationTaskArn='string',
        ReplicationTaskIdentifier='string',
        MigrationType='full-load'|'cdc'|'full-load-and-cdc',
        TableMappings='string',
        ReplicationTaskSettings='string',
        CdcStartTime=datetime(2015, 1, 1),
        CdcStartPosition='string',
        CdcStopPosition='string'
    )
    
    
    :type ReplicationTaskArn: string
    :param ReplicationTaskArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the replication task.
            

    :type ReplicationTaskIdentifier: string
    :param ReplicationTaskIdentifier: The replication task identifier.
            Constraints:
            Must contain from 1 to 255 alphanumeric characters or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            

    :type MigrationType: string
    :param MigrationType: The migration type.
            Valid values: full-load | cdc | full-load-and-cdc
            

    :type TableMappings: string
    :param TableMappings: When using the AWS CLI or boto3, provide the path of the JSON file that contains the table mappings. Precede the path with 'file://'. When working with the DMS API, provide the JSON as the parameter value.
            For example, --table-mappings file://mappingfile.json
            

    :type ReplicationTaskSettings: string
    :param ReplicationTaskSettings: JSON file that contains settings for the task, such as target metadata settings.

    :type CdcStartTime: datetime
    :param CdcStartTime: Indicates the start time for a change data capture (CDC) operation. Use either CdcStartTime or CdcStartPosition to specify when you want a CDC operation to start. Specifying both values results in an error.
            Timestamp Example: --cdc-start-time  2018-03-08T12:12:12 
            

    :type CdcStartPosition: string
    :param CdcStartPosition: Indicates when you want a change data capture (CDC) operation to start. Use either CdcStartPosition or CdcStartTime to specify when you want a CDC operation to start. Specifying both values results in an error.
            The value can be in date, checkpoint, or LSN/SCN format.
            Date Example: --cdc-start-position  2018-03-08T12:12:12 
            Checkpoint Example: --cdc-start-position 'checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93'
            LSN Example: --cdc-start-position  mysql-bin-changelog.000024:373 
            

    :type CdcStopPosition: string
    :param CdcStopPosition: Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.
            Server time example: --cdc-stop-position  server_time:3018-02-09T12:12:12 
            Commit time example: --cdc-stop-position  commit_time: 3018-02-09T12:12:12  
            

    :rtype: dict
    :return: {
        'ReplicationTask': {
            'ReplicationTaskIdentifier': 'string',
            'SourceEndpointArn': 'string',
            'TargetEndpointArn': 'string',
            'ReplicationInstanceArn': 'string',
            'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
            'TableMappings': 'string',
            'ReplicationTaskSettings': 'string',
            'Status': 'string',
            'LastFailureMessage': 'string',
            'StopReason': 'string',
            'ReplicationTaskCreationDate': datetime(2015, 1, 1),
            'ReplicationTaskStartDate': datetime(2015, 1, 1),
            'CdcStartPosition': 'string',
            'CdcStopPosition': 'string',
            'RecoveryCheckpoint': 'string',
            'ReplicationTaskArn': 'string',
            'ReplicationTaskStats': {
                'FullLoadProgressPercent': 123,
                'ElapsedTimeMillis': 123,
                'TablesLoaded': 123,
                'TablesLoading': 123,
                'TablesQueued': 123,
                'TablesErrored': 123
            }
        }
    }
    
    
    :returns: 
    Must contain from 1 to 255 alphanumeric characters or hyphens.
    First character must be a letter.
    Cannot end with a hyphen or contain two consecutive hyphens.
    
    """
    pass

def reboot_replication_instance(ReplicationInstanceArn=None, ForceFailover=None):
    """
    Reboots a replication instance. Rebooting results in a momentary outage, until the replication instance becomes available again.
    See also: AWS API Documentation
    
    
    :example: response = client.reboot_replication_instance(
        ReplicationInstanceArn='string',
        ForceFailover=True|False
    )
    
    
    :type ReplicationInstanceArn: string
    :param ReplicationInstanceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the replication instance.
            

    :type ForceFailover: boolean
    :param ForceFailover: If this parameter is true , the reboot is conducted through a Multi-AZ failover. (If the instance isn't configured for Multi-AZ, then you can't specify true .)

    :rtype: dict
    :return: {
        'ReplicationInstance': {
            'ReplicationInstanceIdentifier': 'string',
            'ReplicationInstanceClass': 'string',
            'ReplicationInstanceStatus': 'string',
            'AllocatedStorage': 123,
            'InstanceCreateTime': datetime(2015, 1, 1),
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'AvailabilityZone': 'string',
            'ReplicationSubnetGroup': {
                'ReplicationSubnetGroupIdentifier': 'string',
                'ReplicationSubnetGroupDescription': 'string',
                'VpcId': 'string',
                'SubnetGroupStatus': 'string',
                'Subnets': [
                    {
                        'SubnetIdentifier': 'string',
                        'SubnetAvailabilityZone': {
                            'Name': 'string'
                        },
                        'SubnetStatus': 'string'
                    },
                ]
            },
            'PreferredMaintenanceWindow': 'string',
            'PendingModifiedValues': {
                'ReplicationInstanceClass': 'string',
                'AllocatedStorage': 123,
                'MultiAZ': True|False,
                'EngineVersion': 'string'
            },
            'MultiAZ': True|False,
            'EngineVersion': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'KmsKeyId': 'string',
            'ReplicationInstanceArn': 'string',
            'ReplicationInstancePublicIpAddress': 'string',
            'ReplicationInstancePrivateIpAddress': 'string',
            'ReplicationInstancePublicIpAddresses': [
                'string',
            ],
            'ReplicationInstancePrivateIpAddresses': [
                'string',
            ],
            'PubliclyAccessible': True|False,
            'SecondaryAvailabilityZone': 'string',
            'FreeUntil': datetime(2015, 1, 1),
            'DnsNameServers': 'string'
        }
    }
    
    
    :returns: 
    Must contain from 1 to 63 alphanumeric characters or hyphens.
    First character must be a letter.
    Cannot end with a hyphen or contain two consecutive hyphens.
    
    """
    pass

def refresh_schemas(EndpointArn=None, ReplicationInstanceArn=None):
    """
    Populates the schema for the specified endpoint. This is an asynchronous operation and can take several minutes. You can check the status of this operation by calling the DescribeRefreshSchemasStatus operation.
    See also: AWS API Documentation
    
    
    :example: response = client.refresh_schemas(
        EndpointArn='string',
        ReplicationInstanceArn='string'
    )
    
    
    :type EndpointArn: string
    :param EndpointArn: [REQUIRED]
            The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
            

    :type ReplicationInstanceArn: string
    :param ReplicationInstanceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the replication instance.
            

    :rtype: dict
    :return: {
        'RefreshSchemasStatus': {
            'EndpointArn': 'string',
            'ReplicationInstanceArn': 'string',
            'Status': 'successful'|'failed'|'refreshing',
            'LastRefreshDate': datetime(2015, 1, 1),
            'LastFailureMessage': 'string'
        }
    }
    
    
    """
    pass

def reload_tables(ReplicationTaskArn=None, TablesToReload=None, ReloadOption=None):
    """
    Reloads the target database table with the source data.
    See also: AWS API Documentation
    
    
    :example: response = client.reload_tables(
        ReplicationTaskArn='string',
        TablesToReload=[
            {
                'SchemaName': 'string',
                'TableName': 'string'
            },
        ],
        ReloadOption='data-reload'|'validate-only'
    )
    
    
    :type ReplicationTaskArn: string
    :param ReplicationTaskArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the replication task.
            

    :type TablesToReload: list
    :param TablesToReload: [REQUIRED]
            The name and schema of the table to be reloaded.
            (dict) --
            SchemaName (string) --The schema name of the table to be reloaded.
            TableName (string) --The table name of the table to be reloaded.
            
            

    :type ReloadOption: string
    :param ReloadOption: Options for reload. Specify data-reload to reload the data and re-validate it if validation is enabled. Specify validate-only to re-validate the table. This option applies only when validation is enabled for the task.
            Valid values: data-reload, validate-only
            Default value is data-reload.
            

    :rtype: dict
    :return: {
        'ReplicationTaskArn': 'string'
    }
    
    
    """
    pass

def remove_tags_from_resource(ResourceArn=None, TagKeys=None):
    """
    Removes metadata tags from a DMS resource.
    See also: AWS API Documentation
    
    
    :example: response = client.remove_tags_from_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            >The Amazon Resource Name (ARN) of the AWS DMS resource the tag is to be removed from.
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            The tag key (name) of the tag to be removed.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def start_replication_task(ReplicationTaskArn=None, StartReplicationTaskType=None, CdcStartTime=None, CdcStartPosition=None, CdcStopPosition=None):
    """
    Starts the replication task.
    For more information about AWS DMS tasks, see Working with Migration Tasks in the AWS Database Migration Service User Guide.
    See also: AWS API Documentation
    
    
    :example: response = client.start_replication_task(
        ReplicationTaskArn='string',
        StartReplicationTaskType='start-replication'|'resume-processing'|'reload-target',
        CdcStartTime=datetime(2015, 1, 1),
        CdcStartPosition='string',
        CdcStopPosition='string'
    )
    
    
    :type ReplicationTaskArn: string
    :param ReplicationTaskArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the replication task to be started.
            

    :type StartReplicationTaskType: string
    :param StartReplicationTaskType: [REQUIRED]
            The type of replication task.
            

    :type CdcStartTime: datetime
    :param CdcStartTime: Indicates the start time for a change data capture (CDC) operation. Use either CdcStartTime or CdcStartPosition to specify when you want a CDC operation to start. Specifying both values results in an error.
            Timestamp Example: --cdc-start-time  2018-03-08T12:12:12 
            

    :type CdcStartPosition: string
    :param CdcStartPosition: Indicates when you want a change data capture (CDC) operation to start. Use either CdcStartPosition or CdcStartTime to specify when you want a CDC operation to start. Specifying both values results in an error.
            The value can be in date, checkpoint, or LSN/SCN format.
            Date Example: --cdc-start-position  2018-03-08T12:12:12 
            Checkpoint Example: --cdc-start-position 'checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93'
            LSN Example: --cdc-start-position  mysql-bin-changelog.000024:373 
            

    :type CdcStopPosition: string
    :param CdcStopPosition: Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.
            Server time example: --cdc-stop-position  server_time:3018-02-09T12:12:12 
            Commit time example: --cdc-stop-position  commit_time: 3018-02-09T12:12:12  
            

    :rtype: dict
    :return: {
        'ReplicationTask': {
            'ReplicationTaskIdentifier': 'string',
            'SourceEndpointArn': 'string',
            'TargetEndpointArn': 'string',
            'ReplicationInstanceArn': 'string',
            'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
            'TableMappings': 'string',
            'ReplicationTaskSettings': 'string',
            'Status': 'string',
            'LastFailureMessage': 'string',
            'StopReason': 'string',
            'ReplicationTaskCreationDate': datetime(2015, 1, 1),
            'ReplicationTaskStartDate': datetime(2015, 1, 1),
            'CdcStartPosition': 'string',
            'CdcStopPosition': 'string',
            'RecoveryCheckpoint': 'string',
            'ReplicationTaskArn': 'string',
            'ReplicationTaskStats': {
                'FullLoadProgressPercent': 123,
                'ElapsedTimeMillis': 123,
                'TablesLoaded': 123,
                'TablesLoading': 123,
                'TablesQueued': 123,
                'TablesErrored': 123
            }
        }
    }
    
    
    :returns: 
    Must contain from 1 to 255 alphanumeric characters or hyphens.
    First character must be a letter.
    Cannot end with a hyphen or contain two consecutive hyphens.
    
    """
    pass

def start_replication_task_assessment(ReplicationTaskArn=None):
    """
    Starts the replication task assessment for unsupported data types in the source database.
    See also: AWS API Documentation
    
    
    :example: response = client.start_replication_task_assessment(
        ReplicationTaskArn='string'
    )
    
    
    :type ReplicationTaskArn: string
    :param ReplicationTaskArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the replication task.
            

    :rtype: dict
    :return: {
        'ReplicationTask': {
            'ReplicationTaskIdentifier': 'string',
            'SourceEndpointArn': 'string',
            'TargetEndpointArn': 'string',
            'ReplicationInstanceArn': 'string',
            'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
            'TableMappings': 'string',
            'ReplicationTaskSettings': 'string',
            'Status': 'string',
            'LastFailureMessage': 'string',
            'StopReason': 'string',
            'ReplicationTaskCreationDate': datetime(2015, 1, 1),
            'ReplicationTaskStartDate': datetime(2015, 1, 1),
            'CdcStartPosition': 'string',
            'CdcStopPosition': 'string',
            'RecoveryCheckpoint': 'string',
            'ReplicationTaskArn': 'string',
            'ReplicationTaskStats': {
                'FullLoadProgressPercent': 123,
                'ElapsedTimeMillis': 123,
                'TablesLoaded': 123,
                'TablesLoading': 123,
                'TablesQueued': 123,
                'TablesErrored': 123
            }
        }
    }
    
    
    """
    pass

def stop_replication_task(ReplicationTaskArn=None):
    """
    Stops the replication task.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_replication_task(
        ReplicationTaskArn='string'
    )
    
    
    :type ReplicationTaskArn: string
    :param ReplicationTaskArn: [REQUIRED]
            The Amazon Resource Name(ARN) of the replication task to be stopped.
            

    :rtype: dict
    :return: {
        'ReplicationTask': {
            'ReplicationTaskIdentifier': 'string',
            'SourceEndpointArn': 'string',
            'TargetEndpointArn': 'string',
            'ReplicationInstanceArn': 'string',
            'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
            'TableMappings': 'string',
            'ReplicationTaskSettings': 'string',
            'Status': 'string',
            'LastFailureMessage': 'string',
            'StopReason': 'string',
            'ReplicationTaskCreationDate': datetime(2015, 1, 1),
            'ReplicationTaskStartDate': datetime(2015, 1, 1),
            'CdcStartPosition': 'string',
            'CdcStopPosition': 'string',
            'RecoveryCheckpoint': 'string',
            'ReplicationTaskArn': 'string',
            'ReplicationTaskStats': {
                'FullLoadProgressPercent': 123,
                'ElapsedTimeMillis': 123,
                'TablesLoaded': 123,
                'TablesLoading': 123,
                'TablesQueued': 123,
                'TablesErrored': 123
            }
        }
    }
    
    
    """
    pass

def test_connection(ReplicationInstanceArn=None, EndpointArn=None):
    """
    Tests the connection between the replication instance and the endpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.test_connection(
        ReplicationInstanceArn='string',
        EndpointArn='string'
    )
    
    
    :type ReplicationInstanceArn: string
    :param ReplicationInstanceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the replication instance.
            

    :type EndpointArn: string
    :param EndpointArn: [REQUIRED]
            The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
            

    :rtype: dict
    :return: {
        'Connection': {
            'ReplicationInstanceArn': 'string',
            'EndpointArn': 'string',
            'Status': 'string',
            'LastFailureMessage': 'string',
            'EndpointIdentifier': 'string',
            'ReplicationInstanceIdentifier': 'string'
        }
    }
    
    
    """
    pass

