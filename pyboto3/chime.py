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

def batch_suspend_user(AccountId=None, UserIdList=None):
    """
    Suspends up to 50 users from a Team or EnterpriseLWA Amazon Chime account. For more information about different account types, see Managing Your Amazon Chime Accounts in the Amazon Chime Administration Guide .
    Users suspended from a Team account are dissociated from the account, but they can continue to use Amazon Chime as free users. To remove the suspension from suspended Team account users, invite them to the Team account again. You can use the  InviteUsers action to do so.
    Users suspended from an EnterpriseLWA account are immediately signed out of Amazon Chime and are no longer able to sign in. To remove the suspension from suspended EnterpriseLWA account users, use the  BatchUnsuspendUser action.
    To sign out users without suspending them, use the  LogoutUser action.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_suspend_user(
        AccountId='string',
        UserIdList=[
            'string',
        ]
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The Amazon Chime account ID.
            

    :type UserIdList: list
    :param UserIdList: [REQUIRED]
            The request containing the user IDs to suspend.
            (string) --
            

    :rtype: dict
    :return: {
        'UserErrors': [
            {
                'UserId': 'string',
                'ErrorCode': 'Unauthorized'|'Forbidden'|'NotFound'|'BadRequest'|'Conflict'|'ServiceFailure'|'ServiceUnavailable'|'Unprocessable'|'Throttled'|'PreconditionFailed',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def batch_unsuspend_user(AccountId=None, UserIdList=None):
    """
    Removes the suspension from up to 50 previously suspended users for the specified Amazon Chime EnterpriseLWA account. Only users on EnterpriseLWA accounts can be unsuspended using this action. For more information about different account types, see Managing Your Amazon Chime Accounts in the Amazon Chime Administration Guide .
    Previously suspended users who are unsuspended using this action are returned to Registered status. Users who are not previously suspended are ignored.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_unsuspend_user(
        AccountId='string',
        UserIdList=[
            'string',
        ]
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The Amazon Chime account ID.
            

    :type UserIdList: list
    :param UserIdList: [REQUIRED]
            The request containing the user IDs to unsuspend.
            (string) --
            

    :rtype: dict
    :return: {
        'UserErrors': [
            {
                'UserId': 'string',
                'ErrorCode': 'Unauthorized'|'Forbidden'|'NotFound'|'BadRequest'|'Conflict'|'ServiceFailure'|'ServiceUnavailable'|'Unprocessable'|'Throttled'|'PreconditionFailed',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def batch_update_user(AccountId=None, UpdateUserRequestItems=None):
    """
    Updates user details within the  UpdateUserRequestItem object for up to 20 users for the specified Amazon Chime account. Currently, only LicenseType updates are supported for this action.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_update_user(
        AccountId='string',
        UpdateUserRequestItems=[
            {
                'UserId': 'string',
                'LicenseType': 'Basic'|'Plus'|'Pro'|'ProTrial'
            },
        ]
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The Amazon Chime account ID.
            

    :type UpdateUserRequestItems: list
    :param UpdateUserRequestItems: [REQUIRED]
            The request containing the user IDs and details to update.
            (dict) --The user ID and user fields to update, used with the BatchUpdateUser action.
            UserId (string) -- [REQUIRED]The user ID.
            LicenseType (string) --The user license type.
            
            

    :rtype: dict
    :return: {
        'UserErrors': [
            {
                'UserId': 'string',
                'ErrorCode': 'Unauthorized'|'Forbidden'|'NotFound'|'BadRequest'|'Conflict'|'ServiceFailure'|'ServiceUnavailable'|'Unprocessable'|'Throttled'|'PreconditionFailed',
                'ErrorMessage': 'string'
            },
        ]
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

def create_account(Name=None):
    """
    Creates an Amazon Chime account under the administrator's AWS account. Only Team account types are currently supported for this action. For more information about different account types, see Managing Your Amazon Chime Accounts in the Amazon Chime Administration Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_account(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the Amazon Chime account.
            

    :rtype: dict
    :return: {
        'Account': {
            'AwsAccountId': 'string',
            'AccountId': 'string',
            'Name': 'string',
            'AccountType': 'Team'|'EnterpriseDirectory'|'EnterpriseLWA'|'EnterpriseOIDC',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'DefaultLicense': 'Basic'|'Plus'|'Pro'|'ProTrial',
            'SupportedLicenses': [
                'Basic'|'Plus'|'Pro'|'ProTrial',
            ]
        }
    }
    
    
    """
    pass

def delete_account(AccountId=None):
    """
    Deletes the specified Amazon Chime account. You must suspend all users before deleting a Team account. You can use the  BatchSuspendUser action to do so.
    For EnterpriseLWA and EnterpriseAD accounts, you must release the claimed domains for your Amazon Chime account before deletion. As soon as you release the domain, all users under that account are suspended.
    Deleted accounts appear in your Disabled accounts list for 90 days. To restore a deleted account from your Disabled accounts list, you must contact AWS Support.
    After 90 days, deleted accounts are permanently removed from your Disabled accounts list.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_account(
        AccountId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The Amazon Chime account ID.
            

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

def get_account(AccountId=None):
    """
    Retrieves details for the specified Amazon Chime account, such as account type and supported licenses.
    See also: AWS API Documentation
    
    
    :example: response = client.get_account(
        AccountId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The Amazon Chime account ID.
            

    :rtype: dict
    :return: {
        'Account': {
            'AwsAccountId': 'string',
            'AccountId': 'string',
            'Name': 'string',
            'AccountType': 'Team'|'EnterpriseDirectory'|'EnterpriseLWA'|'EnterpriseOIDC',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'DefaultLicense': 'Basic'|'Plus'|'Pro'|'ProTrial',
            'SupportedLicenses': [
                'Basic'|'Plus'|'Pro'|'ProTrial',
            ]
        }
    }
    
    
    """
    pass

def get_account_settings(AccountId=None):
    """
    Retrieves account settings for the specified Amazon Chime account ID, such as remote control and dial out settings. For more information about these settings, see Use the Policies Page in the Amazon Chime Administration Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.get_account_settings(
        AccountId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The Amazon Chime account ID.
            

    :rtype: dict
    :return: {
        'AccountSettings': {
            'DisableRemoteControl': True|False,
            'EnableDialOut': True|False
        }
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

def get_user(AccountId=None, UserId=None):
    """
    Retrieves details for the specified user ID, such as primary email address, license type, and personal meeting PIN.
    To retrieve user details with an email address instead of a user ID, use the  ListUsers action, and then filter by email address.
    See also: AWS API Documentation
    
    
    :example: response = client.get_user(
        AccountId='string',
        UserId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The Amazon Chime account ID.
            

    :type UserId: string
    :param UserId: [REQUIRED]
            The user ID.
            

    :rtype: dict
    :return: {
        'User': {
            'UserId': 'string',
            'AccountId': 'string',
            'PrimaryEmail': 'string',
            'DisplayName': 'string',
            'LicenseType': 'Basic'|'Plus'|'Pro'|'ProTrial',
            'UserRegistrationStatus': 'Unregistered'|'Registered'|'Suspended',
            'UserInvitationStatus': 'Pending'|'Accepted'|'Failed',
            'RegisteredOn': datetime(2015, 1, 1),
            'InvitedOn': datetime(2015, 1, 1),
            'PersonalPIN': 'string'
        }
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

def invite_users(AccountId=None, UserEmailList=None):
    """
    Sends email invites to as many as 50 users, inviting them to the specified Amazon Chime Team account. Only Team account types are currently supported for this action.
    See also: AWS API Documentation
    
    
    :example: response = client.invite_users(
        AccountId='string',
        UserEmailList=[
            'string',
        ]
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The Amazon Chime account ID.
            

    :type UserEmailList: list
    :param UserEmailList: [REQUIRED]
            The user email addresses to which to send the invite.
            (string) --
            

    :rtype: dict
    :return: {
        'Invites': [
            {
                'InviteId': 'string',
                'Status': 'Pending'|'Accepted'|'Failed',
                'EmailAddress': 'string',
                'EmailStatus': 'NotSent'|'Sent'|'Failed'
            },
        ]
    }
    
    
    """
    pass

def list_accounts(Name=None, UserEmail=None, NextToken=None, MaxResults=None):
    """
    Lists the Amazon Chime accounts under the administrator's AWS account. You can filter accounts by account name prefix. To find out which Amazon Chime account a user belongs to, you can filter by the user's email address, which returns one account result.
    See also: AWS API Documentation
    
    
    :example: response = client.list_accounts(
        Name='string',
        UserEmail='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Name: string
    :param Name: Amazon Chime account name prefix with which to filter results.

    :type UserEmail: string
    :param UserEmail: User email address with which to filter results.

    :type NextToken: string
    :param NextToken: The token to use to retrieve the next page of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call. Defaults to 100.

    :rtype: dict
    :return: {
        'Accounts': [
            {
                'AwsAccountId': 'string',
                'AccountId': 'string',
                'Name': 'string',
                'AccountType': 'Team'|'EnterpriseDirectory'|'EnterpriseLWA'|'EnterpriseOIDC',
                'CreatedTimestamp': datetime(2015, 1, 1),
                'DefaultLicense': 'Basic'|'Plus'|'Pro'|'ProTrial',
                'SupportedLicenses': [
                    'Basic'|'Plus'|'Pro'|'ProTrial',
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_users(AccountId=None, UserEmail=None, MaxResults=None, NextToken=None):
    """
    Lists the users that belong to the specified Amazon Chime account. You can specify an email address to list only the user that the email address belongs to.
    See also: AWS API Documentation
    
    
    :example: response = client.list_users(
        AccountId='string',
        UserEmail='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The Amazon Chime account ID.
            

    :type UserEmail: string
    :param UserEmail: Optional. The user email address used to filter results. Maximum 1.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call. Defaults to 100.

    :type NextToken: string
    :param NextToken: The token to use to retrieve the next page of results.

    :rtype: dict
    :return: {
        'Users': [
            {
                'UserId': 'string',
                'AccountId': 'string',
                'PrimaryEmail': 'string',
                'DisplayName': 'string',
                'LicenseType': 'Basic'|'Plus'|'Pro'|'ProTrial',
                'UserRegistrationStatus': 'Unregistered'|'Registered'|'Suspended',
                'UserInvitationStatus': 'Pending'|'Accepted'|'Failed',
                'RegisteredOn': datetime(2015, 1, 1),
                'InvitedOn': datetime(2015, 1, 1),
                'PersonalPIN': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def logout_user(AccountId=None, UserId=None):
    """
    Logs out the specified user from all of the devices they are currently logged into.
    See also: AWS API Documentation
    
    
    :example: response = client.logout_user(
        AccountId='string',
        UserId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The Amazon Chime account ID.
            

    :type UserId: string
    :param UserId: [REQUIRED]
            The user ID.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def reset_personal_pin(AccountId=None, UserId=None):
    """
    Resets the personal meeting PIN for the specified user on an Amazon Chime account. Returns the  User object with the updated personal meeting PIN.
    See also: AWS API Documentation
    
    
    :example: response = client.reset_personal_pin(
        AccountId='string',
        UserId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The Amazon Chime account ID.
            

    :type UserId: string
    :param UserId: [REQUIRED]
            The user ID.
            

    :rtype: dict
    :return: {
        'User': {
            'UserId': 'string',
            'AccountId': 'string',
            'PrimaryEmail': 'string',
            'DisplayName': 'string',
            'LicenseType': 'Basic'|'Plus'|'Pro'|'ProTrial',
            'UserRegistrationStatus': 'Unregistered'|'Registered'|'Suspended',
            'UserInvitationStatus': 'Pending'|'Accepted'|'Failed',
            'RegisteredOn': datetime(2015, 1, 1),
            'InvitedOn': datetime(2015, 1, 1),
            'PersonalPIN': 'string'
        }
    }
    
    
    """
    pass

def update_account(AccountId=None, Name=None):
    """
    Updates account details for the specified Amazon Chime account. Currently, only account name updates are supported for this action.
    See also: AWS API Documentation
    
    
    :example: response = client.update_account(
        AccountId='string',
        Name='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The Amazon Chime account ID.
            

    :type Name: string
    :param Name: The new name for the specified Amazon Chime account.

    :rtype: dict
    :return: {
        'Account': {
            'AwsAccountId': 'string',
            'AccountId': 'string',
            'Name': 'string',
            'AccountType': 'Team'|'EnterpriseDirectory'|'EnterpriseLWA'|'EnterpriseOIDC',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'DefaultLicense': 'Basic'|'Plus'|'Pro'|'ProTrial',
            'SupportedLicenses': [
                'Basic'|'Plus'|'Pro'|'ProTrial',
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_account_settings(AccountId=None, AccountSettings=None):
    """
    Updates the settings for the specified Amazon Chime account. You can update settings for remote control of shared screens, or for the dial-out option. For more information about these settings, see Use the Policies Page in the Amazon Chime Administration Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.update_account_settings(
        AccountId='string',
        AccountSettings={
            'DisableRemoteControl': True|False,
            'EnableDialOut': True|False
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The Amazon Chime account ID.
            

    :type AccountSettings: dict
    :param AccountSettings: [REQUIRED]
            The Amazon Chime account settings to update.
            DisableRemoteControl (boolean) --Setting that stops or starts remote control of shared screens during meetings.
            EnableDialOut (boolean) --Setting that allows meeting participants to choose the Call me at a phone number option. For more information, see Join a Meeting without the Amazon Chime App .
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_user(AccountId=None, UserId=None, LicenseType=None):
    """
    Updates user details for a specified user ID. Currently, only LicenseType updates are supported for this action.
    See also: AWS API Documentation
    
    
    :example: response = client.update_user(
        AccountId='string',
        UserId='string',
        LicenseType='Basic'|'Plus'|'Pro'|'ProTrial'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The Amazon Chime account ID.
            

    :type UserId: string
    :param UserId: [REQUIRED]
            The user ID.
            

    :type LicenseType: string
    :param LicenseType: The user license type to update. This must be a supported license type for the Amazon Chime account that the user belongs to.

    :rtype: dict
    :return: {
        'User': {
            'UserId': 'string',
            'AccountId': 'string',
            'PrimaryEmail': 'string',
            'DisplayName': 'string',
            'LicenseType': 'Basic'|'Plus'|'Pro'|'ProTrial',
            'UserRegistrationStatus': 'Unregistered'|'Registered'|'Suspended',
            'UserInvitationStatus': 'Pending'|'Accepted'|'Failed',
            'RegisteredOn': datetime(2015, 1, 1),
            'InvitedOn': datetime(2015, 1, 1),
            'PersonalPIN': 'string'
        }
    }
    
    
    """
    pass

