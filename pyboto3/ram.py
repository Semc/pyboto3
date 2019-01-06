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

def accept_resource_share_invitation(resourceShareInvitationArn=None, clientToken=None):
    """
    Accepts an invitation to a resource share from another AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.accept_resource_share_invitation(
        resourceShareInvitationArn='string',
        clientToken='string'
    )
    
    
    :type resourceShareInvitationArn: string
    :param resourceShareInvitationArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the invitation.
            

    :type clientToken: string
    :param clientToken: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

    :rtype: dict
    :return: {
        'resourceShareInvitation': {
            'resourceShareInvitationArn': 'string',
            'resourceShareName': 'string',
            'resourceShareArn': 'string',
            'senderAccountId': 'string',
            'receiverAccountId': 'string',
            'invitationTimestamp': datetime(2015, 1, 1),
            'status': 'PENDING'|'ACCEPTED'|'REJECTED'|'EXPIRED',
            'resourceShareAssociations': [
                {
                    'resourceShareArn': 'string',
                    'associatedEntity': 'string',
                    'associationType': 'PRINCIPAL'|'RESOURCE',
                    'status': 'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
                    'statusMessage': 'string',
                    'creationTime': datetime(2015, 1, 1),
                    'lastUpdatedTime': datetime(2015, 1, 1),
                    'external': True|False
                },
            ]
        },
        'clientToken': 'string'
    }
    
    
    """
    pass

