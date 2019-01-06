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

def cancel_task_execution(TaskExecutionArn=None):
    """
    Cancels execution of a task.
    When you cancel a task execution, the transfer of some files are abruptly interrupted. The contents of files that are transferred to the destination might be incomplete or inconsistent with the source files. However, if you start a new task execution on the same task and you allow the task execution to complete, file content on the destination is complete and consistent. This applies to other unexpected failures that interrupt a task execution. In all of these cases, AWS DataSync successfully complete the transfer when you start the next task execution.
    See also: AWS API Documentation
    
    
    :example: response = client.cancel_task_execution(
        TaskExecutionArn='string'
    )
    
    
    :type TaskExecutionArn: string
    :param TaskExecutionArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the task execution to cancel.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_agent(ActivationKey=None, AgentName=None, Tags=None):
    """
    Activates an AWS DataSync agent that you have deployed on your host. The activation process associates your agent with your account. In the activation process, you specify information such as the AWS Region that you want to activate the agent in. You activate the agent in the AWS Region where your target locations (in Amazon S3 or Amazon EFS) reside. Your tasks are created in this AWS Region.
    You can use an agent for more than one location. If a task uses multiple agents, all of them need to have status AVAILABLE for the task to run. If you use multiple agents for a source location, the status of all the agents must be AVAILABLE for the task to run. For more information, see Activating a Sync Agent in the AWS DataSync User Guide.
    Agents are automatically updated by AWS on a regular basis, using a mechanism that ensures minimal interruption to your tasks.
    See also: AWS API Documentation
    
    
    :example: response = client.create_agent(
        ActivationKey='string',
        AgentName='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ActivationKey: string
    :param ActivationKey: [REQUIRED]
            Your agent activation key. You can get the activation key either by sending an HTTP GET request with redirects that enable you to get the agent IP address (port 80). Alternatively, you can get it from the AWS DataSync console.
            The redirect URL returned in the response provides you the activation key for your agent in the query string parameter activationKey . It might also include other activation-related parameters; however, these are merely defaults. The arguments you pass to this API call determine the actual configuration of your agent. For more information, see Activating a Sync Agent in the AWS DataSync User Guide.
            

    :type AgentName: string
    :param AgentName: The name you configured for your agent. This value is a text reference that is used to identify the agent in the console.

    :type Tags: list
    :param Tags: The key-value pair that represents the tag you want to associate with the agent. The value can be an empty string. This value helps you manage, filter, and search for your agents.
            Note
            Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @.
            (dict) --Represents a single entry in a list of AWS resource tags. TagListEntry returns an array that contains a list of tasks when the ListTagsForResource operation is called.
            Key (string) --The key for an AWS resource tag.
            Value (string) --The value for an AWS resource tag.
            
            

    :rtype: dict
    :return: {
        'AgentArn': 'string'
    }
    
    
    """
    pass

def create_location_efs(Subdirectory=None, EfsFilesystemArn=None, Ec2Config=None, Tags=None):
    """
    Creates an endpoint for an Amazon EFS file system.
    See also: AWS API Documentation
    
    
    :example: response = client.create_location_efs(
        Subdirectory='string',
        EfsFilesystemArn='string',
        Ec2Config={
            'SubnetArn': 'string',
            'SecurityGroupArns': [
                'string',
            ]
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Subdirectory: string
    :param Subdirectory: [REQUIRED]
            A subdirectory in the location s path. This subdirectory in the EFS file system is used to read data from the EFS source location or write data to the EFS destination. By default, AWS DataSync uses the root directory.
            

    :type EfsFilesystemArn: string
    :param EfsFilesystemArn: [REQUIRED]
            The Amazon Resource Name (ARN) for the Amazon EFS file system.
            

    :type Ec2Config: dict
    :param Ec2Config: [REQUIRED]
            The subnet and security group that the Amazon EFS file system uses.
            SubnetArn (string) -- [REQUIRED]The ARN of the subnet that the Amazon EC2 resource belongs in.
            SecurityGroupArns (list) -- [REQUIRED]The Amazon Resource Names (ARNs) of the security groups that are configured for the Amazon EC2 resource.
            (string) --
            

    :type Tags: list
    :param Tags: The key-value pair that represents a tag that you want to add to the resource. The value can be an empty string. This value helps you manage, filter, and search for your resources. We recommend that you create a name tag for your location.
            (dict) --Represents a single entry in a list of AWS resource tags. TagListEntry returns an array that contains a list of tasks when the ListTagsForResource operation is called.
            Key (string) --The key for an AWS resource tag.
            Value (string) --The value for an AWS resource tag.
            
            

    :rtype: dict
    :return: {
        'LocationArn': 'string'
    }
    
    
    """
    pass

def create_location_nfs(Subdirectory=None, ServerHostname=None, OnPremConfig=None, Tags=None):
    """
    Creates an endpoint for a Network File System (NFS) file system.
    See also: AWS API Documentation
    
    
    :example: response = client.create_location_nfs(
        Subdirectory='string',
        ServerHostname='string',
        OnPremConfig={
            'AgentArns': [
                'string',
            ]
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Subdirectory: string
    :param Subdirectory: [REQUIRED]
            The subdirectory in the NFS file system that is used to read data from the NFS source location or write data to the NFS destination. The NFS path should be a path that's exported by the NFS server, or a subdirectory of that path. The path should be such that it can be mounted by other NFS clients in your network.
            To see all the paths exported by your NFS server. run 'showmount -e nfs-server-name ' from an NFS client that has access to your server. You can specify any directory that appears in the results, and any subdirectory of that directory. Ensure that the NFS export is accessible without Kerberos authentication.
            To transfer all the data in the folder you specified, DataSync needs to have permissions to read all the data. To ensure this, either configure the NFS export with no_root_squash, or ensure that the permissions for all of the files that you want sync allow read access for all users. Doing either enables the agent to read the files. For the agent to access directories, you must additionally enable all execute access. For information about NFS export configuration, see 18.7. The /etc/exports Configuration File in the Centos documentation.
            

    :type ServerHostname: string
    :param ServerHostname: [REQUIRED]
            The name of the NFS server. This value is the IP address or Domain Name Service (DNS) name of the NFS server. An agent that is installed on-premises uses this host name to mount the NFS server in a network.
            Note
            This name must either be DNS-compliant or must be an IP version 4 (IPv4) address.
            

    :type OnPremConfig: dict
    :param OnPremConfig: [REQUIRED]
            Contains a list of Amazon Resource Names (ARNs) of agents that are used to connect to an NFS server.
            AgentArns (list) -- [REQUIRED]ARNs)of the agents to use for an NFS location.
            (string) --
            

    :type Tags: list
    :param Tags: The key-value pair that represents the tag that you want to add to the location. The value can be an empty string. We recommend using tags to name your resources.
            (dict) --Represents a single entry in a list of AWS resource tags. TagListEntry returns an array that contains a list of tasks when the ListTagsForResource operation is called.
            Key (string) --The key for an AWS resource tag.
            Value (string) --The value for an AWS resource tag.
            
            

    :rtype: dict
    :return: {
        'LocationArn': 'string'
    }
    
    
    """
    pass

def create_location_s3(Subdirectory=None, S3BucketArn=None, S3Config=None, Tags=None):
    """
    Creates an endpoint for an Amazon S3 bucket.
    For AWS DataSync to access a destination S3 bucket, it needs an AWS Identity and Access Management (IAM) role that has the required permissions. You can set up the required permissions by creating an IAM policy that grants the required permissions and attaching the policy to the role. An example of such a policy is shown in the examples section. For more information, see Configuring Amazon S3 Location Settings in the AWS DataSync User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_location_s3(
        Subdirectory='string',
        S3BucketArn='string',
        S3Config={
            'BucketAccessRoleArn': 'string'
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Subdirectory: string
    :param Subdirectory: [REQUIRED]
            A subdirectory in the Amazon S3 bucket. This subdirectory in Amazon S3 is used to read data from the S3 source location or write data to the S3 destination.
            

    :type S3BucketArn: string
    :param S3BucketArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the Amazon S3 bucket.
            

    :type S3Config: dict
    :param S3Config: [REQUIRED]
            The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that is used to access an Amazon S3 bucket. For detailed information about using such a role, see Components and Terminology in the AWS DataSync User Guide .
            BucketAccessRoleArn (string) -- [REQUIRED]The Amazon S3 bucket to access. This bucket is used as a parameter in the CreateLocationS3 operation.
            

    :type Tags: list
    :param Tags: The key-value pair that represents the tag that you want to add to the location. The value can be an empty string. We recommend using tags to name your resources.
            (dict) --Represents a single entry in a list of AWS resource tags. TagListEntry returns an array that contains a list of tasks when the ListTagsForResource operation is called.
            Key (string) --The key for an AWS resource tag.
            Value (string) --The value for an AWS resource tag.
            
            

    :rtype: dict
    :return: {
        'LocationArn': 'string'
    }
    
    
    """
    pass

def create_task(SourceLocationArn=None, DestinationLocationArn=None, CloudWatchLogGroupArn=None, Name=None, Options=None, Tags=None):
    """
    Creates a task. A task is a set of two locations (source and destination) and a set of default OverrideOptions that you use to control the behavior of a task. If you don't specify default values for Options when you create a task, AWS DataSync populates them with safe service defaults.
    When you initially create a task, it enters the INITIALIZING status and then the CREATING status. In CREATING status, AWS DataSync attempts to mount the source Network File System (NFS) location. The task transitions to the AVAILABLE status without waiting for the destination location to mount. Instead, AWS DataSync mounts a destination before every task execution and then unmounts it after every task execution.
    If an agent that is associated with a source (NFS) location goes offline, the task transitions to the UNAVAILABLE status. If the status of the task remains in the CREATING status for more than a few minutes, it means that your agent might be having trouble mounting the source NFS file system. Check the task's ErrorCode and ErrorDetail . Mount issues are often caused by either a misconfigured firewall or a mistyped NFS server host name.
    See also: AWS API Documentation
    
    
    :example: response = client.create_task(
        SourceLocationArn='string',
        DestinationLocationArn='string',
        CloudWatchLogGroupArn='string',
        Name='string',
        Options={
            'VerifyMode': 'POINT_IN_TIME_CONSISTENT'|'NONE',
            'Atime': 'NONE'|'BEST_EFFORT',
            'Mtime': 'NONE'|'PRESERVE',
            'Uid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
            'Gid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
            'PreserveDeletedFiles': 'PRESERVE'|'REMOVE',
            'PreserveDevices': 'NONE'|'PRESERVE',
            'PosixPermissions': 'NONE'|'BEST_EFFORT'|'PRESERVE',
            'BytesPerSecond': 123
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type SourceLocationArn: string
    :param SourceLocationArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the source location for the task.
            

    :type DestinationLocationArn: string
    :param DestinationLocationArn: [REQUIRED]
            The Amazon Resource Name (ARN) of an AWS storage resource's location.
            

    :type CloudWatchLogGroupArn: string
    :param CloudWatchLogGroupArn: The Amazon Resource Name (ARN) of the Amazon CloudWatch log group that is used to monitor and log events in the task. For more information on these groups, see Working with Log Groups and Log Streams in the Amazon CloudWatch User Guide.
            For more information about how to useCloudWatchLogs with DataSync, see Monitoring Your Task .
            

    :type Name: string
    :param Name: The name of a task. This value is a text reference that is used to identify the task in the console.

    :type Options: dict
    :param Options: The set of configuration options that control the behavior of a single execution of the task that occurs when you call StartTaskExecution . You can configure these options to preserve metadata such as user ID (UID) and group ID (GID), file permissions, data integrity verification, and so on.
            For each individual task execution, you can override these options by specifying the OverrideOptions before starting a the task execution. For more information, see the operation.
            VerifyMode (string) --A value that determines whether a data integrity verification should be performed at the end of a task execution after all data and metadata have been transferred.
            Default value: POINT_IN_TIME_CONSISTENT.
            POINT_IN_TIME_CONSISTENT: Perform verification (recommended).
            NONE: Skip verification.
            Atime (string) --A file metadata value that shows the last time a file was accessed (that is, when the file was read or written to). If you set Atime to BEST_EFFORT, DataSync attempts to preserve the original Atime attribute on all source files (that is, the version before the PREPARING phase). However, Atime 's behavior is not fully standard across platforms, so AWS DataSync can only do this on a best-effort basis.
            Default value: BEST_EFFORT.
            BEST_EFFORT: Attempt to preserve the per-file Atime value (recommended).
            NONE: Ignore Atime .
            Note
            If Atime is set to BEST_EFFORT, Mtime must be set to PRESERVE.
            If Atime is set to NONE, Mtime must also be NONE.
            Mtime (string) --A value that indicates the last time that a file was modified (that is, a file was written to) before the PREPARING phase.
            Default value: PRESERVE.
            PRESERVE: Preserve original Mtime (recommended)
            NONE: Ignore Mtime .
            Note
            If Mtime is set to PRESERVE, Atime must be set to BEST_EFFORT.
            If Mtime is set to NONE, Atime must also be set to NONE.
            Uid (string) --The user ID (UID) of the file's owner.
            Default value: INT_VALUE. This preserves the integer value of the ID.
            INT_VALUE: Preserve the integer value of UID and group ID (GID) (recommended).
            NONE: Ignore UID and GID.
            Gid (string) --The group ID (GID) of the file's owners.
            Default value: INT_VALUE. This preserves the integer value of the ID.
            INT_VALUE: Preserve the integer value of user ID (UID) and GID (recommended).
            NONE: Ignore UID and GID.
            PreserveDeletedFiles (string) --A value that specifies whether files in the destination that don't exist in the source file system should be preserved.
            Default value: PRESERVE.
            PRESERVE: Ignore such destination files (recommended).
            REMOVE: Delete destination files that aren t present in the source.
            PreserveDevices (string) --A value that determines whether AWS DataSync should preserve the metadata of block and character devices in the source file system, and recreate the files with that device name and metadata on the destination.
            Note
            AWS DataSync can't sync the actual contents of such devices, because they are nonterminal and don't return an end-of-file (EOF) marker.
            Default value: NONE.
            NONE: Ignore special devices (recommended).
            PRESERVE: Preserve character and block device metadata. This option isn't currently supported for Amazon EFS.
            PosixPermissions (string) --A value that determines which users or groups can access a file for a specific purpose such as reading, writing, or execution of the file.
            Default value: PRESERVE.
            PRESERVE: Preserve POSIX-style permissions (recommended).
            NONE: Ignore permissions.
            Note
            AWS DataSync can preserve extant permissions of a source location.
            BytesPerSecond (integer) --A value that limits the bandwidth used by AWS DataSync. For example, if you want AWS DataSync to use a maximum of 1 MB, set this value to 1048576 (=1024*1024 ).
            

    :type Tags: list
    :param Tags: The key-value pair that represents the tag that you want to add to the resource. The value can be an empty string.
            (dict) --Represents a single entry in a list of AWS resource tags. TagListEntry returns an array that contains a list of tasks when the ListTagsForResource operation is called.
            Key (string) --The key for an AWS resource tag.
            Value (string) --The value for an AWS resource tag.
            
            

    :rtype: dict
    :return: {
        'TaskArn': 'string'
    }
    
    
    """
    pass

def delete_agent(AgentArn=None):
    """
    Deletes an agent. To specify which agent to delete, use the Amazon Resource Name (ARN) of the agent in your request. The operation disassociates the agent from your AWS account. However, it doesn't delete the agent virtual machine (VM) from your on-premises environment.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_agent(
        AgentArn='string'
    )
    
    
    :type AgentArn: string
    :param AgentArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the agent to delete. Use the ListAgents operation to return a list of agents for your account and AWS Region.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_location(LocationArn=None):
    """
    Deletes the configuration of a location used by AWS DataSync.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_location(
        LocationArn='string'
    )
    
    
    :type LocationArn: string
    :param LocationArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the location to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_task(TaskArn=None):
    """
    Deletes a task.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_task(
        TaskArn='string'
    )
    
    
    :type TaskArn: string
    :param TaskArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the task to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_agent(AgentArn=None):
    """
    Returns metadata such as the name, the network interfaces, and the status (that is, whether the agent is running or not) for an agent. To specify which agent to describe, use the Amazon Resource Name (ARN) of the agent in your request.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_agent(
        AgentArn='string'
    )
    
    
    :type AgentArn: string
    :param AgentArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the agent to describe.
            

    :rtype: dict
    :return: {
        'AgentArn': 'string',
        'Name': 'string',
        'Status': 'ONLINE'|'OFFLINE',
        'LastConnectionTime': datetime(2015, 1, 1),
        'CreationTime': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_location_efs(LocationArn=None):
    """
    Returns metadata, such as the path information about an Amazon EFS location.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_location_efs(
        LocationArn='string'
    )
    
    
    :type LocationArn: string
    :param LocationArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the EFS location to describe.
            

    :rtype: dict
    :return: {
        'LocationArn': 'string',
        'LocationUri': 'string',
        'Ec2Config': {
            'SubnetArn': 'string',
            'SecurityGroupArns': [
                'string',
            ]
        },
        'CreationTime': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_location_nfs(LocationArn=None):
    """
    Returns metadata, such as the path information, about a NFS location.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_location_nfs(
        LocationArn='string'
    )
    
    
    :type LocationArn: string
    :param LocationArn: [REQUIRED]
            The Amazon resource Name (ARN) of the NFS location to describe.
            

    :rtype: dict
    :return: {
        'LocationArn': 'string',
        'LocationUri': 'string',
        'OnPremConfig': {
            'AgentArns': [
                'string',
            ]
        },
        'CreationTime': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_location_s3(LocationArn=None):
    """
    Returns metadata, such as bucket name, about an Amazon S3 bucket location.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_location_s3(
        LocationArn='string'
    )
    
    
    :type LocationArn: string
    :param LocationArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the Amazon S3 bucket location to describe.
            

    :rtype: dict
    :return: {
        'LocationArn': 'string',
        'LocationUri': 'string',
        'S3Config': {
            'BucketAccessRoleArn': 'string'
        },
        'CreationTime': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_task(TaskArn=None):
    """
    Returns metadata about a task.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_task(
        TaskArn='string'
    )
    
    
    :type TaskArn: string
    :param TaskArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the task to describe.
            

    :rtype: dict
    :return: {
        'TaskArn': 'string',
        'Status': 'AVAILABLE'|'CREATING'|'RUNNING'|'UNAVAILABLE',
        'Name': 'string',
        'CurrentTaskExecutionArn': 'string',
        'SourceLocationArn': 'string',
        'DestinationLocationArn': 'string',
        'CloudWatchLogGroupArn': 'string',
        'Options': {
            'VerifyMode': 'POINT_IN_TIME_CONSISTENT'|'NONE',
            'Atime': 'NONE'|'BEST_EFFORT',
            'Mtime': 'NONE'|'PRESERVE',
            'Uid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
            'Gid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
            'PreserveDeletedFiles': 'PRESERVE'|'REMOVE',
            'PreserveDevices': 'NONE'|'PRESERVE',
            'PosixPermissions': 'NONE'|'BEST_EFFORT'|'PRESERVE',
            'BytesPerSecond': 123
        },
        'ErrorCode': 'string',
        'ErrorDetail': 'string',
        'CreationTime': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_task_execution(TaskExecutionArn=None):
    """
    Returns detailed metadata about a task that is being executed.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_task_execution(
        TaskExecutionArn='string'
    )
    
    
    :type TaskExecutionArn: string
    :param TaskExecutionArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the task that is being executed.
            

    :rtype: dict
    :return: {
        'TaskExecutionArn': 'string',
        'Status': 'LAUNCHING'|'PREPARING'|'TRANSFERRING'|'VERIFYING'|'SUCCESS'|'ERROR',
        'Options': {
            'VerifyMode': 'POINT_IN_TIME_CONSISTENT'|'NONE',
            'Atime': 'NONE'|'BEST_EFFORT',
            'Mtime': 'NONE'|'PRESERVE',
            'Uid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
            'Gid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
            'PreserveDeletedFiles': 'PRESERVE'|'REMOVE',
            'PreserveDevices': 'NONE'|'PRESERVE',
            'PosixPermissions': 'NONE'|'BEST_EFFORT'|'PRESERVE',
            'BytesPerSecond': 123
        },
        'StartTime': datetime(2015, 1, 1),
        'EstimatedFilesToTransfer': 123,
        'EstimatedBytesToTransfer': 123,
        'FilesTransferred': 123,
        'BytesWritten': 123,
        'BytesTransferred': 123,
        'Result': {
            'PrepareDuration': 123,
            'PrepareStatus': 'PENDING'|'SUCCESS'|'ERROR',
            'TransferDuration': 123,
            'TransferStatus': 'PENDING'|'SUCCESS'|'ERROR',
            'VerifyDuration': 123,
            'VerifyStatus': 'PENDING'|'SUCCESS'|'ERROR',
            'ErrorCode': 'string',
            'ErrorDetail': 'string'
        }
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

def list_agents(MaxResults=None, NextToken=None):
    """
    Returns a list of agents owned by an AWS account in the AWS Region specified in the request. The returned list is ordered by agent Amazon Resource Name (ARN).
    By default, this operation returns a maximum of 100 agents. This operation supports pagination that enables you to optionally reduce the number of agents returned in a response.
    If you have more agents than are returned in a response (that is, the response returns only a truncated list of your agents), the response contains a marker that you can specify in your next request to fetch the next page of agents.
    See also: AWS API Documentation
    
    
    :example: response = client.list_agents(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of agents to list.

    :type NextToken: string
    :param NextToken: An opaque string that indicates the position at which to begin the next list of agents.

    :rtype: dict
    :return: {
        'Agents': [
            {
                'AgentArn': 'string',
                'Name': 'string',
                'Status': 'ONLINE'|'OFFLINE'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_locations(MaxResults=None, NextToken=None):
    """
    Returns a lists of source and destination locations.
    If you have more locations than are returned in a response (that is, the response returns only a truncated list of your agents), the response contains a token that you can specify in your next request to fetch the next page of locations.
    See also: AWS API Documentation
    
    
    :example: response = client.list_locations(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of locations to return.

    :type NextToken: string
    :param NextToken: An opaque string that indicates the position at which to begin the next list of locations.

    :rtype: dict
    :return: {
        'Locations': [
            {
                'LocationArn': 'string',
                'LocationUri': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_tags_for_resource(ResourceArn=None, MaxResults=None, NextToken=None):
    """
    Returns all the tags associated with a specified resources.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource whose tags to list.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of locations to return.

    :type NextToken: string
    :param NextToken: An opaque string that indicates the position at which to begin the next list of locations.

    :rtype: dict
    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_task_executions(TaskArn=None, MaxResults=None, NextToken=None):
    """
    Returns a list of executed tasks.
    See also: AWS API Documentation
    
    
    :example: response = client.list_task_executions(
        TaskArn='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type TaskArn: string
    :param TaskArn: The Amazon Resource Name (ARN) of the task whose tasks you want to list.

    :type MaxResults: integer
    :param MaxResults: The maximum number of executed tasks to list.

    :type NextToken: string
    :param NextToken: An opaque string that indicates the position at which to begin the next list of the executed tasks.

    :rtype: dict
    :return: {
        'TaskExecutions': [
            {
                'TaskExecutionArn': 'string',
                'Status': 'LAUNCHING'|'PREPARING'|'TRANSFERRING'|'VERIFYING'|'SUCCESS'|'ERROR'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_tasks(MaxResults=None, NextToken=None):
    """
    Returns a list of all the tasks.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tasks(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of tasks to return.

    :type NextToken: string
    :param NextToken: An opaque string that indicates the position at which to begin the next list of tasks.

    :rtype: dict
    :return: {
        'Tasks': [
            {
                'TaskArn': 'string',
                'Status': 'AVAILABLE'|'CREATING'|'RUNNING'|'UNAVAILABLE',
                'Name': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def start_task_execution(TaskArn=None, OverrideOptions=None):
    """
    Starts a specific invocation of a task. A TaskExecution value represents an individual run of a task. Each task can have at most one TaskExecution at a time.
    For detailed information, see Task Execution in Components and Terminology in the AWS DataSync User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.start_task_execution(
        TaskArn='string',
        OverrideOptions={
            'VerifyMode': 'POINT_IN_TIME_CONSISTENT'|'NONE',
            'Atime': 'NONE'|'BEST_EFFORT',
            'Mtime': 'NONE'|'PRESERVE',
            'Uid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
            'Gid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
            'PreserveDeletedFiles': 'PRESERVE'|'REMOVE',
            'PreserveDevices': 'NONE'|'PRESERVE',
            'PosixPermissions': 'NONE'|'BEST_EFFORT'|'PRESERVE',
            'BytesPerSecond': 123
        }
    )
    
    
    :type TaskArn: string
    :param TaskArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the task to start.
            

    :type OverrideOptions: dict
    :param OverrideOptions: Represents the options that are available to control the behavior of a StartTaskExecution operation. Behavior includes preserving metadata such as user ID (UID), group ID (GID), and file permissions, and also overwriting files in the destination, data integrity verification, and so on.
            A task has a set of default options associated with it. If you don't specify an option in StartTaskExecution , the default value is used. You can override the defaults options on each task execution by specifying an overriding Options value to StartTaskExecution .
            VerifyMode (string) --A value that determines whether a data integrity verification should be performed at the end of a task execution after all data and metadata have been transferred.
            Default value: POINT_IN_TIME_CONSISTENT.
            POINT_IN_TIME_CONSISTENT: Perform verification (recommended).
            NONE: Skip verification.
            Atime (string) --A file metadata value that shows the last time a file was accessed (that is, when the file was read or written to). If you set Atime to BEST_EFFORT, DataSync attempts to preserve the original Atime attribute on all source files (that is, the version before the PREPARING phase). However, Atime 's behavior is not fully standard across platforms, so AWS DataSync can only do this on a best-effort basis.
            Default value: BEST_EFFORT.
            BEST_EFFORT: Attempt to preserve the per-file Atime value (recommended).
            NONE: Ignore Atime .
            Note
            If Atime is set to BEST_EFFORT, Mtime must be set to PRESERVE.
            If Atime is set to NONE, Mtime must also be NONE.
            Mtime (string) --A value that indicates the last time that a file was modified (that is, a file was written to) before the PREPARING phase.
            Default value: PRESERVE.
            PRESERVE: Preserve original Mtime (recommended)
            NONE: Ignore Mtime .
            Note
            If Mtime is set to PRESERVE, Atime must be set to BEST_EFFORT.
            If Mtime is set to NONE, Atime must also be set to NONE.
            Uid (string) --The user ID (UID) of the file's owner.
            Default value: INT_VALUE. This preserves the integer value of the ID.
            INT_VALUE: Preserve the integer value of UID and group ID (GID) (recommended).
            NONE: Ignore UID and GID.
            Gid (string) --The group ID (GID) of the file's owners.
            Default value: INT_VALUE. This preserves the integer value of the ID.
            INT_VALUE: Preserve the integer value of user ID (UID) and GID (recommended).
            NONE: Ignore UID and GID.
            PreserveDeletedFiles (string) --A value that specifies whether files in the destination that don't exist in the source file system should be preserved.
            Default value: PRESERVE.
            PRESERVE: Ignore such destination files (recommended).
            REMOVE: Delete destination files that aren t present in the source.
            PreserveDevices (string) --A value that determines whether AWS DataSync should preserve the metadata of block and character devices in the source file system, and recreate the files with that device name and metadata on the destination.
            Note
            AWS DataSync can't sync the actual contents of such devices, because they are nonterminal and don't return an end-of-file (EOF) marker.
            Default value: NONE.
            NONE: Ignore special devices (recommended).
            PRESERVE: Preserve character and block device metadata. This option isn't currently supported for Amazon EFS.
            PosixPermissions (string) --A value that determines which users or groups can access a file for a specific purpose such as reading, writing, or execution of the file.
            Default value: PRESERVE.
            PRESERVE: Preserve POSIX-style permissions (recommended).
            NONE: Ignore permissions.
            Note
            AWS DataSync can preserve extant permissions of a source location.
            BytesPerSecond (integer) --A value that limits the bandwidth used by AWS DataSync. For example, if you want AWS DataSync to use a maximum of 1 MB, set this value to 1048576 (=1024*1024 ).
            

    :rtype: dict
    :return: {
        'TaskExecutionArn': 'string'
    }
    
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Applies a key-value pair to an AWS resource.
    See also: AWS API Documentation
    
    
    :example: response = client.tag_resource(
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
            The Amazon Resource Name (ARN) of the resource to apply the tag to.
            

    :type Tags: list
    :param Tags: [REQUIRED]
            The tags to apply.
            (dict) --Represents a single entry in a list of AWS resource tags. TagListEntry returns an array that contains a list of tasks when the ListTagsForResource operation is called.
            Key (string) --The key for an AWS resource tag.
            Value (string) --The value for an AWS resource tag.
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceArn=None, Keys=None):
    """
    Removes a tag from an AWS resource.
    See also: AWS API Documentation
    
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        Keys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource to remove the tag from.
            

    :type Keys: list
    :param Keys: [REQUIRED]
            The keys in the key-value pair in the tag to remove.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_agent(AgentArn=None, Name=None):
    """
    Updates the name of an agent.
    See also: AWS API Documentation
    
    
    :example: response = client.update_agent(
        AgentArn='string',
        Name='string'
    )
    
    
    :type AgentArn: string
    :param AgentArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the agent to update.
            

    :type Name: string
    :param Name: The name that you want to use to configure the agent.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_task(TaskArn=None, Options=None, Name=None):
    """
    Updates the metadata associated with a task.
    See also: AWS API Documentation
    
    
    :example: response = client.update_task(
        TaskArn='string',
        Options={
            'VerifyMode': 'POINT_IN_TIME_CONSISTENT'|'NONE',
            'Atime': 'NONE'|'BEST_EFFORT',
            'Mtime': 'NONE'|'PRESERVE',
            'Uid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
            'Gid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
            'PreserveDeletedFiles': 'PRESERVE'|'REMOVE',
            'PreserveDevices': 'NONE'|'PRESERVE',
            'PosixPermissions': 'NONE'|'BEST_EFFORT'|'PRESERVE',
            'BytesPerSecond': 123
        },
        Name='string'
    )
    
    
    :type TaskArn: string
    :param TaskArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource name of the task to update.
            

    :type Options: dict
    :param Options: Represents the options that are available to control the behavior of a StartTaskExecution operation. Behavior includes preserving metadata such as user ID (UID), group ID (GID), and file permissions, and also overwriting files in the destination, data integrity verification, and so on.
            A task has a set of default options associated with it. If you don't specify an option in StartTaskExecution , the default value is used. You can override the defaults options on each task execution by specifying an overriding Options value to StartTaskExecution .
            VerifyMode (string) --A value that determines whether a data integrity verification should be performed at the end of a task execution after all data and metadata have been transferred.
            Default value: POINT_IN_TIME_CONSISTENT.
            POINT_IN_TIME_CONSISTENT: Perform verification (recommended).
            NONE: Skip verification.
            Atime (string) --A file metadata value that shows the last time a file was accessed (that is, when the file was read or written to). If you set Atime to BEST_EFFORT, DataSync attempts to preserve the original Atime attribute on all source files (that is, the version before the PREPARING phase). However, Atime 's behavior is not fully standard across platforms, so AWS DataSync can only do this on a best-effort basis.
            Default value: BEST_EFFORT.
            BEST_EFFORT: Attempt to preserve the per-file Atime value (recommended).
            NONE: Ignore Atime .
            Note
            If Atime is set to BEST_EFFORT, Mtime must be set to PRESERVE.
            If Atime is set to NONE, Mtime must also be NONE.
            Mtime (string) --A value that indicates the last time that a file was modified (that is, a file was written to) before the PREPARING phase.
            Default value: PRESERVE.
            PRESERVE: Preserve original Mtime (recommended)
            NONE: Ignore Mtime .
            Note
            If Mtime is set to PRESERVE, Atime must be set to BEST_EFFORT.
            If Mtime is set to NONE, Atime must also be set to NONE.
            Uid (string) --The user ID (UID) of the file's owner.
            Default value: INT_VALUE. This preserves the integer value of the ID.
            INT_VALUE: Preserve the integer value of UID and group ID (GID) (recommended).
            NONE: Ignore UID and GID.
            Gid (string) --The group ID (GID) of the file's owners.
            Default value: INT_VALUE. This preserves the integer value of the ID.
            INT_VALUE: Preserve the integer value of user ID (UID) and GID (recommended).
            NONE: Ignore UID and GID.
            PreserveDeletedFiles (string) --A value that specifies whether files in the destination that don't exist in the source file system should be preserved.
            Default value: PRESERVE.
            PRESERVE: Ignore such destination files (recommended).
            REMOVE: Delete destination files that aren t present in the source.
            PreserveDevices (string) --A value that determines whether AWS DataSync should preserve the metadata of block and character devices in the source file system, and recreate the files with that device name and metadata on the destination.
            Note
            AWS DataSync can't sync the actual contents of such devices, because they are nonterminal and don't return an end-of-file (EOF) marker.
            Default value: NONE.
            NONE: Ignore special devices (recommended).
            PRESERVE: Preserve character and block device metadata. This option isn't currently supported for Amazon EFS.
            PosixPermissions (string) --A value that determines which users or groups can access a file for a specific purpose such as reading, writing, or execution of the file.
            Default value: PRESERVE.
            PRESERVE: Preserve POSIX-style permissions (recommended).
            NONE: Ignore permissions.
            Note
            AWS DataSync can preserve extant permissions of a source location.
            BytesPerSecond (integer) --A value that limits the bandwidth used by AWS DataSync. For example, if you want AWS DataSync to use a maximum of 1 MB, set this value to 1048576 (=1024*1024 ).
            

    :type Name: string
    :param Name: The name of the task to update.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

