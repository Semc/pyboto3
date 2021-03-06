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

def associate_resolver_endpoint_ip_address(ResolverEndpointId=None, IpAddress=None):
    """
    Adds IP addresses to an inbound or an outbound resolver endpoint. If you want to adding more than one IP address, submit one AssociateResolverEndpointIpAddress request for each IP address.
    To remove an IP address from an endpoint, see  DisassociateResolverEndpointIpAddress .
    See also: AWS API Documentation
    
    
    :example: response = client.associate_resolver_endpoint_ip_address(
        ResolverEndpointId='string',
        IpAddress={
            'IpId': 'string',
            'SubnetId': 'string',
            'Ip': 'string'
        }
    )
    
    
    :type ResolverEndpointId: string
    :param ResolverEndpointId: [REQUIRED]
            The ID of the resolver endpoint that you want to associate IP addresses with.
            

    :type IpAddress: dict
    :param IpAddress: [REQUIRED]
            Either the IPv4 address that you want to add to a resolver endpoint or a subnet ID. If you specify a subnet ID, Resolver chooses an IP address for you from the available IPs in the specified subnet.
            IpId (string) --
            Only when removing an IP address from a resolver endpoint : The ID of the IP address that you want to remove. To get this ID, use GetResolverEndpoint .
            SubnetId (string) --The ID of the subnet that includes the IP address that you want to update. To get this ID, use GetResolverEndpoint .
            Ip (string) --The new IP address.
            

    :rtype: dict
    :return: {
        'ResolverEndpoint': {
            'Id': 'string',
            'CreatorRequestId': 'string',
            'Arn': 'string',
            'Name': 'string',
            'SecurityGroupIds': [
                'string',
            ],
            'Direction': 'INBOUND'|'OUTBOUND',
            'IpAddressCount': 123,
            'HostVPCId': 'string',
            'Status': 'CREATING'|'OPERATIONAL'|'UPDATING'|'AUTO_RECOVERING'|'ACTION_NEEDED'|'DELETING',
            'StatusMessage': 'string',
            'CreationTime': 'string',
            'ModificationTime': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def associate_resolver_rule(ResolverRuleId=None, Name=None, VPCId=None):
    """
    Associates a resolver rule with a VPC. When you associate a rule with a VPC, Resolver forwards all DNS queries for the domain name that is specified in the rule and that originate in the VPC. The queries are forwarded to the IP addresses for the DNS resolvers that are specified in the rule. For more information about rules, see  CreateResolverRule .
    See also: AWS API Documentation
    
    
    :example: response = client.associate_resolver_rule(
        ResolverRuleId='string',
        Name='string',
        VPCId='string'
    )
    
    
    :type ResolverRuleId: string
    :param ResolverRuleId: [REQUIRED]
            The ID of the resolver rule that you want to associate with the VPC. To list the existing resolver rules, use ListResolverRules .
            

    :type Name: string
    :param Name: A name for the association that you're creating between a resolver rule and a VPC.

    :type VPCId: string
    :param VPCId: [REQUIRED]
            The ID of the VPC that you want to associate the resolver rule with.
            

    :rtype: dict
    :return: {
        'ResolverRuleAssociation': {
            'Id': 'string',
            'ResolverRuleId': 'string',
            'Name': 'string',
            'VPCId': 'string',
            'Status': 'CREATING'|'COMPLETE'|'DELETING'|'FAILED'|'OVERRIDDEN',
            'StatusMessage': 'string'
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

def create_resolver_endpoint(CreatorRequestId=None, Name=None, SecurityGroupIds=None, Direction=None, IpAddresses=None, Tags=None):
    """
    Creates a resolver endpoint. There are two types of resolver endpoints, inbound and outbound:
    See also: AWS API Documentation
    
    
    :example: response = client.create_resolver_endpoint(
        CreatorRequestId='string',
        Name='string',
        SecurityGroupIds=[
            'string',
        ],
        Direction='INBOUND'|'OUTBOUND',
        IpAddresses=[
            {
                'SubnetId': 'string',
                'Ip': 'string'
            },
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type CreatorRequestId: string
    :param CreatorRequestId: [REQUIRED]
            A unique string that identifies the request and that allows failed requests to be retried without the risk of executing the operation twice. CreatorRequestId can be any unique string, for example, a date/time stamp.
            

    :type Name: string
    :param Name: A friendly name that lets you easily find a configuration in the Resolver dashboard in the Route 53 console.

    :type SecurityGroupIds: list
    :param SecurityGroupIds: [REQUIRED]
            The ID of one or more security groups that you want to use to control access to this VPC. The security group that you specify must include one or more inbound rules (for inbound resolver endpoints) or outbound rules (for outbound resolver endpoints).
            (string) --
            

    :type Direction: string
    :param Direction: [REQUIRED]
            Specify the applicable value:
            INBOUND : Resolver forwards DNS queries to the DNS service for a VPC from your network or another VPC
            OUTBOUND : Resolver forwards DNS queries from the DNS service for a VPC to your network or another VPC
            

    :type IpAddresses: list
    :param IpAddresses: [REQUIRED]
            The subnets and IP addresses in your VPC that you want DNS queries to pass through on the way from your VPCs to your network (for outbound endpoints) or on the way from your network to your VPCs (for inbound resolver endpoints).
            (dict) --In an CreateResolverEndpoint request, a subnet and IP address that you want to use for DNS queries.
            SubnetId (string) -- [REQUIRED]The subnet that contains the IP address.
            Ip (string) --The IP address that you want to use for DNS queries.
            
            

    :type Tags: list
    :param Tags: A list of the tag keys and values that you want to associate with the endpoint.
            (dict) --One tag that you want to add to the specified resource. A tag consists of a Key (a name for the tag) and a Value .
            Key (string) --The name for the tag. For example, if you want to associate Resolver resources with the account IDs of your customers for billing purposes, the value of Key might be account-id .
            Value (string) --The value for the tag. For example, if Key is account-id , then Value might be the ID of the customer account that you're creating the resource for.
            
            

    :rtype: dict
    :return: {
        'ResolverEndpoint': {
            'Id': 'string',
            'CreatorRequestId': 'string',
            'Arn': 'string',
            'Name': 'string',
            'SecurityGroupIds': [
                'string',
            ],
            'Direction': 'INBOUND'|'OUTBOUND',
            'IpAddressCount': 123,
            'HostVPCId': 'string',
            'Status': 'CREATING'|'OPERATIONAL'|'UPDATING'|'AUTO_RECOVERING'|'ACTION_NEEDED'|'DELETING',
            'StatusMessage': 'string',
            'CreationTime': 'string',
            'ModificationTime': 'string'
        }
    }
    
    
    :returns: 
    CreatorRequestId (string) -- [REQUIRED]
    A unique string that identifies the request and that allows failed requests to be retried without the risk of executing the operation twice. CreatorRequestId can be any unique string, for example, a date/time stamp.
    
    Name (string) -- A friendly name that lets you easily find a configuration in the Resolver dashboard in the Route 53 console.
    SecurityGroupIds (list) -- [REQUIRED]
    The ID of one or more security groups that you want to use to control access to this VPC. The security group that you specify must include one or more inbound rules (for inbound resolver endpoints) or outbound rules (for outbound resolver endpoints).
    
    (string) --
    
    
    Direction (string) -- [REQUIRED]
    Specify the applicable value:
    
    INBOUND : Resolver forwards DNS queries to the DNS service for a VPC from your network or another VPC
    OUTBOUND : Resolver forwards DNS queries from the DNS service for a VPC to your network or another VPC
    
    
    IpAddresses (list) -- [REQUIRED]
    The subnets and IP addresses in your VPC that you want DNS queries to pass through on the way from your VPCs to your network (for outbound endpoints) or on the way from your network to your VPCs (for inbound resolver endpoints).
    
    (dict) --In an  CreateResolverEndpoint request, a subnet and IP address that you want to use for DNS queries.
    
    SubnetId (string) -- [REQUIRED]The subnet that contains the IP address.
    
    Ip (string) --The IP address that you want to use for DNS queries.
    
    
    
    
    
    Tags (list) -- A list of the tag keys and values that you want to associate with the endpoint.
    
    (dict) --One tag that you want to add to the specified resource. A tag consists of a Key (a name for the tag) and a Value .
    
    Key (string) --The name for the tag. For example, if you want to associate Resolver resources with the account IDs of your customers for billing purposes, the value of Key might be account-id .
    
    Value (string) --The value for the tag. For example, if Key is account-id , then Value might be the ID of the customer account that you're creating the resource for.
    
    
    
    
    
    
    """
    pass

def create_resolver_rule(CreatorRequestId=None, Name=None, RuleType=None, DomainName=None, TargetIps=None, ResolverEndpointId=None, Tags=None):
    """
    For DNS queries that originate in your VPCs, specifies which resolver endpoint the queries pass through, one domain name that you want to forward to your network, and the IP addresses of the DNS resolvers in your network.
    See also: AWS API Documentation
    
    
    :example: response = client.create_resolver_rule(
        CreatorRequestId='string',
        Name='string',
        RuleType='FORWARD'|'SYSTEM'|'RECURSIVE',
        DomainName='string',
        TargetIps=[
            {
                'Ip': 'string',
                'Port': 123
            },
        ],
        ResolverEndpointId='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type CreatorRequestId: string
    :param CreatorRequestId: [REQUIRED]
            A unique string that identifies the request and that allows failed requests to be retried without the risk of executing the operation twice. CreatorRequestId can be any unique string, for example, a date/time stamp.
            

    :type Name: string
    :param Name: A friendly name that lets you easily find a rule in the Resolver dashboard in the Route 53 console.

    :type RuleType: string
    :param RuleType: [REQUIRED]
            Specify FORWARD . Other resolver rule types aren't supported.
            

    :type DomainName: string
    :param DomainName: [REQUIRED]
            DNS queries for this domain name are forwarded to the IP addresses that you specify in TargetIps . If a query matches multiple resolver rules (example.com and www.example.com), outbound DNS queries are routed using the resolver rule that contains the most specific domain name (www.example.com).
            

    :type TargetIps: list
    :param TargetIps: The IPs that you want Resolver to forward DNS queries to. You can specify only IPv4 addresses. Separate IP addresses with a comma.
            (dict) --In a CreateResolverRule request, an array of the IPs that you want to forward DNS queries to.
            Ip (string) -- [REQUIRED]One IP address that you want to forward DNS queries to. You can specify only IPv4 addresses.
            Port (integer) --The port at Ip that you want to forward DNS queries to.
            
            

    :type ResolverEndpointId: string
    :param ResolverEndpointId: The ID of the outbound resolver endpoint that you want to use to route DNS queries to the IP addresses that you specify in TargetIps .

    :type Tags: list
    :param Tags: A list of the tag keys and values that you want to associate with the endpoint.
            (dict) --One tag that you want to add to the specified resource. A tag consists of a Key (a name for the tag) and a Value .
            Key (string) --The name for the tag. For example, if you want to associate Resolver resources with the account IDs of your customers for billing purposes, the value of Key might be account-id .
            Value (string) --The value for the tag. For example, if Key is account-id , then Value might be the ID of the customer account that you're creating the resource for.
            
            

    :rtype: dict
    :return: {
        'ResolverRule': {
            'Id': 'string',
            'CreatorRequestId': 'string',
            'Arn': 'string',
            'DomainName': 'string',
            'Status': 'COMPLETE'|'DELETING'|'UPDATING'|'FAILED',
            'StatusMessage': 'string',
            'RuleType': 'FORWARD'|'SYSTEM'|'RECURSIVE',
            'Name': 'string',
            'TargetIps': [
                {
                    'Ip': 'string',
                    'Port': 123
                },
            ],
            'ResolverEndpointId': 'string',
            'OwnerId': 'string',
            'ShareStatus': 'NOT_SHARED'|'SHARED_WITH_ME'|'SHARED_BY_ME'
        }
    }
    
    
    """
    pass

def delete_resolver_endpoint(ResolverEndpointId=None):
    """
    Deletes a resolver endpoint. The effect of deleting a resolver endpoint depends on whether it's an inbound or an outbound resolver endpoint:
    See also: AWS API Documentation
    
    
    :example: response = client.delete_resolver_endpoint(
        ResolverEndpointId='string'
    )
    
    
    :type ResolverEndpointId: string
    :param ResolverEndpointId: [REQUIRED]
            The ID of the resolver endpoint that you want to delete.
            

    :rtype: dict
    :return: {
        'ResolverEndpoint': {
            'Id': 'string',
            'CreatorRequestId': 'string',
            'Arn': 'string',
            'Name': 'string',
            'SecurityGroupIds': [
                'string',
            ],
            'Direction': 'INBOUND'|'OUTBOUND',
            'IpAddressCount': 123,
            'HostVPCId': 'string',
            'Status': 'CREATING'|'OPERATIONAL'|'UPDATING'|'AUTO_RECOVERING'|'ACTION_NEEDED'|'DELETING',
            'StatusMessage': 'string',
            'CreationTime': 'string',
            'ModificationTime': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_resolver_rule(ResolverRuleId=None):
    """
    Deletes a resolver rule. Before you can delete a resolver rule, you must disassociate it from all the VPCs that you associated the resolver rule with. For more infomation, see  DisassociateResolverRule .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_resolver_rule(
        ResolverRuleId='string'
    )
    
    
    :type ResolverRuleId: string
    :param ResolverRuleId: [REQUIRED]
            The ID of the resolver rule that you want to delete.
            

    :rtype: dict
    :return: {
        'ResolverRule': {
            'Id': 'string',
            'CreatorRequestId': 'string',
            'Arn': 'string',
            'DomainName': 'string',
            'Status': 'COMPLETE'|'DELETING'|'UPDATING'|'FAILED',
            'StatusMessage': 'string',
            'RuleType': 'FORWARD'|'SYSTEM'|'RECURSIVE',
            'Name': 'string',
            'TargetIps': [
                {
                    'Ip': 'string',
                    'Port': 123
                },
            ],
            'ResolverEndpointId': 'string',
            'OwnerId': 'string',
            'ShareStatus': 'NOT_SHARED'|'SHARED_WITH_ME'|'SHARED_BY_ME'
        }
    }
    
    
    """
    pass

def disassociate_resolver_endpoint_ip_address(ResolverEndpointId=None, IpAddress=None):
    """
    Removes IP addresses from an inbound or an outbound resolver endpoint. If you want to remove more than one IP address, submit one DisassociateResolverEndpointIpAddress request for each IP address.
    To add an IP address to an endpoint, see  AssociateResolverEndpointIpAddress .
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_resolver_endpoint_ip_address(
        ResolverEndpointId='string',
        IpAddress={
            'IpId': 'string',
            'SubnetId': 'string',
            'Ip': 'string'
        }
    )
    
    
    :type ResolverEndpointId: string
    :param ResolverEndpointId: [REQUIRED]
            The ID of the resolver endpoint that you want to disassociate an IP address from.
            

    :type IpAddress: dict
    :param IpAddress: [REQUIRED]
            The IPv4 address that you want to remove from a resolver endpoint.
            IpId (string) --
            Only when removing an IP address from a resolver endpoint : The ID of the IP address that you want to remove. To get this ID, use GetResolverEndpoint .
            SubnetId (string) --The ID of the subnet that includes the IP address that you want to update. To get this ID, use GetResolverEndpoint .
            Ip (string) --The new IP address.
            

    :rtype: dict
    :return: {
        'ResolverEndpoint': {
            'Id': 'string',
            'CreatorRequestId': 'string',
            'Arn': 'string',
            'Name': 'string',
            'SecurityGroupIds': [
                'string',
            ],
            'Direction': 'INBOUND'|'OUTBOUND',
            'IpAddressCount': 123,
            'HostVPCId': 'string',
            'Status': 'CREATING'|'OPERATIONAL'|'UPDATING'|'AUTO_RECOVERING'|'ACTION_NEEDED'|'DELETING',
            'StatusMessage': 'string',
            'CreationTime': 'string',
            'ModificationTime': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def disassociate_resolver_rule(VPCId=None, ResolverRuleId=None):
    """
    Removes the association between a specified resolver rule and a specified VPC.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_resolver_rule(
        VPCId='string',
        ResolverRuleId='string'
    )
    
    
    :type VPCId: string
    :param VPCId: [REQUIRED]
            The ID of the VPC that you want to disassociate the resolver rule from.
            

    :type ResolverRuleId: string
    :param ResolverRuleId: [REQUIRED]
            The ID of the resolver rule that you want to disassociate from the specified VPC.
            

    :rtype: dict
    :return: {
        'ResolverRuleAssociation': {
            'Id': 'string',
            'ResolverRuleId': 'string',
            'Name': 'string',
            'VPCId': 'string',
            'Status': 'CREATING'|'COMPLETE'|'DELETING'|'FAILED'|'OVERRIDDEN',
            'StatusMessage': 'string'
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

def get_resolver_endpoint(ResolverEndpointId=None):
    """
    Gets information about a specified resolver endpoint, such as whether it's an inbound or an outbound resolver endpoint, and the current status of the endpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.get_resolver_endpoint(
        ResolverEndpointId='string'
    )
    
    
    :type ResolverEndpointId: string
    :param ResolverEndpointId: [REQUIRED]
            The ID of the resolver endpoint that you want to get information about.
            

    :rtype: dict
    :return: {
        'ResolverEndpoint': {
            'Id': 'string',
            'CreatorRequestId': 'string',
            'Arn': 'string',
            'Name': 'string',
            'SecurityGroupIds': [
                'string',
            ],
            'Direction': 'INBOUND'|'OUTBOUND',
            'IpAddressCount': 123,
            'HostVPCId': 'string',
            'Status': 'CREATING'|'OPERATIONAL'|'UPDATING'|'AUTO_RECOVERING'|'ACTION_NEEDED'|'DELETING',
            'StatusMessage': 'string',
            'CreationTime': 'string',
            'ModificationTime': 'string'
        }
    }
    
    
    :returns: 
    INBOUND : allows DNS queries to your VPC from your network or another VPC
    OUTBOUND : allows DNS queries from your VPC to your network or another VPC
    
    """
    pass

def get_resolver_rule(ResolverRuleId=None):
    """
    Gets information about a specified resolver rule, such as the domain name that the rule forwards DNS queries for and the ID of the outbound resolver endpoint that the rule is associated with.
    See also: AWS API Documentation
    
    
    :example: response = client.get_resolver_rule(
        ResolverRuleId='string'
    )
    
    
    :type ResolverRuleId: string
    :param ResolverRuleId: [REQUIRED]
            The ID of the resolver rule that you want to get information about.
            

    :rtype: dict
    :return: {
        'ResolverRule': {
            'Id': 'string',
            'CreatorRequestId': 'string',
            'Arn': 'string',
            'DomainName': 'string',
            'Status': 'COMPLETE'|'DELETING'|'UPDATING'|'FAILED',
            'StatusMessage': 'string',
            'RuleType': 'FORWARD'|'SYSTEM'|'RECURSIVE',
            'Name': 'string',
            'TargetIps': [
                {
                    'Ip': 'string',
                    'Port': 123
                },
            ],
            'ResolverEndpointId': 'string',
            'OwnerId': 'string',
            'ShareStatus': 'NOT_SHARED'|'SHARED_WITH_ME'|'SHARED_BY_ME'
        }
    }
    
    
    """
    pass

def get_resolver_rule_association(ResolverRuleAssociationId=None):
    """
    Gets information about an association between a specified resolver rule and a VPC. You associate a resolver rule and a VPC using  AssociateResolverRule .
    See also: AWS API Documentation
    
    
    :example: response = client.get_resolver_rule_association(
        ResolverRuleAssociationId='string'
    )
    
    
    :type ResolverRuleAssociationId: string
    :param ResolverRuleAssociationId: [REQUIRED]
            The ID of the resolver rule association that you want to get information about.
            

    :rtype: dict
    :return: {
        'ResolverRuleAssociation': {
            'Id': 'string',
            'ResolverRuleId': 'string',
            'Name': 'string',
            'VPCId': 'string',
            'Status': 'CREATING'|'COMPLETE'|'DELETING'|'FAILED'|'OVERRIDDEN',
            'StatusMessage': 'string'
        }
    }
    
    
    """
    pass

def get_resolver_rule_policy(Arn=None):
    """
    Gets information about a resolver rule policy. A resolver rule policy specifies the Resolver operations and resources that you want to allow another AWS account to be able to use.
    See also: AWS API Documentation
    
    
    :example: response = client.get_resolver_rule_policy(
        Arn='string'
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]
            The ID of the resolver rule policy that you want to get information about.
            

    :rtype: dict
    :return: {
        'ResolverRulePolicy': 'string'
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

def list_resolver_endpoint_ip_addresses(ResolverEndpointId=None, MaxResults=None, NextToken=None):
    """
    Gets the IP addresses for a specified resolver endpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.list_resolver_endpoint_ip_addresses(
        ResolverEndpointId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ResolverEndpointId: string
    :param ResolverEndpointId: [REQUIRED]
            The ID of the resolver endpoint that you want to get IP addresses for.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of IP addresses that you want to return in the response to a ListResolverEndpointIpAddresses request. If you don't specify a value for MaxResults , Resolver returns up to 100 IP addresses.

    :type NextToken: string
    :param NextToken: For the first ListResolverEndpointIpAddresses request, omit this value.
            If the specified resolver endpoint has more than MaxResults IP addresses, you can submit another ListResolverEndpointIpAddresses request to get the next group of IP addresses. In the next request, specify the value of NextToken from the previous response.
            

    :rtype: dict
    :return: {
        'NextToken': 'string',
        'MaxResults': 123,
        'IpAddresses': [
            {
                'IpId': 'string',
                'SubnetId': 'string',
                'Ip': 'string',
                'Status': 'CREATING'|'FAILED_CREATION'|'ATTACHING'|'ATTACHED'|'REMAP_DETACHING'|'REMAP_ATTACHING'|'DETACHING'|'FAILED_RESOURCE_GONE'|'DELETING'|'DELETE_FAILED_FAS_EXPIRED',
                'StatusMessage': 'string',
                'CreationTime': 'string',
                'ModificationTime': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_resolver_endpoints(MaxResults=None, NextToken=None, Filters=None):
    """
    Lists all the resolver endpoints that were created using the current AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_resolver_endpoints(
        MaxResults=123,
        NextToken='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of resolver endpoints that you want to return in the response to a ListResolverEndpoints request. If you don't specify a value for MaxResults , Resolver returns up to 100 resolver endpoints.

    :type NextToken: string
    :param NextToken: For the first ListResolverEndpoints request, omit this value.
            If you have more than MaxResults resolver endpoints, you can submit another ListResolverEndpoints request to get the next group of resolver endpoints. In the next request, specify the value of NextToken from the previous response.
            

    :type Filters: list
    :param Filters: An optional specification to return a subset of resolver endpoints, such as all inbound resolver endpoints.
            Note
            If you submit a second or subsequent ListResolverEndpoints request and specify the NextToken parameter, you must use the same values for Filters , if any, as in the previous request.
            (dict) --For List operations, an optional specification to return a subset of objects, such as resolver endpoints or resolver rules.
            Name (string) --When you're using a List operation and you want the operation to return a subset of objects, such as resolver endpoints or resolver rules, the name of the parameter that you want to use to filter objects. For example, to list only inbound resolver endpoints, specify Direction for the value of Name .
            Values (list) --When you're using a List operation and you want the operation to return a subset of objects, such as resolver endpoints or resolver rules, the value of the parameter that you want to use to filter objects. For example, to list only inbound resolver endpoints, specify INBOUND for the value of Values .
            (string) --
            
            

    :rtype: dict
    :return: {
        'NextToken': 'string',
        'MaxResults': 123,
        'ResolverEndpoints': [
            {
                'Id': 'string',
                'CreatorRequestId': 'string',
                'Arn': 'string',
                'Name': 'string',
                'SecurityGroupIds': [
                    'string',
                ],
                'Direction': 'INBOUND'|'OUTBOUND',
                'IpAddressCount': 123,
                'HostVPCId': 'string',
                'Status': 'CREATING'|'OPERATIONAL'|'UPDATING'|'AUTO_RECOVERING'|'ACTION_NEEDED'|'DELETING',
                'StatusMessage': 'string',
                'CreationTime': 'string',
                'ModificationTime': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_resolver_rule_associations(MaxResults=None, NextToken=None, Filters=None):
    """
    Lists the associations that were created between resolver rules and VPCs using the current AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_resolver_rule_associations(
        MaxResults=123,
        NextToken='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of rule associations that you want to return in the response to a ListResolverRuleAssociations request. If you don't specify a value for MaxResults , Resolver returns up to 100 rule associations.

    :type NextToken: string
    :param NextToken: For the first ListResolverRuleAssociation request, omit this value.
            If you have more than MaxResults rule associations, you can submit another ListResolverRuleAssociation request to get the next group of rule associations. In the next request, specify the value of NextToken from the previous response.
            

    :type Filters: list
    :param Filters: An optional specification to return a subset of resolver rules, such as resolver rules that are associated with the same VPC ID.
            Note
            If you submit a second or subsequent ListResolverRuleAssociations request and specify the NextToken parameter, you must use the same values for Filters , if any, as in the previous request.
            (dict) --For List operations, an optional specification to return a subset of objects, such as resolver endpoints or resolver rules.
            Name (string) --When you're using a List operation and you want the operation to return a subset of objects, such as resolver endpoints or resolver rules, the name of the parameter that you want to use to filter objects. For example, to list only inbound resolver endpoints, specify Direction for the value of Name .
            Values (list) --When you're using a List operation and you want the operation to return a subset of objects, such as resolver endpoints or resolver rules, the value of the parameter that you want to use to filter objects. For example, to list only inbound resolver endpoints, specify INBOUND for the value of Values .
            (string) --
            
            

    :rtype: dict
    :return: {
        'NextToken': 'string',
        'MaxResults': 123,
        'ResolverRuleAssociations': [
            {
                'Id': 'string',
                'ResolverRuleId': 'string',
                'Name': 'string',
                'VPCId': 'string',
                'Status': 'CREATING'|'COMPLETE'|'DELETING'|'FAILED'|'OVERRIDDEN',
                'StatusMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_resolver_rules(MaxResults=None, NextToken=None, Filters=None):
    """
    Lists the resolver rules that were created using the current AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_resolver_rules(
        MaxResults=123,
        NextToken='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of resolver rules that you want to return in the response to a ListResolverRules request. If you don't specify a value for MaxResults , Resolver returns up to 100 resolver rules.

    :type NextToken: string
    :param NextToken: For the first ListResolverRules request, omit this value.
            If you have more than MaxResults resolver rules, you can submit another ListResolverRules request to get the next group of resolver rules. In the next request, specify the value of NextToken from the previous response.
            

    :type Filters: list
    :param Filters: An optional specification to return a subset of resolver rules, such as all resolver rules that are associated with the same resolver endpoint.
            Note
            If you submit a second or subsequent ListResolverRules request and specify the NextToken parameter, you must use the same values for Filters , if any, as in the previous request.
            (dict) --For List operations, an optional specification to return a subset of objects, such as resolver endpoints or resolver rules.
            Name (string) --When you're using a List operation and you want the operation to return a subset of objects, such as resolver endpoints or resolver rules, the name of the parameter that you want to use to filter objects. For example, to list only inbound resolver endpoints, specify Direction for the value of Name .
            Values (list) --When you're using a List operation and you want the operation to return a subset of objects, such as resolver endpoints or resolver rules, the value of the parameter that you want to use to filter objects. For example, to list only inbound resolver endpoints, specify INBOUND for the value of Values .
            (string) --
            
            

    :rtype: dict
    :return: {
        'NextToken': 'string',
        'MaxResults': 123,
        'ResolverRules': [
            {
                'Id': 'string',
                'CreatorRequestId': 'string',
                'Arn': 'string',
                'DomainName': 'string',
                'Status': 'COMPLETE'|'DELETING'|'UPDATING'|'FAILED',
                'StatusMessage': 'string',
                'RuleType': 'FORWARD'|'SYSTEM'|'RECURSIVE',
                'Name': 'string',
                'TargetIps': [
                    {
                        'Ip': 'string',
                        'Port': 123
                    },
                ],
                'ResolverEndpointId': 'string',
                'OwnerId': 'string',
                'ShareStatus': 'NOT_SHARED'|'SHARED_WITH_ME'|'SHARED_BY_ME'
            },
        ]
    }
    
    
    """
    pass

def list_tags_for_resource(ResourceArn=None, MaxResults=None, NextToken=None):
    """
    Lists the tags that you associated with the specified resource.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) for the resource that you want to list tags for.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of tags that you want to return in the response to a ListTagsForResource request. If you don't specify a value for MaxResults , Resolver returns up to 100 tags.

    :type NextToken: string
    :param NextToken: For the first ListTagsForResource request, omit this value.
            If you have more than MaxResults tags, you can submit another ListTagsForResource request to get the next group of tags for the resource. In the next request, specify the value of NextToken from the previous response.
            

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

def put_resolver_rule_policy(Arn=None, ResolverRulePolicy=None):
    """
    Specifies the Resolver operations and resources that you want to allow another AWS account to be able to use.
    See also: AWS API Documentation
    
    
    :example: response = client.put_resolver_rule_policy(
        Arn='string',
        ResolverRulePolicy='string'
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the account that you want to grant permissions to.
            

    :type ResolverRulePolicy: string
    :param ResolverRulePolicy: [REQUIRED]
            An AWS Identity and Access Management policy statement that lists the permissions that you want to grant to another AWS account.
            

    :rtype: dict
    :return: {
        'ReturnValue': True|False
    }
    
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Adds one or more tags to a specified resource.
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
            The Amazon Resource Name (ARN) for the resource that you want to add tags to. To get the ARN for a resource, use the applicable Get or List command:
            GetResolverEndpoint
            GetResolverRule
            GetResolverRuleAssociation
            ListResolverEndpoints
            ListResolverRuleAssociations
            ListResolverRules
            

    :type Tags: list
    :param Tags: [REQUIRED]
            The tags that you want to add to the specified resource.
            (dict) --One tag that you want to add to the specified resource. A tag consists of a Key (a name for the tag) and a Value .
            Key (string) --The name for the tag. For example, if you want to associate Resolver resources with the account IDs of your customers for billing purposes, the value of Key might be account-id .
            Value (string) --The value for the tag. For example, if Key is account-id , then Value might be the ID of the customer account that you're creating the resource for.
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Removes one or more tags from a specified resource.
    See also: AWS API Documentation
    
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) for the resource that you want to remove tags from. To get the ARN for a resource, use the applicable Get or List command:
            GetResolverEndpoint
            GetResolverRule
            GetResolverRuleAssociation
            ListResolverEndpoints
            ListResolverRuleAssociations
            ListResolverRules
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            The tags that you want to remove to the specified resource.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_resolver_endpoint(ResolverEndpointId=None, Name=None):
    """
    Updates the name of an inbound or an outbound resolver endpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.update_resolver_endpoint(
        ResolverEndpointId='string',
        Name='string'
    )
    
    
    :type ResolverEndpointId: string
    :param ResolverEndpointId: [REQUIRED]
            The ID of the resolver endpoint that you want to update.
            

    :type Name: string
    :param Name: The name of the resolver endpoint that you want to update.

    :rtype: dict
    :return: {
        'ResolverEndpoint': {
            'Id': 'string',
            'CreatorRequestId': 'string',
            'Arn': 'string',
            'Name': 'string',
            'SecurityGroupIds': [
                'string',
            ],
            'Direction': 'INBOUND'|'OUTBOUND',
            'IpAddressCount': 123,
            'HostVPCId': 'string',
            'Status': 'CREATING'|'OPERATIONAL'|'UPDATING'|'AUTO_RECOVERING'|'ACTION_NEEDED'|'DELETING',
            'StatusMessage': 'string',
            'CreationTime': 'string',
            'ModificationTime': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_resolver_rule(ResolverRuleId=None, Config=None):
    """
    Updates settings for a specified resolver rule. ResolverRuleId is required, and all other parameters are optional. If you don't specify a parameter, it retains its current value.
    See also: AWS API Documentation
    
    
    :example: response = client.update_resolver_rule(
        ResolverRuleId='string',
        Config={
            'Name': 'string',
            'TargetIps': [
                {
                    'Ip': 'string',
                    'Port': 123
                },
            ],
            'ResolverEndpointId': 'string'
        }
    )
    
    
    :type ResolverRuleId: string
    :param ResolverRuleId: [REQUIRED]
            The ID of the resolver rule that you want to update.
            

    :type Config: dict
    :param Config: [REQUIRED]
            The new settings for the resolver rule.
            Name (string) --The new name for the resolver rule. The name that you specify appears in the Resolver dashboard in the Route 53 console.
            TargetIps (list) --For DNS queries that originate in your VPC, the new IP addresses that you want to route outbound DNS queries to.
            (dict) --In a CreateResolverRule request, an array of the IPs that you want to forward DNS queries to.
            Ip (string) -- [REQUIRED]One IP address that you want to forward DNS queries to. You can specify only IPv4 addresses.
            Port (integer) --The port at Ip that you want to forward DNS queries to.
            
            ResolverEndpointId (string) --The ID of the new outbound resolver endpoint that you want to use to route DNS queries to the IP addresses that you specify in TargetIps .
            

    :rtype: dict
    :return: {
        'ResolverRule': {
            'Id': 'string',
            'CreatorRequestId': 'string',
            'Arn': 'string',
            'DomainName': 'string',
            'Status': 'COMPLETE'|'DELETING'|'UPDATING'|'FAILED',
            'StatusMessage': 'string',
            'RuleType': 'FORWARD'|'SYSTEM'|'RECURSIVE',
            'Name': 'string',
            'TargetIps': [
                {
                    'Ip': 'string',
                    'Port': 123
                },
            ],
            'ResolverEndpointId': 'string',
            'OwnerId': 'string',
            'ShareStatus': 'NOT_SHARED'|'SHARED_WITH_ME'|'SHARED_BY_ME'
        }
    }
    
    
    """
    pass

