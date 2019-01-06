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

def create_server(IdentityProviderDetails=None, IdentityProviderType=None, LoggingRole=None, Tags=None):
    """
    Instantiates an autoscaling virtual server based on Secure File Transfer Protocol (SFTP) in AWS. The call returns the ServerId property assigned by the service to the newly created server. Reference this ServerId property when you make updates to your server, or work with users.
    The response returns the ServerId value for the newly created server.
    See also: AWS API Documentation
    
    
    :example: response = client.create_server(
        IdentityProviderDetails={
            'Url': 'string',
            'InvocationRole': 'string'
        },
        IdentityProviderType='SERVICE_MANAGED'|'API_GATEWAY',
        LoggingRole='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type IdentityProviderDetails: dict
    :param IdentityProviderDetails: An array containing all of the information required to call a customer-supplied authentication API. This parameter is not required when the IdentityProviderType value of server that is created uses the SERVICE_MANAGED authentication method.
            Url (string) --The IdentityProviderDetail parameter contains the location of the service endpoint used to authenticate users.
            InvocationRole (string) --The Role parameter provides the type of InvocationRole used to authenticate the user account.
            

    :type IdentityProviderType: string
    :param IdentityProviderType: The mode of authentication enabled for this service. The default value is SERVICE_MANAGED , which allows you to store and access SFTP user credentials within the service. An IdentityProviderType value of API_GATEWAY indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.

    :type LoggingRole: string
    :param LoggingRole: A value that allows the service to write your SFTP users  activity to your Amazon CloudWatch logs for monitoring and auditing purposes.

    :type Tags: list
    :param Tags: Key-value pairs that can be used to group and search for servers.
            (dict) --Creates a key-value pair for a specific resource. Tags are metadata that you can use to search for and group a resource for various purposes. You can apply tags to servers, users, and roles. A tag key can take more than one value. For example, to group servers for accounting purposes, you might create a tag called Group and assign the values Research and Accounting to that group.
            Key (string) -- [REQUIRED]The name assigned to the tag that you create.
            Value (string) -- [REQUIRED]This property contains one or more values that you assigned to the key name you create.
            
            

    :rtype: dict
    :return: {
        'ServerId': 'string'
    }
    
    
    """
    pass

def create_user(HomeDirectory=None, Policy=None, Role=None, ServerId=None, SshPublicKeyBody=None, Tags=None, UserName=None):
    """
    Adds a user and associate them with an existing Secure File Transfer Protocol (SFTP) server. Using parameters for CreateUser , you can specify the user name, set the home directory, store the user's public key, and assign the user's AWS Identity and Access Management (IAM) role. You can also optionally add a scope-down policy, and assign metadata with tags that can be used to group and search for users.
    The response returns the UserName and ServerId values of the new user for that server.
    See also: AWS API Documentation
    
    
    :example: response = client.create_user(
        HomeDirectory='string',
        Policy='string',
        Role='string',
        ServerId='string',
        SshPublicKeyBody='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        UserName='string'
    )
    
    
    :type HomeDirectory: string
    :param HomeDirectory: The landing directory (folder) for a user when they log in to the server using their SFTP client. An example is ``/home/username `` .

    :type Policy: string
    :param Policy: A scope-down policy for your user so you can use the same IAM role across multiple users. This policy scopes down user access to portions of their Amazon S3 bucket. Variables you can use inside this policy include ${Transfer:UserName} , ${Transfer:HomeDirectory} , and ${Transfer:HomeBucket} .

    :type Role: string
    :param Role: [REQUIRED]
            The IAM role that controls your user s access to your Amazon S3 bucket. The policies attached to this role will determine the level of access you want to provide your users when transferring files into and out of your Amazon S3 bucket or buckets. The IAM role should also contain a trust relationship that allows the SFTP server to access your resources when servicing your SFTP user s transfer requests.
            

    :type ServerId: string
    :param ServerId: [REQUIRED]
            A system-assigned unique identifier for an SFTP server instance. This is the specific SFTP server that you added your user to.
            

    :type SshPublicKeyBody: string
    :param SshPublicKeyBody: The public portion of the Secure Shall (SSH) key used to authenticate the user to the SFTP server.

    :type Tags: list
    :param Tags: Key-value pairs that can be used to group and search for users. Tags are metadata attached to users for any purpose.
            (dict) --Creates a key-value pair for a specific resource. Tags are metadata that you can use to search for and group a resource for various purposes. You can apply tags to servers, users, and roles. A tag key can take more than one value. For example, to group servers for accounting purposes, you might create a tag called Group and assign the values Research and Accounting to that group.
            Key (string) -- [REQUIRED]The name assigned to the tag that you create.
            Value (string) -- [REQUIRED]This property contains one or more values that you assigned to the key name you create.
            
            

    :type UserName: string
    :param UserName: [REQUIRED]
            A unique string that identifies a user and is associated with a server as specified by the ServerId .
            

    :rtype: dict
    :return: {
        'ServerId': 'string',
        'UserName': 'string'
    }
    
    
    """
    pass

