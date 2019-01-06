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

def delete_public_access_block(AccountId=None):
    """
    Removes the Public Access Block configuration for an Amazon Web Services account.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_public_access_block(
        AccountId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The Account ID for the Amazon Web Services account whose Public Access Block configuration you want to remove.
            

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

def get_public_access_block(AccountId=None):
    """
    Retrieves the Public Access Block configuration for an Amazon Web Services account.
    See also: AWS API Documentation
    
    
    :example: response = client.get_public_access_block(
        AccountId='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The Account ID for the Amazon Web Services account whose Public Access Block configuration you want to retrieve.
            

    :rtype: dict
    :return: {
        'PublicAccessBlockConfiguration': {
            'BlockPublicAcls': True|False,
            'IgnorePublicAcls': True|False,
            'BlockPublicPolicy': True|False,
            'RestrictPublicBuckets': True|False
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

def put_public_access_block(PublicAccessBlockConfiguration=None, AccountId=None):
    """
    Creates or modifies the Public Access Block configuration for an Amazon Web Services account.
    See also: AWS API Documentation
    
    
    :example: response = client.put_public_access_block(
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True|False,
            'IgnorePublicAcls': True|False,
            'BlockPublicPolicy': True|False,
            'RestrictPublicBuckets': True|False
        },
        AccountId='string'
    )
    
    
    :type PublicAccessBlockConfiguration: dict
    :param PublicAccessBlockConfiguration: [REQUIRED]
            The Public Access Block configuration that you want to apply to this Amazon Web Services account.
            BlockPublicAcls (boolean) --Specifies whether Amazon S3 should block public ACLs for buckets in this account. Setting this element to TRUE causes the following behavior:
            PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.
            PUT Object calls will fail if the request includes an object ACL.
            Note that enabling this setting doesn't affect existing policies or ACLs.
            IgnorePublicAcls (boolean) --Specifies whether Amazon S3 should ignore public ACLs for buckets in this account. Setting this element to TRUE causes Amazon S3 to ignore all public ACLs on buckets in this account and any objects that they contain.
            Note that enabling this setting doesn't affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set.
            BlockPublicPolicy (boolean) --Specifies whether Amazon S3 should block public bucket policies for buckets in this account. Setting this element to TRUE causes Amazon S3 to reject calls to PUT Bucket policy if the specified bucket policy allows public access.
            Note that enabling this setting doesn't affect existing bucket policies.
            RestrictPublicBuckets (boolean) --Specifies whether Amazon S3 should restrict public bucket policies for buckets in this account. If this element is set to TRUE , then only the bucket owner and AWS Services can access buckets with public policies.
            Note that enabling this setting doesn't affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked.
            

    :type AccountId: string
    :param AccountId: [REQUIRED]
            The Account ID for the Amazon Web Services account whose Public Access Block configuration you want to set.
            

    """
    pass

