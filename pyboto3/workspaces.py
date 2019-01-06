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

def associate_ip_groups(DirectoryId=None, GroupIds=None):
    """
    Associates the specified IP access control group with the specified directory.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_ip_groups(
        DirectoryId='string',
        GroupIds=[
            'string',
        ]
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]
            The identifier of the directory.
            

    :type GroupIds: list
    :param GroupIds: [REQUIRED]
            The identifiers of one or more IP access control groups.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def authorize_ip_rules(GroupId=None, UserRules=None):
    """
    Adds one or more rules to the specified IP access control group.
    This action gives users permission to access their WorkSpaces from the CIDR address ranges specified in the rules.
    See also: AWS API Documentation
    
    
    :example: response = client.authorize_ip_rules(
        GroupId='string',
        UserRules=[
            {
                'ipRule': 'string',
                'ruleDesc': 'string'
            },
        ]
    )
    
    
    :type GroupId: string
    :param GroupId: [REQUIRED]
            The identifier of the group.
            

    :type UserRules: list
    :param UserRules: [REQUIRED]
            The rules to add to the group.
            (dict) --Describes a rule for an IP access control group.
            ipRule (string) --The IP address range, in CIDR notation.
            ruleDesc (string) --The description.
            
            

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

def create_ip_group(GroupName=None, GroupDesc=None, UserRules=None):
    """
    Creates an IP access control group.
    An IP access control group provides you with the ability to control the IP addresses from which users are allowed to access their WorkSpaces. To specify the CIDR address ranges, add rules to your IP access control group and then associate the group with your directory. You can add rules when you create the group or at any time using  AuthorizeIpRules .
    There is a default IP access control group associated with your directory. If you don't associate an IP access control group with your directory, the default group is used. The default group includes a default rule that allows users to access their WorkSpaces from anywhere. You cannot modify the default IP access control group for your directory.
    See also: AWS API Documentation
    
    
    :example: response = client.create_ip_group(
        GroupName='string',
        GroupDesc='string',
        UserRules=[
            {
                'ipRule': 'string',
                'ruleDesc': 'string'
            },
        ]
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the group.
            

    :type GroupDesc: string
    :param GroupDesc: The description of the group.

    :type UserRules: list
    :param UserRules: The rules to add to the group.
            (dict) --Describes a rule for an IP access control group.
            ipRule (string) --The IP address range, in CIDR notation.
            ruleDesc (string) --The description.
            
            

    :rtype: dict
    :return: {
        'GroupId': 'string'
    }
    
    
    """
    pass

