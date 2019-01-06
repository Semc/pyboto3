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

def allocate_connection_on_interconnect(bandwidth=None, connectionName=None, ownerAccount=None, interconnectId=None, vlan=None):
    """
    Deprecated. Use  AllocateHostedConnection instead.
    Creates a hosted connection on an interconnect.
    Allocates a VLAN number and a specified amount of bandwidth for use by a hosted connection on the specified interconnect.
    See also: AWS API Documentation
    
    
    :example: response = client.allocate_connection_on_interconnect(
        bandwidth='string',
        connectionName='string',
        ownerAccount='string',
        interconnectId='string',
        vlan=123
    )
    
    
    :type bandwidth: string
    :param bandwidth: [REQUIRED]
            The bandwidth of the connection, in Mbps. The possible values are 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, and 500Mbps.
            

    :type connectionName: string
    :param connectionName: [REQUIRED]
            The name of the provisioned connection.
            

    :type ownerAccount: string
    :param ownerAccount: [REQUIRED]
            The ID of the AWS account of the customer for whom the connection will be provisioned.
            

    :type interconnectId: string
    :param interconnectId: [REQUIRED]
            The ID of the interconnect on which the connection will be provisioned. For example, dxcon-456abc78.
            

    :type vlan: integer
    :param vlan: [REQUIRED]
            The dedicated VLAN provisioned to the connection.
            

    :rtype: dict
    :return: {
        'ownerAccount': 'string',
        'connectionId': 'string',
        'connectionName': 'string',
        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
        'region': 'string',
        'location': 'string',
        'bandwidth': 'string',
        'vlan': 123,
        'partnerName': 'string',
        'loaIssueTime': datetime(2015, 1, 1),
        'lagId': 'string',
        'awsDevice': 'string',
        'jumboFrameCapable': True|False,
        'awsDeviceV2': 'string',
        'hasLogicalRedundancy': 'unknown'|'yes'|'no'
    }
    
    
    :returns: 
    ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
    requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    pending : The connection has been approved and is being initialized.
    available : The network link is up and the connection is ready for use.
    down : The network link is down.
    deleting : The connection is being deleted.
    deleted : The connection has been deleted.
    rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
    
    """
    pass

def allocate_hosted_connection(connectionId=None, ownerAccount=None, bandwidth=None, connectionName=None, vlan=None):
    """
    Creates a hosted connection on the specified interconnect or a link aggregation group (LAG).
    Allocates a VLAN number and a specified amount of bandwidth for use by a hosted connection on the specified interconnect or LAG.
    See also: AWS API Documentation
    
    
    :example: response = client.allocate_hosted_connection(
        connectionId='string',
        ownerAccount='string',
        bandwidth='string',
        connectionName='string',
        vlan=123
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]
            The ID of the interconnect or LAG.
            

    :type ownerAccount: string
    :param ownerAccount: [REQUIRED]
            The ID of the AWS account ID of the customer for the connection.
            

    :type bandwidth: string
    :param bandwidth: [REQUIRED]
            The bandwidth of the hosted connection, in Mbps. The possible values are 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, and 500Mbps.
            

    :type connectionName: string
    :param connectionName: [REQUIRED]
            The name of the hosted connection.
            

    :type vlan: integer
    :param vlan: [REQUIRED]
            The dedicated VLAN provisioned to the hosted connection.
            

    :rtype: dict
    :return: {
        'ownerAccount': 'string',
        'connectionId': 'string',
        'connectionName': 'string',
        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
        'region': 'string',
        'location': 'string',
        'bandwidth': 'string',
        'vlan': 123,
        'partnerName': 'string',
        'loaIssueTime': datetime(2015, 1, 1),
        'lagId': 'string',
        'awsDevice': 'string',
        'jumboFrameCapable': True|False,
        'awsDeviceV2': 'string',
        'hasLogicalRedundancy': 'unknown'|'yes'|'no'
    }
    
    
    :returns: 
    ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
    requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    pending : The connection has been approved and is being initialized.
    available : The network link is up and the connection is ready for use.
    down : The network link is down.
    deleting : The connection is being deleted.
    deleted : The connection has been deleted.
    rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
    
    """
    pass

def allocate_private_virtual_interface(connectionId=None, ownerAccount=None, newPrivateVirtualInterfaceAllocation=None):
    """
    Provisions a private virtual interface to be owned by the specified AWS account.
    Virtual interfaces created using this action must be confirmed by the owner using  ConfirmPrivateVirtualInterface . Until then, the virtual interface is in the Confirming state and is not available to handle traffic.
    See also: AWS API Documentation
    
    
    :example: response = client.allocate_private_virtual_interface(
        connectionId='string',
        ownerAccount='string',
        newPrivateVirtualInterfaceAllocation={
            'virtualInterfaceName': 'string',
            'vlan': 123,
            'asn': 123,
            'mtu': 123,
            'authKey': 'string',
            'amazonAddress': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'customerAddress': 'string'
        }
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]
            The ID of the connection on which the private virtual interface is provisioned.
            

    :type ownerAccount: string
    :param ownerAccount: [REQUIRED]
            The ID of the AWS account that owns the virtual private interface.
            

    :type newPrivateVirtualInterfaceAllocation: dict
    :param newPrivateVirtualInterfaceAllocation: [REQUIRED]
            Information about the private virtual interface.
            virtualInterfaceName (string) -- [REQUIRED]The name of the virtual interface assigned by the customer network.
            vlan (integer) -- [REQUIRED]The ID of the VLAN.
            asn (integer) -- [REQUIRED]The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
            mtu (integer) --The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The default value is 1500.
            authKey (string) --The authentication key for BGP configuration.
            amazonAddress (string) --The IP address assigned to the Amazon interface.
            addressFamily (string) --The address family for the BGP peer.
            customerAddress (string) --The IP address assigned to the customer interface.
            

    :rtype: dict
    :return: {
        'ownerAccount': 'string',
        'virtualInterfaceId': 'string',
        'location': 'string',
        'connectionId': 'string',
        'virtualInterfaceType': 'string',
        'virtualInterfaceName': 'string',
        'vlan': 123,
        'asn': 123,
        'amazonSideAsn': 123,
        'authKey': 'string',
        'amazonAddress': 'string',
        'customerAddress': 'string',
        'addressFamily': 'ipv4'|'ipv6',
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
        'customerRouterConfig': 'string',
        'mtu': 123,
        'jumboFrameCapable': True|False,
        'virtualGatewayId': 'string',
        'directConnectGatewayId': 'string',
        'routeFilterPrefixes': [
            {
                'cidr': 'string'
            },
        ],
        'bgpPeers': [
            {
                'bgpPeerId': 'string',
                'asn': 123,
                'authKey': 'string',
                'addressFamily': 'ipv4'|'ipv6',
                'amazonAddress': 'string',
                'customerAddress': 'string',
                'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                'bgpStatus': 'up'|'down',
                'awsDeviceV2': 'string'
            },
        ],
        'region': 'string',
        'awsDeviceV2': 'string'
    }
    
    
    :returns: 
    confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
    verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
    pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
    available : A virtual interface that is able to forward traffic.
    down : A virtual interface that is BGP down.
    deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
    deleted : A virtual interface that cannot forward traffic.
    rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
    
    """
    pass