def delete_server(ServerId=None):
    """
    Deletes the Secure File Transfer Protocol (SFTP) server that you specify. If you used SERVICE_MANAGED as your IdentityProviderType , you need to delete all users associated with this server before deleting the server itself
    No response returns from this call.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_server(
        ServerId='string'
    )
    
    
    :type ServerId: string
    :param ServerId: [REQUIRED]
            A unique system-assigned identifier for an SFTP server instance.
            

    """
    pass

def delete_ssh_public_key(ServerId=None, SshPublicKeyId=None, UserName=None):
    """
    Deletes a user's Secure Shell (SSH) public key.
    No response is returned from this call.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_ssh_public_key(
        ServerId='string',
        SshPublicKeyId='string',
        UserName='string'
    )
    
    
    :type ServerId: string
    :param ServerId: [REQUIRED]
            A system-assigned unique identifier for a Secure File Transfer Protocol (SFTP) server instance that has the user assigned to it.
            

    :type SshPublicKeyId: string
    :param SshPublicKeyId: [REQUIRED]
            A unique identifier used to reference your user s specific SSH key.
            

    :type UserName: string
    :param UserName: [REQUIRED]
            A unique string that identifies a user whose public key is being deleted.
            

    """
    pass

def delete_user(ServerId=None, UserName=None):
    """
    Deletes the user belonging to the server you specify.
    No response returns from this call.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_user(
        ServerId='string',
        UserName='string'
    )
    
    
    :type ServerId: string
    :param ServerId: [REQUIRED]
            A system-assigned unique identifier for an SFTP server instance that has the user assigned to it.
            

    :type UserName: string
    :param UserName: [REQUIRED]
            A unique string that identifies a user that is being deleted from the server.
            

    """
    pass

def describe_server(ServerId=None):
    """
    Describes the server that you specify by passing the ServerId parameter.
    The response contains a description of the server's properties.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_server(
        ServerId='string'
    )
    
    
    :type ServerId: string
    :param ServerId: [REQUIRED]
            A system-assigned unique identifier for an SFTP server.
            

    :rtype: dict
    :return: {
        'Server': {
            'Arn': 'string',
            'IdentityProviderDetails': {
                'Url': 'string',
                'InvocationRole': 'string'
            },
            'IdentityProviderType': 'SERVICE_MANAGED'|'API_GATEWAY',
            'LoggingRole': 'string',
            'ServerId': 'string',
            'State': 'OFFLINE'|'ONLINE'|'STARTING'|'STOPPING'|'START_FAILED'|'STOP_FAILED',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'UserCount': 123
        }
    }
    
    
    """
    pass