def associate_resource_share(resourceShareArn=None, resourceArns=None, principals=None, clientToken=None):
    """
    Associates the specified resource share with the specified principals and resources.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_resource_share(
        resourceShareArn='string',
        resourceArns=[
            'string',
        ],
        principals=[
            'string',
        ],
        clientToken='string'
    )
    
    
    :type resourceShareArn: string
    :param resourceShareArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource share.
            

    :type resourceArns: list
    :param resourceArns: The Amazon Resource Names (ARN) of the resources.
            (string) --
            

    :type principals: list
    :param principals: The principals.
            (string) --
            

    :type clientToken: string
    :param clientToken: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

    :rtype: dict
    :return: {
        'resourceShareAssociations': [
            {
                'resourceShareArn': 'string',
                'associatedEntity': 'string',
                'associationType': 'PRINCIPAL'|'RESOURCE',
                'status': 'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
                'statusMessage': 'string',
                'creationTime': datetime(2015, 1, 1),
                'lastUpdatedTime': datetime(2015, 1, 1),
                'external': True|False
            },
        ],
        'clientToken': 'string'
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

def create_resource_share(name=None, resourceArns=None, principals=None, tags=None, allowExternalPrincipals=None, clientToken=None):
    """
    Creates a resource share.
    See also: AWS API Documentation
    
    
    :example: response = client.create_resource_share(
        name='string',
        resourceArns=[
            'string',
        ],
        principals=[
            'string',
        ],
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        allowExternalPrincipals=True|False,
        clientToken='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the resource share.
            

    :type resourceArns: list
    :param resourceArns: The Amazon Resource Names (ARN) of the resources to associate with the resource share.
            (string) --
            

    :type principals: list
    :param principals: The principals to associate with the resource share. The possible values are IDs of AWS accounts, the ARN of an OU or organization from AWS Organizations.
            (string) --
            

    :type tags: list
    :param tags: One or more tags.
            (dict) --Information about a tag.
            key (string) --The key of the tag.
            value (string) --The value of the tag.
            
            

    :type allowExternalPrincipals: boolean
    :param allowExternalPrincipals: Indicates whether principals outside your organization can be associated with a resource share.

    :type clientToken: string
    :param clientToken: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

    :rtype: dict
    :return: {
        'resourceShare': {
            'resourceShareArn': 'string',
            'name': 'string',
            'owningAccountId': 'string',
            'allowExternalPrincipals': True|False,
            'status': 'PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED',
            'statusMessage': 'string',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'creationTime': datetime(2015, 1, 1),
            'lastUpdatedTime': datetime(2015, 1, 1)
        },
        'clientToken': 'string'
    }
    
    
    """
    pass

def delete_resource_share(resourceShareArn=None, clientToken=None):
    """
    Deletes the specified resource share.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_resource_share(
        resourceShareArn='string',
        clientToken='string'
    )
    
    
    :type resourceShareArn: string
    :param resourceShareArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource share.
            

    :type clientToken: string
    :param clientToken: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

    :rtype: dict
    :return: {
        'returnValue': True|False,
        'clientToken': 'string'
    }
    
    
    """
    pass

def disassociate_resource_share(resourceShareArn=None, resourceArns=None, principals=None, clientToken=None):
    """
    Disassociates the specified principals or resources from the specified resource share.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_resource_share(
        resourceShareArn='string',
        resourceArns=[
            'string',
        ],
        principals=[
            'string',
        ],
        clientToken='string'
    )
    
    
    :type resourceShareArn: string
    :param resourceShareArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource share.
            

    :type resourceArns: list
    :param resourceArns: The Amazon Resource Names (ARN) of the resources.
            (string) --
            

    :type principals: list
    :param principals: The principals.
            (string) --
            

    :type clientToken: string
    :param clientToken: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

    :rtype: dict
    :return: {
        'resourceShareAssociations': [
            {
                'resourceShareArn': 'string',
                'associatedEntity': 'string',
                'associationType': 'PRINCIPAL'|'RESOURCE',
                'status': 'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
                'statusMessage': 'string',
                'creationTime': datetime(2015, 1, 1),
                'lastUpdatedTime': datetime(2015, 1, 1),
                'external': True|False
            },
        ],
        'clientToken': 'string'
    }
    
    
    """
    pass

def enable_sharing_with_aws_organization():
    """
    Enables resource sharing within your organization.
    See also: AWS API Documentation
    
    
    :example: response = client.enable_sharing_with_aws_organization()
    
    
    :rtype: dict
    :return: {
        'returnValue': True|False
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

def get_resource_policies(resourceArns=None, principal=None, nextToken=None, maxResults=None):
    """
    Gets the policies for the specifies resources.
    See also: AWS API Documentation
    
    
    :example: response = client.get_resource_policies(
        resourceArns=[
            'string',
        ],
        principal='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type resourceArns: list
    :param resourceArns: [REQUIRED]
            The Amazon Resource Names (ARN) of the resources.
            (string) --
            

    :type principal: string
    :param principal: The principal.

    :type nextToken: string
    :param nextToken: The token for the next page of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.

    :rtype: dict
    :return: {
        'policies': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_resource_share_associations(associationType=None, resourceShareArns=None, resourceArn=None, principal=None, associationStatus=None, nextToken=None, maxResults=None):
    """
    Gets the associations for the specified resource share.
    See also: AWS API Documentation
    
    
    :example: response = client.get_resource_share_associations(
        associationType='PRINCIPAL'|'RESOURCE',
        resourceShareArns=[
            'string',
        ],
        resourceArn='string',
        principal='string',
        associationStatus='ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
        nextToken='string',
        maxResults=123
    )
    
    
    :type associationType: string
    :param associationType: [REQUIRED]
            The association type.
            

    :type resourceShareArns: list
    :param resourceShareArns: The Amazon Resource Names (ARN) of the resource shares.
            (string) --
            

    :type resourceArn: string
    :param resourceArn: The Amazon Resource Name (ARN) of the resource.

    :type principal: string
    :param principal: The principal.

    :type associationStatus: string
    :param associationStatus: The status of the association.

    :type nextToken: string
    :param nextToken: The token for the next page of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.

    :rtype: dict
    :return: {
        'resourceShareAssociations': [
            {
                'resourceShareArn': 'string',
                'associatedEntity': 'string',
                'associationType': 'PRINCIPAL'|'RESOURCE',
                'status': 'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
                'statusMessage': 'string',
                'creationTime': datetime(2015, 1, 1),
                'lastUpdatedTime': datetime(2015, 1, 1),
                'external': True|False
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def get_resource_share_invitations(resourceShareInvitationArns=None, resourceShareArns=None, nextToken=None, maxResults=None):
    """
    Gets the specified invitations for resource sharing.
    See also: AWS API Documentation
    
    
    :example: response = client.get_resource_share_invitations(
        resourceShareInvitationArns=[
            'string',
        ],
        resourceShareArns=[
            'string',
        ],
        nextToken='string',
        maxResults=123
    )
    
    
    :type resourceShareInvitationArns: list
    :param resourceShareInvitationArns: The Amazon Resource Names (ARN) of the invitations.
            (string) --
            

    :type resourceShareArns: list
    :param resourceShareArns: The Amazon Resource Names (ARN) of the resource shares.
            (string) --
            

    :type nextToken: string
    :param nextToken: The token for the next page of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.

    :rtype: dict
    :return: {
        'resourceShareInvitations': [
            {
                'resourceShareInvitationArn': 'string',
                'resourceShareName': 'string',
                'resourceShareArn': 'string',
                'senderAccountId': 'string',
                'receiverAccountId': 'string',
                'invitationTimestamp': datetime(2015, 1, 1),
                'status': 'PENDING'|'ACCEPTED'|'REJECTED'|'EXPIRED',
                'resourceShareAssociations': [
                    {
                        'resourceShareArn': 'string',
                        'associatedEntity': 'string',
                        'associationType': 'PRINCIPAL'|'RESOURCE',
                        'status': 'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
                        'statusMessage': 'string',
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdatedTime': datetime(2015, 1, 1),
                        'external': True|False
                    },
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def get_resource_shares(resourceShareArns=None, resourceShareStatus=None, resourceOwner=None, name=None, tagFilters=None, nextToken=None, maxResults=None):
    """
    Gets the specified resource shares or all of your resource shares.
    See also: AWS API Documentation
    
    
    :example: response = client.get_resource_shares(
        resourceShareArns=[
            'string',
        ],
        resourceShareStatus='PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED',
        resourceOwner='SELF'|'OTHER-ACCOUNTS',
        name='string',
        tagFilters=[
            {
                'tagKey': 'string',
                'tagValues': [
                    'string',
                ]
            },
        ],
        nextToken='string',
        maxResults=123
    )
    
    
    :type resourceShareArns: list
    :param resourceShareArns: The Amazon Resource Names (ARN) of the resource shares.
            (string) --
            

    :type resourceShareStatus: string
    :param resourceShareStatus: The status of the resource share.

    :type resourceOwner: string
    :param resourceOwner: [REQUIRED]
            The type of owner.
            

    :type name: string
    :param name: The name of the resource share.

    :type tagFilters: list
    :param tagFilters: One or more tag filters.
            (dict) --Used to filter information based on tags.
            tagKey (string) --The tag key.
            tagValues (list) --The tag values.
            (string) --
            
            

    :type nextToken: string
    :param nextToken: The token for the next page of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.

    :rtype: dict
    :return: {
        'resourceShares': [
            {
                'resourceShareArn': 'string',
                'name': 'string',
                'owningAccountId': 'string',
                'allowExternalPrincipals': True|False,
                'status': 'PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED',
                'statusMessage': 'string',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'creationTime': datetime(2015, 1, 1),
                'lastUpdatedTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
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

def list_principals(resourceOwner=None, resourceArn=None, principals=None, resourceType=None, resourceShareArns=None, nextToken=None, maxResults=None):
    """
    Lists the principals with access to the specified resource.
    See also: AWS API Documentation
    
    
    :example: response = client.list_principals(
        resourceOwner='SELF'|'OTHER-ACCOUNTS',
        resourceArn='string',
        principals=[
            'string',
        ],
        resourceType='string',
        resourceShareArns=[
            'string',
        ],
        nextToken='string',
        maxResults=123
    )
    
    
    :type resourceOwner: string
    :param resourceOwner: [REQUIRED]
            The type of owner.
            

    :type resourceArn: string
    :param resourceArn: The Amazon Resource Name (ARN) of the resource.

    :type principals: list
    :param principals: The principals.
            (string) --
            

    :type resourceType: string
    :param resourceType: The resource type.

    :type resourceShareArns: list
    :param resourceShareArns: The Amazon Resource Names (ARN) of the resource shares.
            (string) --
            

    :type nextToken: string
    :param nextToken: The token for the next page of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.

    :rtype: dict
    :return: {
        'principals': [
            {
                'id': 'string',
                'resourceShareArn': 'string',
                'creationTime': datetime(2015, 1, 1),
                'lastUpdatedTime': datetime(2015, 1, 1),
                'external': True|False
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_resources(resourceOwner=None, principal=None, resourceType=None, resourceArns=None, resourceShareArns=None, nextToken=None, maxResults=None):
    """
    Lists the resources that the specified principal can access.
    See also: AWS API Documentation
    
    
    :example: response = client.list_resources(
        resourceOwner='SELF'|'OTHER-ACCOUNTS',
        principal='string',
        resourceType='string',
        resourceArns=[
            'string',
        ],
        resourceShareArns=[
            'string',
        ],
        nextToken='string',
        maxResults=123
    )
    
    
    :type resourceOwner: string
    :param resourceOwner: [REQUIRED]
            The type of owner.
            

    :type principal: string
    :param principal: The principal.

    :type resourceType: string
    :param resourceType: The resource type.

    :type resourceArns: list
    :param resourceArns: The Amazon Resource Names (ARN) of the resources.
            (string) --
            

    :type resourceShareArns: list
    :param resourceShareArns: The Amazon Resource Names (ARN) of the resource shares.
            (string) --
            

    :type nextToken: string
    :param nextToken: The token for the next page of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.

    :rtype: dict
    :return: {
        'resources': [
            {
                'arn': 'string',
                'type': 'string',
                'resourceShareArn': 'string',
                'status': 'AVAILABLE'|'ZONAL_RESOURCE_INACCESSIBLE'|'LIMIT_EXCEEDED'|'UNAVAILABLE',
                'statusMessage': 'string',
                'creationTime': datetime(2015, 1, 1),
                'lastUpdatedTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def reject_resource_share_invitation(resourceShareInvitationArn=None, clientToken=None):
    """
    Rejects an invitation to a resource share from another AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.reject_resource_share_invitation(
        resourceShareInvitationArn='string',
        clientToken='string'
    )
    
    
    :type resourceShareInvitationArn: string
    :param resourceShareInvitationArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the invitation.
            

    :type clientToken: string
    :param clientToken: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

    :rtype: dict
    :return: {
        'resourceShareInvitation': {
            'resourceShareInvitationArn': 'string',
            'resourceShareName': 'string',
            'resourceShareArn': 'string',
            'senderAccountId': 'string',
            'receiverAccountId': 'string',
            'invitationTimestamp': datetime(2015, 1, 1),
            'status': 'PENDING'|'ACCEPTED'|'REJECTED'|'EXPIRED',
            'resourceShareAssociations': [
                {
                    'resourceShareArn': 'string',
                    'associatedEntity': 'string',
                    'associationType': 'PRINCIPAL'|'RESOURCE',
                    'status': 'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
                    'statusMessage': 'string',
                    'creationTime': datetime(2015, 1, 1),
                    'lastUpdatedTime': datetime(2015, 1, 1),
                    'external': True|False
                },
            ]
        },
        'clientToken': 'string'
    }
    
    
    """
    pass

def tag_resource(resourceShareArn=None, tags=None):
    """
    Adds the specified tags to the specified resource share.
    See also: AWS API Documentation
    
    
    :example: response = client.tag_resource(
        resourceShareArn='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type resourceShareArn: string
    :param resourceShareArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource share.
            

    :type tags: list
    :param tags: [REQUIRED]
            One or more tags.
            (dict) --Information about a tag.
            key (string) --The key of the tag.
            value (string) --The value of the tag.
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(resourceShareArn=None, tagKeys=None):
    """
    Removes the specified tags from the specified resource share.
    See also: AWS API Documentation
    
    
    :example: response = client.untag_resource(
        resourceShareArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceShareArn: string
    :param resourceShareArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource share.
            

    :type tagKeys: list
    :param tagKeys: [REQUIRED]
            The tag keys of the tags to remove.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_resource_share(resourceShareArn=None, name=None, allowExternalPrincipals=None, clientToken=None):
    """
    Updates the specified resource share.
    See also: AWS API Documentation
    
    
    :example: response = client.update_resource_share(
        resourceShareArn='string',
        name='string',
        allowExternalPrincipals=True|False,
        clientToken='string'
    )
    
    
    :type resourceShareArn: string
    :param resourceShareArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource share.
            

    :type name: string
    :param name: The name of the resource share.

    :type allowExternalPrincipals: boolean
    :param allowExternalPrincipals: Indicates whether principals outside your organization can be associated with a resource share.

    :type clientToken: string
    :param clientToken: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

    :rtype: dict
    :return: {
        'resourceShare': {
            'resourceShareArn': 'string',
            'name': 'string',
            'owningAccountId': 'string',
            'allowExternalPrincipals': True|False,
            'status': 'PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED',
            'statusMessage': 'string',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'creationTime': datetime(2015, 1, 1),
            'lastUpdatedTime': datetime(2015, 1, 1)
        },
        'clientToken': 'string'
    }
    
    
    """
    pass