def allocate_public_virtual_interface(connectionId=None, ownerAccount=None, newPublicVirtualInterfaceAllocation=None):
    """
    Provisions a public virtual interface to be owned by the specified AWS account.
    The owner of a connection calls this function to provision a public virtual interface to be owned by the specified AWS account.
    Virtual interfaces created using this function must be confirmed by the owner using  ConfirmPublicVirtualInterface . Until this step has been completed, the virtual interface is in the confirming state and is not available to handle traffic.
    When creating an IPv6 public virtual interface, omit the Amazon address and customer address. IPv6 addresses are automatically assigned from the Amazon pool of IPv6 addresses; you cannot specify custom IPv6 addresses.
    See also: AWS API Documentation
    
    
    :example: response = client.allocate_public_virtual_interface(
        connectionId='string',
        ownerAccount='string',
        newPublicVirtualInterfaceAllocation={
            'virtualInterfaceName': 'string',
            'vlan': 123,
            'asn': 123,
            'authKey': 'string',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'routeFilterPrefixes': [
                {
                    'cidr': 'string'
                },
            ]
        }
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]
            The ID of the connection on which the public virtual interface is provisioned.
            

    :type ownerAccount: string
    :param ownerAccount: [REQUIRED]
            The ID of the AWS account that owns the public virtual interface.
            

    :type newPublicVirtualInterfaceAllocation: dict
    :param newPublicVirtualInterfaceAllocation: [REQUIRED]
            Information about the public virtual interface.
            virtualInterfaceName (string) -- [REQUIRED]The name of the virtual interface assigned by the customer network.
            vlan (integer) -- [REQUIRED]The ID of the VLAN.
            asn (integer) -- [REQUIRED]The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
            authKey (string) --The authentication key for BGP configuration.
            amazonAddress (string) --The IP address assigned to the Amazon interface.
            customerAddress (string) --The IP address assigned to the customer interface.
            addressFamily (string) --The address family for the BGP peer.
            routeFilterPrefixes (list) --The routes to be advertised to the AWS network in this Region. Applies to public virtual interfaces.
            (dict) --Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.
            cidr (string) --The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.
            
            

    :rtype: dict
    :return: {
        'ownerAccount': 'string',
        'virtualInterfaceId': 'string',
        'location': 'string',
        'connectionId': 'string',
        'virtualInterfaceType': 'string',
        'virtualInterfaceName': 'string',
        'vlan': 123,
        'asn': 123,
        'amazonSideAsn': 123,
        'authKey': 'string',
        'amazonAddress': 'string',
        'customerAddress': 'string',
        'addressFamily': 'ipv4'|'ipv6',
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
        'customerRouterConfig': 'string',
        'mtu': 123,
        'jumboFrameCapable': True|False,
        'virtualGatewayId': 'string',
        'directConnectGatewayId': 'string',
        'routeFilterPrefixes': [
            {
                'cidr': 'string'
            },
        ],
        'bgpPeers': [
            {
                'bgpPeerId': 'string',
                'asn': 123,
                'authKey': 'string',
                'addressFamily': 'ipv4'|'ipv6',
                'amazonAddress': 'string',
                'customerAddress': 'string',
                'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                'bgpStatus': 'up'|'down',
                'awsDeviceV2': 'string'
            },
        ],
        'region': 'string',
        'awsDeviceV2': 'string'
    }
    
    
    :returns: 
    confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
    verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
    pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
    available : A virtual interface that is able to forward traffic.
    down : A virtual interface that is BGP down.
    deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
    deleted : A virtual interface that cannot forward traffic.
    rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
    
    """
    pass

def associate_connection_with_lag(connectionId=None, lagId=None):
    """
    Associates an existing connection with a link aggregation group (LAG). The connection is interrupted and re-established as a member of the LAG (connectivity to AWS is interrupted). The connection must be hosted on the same AWS Direct Connect endpoint as the LAG, and its bandwidth must match the bandwidth for the LAG. You can re-associate a connection that's currently associated with a different LAG; however, if removing the connection would cause the original LAG to fall below its setting for minimum number of operational connections, the request fails.
    Any virtual interfaces that are directly associated with the connection are automatically re-associated with the LAG. If the connection was originally associated with a different LAG, the virtual interfaces remain associated with the original LAG.
    For interconnects, any hosted connections are automatically re-associated with the LAG. If the interconnect was originally associated with a different LAG, the hosted connections remain associated with the original LAG.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_connection_with_lag(
        connectionId='string',
        lagId='string'
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]
            The ID of the connection. For example, dxcon-abc123.
            

    :type lagId: string
    :param lagId: [REQUIRED]
            The ID of the LAG with which to associate the connection. For example, dxlag-abc123.
            

    :rtype: dict
    :return: {
        'ownerAccount': 'string',
        'connectionId': 'string',
        'connectionName': 'string',
        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
        'region': 'string',
        'location': 'string',
        'bandwidth': 'string',
        'vlan': 123,
        'partnerName': 'string',
        'loaIssueTime': datetime(2015, 1, 1),
        'lagId': 'string',
        'awsDevice': 'string',
        'jumboFrameCapable': True|False,
        'awsDeviceV2': 'string',
        'hasLogicalRedundancy': 'unknown'|'yes'|'no'
    }
    
    
    :returns: 
    ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
    requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    pending : The connection has been approved and is being initialized.
    available : The network link is up and the connection is ready for use.
    down : The network link is down.
    deleting : The connection is being deleted.
    deleted : The connection has been deleted.
    rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
    
    """
    pass

def associate_hosted_connection(connectionId=None, parentConnectionId=None):
    """
    Associates a hosted connection and its virtual interfaces with a link aggregation group (LAG) or interconnect. If the target interconnect or LAG has an existing hosted connection with a conflicting VLAN number or IP address, the operation fails. This action temporarily interrupts the hosted connection's connectivity to AWS as it is being migrated.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_hosted_connection(
        connectionId='string',
        parentConnectionId='string'
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]
            The ID of the hosted connection.
            

    :type parentConnectionId: string
    :param parentConnectionId: [REQUIRED]
            The ID of the interconnect or the LAG.
            

    :rtype: dict
    :return: {
        'ownerAccount': 'string',
        'connectionId': 'string',
        'connectionName': 'string',
        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
        'region': 'string',
        'location': 'string',
        'bandwidth': 'string',
        'vlan': 123,
        'partnerName': 'string',
        'loaIssueTime': datetime(2015, 1, 1),
        'lagId': 'string',
        'awsDevice': 'string',
        'jumboFrameCapable': True|False,
        'awsDeviceV2': 'string',
        'hasLogicalRedundancy': 'unknown'|'yes'|'no'
    }
    
    
    :returns: 
    ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
    requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    pending : The connection has been approved and is being initialized.
    available : The network link is up and the connection is ready for use.
    down : The network link is down.
    deleting : The connection is being deleted.
    deleted : The connection has been deleted.
    rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
    
    """
    pass

