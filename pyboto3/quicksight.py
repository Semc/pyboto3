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

def create_group(GroupName=None, Description=None, AwsAccountId=None, Namespace=None):
    """
    Creates an Amazon QuickSight group.
    The permissions resource is ``arn:aws:quicksight:us-east-1:<relevant-aws-account-id> :group/default/<group-name> `` .
    The response is a group object.
    See also: AWS API Documentation
    
    
    :example: response = client.create_group(
        GroupName='string',
        Description='string',
        AwsAccountId='string',
        Namespace='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            A name for the group that you want to create.
            

    :type Description: string
    :param Description: A description for the group that you want to create.

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]
            The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
            

    :type Namespace: string
    :param Namespace: [REQUIRED]
            The namespace. Currently, you should set this to default .
            

    :rtype: dict
    :return: {
        'Group': {
            'Arn': 'string',
            'GroupName': 'string',
            'Description': 'string'
        },
        'RequestId': 'string',
        'Status': 123
    }
    
    
    """
    pass

def create_group_membership(MemberName=None, GroupName=None, AwsAccountId=None, Namespace=None):
    """
    Adds an Amazon QuickSight user to an Amazon QuickSight group.
    The permissions resource is ``arn:aws:quicksight:us-east-1:<aws-account-id> :group/default/<group-name> `` .
    The condition resource is the user name.
    The condition key is quicksight:UserName .
    The response is the group member object.
    See also: AWS API Documentation
    
    
    :example: response = client.create_group_membership(
        MemberName='string',
        GroupName='string',
        AwsAccountId='string',
        Namespace='string'
    )
    
    
    :type MemberName: string
    :param MemberName: [REQUIRED]
            The name of the user that you want to add to the group membership.
            

    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the group that you want to add the user to.
            

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]
            The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
            

    :type Namespace: string
    :param Namespace: [REQUIRED]
            The namespace. Currently, you should set this to default .
            

    :rtype: dict
    :return: {
        'GroupMember': {
            'Arn': 'string',
            'MemberName': 'string'
        },
        'RequestId': 'string',
        'Status': 123
    }
    
    
    """
    pass

def delete_group(GroupName=None, AwsAccountId=None, Namespace=None):
    """
    Removes a user group from Amazon QuickSight.
    The permissions resource is ``arn:aws:quicksight:us-east-1:<aws-account-id> :group/default/<group-name> `` .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_group(
        GroupName='string',
        AwsAccountId='string',
        Namespace='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the group that you want to delete.
            

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]
            The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
            

    :type Namespace: string
    :param Namespace: [REQUIRED]
            The namespace. Currently, you should set this to default .
            

    :rtype: dict
    :return: {
        'RequestId': 'string',
        'Status': 123
    }
    
    
    """
    pass

def delete_group_membership(MemberName=None, GroupName=None, AwsAccountId=None, Namespace=None):
    """
    Removes a user from a group so that the user is no longer a member of the group.
    The permissions resource is ``arn:aws:quicksight:us-east-1:<aws-account-id> :group/default/<group-name> `` .
    The condition resource is the user name.
    The condition key is quicksight:UserName .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_group_membership(
        MemberName='string',
        GroupName='string',
        AwsAccountId='string',
        Namespace='string'
    )
    
    
    :type MemberName: string
    :param MemberName: [REQUIRED]
            The name of the user that you want to delete from the group membership.
            

    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the group that you want to delete the user from.
            

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]
            The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
            

    :type Namespace: string
    :param Namespace: [REQUIRED]
            The namespace. Currently, you should set this to default .
            

    :rtype: dict
    :return: {
        'RequestId': 'string',
        'Status': 123
    }
    
    
    """
    pass

def delete_user(UserName=None, AwsAccountId=None, Namespace=None):
    """
    Deletes the Amazon QuickSight user that is associated with the identity of the AWS Identity and Access Management (IAM) user or role that's making the call. The IAM user isn't deleted as a result of this call.
    The permission resource is ``arn:aws:quicksight:us-east-1:<aws-account-id> :user/default/<user-name> `` .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_user(
        UserName='string',
        AwsAccountId='string',
        Namespace='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]
            The name of the user that you want to delete.
            

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]
            The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
            

    :type Namespace: string
    :param Namespace: [REQUIRED]
            The namespace. Currently, you should set this to default .
            

    :rtype: dict
    :return: {
        'RequestId': 'string',
        'Status': 123
    }
    
    
    """
    pass