def describe_user(ServerId=None, UserName=None):
    """
    Describes the user assigned to a specific server, as identified by its ServerId property.
    The response from this call returns the properties of the user associated with the ServerId value that was specified.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_user(
        ServerId='string',
        UserName='string'
    )
    
    
    :type ServerId: string
    :param ServerId: [REQUIRED]
            A system-assigned unique identifier for an SFTP server that has this user assigned.
            

    :type UserName: string
    :param UserName: [REQUIRED]
            The name of the user assigned to one or more servers. User names are part of the sign-in credentials to use the AWS Transfer service and perform file transfer tasks.
            

    :rtype: dict
    :return: {
        'ServerId': 'string',
        'User': {
            'Arn': 'string',
            'HomeDirectory': 'string',
            'Policy': 'string',
            'Role': 'string',
            'SshPublicKeys': [
                {
                    'DateImported': datetime(2015, 1, 1),
                    'SshPublicKeyBody': 'string',
                    'SshPublicKeyId': 'string'
                },
            ],
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'UserName': 'string'
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

def import_ssh_public_key(ServerId=None, SshPublicKeyBody=None, UserName=None):
    """
    Adds a Secure Shell (SSH) public key to a user account identified by a UserName value assigned to a specific server, identified by ServerId .
    The response returns the UserName value, the ServerId value, and the name of the SshPublicKeyId .
    See also: AWS API Documentation
    
    
    :example: response = client.import_ssh_public_key(
        ServerId='string',
        SshPublicKeyBody='string',
        UserName='string'
    )
    
    
    :type ServerId: string
    :param ServerId: [REQUIRED]
            A system-assigned unique identifier for an SFTP server.
            

    :type SshPublicKeyBody: string
    :param SshPublicKeyBody: [REQUIRED]
            The public key portion of an SSH key pair.
            

    :type UserName: string
    :param UserName: [REQUIRED]
            The name of the user account that is assigned to one or more servers.
            

    :rtype: dict
    :return: {
        'ServerId': 'string',
        'SshPublicKeyId': 'string',
        'UserName': 'string'
    }
    
    
    """
    pass

def list_servers(MaxResults=None, NextToken=None):
    """
    Lists the Secure File Transfer Protocol (SFTP) servers that are associated with your AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_servers(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: Specifies the number of servers to return as a response to the ListServers query.

    :type NextToken: string
    :param NextToken: When additional results are obtained from the ListServers command, a NextToken parameter is returned in the output. You can then pass the NextToken parameter in a subsequent command to continue listing additional servers.

    :rtype: dict
    :return: {
        'NextToken': 'string',
        'Servers': [
            {
                'Arn': 'string',
                'IdentityProviderType': 'SERVICE_MANAGED'|'API_GATEWAY',
                'LoggingRole': 'string',
                'ServerId': 'string',
                'State': 'OFFLINE'|'ONLINE'|'STARTING'|'STOPPING'|'START_FAILED'|'STOP_FAILED',
                'UserCount': 123
            },
        ]
    }
    
    
    """
    pass

def list_tags_for_resource(Arn=None, MaxResults=None, NextToken=None):
    """
    Lists all of the tags associated with the Amazon Resource Number (ARN) you specify. The resource can be a user, server, or role.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags_for_resource(
        Arn='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]
            Requests the tags associated with a particular Amazon Resource Name (ARN). An ARN is an identifier for a specific AWS resource, such as a server, user, or role.
            

    :type MaxResults: integer
    :param MaxResults: 

    :type NextToken: string
    :param NextToken: 

    :rtype: dict
    :return: {
        'Arn': 'string',
        'NextToken': 'string',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_users(MaxResults=None, NextToken=None, ServerId=None):
    """
    Lists the users for the server that you specify by passing the ServerId parameter.
    See also: AWS API Documentation
    
    
    :example: response = client.list_users(
        MaxResults=123,
        NextToken='string',
        ServerId='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: Specifies the number of users to return as a response to the ListUsers request.

    :type NextToken: string
    :param NextToken: When you can get additional results from the ListUsers ListUsers call, a NextToken parameter is returned in the output. You can then pass in a subsequent command the NextToken parameter to continue listing additional users.

    :type ServerId: string
    :param ServerId: [REQUIRED]
            A system-assigned unique identifier for a Secure File Transfer Protocol (SFTP) server that has users are assigned to it.
            

    :rtype: dict
    :return: {
        'NextToken': 'string',
        'ServerId': 'string',
        'Users': [
            {
                'Arn': 'string',
                'HomeDirectory': 'string',
                'Role': 'string',
                'SshPublicKeyCount': 123,
                'UserName': 'string'
            },
        ]
    }
    
    
    """
    pass

def start_server(ServerId=None):
    """
    Changes the state of a Secure File Transfer Protocol (SFTP) server from OFFLINE to ONLINE . It has no impact on an SFTP server that is already ONLINE . An ONLINE server can accept and process file transfer jobs.
    The state of STARTING indicates that the server is in an intermediate state, either not fully able to respond, or not fully online. The values of START_FAILED can indicate an error condition.
    No response is returned from this call.
    See also: AWS API Documentation
    
    
    :example: response = client.start_server(
        ServerId='string'
    )
    
    
    :type ServerId: string
    :param ServerId: [REQUIRED]
            A system-assigned unique identifier for an SFTP server that you start.
            

    """
    pass

def stop_server(ServerId=None):
    """
    Changes the state of an SFTP server from ONLINE to OFFLINE . An OFFLINE server cannot accept and process file transfer jobs. Information tied to your server such as server and user properties are not affected by stopping your server. Stopping a server will not reduce or impact your Secure File Transfer Protocol (SFTP) endpoint billing.
    The states of STOPPING indicates that the server is in an intermediate state, either not fully able to respond, or not fully offline. The values of STOP_FAILED can indicate an error condition.
    No response is returned from this call.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_server(
        ServerId='string'
    )
    
    
    :type ServerId: string
    :param ServerId: [REQUIRED]
            A system-assigned unique identifier for an SFTP server that you stopped.
            

    """
    pass

def tag_resource(Arn=None, Tags=None):
    """
    Attaches a key-value pair to a resource, as identified by its Amazon Resource Name (ARN). Resources are users, servers, roles, and other entities.
    There is no response returned from this call.
    See also: AWS API Documentation
    
    
    :example: response = client.tag_resource(
        Arn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]
            An Amazon Resource Name (ARN) for a specific AWS resource, such as a server, user, or role.
            

    :type Tags: list
    :param Tags: [REQUIRED]
            Key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to user accounts for any purpose.
            (dict) --Creates a key-value pair for a specific resource. Tags are metadata that you can use to search for and group a resource for various purposes. You can apply tags to servers, users, and roles. A tag key can take more than one value. For example, to group servers for accounting purposes, you might create a tag called Group and assign the values Research and Accounting to that group.
            Key (string) -- [REQUIRED]The name assigned to the tag that you create.
            Value (string) -- [REQUIRED]This property contains one or more values that you assigned to the key name you create.
            
            

    """
    pass

def test_identity_provider(ServerId=None, UserName=None, UserPassword=None):
    """
    If the IdentityProviderType of the server is API_Gateway , tests whether your API Gateway is set up successfully. We highly recommend that you call this method to test your authentication method as soon as you create your server. By doing so, you can troubleshoot issues with the API Gateway integration to ensure that your users can successfully use the service.
    See also: AWS API Documentation
    
    
    :example: response = client.test_identity_provider(
        ServerId='string',
        UserName='string',
        UserPassword='string'
    )
    
    
    :type ServerId: string
    :param ServerId: [REQUIRED]
            A system assigned identifier for a specific server. That server's user authentication method is tested with a user name and password.
            

    :type UserName: string
    :param UserName: [REQUIRED]
            This request parameter is name of the user account to be tested.
            

    :type UserPassword: string
    :param UserPassword: The password of the user account to be tested.

    :rtype: dict
    :return: {
        'Message': 'string',
        'StatusCode': 123,
        'Url': 'string'
    }
    
    
    """
    pass

def untag_resource(Arn=None, TagKeys=None):
    """
    Detaches a key-value pair from a resource, as identified by its Amazon Resource Name (ARN). Resources are users, servers, roles, and other entities.
    No response is returned from this call.
    See also: AWS API Documentation
    
    
    :example: response = client.untag_resource(
        Arn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]
            This is the value of the resource that will have the tag removed. An Amazon Resource Name (ARN) is an identifier for a specific AWS resource, such as a server, user, or role.
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            TagKeys are key-value pairs assigned to ARNs that can be used to group and search for resources by type. This metadata can be attached to resources for any purpose.
            (string) --
            

    """
    pass

def update_server(IdentityProviderDetails=None, LoggingRole=None, ServerId=None):
    """
    Updates the server properties after that server has been created.
    The UpdateServer call returns the ServerId of the Secure File Transfer Protocol (SFTP) server you updated.
    See also: AWS API Documentation
    
    
    :example: response = client.update_server(
        IdentityProviderDetails={
            'Url': 'string',
            'InvocationRole': 'string'
        },
        LoggingRole='string',
        ServerId='string'
    )
    
    
    :type IdentityProviderDetails: dict
    :param IdentityProviderDetails: This response parameter is an array containing all of the information required to call a customer's authentication API method.
            Url (string) --The IdentityProviderDetail parameter contains the location of the service endpoint used to authenticate users.
            InvocationRole (string) --The Role parameter provides the type of InvocationRole used to authenticate the user account.
            

    :type LoggingRole: string
    :param LoggingRole: Changes the AWS Identity and Access Management (IAM) role that allows Amazon S3 events to be logged in Amazon CloudWatch, turning logging on or off.

    :type ServerId: string
    :param ServerId: [REQUIRED]
            A system-assigned unique identifier for an SFTP server instance that the user account is assigned to.
            

    :rtype: dict
    :return: {
        'ServerId': 'string'
    }
    
    
    """
    pass

def update_user(HomeDirectory=None, Policy=None, Role=None, ServerId=None, UserName=None):
    """
    Assigns new properties to a user. Parameters you pass modify any or all of the following: the home directory, role, and policy for the UserName and ServerId you specify.
    The response returns the ServerId and the UserName for the updated user.
    See also: AWS API Documentation
    
    
    :example: response = client.update_user(
        HomeDirectory='string',
        Policy='string',
        Role='string',
        ServerId='string',
        UserName='string'
    )
    
    
    :type HomeDirectory: string
    :param HomeDirectory: The HomeDirectory parameter specifies the landing directory (folder) for a user when they log in to the server using their client. An example would be: ``/home/username `` .

    :type Policy: string
    :param Policy: Allows you to supply a scope-down policy for your user so you can use the same AWS Identity and Access Management (IAM) role across multiple users. The policy scopes down users access to portions of your Amazon S3 bucket. Variables you can use inside this policy include ${Transfer:UserName} , ${Transfer:HomeDirectory} , and ${Transfer:HomeBucket} .

    :type Role: string
    :param Role: The IAM role that controls your user s access to your Amazon S3 bucket. The policies attached to this role will determine the level of access you want to provide your users when transferring files into and out of your Amazon S3 bucket or buckets. The IAM role should also contain a trust relationship that allows the Secure File Transfer Protocol (SFTP) server to access your resources when servicing your SFTP user s transfer requests.

    :type ServerId: string
    :param ServerId: [REQUIRED]
            A system-assigned unique identifier for an SFTP server instance that the user account is assigned to.
            

    :type UserName: string
    :param UserName: [REQUIRED]
            A unique string that identifies a user and is associated with a server as specified by the ServerId. This is the string that will be used by your user when they log in to your SFTP server.
            

    :rtype: dict
    :return: {
        'ServerId': 'string',
        'UserName': 'string'
    }
    
    
    """
    pass

