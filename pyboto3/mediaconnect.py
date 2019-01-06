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

def add_flow_outputs(FlowArn=None, Outputs=None):
    """
    Adds outputs to an existing flow. You can create up to 20 outputs per flow.
    See also: AWS API Documentation
    
    
    :example: response = client.add_flow_outputs(
        FlowArn='string',
        Outputs=[
            {
                'Description': 'string',
                'Destination': 'string',
                'Encryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'KeyType': 'static-key',
                    'RoleArn': 'string',
                    'SecretArn': 'string'
                },
                'MaxLatency': 123,
                'Name': 'string',
                'Port': 123,
                'Protocol': 'zixi-push'|'rtp-fec'|'rtp',
                'SmoothingLatency': 123,
                'StreamId': 'string'
            },
        ]
    )
    
    
    :type FlowArn: string
    :param FlowArn: [REQUIRED] The flow that you want to add outputs to.

    :type Outputs: list
    :param Outputs: [REQUIRED] A list of outputs that you want to add.
            (dict) -- The output that you want to add to this flow.
            Description (string) -- A description of the output. This description appears only on the AWS Elemental MediaConnect console and will not be seen by the end user.
            Destination (string) -- [REQUIRED] The IP address from which video will be sent to output destinations.
            Encryption (dict) -- The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
            Algorithm (string) -- [REQUIRED] The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
            KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
            RoleArn (string) -- [REQUIRED] The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
            SecretArn (string) -- [REQUIRED] The ARN that was assigned to the secret that you created in AWS Secrets Manager to store the encryption key.
            MaxLatency (integer) -- The maximum latency in milliseconds for Zixi-based streams.
            Name (string) -- The name of the output. This value must be unique within the current flow.
            Port (integer) -- [REQUIRED] The port to use when content is distributed to this output.
            Protocol (string) -- [REQUIRED] The protocol to use for the output.
            SmoothingLatency (integer) -- The smoothing latency in milliseconds for RTP and RTP-FEC streams.
            StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.
            

    :rtype: dict
    :return: {
        'FlowArn': 'string',
        'Outputs': [
            {
                'Description': 'string',
                'Destination': 'string',
                'Encryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'KeyType': 'static-key',
                    'RoleArn': 'string',
                    'SecretArn': 'string'
                },
                'EntitlementArn': 'string',
                'MediaLiveInputArn': 'string',
                'Name': 'string',
                'OutputArn': 'string',
                'Port': 123,
                'Transport': {
                    'MaxBitrate': 123,
                    'MaxLatency': 123,
                    'Protocol': 'zixi-push'|'rtp-fec'|'rtp',
                    'SmoothingLatency': 123,
                    'StreamId': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    (dict) -- AWS Elemental MediaConnect added the outputs successfully.
    FlowArn (string) -- The ARN of the flow that these outputs were added to.
    Outputs (list) -- The details of the newly added outputs.
    (dict) -- The settings for an output.
    Description (string) -- A description of the output.
    Destination (string) -- The address where you want to send the output.
    Encryption (dict) -- The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
    KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
    SecretArn (string) -- The ARN that was assigned to the secret that you created in AWS Secrets Manager to store the encryption key.
    
    
    EntitlementArn (string) -- The ARN of the entitlement on the originator''s flow. This value is relevant only on entitled flows.
    MediaLiveInputArn (string) -- The input ARN of the AWS Elemental MediaLive channel. This parameter is relevant only for outputs that were added by creating a MediaLive input.
    Name (string) -- The name of the output. This value must be unique within the current flow.
    OutputArn (string) -- The ARN of the output.
    Port (integer) -- The port to use when content is distributed to this output.
    Transport (dict) -- Attributes related to the transport stream that are used in the output.
    MaxBitrate (integer) -- The smoothing max bitrate for RTP and RTP-FEC streams.
    MaxLatency (integer) -- The maximum latency in milliseconds for Zixi-based streams.
    Protocol (string) -- The protocol that is used by the source or output.
    SmoothingLatency (integer) -- The smoothing latency in milliseconds for RTP and RTP-FEC streams.
    StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.
    
    
    
    
    
    
    
    
    
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

def create_flow(AvailabilityZone=None, Entitlements=None, Name=None, Outputs=None, Source=None):
    """
    Creates a new flow. The request must include one source. The request optionally can include outputs (up to 20) and entitlements (up to 50).
    See also: AWS API Documentation
    
    
    :example: response = client.create_flow(
        AvailabilityZone='string',
        Entitlements=[
            {
                'Description': 'string',
                'Encryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'KeyType': 'static-key',
                    'RoleArn': 'string',
                    'SecretArn': 'string'
                },
                'Name': 'string',
                'Subscribers': [
                    'string',
                ]
            },
        ],
        Name='string',
        Outputs=[
            {
                'Description': 'string',
                'Destination': 'string',
                'Encryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'KeyType': 'static-key',
                    'RoleArn': 'string',
                    'SecretArn': 'string'
                },
                'MaxLatency': 123,
                'Name': 'string',
                'Port': 123,
                'Protocol': 'zixi-push'|'rtp-fec'|'rtp',
                'SmoothingLatency': 123,
                'StreamId': 'string'
            },
        ],
        Source={
            'Decryption': {
                'Algorithm': 'aes128'|'aes192'|'aes256',
                'KeyType': 'static-key',
                'RoleArn': 'string',
                'SecretArn': 'string'
            },
            'Description': 'string',
            'EntitlementArn': 'string',
            'IngestPort': 123,
            'MaxBitrate': 123,
            'MaxLatency': 123,
            'Name': 'string',
            'Protocol': 'zixi-push'|'rtp-fec'|'rtp',
            'StreamId': 'string',
            'WhitelistCidr': 'string'
        }
    )
    
    
    :type AvailabilityZone: string
    :param AvailabilityZone: The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS Region.

    :type Entitlements: list
    :param Entitlements: The entitlements that you want to grant on a flow.
            (dict) -- The entitlements that you want to grant on a flow.
            Description (string) -- A description of the entitlement. This description appears only on the AWS Elemental MediaConnect console and will not be seen by the subscriber or end user.
            Encryption (dict) -- The type of encryption that will be used on the output that is associated with this entitlement.
            Algorithm (string) -- [REQUIRED] The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
            KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
            RoleArn (string) -- [REQUIRED] The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
            SecretArn (string) -- [REQUIRED] The ARN that was assigned to the secret that you created in AWS Secrets Manager to store the encryption key.
            Name (string) -- The name of the entitlement. This value must be unique within the current flow.
            Subscribers (list) -- [REQUIRED] The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flows using your content as the source.
            (string) --
            
            

    :type Name: string
    :param Name: [REQUIRED] The name of the flow.

    :type Outputs: list
    :param Outputs: The outputs that you want to add to this flow.
            (dict) -- The output that you want to add to this flow.
            Description (string) -- A description of the output. This description appears only on the AWS Elemental MediaConnect console and will not be seen by the end user.
            Destination (string) -- [REQUIRED] The IP address from which video will be sent to output destinations.
            Encryption (dict) -- The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
            Algorithm (string) -- [REQUIRED] The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
            KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
            RoleArn (string) -- [REQUIRED] The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
            SecretArn (string) -- [REQUIRED] The ARN that was assigned to the secret that you created in AWS Secrets Manager to store the encryption key.
            MaxLatency (integer) -- The maximum latency in milliseconds for Zixi-based streams.
            Name (string) -- The name of the output. This value must be unique within the current flow.
            Port (integer) -- [REQUIRED] The port to use when content is distributed to this output.
            Protocol (string) -- [REQUIRED] The protocol to use for the output.
            SmoothingLatency (integer) -- The smoothing latency in milliseconds for RTP and RTP-FEC streams.
            StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.
            

    :type Source: dict
    :param Source: [REQUIRED] The settings for the source of the flow.
            Decryption (dict) -- The type of encryption that is used on the content ingested from this source.
            Algorithm (string) -- [REQUIRED] The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
            KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
            RoleArn (string) -- [REQUIRED] The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
            SecretArn (string) -- [REQUIRED] The ARN that was assigned to the secret that you created in AWS Secrets Manager to store the encryption key.
            Description (string) -- A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
            EntitlementArn (string) -- The ARN of the entitlement that allows you to subscribe to this flow. The entitlement is set by the flow originator, and the ARN is generated as part of the originator's flow.
            IngestPort (integer) -- The port that the flow will be listening on for incoming content.
            MaxBitrate (integer) -- The smoothing max bitrate for RTP and RTP-FEC streams.
            MaxLatency (integer) -- The maximum latency in milliseconds for Zixi-based streams.
            Name (string) -- The name of the source.
            Protocol (string) -- The protocol that is used by the source.
            StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.
            WhitelistCidr (string) -- The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
            

    :rtype: dict
    :return: {
        'Flow': {
            'AvailabilityZone': 'string',
            'Description': 'string',
            'EgressIp': 'string',
            'Entitlements': [
                {
                    'Description': 'string',
                    'Encryption': {
                        'Algorithm': 'aes128'|'aes192'|'aes256',
                        'KeyType': 'static-key',
                        'RoleArn': 'string',
                        'SecretArn': 'string'
                    },
                    'EntitlementArn': 'string',
                    'Name': 'string',
                    'Subscribers': [
                        'string',
                    ]
                },
            ],
            'FlowArn': 'string',
            'Name': 'string',
            'Outputs': [
                {
                    'Description': 'string',
                    'Destination': 'string',
                    'Encryption': {
                        'Algorithm': 'aes128'|'aes192'|'aes256',
                        'KeyType': 'static-key',
                        'RoleArn': 'string',
                        'SecretArn': 'string'
                    },
                    'EntitlementArn': 'string',
                    'MediaLiveInputArn': 'string',
                    'Name': 'string',
                    'OutputArn': 'string',
                    'Port': 123,
                    'Transport': {
                        'MaxBitrate': 123,
                        'MaxLatency': 123,
                        'Protocol': 'zixi-push'|'rtp-fec'|'rtp',
                        'SmoothingLatency': 123,
                        'StreamId': 'string'
                    }
                },
            ],
            'Source': {
                'Decryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'KeyType': 'static-key',
                    'RoleArn': 'string',
                    'SecretArn': 'string'
                },
                'Description': 'string',
                'EntitlementArn': 'string',
                'IngestIp': 'string',
                'IngestPort': 123,
                'Name': 'string',
                'SourceArn': 'string',
                'Transport': {
                    'MaxBitrate': 123,
                    'MaxLatency': 123,
                    'Protocol': 'zixi-push'|'rtp-fec'|'rtp',
                    'SmoothingLatency': 123,
                    'StreamId': 'string'
                },
                'WhitelistCidr': 'string'
            },
            'Status': 'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'|'STOPPING'|'ERROR'
        }
    }
    
    
    :returns: 
    (dict) -- AWS Elemental MediaConnect created the new flow successfully.
    Flow (dict) -- The settings for a flow, including its source, outputs, and entitlements.
    AvailabilityZone (string) -- The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS.
    Description (string) -- A description of the flow. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
    EgressIp (string) -- The IP address from which video will be sent to output destinations.
    Entitlements (list) -- The entitlements in this flow.
    (dict) -- The settings for a flow entitlement.
    Description (string) -- A description of the entitlement.
    Encryption (dict) -- The type of encryption that will be used on the output that is associated with this entitlement.
    Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
    KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
    SecretArn (string) -- The ARN that was assigned to the secret that you created in AWS Secrets Manager to store the encryption key.
    
    
    EntitlementArn (string) -- The ARN of the entitlement.
    Name (string) -- The name of the entitlement.
    Subscribers (list) -- The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.
    (string) --
    
    
    
    
    
    
    FlowArn (string) -- The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.
    Name (string) -- The name of the flow.
    Outputs (list) -- The outputs in this flow.
    (dict) -- The settings for an output.
    Description (string) -- A description of the output.
    Destination (string) -- The address where you want to send the output.
    Encryption (dict) -- The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
    KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
    SecretArn (string) -- The ARN that was assigned to the secret that you created in AWS Secrets Manager to store the encryption key.
    
    
    EntitlementArn (string) -- The ARN of the entitlement on the originator''s flow. This value is relevant only on entitled flows.
    MediaLiveInputArn (string) -- The input ARN of the AWS Elemental MediaLive channel. This parameter is relevant only for outputs that were added by creating a MediaLive input.
    Name (string) -- The name of the output. This value must be unique within the current flow.
    OutputArn (string) -- The ARN of the output.
    Port (integer) -- The port to use when content is distributed to this output.
    Transport (dict) -- Attributes related to the transport stream that are used in the output.
    MaxBitrate (integer) -- The smoothing max bitrate for RTP and RTP-FEC streams.
    MaxLatency (integer) -- The maximum latency in milliseconds for Zixi-based streams.
    Protocol (string) -- The protocol that is used by the source or output.
    SmoothingLatency (integer) -- The smoothing latency in milliseconds for RTP and RTP-FEC streams.
    StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.
    
    
    
    
    
    
    Source (dict) -- The settings for the source of the flow.
    Decryption (dict) -- The type of encryption that is used on the content ingested from this source.
    Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
    KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
    SecretArn (string) -- The ARN that was assigned to the secret that you created in AWS Secrets Manager to store the encryption key.
    
    
    Description (string) -- A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
    EntitlementArn (string) -- The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account. The entitlement is set by the content originator and the ARN is generated as part of the originator's flow.
    IngestIp (string) -- The IP address that the flow will be listening on for incoming content.
    IngestPort (integer) -- The port that the flow will be listening on for incoming content.
    Name (string) -- The name of the source.
    SourceArn (string) -- The ARN of the source.
    Transport (dict) -- Attributes related to the transport stream that are used in the source.
    MaxBitrate (integer) -- The smoothing max bitrate for RTP and RTP-FEC streams.
    MaxLatency (integer) -- The maximum latency in milliseconds for Zixi-based streams.
    Protocol (string) -- The protocol that is used by the source or output.
    SmoothingLatency (integer) -- The smoothing latency in milliseconds for RTP and RTP-FEC streams.
    StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.
    
    
    WhitelistCidr (string) -- The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
    
    
    Status (string) -- The current status of the flow.
    
    
    
    
    
    """
    pass

def delete_flow(FlowArn=None):
    """
    Deletes a flow. Before you can delete a flow, you must stop the flow.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_flow(
        FlowArn='string'
    )
    
    
    :type FlowArn: string
    :param FlowArn: [REQUIRED] The ARN of the flow that you want to delete.

    :rtype: dict
    :return: {
        'FlowArn': 'string',
        'Status': 'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'|'STOPPING'|'ERROR'
    }
    
    
    """
    pass

def describe_flow(FlowArn=None):
    """
    Displays the details of a flow. The response includes the flow ARN, name, and Availability Zone, as well as details about the source, outputs, and entitlements.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_flow(
        FlowArn='string'
    )
    
    
    :type FlowArn: string
    :param FlowArn: [REQUIRED] The ARN of the flow that you want to describe.

    :rtype: dict
    :return: {
        'Flow': {
            'AvailabilityZone': 'string',
            'Description': 'string',
            'EgressIp': 'string',
            'Entitlements': [
                {
                    'Description': 'string',
                    'Encryption': {
                        'Algorithm': 'aes128'|'aes192'|'aes256',
                        'KeyType': 'static-key',
                        'RoleArn': 'string',
                        'SecretArn': 'string'
                    },
                    'EntitlementArn': 'string',
                    'Name': 'string',
                    'Subscribers': [
                        'string',
                    ]
                },
            ],
            'FlowArn': 'string',
            'Name': 'string',
            'Outputs': [
                {
                    'Description': 'string',
                    'Destination': 'string',
                    'Encryption': {
                        'Algorithm': 'aes128'|'aes192'|'aes256',
                        'KeyType': 'static-key',
                        'RoleArn': 'string',
                        'SecretArn': 'string'
                    },
                    'EntitlementArn': 'string',
                    'MediaLiveInputArn': 'string',
                    'Name': 'string',
                    'OutputArn': 'string',
                    'Port': 123,
                    'Transport': {
                        'MaxBitrate': 123,
                        'MaxLatency': 123,
                        'Protocol': 'zixi-push'|'rtp-fec'|'rtp',
                        'SmoothingLatency': 123,
                        'StreamId': 'string'
                    }
                },
            ],
            'Source': {
                'Decryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'KeyType': 'static-key',
                    'RoleArn': 'string',
                    'SecretArn': 'string'
                },
                'Description': 'string',
                'EntitlementArn': 'string',
                'IngestIp': 'string',
                'IngestPort': 123,
                'Name': 'string',
                'SourceArn': 'string',
                'Transport': {
                    'MaxBitrate': 123,
                    'MaxLatency': 123,
                    'Protocol': 'zixi-push'|'rtp-fec'|'rtp',
                    'SmoothingLatency': 123,
                    'StreamId': 'string'
                },
                'WhitelistCidr': 'string'
            },
            'Status': 'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'|'STOPPING'|'ERROR'
        },
        'Messages': {
            'Errors': [
                'string',
            ]
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

def grant_flow_entitlements(Entitlements=None, FlowArn=None):
    """
    Grants entitlements to an existing flow.
    See also: AWS API Documentation
    
    
    :example: response = client.grant_flow_entitlements(
        Entitlements=[
            {
                'Description': 'string',
                'Encryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'KeyType': 'static-key',
                    'RoleArn': 'string',
                    'SecretArn': 'string'
                },
                'Name': 'string',
                'Subscribers': [
                    'string',
                ]
            },
        ],
        FlowArn='string'
    )
    
    
    :type Entitlements: list
    :param Entitlements: [REQUIRED] The list of entitlements that you want to grant.
            (dict) -- The entitlements that you want to grant on a flow.
            Description (string) -- A description of the entitlement. This description appears only on the AWS Elemental MediaConnect console and will not be seen by the subscriber or end user.
            Encryption (dict) -- The type of encryption that will be used on the output that is associated with this entitlement.
            Algorithm (string) -- [REQUIRED] The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
            KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
            RoleArn (string) -- [REQUIRED] The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
            SecretArn (string) -- [REQUIRED] The ARN that was assigned to the secret that you created in AWS Secrets Manager to store the encryption key.
            Name (string) -- The name of the entitlement. This value must be unique within the current flow.
            Subscribers (list) -- [REQUIRED] The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flows using your content as the source.
            (string) --
            
            

    :type FlowArn: string
    :param FlowArn: [REQUIRED] The flow that you want to grant entitlements on.

    :rtype: dict
    :return: {
        'Entitlements': [
            {
                'Description': 'string',
                'Encryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'KeyType': 'static-key',
                    'RoleArn': 'string',
                    'SecretArn': 'string'
                },
                'EntitlementArn': 'string',
                'Name': 'string',
                'Subscribers': [
                    'string',
                ]
            },
        ],
        'FlowArn': 'string'
    }
    
    
    :returns: 
    (dict) -- AWS Elemental MediaConnect granted the entitlements successfully.
    Entitlements (list) -- The entitlements that were just granted.
    (dict) -- The settings for a flow entitlement.
    Description (string) -- A description of the entitlement.
    Encryption (dict) -- The type of encryption that will be used on the output that is associated with this entitlement.
    Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
    KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
    SecretArn (string) -- The ARN that was assigned to the secret that you created in AWS Secrets Manager to store the encryption key.
    
    
    EntitlementArn (string) -- The ARN of the entitlement.
    Name (string) -- The name of the entitlement.
    Subscribers (list) -- The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.
    (string) --
    
    
    
    
    
    
    FlowArn (string) -- The ARN of the flow that these entitlements were granted to.
    
    
    
    """
    pass

def list_entitlements(MaxResults=None, NextToken=None):
    """
    Displays a list of all entitlements that have been granted to this account. This request returns 20 results per page.
    See also: AWS API Documentation
    
    
    :example: response = client.list_entitlements(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return per API request. For example, you submit a ListEntitlements request with MaxResults set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a NextToken value that you can use to fetch the next batch of results.) The service might return fewer results than the MaxResults value. If MaxResults is not included in the request, the service defaults to pagination with a maximum of 20 results per page.

    :type NextToken: string
    :param NextToken: The token that identifies which batch of results that you want to see. For example, you submit a ListEntitlements request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a NextToken value. To see the next batch of results, you can submit the ListEntitlements request a second time and specify the NextToken value.

    :rtype: dict
    :return: {
        'Entitlements': [
            {
                'EntitlementArn': 'string',
                'EntitlementName': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (dict) -- AWS Elemental MediaConnect returned the list of entitlements successfully.
    Entitlements (list) -- A list of entitlements that have been granted to you from other AWS accounts.
    (dict) -- An entitlement that has been granted to you from other AWS accounts.
    EntitlementArn (string) -- The ARN of the entitlement.
    EntitlementName (string) -- The name of the entitlement.
    
    
    
    
    NextToken (string) -- The token that identifies which batch of results that you want to see. For example, you submit a ListEntitlements request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a NextToken value. To see the next batch of results, you can submit the ListEntitlements request a second time and specify the NextToken value.
    
    
    
    """
    pass

def list_flows(MaxResults=None, NextToken=None):
    """
    Displays a list of flows that are associated with this account. This request returns a paginated result.
    See also: AWS API Documentation
    
    
    :example: response = client.list_flows(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return per API request. For example, you submit a ListFlows request with MaxResults set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a NextToken value that you can use to fetch the next batch of results.) The service might return fewer results than the MaxResults value. If MaxResults is not included in the request, the service defaults to pagination with a maximum of 10 results per page.

    :type NextToken: string
    :param NextToken: The token that identifies which batch of results that you want to see. For example, you submit a ListFlows request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a NextToken value. To see the next batch of results, you can submit the ListFlows request a second time and specify the NextToken value.

    :rtype: dict
    :return: {
        'Flows': [
            {
                'AvailabilityZone': 'string',
                'Description': 'string',
                'FlowArn': 'string',
                'Name': 'string',
                'SourceType': 'OWNED'|'ENTITLED',
                'Status': 'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'|'STOPPING'|'ERROR'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (dict) -- AWS Elemental MediaConnect returned the list of flows successfully.
    Flows (list) -- A list of flow summaries.
    (dict) -- Provides a summary of a flow, including its ARN, Availability Zone, and source type.
    AvailabilityZone (string) -- The Availability Zone that the flow was created in.
    Description (string) -- A description of the flow.
    FlowArn (string) -- The ARN of the flow.
    Name (string) -- The name of the flow.
    SourceType (string) -- The type of source. This value is either owned (originated somewhere other than an AWS Elemental MediaConnect flow owned by another AWS account) or entitled (originated at an AWS Elemental MediaConnect flow owned by another AWS account).
    Status (string) -- The current status of the flow.
    
    
    
    
    NextToken (string) -- The token that identifies which batch of results that you want to see. For example, you submit a ListFlows request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a NextToken value. To see the next batch of results, you can submit the ListFlows request a second time and specify the NextToken value.
    
    
    
    """
    pass

def remove_flow_output(FlowArn=None, OutputArn=None):
    """
    Removes an output from an existing flow. This request can be made only on an output that does not have an entitlement associated with it. If the output has an entitlement, you must revoke the entitlement instead. When an entitlement is revoked from a flow, the service automatically removes the associated output.
    See also: AWS API Documentation
    
    
    :example: response = client.remove_flow_output(
        FlowArn='string',
        OutputArn='string'
    )
    
    
    :type FlowArn: string
    :param FlowArn: [REQUIRED] The flow that you want to remove an output from.

    :type OutputArn: string
    :param OutputArn: [REQUIRED] The ARN of the output that you want to remove.

    :rtype: dict
    :return: {
        'FlowArn': 'string',
        'OutputArn': 'string'
    }
    
    
    :returns: 
    (dict) -- output successfully removed from flow configuration.
    FlowArn (string) -- The ARN of the flow that is associated with the output you removed.
    OutputArn (string) -- The ARN of the output that was removed.
    
    
    
    """
    pass

def revoke_flow_entitlement(EntitlementArn=None, FlowArn=None):
    """
    Revokes an entitlement from a flow. Once an entitlement is revoked, the content becomes unavailable to the subscriber and the associated output is removed.
    See also: AWS API Documentation
    
    
    :example: response = client.revoke_flow_entitlement(
        EntitlementArn='string',
        FlowArn='string'
    )
    
    
    :type EntitlementArn: string
    :param EntitlementArn: [REQUIRED] The ARN of the entitlement that you want to revoke.

    :type FlowArn: string
    :param FlowArn: [REQUIRED] The flow that you want to revoke an entitlement from.

    :rtype: dict
    :return: {
        'EntitlementArn': 'string',
        'FlowArn': 'string'
    }
    
    
    :returns: 
    (dict) -- AWS Elemental MediaConnect revoked the entitlement successfully.
    EntitlementArn (string) -- The ARN of the entitlement that was revoked.
    FlowArn (string) -- The ARN of the flow that the entitlement was revoked from.
    
    
    
    """
    pass

def start_flow(FlowArn=None):
    """
    Starts a flow.
    See also: AWS API Documentation
    
    
    :example: response = client.start_flow(
        FlowArn='string'
    )
    
    
    :type FlowArn: string
    :param FlowArn: [REQUIRED] The ARN of the flow that you want to start.

    :rtype: dict
    :return: {
        'FlowArn': 'string',
        'Status': 'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'|'STOPPING'|'ERROR'
    }
    
    
    """
    pass

def stop_flow(FlowArn=None):
    """
    Stops a flow.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_flow(
        FlowArn='string'
    )
    
    
    :type FlowArn: string
    :param FlowArn: [REQUIRED] The ARN of the flow that you want to stop.

    :rtype: dict
    :return: {
        'FlowArn': 'string',
        'Status': 'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'|'STOPPING'|'ERROR'
    }
    
    
    """
    pass

def update_flow_entitlement(Description=None, Encryption=None, EntitlementArn=None, FlowArn=None, Subscribers=None):
    """
    You can change an entitlement's description, subscribers, and encryption. If you change the subscribers, the service will remove the outputs that are are used by the subscribers that are removed.
    See also: AWS API Documentation
    
    
    :example: response = client.update_flow_entitlement(
        Description='string',
        Encryption={
            'Algorithm': 'aes128'|'aes192'|'aes256',
            'KeyType': 'static-key',
            'RoleArn': 'string',
            'SecretArn': 'string'
        },
        EntitlementArn='string',
        FlowArn='string',
        Subscribers=[
            'string',
        ]
    )
    
    
    :type Description: string
    :param Description: A description of the entitlement. This description appears only on the AWS Elemental MediaConnect console and will not be seen by the subscriber or end user.

    :type Encryption: dict
    :param Encryption: The type of encryption that will be used on the output associated with this entitlement.
            Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
            KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
            RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
            SecretArn (string) -- The ARN that was assigned to the secret that you created in AWS Secrets Manager to store the encryption key.
            

    :type EntitlementArn: string
    :param EntitlementArn: [REQUIRED] The ARN of the entitlement that you want to update.

    :type FlowArn: string
    :param FlowArn: [REQUIRED] The flow that is associated with the entitlement that you want to update.

    :type Subscribers: list
    :param Subscribers: The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.
            (string) --
            

    :rtype: dict
    :return: {
        'Entitlement': {
            'Description': 'string',
            'Encryption': {
                'Algorithm': 'aes128'|'aes192'|'aes256',
                'KeyType': 'static-key',
                'RoleArn': 'string',
                'SecretArn': 'string'
            },
            'EntitlementArn': 'string',
            'Name': 'string',
            'Subscribers': [
                'string',
            ]
        },
        'FlowArn': 'string'
    }
    
    
    :returns: 
    (dict) -- AWS Elemental MediaConnect updated the entitlement successfully.
    Entitlement (dict) -- The settings for a flow entitlement.
    Description (string) -- A description of the entitlement.
    Encryption (dict) -- The type of encryption that will be used on the output that is associated with this entitlement.
    Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
    KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
    SecretArn (string) -- The ARN that was assigned to the secret that you created in AWS Secrets Manager to store the encryption key.
    
    
    EntitlementArn (string) -- The ARN of the entitlement.
    Name (string) -- The name of the entitlement.
    Subscribers (list) -- The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.
    (string) --
    
    
    
    
    FlowArn (string) -- The ARN of the flow that this entitlement was granted on.
    
    
    
    """
    pass

def update_flow_output(Description=None, Destination=None, Encryption=None, FlowArn=None, MaxLatency=None, OutputArn=None, Port=None, Protocol=None, SmoothingLatency=None, StreamId=None):
    """
    Updates an existing flow output.
    See also: AWS API Documentation
    
    
    :example: response = client.update_flow_output(
        Description='string',
        Destination='string',
        Encryption={
            'Algorithm': 'aes128'|'aes192'|'aes256',
            'KeyType': 'static-key',
            'RoleArn': 'string',
            'SecretArn': 'string'
        },
        FlowArn='string',
        MaxLatency=123,
        OutputArn='string',
        Port=123,
        Protocol='zixi-push'|'rtp-fec'|'rtp',
        SmoothingLatency=123,
        StreamId='string'
    )
    
    
    :type Description: string
    :param Description: A description of the output. This description appears only on the AWS Elemental MediaConnect console and will not be seen by the end user.

    :type Destination: string
    :param Destination: The IP address where you want to send the output.

    :type Encryption: dict
    :param Encryption: The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
            Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
            KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
            RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
            SecretArn (string) -- The ARN that was assigned to the secret that you created in AWS Secrets Manager to store the encryption key.
            

    :type FlowArn: string
    :param FlowArn: [REQUIRED] The flow that is associated with the output that you want to update.

    :type MaxLatency: integer
    :param MaxLatency: The maximum latency in milliseconds for Zixi-based streams.

    :type OutputArn: string
    :param OutputArn: [REQUIRED] The ARN of the output that you want to update.

    :type Port: integer
    :param Port: The port to use when content is distributed to this output.

    :type Protocol: string
    :param Protocol: The protocol to use for the output.

    :type SmoothingLatency: integer
    :param SmoothingLatency: The smoothing latency in milliseconds for RTP and RTP-FEC streams.

    :type StreamId: string
    :param StreamId: The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.

    :rtype: dict
    :return: {
        'FlowArn': 'string',
        'Output': {
            'Description': 'string',
            'Destination': 'string',
            'Encryption': {
                'Algorithm': 'aes128'|'aes192'|'aes256',
                'KeyType': 'static-key',
                'RoleArn': 'string',
                'SecretArn': 'string'
            },
            'EntitlementArn': 'string',
            'MediaLiveInputArn': 'string',
            'Name': 'string',
            'OutputArn': 'string',
            'Port': 123,
            'Transport': {
                'MaxBitrate': 123,
                'MaxLatency': 123,
                'Protocol': 'zixi-push'|'rtp-fec'|'rtp',
                'SmoothingLatency': 123,
                'StreamId': 'string'
            }
        }
    }
    
    
    :returns: 
    (dict) -- AWS Elemental MediaConnect updated the output successfully.
    FlowArn (string) -- The ARN of the flow that is associated with the updated output.
    Output (dict) -- The settings for an output.
    Description (string) -- A description of the output.
    Destination (string) -- The address where you want to send the output.
    Encryption (dict) -- The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
    KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
    SecretArn (string) -- The ARN that was assigned to the secret that you created in AWS Secrets Manager to store the encryption key.
    
    
    EntitlementArn (string) -- The ARN of the entitlement on the originator''s flow. This value is relevant only on entitled flows.
    MediaLiveInputArn (string) -- The input ARN of the AWS Elemental MediaLive channel. This parameter is relevant only for outputs that were added by creating a MediaLive input.
    Name (string) -- The name of the output. This value must be unique within the current flow.
    OutputArn (string) -- The ARN of the output.
    Port (integer) -- The port to use when content is distributed to this output.
    Transport (dict) -- Attributes related to the transport stream that are used in the output.
    MaxBitrate (integer) -- The smoothing max bitrate for RTP and RTP-FEC streams.
    MaxLatency (integer) -- The maximum latency in milliseconds for Zixi-based streams.
    Protocol (string) -- The protocol that is used by the source or output.
    SmoothingLatency (integer) -- The smoothing latency in milliseconds for RTP and RTP-FEC streams.
    StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.
    
    
    
    
    
    
    
    """
    pass

def update_flow_source(Decryption=None, Description=None, EntitlementArn=None, FlowArn=None, IngestPort=None, MaxBitrate=None, MaxLatency=None, Protocol=None, SourceArn=None, StreamId=None, WhitelistCidr=None):
    """
    Updates the source of a flow.
    See also: AWS API Documentation
    
    
    :example: response = client.update_flow_source(
        Decryption={
            'Algorithm': 'aes128'|'aes192'|'aes256',
            'KeyType': 'static-key',
            'RoleArn': 'string',
            'SecretArn': 'string'
        },
        Description='string',
        EntitlementArn='string',
        FlowArn='string',
        IngestPort=123,
        MaxBitrate=123,
        MaxLatency=123,
        Protocol='zixi-push'|'rtp-fec'|'rtp',
        SourceArn='string',
        StreamId='string',
        WhitelistCidr='string'
    )
    
    
    :type Decryption: dict
    :param Decryption: The type of encryption used on the content ingested from this source.
            Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
            KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
            RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
            SecretArn (string) -- The ARN that was assigned to the secret that you created in AWS Secrets Manager to store the encryption key.
            

    :type Description: string
    :param Description: A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.

    :type EntitlementArn: string
    :param EntitlementArn: The ARN of the entitlement that allows you to subscribe to this flow. The entitlement is set by the flow originator, and the ARN is generated as part of the originator's flow.

    :type FlowArn: string
    :param FlowArn: [REQUIRED] The flow that is associated with the source that you want to update.

    :type IngestPort: integer
    :param IngestPort: The port that the flow will be listening on for incoming content.

    :type MaxBitrate: integer
    :param MaxBitrate: The smoothing max bitrate for RTP and RTP-FEC streams.

    :type MaxLatency: integer
    :param MaxLatency: The maximum latency in milliseconds for Zixi-based streams.

    :type Protocol: string
    :param Protocol: The protocol that is used by the source.

    :type SourceArn: string
    :param SourceArn: [REQUIRED] The ARN of the source that you want to update.

    :type StreamId: string
    :param StreamId: The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.

    :type WhitelistCidr: string
    :param WhitelistCidr: The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

    :rtype: dict
    :return: {
        'FlowArn': 'string',
        'Source': {
            'Decryption': {
                'Algorithm': 'aes128'|'aes192'|'aes256',
                'KeyType': 'static-key',
                'RoleArn': 'string',
                'SecretArn': 'string'
            },
            'Description': 'string',
            'EntitlementArn': 'string',
            'IngestIp': 'string',
            'IngestPort': 123,
            'Name': 'string',
            'SourceArn': 'string',
            'Transport': {
                'MaxBitrate': 123,
                'MaxLatency': 123,
                'Protocol': 'zixi-push'|'rtp-fec'|'rtp',
                'SmoothingLatency': 123,
                'StreamId': 'string'
            },
            'WhitelistCidr': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- AWS Elemental MediaConnect updated the flow successfully.
    FlowArn (string) -- The ARN of the flow that you want to update.
    Source (dict) -- The settings for the source of the flow.
    Decryption (dict) -- The type of encryption that is used on the content ingested from this source.
    Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
    KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
    SecretArn (string) -- The ARN that was assigned to the secret that you created in AWS Secrets Manager to store the encryption key.
    
    
    Description (string) -- A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
    EntitlementArn (string) -- The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account. The entitlement is set by the content originator and the ARN is generated as part of the originator's flow.
    IngestIp (string) -- The IP address that the flow will be listening on for incoming content.
    IngestPort (integer) -- The port that the flow will be listening on for incoming content.
    Name (string) -- The name of the source.
    SourceArn (string) -- The ARN of the source.
    Transport (dict) -- Attributes related to the transport stream that are used in the source.
    MaxBitrate (integer) -- The smoothing max bitrate for RTP and RTP-FEC streams.
    MaxLatency (integer) -- The maximum latency in milliseconds for Zixi-based streams.
    Protocol (string) -- The protocol that is used by the source or output.
    SmoothingLatency (integer) -- The smoothing latency in milliseconds for RTP and RTP-FEC streams.
    StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.
    
    
    WhitelistCidr (string) -- The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
    
    
    
    
    
    """
    pass