def associate_virtual_interface(virtualInterfaceId=None, connectionId=None):
    """
    Associates a virtual interface with a specified link aggregation group (LAG) or connection. Connectivity to AWS is temporarily interrupted as the virtual interface is being migrated. If the target connection or LAG has an associated virtual interface with a conflicting VLAN number or a conflicting IP address, the operation fails.
    Virtual interfaces associated with a hosted connection cannot be associated with a LAG; hosted connections must be migrated along with their virtual interfaces using  AssociateHostedConnection .
    To reassociate a virtual interface to a new connection or LAG, the requester must own either the virtual interface itself or the connection to which the virtual interface is currently associated. Additionally, the requester must own the connection or LAG for the association.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_virtual_interface(
        virtualInterfaceId='string',
        connectionId='string'
    )
    
    
    :type virtualInterfaceId: string
    :param virtualInterfaceId: [REQUIRED]
            The ID of the virtual interface.
            

    :type connectionId: string
    :param connectionId: [REQUIRED]
            The ID of the LAG or connection.
            

    :rtype: dict
    :return: {
        'ownerAccount': 'string',
        'virtualInterfaceId': 'string',
        'location': 'string',
        'connectionId': 'string',
        'virtualInterfaceType': 'string',
        'virtualInterfaceName': 'string',
        'vlan': 123,
        'asn': 123,
        'amazonSideAsn': 123,
        'authKey': 'string',
        'amazonAddress': 'string',
        'customerAddress': 'string',
        'addressFamily': 'ipv4'|'ipv6',
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
        'customerRouterConfig': 'string',
        'mtu': 123,
        'jumboFrameCapable': True|False,
        'virtualGatewayId': 'string',
        'directConnectGatewayId': 'string',
        'routeFilterPrefixes': [
            {
                'cidr': 'string'
            },
        ],
        'bgpPeers': [
            {
                'bgpPeerId': 'string',
                'asn': 123,
                'authKey': 'string',
                'addressFamily': 'ipv4'|'ipv6',
                'amazonAddress': 'string',
                'customerAddress': 'string',
                'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                'bgpStatus': 'up'|'down',
                'awsDeviceV2': 'string'
            },
        ],
        'region': 'string',
        'awsDeviceV2': 'string'
    }
    
    
    :returns: 
    confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
    verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
    pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
    available : A virtual interface that is able to forward traffic.
    down : A virtual interface that is BGP down.
    deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
    deleted : A virtual interface that cannot forward traffic.
    rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
    
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

def confirm_connection(connectionId=None):
    """
    Confirms the creation of the specified hosted connection on an interconnect.
    Upon creation, the hosted connection is initially in the Ordering state, and remains in this state until the owner confirms creation of the hosted connection.
    See also: AWS API Documentation
    
    
    :example: response = client.confirm_connection(
        connectionId='string'
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]
            The ID of the hosted connection.
            

    :rtype: dict
    :return: {
        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'
    }
    
    
    """
    pass

def confirm_private_virtual_interface(virtualInterfaceId=None, virtualGatewayId=None, directConnectGatewayId=None):
    """
    Accepts ownership of a private virtual interface created by another AWS account.
    After the virtual interface owner makes this call, the virtual interface is created and attached to the specified virtual private gateway or Direct Connect gateway, and is made available to handle traffic.
    See also: AWS API Documentation
    
    
    :example: response = client.confirm_private_virtual_interface(
        virtualInterfaceId='string',
        virtualGatewayId='string',
        directConnectGatewayId='string'
    )
    
    
    :type virtualInterfaceId: string
    :param virtualInterfaceId: [REQUIRED]
            The ID of the virtual interface.
            

    :type virtualGatewayId: string
    :param virtualGatewayId: The ID of the virtual private gateway.

    :type directConnectGatewayId: string
    :param directConnectGatewayId: The ID of the Direct Connect gateway.

    :rtype: dict
    :return: {
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'
    }
    
    
    :returns: 
    confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
    verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
    pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
    available : A virtual interface that is able to forward traffic.
    down : A virtual interface that is BGP down.
    deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
    deleted : A virtual interface that cannot forward traffic.
    rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
    
    """
    pass

def confirm_public_virtual_interface(virtualInterfaceId=None):
    """
    Accepts ownership of a public virtual interface created by another AWS account.
    After the virtual interface owner makes this call, the specified virtual interface is created and made available to handle traffic.
    See also: AWS API Documentation
    
    
    :example: response = client.confirm_public_virtual_interface(
        virtualInterfaceId='string'
    )
    
    
    :type virtualInterfaceId: string
    :param virtualInterfaceId: [REQUIRED]
            The ID of the virtual interface.
            

    :rtype: dict
    :return: {
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'
    }
    
    
    """
    pass

def create_bgp_peer(virtualInterfaceId=None, newBGPPeer=None):
    """
    Creates a BGP peer on the specified virtual interface.
    You must create a BGP peer for the corresponding address family (IPv4/IPv6) in order to access AWS resources that also use that address family.
    If logical redundancy is not supported by the connection, interconnect, or LAG, the BGP peer cannot be in the same address family as an existing BGP peer on the virtual interface.
    When creating a IPv6 BGP peer, omit the Amazon address and customer address. IPv6 addresses are automatically assigned from the Amazon pool of IPv6 addresses; you cannot specify custom IPv6 addresses.
    For a public virtual interface, the Autonomous System Number (ASN) must be private or already whitelisted for the virtual interface.
    See also: AWS API Documentation
    
    
    :example: response = client.create_bgp_peer(
        virtualInterfaceId='string',
        newBGPPeer={
            'asn': 123,
            'authKey': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'amazonAddress': 'string',
            'customerAddress': 'string'
        }
    )
    
    
    :type virtualInterfaceId: string
    :param virtualInterfaceId: The ID of the virtual interface.

    :type newBGPPeer: dict
    :param newBGPPeer: Information about the BGP peer.
            asn (integer) --The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
            authKey (string) --The authentication key for BGP configuration.
            addressFamily (string) --The address family for the BGP peer.
            amazonAddress (string) --The IP address assigned to the Amazon interface.
            customerAddress (string) --The IP address assigned to the customer interface.
            

    :rtype: dict
    :return: {
        'virtualInterface': {
            'ownerAccount': 'string',
            'virtualInterfaceId': 'string',
            'location': 'string',
            'connectionId': 'string',
            'virtualInterfaceType': 'string',
            'virtualInterfaceName': 'string',
            'vlan': 123,
            'asn': 123,
            'amazonSideAsn': 123,
            'authKey': 'string',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
            'customerRouterConfig': 'string',
            'mtu': 123,
            'jumboFrameCapable': True|False,
            'virtualGatewayId': 'string',
            'directConnectGatewayId': 'string',
            'routeFilterPrefixes': [
                {
                    'cidr': 'string'
                },
            ],
            'bgpPeers': [
                {
                    'bgpPeerId': 'string',
                    'asn': 123,
                    'authKey': 'string',
                    'addressFamily': 'ipv4'|'ipv6',
                    'amazonAddress': 'string',
                    'customerAddress': 'string',
                    'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                    'bgpStatus': 'up'|'down',
                    'awsDeviceV2': 'string'
                },
            ],
            'region': 'string',
            'awsDeviceV2': 'string'
        }
    }
    
    
    :returns: 
    confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
    verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
    pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
    available : A virtual interface that is able to forward traffic.
    down : A virtual interface that is BGP down.
    deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
    deleted : A virtual interface that cannot forward traffic.
    rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
    
    """
    pass

def create_connection(location=None, bandwidth=None, connectionName=None, lagId=None):
    """
    Creates a connection between a customer network and a specific AWS Direct Connect location.
    A connection links your internal network to an AWS Direct Connect location over a standard Ethernet fiber-optic cable. One end of the cable is connected to your router, the other to an AWS Direct Connect router.
    To find the locations for your Region, use  DescribeLocations .
    You can automatically add the new connection to a link aggregation group (LAG) by specifying a LAG ID in the request. This ensures that the new connection is allocated on the same AWS Direct Connect endpoint that hosts the specified LAG. If there are no available ports on the endpoint, the request fails and no connection is created.
    See also: AWS API Documentation
    
    
    :example: response = client.create_connection(
        location='string',
        bandwidth='string',
        connectionName='string',
        lagId='string'
    )
    
    
    :type location: string
    :param location: [REQUIRED]
            The location of the connection.
            

    :type bandwidth: string
    :param bandwidth: [REQUIRED]
            The bandwidth of the connection.
            

    :type connectionName: string
    :param connectionName: [REQUIRED]
            The name of the connection.
            

    :type lagId: string
    :param lagId: The ID of the LAG.

    :rtype: dict
    :return: {
        'ownerAccount': 'string',
        'connectionId': 'string',
        'connectionName': 'string',
        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
        'region': 'string',
        'location': 'string',
        'bandwidth': 'string',
        'vlan': 123,
        'partnerName': 'string',
        'loaIssueTime': datetime(2015, 1, 1),
        'lagId': 'string',
        'awsDevice': 'string',
        'jumboFrameCapable': True|False,
        'awsDeviceV2': 'string',
        'hasLogicalRedundancy': 'unknown'|'yes'|'no'
    }
    
    
    :returns: 
    ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
    requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    pending : The connection has been approved and is being initialized.
    available : The network link is up and the connection is ready for use.
    down : The network link is down.
    deleting : The connection is being deleted.
    deleted : The connection has been deleted.
    rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
    
    """
    pass

def create_direct_connect_gateway(directConnectGatewayName=None, amazonSideAsn=None):
    """
    Creates a Direct Connect gateway, which is an intermediate object that enables you to connect a set of virtual interfaces and virtual private gateways. A Direct Connect gateway is global and visible in any AWS Region after it is created. The virtual interfaces and virtual private gateways that are connected through a Direct Connect gateway can be in different AWS Regions. This enables you to connect to a VPC in any Region, regardless of the Region in which the virtual interfaces are located, and pass traffic between them.
    See also: AWS API Documentation
    
    
    :example: response = client.create_direct_connect_gateway(
        directConnectGatewayName='string',
        amazonSideAsn=123
    )
    
    
    :type directConnectGatewayName: string
    :param directConnectGatewayName: [REQUIRED]
            The name of the Direct Connect gateway.
            

    :type amazonSideAsn: integer
    :param amazonSideAsn: The autonomous system number (ASN) for Border Gateway Protocol (BGP) to be configured on the Amazon side of the connection. The ASN must be in the private range of 64,512 to 65,534 or 4,200,000,000 to 4,294,967,294. The default is 64512.

    :rtype: dict
    :return: {
        'directConnectGateway': {
            'directConnectGatewayId': 'string',
            'directConnectGatewayName': 'string',
            'amazonSideAsn': 123,
            'ownerAccount': 'string',
            'directConnectGatewayState': 'pending'|'available'|'deleting'|'deleted',
            'stateChangeError': 'string'
        }
    }
    
    
    :returns: 
    pending : The initial state after calling  CreateDirectConnectGateway .
    available : The Direct Connect gateway is ready for use.
    deleting : The initial state after calling  DeleteDirectConnectGateway .
    deleted : The Direct Connect gateway is deleted and cannot pass traffic.
    
    """
    pass

def create_direct_connect_gateway_association(directConnectGatewayId=None, virtualGatewayId=None):
    """
    Creates an association between a Direct Connect gateway and a virtual private gateway. The virtual private gateway must be attached to a VPC and must not be associated with another Direct Connect gateway.
    See also: AWS API Documentation
    
    
    :example: response = client.create_direct_connect_gateway_association(
        directConnectGatewayId='string',
        virtualGatewayId='string'
    )
    
    
    :type directConnectGatewayId: string
    :param directConnectGatewayId: [REQUIRED]
            The ID of the Direct Connect gateway.
            

    :type virtualGatewayId: string
    :param virtualGatewayId: [REQUIRED]
            The ID of the virtual private gateway.
            

    :rtype: dict
    :return: {
        'directConnectGatewayAssociation': {
            'directConnectGatewayId': 'string',
            'virtualGatewayId': 'string',
            'virtualGatewayRegion': 'string',
            'virtualGatewayOwnerAccount': 'string',
            'associationState': 'associating'|'associated'|'disassociating'|'disassociated',
            'stateChangeError': 'string'
        }
    }
    
    
    :returns: 
    associating : The initial state after calling  CreateDirectConnectGatewayAssociation .
    associated : The Direct Connect gateway and virtual private gateway are successfully associated and ready to pass traffic.
    disassociating : The initial state after calling  DeleteDirectConnectGatewayAssociation .
    disassociated : The virtual private gateway is disassociated from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual private gateway is stopped.
    
    """
    pass

def create_interconnect(interconnectName=None, bandwidth=None, location=None, lagId=None):
    """
    Creates an interconnect between an AWS Direct Connect partner's network and a specific AWS Direct Connect location.
    An interconnect is a connection which is capable of hosting other connections. The partner can use an interconnect to provide sub-1Gbps AWS Direct Connect service to tier 2 customers who do not have their own connections. Like a standard connection, an interconnect links the partner's network to an AWS Direct Connect location over a standard Ethernet fiber-optic cable. One end is connected to the partner's router, the other to an AWS Direct Connect router.
    You can automatically add the new interconnect to a link aggregation group (LAG) by specifying a LAG ID in the request. This ensures that the new interconnect is allocated on the same AWS Direct Connect endpoint that hosts the specified LAG. If there are no available ports on the endpoint, the request fails and no interconnect is created.
    For each end customer, the AWS Direct Connect partner provisions a connection on their interconnect by calling  AllocateConnectionOnInterconnect . The end customer can then connect to AWS resources by creating a virtual interface on their connection, using the VLAN assigned to them by the partner.
    See also: AWS API Documentation
    
    
    :example: response = client.create_interconnect(
        interconnectName='string',
        bandwidth='string',
        location='string',
        lagId='string'
    )
    
    
    :type interconnectName: string
    :param interconnectName: [REQUIRED]
            The name of the interconnect.
            

    :type bandwidth: string
    :param bandwidth: [REQUIRED]
            The port bandwidth, in Gbps. The possible values are 1 and 10.
            

    :type location: string
    :param location: [REQUIRED]
            The location of the interconnect.
            

    :type lagId: string
    :param lagId: The ID of the LAG.

    :rtype: dict
    :return: {
        'interconnectId': 'string',
        'interconnectName': 'string',
        'interconnectState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted',
        'region': 'string',
        'location': 'string',
        'bandwidth': 'string',
        'loaIssueTime': datetime(2015, 1, 1),
        'lagId': 'string',
        'awsDevice': 'string',
        'jumboFrameCapable': True|False,
        'awsDeviceV2': 'string',
        'hasLogicalRedundancy': 'unknown'|'yes'|'no'
    }
    
    
    :returns: 
    requested : The initial state of an interconnect. The interconnect stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    pending : The interconnect is approved, and is being initialized.
    available : The network link is up, and the interconnect is ready for use.
    down : The network link is down.
    deleting : The interconnect is being deleted.
    deleted : The interconnect is deleted.
    
    """
    pass

def create_lag(numberOfConnections=None, location=None, connectionsBandwidth=None, lagName=None, connectionId=None):
    """
    Creates a link aggregation group (LAG) with the specified number of bundled physical connections between the customer network and a specific AWS Direct Connect location. A LAG is a logical interface that uses the Link Aggregation Control Protocol (LACP) to aggregate multiple interfaces, enabling you to treat them as a single interface.
    All connections in a LAG must use the same bandwidth and must terminate at the same AWS Direct Connect endpoint.
    You can have up to 10 connections per LAG. Regardless of this limit, if you request more connections for the LAG than AWS Direct Connect can allocate on a single endpoint, no LAG is created.
    You can specify an existing physical connection or interconnect to include in the LAG (which counts towards the total number of connections). Doing so interrupts the current physical connection or hosted connections, and re-establishes them as a member of the LAG. The LAG will be created on the same AWS Direct Connect endpoint to which the connection terminates. Any virtual interfaces associated with the connection are automatically disassociated and re-associated with the LAG. The connection ID does not change.
    If the AWS account used to create a LAG is a registered AWS Direct Connect partner, the LAG is automatically enabled to host sub-connections. For a LAG owned by a partner, any associated virtual interfaces cannot be directly configured.
    See also: AWS API Documentation
    
    
    :example: response = client.create_lag(
        numberOfConnections=123,
        location='string',
        connectionsBandwidth='string',
        lagName='string',
        connectionId='string'
    )
    
    
    :type numberOfConnections: integer
    :param numberOfConnections: [REQUIRED]
            The number of physical connections initially provisioned and bundled by the LAG.
            

    :type location: string
    :param location: [REQUIRED]
            The location for the LAG.
            

    :type connectionsBandwidth: string
    :param connectionsBandwidth: [REQUIRED]
            The bandwidth of the individual physical connections bundled by the LAG. The possible values are 1Gbps and 10Gbps.
            

    :type lagName: string
    :param lagName: [REQUIRED]
            The name of the LAG.
            

    :type connectionId: string
    :param connectionId: The ID of an existing connection to migrate to the LAG.

    :rtype: dict
    :return: {
        'connectionsBandwidth': 'string',
        'numberOfConnections': 123,
        'lagId': 'string',
        'ownerAccount': 'string',
        'lagName': 'string',
        'lagState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted',
        'location': 'string',
        'region': 'string',
        'minimumLinks': 123,
        'awsDevice': 'string',
        'awsDeviceV2': 'string',
        'connections': [
            {
                'ownerAccount': 'string',
                'connectionId': 'string',
                'connectionName': 'string',
                'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
                'region': 'string',
                'location': 'string',
                'bandwidth': 'string',
                'vlan': 123,
                'partnerName': 'string',
                'loaIssueTime': datetime(2015, 1, 1),
                'lagId': 'string',
                'awsDevice': 'string',
                'jumboFrameCapable': True|False,
                'awsDeviceV2': 'string',
                'hasLogicalRedundancy': 'unknown'|'yes'|'no'
            },
        ],
        'allowsHostedConnections': True|False,
        'jumboFrameCapable': True|False,
        'hasLogicalRedundancy': 'unknown'|'yes'|'no'
    }
    
    
    :returns: 
    requested : The initial state of a LAG. The LAG stays in the requested state until the Letter of Authorization (LOA) is available.
    pending : The LAG has been approved and is being initialized.
    available : The network link is established and the LAG is ready for use.
    down : The network link is down.
    deleting : The LAG is being deleted.
    deleted : The LAG is deleted.
    
    """
    pass

def create_private_virtual_interface(connectionId=None, newPrivateVirtualInterface=None):
    """
    Creates a private virtual interface. A virtual interface is the VLAN that transports AWS Direct Connect traffic. A private virtual interface can be connected to either a Direct Connect gateway or a Virtual Private Gateway (VGW). Connecting the private virtual interface to a Direct Connect gateway enables the possibility for connecting to multiple VPCs, including VPCs in different AWS Regions. Connecting the private virtual interface to a VGW only provides access to a single VPC within the same Region.
    See also: AWS API Documentation
    
    
    :example: response = client.create_private_virtual_interface(
        connectionId='string',
        newPrivateVirtualInterface={
            'virtualInterfaceName': 'string',
            'vlan': 123,
            'asn': 123,
            'mtu': 123,
            'authKey': 'string',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'virtualGatewayId': 'string',
            'directConnectGatewayId': 'string'
        }
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]
            The ID of the connection.
            

    :type newPrivateVirtualInterface: dict
    :param newPrivateVirtualInterface: [REQUIRED]
            Information about the private virtual interface.
            virtualInterfaceName (string) -- [REQUIRED]The name of the virtual interface assigned by the customer network.
            vlan (integer) -- [REQUIRED]The ID of the VLAN.
            asn (integer) -- [REQUIRED]The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
            mtu (integer) --The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The default value is 1500.
            authKey (string) --The authentication key for BGP configuration.
            amazonAddress (string) --The IP address assigned to the Amazon interface.
            customerAddress (string) --The IP address assigned to the customer interface.
            addressFamily (string) --The address family for the BGP peer.
            virtualGatewayId (string) --The ID of the virtual private gateway.
            directConnectGatewayId (string) --The ID of the Direct Connect gateway.
            

    :rtype: dict
    :return: {
        'ownerAccount': 'string',
        'virtualInterfaceId': 'string',
        'location': 'string',
        'connectionId': 'string',
        'virtualInterfaceType': 'string',
        'virtualInterfaceName': 'string',
        'vlan': 123,
        'asn': 123,
        'amazonSideAsn': 123,
        'authKey': 'string',
        'amazonAddress': 'string',
        'customerAddress': 'string',
        'addressFamily': 'ipv4'|'ipv6',
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
        'customerRouterConfig': 'string',
        'mtu': 123,
        'jumboFrameCapable': True|False,
        'virtualGatewayId': 'string',
        'directConnectGatewayId': 'string',
        'routeFilterPrefixes': [
            {
                'cidr': 'string'
            },
        ],
        'bgpPeers': [
            {
                'bgpPeerId': 'string',
                'asn': 123,
                'authKey': 'string',
                'addressFamily': 'ipv4'|'ipv6',
                'amazonAddress': 'string',
                'customerAddress': 'string',
                'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                'bgpStatus': 'up'|'down',
                'awsDeviceV2': 'string'
            },
        ],
        'region': 'string',
        'awsDeviceV2': 'string'
    }
    
    
    :returns: 
    confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
    verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
    pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
    available : A virtual interface that is able to forward traffic.
    down : A virtual interface that is BGP down.
    deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
    deleted : A virtual interface that cannot forward traffic.
    rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
    
    """
    pass

def create_public_virtual_interface(connectionId=None, newPublicVirtualInterface=None):
    """
    Creates a public virtual interface. A virtual interface is the VLAN that transports AWS Direct Connect traffic. A public virtual interface supports sending traffic to public services of AWS such as Amazon S3.
    When creating an IPv6 public virtual interface (addressFamily is ipv6 ), leave the customer and amazon address fields blank to use auto-assigned IPv6 space. Custom IPv6 addresses are not supported.
    See also: AWS API Documentation
    
    
    :example: response = client.create_public_virtual_interface(
        connectionId='string',
        newPublicVirtualInterface={
            'virtualInterfaceName': 'string',
            'vlan': 123,
            'asn': 123,
            'authKey': 'string',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'routeFilterPrefixes': [
                {
                    'cidr': 'string'
                },
            ]
        }
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]
            The ID of the connection.
            

    :type newPublicVirtualInterface: dict
    :param newPublicVirtualInterface: [REQUIRED]
            Information about the public virtual interface.
            virtualInterfaceName (string) -- [REQUIRED]The name of the virtual interface assigned by the customer network.
            vlan (integer) -- [REQUIRED]The ID of the VLAN.
            asn (integer) -- [REQUIRED]The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
            authKey (string) --The authentication key for BGP configuration.
            amazonAddress (string) --The IP address assigned to the Amazon interface.
            customerAddress (string) --The IP address assigned to the customer interface.
            addressFamily (string) --The address family for the BGP peer.
            routeFilterPrefixes (list) --The routes to be advertised to the AWS network in this Region. Applies to public virtual interfaces.
            (dict) --Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.
            cidr (string) --The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.
            
            

    :rtype: dict
    :return: {
        'ownerAccount': 'string',
        'virtualInterfaceId': 'string',
        'location': 'string',
        'connectionId': 'string',
        'virtualInterfaceType': 'string',
        'virtualInterfaceName': 'string',
        'vlan': 123,
        'asn': 123,
        'amazonSideAsn': 123,
        'authKey': 'string',
        'amazonAddress': 'string',
        'customerAddress': 'string',
        'addressFamily': 'ipv4'|'ipv6',
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
        'customerRouterConfig': 'string',
        'mtu': 123,
        'jumboFrameCapable': True|False,
        'virtualGatewayId': 'string',
        'directConnectGatewayId': 'string',
        'routeFilterPrefixes': [
            {
                'cidr': 'string'
            },
        ],
        'bgpPeers': [
            {
                'bgpPeerId': 'string',
                'asn': 123,
                'authKey': 'string',
                'addressFamily': 'ipv4'|'ipv6',
                'amazonAddress': 'string',
                'customerAddress': 'string',
                'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                'bgpStatus': 'up'|'down',
                'awsDeviceV2': 'string'
            },
        ],
        'region': 'string',
        'awsDeviceV2': 'string'
    }
    
    
    :returns: 
    confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
    verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
    pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
    available : A virtual interface that is able to forward traffic.
    down : A virtual interface that is BGP down.
    deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
    deleted : A virtual interface that cannot forward traffic.
    rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
    
    """
    pass

def delete_bgp_peer(virtualInterfaceId=None, asn=None, customerAddress=None, bgpPeerId=None):
    """
    Deletes the specified BGP peer on the specified virtual interface with the specified customer address and ASN.
    You cannot delete the last BGP peer from a virtual interface.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_bgp_peer(
        virtualInterfaceId='string',
        asn=123,
        customerAddress='string',
        bgpPeerId='string'
    )
    
    
    :type virtualInterfaceId: string
    :param virtualInterfaceId: The ID of the virtual interface.

    :type asn: integer
    :param asn: The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

    :type customerAddress: string
    :param customerAddress: The IP address assigned to the customer interface.

    :type bgpPeerId: string
    :param bgpPeerId: The ID of the BGP peer.

    :rtype: dict
    :return: {
        'virtualInterface': {
            'ownerAccount': 'string',
            'virtualInterfaceId': 'string',
            'location': 'string',
            'connectionId': 'string',
            'virtualInterfaceType': 'string',
            'virtualInterfaceName': 'string',
            'vlan': 123,
            'asn': 123,
            'amazonSideAsn': 123,
            'authKey': 'string',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
            'customerRouterConfig': 'string',
            'mtu': 123,
            'jumboFrameCapable': True|False,
            'virtualGatewayId': 'string',
            'directConnectGatewayId': 'string',
            'routeFilterPrefixes': [
                {
                    'cidr': 'string'
                },
            ],
            'bgpPeers': [
                {
                    'bgpPeerId': 'string',
                    'asn': 123,
                    'authKey': 'string',
                    'addressFamily': 'ipv4'|'ipv6',
                    'amazonAddress': 'string',
                    'customerAddress': 'string',
                    'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                    'bgpStatus': 'up'|'down',
                    'awsDeviceV2': 'string'
                },
            ],
            'region': 'string',
            'awsDeviceV2': 'string'
        }
    }
    
    
    :returns: 
    confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
    verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
    pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
    available : A virtual interface that is able to forward traffic.
    down : A virtual interface that is BGP down.
    deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
    deleted : A virtual interface that cannot forward traffic.
    rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
    
    """
    pass

def delete_connection(connectionId=None):
    """
    Deletes the specified connection.
    Deleting a connection only stops the AWS Direct Connect port hour and data transfer charges. If you are partnering with any third parties to connect with the AWS Direct Connect location, you must cancel your service with them separately.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_connection(
        connectionId='string'
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]
            The ID of the connection.
            

    :rtype: dict
    :return: {
        'ownerAccount': 'string',
        'connectionId': 'string',
        'connectionName': 'string',
        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
        'region': 'string',
        'location': 'string',
        'bandwidth': 'string',
        'vlan': 123,
        'partnerName': 'string',
        'loaIssueTime': datetime(2015, 1, 1),
        'lagId': 'string',
        'awsDevice': 'string',
        'jumboFrameCapable': True|False,
        'awsDeviceV2': 'string',
        'hasLogicalRedundancy': 'unknown'|'yes'|'no'
    }
    
    
    """
    pass

def delete_direct_connect_gateway(directConnectGatewayId=None):
    """
    Deletes the specified Direct Connect gateway. You must first delete all virtual interfaces that are attached to the Direct Connect gateway and disassociate all virtual private gateways that are associated with the Direct Connect gateway.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_direct_connect_gateway(
        directConnectGatewayId='string'
    )
    
    
    :type directConnectGatewayId: string
    :param directConnectGatewayId: [REQUIRED]
            The ID of the Direct Connect gateway.
            

    :rtype: dict
    :return: {
        'directConnectGateway': {
            'directConnectGatewayId': 'string',
            'directConnectGatewayName': 'string',
            'amazonSideAsn': 123,
            'ownerAccount': 'string',
            'directConnectGatewayState': 'pending'|'available'|'deleting'|'deleted',
            'stateChangeError': 'string'
        }
    }
    
    
    """
    pass

def delete_direct_connect_gateway_association(directConnectGatewayId=None, virtualGatewayId=None):
    """
    Deletes the association between the specified Direct Connect gateway and virtual private gateway.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_direct_connect_gateway_association(
        directConnectGatewayId='string',
        virtualGatewayId='string'
    )
    
    
    :type directConnectGatewayId: string
    :param directConnectGatewayId: [REQUIRED]
            The ID of the Direct Connect gateway.
            

    :type virtualGatewayId: string
    :param virtualGatewayId: [REQUIRED]
            The ID of the virtual private gateway.
            

    :rtype: dict
    :return: {
        'directConnectGatewayAssociation': {
            'directConnectGatewayId': 'string',
            'virtualGatewayId': 'string',
            'virtualGatewayRegion': 'string',
            'virtualGatewayOwnerAccount': 'string',
            'associationState': 'associating'|'associated'|'disassociating'|'disassociated',
            'stateChangeError': 'string'
        }
    }
    
    
    :returns: 
    associating : The initial state after calling  CreateDirectConnectGatewayAssociation .
    associated : The Direct Connect gateway and virtual private gateway are successfully associated and ready to pass traffic.
    disassociating : The initial state after calling  DeleteDirectConnectGatewayAssociation .
    disassociated : The virtual private gateway is disassociated from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual private gateway is stopped.
    
    """
    pass

def delete_interconnect(interconnectId=None):
    """
    Deletes the specified interconnect.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_interconnect(
        interconnectId='string'
    )
    
    
    :type interconnectId: string
    :param interconnectId: [REQUIRED]
            The ID of the interconnect.
            

    :rtype: dict
    :return: {
        'interconnectState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted'
    }
    
    
    """
    pass

def delete_lag(lagId=None):
    """
    Deletes the specified link aggregation group (LAG). You cannot delete a LAG if it has active virtual interfaces or hosted connections.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_lag(
        lagId='string'
    )
    
    
    :type lagId: string
    :param lagId: [REQUIRED]
            The ID of the LAG.
            

    :rtype: dict
    :return: {
        'connectionsBandwidth': 'string',
        'numberOfConnections': 123,
        'lagId': 'string',
        'ownerAccount': 'string',
        'lagName': 'string',
        'lagState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted',
        'location': 'string',
        'region': 'string',
        'minimumLinks': 123,
        'awsDevice': 'string',
        'awsDeviceV2': 'string',
        'connections': [
            {
                'ownerAccount': 'string',
                'connectionId': 'string',
                'connectionName': 'string',
                'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
                'region': 'string',
                'location': 'string',
                'bandwidth': 'string',
                'vlan': 123,
                'partnerName': 'string',
                'loaIssueTime': datetime(2015, 1, 1),
                'lagId': 'string',
                'awsDevice': 'string',
                'jumboFrameCapable': True|False,
                'awsDeviceV2': 'string',
                'hasLogicalRedundancy': 'unknown'|'yes'|'no'
            },
        ],
        'allowsHostedConnections': True|False,
        'jumboFrameCapable': True|False,
        'hasLogicalRedundancy': 'unknown'|'yes'|'no'
    }
    
    
    :returns: 
    ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
    requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    pending : The connection has been approved and is being initialized.
    available : The network link is up and the connection is ready for use.
    down : The network link is down.
    deleting : The connection is being deleted.
    deleted : The connection has been deleted.
    rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
    
    """
    pass

def delete_virtual_interface(virtualInterfaceId=None):
    """
    Deletes a virtual interface.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_virtual_interface(
        virtualInterfaceId='string'
    )
    
    
    :type virtualInterfaceId: string
    :param virtualInterfaceId: [REQUIRED]
            The ID of the virtual interface.
            

    :rtype: dict
    :return: {
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'
    }
    
    
    """
    pass

def describe_connection_loa(connectionId=None, providerName=None, loaContentType=None):
    """
    Deprecated. Use  DescribeLoa instead.
    Gets the LOA-CFA for a connection.
    The Letter of Authorization - Connecting Facility Assignment (LOA-CFA) is a document that your APN partner or service provider uses when establishing your cross connect to AWS at the colocation facility. For more information, see Requesting Cross Connects at AWS Direct Connect Locations in the AWS Direct Connect User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_connection_loa(
        connectionId='string',
        providerName='string',
        loaContentType='application/pdf'
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]
            The ID of the connection.
            

    :type providerName: string
    :param providerName: The name of the APN partner or service provider who establishes connectivity on your behalf. If you specify this parameter, the LOA-CFA lists the provider name alongside your company name as the requester of the cross connect.

    :type loaContentType: string
    :param loaContentType: The standard media type for the LOA-CFA document. The only supported value is application/pdf.

    :rtype: dict
    :return: {
        'loa': {
            'loaContent': b'bytes',
            'loaContentType': 'application/pdf'
        }
    }
    
    
    """
    pass

def describe_connections(connectionId=None):
    """
    Displays the specified connection or all connections in this Region.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_connections(
        connectionId='string'
    )
    
    
    :type connectionId: string
    :param connectionId: The ID of the connection.

    :rtype: dict
    :return: {
        'connections': [
            {
                'ownerAccount': 'string',
                'connectionId': 'string',
                'connectionName': 'string',
                'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
                'region': 'string',
                'location': 'string',
                'bandwidth': 'string',
                'vlan': 123,
                'partnerName': 'string',
                'loaIssueTime': datetime(2015, 1, 1),
                'lagId': 'string',
                'awsDevice': 'string',
                'jumboFrameCapable': True|False,
                'awsDeviceV2': 'string',
                'hasLogicalRedundancy': 'unknown'|'yes'|'no'
            },
        ]
    }
    
    
    """
    pass

def describe_connections_on_interconnect(interconnectId=None):
    """
    Deprecated. Use  DescribeHostedConnections instead.
    Lists the connections that have been provisioned on the specified interconnect.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_connections_on_interconnect(
        interconnectId='string'
    )
    
    
    :type interconnectId: string
    :param interconnectId: [REQUIRED]
            The ID of the interconnect.
            

    :rtype: dict
    :return: {
        'connections': [
            {
                'ownerAccount': 'string',
                'connectionId': 'string',
                'connectionName': 'string',
                'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
                'region': 'string',
                'location': 'string',
                'bandwidth': 'string',
                'vlan': 123,
                'partnerName': 'string',
                'loaIssueTime': datetime(2015, 1, 1),
                'lagId': 'string',
                'awsDevice': 'string',
                'jumboFrameCapable': True|False,
                'awsDeviceV2': 'string',
                'hasLogicalRedundancy': 'unknown'|'yes'|'no'
            },
        ]
    }
    
    
    """
    pass

def describe_direct_connect_gateway_associations(directConnectGatewayId=None, virtualGatewayId=None, maxResults=None, nextToken=None):
    """
    Lists the associations between your Direct Connect gateways and virtual private gateways. You must specify a Direct Connect gateway, a virtual private gateway, or both. If you specify a Direct Connect gateway, the response contains all virtual private gateways associated with the Direct Connect gateway. If you specify a virtual private gateway, the response contains all Direct Connect gateways associated with the virtual private gateway. If you specify both, the response contains the association between the Direct Connect gateway and the virtual private gateway.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_direct_connect_gateway_associations(
        directConnectGatewayId='string',
        virtualGatewayId='string',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type directConnectGatewayId: string
    :param directConnectGatewayId: The ID of the Direct Connect gateway.

    :type virtualGatewayId: string
    :param virtualGatewayId: The ID of the virtual private gateway.

    :type maxResults: integer
    :param maxResults: The maximum number of associations to return per page.

    :type nextToken: string
    :param nextToken: The token provided in the previous call to retrieve the next page.

    :rtype: dict
    :return: {
        'directConnectGatewayAssociations': [
            {
                'directConnectGatewayId': 'string',
                'virtualGatewayId': 'string',
                'virtualGatewayRegion': 'string',
                'virtualGatewayOwnerAccount': 'string',
                'associationState': 'associating'|'associated'|'disassociating'|'disassociated',
                'stateChangeError': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    associating : The initial state after calling  CreateDirectConnectGatewayAssociation .
    associated : The Direct Connect gateway and virtual private gateway are successfully associated and ready to pass traffic.
    disassociating : The initial state after calling  DeleteDirectConnectGatewayAssociation .
    disassociated : The virtual private gateway is disassociated from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual private gateway is stopped.
    
    """
    pass

def describe_direct_connect_gateway_attachments(directConnectGatewayId=None, virtualInterfaceId=None, maxResults=None, nextToken=None):
    """
    Lists the attachments between your Direct Connect gateways and virtual interfaces. You must specify a Direct Connect gateway, a virtual interface, or both. If you specify a Direct Connect gateway, the response contains all virtual interfaces attached to the Direct Connect gateway. If you specify a virtual interface, the response contains all Direct Connect gateways attached to the virtual interface. If you specify both, the response contains the attachment between the Direct Connect gateway and the virtual interface.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_direct_connect_gateway_attachments(
        directConnectGatewayId='string',
        virtualInterfaceId='string',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type directConnectGatewayId: string
    :param directConnectGatewayId: The ID of the Direct Connect gateway.

    :type virtualInterfaceId: string
    :param virtualInterfaceId: The ID of the virtual interface.

    :type maxResults: integer
    :param maxResults: The maximum number of attachments to return per page.

    :type nextToken: string
    :param nextToken: The token provided in the previous call to retrieve the next page.

    :rtype: dict
    :return: {
        'directConnectGatewayAttachments': [
            {
                'directConnectGatewayId': 'string',
                'virtualInterfaceId': 'string',
                'virtualInterfaceRegion': 'string',
                'virtualInterfaceOwnerAccount': 'string',
                'attachmentState': 'attaching'|'attached'|'detaching'|'detached',
                'stateChangeError': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    attaching : The initial state after a virtual interface is created using the Direct Connect gateway.
    attached : The Direct Connect gateway and virtual interface are attached and ready to pass traffic.
    detaching : The initial state after calling  DeleteVirtualInterface .
    detached : The virtual interface is detached from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual interface is stopped.
    
    """
    pass

def describe_direct_connect_gateways(directConnectGatewayId=None, maxResults=None, nextToken=None):
    """
    Lists all your Direct Connect gateways or only the specified Direct Connect gateway. Deleted Direct Connect gateways are not returned.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_direct_connect_gateways(
        directConnectGatewayId='string',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type directConnectGatewayId: string
    :param directConnectGatewayId: The ID of the Direct Connect gateway.

    :type maxResults: integer
    :param maxResults: The maximum number of Direct Connect gateways to return per page.

    :type nextToken: string
    :param nextToken: The token provided in the previous call to retrieve the next page.

    :rtype: dict
    :return: {
        'directConnectGateways': [
            {
                'directConnectGatewayId': 'string',
                'directConnectGatewayName': 'string',
                'amazonSideAsn': 123,
                'ownerAccount': 'string',
                'directConnectGatewayState': 'pending'|'available'|'deleting'|'deleted',
                'stateChangeError': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    pending : The initial state after calling  CreateDirectConnectGateway .
    available : The Direct Connect gateway is ready for use.
    deleting : The initial state after calling  DeleteDirectConnectGateway .
    deleted : The Direct Connect gateway is deleted and cannot pass traffic.
    
    """
    pass

def describe_hosted_connections(connectionId=None):
    """
    Lists the hosted connections that have been provisioned on the specified interconnect or link aggregation group (LAG).
    See also: AWS API Documentation
    
    
    :example: response = client.describe_hosted_connections(
        connectionId='string'
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]
            The ID of the interconnect or LAG.
            

    :rtype: dict
    :return: {
        'connections': [
            {
                'ownerAccount': 'string',
                'connectionId': 'string',
                'connectionName': 'string',
                'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
                'region': 'string',
                'location': 'string',
                'bandwidth': 'string',
                'vlan': 123,
                'partnerName': 'string',
                'loaIssueTime': datetime(2015, 1, 1),
                'lagId': 'string',
                'awsDevice': 'string',
                'jumboFrameCapable': True|False,
                'awsDeviceV2': 'string',
                'hasLogicalRedundancy': 'unknown'|'yes'|'no'
            },
        ]
    }
    
    
    """
    pass

def describe_interconnect_loa(interconnectId=None, providerName=None, loaContentType=None):
    """
    Deprecated. Use  DescribeLoa instead.
    Gets the LOA-CFA for the specified interconnect.
    The Letter of Authorization - Connecting Facility Assignment (LOA-CFA) is a document that is used when establishing your cross connect to AWS at the colocation facility. For more information, see Requesting Cross Connects at AWS Direct Connect Locations in the AWS Direct Connect User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_interconnect_loa(
        interconnectId='string',
        providerName='string',
        loaContentType='application/pdf'
    )
    
    
    :type interconnectId: string
    :param interconnectId: [REQUIRED]
            The ID of the interconnect.
            

    :type providerName: string
    :param providerName: The name of the service provider who establishes connectivity on your behalf. If you supply this parameter, the LOA-CFA lists the provider name alongside your company name as the requester of the cross connect.

    :type loaContentType: string
    :param loaContentType: The standard media type for the LOA-CFA document. The only supported value is application/pdf.

    :rtype: dict
    :return: {
        'loa': {
            'loaContent': b'bytes',
            'loaContentType': 'application/pdf'
        }
    }
    
    
    """
    pass

def describe_interconnects(interconnectId=None):
    """
    Lists the interconnects owned by the AWS account or only the specified interconnect.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_interconnects(
        interconnectId='string'
    )
    
    
    :type interconnectId: string
    :param interconnectId: The ID of the interconnect.

    :rtype: dict
    :return: {
        'interconnects': [
            {
                'interconnectId': 'string',
                'interconnectName': 'string',
                'interconnectState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted',
                'region': 'string',
                'location': 'string',
                'bandwidth': 'string',
                'loaIssueTime': datetime(2015, 1, 1),
                'lagId': 'string',
                'awsDevice': 'string',
                'jumboFrameCapable': True|False,
                'awsDeviceV2': 'string',
                'hasLogicalRedundancy': 'unknown'|'yes'|'no'
            },
        ]
    }
    
    
    """
    pass

def describe_lags(lagId=None):
    """
    Describes all your link aggregation groups (LAG) or the specified LAG.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_lags(
        lagId='string'
    )
    
    
    :type lagId: string
    :param lagId: The ID of the LAG.

    :rtype: dict
    :return: {
        'lags': [
            {
                'connectionsBandwidth': 'string',
                'numberOfConnections': 123,
                'lagId': 'string',
                'ownerAccount': 'string',
                'lagName': 'string',
                'lagState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted',
                'location': 'string',
                'region': 'string',
                'minimumLinks': 123,
                'awsDevice': 'string',
                'awsDeviceV2': 'string',
                'connections': [
                    {
                        'ownerAccount': 'string',
                        'connectionId': 'string',
                        'connectionName': 'string',
                        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
                        'region': 'string',
                        'location': 'string',
                        'bandwidth': 'string',
                        'vlan': 123,
                        'partnerName': 'string',
                        'loaIssueTime': datetime(2015, 1, 1),
                        'lagId': 'string',
                        'awsDevice': 'string',
                        'jumboFrameCapable': True|False,
                        'awsDeviceV2': 'string',
                        'hasLogicalRedundancy': 'unknown'|'yes'|'no'
                    },
                ],
                'allowsHostedConnections': True|False,
                'jumboFrameCapable': True|False,
                'hasLogicalRedundancy': 'unknown'|'yes'|'no'
            },
        ]
    }
    
    
    :returns: 
    ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
    requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    pending : The connection has been approved and is being initialized.
    available : The network link is up and the connection is ready for use.
    down : The network link is down.
    deleting : The connection is being deleted.
    deleted : The connection has been deleted.
    rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
    
    """
    pass

def describe_loa(connectionId=None, providerName=None, loaContentType=None):
    """
    Gets the LOA-CFA for a connection, interconnect, or link aggregation group (LAG).
    The Letter of Authorization - Connecting Facility Assignment (LOA-CFA) is a document that is used when establishing your cross connect to AWS at the colocation facility. For more information, see Requesting Cross Connects at AWS Direct Connect Locations in the AWS Direct Connect User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_loa(
        connectionId='string',
        providerName='string',
        loaContentType='application/pdf'
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]
            The ID of a connection, LAG, or interconnect.
            

    :type providerName: string
    :param providerName: The name of the service provider who establishes connectivity on your behalf. If you specify this parameter, the LOA-CFA lists the provider name alongside your company name as the requester of the cross connect.

    :type loaContentType: string
    :param loaContentType: The standard media type for the LOA-CFA document. The only supported value is application/pdf.

    :rtype: dict
    :return: {
        'loaContent': b'bytes',
        'loaContentType': 'application/pdf'
    }
    
    
    """
    pass

def describe_locations():
    """
    Lists the AWS Direct Connect locations in the current AWS Region. These are the locations that can be selected when calling  CreateConnection or  CreateInterconnect .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_locations()
    
    
    :rtype: dict
    :return: {
        'locations': [
            {
                'locationCode': 'string',
                'locationName': 'string',
                'region': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_tags(resourceArns=None):
    """
    Describes the tags associated with the specified AWS Direct Connect resources.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_tags(
        resourceArns=[
            'string',
        ]
    )
    
    
    :type resourceArns: list
    :param resourceArns: [REQUIRED]
            The Amazon Resource Names (ARNs) of the resources.
            (string) --
            

    :rtype: dict
    :return: {
        'resourceTags': [
            {
                'resourceArn': 'string',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def describe_virtual_gateways():
    """
    Lists the virtual private gateways owned by the AWS account.
    You can create one or more AWS Direct Connect private virtual interfaces linked to a virtual private gateway.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_virtual_gateways()
    
    
    :rtype: dict
    :return: {
        'virtualGateways': [
            {
                'virtualGatewayId': 'string',
                'virtualGatewayState': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_virtual_interfaces(connectionId=None, virtualInterfaceId=None):
    """
    Displays all virtual interfaces for an AWS account. Virtual interfaces deleted fewer than 15 minutes before you make the request are also returned. If you specify a connection ID, only the virtual interfaces associated with the connection are returned. If you specify a virtual interface ID, then only a single virtual interface is returned.
    A virtual interface (VLAN) transmits the traffic between the AWS Direct Connect location and the customer network.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_virtual_interfaces(
        connectionId='string',
        virtualInterfaceId='string'
    )
    
    
    :type connectionId: string
    :param connectionId: The ID of the connection.

    :type virtualInterfaceId: string
    :param virtualInterfaceId: The ID of the virtual interface.

    :rtype: dict
    :return: {
        'virtualInterfaces': [
            {
                'ownerAccount': 'string',
                'virtualInterfaceId': 'string',
                'location': 'string',
                'connectionId': 'string',
                'virtualInterfaceType': 'string',
                'virtualInterfaceName': 'string',
                'vlan': 123,
                'asn': 123,
                'amazonSideAsn': 123,
                'authKey': 'string',
                'amazonAddress': 'string',
                'customerAddress': 'string',
                'addressFamily': 'ipv4'|'ipv6',
                'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
                'customerRouterConfig': 'string',
                'mtu': 123,
                'jumboFrameCapable': True|False,
                'virtualGatewayId': 'string',
                'directConnectGatewayId': 'string',
                'routeFilterPrefixes': [
                    {
                        'cidr': 'string'
                    },
                ],
                'bgpPeers': [
                    {
                        'bgpPeerId': 'string',
                        'asn': 123,
                        'authKey': 'string',
                        'addressFamily': 'ipv4'|'ipv6',
                        'amazonAddress': 'string',
                        'customerAddress': 'string',
                        'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                        'bgpStatus': 'up'|'down',
                        'awsDeviceV2': 'string'
                    },
                ],
                'region': 'string',
                'awsDeviceV2': 'string'
            },
        ]
    }
    
    
    :returns: 
    confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
    verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
    pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
    available : A virtual interface that is able to forward traffic.
    down : A virtual interface that is BGP down.
    deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
    deleted : A virtual interface that cannot forward traffic.
    rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
    
    """
    pass

def disassociate_connection_from_lag(connectionId=None, lagId=None):
    """
    Disassociates a connection from a link aggregation group (LAG). The connection is interrupted and re-established as a standalone connection (the connection is not deleted; to delete the connection, use the  DeleteConnection request). If the LAG has associated virtual interfaces or hosted connections, they remain associated with the LAG. A disassociated connection owned by an AWS Direct Connect partner is automatically converted to an interconnect.
    If disassociating the connection would cause the LAG to fall below its setting for minimum number of operational connections, the request fails, except when it's the last member of the LAG. If all connections are disassociated, the LAG continues to exist as an empty LAG with no physical connections.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_connection_from_lag(
        connectionId='string',
        lagId='string'
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]
            The ID of the connection. For example, dxcon-abc123.
            

    :type lagId: string
    :param lagId: [REQUIRED]
            The ID of the LAG. For example, dxlag-abc123.
            

    :rtype: dict
    :return: {
        'ownerAccount': 'string',
        'connectionId': 'string',
        'connectionName': 'string',
        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
        'region': 'string',
        'location': 'string',
        'bandwidth': 'string',
        'vlan': 123,
        'partnerName': 'string',
        'loaIssueTime': datetime(2015, 1, 1),
        'lagId': 'string',
        'awsDevice': 'string',
        'jumboFrameCapable': True|False,
        'awsDeviceV2': 'string',
        'hasLogicalRedundancy': 'unknown'|'yes'|'no'
    }
    
    
    :returns: 
    ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
    requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    pending : The connection has been approved and is being initialized.
    available : The network link is up and the connection is ready for use.
    down : The network link is down.
    deleting : The connection is being deleted.
    deleted : The connection has been deleted.
    rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
    
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

def tag_resource(resourceArn=None, tags=None):
    """
    Adds the specified tags to the specified AWS Direct Connect resource. Each resource can have a maximum of 50 tags.
    Each tag consists of a key and an optional value. If a tag with the same key is already associated with the resource, this action updates its value.
    See also: AWS API Documentation
    
    
    :example: response = client.tag_resource(
        resourceArn='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource.
            

    :type tags: list
    :param tags: [REQUIRED]
            The tags to add.
            (dict) --Information about a tag.
            key (string) -- [REQUIRED]The key.
            value (string) --The value.
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Removes one or more tags from the specified AWS Direct Connect resource.
    See also: AWS API Documentation
    
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource.
            

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

def update_lag(lagId=None, lagName=None, minimumLinks=None):
    """
    Updates the attributes of the specified link aggregation group (LAG).
    You can update the following attributes:
    When you create a LAG, the default value for the minimum number of operational connections is zero (0). If you update this value and the number of operational connections falls below the specified value, the LAG automatically goes down to avoid over-utilization of the remaining connections. Adjust this value with care, as it could force the LAG down if it is set higher than the current number of operational connections.
    See also: AWS API Documentation
    
    
    :example: response = client.update_lag(
        lagId='string',
        lagName='string',
        minimumLinks=123
    )
    
    
    :type lagId: string
    :param lagId: [REQUIRED]
            The ID of the LAG.
            

    :type lagName: string
    :param lagName: The name of the LAG.

    :type minimumLinks: integer
    :param minimumLinks: The minimum number of physical connections that must be operational for the LAG itself to be operational.

    :rtype: dict
    :return: {
        'connectionsBandwidth': 'string',
        'numberOfConnections': 123,
        'lagId': 'string',
        'ownerAccount': 'string',
        'lagName': 'string',
        'lagState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted',
        'location': 'string',
        'region': 'string',
        'minimumLinks': 123,
        'awsDevice': 'string',
        'awsDeviceV2': 'string',
        'connections': [
            {
                'ownerAccount': 'string',
                'connectionId': 'string',
                'connectionName': 'string',
                'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
                'region': 'string',
                'location': 'string',
                'bandwidth': 'string',
                'vlan': 123,
                'partnerName': 'string',
                'loaIssueTime': datetime(2015, 1, 1),
                'lagId': 'string',
                'awsDevice': 'string',
                'jumboFrameCapable': True|False,
                'awsDeviceV2': 'string',
                'hasLogicalRedundancy': 'unknown'|'yes'|'no'
            },
        ],
        'allowsHostedConnections': True|False,
        'jumboFrameCapable': True|False,
        'hasLogicalRedundancy': 'unknown'|'yes'|'no'
    }
    
    
    :returns: 
    lagId (string) -- [REQUIRED]
    The ID of the LAG.
    
    lagName (string) -- The name of the LAG.
    minimumLinks (integer) -- The minimum number of physical connections that must be operational for the LAG itself to be operational.
    
    """
    pass

def update_virtual_interface_attributes(virtualInterfaceId=None, mtu=None):
    """
    Updates the specified attributes of the specified virtual private interface.
    Setting the MTU of a virtual interface to 9001 (jumbo frames) can cause an update to the underlying physical connection if it wasn't updated to support jumbo frames. Updating the connection disrupts network connectivity for all virtual interfaces associated with the connection for up to 30 seconds. To check whether your connection supports jumbo frames, call  DescribeConnections . To check whether your virtual interface supports jumbo frames, call  DescribeVirtualInterfaces .
    See also: AWS API Documentation
    
    
    :example: response = client.update_virtual_interface_attributes(
        virtualInterfaceId='string',
        mtu=123
    )
    
    
    :type virtualInterfaceId: string
    :param virtualInterfaceId: [REQUIRED]
            The ID of the virtual private interface.
            

    :type mtu: integer
    :param mtu: The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The default value is 1500.

    :rtype: dict
    :return: {
        'ownerAccount': 'string',
        'virtualInterfaceId': 'string',
        'location': 'string',
        'connectionId': 'string',
        'virtualInterfaceType': 'string',
        'virtualInterfaceName': 'string',
        'vlan': 123,
        'asn': 123,
        'amazonSideAsn': 123,
        'authKey': 'string',
        'amazonAddress': 'string',
        'customerAddress': 'string',
        'addressFamily': 'ipv4'|'ipv6',
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
        'customerRouterConfig': 'string',
        'mtu': 123,
        'jumboFrameCapable': True|False,
        'virtualGatewayId': 'string',
        'directConnectGatewayId': 'string',
        'routeFilterPrefixes': [
            {
                'cidr': 'string'
            },
        ],
        'bgpPeers': [
            {
                'bgpPeerId': 'string',
                'asn': 123,
                'authKey': 'string',
                'addressFamily': 'ipv4'|'ipv6',
                'amazonAddress': 'string',
                'customerAddress': 'string',
                'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                'bgpStatus': 'up'|'down',
                'awsDeviceV2': 'string'
            },
        ],
        'region': 'string',
        'awsDeviceV2': 'string'
    }
    
    
    :returns: 
    confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
    verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
    pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
    available : A virtual interface that is able to forward traffic.
    down : A virtual interface that is BGP down.
    deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
    deleted : A virtual interface that cannot forward traffic.
    rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
    
    """
    pass