def create_tags(ResourceId=None, Tags=None):
    """
    Creates the specified tags for the specified WorkSpace.
    See also: AWS API Documentation
    
    
    :example: response = client.create_tags(
        ResourceId='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The identifier of the WorkSpace. To find this ID, use DescribeWorkspaces .
            

    :type Tags: list
    :param Tags: [REQUIRED]
            The tags. Each WorkSpace can have a maximum of 50 tags.
            (dict) --Describes a tag.
            Key (string) -- [REQUIRED]The key of the tag.
            Value (string) --The value of the tag.
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_workspaces(Workspaces=None):
    """
    Creates one or more WorkSpaces.
    This operation is asynchronous and returns before the WorkSpaces are created.
    See also: AWS API Documentation
    
    
    :example: response = client.create_workspaces(
        Workspaces=[
            {
                'DirectoryId': 'string',
                'UserName': 'string',
                'BundleId': 'string',
                'VolumeEncryptionKey': 'string',
                'UserVolumeEncryptionEnabled': True|False,
                'RootVolumeEncryptionEnabled': True|False,
                'WorkspaceProperties': {
                    'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
                    'RunningModeAutoStopTimeoutInMinutes': 123,
                    'RootVolumeSizeGib': 123,
                    'UserVolumeSizeGib': 123,
                    'ComputeTypeName': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'|'POWERPRO'|'GRAPHICSPRO'
                },
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    )
    
    
    :type Workspaces: list
    :param Workspaces: [REQUIRED]
            The WorkSpaces to create. You can specify up to 25 WorkSpaces.
            (dict) --Describes the information used to create a WorkSpace.
            DirectoryId (string) -- [REQUIRED]The identifier of the AWS Directory Service directory for the WorkSpace. You can use DescribeWorkspaceDirectories to list the available directories.
            UserName (string) -- [REQUIRED]The username of the user for the WorkSpace. This username must exist in the AWS Directory Service directory for the WorkSpace.
            BundleId (string) -- [REQUIRED]The identifier of the bundle for the WorkSpace. You can use DescribeWorkspaceBundles to list the available bundles.
            VolumeEncryptionKey (string) --The KMS key used to encrypt data stored on your WorkSpace.
            UserVolumeEncryptionEnabled (boolean) --Indicates whether the data stored on the user volume is encrypted.
            RootVolumeEncryptionEnabled (boolean) --Indicates whether the data stored on the root volume is encrypted.
            WorkspaceProperties (dict) --The WorkSpace properties.
            RunningMode (string) --The running mode. For more information, see Manage the WorkSpace Running Mode .
            RunningModeAutoStopTimeoutInMinutes (integer) --The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60 minute intervals.
            RootVolumeSizeGib (integer) --The size of the root volume.
            UserVolumeSizeGib (integer) --The size of the user storage.
            ComputeTypeName (string) --The compute type. For more information, see Amazon WorkSpaces Bundles .
            Tags (list) --The tags for the WorkSpace.
            (dict) --Describes a tag.
            Key (string) -- [REQUIRED]The key of the tag.
            Value (string) --The value of the tag.
            
            
            

    :rtype: dict
    :return: {
        'FailedRequests': [
            {
                'WorkspaceRequest': {
                    'DirectoryId': 'string',
                    'UserName': 'string',
                    'BundleId': 'string',
                    'VolumeEncryptionKey': 'string',
                    'UserVolumeEncryptionEnabled': True|False,
                    'RootVolumeEncryptionEnabled': True|False,
                    'WorkspaceProperties': {
                        'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
                        'RunningModeAutoStopTimeoutInMinutes': 123,
                        'RootVolumeSizeGib': 123,
                        'UserVolumeSizeGib': 123,
                        'ComputeTypeName': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'|'POWERPRO'|'GRAPHICSPRO'
                    },
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                },
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ],
        'PendingRequests': [
            {
                'WorkspaceId': 'string',
                'DirectoryId': 'string',
                'UserName': 'string',
                'IpAddress': 'string',
                'State': 'PENDING'|'AVAILABLE'|'IMPAIRED'|'UNHEALTHY'|'REBOOTING'|'STARTING'|'REBUILDING'|'MAINTENANCE'|'ADMIN_MAINTENANCE'|'TERMINATING'|'TERMINATED'|'SUSPENDED'|'UPDATING'|'STOPPING'|'STOPPED'|'ERROR',
                'BundleId': 'string',
                'SubnetId': 'string',
                'ErrorMessage': 'string',
                'ErrorCode': 'string',
                'ComputerName': 'string',
                'VolumeEncryptionKey': 'string',
                'UserVolumeEncryptionEnabled': True|False,
                'RootVolumeEncryptionEnabled': True|False,
                'WorkspaceProperties': {
                    'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
                    'RunningModeAutoStopTimeoutInMinutes': 123,
                    'RootVolumeSizeGib': 123,
                    'UserVolumeSizeGib': 123,
                    'ComputeTypeName': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'|'POWERPRO'|'GRAPHICSPRO'
                },
                'ModificationStates': [
                    {
                        'Resource': 'ROOT_VOLUME'|'USER_VOLUME'|'COMPUTE_TYPE',
                        'State': 'UPDATE_INITIATED'|'UPDATE_IN_PROGRESS'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def delete_ip_group(GroupId=None):
    """
    Deletes the specified IP access control group.
    You cannot delete an IP access control group that is associated with a directory.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_ip_group(
        GroupId='string'
    )
    
    
    :type GroupId: string
    :param GroupId: [REQUIRED]
            The identifier of the IP access control group.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_tags(ResourceId=None, TagKeys=None):
    """
    Deletes the specified tags from the specified WorkSpace.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_tags(
        ResourceId='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The identifier of the WorkSpace. To find this ID, use DescribeWorkspaces .
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            The tag keys.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_workspace_image(ImageId=None):
    """
    Deletes the specified image from your account. To delete an image, you must first delete any bundles that are associated with the image.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_workspace_image(
        ImageId='string'
    )
    
    
    :type ImageId: string
    :param ImageId: [REQUIRED]
            The identifier of the image.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_account():
    """
    Retrieves a list that describes the configuration of bring your own license (BYOL) for the specified account.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_account()
    
    
    :rtype: dict
    :return: {
        'DedicatedTenancySupport': 'ENABLED'|'DISABLED',
        'DedicatedTenancyManagementCidrRange': 'string'
    }
    
    
    """
    pass

def describe_account_modifications(NextToken=None):
    """
    Retrieves a list that describes modifications to the configuration of bring your own license (BYOL) for the specified account.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_account_modifications(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: If you received a NextToken from a previous call that was paginated, provide this token to receive the next set of results.

    :rtype: dict
    :return: {
        'AccountModifications': [
            {
                'ModificationState': 'PENDING'|'COMPLETED'|'FAILED',
                'DedicatedTenancySupport': 'ENABLED'|'DISABLED',
                'DedicatedTenancyManagementCidrRange': 'string',
                'StartTime': datetime(2015, 1, 1),
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_client_properties(ResourceIds=None):
    """
    Retrieves a list that describes one or more specified Amazon WorkSpaces clients.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_client_properties(
        ResourceIds=[
            'string',
        ]
    )
    
    
    :type ResourceIds: list
    :param ResourceIds: [REQUIRED]
            The resource identifiers, in the form of directory IDs.
            (string) --
            

    :rtype: dict
    :return: {
        'ClientPropertiesList': [
            {
                'ResourceId': 'string',
                'ClientProperties': {
                    'ReconnectEnabled': 'ENABLED'|'DISABLED'
                }
            },
        ]
    }
    
    
    """
    pass

def describe_ip_groups(GroupIds=None, NextToken=None, MaxResults=None):
    """
    Describes one or more of your IP access control groups.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_ip_groups(
        GroupIds=[
            'string',
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type GroupIds: list
    :param GroupIds: The identifiers of one or more IP access control groups.
            (string) --
            

    :type NextToken: string
    :param NextToken: If you received a NextToken from a previous call that was paginated, provide this token to receive the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return.

    :rtype: dict
    :return: {
        'Result': [
            {
                'groupId': 'string',
                'groupName': 'string',
                'groupDesc': 'string',
                'userRules': [
                    {
                        'ipRule': 'string',
                        'ruleDesc': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_tags(ResourceId=None):
    """
    Describes the specified tags for the specified WorkSpace.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_tags(
        ResourceId='string'
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The identifier of the WorkSpace. To find this ID, use DescribeWorkspaces .
            

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

def describe_workspace_bundles(BundleIds=None, Owner=None, NextToken=None):
    """
    Retrieves a list that describes the available WorkSpace bundles.
    You can filter the results using either bundle ID or owner, but not both.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_workspace_bundles(
        BundleIds=[
            'string',
        ],
        Owner='string',
        NextToken='string'
    )
    
    
    :type BundleIds: list
    :param BundleIds: The identifiers of the bundles. You cannot combine this parameter with any other filter.
            (string) --
            

    :type Owner: string
    :param Owner: The owner of the bundles. You cannot combine this parameter with any other filter.
            Specify AMAZON to describe the bundles provided by AWS or null to describe the bundles that belong to your account.
            

    :type NextToken: string
    :param NextToken: The token for the next set of results. (You received this token from a previous call.)

    :rtype: dict
    :return: {
        'Bundles': [
            {
                'BundleId': 'string',
                'Name': 'string',
                'Owner': 'string',
                'Description': 'string',
                'RootStorage': {
                    'Capacity': 'string'
                },
                'UserStorage': {
                    'Capacity': 'string'
                },
                'ComputeType': {
                    'Name': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'|'POWERPRO'|'GRAPHICSPRO'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_workspace_directories(DirectoryIds=None, NextToken=None):
    """
    Describes the available AWS Directory Service directories that are registered with Amazon WorkSpaces.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_workspace_directories(
        DirectoryIds=[
            'string',
        ],
        NextToken='string'
    )
    
    
    :type DirectoryIds: list
    :param DirectoryIds: The identifiers of the directories. If the value is null, all directories are retrieved.
            (string) --
            

    :type NextToken: string
    :param NextToken: If you received a NextToken from a previous call that was paginated, provide this token to receive the next set of results.

    :rtype: dict
    :return: {
        'Directories': [
            {
                'DirectoryId': 'string',
                'Alias': 'string',
                'DirectoryName': 'string',
                'RegistrationCode': 'string',
                'SubnetIds': [
                    'string',
                ],
                'DnsIpAddresses': [
                    'string',
                ],
                'CustomerUserName': 'string',
                'IamRoleId': 'string',
                'DirectoryType': 'SIMPLE_AD'|'AD_CONNECTOR',
                'WorkspaceSecurityGroupId': 'string',
                'State': 'REGISTERING'|'REGISTERED'|'DEREGISTERING'|'DEREGISTERED'|'ERROR',
                'WorkspaceCreationProperties': {
                    'EnableWorkDocs': True|False,
                    'EnableInternetAccess': True|False,
                    'DefaultOu': 'string',
                    'CustomSecurityGroupId': 'string',
                    'UserEnabledAsLocalAdministrator': True|False
                },
                'ipGroupIds': [
                    'string',
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_workspace_images(ImageIds=None, NextToken=None, MaxResults=None):
    """
    Retrieves a list that describes one or more specified images, if the image identifiers are provided. Otherwise, all images in the account are described.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_workspace_images(
        ImageIds=[
            'string',
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ImageIds: list
    :param ImageIds: The identifier of the image.
            (string) --
            

    :type NextToken: string
    :param NextToken: If you received a NextToken from a previous call that was paginated, provide this token to receive the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return.

    :rtype: dict
    :return: {
        'Images': [
            {
                'ImageId': 'string',
                'Name': 'string',
                'Description': 'string',
                'OperatingSystem': {
                    'Type': 'WINDOWS'|'LINUX'
                },
                'State': 'AVAILABLE'|'PENDING'|'ERROR',
                'RequiredTenancy': 'DEFAULT'|'DEDICATED',
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_workspaces(WorkspaceIds=None, DirectoryId=None, UserName=None, BundleId=None, Limit=None, NextToken=None):
    """
    Describes the specified WorkSpaces.
    You can filter the results by using the bundle identifier, directory identifier, or owner, but you can specify only one filter at a time.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_workspaces(
        WorkspaceIds=[
            'string',
        ],
        DirectoryId='string',
        UserName='string',
        BundleId='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type WorkspaceIds: list
    :param WorkspaceIds: The identifiers of the WorkSpaces. You cannot combine this parameter with any other filter.
            Because the CreateWorkspaces operation is asynchronous, the identifier it returns is not immediately available. If you immediately call DescribeWorkspaces with this identifier, no information is returned.
            (string) --
            

    :type DirectoryId: string
    :param DirectoryId: The identifier of the directory. In addition, you can optionally specify a specific directory user (see UserName ). You cannot combine this parameter with any other filter.

    :type UserName: string
    :param UserName: The name of the directory user. You must specify this parameter with DirectoryId .

    :type BundleId: string
    :param BundleId: The identifier of the bundle. All WorkSpaces that are created from this bundle are retrieved. You cannot combine this parameter with any other filter.

    :type Limit: integer
    :param Limit: The maximum number of items to return.

    :type NextToken: string
    :param NextToken: If you received a NextToken from a previous call that was paginated, provide this token to receive the next set of results.

    :rtype: dict
    :return: {
        'Workspaces': [
            {
                'WorkspaceId': 'string',
                'DirectoryId': 'string',
                'UserName': 'string',
                'IpAddress': 'string',
                'State': 'PENDING'|'AVAILABLE'|'IMPAIRED'|'UNHEALTHY'|'REBOOTING'|'STARTING'|'REBUILDING'|'MAINTENANCE'|'ADMIN_MAINTENANCE'|'TERMINATING'|'TERMINATED'|'SUSPENDED'|'UPDATING'|'STOPPING'|'STOPPED'|'ERROR',
                'BundleId': 'string',
                'SubnetId': 'string',
                'ErrorMessage': 'string',
                'ErrorCode': 'string',
                'ComputerName': 'string',
                'VolumeEncryptionKey': 'string',
                'UserVolumeEncryptionEnabled': True|False,
                'RootVolumeEncryptionEnabled': True|False,
                'WorkspaceProperties': {
                    'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
                    'RunningModeAutoStopTimeoutInMinutes': 123,
                    'RootVolumeSizeGib': 123,
                    'UserVolumeSizeGib': 123,
                    'ComputeTypeName': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'|'POWERPRO'|'GRAPHICSPRO'
                },
                'ModificationStates': [
                    {
                        'Resource': 'ROOT_VOLUME'|'USER_VOLUME'|'COMPUTE_TYPE',
                        'State': 'UPDATE_INITIATED'|'UPDATE_IN_PROGRESS'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_workspaces_connection_status(WorkspaceIds=None, NextToken=None):
    """
    Describes the connection status of the specified WorkSpaces.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_workspaces_connection_status(
        WorkspaceIds=[
            'string',
        ],
        NextToken='string'
    )
    
    
    :type WorkspaceIds: list
    :param WorkspaceIds: The identifiers of the WorkSpaces. You can specify up to 25 WorkSpaces.
            (string) --
            

    :type NextToken: string
    :param NextToken: If you received a NextToken from a previous call that was paginated, provide this token to receive the next set of results.

    :rtype: dict
    :return: {
        'WorkspacesConnectionStatus': [
            {
                'WorkspaceId': 'string',
                'ConnectionState': 'CONNECTED'|'DISCONNECTED'|'UNKNOWN',
                'ConnectionStateCheckTimestamp': datetime(2015, 1, 1),
                'LastKnownUserConnectionTimestamp': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def disassociate_ip_groups(DirectoryId=None, GroupIds=None):
    """
    Disassociates the specified IP access control group from the specified directory.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_ip_groups(
        DirectoryId='string',
        GroupIds=[
            'string',
        ]
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]
            The identifier of the directory.
            

    :type GroupIds: list
    :param GroupIds: [REQUIRED]
            The identifiers of one or more IP access control groups.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
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

def import_workspace_image(Ec2ImageId=None, IngestionProcess=None, ImageName=None, ImageDescription=None):
    """
    Imports the specified Windows 7 or Windows 10 bring your own license (BYOL) image into Amazon WorkSpaces. The image must be an already licensed EC2 image that is in your AWS account, and you must own the image.
    See also: AWS API Documentation
    
    
    :example: response = client.import_workspace_image(
        Ec2ImageId='string',
        IngestionProcess='BYOL_REGULAR'|'BYOL_GRAPHICS'|'BYOL_GRAPHICSPRO',
        ImageName='string',
        ImageDescription='string'
    )
    
    
    :type Ec2ImageId: string
    :param Ec2ImageId: [REQUIRED]
            The identifier of the EC2 image.
            

    :type IngestionProcess: string
    :param IngestionProcess: [REQUIRED]
            The ingestion process to be used when importing the image.
            

    :type ImageName: string
    :param ImageName: [REQUIRED]
            The name of the WorkSpace image.
            

    :type ImageDescription: string
    :param ImageDescription: [REQUIRED]
            The description of the WorkSpace image.
            

    :rtype: dict
    :return: {
        'ImageId': 'string'
    }
    
    
    """
    pass

def list_available_management_cidr_ranges(ManagementCidrRangeConstraint=None, MaxResults=None, NextToken=None):
    """
    Retrieves a list of IP address ranges, specified as IPv4 CIDR blocks, that you can use for the network management interface when you enable bring your own license (BYOL).
    The management network interface is connected to a secure Amazon WorkSpaces management network. It is used for interactive streaming of the WorkSpace desktop to Amazon WorkSpaces clients, and to allow Amazon WorkSpaces to manage the WorkSpace.
    See also: AWS API Documentation
    
    
    :example: response = client.list_available_management_cidr_ranges(
        ManagementCidrRangeConstraint='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ManagementCidrRangeConstraint: string
    :param ManagementCidrRangeConstraint: [REQUIRED]
            The IP address range to search. Specify an IP address range that is compatible with your network and in CIDR notation (that is, specify the range as an IPv4 CIDR block).
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return.

    :type NextToken: string
    :param NextToken: If you received a NextToken from a previous call that was paginated, provide this token to receive the next set of results.

    :rtype: dict
    :return: {
        'ManagementCidrRanges': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def modify_account(DedicatedTenancySupport=None, DedicatedTenancyManagementCidrRange=None):
    """
    Modifies the configuration of bring your own license (BYOL) for the specified account.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_account(
        DedicatedTenancySupport='ENABLED',
        DedicatedTenancyManagementCidrRange='string'
    )
    
    
    :type DedicatedTenancySupport: string
    :param DedicatedTenancySupport: The status of BYOL.

    :type DedicatedTenancyManagementCidrRange: string
    :param DedicatedTenancyManagementCidrRange: The IP address range, specified as an IPv4 CIDR block, for the management network interface. Specify an IP address range that is compatible with your network and in CIDR notation (that is, specify the range as an IPv4 CIDR block). The CIDR block size must be /16 (for example, 203.0.113.25/16). It must also be specified as available by the ListAvailableManagementCidrRanges operation.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def modify_client_properties(ResourceId=None, ClientProperties=None):
    """
    Modifies the properties of the specified Amazon WorkSpaces client.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_client_properties(
        ResourceId='string',
        ClientProperties={
            'ReconnectEnabled': 'ENABLED'|'DISABLED'
        }
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The resource identifiers, in the form of directory IDs.
            

    :type ClientProperties: dict
    :param ClientProperties: Information about the Amazon WorkSpaces client.
            ReconnectEnabled (string) --Specifies whether users can cache their credentials on the Amazon WorkSpaces client. When enabled, users can choose to reconnect to their WorkSpaces without re-entering their credentials.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def modify_workspace_properties(WorkspaceId=None, WorkspaceProperties=None):
    """
    Modifies the specified WorkSpace properties.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_workspace_properties(
        WorkspaceId='string',
        WorkspaceProperties={
            'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
            'RunningModeAutoStopTimeoutInMinutes': 123,
            'RootVolumeSizeGib': 123,
            'UserVolumeSizeGib': 123,
            'ComputeTypeName': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'|'POWERPRO'|'GRAPHICSPRO'
        }
    )
    
    
    :type WorkspaceId: string
    :param WorkspaceId: [REQUIRED]
            The identifier of the WorkSpace.
            

    :type WorkspaceProperties: dict
    :param WorkspaceProperties: [REQUIRED]
            The properties of the WorkSpace.
            RunningMode (string) --The running mode. For more information, see Manage the WorkSpace Running Mode .
            RunningModeAutoStopTimeoutInMinutes (integer) --The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60 minute intervals.
            RootVolumeSizeGib (integer) --The size of the root volume.
            UserVolumeSizeGib (integer) --The size of the user storage.
            ComputeTypeName (string) --The compute type. For more information, see Amazon WorkSpaces Bundles .
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def modify_workspace_state(WorkspaceId=None, WorkspaceState=None):
    """
    Sets the state of the specified WorkSpace.
    To maintain a WorkSpace without being interrupted, set the WorkSpace state to ADMIN_MAINTENANCE . WorkSpaces in this state do not respond to requests to reboot, stop, start, or rebuild. An AutoStop WorkSpace in this state is not stopped. Users can log into a WorkSpace in the ADMIN_MAINTENANCE state.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_workspace_state(
        WorkspaceId='string',
        WorkspaceState='AVAILABLE'|'ADMIN_MAINTENANCE'
    )
    
    
    :type WorkspaceId: string
    :param WorkspaceId: [REQUIRED]
            The identifier of the WorkSpace.
            

    :type WorkspaceState: string
    :param WorkspaceState: [REQUIRED]
            The WorkSpace state.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def reboot_workspaces(RebootWorkspaceRequests=None):
    """
    Reboots the specified WorkSpaces.
    You cannot reboot a WorkSpace unless its state is AVAILABLE or UNHEALTHY .
    This operation is asynchronous and returns before the WorkSpaces have rebooted.
    See also: AWS API Documentation
    
    
    :example: response = client.reboot_workspaces(
        RebootWorkspaceRequests=[
            {
                'WorkspaceId': 'string'
            },
        ]
    )
    
    
    :type RebootWorkspaceRequests: list
    :param RebootWorkspaceRequests: [REQUIRED]
            The WorkSpaces to reboot. You can specify up to 25 WorkSpaces.
            (dict) --Describes the information used to reboot a WorkSpace.
            WorkspaceId (string) -- [REQUIRED]The identifier of the WorkSpace.
            
            

    :rtype: dict
    :return: {
        'FailedRequests': [
            {
                'WorkspaceId': 'string',
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def rebuild_workspaces(RebuildWorkspaceRequests=None):
    """
    Rebuilds the specified WorkSpace.
    You cannot rebuild a WorkSpace unless its state is AVAILABLE , ERROR , or UNHEALTHY .
    Rebuilding a WorkSpace is a potentially destructive action that can result in the loss of data. For more information, see Rebuild a WorkSpace .
    This operation is asynchronous and returns before the WorkSpaces have been completely rebuilt.
    See also: AWS API Documentation
    
    
    :example: response = client.rebuild_workspaces(
        RebuildWorkspaceRequests=[
            {
                'WorkspaceId': 'string'
            },
        ]
    )
    
    
    :type RebuildWorkspaceRequests: list
    :param RebuildWorkspaceRequests: [REQUIRED]
            The WorkSpace to rebuild. You can specify a single WorkSpace.
            (dict) --Describes the information used to rebuild a WorkSpace.
            WorkspaceId (string) -- [REQUIRED]The identifier of the WorkSpace.
            
            

    :rtype: dict
    :return: {
        'FailedRequests': [
            {
                'WorkspaceId': 'string',
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def revoke_ip_rules(GroupId=None, UserRules=None):
    """
    Removes one or more rules from the specified IP access control group.
    See also: AWS API Documentation
    
    
    :example: response = client.revoke_ip_rules(
        GroupId='string',
        UserRules=[
            'string',
        ]
    )
    
    
    :type GroupId: string
    :param GroupId: [REQUIRED]
            The identifier of the group.
            

    :type UserRules: list
    :param UserRules: [REQUIRED]
            The rules to remove from the group.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def start_workspaces(StartWorkspaceRequests=None):
    """
    Starts the specified WorkSpaces.
    You cannot start a WorkSpace unless it has a running mode of AutoStop and a state of STOPPED .
    See also: AWS API Documentation
    
    
    :example: response = client.start_workspaces(
        StartWorkspaceRequests=[
            {
                'WorkspaceId': 'string'
            },
        ]
    )
    
    
    :type StartWorkspaceRequests: list
    :param StartWorkspaceRequests: [REQUIRED]
            The WorkSpaces to start. You can specify up to 25 WorkSpaces.
            (dict) --Information used to start a WorkSpace.
            WorkspaceId (string) --The identifier of the WorkSpace.
            
            

    :rtype: dict
    :return: {
        'FailedRequests': [
            {
                'WorkspaceId': 'string',
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def stop_workspaces(StopWorkspaceRequests=None):
    """
    Stops the specified WorkSpaces.
    You cannot stop a WorkSpace unless it has a running mode of AutoStop and a state of AVAILABLE , IMPAIRED , UNHEALTHY , or ERROR .
    See also: AWS API Documentation
    
    
    :example: response = client.stop_workspaces(
        StopWorkspaceRequests=[
            {
                'WorkspaceId': 'string'
            },
        ]
    )
    
    
    :type StopWorkspaceRequests: list
    :param StopWorkspaceRequests: [REQUIRED]
            The WorkSpaces to stop. You can specify up to 25 WorkSpaces.
            (dict) --Describes the information used to stop a WorkSpace.
            WorkspaceId (string) --The identifier of the WorkSpace.
            
            

    :rtype: dict
    :return: {
        'FailedRequests': [
            {
                'WorkspaceId': 'string',
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def terminate_workspaces(TerminateWorkspaceRequests=None):
    """
    Terminates the specified WorkSpaces.
    Terminating a WorkSpace is a permanent action and cannot be undone. The user's data is destroyed. If you need to archive any user data, contact Amazon Web Services before terminating the WorkSpace.
    You can terminate a WorkSpace that is in any state except SUSPENDED .
    This operation is asynchronous and returns before the WorkSpaces have been completely terminated.
    See also: AWS API Documentation
    
    
    :example: response = client.terminate_workspaces(
        TerminateWorkspaceRequests=[
            {
                'WorkspaceId': 'string'
            },
        ]
    )
    
    
    :type TerminateWorkspaceRequests: list
    :param TerminateWorkspaceRequests: [REQUIRED]
            The WorkSpaces to terminate. You can specify up to 25 WorkSpaces.
            (dict) --Describes the information used to terminate a WorkSpace.
            WorkspaceId (string) -- [REQUIRED]The identifier of the WorkSpace.
            
            

    :rtype: dict
    :return: {
        'FailedRequests': [
            {
                'WorkspaceId': 'string',
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def update_rules_of_ip_group(GroupId=None, UserRules=None):
    """
    Replaces the current rules of the specified IP access control group with the specified rules.
    See also: AWS API Documentation
    
    
    :example: response = client.update_rules_of_ip_group(
        GroupId='string',
        UserRules=[
            {
                'ipRule': 'string',
                'ruleDesc': 'string'
            },
        ]
    )
    
    
    :type GroupId: string
    :param GroupId: [REQUIRED]
            The identifier of the group.
            

    :type UserRules: list
    :param UserRules: [REQUIRED]
            One or more rules.
            (dict) --Describes a rule for an IP access control group.
            ipRule (string) --The IP address range, in CIDR notation.
            ruleDesc (string) --The description.
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

