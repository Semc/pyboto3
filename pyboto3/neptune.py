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

def add_role_to_db_cluster(DBClusterIdentifier=None, RoleArn=None):
    """
    Associates an Identity and Access Management (IAM) role from an Neptune DB cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.add_role_to_db_cluster(
        DBClusterIdentifier='string',
        RoleArn='string'
    )
    
    
    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]
            The name of the DB cluster to associate the IAM role with.
            

    :type RoleArn: string
    :param RoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM role to associate with the Neptune DB cluster, for example arn:aws:iam::123456789012:role/NeptuneAccessRole .
            

    """
    pass

def add_source_identifier_to_subscription(SubscriptionName=None, SourceIdentifier=None):
    """
    Adds a source identifier to an existing event notification subscription.
    See also: AWS API Documentation
    
    
    :example: response = client.add_source_identifier_to_subscription(
        SubscriptionName='string',
        SourceIdentifier='string'
    )
    
    
    :type SubscriptionName: string
    :param SubscriptionName: [REQUIRED]
            The name of the event notification subscription you want to add a source identifier to.
            

    :type SourceIdentifier: string
    :param SourceIdentifier: [REQUIRED]
            The identifier of the event source to be added.
            Constraints:
            If the source type is a DB instance, then a DBInstanceIdentifier must be supplied.
            If the source type is a DB security group, a DBSecurityGroupName must be supplied.
            If the source type is a DB parameter group, a DBParameterGroupName must be supplied.
            If the source type is a DB snapshot, a DBSnapshotIdentifier must be supplied.
            

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
            'Enabled': True|False,
            'EventSubscriptionArn': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def add_tags_to_resource(ResourceName=None, Tags=None):
    """
    Adds metadata tags to an Amazon Neptune resource. These tags can also be used with cost allocation reporting to track cost associated with Amazon Neptune resources, or used in a Condition statement in an IAM policy for Amazon Neptune.
    See also: AWS API Documentation
    
    
    :example: response = client.add_tags_to_resource(
        ResourceName='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceName: string
    :param ResourceName: [REQUIRED]
            The Amazon Neptune resource that the tags are added to. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see Constructing an Amazon Resource Name (ARN) .
            

    :type Tags: list
    :param Tags: [REQUIRED]
            The tags to be assigned to the Amazon Neptune resource.
            (dict) --Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can't be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can't be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            

    """
    pass

def apply_pending_maintenance_action(ResourceIdentifier=None, ApplyAction=None, OptInType=None):
    """
    Applies a pending maintenance action to a resource (for example, to a DB instance).
    See also: AWS API Documentation
    
    
    :example: response = client.apply_pending_maintenance_action(
        ResourceIdentifier='string',
        ApplyAction='string',
        OptInType='string'
    )
    
    
    :type ResourceIdentifier: string
    :param ResourceIdentifier: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource that the pending maintenance action applies to. For information about creating an ARN, see Constructing an Amazon Resource Name (ARN) .
            

    :type ApplyAction: string
    :param ApplyAction: [REQUIRED]
            The pending maintenance action to apply to this resource.
            Valid values: system-update , db-upgrade
            

    :type OptInType: string
    :param OptInType: [REQUIRED]
            A value that specifies the type of opt-in request, or undoes an opt-in request. An opt-in request of type immediate can't be undone.
            Valid values:
            immediate - Apply the maintenance action immediately.
            next-maintenance - Apply the maintenance action during the next maintenance window for the resource.
            undo-opt-in - Cancel any existing next-maintenance opt-in requests.
            

    :rtype: dict
    :return: {
        'ResourcePendingMaintenanceActions': {
            'ResourceIdentifier': 'string',
            'PendingMaintenanceActionDetails': [
                {
                    'Action': 'string',
                    'AutoAppliedAfterDate': datetime(2015, 1, 1),
                    'ForcedApplyDate': datetime(2015, 1, 1),
                    'OptInStatus': 'string',
                    'CurrentApplyDate': datetime(2015, 1, 1),
                    'Description': 'string'
                },
            ]
        }
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

def copy_db_cluster_parameter_group(SourceDBClusterParameterGroupIdentifier=None, TargetDBClusterParameterGroupIdentifier=None, TargetDBClusterParameterGroupDescription=None, Tags=None):
    """
    Copies the specified DB cluster parameter group.
    See also: AWS API Documentation
    
    
    :example: response = client.copy_db_cluster_parameter_group(
        SourceDBClusterParameterGroupIdentifier='string',
        TargetDBClusterParameterGroupIdentifier='string',
        TargetDBClusterParameterGroupDescription='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type SourceDBClusterParameterGroupIdentifier: string
    :param SourceDBClusterParameterGroupIdentifier: [REQUIRED]
            The identifier or Amazon Resource Name (ARN) for the source DB cluster parameter group. For information about creating an ARN, see Constructing an Amazon Resource Name (ARN) .
            Constraints:
            Must specify a valid DB cluster parameter group.
            If the source DB cluster parameter group is in the same AWS Region as the copy, specify a valid DB parameter group identifier, for example my-db-cluster-param-group , or a valid ARN.
            If the source DB parameter group is in a different AWS Region than the copy, specify a valid DB cluster parameter group ARN, for example arn:aws:rds:us-east-1:123456789012:cluster-pg:custom-cluster-group1 .
            

    :type TargetDBClusterParameterGroupIdentifier: string
    :param TargetDBClusterParameterGroupIdentifier: [REQUIRED]
            The identifier for the copied DB cluster parameter group.
            Constraints:
            Cannot be null, empty, or blank
            Must contain from 1 to 255 letters, numbers, or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            Example: my-cluster-param-group1
            

    :type TargetDBClusterParameterGroupDescription: string
    :param TargetDBClusterParameterGroupDescription: [REQUIRED]
            A description for the copied DB cluster parameter group.
            

    :type Tags: list
    :param Tags: A list of tags. For more information, see Tagging Amazon Neptune Resources .
            (dict) --Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can't be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can't be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            

    :rtype: dict
    :return: {
        'DBClusterParameterGroup': {
            'DBClusterParameterGroupName': 'string',
            'DBParameterGroupFamily': 'string',
            'Description': 'string',
            'DBClusterParameterGroupArn': 'string'
        }
    }
    
    
    """
    pass

def copy_db_cluster_snapshot(SourceDBClusterSnapshotIdentifier=None, TargetDBClusterSnapshotIdentifier=None, KmsKeyId=None, PreSignedUrl=None, CopyTags=None, Tags=None, SourceRegion=None):
    """
    Copies a snapshot of a DB cluster.
    To copy a DB cluster snapshot from a shared manual DB cluster snapshot, SourceDBClusterSnapshotIdentifier must be the Amazon Resource Name (ARN) of the shared DB cluster snapshot.
    You can copy an encrypted DB cluster snapshot from another AWS Region. In that case, the AWS Region where you call the CopyDBClusterSnapshot action is the destination AWS Region for the encrypted DB cluster snapshot to be copied to. To copy an encrypted DB cluster snapshot from another AWS Region, you must provide the following values:
    To learn how to generate a Signature Version 4 signed request, see Authenticating Requests: Using Query Parameters (AWS Signature Version 4) and Signature Version 4 Signing Process .
    To cancel the copy operation once it is in progress, delete the target DB cluster snapshot identified by TargetDBClusterSnapshotIdentifier while that DB cluster snapshot is in "copying" status.
    See also: AWS API Documentation
    
    
    :example: response = client.copy_db_cluster_snapshot(
        SourceDBClusterSnapshotIdentifier='string',
        TargetDBClusterSnapshotIdentifier='string',
        KmsKeyId='string',
        CopyTags=True|False,
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        SourceRegion='string'
    )
    
    
    :type SourceDBClusterSnapshotIdentifier: string
    :param SourceDBClusterSnapshotIdentifier: [REQUIRED]
            The identifier of the DB cluster snapshot to copy. This parameter is not case-sensitive.
            You can't copy an encrypted, shared DB cluster snapshot from one AWS Region to another.
            Constraints:
            Must specify a valid system snapshot in the 'available' state.
            If the source snapshot is in the same AWS Region as the copy, specify a valid DB snapshot identifier.
            If the source snapshot is in a different AWS Region than the copy, specify a valid DB cluster snapshot ARN.
            Example: my-cluster-snapshot1
            

    :type TargetDBClusterSnapshotIdentifier: string
    :param TargetDBClusterSnapshotIdentifier: [REQUIRED]
            The identifier of the new DB cluster snapshot to create from the source DB cluster snapshot. This parameter is not case-sensitive.
            Constraints:
            Must contain from 1 to 63 letters, numbers, or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Example: my-cluster-snapshot2
            

    :type KmsKeyId: string
    :param KmsKeyId: The AWS AWS KMS key ID for an encrypted DB cluster snapshot. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key.
            If you copy an unencrypted DB cluster snapshot and specify a value for the KmsKeyId parameter, Amazon Neptune encrypts the target DB cluster snapshot using the specified KMS encryption key.
            If you copy an encrypted DB cluster snapshot from your AWS account, you can specify a value for KmsKeyId to encrypt the copy with a new KMS encryption key. If you don't specify a value for KmsKeyId , then the copy of the DB cluster snapshot is encrypted with the same KMS key as the source DB cluster snapshot.
            If you copy an encrypted DB cluster snapshot that is shared from another AWS account, then you must specify a value for KmsKeyId .
            To copy an encrypted DB cluster snapshot to another AWS Region, you must set KmsKeyId to the KMS key ID you want to use to encrypt the copy of the DB cluster snapshot in the destination AWS Region. KMS encryption keys are specific to the AWS Region that they are created in, and you can't use encryption keys from one AWS Region in another AWS Region.
            

    :type PreSignedUrl: string
    :param PreSignedUrl: The URL that contains a Signature Version 4 signed request for the CopyDBClusterSnapshot API action in the AWS Region that contains the source DB cluster snapshot to copy. The PreSignedUrl parameter must be used when copying an encrypted DB cluster snapshot from another AWS Region.
            The pre-signed URL must be a valid request for the CopyDBSClusterSnapshot API action that can be executed in the source AWS Region that contains the encrypted DB cluster snapshot to be copied. The pre-signed URL request must contain the following parameter values:
            KmsKeyId - The AWS KMS key identifier for the key to use to encrypt the copy of the DB cluster snapshot in the destination AWS Region. This is the same identifier for both the CopyDBClusterSnapshot action that is called in the destination AWS Region, and the action contained in the pre-signed URL.
            DestinationRegion - The name of the AWS Region that the DB cluster snapshot will be created in.
            SourceDBClusterSnapshotIdentifier - The DB cluster snapshot identifier for the encrypted DB cluster snapshot to be copied. This identifier must be in the Amazon Resource Name (ARN) format for the source AWS Region. For example, if you are copying an encrypted DB cluster snapshot from the us-west-2 AWS Region, then your SourceDBClusterSnapshotIdentifier looks like the following example: arn:aws:rds:us-west-2:123456789012:cluster-snapshot:neptune-cluster1-snapshot-20161115 .
            To learn how to generate a Signature Version 4 signed request, see Authenticating Requests: Using Query Parameters (AWS Signature Version 4) and Signature Version 4 Signing Process .
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
            

    :type CopyTags: boolean
    :param CopyTags: True to copy all tags from the source DB cluster snapshot to the target DB cluster snapshot, and otherwise false. The default is false.

    :type Tags: list
    :param Tags: A list of tags. For more information, see Tagging Amazon Neptune Resources .
            (dict) --Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can't be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can't be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            

    :type SourceRegion: string
    :param SourceRegion: The ID of the region that contains the snapshot to be copied.

    :rtype: dict
    :return: {
        'DBClusterSnapshot': {
            'AvailabilityZones': [
                'string',
            ],
            'DBClusterSnapshotIdentifier': 'string',
            'DBClusterIdentifier': 'string',
            'SnapshotCreateTime': datetime(2015, 1, 1),
            'Engine': 'string',
            'AllocatedStorage': 123,
            'Status': 'string',
            'Port': 123,
            'VpcId': 'string',
            'ClusterCreateTime': datetime(2015, 1, 1),
            'MasterUsername': 'string',
            'EngineVersion': 'string',
            'LicenseModel': 'string',
            'SnapshotType': 'string',
            'PercentProgress': 123,
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DBClusterSnapshotArn': 'string',
            'SourceDBClusterSnapshotArn': 'string',
            'IAMDatabaseAuthenticationEnabled': True|False
        }
    }
    
    
    :returns: 
    TargetDBClusterSnapshotIdentifier - The identifier for the new copy of the DB cluster snapshot in the destination AWS Region.
    SourceDBClusterSnapshotIdentifier - The DB cluster snapshot identifier for the encrypted DB cluster snapshot to be copied. This identifier must be in the ARN format for the source AWS Region and is the same value as the SourceDBClusterSnapshotIdentifier in the pre-signed URL.
    
    """
    pass

def copy_db_parameter_group(SourceDBParameterGroupIdentifier=None, TargetDBParameterGroupIdentifier=None, TargetDBParameterGroupDescription=None, Tags=None):
    """
    Copies the specified DB parameter group.
    See also: AWS API Documentation
    
    
    :example: response = client.copy_db_parameter_group(
        SourceDBParameterGroupIdentifier='string',
        TargetDBParameterGroupIdentifier='string',
        TargetDBParameterGroupDescription='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type SourceDBParameterGroupIdentifier: string
    :param SourceDBParameterGroupIdentifier: [REQUIRED]
            The identifier or ARN for the source DB parameter group. For information about creating an ARN, see Constructing an Amazon Resource Name (ARN) .
            Constraints:
            Must specify a valid DB parameter group.
            Must specify a valid DB parameter group identifier, for example my-db-param-group , or a valid ARN.
            

    :type TargetDBParameterGroupIdentifier: string
    :param TargetDBParameterGroupIdentifier: [REQUIRED]
            The identifier for the copied DB parameter group.
            Constraints:
            Cannot be null, empty, or blank
            Must contain from 1 to 255 letters, numbers, or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            Example: my-db-parameter-group
            

    :type TargetDBParameterGroupDescription: string
    :param TargetDBParameterGroupDescription: [REQUIRED]
            A description for the copied DB parameter group.
            

    :type Tags: list
    :param Tags: A list of tags. For more information, see Tagging Amazon Neptune Resources .
            (dict) --Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can't be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can't be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            

    :rtype: dict
    :return: {
        'DBParameterGroup': {
            'DBParameterGroupName': 'string',
            'DBParameterGroupFamily': 'string',
            'Description': 'string',
            'DBParameterGroupArn': 'string'
        }
    }
    
    
    """
    pass

def create_db_cluster(AvailabilityZones=None, BackupRetentionPeriod=None, CharacterSetName=None, DatabaseName=None, DBClusterIdentifier=None, DBClusterParameterGroupName=None, VpcSecurityGroupIds=None, DBSubnetGroupName=None, Engine=None, EngineVersion=None, Port=None, MasterUsername=None, MasterUserPassword=None, OptionGroupName=None, PreferredBackupWindow=None, PreferredMaintenanceWindow=None, ReplicationSourceIdentifier=None, Tags=None, StorageEncrypted=None, KmsKeyId=None, PreSignedUrl=None, EnableIAMDatabaseAuthentication=None, SourceRegion=None):
    """
    Creates a new Amazon Neptune DB cluster.
    You can use the ReplicationSourceIdentifier parameter to create the DB cluster as a Read Replica of another DB cluster or Amazon Neptune DB instance. For cross-region replication where the DB cluster identified by ReplicationSourceIdentifier is encrypted, you must also specify the PreSignedUrl parameter.
    See also: AWS API Documentation
    
    
    :example: response = client.create_db_cluster(
        AvailabilityZones=[
            'string',
        ],
        BackupRetentionPeriod=123,
        CharacterSetName='string',
        DatabaseName='string',
        DBClusterIdentifier='string',
        DBClusterParameterGroupName='string',
        VpcSecurityGroupIds=[
            'string',
        ],
        DBSubnetGroupName='string',
        Engine='string',
        EngineVersion='string',
        Port=123,
        MasterUsername='string',
        MasterUserPassword='string',
        OptionGroupName='string',
        PreferredBackupWindow='string',
        PreferredMaintenanceWindow='string',
        ReplicationSourceIdentifier='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        StorageEncrypted=True|False,
        KmsKeyId='string',
        EnableIAMDatabaseAuthentication=True|False,
        SourceRegion='string'
    )
    
    
    :type AvailabilityZones: list
    :param AvailabilityZones: A list of EC2 Availability Zones that instances in the DB cluster can be created in.
            (string) --
            

    :type BackupRetentionPeriod: integer
    :param BackupRetentionPeriod: The number of days for which automated backups are retained. You must specify a minimum value of 1.
            Default: 1
            Constraints:
            Must be a value from 1 to 35
            

    :type CharacterSetName: string
    :param CharacterSetName: A value that indicates that the DB cluster should be associated with the specified CharacterSet.

    :type DatabaseName: string
    :param DatabaseName: The name for your database of up to 64 alpha-numeric characters. If you do not provide a name, Amazon Neptune will not create a database in the DB cluster you are creating.

    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]
            The DB cluster identifier. This parameter is stored as a lowercase string.
            Constraints:
            Must contain from 1 to 63 letters, numbers, or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Example: my-cluster1
            

    :type DBClusterParameterGroupName: string
    :param DBClusterParameterGroupName: The name of the DB cluster parameter group to associate with this DB cluster. If this argument is omitted, the default is used.
            Constraints:
            If supplied, must match the name of an existing DBClusterParameterGroup.
            

    :type VpcSecurityGroupIds: list
    :param VpcSecurityGroupIds: A list of EC2 VPC security groups to associate with this DB cluster.
            (string) --
            

    :type DBSubnetGroupName: string
    :param DBSubnetGroupName: A DB subnet group to associate with this DB cluster.
            Constraints: Must match the name of an existing DBSubnetGroup. Must not be default.
            Example: mySubnetgroup
            

    :type Engine: string
    :param Engine: [REQUIRED]
            The name of the database engine to be used for this DB cluster.
            Valid Values: neptune
            

    :type EngineVersion: string
    :param EngineVersion: The version number of the database engine to use.
            Example: 1.0.1
            

    :type Port: integer
    :param Port: The port number on which the instances in the DB cluster accept connections.
            Default: 8182
            

    :type MasterUsername: string
    :param MasterUsername: The name of the master user for the DB cluster.
            Constraints:
            Must be 1 to 16 letters or numbers.
            First character must be a letter.
            Cannot be a reserved word for the chosen database engine.
            

    :type MasterUserPassword: string
    :param MasterUserPassword: The password for the master database user. This password can contain any printable ASCII character except '/', ''', or '@'.
            Constraints: Must contain from 8 to 41 characters.
            

    :type OptionGroupName: string
    :param OptionGroupName: A value that indicates that the DB cluster should be associated with the specified option group.
            Permanent options can't be removed from an option group. The option group can't be removed from a DB cluster once it is associated with a DB cluster.
            

    :type PreferredBackupWindow: string
    :param PreferredBackupWindow: The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.
            The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region. To see the time blocks available, see Adjusting the Preferred Maintenance Window in the Amazon Neptune User Guide.
            Constraints:
            Must be in the format hh24:mi-hh24:mi .
            Must be in Universal Coordinated Time (UTC).
            Must not conflict with the preferred maintenance window.
            Must be at least 30 minutes.
            

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
            Format: ddd:hh24:mi-ddd:hh24:mi
            The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week. To see the time blocks available, see Adjusting the Preferred Maintenance Window in the Amazon Neptune User Guide.
            Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.
            Constraints: Minimum 30-minute window.
            

    :type ReplicationSourceIdentifier: string
    :param ReplicationSourceIdentifier: The Amazon Resource Name (ARN) of the source DB instance or DB cluster if this DB cluster is created as a Read Replica.

    :type Tags: list
    :param Tags: A list of tags. For more information, see Tagging Amazon Neptune Resources .
            (dict) --Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can't be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can't be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            

    :type StorageEncrypted: boolean
    :param StorageEncrypted: Specifies whether the DB cluster is encrypted.

    :type KmsKeyId: string
    :param KmsKeyId: The AWS KMS key identifier for an encrypted DB cluster.
            The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a DB cluster with the same AWS account that owns the KMS encryption key used to encrypt the new DB cluster, then you can use the KMS key alias instead of the ARN for the KMS encryption key.
            If an encryption key is not specified in KmsKeyId :
            If ReplicationSourceIdentifier identifies an encrypted source, then Amazon Neptune will use the encryption key used to encrypt the source. Otherwise, Amazon Neptune will use your default encryption key.
            If the StorageEncrypted parameter is true and ReplicationSourceIdentifier is not specified, then Amazon Neptune will use your default encryption key.
            AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.
            If you create a Read Replica of an encrypted DB cluster in another AWS Region, you must set KmsKeyId to a KMS key ID that is valid in the destination AWS Region. This key is used to encrypt the Read Replica in that AWS Region.
            

    :type PreSignedUrl: string
    :param PreSignedUrl: A URL that contains a Signature Version 4 signed request for the CreateDBCluster action to be called in the source AWS Region where the DB cluster is replicated from. You only need to specify PreSignedUrl when you are performing cross-region replication from an encrypted DB cluster.
            The pre-signed URL must be a valid request for the CreateDBCluster API action that can be executed in the source AWS Region that contains the encrypted DB cluster to be copied.
            The pre-signed URL request must contain the following parameter values:
            KmsKeyId - The AWS KMS key identifier for the key to use to encrypt the copy of the DB cluster in the destination AWS Region. This should refer to the same KMS key for both the CreateDBCluster action that is called in the destination AWS Region, and the action contained in the pre-signed URL.
            DestinationRegion - The name of the AWS Region that Read Replica will be created in.
            ReplicationSourceIdentifier - The DB cluster identifier for the encrypted DB cluster to be copied. This identifier must be in the Amazon Resource Name (ARN) format for the source AWS Region. For example, if you are copying an encrypted DB cluster from the us-west-2 AWS Region, then your ReplicationSourceIdentifier would look like Example: arn:aws:rds:us-west-2:123456789012:cluster:neptune-cluster1 .
            To learn how to generate a Signature Version 4 signed request, see Authenticating Requests: Using Query Parameters (AWS Signature Version 4) and Signature Version 4 Signing Process .
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
            

    :type EnableIAMDatabaseAuthentication: boolean
    :param EnableIAMDatabaseAuthentication: True to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts, and otherwise false.
            Default: false
            

    :type SourceRegion: string
    :param SourceRegion: The ID of the region that contains the source for the db cluster.

    :rtype: dict
    :return: {
        'DBCluster': {
            'AllocatedStorage': 123,
            'AvailabilityZones': [
                'string',
            ],
            'BackupRetentionPeriod': 123,
            'CharacterSetName': 'string',
            'DatabaseName': 'string',
            'DBClusterIdentifier': 'string',
            'DBClusterParameterGroup': 'string',
            'DBSubnetGroup': 'string',
            'Status': 'string',
            'PercentProgress': 'string',
            'EarliestRestorableTime': datetime(2015, 1, 1),
            'Endpoint': 'string',
            'ReaderEndpoint': 'string',
            'MultiAZ': True|False,
            'Engine': 'string',
            'EngineVersion': 'string',
            'LatestRestorableTime': datetime(2015, 1, 1),
            'Port': 123,
            'MasterUsername': 'string',
            'DBClusterOptionGroupMemberships': [
                {
                    'DBClusterOptionGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'PreferredBackupWindow': 'string',
            'PreferredMaintenanceWindow': 'string',
            'ReplicationSourceIdentifier': 'string',
            'ReadReplicaIdentifiers': [
                'string',
            ],
            'DBClusterMembers': [
                {
                    'DBInstanceIdentifier': 'string',
                    'IsClusterWriter': True|False,
                    'DBClusterParameterGroupStatus': 'string',
                    'PromotionTier': 123
                },
            ],
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'HostedZoneId': 'string',
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DbClusterResourceId': 'string',
            'DBClusterArn': 'string',
            'AssociatedRoles': [
                {
                    'RoleArn': 'string',
                    'Status': 'string'
                },
            ],
            'IAMDatabaseAuthenticationEnabled': True|False,
            'CloneGroupId': 'string',
            'ClusterCreateTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_db_cluster_parameter_group(DBClusterParameterGroupName=None, DBParameterGroupFamily=None, Description=None, Tags=None):
    """
    Creates a new DB cluster parameter group.
    Parameters in a DB cluster parameter group apply to all of the instances in a DB cluster.
    A DB cluster parameter group is initially created with the default parameters for the database engine used by instances in the DB cluster. To provide custom values for any of the parameters, you must modify the group after creating it using  ModifyDBClusterParameterGroup . Once you've created a DB cluster parameter group, you need to associate it with your DB cluster using  ModifyDBCluster . When you associate a new DB cluster parameter group with a running DB cluster, you need to reboot the DB instances in the DB cluster without failover for the new DB cluster parameter group and associated settings to take effect.
    See also: AWS API Documentation
    
    
    :example: response = client.create_db_cluster_parameter_group(
        DBClusterParameterGroupName='string',
        DBParameterGroupFamily='string',
        Description='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type DBClusterParameterGroupName: string
    :param DBClusterParameterGroupName: [REQUIRED]
            The name of the DB cluster parameter group.
            Constraints:
            Must match the name of an existing DBClusterParameterGroup.
            Note
            This value is stored as a lowercase string.
            

    :type DBParameterGroupFamily: string
    :param DBParameterGroupFamily: [REQUIRED]
            The DB cluster parameter group family name. A DB cluster parameter group can be associated with one and only one DB cluster parameter group family, and can be applied only to a DB cluster running a database engine and engine version compatible with that DB cluster parameter group family.
            

    :type Description: string
    :param Description: [REQUIRED]
            The description for the DB cluster parameter group.
            

    :type Tags: list
    :param Tags: A list of tags. For more information, see Tagging Amazon Neptune Resources .
            (dict) --Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can't be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can't be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            

    :rtype: dict
    :return: {
        'DBClusterParameterGroup': {
            'DBClusterParameterGroupName': 'string',
            'DBParameterGroupFamily': 'string',
            'Description': 'string',
            'DBClusterParameterGroupArn': 'string'
        }
    }
    
    
    """
    pass

def create_db_cluster_snapshot(DBClusterSnapshotIdentifier=None, DBClusterIdentifier=None, Tags=None):
    """
    Creates a snapshot of a DB cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.create_db_cluster_snapshot(
        DBClusterSnapshotIdentifier='string',
        DBClusterIdentifier='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type DBClusterSnapshotIdentifier: string
    :param DBClusterSnapshotIdentifier: [REQUIRED]
            The identifier of the DB cluster snapshot. This parameter is stored as a lowercase string.
            Constraints:
            Must contain from 1 to 63 letters, numbers, or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Example: my-cluster1-snapshot1
            

    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]
            The identifier of the DB cluster to create a snapshot for. This parameter is not case-sensitive.
            Constraints:
            Must match the identifier of an existing DBCluster.
            Example: my-cluster1
            

    :type Tags: list
    :param Tags: The tags to be assigned to the DB cluster snapshot.
            (dict) --Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can't be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can't be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            

    :rtype: dict
    :return: {
        'DBClusterSnapshot': {
            'AvailabilityZones': [
                'string',
            ],
            'DBClusterSnapshotIdentifier': 'string',
            'DBClusterIdentifier': 'string',
            'SnapshotCreateTime': datetime(2015, 1, 1),
            'Engine': 'string',
            'AllocatedStorage': 123,
            'Status': 'string',
            'Port': 123,
            'VpcId': 'string',
            'ClusterCreateTime': datetime(2015, 1, 1),
            'MasterUsername': 'string',
            'EngineVersion': 'string',
            'LicenseModel': 'string',
            'SnapshotType': 'string',
            'PercentProgress': 123,
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DBClusterSnapshotArn': 'string',
            'SourceDBClusterSnapshotArn': 'string',
            'IAMDatabaseAuthenticationEnabled': True|False
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_db_instance(DBName=None, DBInstanceIdentifier=None, AllocatedStorage=None, DBInstanceClass=None, Engine=None, MasterUsername=None, MasterUserPassword=None, DBSecurityGroups=None, VpcSecurityGroupIds=None, AvailabilityZone=None, DBSubnetGroupName=None, PreferredMaintenanceWindow=None, DBParameterGroupName=None, BackupRetentionPeriod=None, PreferredBackupWindow=None, Port=None, MultiAZ=None, EngineVersion=None, AutoMinorVersionUpgrade=None, LicenseModel=None, Iops=None, OptionGroupName=None, CharacterSetName=None, PubliclyAccessible=None, Tags=None, DBClusterIdentifier=None, StorageType=None, TdeCredentialArn=None, TdeCredentialPassword=None, StorageEncrypted=None, KmsKeyId=None, Domain=None, CopyTagsToSnapshot=None, MonitoringInterval=None, MonitoringRoleArn=None, DomainIAMRoleName=None, PromotionTier=None, Timezone=None, EnableIAMDatabaseAuthentication=None, EnablePerformanceInsights=None, PerformanceInsightsKMSKeyId=None, EnableCloudwatchLogsExports=None):
    """
    Creates a new DB instance.
    See also: AWS API Documentation
    
    
    :example: response = client.create_db_instance(
        DBName='string',
        DBInstanceIdentifier='string',
        AllocatedStorage=123,
        DBInstanceClass='string',
        Engine='string',
        MasterUsername='string',
        MasterUserPassword='string',
        DBSecurityGroups=[
            'string',
        ],
        VpcSecurityGroupIds=[
            'string',
        ],
        AvailabilityZone='string',
        DBSubnetGroupName='string',
        PreferredMaintenanceWindow='string',
        DBParameterGroupName='string',
        BackupRetentionPeriod=123,
        PreferredBackupWindow='string',
        Port=123,
        MultiAZ=True|False,
        EngineVersion='string',
        AutoMinorVersionUpgrade=True|False,
        LicenseModel='string',
        Iops=123,
        OptionGroupName='string',
        CharacterSetName='string',
        PubliclyAccessible=True|False,
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        DBClusterIdentifier='string',
        StorageType='string',
        TdeCredentialArn='string',
        TdeCredentialPassword='string',
        StorageEncrypted=True|False,
        KmsKeyId='string',
        Domain='string',
        CopyTagsToSnapshot=True|False,
        MonitoringInterval=123,
        MonitoringRoleArn='string',
        DomainIAMRoleName='string',
        PromotionTier=123,
        Timezone='string',
        EnableIAMDatabaseAuthentication=True|False,
        EnablePerformanceInsights=True|False,
        PerformanceInsightsKMSKeyId='string',
        EnableCloudwatchLogsExports=[
            'string',
        ]
    )
    
    
    :type DBName: string
    :param DBName: The database name.
            Type: String
            

    :type DBInstanceIdentifier: string
    :param DBInstanceIdentifier: [REQUIRED]
            The DB instance identifier. This parameter is stored as a lowercase string.
            Constraints:
            Must contain from 1 to 63 letters, numbers, or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Example: mydbinstance
            

    :type AllocatedStorage: integer
    :param AllocatedStorage: The amount of storage (in gibibytes) to allocate for the DB instance.
            Type: Integer
            Not applicable. Neptune cluster volumes automatically grow as the amount of data in your database increases, though you are only charged for the space that you use in a Neptune cluster volume.
            

    :type DBInstanceClass: string
    :param DBInstanceClass: [REQUIRED]
            The compute and memory capacity of the DB instance, for example, db.m4.large . Not all DB instance classes are available in all AWS Regions.
            

    :type Engine: string
    :param Engine: [REQUIRED]
            The name of the database engine to be used for this instance.
            Valid Values: neptune
            

    :type MasterUsername: string
    :param MasterUsername: The name for the master user. Not used.

    :type MasterUserPassword: string
    :param MasterUserPassword: The password for the master user. The password can include any printable ASCII character except '/', ''', or '@'.
            Not used.
            

    :type DBSecurityGroups: list
    :param DBSecurityGroups: A list of DB security groups to associate with this DB instance.
            Default: The default DB security group for the database engine.
            (string) --
            

    :type VpcSecurityGroupIds: list
    :param VpcSecurityGroupIds: A list of EC2 VPC security groups to associate with this DB instance.
            Not applicable. The associated list of EC2 VPC security groups is managed by the DB cluster. For more information, see CreateDBCluster .
            Default: The default EC2 VPC security group for the DB subnet group's VPC.
            (string) --
            

    :type AvailabilityZone: string
    :param AvailabilityZone: The EC2 Availability Zone that the DB instance is created in.
            Default: A random, system-chosen Availability Zone in the endpoint's AWS Region.
            Example: us-east-1d
            Constraint: The AvailabilityZone parameter can't be specified if the MultiAZ parameter is set to true . The specified Availability Zone must be in the same AWS Region as the current endpoint.
            

    :type DBSubnetGroupName: string
    :param DBSubnetGroupName: A DB subnet group to associate with this DB instance.
            If there is no DB subnet group, then it is a non-VPC DB instance.
            

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: The time range each week during which system maintenance can occur, in Universal Coordinated Time (UTC).
            Format: ddd:hh24:mi-ddd:hh24:mi
            The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.
            Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.
            Constraints: Minimum 30-minute window.
            

    :type DBParameterGroupName: string
    :param DBParameterGroupName: The name of the DB parameter group to associate with this DB instance. If this argument is omitted, the default DBParameterGroup for the specified engine is used.
            Constraints:
            Must be 1 to 255 letters, numbers, or hyphens.
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            

    :type BackupRetentionPeriod: integer
    :param BackupRetentionPeriod: The number of days for which automated backups are retained.
            Not applicable. The retention period for automated backups is managed by the DB cluster. For more information, see CreateDBCluster .
            Default: 1
            Constraints:
            Must be a value from 0 to 35
            Cannot be set to 0 if the DB instance is a source to Read Replicas
            

    :type PreferredBackupWindow: string
    :param PreferredBackupWindow: The daily time range during which automated backups are created.
            Not applicable. The daily time range for creating automated backups is managed by the DB cluster. For more information, see CreateDBCluster .
            

    :type Port: integer
    :param Port: The port number on which the database accepts connections.
            Not applicable. The port is managed by the DB cluster. For more information, see CreateDBCluster .
            Default: 8182
            Type: Integer
            

    :type MultiAZ: boolean
    :param MultiAZ: Specifies if the DB instance is a Multi-AZ deployment. You can't set the AvailabilityZone parameter if the MultiAZ parameter is set to true.

    :type EngineVersion: string
    :param EngineVersion: The version number of the database engine to use.

    :type AutoMinorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: Indicates that minor engine upgrades are applied automatically to the DB instance during the maintenance window.
            Default: true
            

    :type LicenseModel: string
    :param LicenseModel: License model information for this DB instance.
            Valid values: license-included | bring-your-own-license | general-public-license
            

    :type Iops: integer
    :param Iops: The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for the DB instance.

    :type OptionGroupName: string
    :param OptionGroupName: Indicates that the DB instance should be associated with the specified option group.
            Permanent options, such as the TDE option for Oracle Advanced Security TDE, can't be removed from an option group, and that option group can't be removed from a DB instance once it is associated with a DB instance
            

    :type CharacterSetName: string
    :param CharacterSetName: Indicates that the DB instance should be associated with the specified CharacterSet.
            Not applicable. The character set is managed by the DB cluster. For more information, see CreateDBCluster .
            

    :type PubliclyAccessible: boolean
    :param PubliclyAccessible: This parameter is not supported.

    :type Tags: list
    :param Tags: A list of tags. For more information, see Tagging Amazon Neptune Resources .
            (dict) --Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can't be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can't be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            

    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: The identifier of the DB cluster that the instance will belong to.
            For information on creating a DB cluster, see CreateDBCluster .
            Type: String
            

    :type StorageType: string
    :param StorageType: Specifies the storage type to be associated with the DB instance.
            Not applicable. Storage is managed by the DB Cluster.
            

    :type TdeCredentialArn: string
    :param TdeCredentialArn: The ARN from the key store with which to associate the instance for TDE encryption.

    :type TdeCredentialPassword: string
    :param TdeCredentialPassword: The password for the given ARN from the key store in order to access the device.

    :type StorageEncrypted: boolean
    :param StorageEncrypted: Specifies whether the DB instance is encrypted.
            Not applicable. The encryption for DB instances is managed by the DB cluster. For more information, see CreateDBCluster .
            Default: false
            

    :type KmsKeyId: string
    :param KmsKeyId: The AWS KMS key identifier for an encrypted DB instance.
            The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a DB instance with the same AWS account that owns the KMS encryption key used to encrypt the new DB instance, then you can use the KMS key alias instead of the ARN for the KM encryption key.
            Not applicable. The KMS key identifier is managed by the DB cluster. For more information, see CreateDBCluster .
            If the StorageEncrypted parameter is true, and you do not specify a value for the KmsKeyId parameter, then Amazon Neptune will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.
            

    :type Domain: string
    :param Domain: Specify the Active Directory Domain to create the instance in.

    :type CopyTagsToSnapshot: boolean
    :param CopyTagsToSnapshot: True to copy all tags from the DB instance to snapshots of the DB instance, and otherwise false. The default is false.

    :type MonitoringInterval: integer
    :param MonitoringInterval: The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0.
            If MonitoringRoleArn is specified, then you must also set MonitoringInterval to a value other than 0.
            Valid Values: 0, 1, 5, 10, 15, 30, 60
            

    :type MonitoringRoleArn: string
    :param MonitoringRoleArn: The ARN for the IAM role that permits Neptune to send enhanced monitoring metrics to Amazon CloudWatch Logs. For example, arn:aws:iam:123456789012:role/emaccess .
            If MonitoringInterval is set to a value other than 0, then you must supply a MonitoringRoleArn value.
            

    :type DomainIAMRoleName: string
    :param DomainIAMRoleName: Specify the name of the IAM role to be used when making API calls to the Directory Service.

    :type PromotionTier: integer
    :param PromotionTier: A value that specifies the order in which an Read Replica is promoted to the primary instance after a failure of the existing primary instance.
            Default: 1
            Valid Values: 0 - 15
            

    :type Timezone: string
    :param Timezone: The time zone of the DB instance.

    :type EnableIAMDatabaseAuthentication: boolean
    :param EnableIAMDatabaseAuthentication: True to enable AWS Identity and Access Management (IAM) authentication for Neptune.
            Default: false
            

    :type EnablePerformanceInsights: boolean
    :param EnablePerformanceInsights: True to enable Performance Insights for the DB instance, and otherwise false.

    :type PerformanceInsightsKMSKeyId: string
    :param PerformanceInsightsKMSKeyId: The AWS KMS key identifier for encryption of Performance Insights data. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key.

    :type EnableCloudwatchLogsExports: list
    :param EnableCloudwatchLogsExports: The list of log types that need to be enabled for exporting to CloudWatch Logs.
            (string) --
            

    :rtype: dict
    :return: {
        'DBInstance': {
            'DBInstanceIdentifier': 'string',
            'DBInstanceClass': 'string',
            'Engine': 'string',
            'DBInstanceStatus': 'string',
            'MasterUsername': 'string',
            'DBName': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123,
                'HostedZoneId': 'string'
            },
            'AllocatedStorage': 123,
            'InstanceCreateTime': datetime(2015, 1, 1),
            'PreferredBackupWindow': 'string',
            'BackupRetentionPeriod': 123,
            'DBSecurityGroups': [
                {
                    'DBSecurityGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'DBParameterGroups': [
                {
                    'DBParameterGroupName': 'string',
                    'ParameterApplyStatus': 'string'
                },
            ],
            'AvailabilityZone': 'string',
            'DBSubnetGroup': {
                'DBSubnetGroupName': 'string',
                'DBSubnetGroupDescription': 'string',
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
                ],
                'DBSubnetGroupArn': 'string'
            },
            'PreferredMaintenanceWindow': 'string',
            'PendingModifiedValues': {
                'DBInstanceClass': 'string',
                'AllocatedStorage': 123,
                'MasterUserPassword': 'string',
                'Port': 123,
                'BackupRetentionPeriod': 123,
                'MultiAZ': True|False,
                'EngineVersion': 'string',
                'LicenseModel': 'string',
                'Iops': 123,
                'DBInstanceIdentifier': 'string',
                'StorageType': 'string',
                'CACertificateIdentifier': 'string',
                'DBSubnetGroupName': 'string',
                'PendingCloudwatchLogsExports': {
                    'LogTypesToEnable': [
                        'string',
                    ],
                    'LogTypesToDisable': [
                        'string',
                    ]
                }
            },
            'LatestRestorableTime': datetime(2015, 1, 1),
            'MultiAZ': True|False,
            'EngineVersion': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'ReadReplicaSourceDBInstanceIdentifier': 'string',
            'ReadReplicaDBInstanceIdentifiers': [
                'string',
            ],
            'ReadReplicaDBClusterIdentifiers': [
                'string',
            ],
            'LicenseModel': 'string',
            'Iops': 123,
            'OptionGroupMemberships': [
                {
                    'OptionGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'CharacterSetName': 'string',
            'SecondaryAvailabilityZone': 'string',
            'PubliclyAccessible': True|False,
            'StatusInfos': [
                {
                    'StatusType': 'string',
                    'Normal': True|False,
                    'Status': 'string',
                    'Message': 'string'
                },
            ],
            'StorageType': 'string',
            'TdeCredentialArn': 'string',
            'DbInstancePort': 123,
            'DBClusterIdentifier': 'string',
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DbiResourceId': 'string',
            'CACertificateIdentifier': 'string',
            'DomainMemberships': [
                {
                    'Domain': 'string',
                    'Status': 'string',
                    'FQDN': 'string',
                    'IAMRoleName': 'string'
                },
            ],
            'CopyTagsToSnapshot': True|False,
            'MonitoringInterval': 123,
            'EnhancedMonitoringResourceArn': 'string',
            'MonitoringRoleArn': 'string',
            'PromotionTier': 123,
            'DBInstanceArn': 'string',
            'Timezone': 'string',
            'IAMDatabaseAuthenticationEnabled': True|False,
            'PerformanceInsightsEnabled': True|False,
            'PerformanceInsightsKMSKeyId': 'string',
            'EnabledCloudwatchLogsExports': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    ModifyDBInstance
    RebootDBInstance
    
    """
    pass

def create_db_parameter_group(DBParameterGroupName=None, DBParameterGroupFamily=None, Description=None, Tags=None):
    """
    Creates a new DB parameter group.
    A DB parameter group is initially created with the default parameters for the database engine used by the DB instance. To provide custom values for any of the parameters, you must modify the group after creating it using ModifyDBParameterGroup . Once you've created a DB parameter group, you need to associate it with your DB instance using ModifyDBInstance . When you associate a new DB parameter group with a running DB instance, you need to reboot the DB instance without failover for the new DB parameter group and associated settings to take effect.
    See also: AWS API Documentation
    
    
    :example: response = client.create_db_parameter_group(
        DBParameterGroupName='string',
        DBParameterGroupFamily='string',
        Description='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type DBParameterGroupName: string
    :param DBParameterGroupName: [REQUIRED]
            The name of the DB parameter group.
            Constraints:
            Must be 1 to 255 letters, numbers, or hyphens.
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            Note
            This value is stored as a lowercase string.
            

    :type DBParameterGroupFamily: string
    :param DBParameterGroupFamily: [REQUIRED]
            The DB parameter group family name. A DB parameter group can be associated with one and only one DB parameter group family, and can be applied only to a DB instance running a database engine and engine version compatible with that DB parameter group family.
            

    :type Description: string
    :param Description: [REQUIRED]
            The description for the DB parameter group.
            

    :type Tags: list
    :param Tags: A list of tags. For more information, see Tagging Amazon Neptune Resources .
            (dict) --Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can't be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can't be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            

    :rtype: dict
    :return: {
        'DBParameterGroup': {
            'DBParameterGroupName': 'string',
            'DBParameterGroupFamily': 'string',
            'Description': 'string',
            'DBParameterGroupArn': 'string'
        }
    }
    
    
    """
    pass

def create_db_subnet_group(DBSubnetGroupName=None, DBSubnetGroupDescription=None, SubnetIds=None, Tags=None):
    """
    Creates a new DB subnet group. DB subnet groups must contain at least one subnet in at least two AZs in the AWS Region.
    See also: AWS API Documentation
    
    
    :example: response = client.create_db_subnet_group(
        DBSubnetGroupName='string',
        DBSubnetGroupDescription='string',
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
    
    
    :type DBSubnetGroupName: string
    :param DBSubnetGroupName: [REQUIRED]
            The name for the DB subnet group. This value is stored as a lowercase string.
            Constraints: Must contain no more than 255 letters, numbers, periods, underscores, spaces, or hyphens. Must not be default.
            Example: mySubnetgroup
            

    :type DBSubnetGroupDescription: string
    :param DBSubnetGroupDescription: [REQUIRED]
            The description for the DB subnet group.
            

    :type SubnetIds: list
    :param SubnetIds: [REQUIRED]
            The EC2 Subnet IDs for the DB subnet group.
            (string) --
            

    :type Tags: list
    :param Tags: A list of tags. For more information, see Tagging Amazon Neptune Resources .
            (dict) --Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can't be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can't be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            

    :rtype: dict
    :return: {
        'DBSubnetGroup': {
            'DBSubnetGroupName': 'string',
            'DBSubnetGroupDescription': 'string',
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
            ],
            'DBSubnetGroupArn': 'string'
        }
    }
    
    
    :returns: 
    OrderableDBInstanceOption
    
    """
    pass

def create_event_subscription(SubscriptionName=None, SnsTopicArn=None, SourceType=None, EventCategories=None, SourceIds=None, Enabled=None, Tags=None):
    """
    Creates an event notification subscription. This action requires a topic ARN (Amazon Resource Name) created by either the Neptune console, the SNS console, or the SNS API. To obtain an ARN with SNS, you must create a topic in Amazon SNS and subscribe to the topic. The ARN is displayed in the SNS console.
    You can specify the type of source (SourceType) you want to be notified of, provide a list of Neptune sources (SourceIds) that triggers the events, and provide a list of event categories (EventCategories) for events you want to be notified of. For example, you can specify SourceType = db-instance, SourceIds = mydbinstance1, mydbinstance2 and EventCategories = Availability, Backup.
    If you specify both the SourceType and SourceIds, such as SourceType = db-instance and SourceIdentifier = myDBInstance1, you are notified of all the db-instance events for the specified source. If you specify a SourceType but do not specify a SourceIdentifier, you receive notice of the events for that source type for all your Neptune sources. If you do not specify either the SourceType nor the SourceIdentifier, you are notified of events generated from all Neptune sources belonging to your customer account.
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
            The name of the subscription.
            Constraints: The name must be less than 255 characters.
            

    :type SnsTopicArn: string
    :param SnsTopicArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.
            

    :type SourceType: string
    :param SourceType: The type of source that is generating the events. For example, if you want to be notified of events generated by a DB instance, you would set this parameter to db-instance. if this value is not specified, all events are returned.
            Valid values: db-instance | db-cluster | db-parameter-group | db-security-group | db-snapshot | db-cluster-snapshot
            

    :type EventCategories: list
    :param EventCategories: A list of event categories for a SourceType that you want to subscribe to. You can see a list of the categories for a given SourceType by using the DescribeEventCategories action.
            (string) --
            

    :type SourceIds: list
    :param SourceIds: The list of identifiers of the event sources for which events are returned. If not specified, then all sources are included in the response. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens; it can't end with a hyphen or contain two consecutive hyphens.
            Constraints:
            If SourceIds are supplied, SourceType must also be provided.
            If the source type is a DB instance, then a DBInstanceIdentifier must be supplied.
            If the source type is a DB security group, a DBSecurityGroupName must be supplied.
            If the source type is a DB parameter group, a DBParameterGroupName must be supplied.
            If the source type is a DB snapshot, a DBSnapshotIdentifier must be supplied.
            (string) --
            

    :type Enabled: boolean
    :param Enabled: A Boolean value; set to true to activate the subscription, set to false to create the subscription but not active it.

    :type Tags: list
    :param Tags: A list of tags. For more information, see Tagging Amazon Neptune Resources .
            (dict) --Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can't be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can't be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            

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
            'Enabled': True|False,
            'EventSubscriptionArn': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_db_cluster(DBClusterIdentifier=None, SkipFinalSnapshot=None, FinalDBSnapshotIdentifier=None):
    """
    The DeleteDBCluster action deletes a previously provisioned DB cluster. When you delete a DB cluster, all automated backups for that DB cluster are deleted and can't be recovered. Manual DB cluster snapshots of the specified DB cluster are not deleted.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_db_cluster(
        DBClusterIdentifier='string',
        SkipFinalSnapshot=True|False,
        FinalDBSnapshotIdentifier='string'
    )
    
    
    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]
            The DB cluster identifier for the DB cluster to be deleted. This parameter isn't case-sensitive.
            Constraints:
            Must match an existing DBClusterIdentifier.
            

    :type SkipFinalSnapshot: boolean
    :param SkipFinalSnapshot: Determines whether a final DB cluster snapshot is created before the DB cluster is deleted. If true is specified, no DB cluster snapshot is created. If false is specified, a DB cluster snapshot is created before the DB cluster is deleted.
            Note
            You must specify a FinalDBSnapshotIdentifier parameter if SkipFinalSnapshot is false .
            Default: false
            

    :type FinalDBSnapshotIdentifier: string
    :param FinalDBSnapshotIdentifier: The DB cluster snapshot identifier of the new DB cluster snapshot created when SkipFinalSnapshot is set to false .
            Note
            Specifying this parameter and also setting the SkipFinalShapshot parameter to true results in an error.
            Constraints:
            Must be 1 to 255 letters, numbers, or hyphens.
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            

    :rtype: dict
    :return: {
        'DBCluster': {
            'AllocatedStorage': 123,
            'AvailabilityZones': [
                'string',
            ],
            'BackupRetentionPeriod': 123,
            'CharacterSetName': 'string',
            'DatabaseName': 'string',
            'DBClusterIdentifier': 'string',
            'DBClusterParameterGroup': 'string',
            'DBSubnetGroup': 'string',
            'Status': 'string',
            'PercentProgress': 'string',
            'EarliestRestorableTime': datetime(2015, 1, 1),
            'Endpoint': 'string',
            'ReaderEndpoint': 'string',
            'MultiAZ': True|False,
            'Engine': 'string',
            'EngineVersion': 'string',
            'LatestRestorableTime': datetime(2015, 1, 1),
            'Port': 123,
            'MasterUsername': 'string',
            'DBClusterOptionGroupMemberships': [
                {
                    'DBClusterOptionGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'PreferredBackupWindow': 'string',
            'PreferredMaintenanceWindow': 'string',
            'ReplicationSourceIdentifier': 'string',
            'ReadReplicaIdentifiers': [
                'string',
            ],
            'DBClusterMembers': [
                {
                    'DBInstanceIdentifier': 'string',
                    'IsClusterWriter': True|False,
                    'DBClusterParameterGroupStatus': 'string',
                    'PromotionTier': 123
                },
            ],
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'HostedZoneId': 'string',
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DbClusterResourceId': 'string',
            'DBClusterArn': 'string',
            'AssociatedRoles': [
                {
                    'RoleArn': 'string',
                    'Status': 'string'
                },
            ],
            'IAMDatabaseAuthenticationEnabled': True|False,
            'CloneGroupId': 'string',
            'ClusterCreateTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_db_cluster_parameter_group(DBClusterParameterGroupName=None):
    """
    Deletes a specified DB cluster parameter group. The DB cluster parameter group to be deleted can't be associated with any DB clusters.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_db_cluster_parameter_group(
        DBClusterParameterGroupName='string'
    )
    
    
    :type DBClusterParameterGroupName: string
    :param DBClusterParameterGroupName: [REQUIRED]
            The name of the DB cluster parameter group.
            Constraints:
            Must be the name of an existing DB cluster parameter group.
            You can't delete a default DB cluster parameter group.
            Cannot be associated with any DB clusters.
            

    """
    pass

def delete_db_cluster_snapshot(DBClusterSnapshotIdentifier=None):
    """
    Deletes a DB cluster snapshot. If the snapshot is being copied, the copy operation is terminated.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_db_cluster_snapshot(
        DBClusterSnapshotIdentifier='string'
    )
    
    
    :type DBClusterSnapshotIdentifier: string
    :param DBClusterSnapshotIdentifier: [REQUIRED]
            The identifier of the DB cluster snapshot to delete.
            Constraints: Must be the name of an existing DB cluster snapshot in the available state.
            

    :rtype: dict
    :return: {
        'DBClusterSnapshot': {
            'AvailabilityZones': [
                'string',
            ],
            'DBClusterSnapshotIdentifier': 'string',
            'DBClusterIdentifier': 'string',
            'SnapshotCreateTime': datetime(2015, 1, 1),
            'Engine': 'string',
            'AllocatedStorage': 123,
            'Status': 'string',
            'Port': 123,
            'VpcId': 'string',
            'ClusterCreateTime': datetime(2015, 1, 1),
            'MasterUsername': 'string',
            'EngineVersion': 'string',
            'LicenseModel': 'string',
            'SnapshotType': 'string',
            'PercentProgress': 123,
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DBClusterSnapshotArn': 'string',
            'SourceDBClusterSnapshotArn': 'string',
            'IAMDatabaseAuthenticationEnabled': True|False
        }
    }
    
    
    """
    pass

def delete_db_instance(DBInstanceIdentifier=None, SkipFinalSnapshot=None, FinalDBSnapshotIdentifier=None):
    """
    The DeleteDBInstance action deletes a previously provisioned DB instance. When you delete a DB instance, all automated backups for that instance are deleted and can't be recovered. Manual DB snapshots of the DB instance to be deleted by DeleteDBInstance are not deleted.
    If you request a final DB snapshot the status of the Amazon Neptune DB instance is deleting until the DB snapshot is created. The API action DescribeDBInstance is used to monitor the status of this operation. The action can't be canceled or reverted once submitted.
    Note that when a DB instance is in a failure state and has a status of failed , incompatible-restore , or incompatible-network , you can only delete it when the SkipFinalSnapshot parameter is set to true .
    If the specified DB instance is part of a DB cluster, you can't delete the DB instance if both of the following conditions are true:
    To delete a DB instance in this case, first call the  PromoteReadReplicaDBCluster API action to promote the DB cluster so it's no longer a Read Replica. After the promotion completes, then call the DeleteDBInstance API action to delete the final instance in the DB cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_db_instance(
        DBInstanceIdentifier='string',
        SkipFinalSnapshot=True|False,
        FinalDBSnapshotIdentifier='string'
    )
    
    
    :type DBInstanceIdentifier: string
    :param DBInstanceIdentifier: [REQUIRED]
            The DB instance identifier for the DB instance to be deleted. This parameter isn't case-sensitive.
            Constraints:
            Must match the name of an existing DB instance.
            

    :type SkipFinalSnapshot: boolean
    :param SkipFinalSnapshot: Determines whether a final DB snapshot is created before the DB instance is deleted. If true is specified, no DBSnapshot is created. If false is specified, a DB snapshot is created before the DB instance is deleted.
            Note that when a DB instance is in a failure state and has a status of 'failed', 'incompatible-restore', or 'incompatible-network', it can only be deleted when the SkipFinalSnapshot parameter is set to 'true'.
            Specify true when deleting a Read Replica.
            Note
            The FinalDBSnapshotIdentifier parameter must be specified if SkipFinalSnapshot is false .
            Default: false
            

    :type FinalDBSnapshotIdentifier: string
    :param FinalDBSnapshotIdentifier: The DBSnapshotIdentifier of the new DBSnapshot created when SkipFinalSnapshot is set to false .
            Note
            Specifying this parameter and also setting the SkipFinalShapshot parameter to true results in an error.
            Constraints:
            Must be 1 to 255 letters or numbers.
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            Cannot be specified when deleting a Read Replica.
            

    :rtype: dict
    :return: {
        'DBInstance': {
            'DBInstanceIdentifier': 'string',
            'DBInstanceClass': 'string',
            'Engine': 'string',
            'DBInstanceStatus': 'string',
            'MasterUsername': 'string',
            'DBName': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123,
                'HostedZoneId': 'string'
            },
            'AllocatedStorage': 123,
            'InstanceCreateTime': datetime(2015, 1, 1),
            'PreferredBackupWindow': 'string',
            'BackupRetentionPeriod': 123,
            'DBSecurityGroups': [
                {
                    'DBSecurityGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'DBParameterGroups': [
                {
                    'DBParameterGroupName': 'string',
                    'ParameterApplyStatus': 'string'
                },
            ],
            'AvailabilityZone': 'string',
            'DBSubnetGroup': {
                'DBSubnetGroupName': 'string',
                'DBSubnetGroupDescription': 'string',
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
                ],
                'DBSubnetGroupArn': 'string'
            },
            'PreferredMaintenanceWindow': 'string',
            'PendingModifiedValues': {
                'DBInstanceClass': 'string',
                'AllocatedStorage': 123,
                'MasterUserPassword': 'string',
                'Port': 123,
                'BackupRetentionPeriod': 123,
                'MultiAZ': True|False,
                'EngineVersion': 'string',
                'LicenseModel': 'string',
                'Iops': 123,
                'DBInstanceIdentifier': 'string',
                'StorageType': 'string',
                'CACertificateIdentifier': 'string',
                'DBSubnetGroupName': 'string',
                'PendingCloudwatchLogsExports': {
                    'LogTypesToEnable': [
                        'string',
                    ],
                    'LogTypesToDisable': [
                        'string',
                    ]
                }
            },
            'LatestRestorableTime': datetime(2015, 1, 1),
            'MultiAZ': True|False,
            'EngineVersion': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'ReadReplicaSourceDBInstanceIdentifier': 'string',
            'ReadReplicaDBInstanceIdentifiers': [
                'string',
            ],
            'ReadReplicaDBClusterIdentifiers': [
                'string',
            ],
            'LicenseModel': 'string',
            'Iops': 123,
            'OptionGroupMemberships': [
                {
                    'OptionGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'CharacterSetName': 'string',
            'SecondaryAvailabilityZone': 'string',
            'PubliclyAccessible': True|False,
            'StatusInfos': [
                {
                    'StatusType': 'string',
                    'Normal': True|False,
                    'Status': 'string',
                    'Message': 'string'
                },
            ],
            'StorageType': 'string',
            'TdeCredentialArn': 'string',
            'DbInstancePort': 123,
            'DBClusterIdentifier': 'string',
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DbiResourceId': 'string',
            'CACertificateIdentifier': 'string',
            'DomainMemberships': [
                {
                    'Domain': 'string',
                    'Status': 'string',
                    'FQDN': 'string',
                    'IAMRoleName': 'string'
                },
            ],
            'CopyTagsToSnapshot': True|False,
            'MonitoringInterval': 123,
            'EnhancedMonitoringResourceArn': 'string',
            'MonitoringRoleArn': 'string',
            'PromotionTier': 123,
            'DBInstanceArn': 'string',
            'Timezone': 'string',
            'IAMDatabaseAuthenticationEnabled': True|False,
            'PerformanceInsightsEnabled': True|False,
            'PerformanceInsightsKMSKeyId': 'string',
            'EnabledCloudwatchLogsExports': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    DBInstanceIdentifier (string) -- [REQUIRED]
    The DB instance identifier for the DB instance to be deleted. This parameter isn't case-sensitive.
    Constraints:
    
    Must match the name of an existing DB instance.
    
    
    SkipFinalSnapshot (boolean) -- Determines whether a final DB snapshot is created before the DB instance is deleted. If true is specified, no DBSnapshot is created. If false is specified, a DB snapshot is created before the DB instance is deleted.
    Note that when a DB instance is in a failure state and has a status of 'failed', 'incompatible-restore', or 'incompatible-network', it can only be deleted when the SkipFinalSnapshot parameter is set to "true".
    Specify true when deleting a Read Replica.
    
    Note
    The FinalDBSnapshotIdentifier parameter must be specified if SkipFinalSnapshot is false .
    
    Default: false
    
    FinalDBSnapshotIdentifier (string) -- The DBSnapshotIdentifier of the new DBSnapshot created when SkipFinalSnapshot is set to false .
    
    Note
    Specifying this parameter and also setting the SkipFinalShapshot parameter to true results in an error.
    
    Constraints:
    
    Must be 1 to 255 letters or numbers.
    First character must be a letter
    Cannot end with a hyphen or contain two consecutive hyphens
    Cannot be specified when deleting a Read Replica.
    
    
    
    """
    pass

def delete_db_parameter_group(DBParameterGroupName=None):
    """
    Deletes a specified DBParameterGroup. The DBParameterGroup to be deleted can't be associated with any DB instances.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_db_parameter_group(
        DBParameterGroupName='string'
    )
    
    
    :type DBParameterGroupName: string
    :param DBParameterGroupName: [REQUIRED]
            The name of the DB parameter group.
            Constraints:
            Must be the name of an existing DB parameter group
            You can't delete a default DB parameter group
            Cannot be associated with any DB instances
            

    """
    pass

def delete_db_subnet_group(DBSubnetGroupName=None):
    """
    Deletes a DB subnet group.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_db_subnet_group(
        DBSubnetGroupName='string'
    )
    
    
    :type DBSubnetGroupName: string
    :param DBSubnetGroupName: [REQUIRED]
            The name of the database subnet group to delete.
            Note
            You can't delete the default subnet group.
            Constraints:
            Constraints: Must match the name of an existing DBSubnetGroup. Must not be default.
            Example: mySubnetgroup
            

    """
    pass

def delete_event_subscription(SubscriptionName=None):
    """
    Deletes an event notification subscription.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_event_subscription(
        SubscriptionName='string'
    )
    
    
    :type SubscriptionName: string
    :param SubscriptionName: [REQUIRED]
            The name of the event notification subscription you want to delete.
            

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
            'Enabled': True|False,
            'EventSubscriptionArn': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_db_cluster_parameter_groups(DBClusterParameterGroupName=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns a list of DBClusterParameterGroup descriptions. If a DBClusterParameterGroupName parameter is specified, the list will contain only the description of the specified DB cluster parameter group.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_db_cluster_parameter_groups(
        DBClusterParameterGroupName='string',
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
    
    
    :type DBClusterParameterGroupName: string
    :param DBClusterParameterGroupName: The name of a specific DB cluster parameter group to return details for.
            Constraints:
            If supplied, must match the name of an existing DBClusterParameterGroup.
            

    :type Filters: list
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeDBClusterParameterGroups request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
    :return: {
        'Marker': 'string',
        'DBClusterParameterGroups': [
            {
                'DBClusterParameterGroupName': 'string',
                'DBParameterGroupFamily': 'string',
                'Description': 'string',
                'DBClusterParameterGroupArn': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_db_cluster_parameters(DBClusterParameterGroupName=None, Source=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns the detailed parameter list for a particular DB cluster parameter group.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_db_cluster_parameters(
        DBClusterParameterGroupName='string',
        Source='string',
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
    
    
    :type DBClusterParameterGroupName: string
    :param DBClusterParameterGroupName: [REQUIRED]
            The name of a specific DB cluster parameter group to return parameter details for.
            Constraints:
            If supplied, must match the name of an existing DBClusterParameterGroup.
            

    :type Source: string
    :param Source: A value that indicates to return only parameters for a specific source. Parameter sources can be engine , service , or customer .

    :type Filters: list
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeDBClusterParameters request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
    :return: {
        'Parameters': [
            {
                'ParameterName': 'string',
                'ParameterValue': 'string',
                'Description': 'string',
                'Source': 'string',
                'ApplyType': 'string',
                'DataType': 'string',
                'AllowedValues': 'string',
                'IsModifiable': True|False,
                'MinimumEngineVersion': 'string',
                'ApplyMethod': 'immediate'|'pending-reboot'
            },
        ],
        'Marker': 'string'
    }
    
    
    """
    pass

def describe_db_cluster_snapshot_attributes(DBClusterSnapshotIdentifier=None):
    """
    Returns a list of DB cluster snapshot attribute names and values for a manual DB cluster snapshot.
    When sharing snapshots with other AWS accounts, DescribeDBClusterSnapshotAttributes returns the restore attribute and a list of IDs for the AWS accounts that are authorized to copy or restore the manual DB cluster snapshot. If all is included in the list of values for the restore attribute, then the manual DB cluster snapshot is public and can be copied or restored by all AWS accounts.
    To add or remove access for an AWS account to copy or restore a manual DB cluster snapshot, or to make the manual DB cluster snapshot public or private, use the  ModifyDBClusterSnapshotAttribute API action.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_db_cluster_snapshot_attributes(
        DBClusterSnapshotIdentifier='string'
    )
    
    
    :type DBClusterSnapshotIdentifier: string
    :param DBClusterSnapshotIdentifier: [REQUIRED]
            The identifier for the DB cluster snapshot to describe the attributes for.
            

    :rtype: dict
    :return: {
        'DBClusterSnapshotAttributesResult': {
            'DBClusterSnapshotIdentifier': 'string',
            'DBClusterSnapshotAttributes': [
                {
                    'AttributeName': 'string',
                    'AttributeValues': [
                        'string',
                    ]
                },
            ]
        }
    }
    
    
    """
    pass

def describe_db_cluster_snapshots(DBClusterIdentifier=None, DBClusterSnapshotIdentifier=None, SnapshotType=None, Filters=None, MaxRecords=None, Marker=None, IncludeShared=None, IncludePublic=None):
    """
    Returns information about DB cluster snapshots. This API action supports pagination.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_db_cluster_snapshots(
        DBClusterIdentifier='string',
        DBClusterSnapshotIdentifier='string',
        SnapshotType='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string',
        IncludeShared=True|False,
        IncludePublic=True|False
    )
    
    
    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: The ID of the DB cluster to retrieve the list of DB cluster snapshots for. This parameter can't be used in conjunction with the DBClusterSnapshotIdentifier parameter. This parameter is not case-sensitive.
            Constraints:
            If supplied, must match the identifier of an existing DBCluster.
            

    :type DBClusterSnapshotIdentifier: string
    :param DBClusterSnapshotIdentifier: A specific DB cluster snapshot identifier to describe. This parameter can't be used in conjunction with the DBClusterIdentifier parameter. This value is stored as a lowercase string.
            Constraints:
            If supplied, must match the identifier of an existing DBClusterSnapshot.
            If this identifier is for an automated snapshot, the SnapshotType parameter must also be specified.
            

    :type SnapshotType: string
    :param SnapshotType: The type of DB cluster snapshots to be returned. You can specify one of the following values:
            automated - Return all DB cluster snapshots that have been automatically taken by Amazon Neptune for my AWS account.
            manual - Return all DB cluster snapshots that have been taken by my AWS account.
            shared - Return all manual DB cluster snapshots that have been shared to my AWS account.
            public - Return all DB cluster snapshots that have been marked as public.
            If you don't specify a SnapshotType value, then both automated and manual DB cluster snapshots are returned. You can include shared DB cluster snapshots with these results by setting the IncludeShared parameter to true . You can include public DB cluster snapshots with these results by setting the IncludePublic parameter to true .
            The IncludeShared and IncludePublic parameters don't apply for SnapshotType values of manual or automated . The IncludePublic parameter doesn't apply when SnapshotType is set to shared . The IncludeShared parameter doesn't apply when SnapshotType is set to public .
            

    :type Filters: list
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeDBClusterSnapshots request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :type IncludeShared: boolean
    :param IncludeShared: True to include shared manual DB cluster snapshots from other AWS accounts that this AWS account has been given permission to copy or restore, and otherwise false. The default is false .
            You can give an AWS account permission to restore a manual DB cluster snapshot from another AWS account by the ModifyDBClusterSnapshotAttribute API action.
            

    :type IncludePublic: boolean
    :param IncludePublic: True to include manual DB cluster snapshots that are public and can be copied or restored by any AWS account, and otherwise false. The default is false . The default is false.
            You can share a manual DB cluster snapshot as public by using the ModifyDBClusterSnapshotAttribute API action.
            

    :rtype: dict
    :return: {
        'Marker': 'string',
        'DBClusterSnapshots': [
            {
                'AvailabilityZones': [
                    'string',
                ],
                'DBClusterSnapshotIdentifier': 'string',
                'DBClusterIdentifier': 'string',
                'SnapshotCreateTime': datetime(2015, 1, 1),
                'Engine': 'string',
                'AllocatedStorage': 123,
                'Status': 'string',
                'Port': 123,
                'VpcId': 'string',
                'ClusterCreateTime': datetime(2015, 1, 1),
                'MasterUsername': 'string',
                'EngineVersion': 'string',
                'LicenseModel': 'string',
                'SnapshotType': 'string',
                'PercentProgress': 123,
                'StorageEncrypted': True|False,
                'KmsKeyId': 'string',
                'DBClusterSnapshotArn': 'string',
                'SourceDBClusterSnapshotArn': 'string',
                'IAMDatabaseAuthenticationEnabled': True|False
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_db_clusters(DBClusterIdentifier=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns information about provisioned DB clusters. This API supports pagination.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_db_clusters(
        DBClusterIdentifier='string',
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
    
    
    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: The user-supplied DB cluster identifier. If this parameter is specified, information from only the specific DB cluster is returned. This parameter isn't case-sensitive.
            Constraints:
            If supplied, must match an existing DBClusterIdentifier.
            

    :type Filters: list
    :param Filters: A filter that specifies one or more DB clusters to describe.
            Supported filters:
            db-cluster-id - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list will only include information about the DB clusters identified by these ARNs.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeDBClusters request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
    :return: {
        'Marker': 'string',
        'DBClusters': [
            {
                'AllocatedStorage': 123,
                'AvailabilityZones': [
                    'string',
                ],
                'BackupRetentionPeriod': 123,
                'CharacterSetName': 'string',
                'DatabaseName': 'string',
                'DBClusterIdentifier': 'string',
                'DBClusterParameterGroup': 'string',
                'DBSubnetGroup': 'string',
                'Status': 'string',
                'PercentProgress': 'string',
                'EarliestRestorableTime': datetime(2015, 1, 1),
                'Endpoint': 'string',
                'ReaderEndpoint': 'string',
                'MultiAZ': True|False,
                'Engine': 'string',
                'EngineVersion': 'string',
                'LatestRestorableTime': datetime(2015, 1, 1),
                'Port': 123,
                'MasterUsername': 'string',
                'DBClusterOptionGroupMemberships': [
                    {
                        'DBClusterOptionGroupName': 'string',
                        'Status': 'string'
                    },
                ],
                'PreferredBackupWindow': 'string',
                'PreferredMaintenanceWindow': 'string',
                'ReplicationSourceIdentifier': 'string',
                'ReadReplicaIdentifiers': [
                    'string',
                ],
                'DBClusterMembers': [
                    {
                        'DBInstanceIdentifier': 'string',
                        'IsClusterWriter': True|False,
                        'DBClusterParameterGroupStatus': 'string',
                        'PromotionTier': 123
                    },
                ],
                'VpcSecurityGroups': [
                    {
                        'VpcSecurityGroupId': 'string',
                        'Status': 'string'
                    },
                ],
                'HostedZoneId': 'string',
                'StorageEncrypted': True|False,
                'KmsKeyId': 'string',
                'DbClusterResourceId': 'string',
                'DBClusterArn': 'string',
                'AssociatedRoles': [
                    {
                        'RoleArn': 'string',
                        'Status': 'string'
                    },
                ],
                'IAMDatabaseAuthenticationEnabled': True|False,
                'CloneGroupId': 'string',
                'ClusterCreateTime': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_db_engine_versions(Engine=None, EngineVersion=None, DBParameterGroupFamily=None, Filters=None, MaxRecords=None, Marker=None, DefaultOnly=None, ListSupportedCharacterSets=None, ListSupportedTimezones=None):
    """
    Returns a list of the available DB engines.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_db_engine_versions(
        Engine='string',
        EngineVersion='string',
        DBParameterGroupFamily='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string',
        DefaultOnly=True|False,
        ListSupportedCharacterSets=True|False,
        ListSupportedTimezones=True|False
    )
    
    
    :type Engine: string
    :param Engine: The database engine to return.

    :type EngineVersion: string
    :param EngineVersion: The database engine version to return.
            Example: 5.1.49
            

    :type DBParameterGroupFamily: string
    :param DBParameterGroupFamily: The name of a specific DB parameter group family to return details for.
            Constraints:
            If supplied, must match an existing DBParameterGroupFamily.
            

    :type Filters: list
    :param Filters: Not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more than the MaxRecords value is available, a pagination token called a marker is included in the response so that the following results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :type DefaultOnly: boolean
    :param DefaultOnly: Indicates that only the default version of the specified engine or engine and major version combination is returned.

    :type ListSupportedCharacterSets: boolean
    :param ListSupportedCharacterSets: If this parameter is specified and the requested engine supports the CharacterSetName parameter for CreateDBInstance , the response includes a list of supported character sets for each engine version.

    :type ListSupportedTimezones: boolean
    :param ListSupportedTimezones: If this parameter is specified and the requested engine supports the TimeZone parameter for CreateDBInstance , the response includes a list of supported time zones for each engine version.

    :rtype: dict
    :return: {
        'Marker': 'string',
        'DBEngineVersions': [
            {
                'Engine': 'string',
                'EngineVersion': 'string',
                'DBParameterGroupFamily': 'string',
                'DBEngineDescription': 'string',
                'DBEngineVersionDescription': 'string',
                'DefaultCharacterSet': {
                    'CharacterSetName': 'string',
                    'CharacterSetDescription': 'string'
                },
                'SupportedCharacterSets': [
                    {
                        'CharacterSetName': 'string',
                        'CharacterSetDescription': 'string'
                    },
                ],
                'ValidUpgradeTarget': [
                    {
                        'Engine': 'string',
                        'EngineVersion': 'string',
                        'Description': 'string',
                        'AutoUpgrade': True|False,
                        'IsMajorVersionUpgrade': True|False
                    },
                ],
                'SupportedTimezones': [
                    {
                        'TimezoneName': 'string'
                    },
                ],
                'ExportableLogTypes': [
                    'string',
                ],
                'SupportsLogExportsToCloudwatchLogs': True|False,
                'SupportsReadReplica': True|False
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_db_instances(DBInstanceIdentifier=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns information about provisioned instances. This API supports pagination.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_db_instances(
        DBInstanceIdentifier='string',
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
    
    
    :type DBInstanceIdentifier: string
    :param DBInstanceIdentifier: The user-supplied instance identifier. If this parameter is specified, information from only the specific DB instance is returned. This parameter isn't case-sensitive.
            Constraints:
            If supplied, must match the identifier of an existing DBInstance.
            

    :type Filters: list
    :param Filters: A filter that specifies one or more DB instances to describe.
            Supported filters:
            db-cluster-id - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list will only include information about the DB instances associated with the DB clusters identified by these ARNs.
            db-instance-id - Accepts DB instance identifiers and DB instance Amazon Resource Names (ARNs). The results list will only include information about the DB instances identified by these ARNs.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeDBInstances request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
    :return: {
        'Marker': 'string',
        'DBInstances': [
            {
                'DBInstanceIdentifier': 'string',
                'DBInstanceClass': 'string',
                'Engine': 'string',
                'DBInstanceStatus': 'string',
                'MasterUsername': 'string',
                'DBName': 'string',
                'Endpoint': {
                    'Address': 'string',
                    'Port': 123,
                    'HostedZoneId': 'string'
                },
                'AllocatedStorage': 123,
                'InstanceCreateTime': datetime(2015, 1, 1),
                'PreferredBackupWindow': 'string',
                'BackupRetentionPeriod': 123,
                'DBSecurityGroups': [
                    {
                        'DBSecurityGroupName': 'string',
                        'Status': 'string'
                    },
                ],
                'VpcSecurityGroups': [
                    {
                        'VpcSecurityGroupId': 'string',
                        'Status': 'string'
                    },
                ],
                'DBParameterGroups': [
                    {
                        'DBParameterGroupName': 'string',
                        'ParameterApplyStatus': 'string'
                    },
                ],
                'AvailabilityZone': 'string',
                'DBSubnetGroup': {
                    'DBSubnetGroupName': 'string',
                    'DBSubnetGroupDescription': 'string',
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
                    ],
                    'DBSubnetGroupArn': 'string'
                },
                'PreferredMaintenanceWindow': 'string',
                'PendingModifiedValues': {
                    'DBInstanceClass': 'string',
                    'AllocatedStorage': 123,
                    'MasterUserPassword': 'string',
                    'Port': 123,
                    'BackupRetentionPeriod': 123,
                    'MultiAZ': True|False,
                    'EngineVersion': 'string',
                    'LicenseModel': 'string',
                    'Iops': 123,
                    'DBInstanceIdentifier': 'string',
                    'StorageType': 'string',
                    'CACertificateIdentifier': 'string',
                    'DBSubnetGroupName': 'string',
                    'PendingCloudwatchLogsExports': {
                        'LogTypesToEnable': [
                            'string',
                        ],
                        'LogTypesToDisable': [
                            'string',
                        ]
                    }
                },
                'LatestRestorableTime': datetime(2015, 1, 1),
                'MultiAZ': True|False,
                'EngineVersion': 'string',
                'AutoMinorVersionUpgrade': True|False,
                'ReadReplicaSourceDBInstanceIdentifier': 'string',
                'ReadReplicaDBInstanceIdentifiers': [
                    'string',
                ],
                'ReadReplicaDBClusterIdentifiers': [
                    'string',
                ],
                'LicenseModel': 'string',
                'Iops': 123,
                'OptionGroupMemberships': [
                    {
                        'OptionGroupName': 'string',
                        'Status': 'string'
                    },
                ],
                'CharacterSetName': 'string',
                'SecondaryAvailabilityZone': 'string',
                'PubliclyAccessible': True|False,
                'StatusInfos': [
                    {
                        'StatusType': 'string',
                        'Normal': True|False,
                        'Status': 'string',
                        'Message': 'string'
                    },
                ],
                'StorageType': 'string',
                'TdeCredentialArn': 'string',
                'DbInstancePort': 123,
                'DBClusterIdentifier': 'string',
                'StorageEncrypted': True|False,
                'KmsKeyId': 'string',
                'DbiResourceId': 'string',
                'CACertificateIdentifier': 'string',
                'DomainMemberships': [
                    {
                        'Domain': 'string',
                        'Status': 'string',
                        'FQDN': 'string',
                        'IAMRoleName': 'string'
                    },
                ],
                'CopyTagsToSnapshot': True|False,
                'MonitoringInterval': 123,
                'EnhancedMonitoringResourceArn': 'string',
                'MonitoringRoleArn': 'string',
                'PromotionTier': 123,
                'DBInstanceArn': 'string',
                'Timezone': 'string',
                'IAMDatabaseAuthenticationEnabled': True|False,
                'PerformanceInsightsEnabled': True|False,
                'PerformanceInsightsKMSKeyId': 'string',
                'EnabledCloudwatchLogsExports': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    ModifyDBInstance
    RebootDBInstance
    
    """
    pass

def describe_db_parameter_groups(DBParameterGroupName=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns a list of DBParameterGroup descriptions. If a DBParameterGroupName is specified, the list will contain only the description of the specified DB parameter group.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_db_parameter_groups(
        DBParameterGroupName='string',
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
    
    
    :type DBParameterGroupName: string
    :param DBParameterGroupName: The name of a specific DB parameter group to return details for.
            Constraints:
            If supplied, must match the name of an existing DBClusterParameterGroup.
            

    :type Filters: list
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeDBParameterGroups request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
    :return: {
        'Marker': 'string',
        'DBParameterGroups': [
            {
                'DBParameterGroupName': 'string',
                'DBParameterGroupFamily': 'string',
                'Description': 'string',
                'DBParameterGroupArn': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_db_parameters(DBParameterGroupName=None, Source=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns the detailed parameter list for a particular DB parameter group.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_db_parameters(
        DBParameterGroupName='string',
        Source='string',
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
    
    
    :type DBParameterGroupName: string
    :param DBParameterGroupName: [REQUIRED]
            The name of a specific DB parameter group to return details for.
            Constraints:
            If supplied, must match the name of an existing DBParameterGroup.
            

    :type Source: string
    :param Source: The parameter types to return.
            Default: All parameter types returned
            Valid Values: user | system | engine-default
            

    :type Filters: list
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeDBParameters request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
    :return: {
        'Parameters': [
            {
                'ParameterName': 'string',
                'ParameterValue': 'string',
                'Description': 'string',
                'Source': 'string',
                'ApplyType': 'string',
                'DataType': 'string',
                'AllowedValues': 'string',
                'IsModifiable': True|False,
                'MinimumEngineVersion': 'string',
                'ApplyMethod': 'immediate'|'pending-reboot'
            },
        ],
        'Marker': 'string'
    }
    
    
    """
    pass

def describe_db_subnet_groups(DBSubnetGroupName=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns a list of DBSubnetGroup descriptions. If a DBSubnetGroupName is specified, the list will contain only the descriptions of the specified DBSubnetGroup.
    For an overview of CIDR ranges, go to the Wikipedia Tutorial .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_db_subnet_groups(
        DBSubnetGroupName='string',
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
    
    
    :type DBSubnetGroupName: string
    :param DBSubnetGroupName: The name of the DB subnet group to return details for.

    :type Filters: list
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeDBSubnetGroups request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
    :return: {
        'Marker': 'string',
        'DBSubnetGroups': [
            {
                'DBSubnetGroupName': 'string',
                'DBSubnetGroupDescription': 'string',
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
                ],
                'DBSubnetGroupArn': 'string'
            },
        ]
    }
    
    
    :returns: 
    OrderableDBInstanceOption
    
    """
    pass

def describe_engine_default_cluster_parameters(DBParameterGroupFamily=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns the default engine and system parameter information for the cluster database engine.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_engine_default_cluster_parameters(
        DBParameterGroupFamily='string',
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
    
    
    :type DBParameterGroupFamily: string
    :param DBParameterGroupFamily: [REQUIRED]
            The name of the DB cluster parameter group family to return engine parameter information for.
            

    :type Filters: list
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeEngineDefaultClusterParameters request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
    :return: {
        'EngineDefaults': {
            'DBParameterGroupFamily': 'string',
            'Marker': 'string',
            'Parameters': [
                {
                    'ParameterName': 'string',
                    'ParameterValue': 'string',
                    'Description': 'string',
                    'Source': 'string',
                    'ApplyType': 'string',
                    'DataType': 'string',
                    'AllowedValues': 'string',
                    'IsModifiable': True|False,
                    'MinimumEngineVersion': 'string',
                    'ApplyMethod': 'immediate'|'pending-reboot'
                },
            ]
        }
    }
    
    
    """
    pass

def describe_engine_default_parameters(DBParameterGroupFamily=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns the default engine and system parameter information for the specified database engine.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_engine_default_parameters(
        DBParameterGroupFamily='string',
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
    
    
    :type DBParameterGroupFamily: string
    :param DBParameterGroupFamily: [REQUIRED]
            The name of the DB parameter group family.
            

    :type Filters: list
    :param Filters: Not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeEngineDefaultParameters request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
    :return: {
        'EngineDefaults': {
            'DBParameterGroupFamily': 'string',
            'Marker': 'string',
            'Parameters': [
                {
                    'ParameterName': 'string',
                    'ParameterValue': 'string',
                    'Description': 'string',
                    'Source': 'string',
                    'ApplyType': 'string',
                    'DataType': 'string',
                    'AllowedValues': 'string',
                    'IsModifiable': True|False,
                    'MinimumEngineVersion': 'string',
                    'ApplyMethod': 'immediate'|'pending-reboot'
                },
            ]
        }
    }
    
    
    """
    pass

def describe_event_categories(SourceType=None, Filters=None):
    """
    Displays a list of categories for all event source types, or, if specified, for a specified source type.
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
    :param SourceType: The type of source that is generating the events.
            Valid values: db-instance | db-parameter-group | db-security-group | db-snapshot
            

    :type Filters: list
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            

    :rtype: dict
    :return: {
        'EventCategoriesMapList': [
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
    Lists all the subscription descriptions for a customer account. The description for a subscription includes SubscriptionName, SNSTopicARN, CustomerID, SourceType, SourceID, CreationTime, and Status.
    If you specify a SubscriptionName, lists the description for that subscription.
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
    :param SubscriptionName: The name of the event notification subscription you want to describe.

    :type Filters: list
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeOrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

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
                'Enabled': True|False,
                'EventSubscriptionArn': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_events(SourceIdentifier=None, SourceType=None, StartTime=None, EndTime=None, Duration=None, EventCategories=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns events related to DB instances, DB security groups, DB snapshots, and DB parameter groups for the past 14 days. Events specific to a particular DB instance, DB security group, database snapshot, or DB parameter group can be obtained by providing the name as a parameter. By default, the past hour of events are returned.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_events(
        SourceIdentifier='string',
        SourceType='db-instance'|'db-parameter-group'|'db-security-group'|'db-snapshot'|'db-cluster'|'db-cluster-snapshot',
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
    :param SourceIdentifier: The identifier of the event source for which events are returned. If not specified, then all sources are included in the response.
            Constraints:
            If SourceIdentifier is supplied, SourceType must also be provided.
            If the source type is DBInstance , then a DBInstanceIdentifier must be supplied.
            If the source type is DBSecurityGroup , a DBSecurityGroupName must be supplied.
            If the source type is DBParameterGroup , a DBParameterGroupName must be supplied.
            If the source type is DBSnapshot , a DBSnapshotIdentifier must be supplied.
            Cannot end with a hyphen or contain two consecutive hyphens.
            

    :type SourceType: string
    :param SourceType: The event source to retrieve events for. If no value is specified, all events are returned.

    :type StartTime: datetime
    :param StartTime: The beginning of the time interval to retrieve events for, specified in ISO 8601 format. For more information about ISO 8601, go to the ISO8601 Wikipedia page.
            Example: 2009-07-08T18:00Z
            

    :type EndTime: datetime
    :param EndTime: The end of the time interval for which to retrieve events, specified in ISO 8601 format. For more information about ISO 8601, go to the ISO8601 Wikipedia page.
            Example: 2009-07-08T18:00Z
            

    :type Duration: integer
    :param Duration: The number of minutes to retrieve events for.
            Default: 60
            

    :type EventCategories: list
    :param EventCategories: A list of event categories that trigger notifications for a event notification subscription.
            (string) --
            

    :type Filters: list
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeEvents request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
    :return: {
        'Marker': 'string',
        'Events': [
            {
                'SourceIdentifier': 'string',
                'SourceType': 'db-instance'|'db-parameter-group'|'db-security-group'|'db-snapshot'|'db-cluster'|'db-cluster-snapshot',
                'Message': 'string',
                'EventCategories': [
                    'string',
                ],
                'Date': datetime(2015, 1, 1),
                'SourceArn': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_orderable_db_instance_options(Engine=None, EngineVersion=None, DBInstanceClass=None, LicenseModel=None, Vpc=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns a list of orderable DB instance options for the specified engine.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_orderable_db_instance_options(
        Engine='string',
        EngineVersion='string',
        DBInstanceClass='string',
        LicenseModel='string',
        Vpc=True|False,
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
    
    
    :type Engine: string
    :param Engine: [REQUIRED]
            The name of the engine to retrieve DB instance options for.
            

    :type EngineVersion: string
    :param EngineVersion: The engine version filter value. Specify this parameter to show only the available offerings matching the specified engine version.

    :type DBInstanceClass: string
    :param DBInstanceClass: The DB instance class filter value. Specify this parameter to show only the available offerings matching the specified DB instance class.

    :type LicenseModel: string
    :param LicenseModel: The license model filter value. Specify this parameter to show only the available offerings matching the specified license model.

    :type Vpc: boolean
    :param Vpc: The VPC filter value. Specify this parameter to show only the available VPC or non-VPC offerings.

    :type Filters: list
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeOrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
    :return: {
        'OrderableDBInstanceOptions': [
            {
                'Engine': 'string',
                'EngineVersion': 'string',
                'DBInstanceClass': 'string',
                'LicenseModel': 'string',
                'AvailabilityZones': [
                    {
                        'Name': 'string'
                    },
                ],
                'MultiAZCapable': True|False,
                'ReadReplicaCapable': True|False,
                'Vpc': True|False,
                'SupportsStorageEncryption': True|False,
                'StorageType': 'string',
                'SupportsIops': True|False,
                'SupportsEnhancedMonitoring': True|False,
                'SupportsIAMDatabaseAuthentication': True|False,
                'SupportsPerformanceInsights': True|False,
                'MinStorageSize': 123,
                'MaxStorageSize': 123,
                'MinIopsPerDbInstance': 123,
                'MaxIopsPerDbInstance': 123,
                'MinIopsPerGib': 123.0,
                'MaxIopsPerGib': 123.0
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    OrderableDBInstanceOption
    
    """
    pass

def describe_pending_maintenance_actions(ResourceIdentifier=None, Filters=None, Marker=None, MaxRecords=None):
    """
    Returns a list of resources (for example, DB instances) that have at least one pending maintenance action.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_pending_maintenance_actions(
        ResourceIdentifier='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        Marker='string',
        MaxRecords=123
    )
    
    
    :type ResourceIdentifier: string
    :param ResourceIdentifier: The ARN of a resource to return pending maintenance actions for.

    :type Filters: list
    :param Filters: A filter that specifies one or more resources to return pending maintenance actions for.
            Supported filters:
            db-cluster-id - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list will only include pending maintenance actions for the DB clusters identified by these ARNs.
            db-instance-id - Accepts DB instance identifiers and DB instance ARNs. The results list will only include pending maintenance actions for the DB instances identified by these ARNs.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribePendingMaintenanceActions request. If this parameter is specified, the response includes only records beyond the marker, up to a number of records specified by MaxRecords .

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            

    :rtype: dict
    :return: {
        'PendingMaintenanceActions': [
            {
                'ResourceIdentifier': 'string',
                'PendingMaintenanceActionDetails': [
                    {
                        'Action': 'string',
                        'AutoAppliedAfterDate': datetime(2015, 1, 1),
                        'ForcedApplyDate': datetime(2015, 1, 1),
                        'OptInStatus': 'string',
                        'CurrentApplyDate': datetime(2015, 1, 1),
                        'Description': 'string'
                    },
                ]
            },
        ],
        'Marker': 'string'
    }
    
    
    """
    pass

def describe_valid_db_instance_modifications(DBInstanceIdentifier=None):
    """
    You can call  DescribeValidDBInstanceModifications to learn what modifications you can make to your DB instance. You can use this information when you call  ModifyDBInstance .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_valid_db_instance_modifications(
        DBInstanceIdentifier='string'
    )
    
    
    :type DBInstanceIdentifier: string
    :param DBInstanceIdentifier: [REQUIRED]
            The customer identifier or the ARN of your DB instance.
            

    :rtype: dict
    :return: {
        'ValidDBInstanceModificationsMessage': {
            'Storage': [
                {
                    'StorageType': 'string',
                    'StorageSize': [
                        {
                            'From': 123,
                            'To': 123,
                            'Step': 123
                        },
                    ],
                    'ProvisionedIops': [
                        {
                            'From': 123,
                            'To': 123,
                            'Step': 123
                        },
                    ],
                    'IopsToStorageRatio': [
                        {
                            'From': 123.0,
                            'To': 123.0
                        },
                    ]
                },
            ]
        }
    }
    
    
    """
    pass

def failover_db_cluster(DBClusterIdentifier=None, TargetDBInstanceIdentifier=None):
    """
    Forces a failover for a DB cluster.
    A failover for a DB cluster promotes one of the Read Replicas (read-only instances) in the DB cluster to be the primary instance (the cluster writer).
    Amazon Neptune will automatically fail over to a Read Replica, if one exists, when the primary instance fails. You can force a failover when you want to simulate a failure of a primary instance for testing. Because each instance in a DB cluster has its own endpoint address, you will need to clean up and re-establish any existing connections that use those endpoint addresses when the failover is complete.
    See also: AWS API Documentation
    
    
    :example: response = client.failover_db_cluster(
        DBClusterIdentifier='string',
        TargetDBInstanceIdentifier='string'
    )
    
    
    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: A DB cluster identifier to force a failover for. This parameter is not case-sensitive.
            Constraints:
            Must match the identifier of an existing DBCluster.
            

    :type TargetDBInstanceIdentifier: string
    :param TargetDBInstanceIdentifier: The name of the instance to promote to the primary instance.
            You must specify the instance identifier for an Read Replica in the DB cluster. For example, mydbcluster-replica1 .
            

    :rtype: dict
    :return: {
        'DBCluster': {
            'AllocatedStorage': 123,
            'AvailabilityZones': [
                'string',
            ],
            'BackupRetentionPeriod': 123,
            'CharacterSetName': 'string',
            'DatabaseName': 'string',
            'DBClusterIdentifier': 'string',
            'DBClusterParameterGroup': 'string',
            'DBSubnetGroup': 'string',
            'Status': 'string',
            'PercentProgress': 'string',
            'EarliestRestorableTime': datetime(2015, 1, 1),
            'Endpoint': 'string',
            'ReaderEndpoint': 'string',
            'MultiAZ': True|False,
            'Engine': 'string',
            'EngineVersion': 'string',
            'LatestRestorableTime': datetime(2015, 1, 1),
            'Port': 123,
            'MasterUsername': 'string',
            'DBClusterOptionGroupMemberships': [
                {
                    'DBClusterOptionGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'PreferredBackupWindow': 'string',
            'PreferredMaintenanceWindow': 'string',
            'ReplicationSourceIdentifier': 'string',
            'ReadReplicaIdentifiers': [
                'string',
            ],
            'DBClusterMembers': [
                {
                    'DBInstanceIdentifier': 'string',
                    'IsClusterWriter': True|False,
                    'DBClusterParameterGroupStatus': 'string',
                    'PromotionTier': 123
                },
            ],
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'HostedZoneId': 'string',
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DbClusterResourceId': 'string',
            'DBClusterArn': 'string',
            'AssociatedRoles': [
                {
                    'RoleArn': 'string',
                    'Status': 'string'
                },
            ],
            'IAMDatabaseAuthenticationEnabled': True|False,
            'CloneGroupId': 'string',
            'ClusterCreateTime': datetime(2015, 1, 1)
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

def list_tags_for_resource(ResourceName=None, Filters=None):
    """
    Lists all tags on an Amazon Neptune resource.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags_for_resource(
        ResourceName='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type ResourceName: string
    :param ResourceName: [REQUIRED]
            The Amazon Neptune resource with tags to be listed. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see Constructing an Amazon Resource Name (ARN) .
            

    :type Filters: list
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            

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

def modify_db_cluster(DBClusterIdentifier=None, NewDBClusterIdentifier=None, ApplyImmediately=None, BackupRetentionPeriod=None, DBClusterParameterGroupName=None, VpcSecurityGroupIds=None, Port=None, MasterUserPassword=None, OptionGroupName=None, PreferredBackupWindow=None, PreferredMaintenanceWindow=None, EnableIAMDatabaseAuthentication=None, EngineVersion=None):
    """
    Modify a setting for a DB cluster. You can change one or more database configuration parameters by specifying these parameters and the new values in the request.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_db_cluster(
        DBClusterIdentifier='string',
        NewDBClusterIdentifier='string',
        ApplyImmediately=True|False,
        BackupRetentionPeriod=123,
        DBClusterParameterGroupName='string',
        VpcSecurityGroupIds=[
            'string',
        ],
        Port=123,
        MasterUserPassword='string',
        OptionGroupName='string',
        PreferredBackupWindow='string',
        PreferredMaintenanceWindow='string',
        EnableIAMDatabaseAuthentication=True|False,
        EngineVersion='string'
    )
    
    
    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]
            The DB cluster identifier for the cluster being modified. This parameter is not case-sensitive.
            Constraints:
            Must match the identifier of an existing DBCluster.
            

    :type NewDBClusterIdentifier: string
    :param NewDBClusterIdentifier: The new DB cluster identifier for the DB cluster when renaming a DB cluster. This value is stored as a lowercase string.
            Constraints:
            Must contain from 1 to 63 letters, numbers, or hyphens
            The first character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            Example: my-cluster2
            

    :type ApplyImmediately: boolean
    :param ApplyImmediately: A value that specifies whether the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the PreferredMaintenanceWindow setting for the DB cluster. If this parameter is set to false , changes to the DB cluster are applied during the next maintenance window.
            The ApplyImmediately parameter only affects the NewDBClusterIdentifier and MasterUserPassword values. If you set the ApplyImmediately parameter value to false, then changes to the NewDBClusterIdentifier and MasterUserPassword values are applied during the next maintenance window. All other changes are applied immediately, regardless of the value of the ApplyImmediately parameter.
            Default: false
            

    :type BackupRetentionPeriod: integer
    :param BackupRetentionPeriod: The number of days for which automated backups are retained. You must specify a minimum value of 1.
            Default: 1
            Constraints:
            Must be a value from 1 to 35
            

    :type DBClusterParameterGroupName: string
    :param DBClusterParameterGroupName: The name of the DB cluster parameter group to use for the DB cluster.

    :type VpcSecurityGroupIds: list
    :param VpcSecurityGroupIds: A list of VPC security groups that the DB cluster will belong to.
            (string) --
            

    :type Port: integer
    :param Port: The port number on which the DB cluster accepts connections.
            Constraints: Value must be 1150-65535
            Default: The same port as the original DB cluster.
            

    :type MasterUserPassword: string
    :param MasterUserPassword: The new password for the master database user. This password can contain any printable ASCII character except '/', ''', or '@'.
            Constraints: Must contain from 8 to 41 characters.
            

    :type OptionGroupName: string
    :param OptionGroupName: A value that indicates that the DB cluster should be associated with the specified option group. Changing this parameter doesn't result in an outage except in the following case, and the change is applied during the next maintenance window unless the ApplyImmediately parameter is set to true for this request. If the parameter change results in an option group that enables OEM, this change can cause a brief (sub-second) period during which new connections are rejected but existing connections are not interrupted.
            Permanent options can't be removed from an option group. The option group can't be removed from a DB cluster once it is associated with a DB cluster.
            

    :type PreferredBackupWindow: string
    :param PreferredBackupWindow: The daily time range during which automated backups are created if automated backups are enabled, using the BackupRetentionPeriod parameter.
            The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region.
            Constraints:
            Must be in the format hh24:mi-hh24:mi .
            Must be in Universal Coordinated Time (UTC).
            Must not conflict with the preferred maintenance window.
            Must be at least 30 minutes.
            

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
            Format: ddd:hh24:mi-ddd:hh24:mi
            The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.
            Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.
            Constraints: Minimum 30-minute window.
            

    :type EnableIAMDatabaseAuthentication: boolean
    :param EnableIAMDatabaseAuthentication: True to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts, and otherwise false.
            Default: false
            

    :type EngineVersion: string
    :param EngineVersion: The version number of the database engine to which you want to upgrade. Changing this parameter results in an outage. The change is applied during the next maintenance window unless the ApplyImmediately parameter is set to true.
            For a list of valid engine versions, see CreateDBInstance , or call DescribeDBEngineVersions .
            

    :rtype: dict
    :return: {
        'DBCluster': {
            'AllocatedStorage': 123,
            'AvailabilityZones': [
                'string',
            ],
            'BackupRetentionPeriod': 123,
            'CharacterSetName': 'string',
            'DatabaseName': 'string',
            'DBClusterIdentifier': 'string',
            'DBClusterParameterGroup': 'string',
            'DBSubnetGroup': 'string',
            'Status': 'string',
            'PercentProgress': 'string',
            'EarliestRestorableTime': datetime(2015, 1, 1),
            'Endpoint': 'string',
            'ReaderEndpoint': 'string',
            'MultiAZ': True|False,
            'Engine': 'string',
            'EngineVersion': 'string',
            'LatestRestorableTime': datetime(2015, 1, 1),
            'Port': 123,
            'MasterUsername': 'string',
            'DBClusterOptionGroupMemberships': [
                {
                    'DBClusterOptionGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'PreferredBackupWindow': 'string',
            'PreferredMaintenanceWindow': 'string',
            'ReplicationSourceIdentifier': 'string',
            'ReadReplicaIdentifiers': [
                'string',
            ],
            'DBClusterMembers': [
                {
                    'DBInstanceIdentifier': 'string',
                    'IsClusterWriter': True|False,
                    'DBClusterParameterGroupStatus': 'string',
                    'PromotionTier': 123
                },
            ],
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'HostedZoneId': 'string',
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DbClusterResourceId': 'string',
            'DBClusterArn': 'string',
            'AssociatedRoles': [
                {
                    'RoleArn': 'string',
                    'Status': 'string'
                },
            ],
            'IAMDatabaseAuthenticationEnabled': True|False,
            'CloneGroupId': 'string',
            'ClusterCreateTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def modify_db_cluster_parameter_group(DBClusterParameterGroupName=None, Parameters=None):
    """
    Modifies the parameters of a DB cluster parameter group. To modify more than one parameter, submit a list of the following: ParameterName , ParameterValue , and ApplyMethod . A maximum of 20 parameters can be modified in a single request.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_db_cluster_parameter_group(
        DBClusterParameterGroupName='string',
        Parameters=[
            {
                'ParameterName': 'string',
                'ParameterValue': 'string',
                'Description': 'string',
                'Source': 'string',
                'ApplyType': 'string',
                'DataType': 'string',
                'AllowedValues': 'string',
                'IsModifiable': True|False,
                'MinimumEngineVersion': 'string',
                'ApplyMethod': 'immediate'|'pending-reboot'
            },
        ]
    )
    
    
    :type DBClusterParameterGroupName: string
    :param DBClusterParameterGroupName: [REQUIRED]
            The name of the DB cluster parameter group to modify.
            

    :type Parameters: list
    :param Parameters: [REQUIRED]
            A list of parameters in the DB cluster parameter group to modify.
            (dict) --This data type is used as a request parameter in the ModifyDBParameterGroup and ResetDBParameterGroup actions.
            This data type is used as a response element in the DescribeEngineDefaultParameters and DescribeDBParameters actions.
            ParameterName (string) --Specifies the name of the parameter.
            ParameterValue (string) --Specifies the value of the parameter.
            Description (string) --Provides a description of the parameter.
            Source (string) --Indicates the source of the parameter value.
            ApplyType (string) --Specifies the engine specific parameters type.
            DataType (string) --Specifies the valid data type for the parameter.
            AllowedValues (string) --Specifies the valid range of values for the parameter.
            IsModifiable (boolean) --Indicates whether (true ) or not (false ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.
            MinimumEngineVersion (string) --The earliest engine version to which the parameter can apply.
            ApplyMethod (string) --Indicates when to apply parameter updates.
            
            

    :rtype: dict
    :return: {
        'DBClusterParameterGroupName': 'string'
    }
    
    
    :returns: 
    Must be 1 to 255 letters or numbers.
    First character must be a letter
    Cannot end with a hyphen or contain two consecutive hyphens
    
    """
    pass

def modify_db_cluster_snapshot_attribute(DBClusterSnapshotIdentifier=None, AttributeName=None, ValuesToAdd=None, ValuesToRemove=None):
    """
    Adds an attribute and values to, or removes an attribute and values from, a manual DB cluster snapshot.
    To share a manual DB cluster snapshot with other AWS accounts, specify restore as the AttributeName and use the ValuesToAdd parameter to add a list of IDs of the AWS accounts that are authorized to restore the manual DB cluster snapshot. Use the value all to make the manual DB cluster snapshot public, which means that it can be copied or restored by all AWS accounts. Do not add the all value for any manual DB cluster snapshots that contain private information that you don't want available to all AWS accounts. If a manual DB cluster snapshot is encrypted, it can be shared, but only by specifying a list of authorized AWS account IDs for the ValuesToAdd parameter. You can't use all as a value for that parameter in this case.
    To view which AWS accounts have access to copy or restore a manual DB cluster snapshot, or whether a manual DB cluster snapshot public or private, use the  DescribeDBClusterSnapshotAttributes API action.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_db_cluster_snapshot_attribute(
        DBClusterSnapshotIdentifier='string',
        AttributeName='string',
        ValuesToAdd=[
            'string',
        ],
        ValuesToRemove=[
            'string',
        ]
    )
    
    
    :type DBClusterSnapshotIdentifier: string
    :param DBClusterSnapshotIdentifier: [REQUIRED]
            The identifier for the DB cluster snapshot to modify the attributes for.
            

    :type AttributeName: string
    :param AttributeName: [REQUIRED]
            The name of the DB cluster snapshot attribute to modify.
            To manage authorization for other AWS accounts to copy or restore a manual DB cluster snapshot, set this value to restore .
            

    :type ValuesToAdd: list
    :param ValuesToAdd: A list of DB cluster snapshot attributes to add to the attribute specified by AttributeName .
            To authorize other AWS accounts to copy or restore a manual DB cluster snapshot, set this list to include one or more AWS account IDs, or all to make the manual DB cluster snapshot restorable by any AWS account. Do not add the all value for any manual DB cluster snapshots that contain private information that you don't want available to all AWS accounts.
            (string) --
            

    :type ValuesToRemove: list
    :param ValuesToRemove: A list of DB cluster snapshot attributes to remove from the attribute specified by AttributeName .
            To remove authorization for other AWS accounts to copy or restore a manual DB cluster snapshot, set this list to include one or more AWS account identifiers, or all to remove authorization for any AWS account to copy or restore the DB cluster snapshot. If you specify all , an AWS account whose account ID is explicitly added to the restore attribute can still copy or restore a manual DB cluster snapshot.
            (string) --
            

    :rtype: dict
    :return: {
        'DBClusterSnapshotAttributesResult': {
            'DBClusterSnapshotIdentifier': 'string',
            'DBClusterSnapshotAttributes': [
                {
                    'AttributeName': 'string',
                    'AttributeValues': [
                        'string',
                    ]
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def modify_db_instance(DBInstanceIdentifier=None, AllocatedStorage=None, DBInstanceClass=None, DBSubnetGroupName=None, DBSecurityGroups=None, VpcSecurityGroupIds=None, ApplyImmediately=None, MasterUserPassword=None, DBParameterGroupName=None, BackupRetentionPeriod=None, PreferredBackupWindow=None, PreferredMaintenanceWindow=None, MultiAZ=None, EngineVersion=None, AllowMajorVersionUpgrade=None, AutoMinorVersionUpgrade=None, LicenseModel=None, Iops=None, OptionGroupName=None, NewDBInstanceIdentifier=None, StorageType=None, TdeCredentialArn=None, TdeCredentialPassword=None, CACertificateIdentifier=None, Domain=None, CopyTagsToSnapshot=None, MonitoringInterval=None, DBPortNumber=None, PubliclyAccessible=None, MonitoringRoleArn=None, DomainIAMRoleName=None, PromotionTier=None, EnableIAMDatabaseAuthentication=None, EnablePerformanceInsights=None, PerformanceInsightsKMSKeyId=None, CloudwatchLogsExportConfiguration=None):
    """
    Modifies settings for a DB instance. You can change one or more database configuration parameters by specifying these parameters and the new values in the request. To learn what modifications you can make to your DB instance, call  DescribeValidDBInstanceModifications before you call  ModifyDBInstance .
    See also: AWS API Documentation
    
    
    :example: response = client.modify_db_instance(
        DBInstanceIdentifier='string',
        AllocatedStorage=123,
        DBInstanceClass='string',
        DBSubnetGroupName='string',
        DBSecurityGroups=[
            'string',
        ],
        VpcSecurityGroupIds=[
            'string',
        ],
        ApplyImmediately=True|False,
        MasterUserPassword='string',
        DBParameterGroupName='string',
        BackupRetentionPeriod=123,
        PreferredBackupWindow='string',
        PreferredMaintenanceWindow='string',
        MultiAZ=True|False,
        EngineVersion='string',
        AllowMajorVersionUpgrade=True|False,
        AutoMinorVersionUpgrade=True|False,
        LicenseModel='string',
        Iops=123,
        OptionGroupName='string',
        NewDBInstanceIdentifier='string',
        StorageType='string',
        TdeCredentialArn='string',
        TdeCredentialPassword='string',
        CACertificateIdentifier='string',
        Domain='string',
        CopyTagsToSnapshot=True|False,
        MonitoringInterval=123,
        DBPortNumber=123,
        PubliclyAccessible=True|False,
        MonitoringRoleArn='string',
        DomainIAMRoleName='string',
        PromotionTier=123,
        EnableIAMDatabaseAuthentication=True|False,
        EnablePerformanceInsights=True|False,
        PerformanceInsightsKMSKeyId='string',
        CloudwatchLogsExportConfiguration={
            'EnableLogTypes': [
                'string',
            ],
            'DisableLogTypes': [
                'string',
            ]
        }
    )
    
    
    :type DBInstanceIdentifier: string
    :param DBInstanceIdentifier: [REQUIRED]
            The DB instance identifier. This value is stored as a lowercase string.
            Constraints:
            Must match the identifier of an existing DBInstance.
            

    :type AllocatedStorage: integer
    :param AllocatedStorage: The new amount of storage (in gibibytes) to allocate for the DB instance.
            Not applicable. Storage is managed by the DB Cluster.
            

    :type DBInstanceClass: string
    :param DBInstanceClass: The new compute and memory capacity of the DB instance, for example, db.m4.large . Not all DB instance classes are available in all AWS Regions.
            If you modify the DB instance class, an outage occurs during the change. The change is applied during the next maintenance window, unless ApplyImmediately is specified as true for this request.
            Default: Uses existing setting
            

    :type DBSubnetGroupName: string
    :param DBSubnetGroupName: The new DB subnet group for the DB instance. You can use this parameter to move your DB instance to a different VPC.
            Changing the subnet group causes an outage during the change. The change is applied during the next maintenance window, unless you specify true for the ApplyImmediately parameter.
            Constraints: If supplied, must match the name of an existing DBSubnetGroup.
            Example: mySubnetGroup
            

    :type DBSecurityGroups: list
    :param DBSecurityGroups: A list of DB security groups to authorize on this DB instance. Changing this setting doesn't result in an outage and the change is asynchronously applied as soon as possible.
            Constraints:
            If supplied, must match existing DBSecurityGroups.
            (string) --
            

    :type VpcSecurityGroupIds: list
    :param VpcSecurityGroupIds: A list of EC2 VPC security groups to authorize on this DB instance. This change is asynchronously applied as soon as possible.
            Not applicable. The associated list of EC2 VPC security groups is managed by the DB cluster. For more information, see ModifyDBCluster .
            Constraints:
            If supplied, must match existing VpcSecurityGroupIds.
            (string) --
            

    :type ApplyImmediately: boolean
    :param ApplyImmediately: Specifies whether the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the PreferredMaintenanceWindow setting for the DB instance.
            If this parameter is set to false , changes to the DB instance are applied during the next maintenance window. Some parameter changes can cause an outage and are applied on the next call to RebootDBInstance , or the next failure reboot.
            Default: false
            

    :type MasterUserPassword: string
    :param MasterUserPassword: The new password for the master user. The password can include any printable ASCII character except '/', ''', or '@'.
            Not applicable.
            Default: Uses existing setting
            

    :type DBParameterGroupName: string
    :param DBParameterGroupName: The name of the DB parameter group to apply to the DB instance. Changing this setting doesn't result in an outage. The parameter group name itself is changed immediately, but the actual parameter changes are not applied until you reboot the instance without failover. The db instance will NOT be rebooted automatically and the parameter changes will NOT be applied during the next maintenance window.
            Default: Uses existing setting
            Constraints: The DB parameter group must be in the same DB parameter group family as this DB instance.
            

    :type BackupRetentionPeriod: integer
    :param BackupRetentionPeriod: The number of days to retain automated backups. Setting this parameter to a positive number enables backups. Setting this parameter to 0 disables automated backups.
            Not applicable. The retention period for automated backups is managed by the DB cluster. For more information, see ModifyDBCluster .
            Default: Uses existing setting
            

    :type PreferredBackupWindow: string
    :param PreferredBackupWindow: The daily time range during which automated backups are created if automated backups are enabled.
            Not applicable. The daily time range for creating automated backups is managed by the DB cluster. For more information, see ModifyDBCluster .
            Constraints:
            Must be in the format hh24:mi-hh24:mi
            Must be in Universal Time Coordinated (UTC)
            Must not conflict with the preferred maintenance window
            Must be at least 30 minutes
            

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: The weekly time range (in UTC) during which system maintenance can occur, which might result in an outage. Changing this parameter doesn't result in an outage, except in the following situation, and the change is asynchronously applied as soon as possible. If there are pending actions that cause a reboot, and the maintenance window is changed to include the current time, then changing this parameter will cause a reboot of the DB instance. If moving this window to the current time, there must be at least 30 minutes between the current time and end of the window to ensure pending changes are applied.
            Default: Uses existing setting
            Format: ddd:hh24:mi-ddd:hh24:mi
            Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun
            Constraints: Must be at least 30 minutes
            

    :type MultiAZ: boolean
    :param MultiAZ: Specifies if the DB instance is a Multi-AZ deployment. Changing this parameter doesn't result in an outage and the change is applied during the next maintenance window unless the ApplyImmediately parameter is set to true for this request.

    :type EngineVersion: string
    :param EngineVersion: The version number of the database engine to upgrade to. Changing this parameter results in an outage and the change is applied during the next maintenance window unless the ApplyImmediately parameter is set to true for this request.
            For major version upgrades, if a nondefault DB parameter group is currently in use, a new DB parameter group in the DB parameter group family for the new engine version must be specified. The new DB parameter group can be the default for that DB parameter group family.
            

    :type AllowMajorVersionUpgrade: boolean
    :param AllowMajorVersionUpgrade: Indicates that major version upgrades are allowed. Changing this parameter doesn't result in an outage and the change is asynchronously applied as soon as possible.
            Constraints: This parameter must be set to true when specifying a value for the EngineVersion parameter that is a different major version than the DB instance's current version.
            

    :type AutoMinorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: Indicates that minor version upgrades are applied automatically to the DB instance during the maintenance window. Changing this parameter doesn't result in an outage except in the following case and the change is asynchronously applied as soon as possible. An outage will result if this parameter is set to true during the maintenance window, and a newer minor version is available, and Neptune has enabled auto patching for that engine version.

    :type LicenseModel: string
    :param LicenseModel: The license model for the DB instance.
            Valid values: license-included | bring-your-own-license | general-public-license
            

    :type Iops: integer
    :param Iops: The new Provisioned IOPS (I/O operations per second) value for the instance.
            Changing this setting doesn't result in an outage and the change is applied during the next maintenance window unless the ApplyImmediately parameter is set to true for this request.
            Default: Uses existing setting
            

    :type OptionGroupName: string
    :param OptionGroupName: Indicates that the DB instance should be associated with the specified option group. Changing this parameter doesn't result in an outage except in the following case and the change is applied during the next maintenance window unless the ApplyImmediately parameter is set to true for this request. If the parameter change results in an option group that enables OEM, this change can cause a brief (sub-second) period during which new connections are rejected but existing connections are not interrupted.
            Permanent options, such as the TDE option for Oracle Advanced Security TDE, can't be removed from an option group, and that option group can't be removed from a DB instance once it is associated with a DB instance
            

    :type NewDBInstanceIdentifier: string
    :param NewDBInstanceIdentifier: The new DB instance identifier for the DB instance when renaming a DB instance. When you change the DB instance identifier, an instance reboot will occur immediately if you set Apply Immediately to true, or will occur during the next maintenance window if Apply Immediately to false. This value is stored as a lowercase string.
            Constraints:
            Must contain from 1 to 63 letters, numbers, or hyphens.
            The first character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Example: mydbinstance
            

    :type StorageType: string
    :param StorageType: Specifies the storage type to be associated with the DB instance.
            If you specify Provisioned IOPS (io1 ), you must also include a value for the Iops parameter.
            If you choose to migrate your DB instance from using standard storage to using Provisioned IOPS, or from using Provisioned IOPS to using standard storage, the process can take time. The duration of the migration depends on several factors such as database load, storage size, storage type (standard or Provisioned IOPS), amount of IOPS provisioned (if any), and the number of prior scale storage operations. Typical migration times are under 24 hours, but the process can take up to several days in some cases. During the migration, the DB instance is available for use, but might experience performance degradation. While the migration takes place, nightly backups for the instance are suspended. No other Amazon Neptune operations can take place for the instance, including modifying the instance, rebooting the instance, deleting the instance, creating a Read Replica for the instance, and creating a DB snapshot of the instance.
            Valid values: standard | gp2 | io1
            Default: io1 if the Iops parameter is specified, otherwise standard
            

    :type TdeCredentialArn: string
    :param TdeCredentialArn: The ARN from the key store with which to associate the instance for TDE encryption.

    :type TdeCredentialPassword: string
    :param TdeCredentialPassword: The password for the given ARN from the key store in order to access the device.

    :type CACertificateIdentifier: string
    :param CACertificateIdentifier: Indicates the certificate that needs to be associated with the instance.

    :type Domain: string
    :param Domain: Not supported.

    :type CopyTagsToSnapshot: boolean
    :param CopyTagsToSnapshot: True to copy all tags from the DB instance to snapshots of the DB instance, and otherwise false. The default is false.

    :type MonitoringInterval: integer
    :param MonitoringInterval: The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0.
            If MonitoringRoleArn is specified, then you must also set MonitoringInterval to a value other than 0.
            Valid Values: 0, 1, 5, 10, 15, 30, 60
            

    :type DBPortNumber: integer
    :param DBPortNumber: The port number on which the database accepts connections.
            The value of the DBPortNumber parameter must not match any of the port values specified for options in the option group for the DB instance.
            Your database will restart when you change the DBPortNumber value regardless of the value of the ApplyImmediately parameter.
            Default: 8182
            

    :type PubliclyAccessible: boolean
    :param PubliclyAccessible: This parameter is not supported.

    :type MonitoringRoleArn: string
    :param MonitoringRoleArn: The ARN for the IAM role that permits Neptune to send enhanced monitoring metrics to Amazon CloudWatch Logs. For example, arn:aws:iam:123456789012:role/emaccess .
            If MonitoringInterval is set to a value other than 0, then you must supply a MonitoringRoleArn value.
            

    :type DomainIAMRoleName: string
    :param DomainIAMRoleName: Not supported

    :type PromotionTier: integer
    :param PromotionTier: A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.
            Default: 1
            Valid Values: 0 - 15
            

    :type EnableIAMDatabaseAuthentication: boolean
    :param EnableIAMDatabaseAuthentication: True to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts, and otherwise false.
            You can enable IAM database authentication for the following database engines
            Not applicable. Mapping AWS IAM accounts to database accounts is managed by the DB cluster. For more information, see ModifyDBCluster .
            Default: false
            

    :type EnablePerformanceInsights: boolean
    :param EnablePerformanceInsights: True to enable Performance Insights for the DB instance, and otherwise false.

    :type PerformanceInsightsKMSKeyId: string
    :param PerformanceInsightsKMSKeyId: The AWS KMS key identifier for encryption of Performance Insights data. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key.

    :type CloudwatchLogsExportConfiguration: dict
    :param CloudwatchLogsExportConfiguration: The configuration setting for the log types to be enabled for export to CloudWatch Logs for a specific DB instance or DB cluster.
            EnableLogTypes (list) --The list of log types to enable.
            (string) --
            DisableLogTypes (list) --The list of log types to disable.
            (string) --
            

    :rtype: dict
    :return: {
        'DBInstance': {
            'DBInstanceIdentifier': 'string',
            'DBInstanceClass': 'string',
            'Engine': 'string',
            'DBInstanceStatus': 'string',
            'MasterUsername': 'string',
            'DBName': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123,
                'HostedZoneId': 'string'
            },
            'AllocatedStorage': 123,
            'InstanceCreateTime': datetime(2015, 1, 1),
            'PreferredBackupWindow': 'string',
            'BackupRetentionPeriod': 123,
            'DBSecurityGroups': [
                {
                    'DBSecurityGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'DBParameterGroups': [
                {
                    'DBParameterGroupName': 'string',
                    'ParameterApplyStatus': 'string'
                },
            ],
            'AvailabilityZone': 'string',
            'DBSubnetGroup': {
                'DBSubnetGroupName': 'string',
                'DBSubnetGroupDescription': 'string',
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
                ],
                'DBSubnetGroupArn': 'string'
            },
            'PreferredMaintenanceWindow': 'string',
            'PendingModifiedValues': {
                'DBInstanceClass': 'string',
                'AllocatedStorage': 123,
                'MasterUserPassword': 'string',
                'Port': 123,
                'BackupRetentionPeriod': 123,
                'MultiAZ': True|False,
                'EngineVersion': 'string',
                'LicenseModel': 'string',
                'Iops': 123,
                'DBInstanceIdentifier': 'string',
                'StorageType': 'string',
                'CACertificateIdentifier': 'string',
                'DBSubnetGroupName': 'string',
                'PendingCloudwatchLogsExports': {
                    'LogTypesToEnable': [
                        'string',
                    ],
                    'LogTypesToDisable': [
                        'string',
                    ]
                }
            },
            'LatestRestorableTime': datetime(2015, 1, 1),
            'MultiAZ': True|False,
            'EngineVersion': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'ReadReplicaSourceDBInstanceIdentifier': 'string',
            'ReadReplicaDBInstanceIdentifiers': [
                'string',
            ],
            'ReadReplicaDBClusterIdentifiers': [
                'string',
            ],
            'LicenseModel': 'string',
            'Iops': 123,
            'OptionGroupMemberships': [
                {
                    'OptionGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'CharacterSetName': 'string',
            'SecondaryAvailabilityZone': 'string',
            'PubliclyAccessible': True|False,
            'StatusInfos': [
                {
                    'StatusType': 'string',
                    'Normal': True|False,
                    'Status': 'string',
                    'Message': 'string'
                },
            ],
            'StorageType': 'string',
            'TdeCredentialArn': 'string',
            'DbInstancePort': 123,
            'DBClusterIdentifier': 'string',
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DbiResourceId': 'string',
            'CACertificateIdentifier': 'string',
            'DomainMemberships': [
                {
                    'Domain': 'string',
                    'Status': 'string',
                    'FQDN': 'string',
                    'IAMRoleName': 'string'
                },
            ],
            'CopyTagsToSnapshot': True|False,
            'MonitoringInterval': 123,
            'EnhancedMonitoringResourceArn': 'string',
            'MonitoringRoleArn': 'string',
            'PromotionTier': 123,
            'DBInstanceArn': 'string',
            'Timezone': 'string',
            'IAMDatabaseAuthenticationEnabled': True|False,
            'PerformanceInsightsEnabled': True|False,
            'PerformanceInsightsKMSKeyId': 'string',
            'EnabledCloudwatchLogsExports': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    ModifyDBInstance
    RebootDBInstance
    
    """
    pass

def modify_db_parameter_group(DBParameterGroupName=None, Parameters=None):
    """
    Modifies the parameters of a DB parameter group. To modify more than one parameter, submit a list of the following: ParameterName , ParameterValue , and ApplyMethod . A maximum of 20 parameters can be modified in a single request.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_db_parameter_group(
        DBParameterGroupName='string',
        Parameters=[
            {
                'ParameterName': 'string',
                'ParameterValue': 'string',
                'Description': 'string',
                'Source': 'string',
                'ApplyType': 'string',
                'DataType': 'string',
                'AllowedValues': 'string',
                'IsModifiable': True|False,
                'MinimumEngineVersion': 'string',
                'ApplyMethod': 'immediate'|'pending-reboot'
            },
        ]
    )
    
    
    :type DBParameterGroupName: string
    :param DBParameterGroupName: [REQUIRED]
            The name of the DB parameter group.
            Constraints:
            If supplied, must match the name of an existing DBParameterGroup.
            

    :type Parameters: list
    :param Parameters: [REQUIRED]
            An array of parameter names, values, and the apply method for the parameter update. At least one parameter name, value, and apply method must be supplied; subsequent arguments are optional. A maximum of 20 parameters can be modified in a single request.
            Valid Values (for the application method): immediate | pending-reboot
            Note
            You can use the immediate value with dynamic parameters only. You can use the pending-reboot value for both dynamic and static parameters, and changes are applied when you reboot the DB instance without failover.
            (dict) --This data type is used as a request parameter in the ModifyDBParameterGroup and ResetDBParameterGroup actions.
            This data type is used as a response element in the DescribeEngineDefaultParameters and DescribeDBParameters actions.
            ParameterName (string) --Specifies the name of the parameter.
            ParameterValue (string) --Specifies the value of the parameter.
            Description (string) --Provides a description of the parameter.
            Source (string) --Indicates the source of the parameter value.
            ApplyType (string) --Specifies the engine specific parameters type.
            DataType (string) --Specifies the valid data type for the parameter.
            AllowedValues (string) --Specifies the valid range of values for the parameter.
            IsModifiable (boolean) --Indicates whether (true ) or not (false ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.
            MinimumEngineVersion (string) --The earliest engine version to which the parameter can apply.
            ApplyMethod (string) --Indicates when to apply parameter updates.
            
            

    :rtype: dict
    :return: {
        'DBParameterGroupName': 'string'
    }
    
    
    """
    pass

def modify_db_subnet_group(DBSubnetGroupName=None, DBSubnetGroupDescription=None, SubnetIds=None):
    """
    Modifies an existing DB subnet group. DB subnet groups must contain at least one subnet in at least two AZs in the AWS Region.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_db_subnet_group(
        DBSubnetGroupName='string',
        DBSubnetGroupDescription='string',
        SubnetIds=[
            'string',
        ]
    )
    
    
    :type DBSubnetGroupName: string
    :param DBSubnetGroupName: [REQUIRED]
            The name for the DB subnet group. This value is stored as a lowercase string. You can't modify the default subnet group.
            Constraints: Must match the name of an existing DBSubnetGroup. Must not be default.
            Example: mySubnetgroup
            

    :type DBSubnetGroupDescription: string
    :param DBSubnetGroupDescription: The description for the DB subnet group.

    :type SubnetIds: list
    :param SubnetIds: [REQUIRED]
            The EC2 subnet IDs for the DB subnet group.
            (string) --
            

    :rtype: dict
    :return: {
        'DBSubnetGroup': {
            'DBSubnetGroupName': 'string',
            'DBSubnetGroupDescription': 'string',
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
            ],
            'DBSubnetGroupArn': 'string'
        }
    }
    
    
    :returns: 
    OrderableDBInstanceOption
    
    """
    pass

def modify_event_subscription(SubscriptionName=None, SnsTopicArn=None, SourceType=None, EventCategories=None, Enabled=None):
    """
    Modifies an existing event notification subscription. Note that you can't modify the source identifiers using this call; to change source identifiers for a subscription, use the  AddSourceIdentifierToSubscription and  RemoveSourceIdentifierFromSubscription calls.
    You can see a list of the event categories for a given SourceType by using the DescribeEventCategories action.
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
            The name of the event notification subscription.
            

    :type SnsTopicArn: string
    :param SnsTopicArn: The Amazon Resource Name (ARN) of the SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.

    :type SourceType: string
    :param SourceType: The type of source that is generating the events. For example, if you want to be notified of events generated by a DB instance, you would set this parameter to db-instance. if this value is not specified, all events are returned.
            Valid values: db-instance | db-parameter-group | db-security-group | db-snapshot
            

    :type EventCategories: list
    :param EventCategories: A list of event categories for a SourceType that you want to subscribe to. You can see a list of the categories for a given SourceType by using the DescribeEventCategories action.
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
            'Enabled': True|False,
            'EventSubscriptionArn': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def promote_read_replica_db_cluster(DBClusterIdentifier=None):
    """
    Promotes a Read Replica DB cluster to a standalone DB cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.promote_read_replica_db_cluster(
        DBClusterIdentifier='string'
    )
    
    
    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]
            The identifier of the DB cluster Read Replica to promote. This parameter is not case-sensitive.
            Constraints:
            Must match the identifier of an existing DBCluster Read Replica.
            Example: my-cluster-replica1
            

    :rtype: dict
    :return: {
        'DBCluster': {
            'AllocatedStorage': 123,
            'AvailabilityZones': [
                'string',
            ],
            'BackupRetentionPeriod': 123,
            'CharacterSetName': 'string',
            'DatabaseName': 'string',
            'DBClusterIdentifier': 'string',
            'DBClusterParameterGroup': 'string',
            'DBSubnetGroup': 'string',
            'Status': 'string',
            'PercentProgress': 'string',
            'EarliestRestorableTime': datetime(2015, 1, 1),
            'Endpoint': 'string',
            'ReaderEndpoint': 'string',
            'MultiAZ': True|False,
            'Engine': 'string',
            'EngineVersion': 'string',
            'LatestRestorableTime': datetime(2015, 1, 1),
            'Port': 123,
            'MasterUsername': 'string',
            'DBClusterOptionGroupMemberships': [
                {
                    'DBClusterOptionGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'PreferredBackupWindow': 'string',
            'PreferredMaintenanceWindow': 'string',
            'ReplicationSourceIdentifier': 'string',
            'ReadReplicaIdentifiers': [
                'string',
            ],
            'DBClusterMembers': [
                {
                    'DBInstanceIdentifier': 'string',
                    'IsClusterWriter': True|False,
                    'DBClusterParameterGroupStatus': 'string',
                    'PromotionTier': 123
                },
            ],
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'HostedZoneId': 'string',
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DbClusterResourceId': 'string',
            'DBClusterArn': 'string',
            'AssociatedRoles': [
                {
                    'RoleArn': 'string',
                    'Status': 'string'
                },
            ],
            'IAMDatabaseAuthenticationEnabled': True|False,
            'CloneGroupId': 'string',
            'ClusterCreateTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def reboot_db_instance(DBInstanceIdentifier=None, ForceFailover=None):
    """
    You might need to reboot your DB instance, usually for maintenance reasons. For example, if you make certain modifications, or if you change the DB parameter group associated with the DB instance, you must reboot the instance for the changes to take effect.
    Rebooting a DB instance restarts the database engine service. Rebooting a DB instance results in a momentary outage, during which the DB instance status is set to rebooting.
    See also: AWS API Documentation
    
    
    :example: response = client.reboot_db_instance(
        DBInstanceIdentifier='string',
        ForceFailover=True|False
    )
    
    
    :type DBInstanceIdentifier: string
    :param DBInstanceIdentifier: [REQUIRED]
            The DB instance identifier. This parameter is stored as a lowercase string.
            Constraints:
            Must match the identifier of an existing DBInstance.
            

    :type ForceFailover: boolean
    :param ForceFailover: When true , the reboot is conducted through a MultiAZ failover.
            Constraint: You can't specify true if the instance is not configured for MultiAZ.
            

    :rtype: dict
    :return: {
        'DBInstance': {
            'DBInstanceIdentifier': 'string',
            'DBInstanceClass': 'string',
            'Engine': 'string',
            'DBInstanceStatus': 'string',
            'MasterUsername': 'string',
            'DBName': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123,
                'HostedZoneId': 'string'
            },
            'AllocatedStorage': 123,
            'InstanceCreateTime': datetime(2015, 1, 1),
            'PreferredBackupWindow': 'string',
            'BackupRetentionPeriod': 123,
            'DBSecurityGroups': [
                {
                    'DBSecurityGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'DBParameterGroups': [
                {
                    'DBParameterGroupName': 'string',
                    'ParameterApplyStatus': 'string'
                },
            ],
            'AvailabilityZone': 'string',
            'DBSubnetGroup': {
                'DBSubnetGroupName': 'string',
                'DBSubnetGroupDescription': 'string',
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
                ],
                'DBSubnetGroupArn': 'string'
            },
            'PreferredMaintenanceWindow': 'string',
            'PendingModifiedValues': {
                'DBInstanceClass': 'string',
                'AllocatedStorage': 123,
                'MasterUserPassword': 'string',
                'Port': 123,
                'BackupRetentionPeriod': 123,
                'MultiAZ': True|False,
                'EngineVersion': 'string',
                'LicenseModel': 'string',
                'Iops': 123,
                'DBInstanceIdentifier': 'string',
                'StorageType': 'string',
                'CACertificateIdentifier': 'string',
                'DBSubnetGroupName': 'string',
                'PendingCloudwatchLogsExports': {
                    'LogTypesToEnable': [
                        'string',
                    ],
                    'LogTypesToDisable': [
                        'string',
                    ]
                }
            },
            'LatestRestorableTime': datetime(2015, 1, 1),
            'MultiAZ': True|False,
            'EngineVersion': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'ReadReplicaSourceDBInstanceIdentifier': 'string',
            'ReadReplicaDBInstanceIdentifiers': [
                'string',
            ],
            'ReadReplicaDBClusterIdentifiers': [
                'string',
            ],
            'LicenseModel': 'string',
            'Iops': 123,
            'OptionGroupMemberships': [
                {
                    'OptionGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'CharacterSetName': 'string',
            'SecondaryAvailabilityZone': 'string',
            'PubliclyAccessible': True|False,
            'StatusInfos': [
                {
                    'StatusType': 'string',
                    'Normal': True|False,
                    'Status': 'string',
                    'Message': 'string'
                },
            ],
            'StorageType': 'string',
            'TdeCredentialArn': 'string',
            'DbInstancePort': 123,
            'DBClusterIdentifier': 'string',
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DbiResourceId': 'string',
            'CACertificateIdentifier': 'string',
            'DomainMemberships': [
                {
                    'Domain': 'string',
                    'Status': 'string',
                    'FQDN': 'string',
                    'IAMRoleName': 'string'
                },
            ],
            'CopyTagsToSnapshot': True|False,
            'MonitoringInterval': 123,
            'EnhancedMonitoringResourceArn': 'string',
            'MonitoringRoleArn': 'string',
            'PromotionTier': 123,
            'DBInstanceArn': 'string',
            'Timezone': 'string',
            'IAMDatabaseAuthenticationEnabled': True|False,
            'PerformanceInsightsEnabled': True|False,
            'PerformanceInsightsKMSKeyId': 'string',
            'EnabledCloudwatchLogsExports': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    ModifyDBInstance
    RebootDBInstance
    
    """
    pass

def remove_role_from_db_cluster(DBClusterIdentifier=None, RoleArn=None):
    """
    Disassociates an Identity and Access Management (IAM) role from a DB cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.remove_role_from_db_cluster(
        DBClusterIdentifier='string',
        RoleArn='string'
    )
    
    
    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]
            The name of the DB cluster to disassociate the IAM role from.
            

    :type RoleArn: string
    :param RoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM role to disassociate from the DB cluster, for example arn:aws:iam::123456789012:role/NeptuneAccessRole .
            

    """
    pass

def remove_source_identifier_from_subscription(SubscriptionName=None, SourceIdentifier=None):
    """
    Removes a source identifier from an existing event notification subscription.
    See also: AWS API Documentation
    
    
    :example: response = client.remove_source_identifier_from_subscription(
        SubscriptionName='string',
        SourceIdentifier='string'
    )
    
    
    :type SubscriptionName: string
    :param SubscriptionName: [REQUIRED]
            The name of the event notification subscription you want to remove a source identifier from.
            

    :type SourceIdentifier: string
    :param SourceIdentifier: [REQUIRED]
            The source identifier to be removed from the subscription, such as the DB instance identifier for a DB instance or the name of a security group.
            

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
            'Enabled': True|False,
            'EventSubscriptionArn': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def remove_tags_from_resource(ResourceName=None, TagKeys=None):
    """
    Removes metadata tags from an Amazon Neptune resource.
    See also: AWS API Documentation
    
    
    :example: response = client.remove_tags_from_resource(
        ResourceName='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceName: string
    :param ResourceName: [REQUIRED]
            The Amazon Neptune resource that the tags are removed from. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see Constructing an Amazon Resource Name (ARN) .
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            The tag key (name) of the tag to be removed.
            (string) --
            

    """
    pass

def reset_db_cluster_parameter_group(DBClusterParameterGroupName=None, ResetAllParameters=None, Parameters=None):
    """
    Modifies the parameters of a DB cluster parameter group to the default value. To reset specific parameters submit a list of the following: ParameterName and ApplyMethod . To reset the entire DB cluster parameter group, specify the DBClusterParameterGroupName and ResetAllParameters parameters.
    When resetting the entire group, dynamic parameters are updated immediately and static parameters are set to pending-reboot to take effect on the next DB instance restart or  RebootDBInstance request. You must call  RebootDBInstance for every DB instance in your DB cluster that you want the updated static parameter to apply to.
    See also: AWS API Documentation
    
    
    :example: response = client.reset_db_cluster_parameter_group(
        DBClusterParameterGroupName='string',
        ResetAllParameters=True|False,
        Parameters=[
            {
                'ParameterName': 'string',
                'ParameterValue': 'string',
                'Description': 'string',
                'Source': 'string',
                'ApplyType': 'string',
                'DataType': 'string',
                'AllowedValues': 'string',
                'IsModifiable': True|False,
                'MinimumEngineVersion': 'string',
                'ApplyMethod': 'immediate'|'pending-reboot'
            },
        ]
    )
    
    
    :type DBClusterParameterGroupName: string
    :param DBClusterParameterGroupName: [REQUIRED]
            The name of the DB cluster parameter group to reset.
            

    :type ResetAllParameters: boolean
    :param ResetAllParameters: A value that is set to true to reset all parameters in the DB cluster parameter group to their default values, and false otherwise. You can't use this parameter if there is a list of parameter names specified for the Parameters parameter.

    :type Parameters: list
    :param Parameters: A list of parameter names in the DB cluster parameter group to reset to the default values. You can't use this parameter if the ResetAllParameters parameter is set to true .
            (dict) --This data type is used as a request parameter in the ModifyDBParameterGroup and ResetDBParameterGroup actions.
            This data type is used as a response element in the DescribeEngineDefaultParameters and DescribeDBParameters actions.
            ParameterName (string) --Specifies the name of the parameter.
            ParameterValue (string) --Specifies the value of the parameter.
            Description (string) --Provides a description of the parameter.
            Source (string) --Indicates the source of the parameter value.
            ApplyType (string) --Specifies the engine specific parameters type.
            DataType (string) --Specifies the valid data type for the parameter.
            AllowedValues (string) --Specifies the valid range of values for the parameter.
            IsModifiable (boolean) --Indicates whether (true ) or not (false ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.
            MinimumEngineVersion (string) --The earliest engine version to which the parameter can apply.
            ApplyMethod (string) --Indicates when to apply parameter updates.
            
            

    :rtype: dict
    :return: {
        'DBClusterParameterGroupName': 'string'
    }
    
    
    :returns: 
    Must be 1 to 255 letters or numbers.
    First character must be a letter
    Cannot end with a hyphen or contain two consecutive hyphens
    
    """
    pass

def reset_db_parameter_group(DBParameterGroupName=None, ResetAllParameters=None, Parameters=None):
    """
    Modifies the parameters of a DB parameter group to the engine/system default value. To reset specific parameters, provide a list of the following: ParameterName and ApplyMethod . To reset the entire DB parameter group, specify the DBParameterGroup name and ResetAllParameters parameters. When resetting the entire group, dynamic parameters are updated immediately and static parameters are set to pending-reboot to take effect on the next DB instance restart or RebootDBInstance request.
    See also: AWS API Documentation
    
    
    :example: response = client.reset_db_parameter_group(
        DBParameterGroupName='string',
        ResetAllParameters=True|False,
        Parameters=[
            {
                'ParameterName': 'string',
                'ParameterValue': 'string',
                'Description': 'string',
                'Source': 'string',
                'ApplyType': 'string',
                'DataType': 'string',
                'AllowedValues': 'string',
                'IsModifiable': True|False,
                'MinimumEngineVersion': 'string',
                'ApplyMethod': 'immediate'|'pending-reboot'
            },
        ]
    )
    
    
    :type DBParameterGroupName: string
    :param DBParameterGroupName: [REQUIRED]
            The name of the DB parameter group.
            Constraints:
            Must match the name of an existing DBParameterGroup.
            

    :type ResetAllParameters: boolean
    :param ResetAllParameters: Specifies whether (true ) or not (false ) to reset all parameters in the DB parameter group to default values.
            Default: true
            

    :type Parameters: list
    :param Parameters: To reset the entire DB parameter group, specify the DBParameterGroup name and ResetAllParameters parameters. To reset specific parameters, provide a list of the following: ParameterName and ApplyMethod . A maximum of 20 parameters can be modified in a single request.
            Valid Values (for Apply method): pending-reboot
            (dict) --This data type is used as a request parameter in the ModifyDBParameterGroup and ResetDBParameterGroup actions.
            This data type is used as a response element in the DescribeEngineDefaultParameters and DescribeDBParameters actions.
            ParameterName (string) --Specifies the name of the parameter.
            ParameterValue (string) --Specifies the value of the parameter.
            Description (string) --Provides a description of the parameter.
            Source (string) --Indicates the source of the parameter value.
            ApplyType (string) --Specifies the engine specific parameters type.
            DataType (string) --Specifies the valid data type for the parameter.
            AllowedValues (string) --Specifies the valid range of values for the parameter.
            IsModifiable (boolean) --Indicates whether (true ) or not (false ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.
            MinimumEngineVersion (string) --The earliest engine version to which the parameter can apply.
            ApplyMethod (string) --Indicates when to apply parameter updates.
            
            

    :rtype: dict
    :return: {
        'DBParameterGroupName': 'string'
    }
    
    
    """
    pass

def restore_db_cluster_from_snapshot(AvailabilityZones=None, DBClusterIdentifier=None, SnapshotIdentifier=None, Engine=None, EngineVersion=None, Port=None, DBSubnetGroupName=None, DatabaseName=None, OptionGroupName=None, VpcSecurityGroupIds=None, Tags=None, KmsKeyId=None, EnableIAMDatabaseAuthentication=None):
    """
    Creates a new DB cluster from a DB snapshot or DB cluster snapshot.
    If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group.
    If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.
    See also: AWS API Documentation
    
    
    :example: response = client.restore_db_cluster_from_snapshot(
        AvailabilityZones=[
            'string',
        ],
        DBClusterIdentifier='string',
        SnapshotIdentifier='string',
        Engine='string',
        EngineVersion='string',
        Port=123,
        DBSubnetGroupName='string',
        DatabaseName='string',
        OptionGroupName='string',
        VpcSecurityGroupIds=[
            'string',
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        KmsKeyId='string',
        EnableIAMDatabaseAuthentication=True|False
    )
    
    
    :type AvailabilityZones: list
    :param AvailabilityZones: Provides the list of EC2 Availability Zones that instances in the restored DB cluster can be created in.
            (string) --
            

    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]
            The name of the DB cluster to create from the DB snapshot or DB cluster snapshot. This parameter isn't case-sensitive.
            Constraints:
            Must contain from 1 to 63 letters, numbers, or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            Example: my-snapshot-id
            

    :type SnapshotIdentifier: string
    :param SnapshotIdentifier: [REQUIRED]
            The identifier for the DB snapshot or DB cluster snapshot to restore from.
            You can use either the name or the Amazon Resource Name (ARN) to specify a DB cluster snapshot. However, you can use only the ARN to specify a DB snapshot.
            Constraints:
            Must match the identifier of an existing Snapshot.
            

    :type Engine: string
    :param Engine: [REQUIRED]
            The database engine to use for the new DB cluster.
            Default: The same as source
            Constraint: Must be compatible with the engine of the source
            

    :type EngineVersion: string
    :param EngineVersion: The version of the database engine to use for the new DB cluster.

    :type Port: integer
    :param Port: The port number on which the new DB cluster accepts connections.
            Constraints: Value must be 1150-65535
            Default: The same port as the original DB cluster.
            

    :type DBSubnetGroupName: string
    :param DBSubnetGroupName: The name of the DB subnet group to use for the new DB cluster.
            Constraints: If supplied, must match the name of an existing DBSubnetGroup.
            Example: mySubnetgroup
            

    :type DatabaseName: string
    :param DatabaseName: The database name for the restored DB cluster.

    :type OptionGroupName: string
    :param OptionGroupName: The name of the option group to use for the restored DB cluster.

    :type VpcSecurityGroupIds: list
    :param VpcSecurityGroupIds: A list of VPC security groups that the new DB cluster will belong to.
            (string) --
            

    :type Tags: list
    :param Tags: The tags to be assigned to the restored DB cluster.
            (dict) --Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can't be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can't be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            

    :type KmsKeyId: string
    :param KmsKeyId: The AWS KMS key identifier to use when restoring an encrypted DB cluster from a DB snapshot or DB cluster snapshot.
            The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are restoring a DB cluster with the same AWS account that owns the KMS encryption key used to encrypt the new DB cluster, then you can use the KMS key alias instead of the ARN for the KMS encryption key.
            If you do not specify a value for the KmsKeyId parameter, then the following will occur:
            If the DB snapshot or DB cluster snapshot in SnapshotIdentifier is encrypted, then the restored DB cluster is encrypted using the KMS key that was used to encrypt the DB snapshot or DB cluster snapshot.
            If the DB snapshot or DB cluster snapshot in SnapshotIdentifier is not encrypted, then the restored DB cluster is not encrypted.
            

    :type EnableIAMDatabaseAuthentication: boolean
    :param EnableIAMDatabaseAuthentication: True to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts, and otherwise false.
            Default: false
            

    :rtype: dict
    :return: {
        'DBCluster': {
            'AllocatedStorage': 123,
            'AvailabilityZones': [
                'string',
            ],
            'BackupRetentionPeriod': 123,
            'CharacterSetName': 'string',
            'DatabaseName': 'string',
            'DBClusterIdentifier': 'string',
            'DBClusterParameterGroup': 'string',
            'DBSubnetGroup': 'string',
            'Status': 'string',
            'PercentProgress': 'string',
            'EarliestRestorableTime': datetime(2015, 1, 1),
            'Endpoint': 'string',
            'ReaderEndpoint': 'string',
            'MultiAZ': True|False,
            'Engine': 'string',
            'EngineVersion': 'string',
            'LatestRestorableTime': datetime(2015, 1, 1),
            'Port': 123,
            'MasterUsername': 'string',
            'DBClusterOptionGroupMemberships': [
                {
                    'DBClusterOptionGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'PreferredBackupWindow': 'string',
            'PreferredMaintenanceWindow': 'string',
            'ReplicationSourceIdentifier': 'string',
            'ReadReplicaIdentifiers': [
                'string',
            ],
            'DBClusterMembers': [
                {
                    'DBInstanceIdentifier': 'string',
                    'IsClusterWriter': True|False,
                    'DBClusterParameterGroupStatus': 'string',
                    'PromotionTier': 123
                },
            ],
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'HostedZoneId': 'string',
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DbClusterResourceId': 'string',
            'DBClusterArn': 'string',
            'AssociatedRoles': [
                {
                    'RoleArn': 'string',
                    'Status': 'string'
                },
            ],
            'IAMDatabaseAuthenticationEnabled': True|False,
            'CloneGroupId': 'string',
            'ClusterCreateTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def restore_db_cluster_to_point_in_time(DBClusterIdentifier=None, RestoreType=None, SourceDBClusterIdentifier=None, RestoreToTime=None, UseLatestRestorableTime=None, Port=None, DBSubnetGroupName=None, OptionGroupName=None, VpcSecurityGroupIds=None, Tags=None, KmsKeyId=None, EnableIAMDatabaseAuthentication=None):
    """
    Restores a DB cluster to an arbitrary point in time. Users can restore to any point in time before LatestRestorableTime for up to BackupRetentionPeriod days. The target DB cluster is created from the source DB cluster with the same configuration as the original DB cluster, except that the new DB cluster is created with the default DB security group.
    See also: AWS API Documentation
    
    
    :example: response = client.restore_db_cluster_to_point_in_time(
        DBClusterIdentifier='string',
        RestoreType='string',
        SourceDBClusterIdentifier='string',
        RestoreToTime=datetime(2015, 1, 1),
        UseLatestRestorableTime=True|False,
        Port=123,
        DBSubnetGroupName='string',
        OptionGroupName='string',
        VpcSecurityGroupIds=[
            'string',
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        KmsKeyId='string',
        EnableIAMDatabaseAuthentication=True|False
    )
    
    
    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]
            The name of the new DB cluster to be created.
            Constraints:
            Must contain from 1 to 63 letters, numbers, or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            

    :type RestoreType: string
    :param RestoreType: The type of restore to be performed. You can specify one of the following values:
            full-copy - The new DB cluster is restored as a full copy of the source DB cluster.
            copy-on-write - The new DB cluster is restored as a clone of the source DB cluster.
            Constraints: You can't specify copy-on-write if the engine version of the source DB cluster is earlier than 1.11.
            If you don't specify a RestoreType value, then the new DB cluster is restored as a full copy of the source DB cluster.
            

    :type SourceDBClusterIdentifier: string
    :param SourceDBClusterIdentifier: [REQUIRED]
            The identifier of the source DB cluster from which to restore.
            Constraints:
            Must match the identifier of an existing DBCluster.
            

    :type RestoreToTime: datetime
    :param RestoreToTime: The date and time to restore the DB cluster to.
            Valid Values: Value must be a time in Universal Coordinated Time (UTC) format
            Constraints:
            Must be before the latest restorable time for the DB instance
            Must be specified if UseLatestRestorableTime parameter is not provided
            Cannot be specified if UseLatestRestorableTime parameter is true
            Cannot be specified if RestoreType parameter is copy-on-write
            Example: 2015-03-07T23:45:00Z
            

    :type UseLatestRestorableTime: boolean
    :param UseLatestRestorableTime: A value that is set to true to restore the DB cluster to the latest restorable backup time, and false otherwise.
            Default: false
            Constraints: Cannot be specified if RestoreToTime parameter is provided.
            

    :type Port: integer
    :param Port: The port number on which the new DB cluster accepts connections.
            Constraints: Value must be 1150-65535
            Default: The same port as the original DB cluster.
            

    :type DBSubnetGroupName: string
    :param DBSubnetGroupName: The DB subnet group name to use for the new DB cluster.
            Constraints: If supplied, must match the name of an existing DBSubnetGroup.
            Example: mySubnetgroup
            

    :type OptionGroupName: string
    :param OptionGroupName: The name of the option group for the new DB cluster.

    :type VpcSecurityGroupIds: list
    :param VpcSecurityGroupIds: A list of VPC security groups that the new DB cluster belongs to.
            (string) --
            

    :type Tags: list
    :param Tags: A list of tags. For more information, see Tagging Amazon Neptune Resources .
            (dict) --Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can't be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can't be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            

    :type KmsKeyId: string
    :param KmsKeyId: The AWS KMS key identifier to use when restoring an encrypted DB cluster from an encrypted DB cluster.
            The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are restoring a DB cluster with the same AWS account that owns the KMS encryption key used to encrypt the new DB cluster, then you can use the KMS key alias instead of the ARN for the KMS encryption key.
            You can restore to a new DB cluster and encrypt the new DB cluster with a KMS key that is different than the KMS key used to encrypt the source DB cluster. The new DB cluster is encrypted with the KMS key identified by the KmsKeyId parameter.
            If you do not specify a value for the KmsKeyId parameter, then the following will occur:
            If the DB cluster is encrypted, then the restored DB cluster is encrypted using the KMS key that was used to encrypt the source DB cluster.
            If the DB cluster is not encrypted, then the restored DB cluster is not encrypted.
            If DBClusterIdentifier refers to a DB cluster that is not encrypted, then the restore request is rejected.
            

    :type EnableIAMDatabaseAuthentication: boolean
    :param EnableIAMDatabaseAuthentication: True to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts, and otherwise false.
            Default: false
            

    :rtype: dict
    :return: {
        'DBCluster': {
            'AllocatedStorage': 123,
            'AvailabilityZones': [
                'string',
            ],
            'BackupRetentionPeriod': 123,
            'CharacterSetName': 'string',
            'DatabaseName': 'string',
            'DBClusterIdentifier': 'string',
            'DBClusterParameterGroup': 'string',
            'DBSubnetGroup': 'string',
            'Status': 'string',
            'PercentProgress': 'string',
            'EarliestRestorableTime': datetime(2015, 1, 1),
            'Endpoint': 'string',
            'ReaderEndpoint': 'string',
            'MultiAZ': True|False,
            'Engine': 'string',
            'EngineVersion': 'string',
            'LatestRestorableTime': datetime(2015, 1, 1),
            'Port': 123,
            'MasterUsername': 'string',
            'DBClusterOptionGroupMemberships': [
                {
                    'DBClusterOptionGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'PreferredBackupWindow': 'string',
            'PreferredMaintenanceWindow': 'string',
            'ReplicationSourceIdentifier': 'string',
            'ReadReplicaIdentifiers': [
                'string',
            ],
            'DBClusterMembers': [
                {
                    'DBInstanceIdentifier': 'string',
                    'IsClusterWriter': True|False,
                    'DBClusterParameterGroupStatus': 'string',
                    'PromotionTier': 123
                },
            ],
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'HostedZoneId': 'string',
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DbClusterResourceId': 'string',
            'DBClusterArn': 'string',
            'AssociatedRoles': [
                {
                    'RoleArn': 'string',
                    'Status': 'string'
                },
            ],
            'IAMDatabaseAuthenticationEnabled': True|False,
            'CloneGroupId': 'string',
            'ClusterCreateTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