def describe_group(GroupName=None, AwsAccountId=None, Namespace=None):
    """
    Returns an Amazon QuickSight group's description and Amazon Resource Name (ARN).
    The permissions resource is ``arn:aws:quicksight:us-east-1:<relevant-aws-account-id> :group/default/<group-name> `` .
    The response is the group object.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_group(
        GroupName='string',
        AwsAccountId='string',
        Namespace='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the group that you want to describe.
            

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]
            The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
            

    :type Namespace: string
    :param Namespace: [REQUIRED]
            The namespace. Currently, you should set this to default .
            

    :rtype: dict
    :return: {
        'Group': {
            'Arn': 'string',
            'GroupName': 'string',
            'Description': 'string'
        },
        'RequestId': 'string',
        'Status': 123
    }
    
    
    """
    pass

def describe_user(UserName=None, AwsAccountId=None, Namespace=None):
    """
    Returns information about a user, given the user name.
    The permission resource is ``arn:aws:quicksight:us-east-1:<aws-account-id> :user/default/<user-name> `` .
    The response is a user object that contains the user's Amazon Resource Name (ARN), AWS Identity and Access Management (IAM) role, and email address.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_user(
        UserName='string',
        AwsAccountId='string',
        Namespace='string'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]
            The name of the user that you want to describe.
            

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]
            The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
            

    :type Namespace: string
    :param Namespace: [REQUIRED]
            The namespace. Currently, you should set this to default .
            

    :rtype: dict
    :return: {
        'User': {
            'Arn': 'string',
            'UserName': 'string',
            'Email': 'string',
            'Role': 'ADMIN'|'AUTHOR'|'READER'|'RESTRICTED_AUTHOR'|'RESTRICTED_READER',
            'IdentityType': 'IAM'|'QUICKSIGHT',
            'Active': True|False
        },
        'RequestId': 'string',
        'Status': 123
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

def get_dashboard_embed_url(AwsAccountId=None, DashboardId=None, IdentityType=None, SessionLifetimeInMinutes=None, UndoRedoDisabled=None, ResetDisabled=None):
    """
    Generates a server-side embeddable URL and authorization code. Before this can work properly, first you need to configure the dashboards and user permissions. For more information, see Embedding Amazon QuickSight Dashboards .
    Currently, you can use GetDashboardEmbedURL only from the server, not from the users browser.
    Assume the role with permissions enabled for actions: quickSight:RegisterUser and quicksight:GetDashboardEmbedURL . You can use assume-role, assume-role-with-web-identity, or assume-role-with-saml.
    If the user does not exist in QuickSight, register the user:
    Get the URL for the embedded dashboard
    See also: AWS API Documentation
    
    
    :example: response = client.get_dashboard_embed_url(
        AwsAccountId='string',
        DashboardId='string',
        IdentityType='IAM'|'QUICKSIGHT',
        SessionLifetimeInMinutes=123,
        UndoRedoDisabled=True|False,
        ResetDisabled=True|False
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]
            AWS account ID that contains the dashboard you are embedding.
            

    :type DashboardId: string
    :param DashboardId: [REQUIRED]
            The ID for the dashboard, also added to IAM policy
            

    :type IdentityType: string
    :param IdentityType: [REQUIRED]
            The authentication method the user uses to sign in (IAM only).
            

    :type SessionLifetimeInMinutes: integer
    :param SessionLifetimeInMinutes: How many minutes the session is valid. The session lifetime must be between 15 and 600 minutes.

    :type UndoRedoDisabled: boolean
    :param UndoRedoDisabled: Remove the undo/redo button on embedded dashboard. The default is FALSE, which enables the undo/redo button.

    :type ResetDisabled: boolean
    :param ResetDisabled: Remove the reset button on embedded dashboard. The default is FALSE, which allows the reset button.

    :rtype: dict
    :return: {
        'EmbedUrl': 'string',
        'Status': 123,
        'RequestId': 'string'
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

def get_waiter(waiter_name=None):
    """
    Returns an object that can wait for some condition.
    
    :type waiter_name: str
    :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.

    :rtype: botocore.waiter.Waiter
    """
    pass

def list_group_memberships(GroupName=None, NextToken=None, MaxResults=None, AwsAccountId=None, Namespace=None):
    """
    Lists member users in a group.
    The permissions resource is ``arn:aws:quicksight:us-east-1:<aws-account-id> :group/default/<group-name> `` .
    The response is a list of group member objects.
    See also: AWS API Documentation
    
    
    :example: response = client.list_group_memberships(
        GroupName='string',
        NextToken='string',
        MaxResults=123,
        AwsAccountId='string',
        Namespace='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the group that you want to see a membership list of.
            

    :type NextToken: string
    :param NextToken: A pagination token that can be used in a subsequent request.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return from this request.

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]
            The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
            

    :type Namespace: string
    :param Namespace: [REQUIRED]
            The namespace. Currently, you should set this to default .
            

    :rtype: dict
    :return: {
        'GroupMemberList': [
            {
                'Arn': 'string',
                'MemberName': 'string'
            },
        ],
        'NextToken': 'string',
        'RequestId': 'string',
        'Status': 123
    }
    
    
    """
    pass

def list_groups(AwsAccountId=None, NextToken=None, MaxResults=None, Namespace=None):
    """
    Lists all user groups in Amazon QuickSight.
    The permissions resource is arn:aws:quicksight:us-east-1:*<aws-account-id>* :group/default/* .
    The response is a list of group objects.
    See also: AWS API Documentation
    
    
    :example: response = client.list_groups(
        AwsAccountId='string',
        NextToken='string',
        MaxResults=123,
        Namespace='string'
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]
            The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
            

    :type NextToken: string
    :param NextToken: A pagination token that can be used in a subsequent request.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return.

    :type Namespace: string
    :param Namespace: [REQUIRED]
            The namespace. Currently, you should set this to default .
            

    :rtype: dict
    :return: {
        'GroupList': [
            {
                'Arn': 'string',
                'GroupName': 'string',
                'Description': 'string'
            },
        ],
        'NextToken': 'string',
        'RequestId': 'string',
        'Status': 123
    }
    
    
    """
    pass

def list_user_groups(UserName=None, AwsAccountId=None, Namespace=None, NextToken=None, MaxResults=None):
    """
    Lists the Amazon QuickSight groups that an Amazon QuickSight user is a member of.
    The permission resource is ``arn:aws:quicksight:us-east-1:<aws-account-id> :user/default/<user-name> `` .
    The response is a one or more group objects.
    See also: AWS API Documentation
    
    
    :example: response = client.list_user_groups(
        UserName='string',
        AwsAccountId='string',
        Namespace='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]
            The Amazon QuickSight user name that you want to list group memberships for.
            

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]
            The AWS Account ID that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
            

    :type Namespace: string
    :param Namespace: [REQUIRED]
            The namespace. Currently, you should set this to default .
            

    :type NextToken: string
    :param NextToken: A pagination token that can be used in a subsequent request.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return from this request.

    :rtype: dict
    :return: {
        'GroupList': [
            {
                'Arn': 'string',
                'GroupName': 'string',
                'Description': 'string'
            },
        ],
        'NextToken': 'string',
        'RequestId': 'string',
        'Status': 123
    }
    
    
    """
    pass

def list_users(AwsAccountId=None, NextToken=None, MaxResults=None, Namespace=None):
    """
    Returns a list of all of the Amazon QuickSight users belonging to this account.
    The permission resource is arn:aws:quicksight:us-east-1:*<aws-account-id>* :user/default/* .
    The response is a list of user objects, containing each user's Amazon Resource Name (ARN), AWS Identity and Access Management (IAM) role, and email address.
    See also: AWS API Documentation
    
    
    :example: response = client.list_users(
        AwsAccountId='string',
        NextToken='string',
        MaxResults=123,
        Namespace='string'
    )
    
    
    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]
            The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
            

    :type NextToken: string
    :param NextToken: A pagination token that can be used in a subsequent request.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return from this request.

    :type Namespace: string
    :param Namespace: [REQUIRED]
            The namespace. Currently, you should set this to default .
            

    :rtype: dict
    :return: {
        'UserList': [
            {
                'Arn': 'string',
                'UserName': 'string',
                'Email': 'string',
                'Role': 'ADMIN'|'AUTHOR'|'READER'|'RESTRICTED_AUTHOR'|'RESTRICTED_READER',
                'IdentityType': 'IAM'|'QUICKSIGHT',
                'Active': True|False
            },
        ],
        'NextToken': 'string',
        'RequestId': 'string',
        'Status': 123
    }
    
    
    """
    pass

def register_user(IdentityType=None, Email=None, UserRole=None, IamArn=None, SessionName=None, AwsAccountId=None, Namespace=None, UserName=None):
    """
    Creates an Amazon QuickSight user, whose identity is associated with the AWS Identity and Access Management (IAM) identity or role specified in the request.
    The permission resource is ``arn:aws:quicksight:us-east-1:<aws-account-id> :user/default/<user-name> `` .
    The condition resource is the Amazon Resource Name (ARN) for the IAM user or role, and the session name.
    The condition keys are quicksight:IamArn and quicksight:SessionName .
    See also: AWS API Documentation
    
    
    :example: response = client.register_user(
        IdentityType='IAM'|'QUICKSIGHT',
        Email='string',
        UserRole='ADMIN'|'AUTHOR'|'READER'|'RESTRICTED_AUTHOR'|'RESTRICTED_READER',
        IamArn='string',
        SessionName='string',
        AwsAccountId='string',
        Namespace='string',
        UserName='string'
    )
    
    
    :type IdentityType: string
    :param IdentityType: [REQUIRED]
            Amazon QuickSight supports several ways of managing the identity of users. This parameter accepts two values:
            IAM : A user whose identity maps to an existing IAM user or role.
            QUICKSIGHT : A user whose identity is owned and managed internally by Amazon QuickSight.
            

    :type Email: string
    :param Email: [REQUIRED]
            The email address of the user that you want to register.
            

    :type UserRole: string
    :param UserRole: [REQUIRED]
            The Amazon QuickSight role of the user. The user role can be one of the following:
            READER : A user who has read-only access to dashboards.
            AUTHOR : A user who can create data sources, data sets, analyses, and dashboards.
            ADMIN : A user who is an author, who can also manage Amazon QuickSight settings.
            

    :type IamArn: string
    :param IamArn: The ARN of the IAM user or role that you are registering with Amazon QuickSight.

    :type SessionName: string
    :param SessionName: The name of the session with the assumed IAM role. By using this parameter, you can register multiple users with the same IAM role, provided that each has a different session name. For more information on assuming IAM roles, see ` assume-role https://docs.aws.amazon.com/cli/latest/reference/sts/assume-role.html`__ in the AWS CLI Reference.

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]
            The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
            

    :type Namespace: string
    :param Namespace: [REQUIRED]
            The namespace. Currently, you should set this to default .
            

    :type UserName: string
    :param UserName: The Amazon QuickSight user name that you want to create for the user you are registering.

    :rtype: dict
    :return: {
        'User': {
            'Arn': 'string',
            'UserName': 'string',
            'Email': 'string',
            'Role': 'ADMIN'|'AUTHOR'|'READER'|'RESTRICTED_AUTHOR'|'RESTRICTED_READER',
            'IdentityType': 'IAM'|'QUICKSIGHT',
            'Active': True|False
        },
        'UserInvitationUrl': 'string',
        'RequestId': 'string',
        'Status': 123
    }
    
    
    """
    pass

def update_group(GroupName=None, Description=None, AwsAccountId=None, Namespace=None):
    """
    Changes a group description.
    The permissions resource is ``arn:aws:quicksight:us-east-1:<aws-account-id> :group/default/<group-name> `` .
    The response is a group object.
    See also: AWS API Documentation
    
    
    :example: response = client.update_group(
        GroupName='string',
        Description='string',
        AwsAccountId='string',
        Namespace='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the group that you want to update.
            

    :type Description: string
    :param Description: The description for the group that you want to update.

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]
            The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
            

    :type Namespace: string
    :param Namespace: [REQUIRED]
            The namespace. Currently, you should set this to default .
            

    :rtype: dict
    :return: {
        'Group': {
            'Arn': 'string',
            'GroupName': 'string',
            'Description': 'string'
        },
        'RequestId': 'string',
        'Status': 123
    }
    
    
    """
    pass

def update_user(UserName=None, AwsAccountId=None, Namespace=None, Email=None, Role=None):
    """
    Updates an Amazon QuickSight user.
    The permission resource is ``arn:aws:quicksight:us-east-1:<aws-account-id> :user/default/<user-name> `` .
    The response is a user object that contains the user's Amazon QuickSight user name, email address, active or inactive status in Amazon QuickSight, Amazon QuickSight role, and Amazon Resource Name (ARN).
    See also: AWS API Documentation
    
    
    :example: response = client.update_user(
        UserName='string',
        AwsAccountId='string',
        Namespace='string',
        Email='string',
        Role='ADMIN'|'AUTHOR'|'READER'|'RESTRICTED_AUTHOR'|'RESTRICTED_READER'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]
            The Amazon QuickSight user name that you want to update.
            

    :type AwsAccountId: string
    :param AwsAccountId: [REQUIRED]
            The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
            

    :type Namespace: string
    :param Namespace: [REQUIRED]
            The namespace. Currently, you should set this to default .
            

    :type Email: string
    :param Email: [REQUIRED]
            The email address of the user that you want to update.
            

    :type Role: string
    :param Role: [REQUIRED]
            The Amazon QuickSight role of the user. The user role can be one of the following:
            READER : A user who has read-only access to dashboards.
            AUTHOR : A user who can create data sources, data sets, analyses, and dashboards.
            ADMIN : A user who is an author, who can also manage Amazon QuickSight settings.
            

    :rtype: dict
    :return: {
        'User': {
            'Arn': 'string',
            'UserName': 'string',
            'Email': 'string',
            'Role': 'ADMIN'|'AUTHOR'|'READER'|'RESTRICTED_AUTHOR'|'RESTRICTED_READER',
            'IdentityType': 'IAM'|'QUICKSIGHT',
            'Active': True|False
        },
        'RequestId': 'string',
        'Status': 123
    }
    
    
    """
    pass

