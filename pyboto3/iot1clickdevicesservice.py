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

def claim_devices_by_claim_code(ClaimCode=None):
    """
    Adds device(s) to your account (i.e., claim one or more devices) if and only if you received a claim code with the device(s).
    See also: AWS API Documentation
    
    
    :example: response = client.claim_devices_by_claim_code(
        ClaimCode='string'
    )
    
    
    :type ClaimCode: string
    :param ClaimCode: [REQUIRED]
            The claim code, starting with 'C-', as provided by the device manufacturer.
            

    :rtype: dict
    :return: {
        'ClaimCode': 'string',
        'Total': 123
    }
    
    
    """
    pass

def describe_device(DeviceId=None):
    """
    Given a device ID, returns a DescribeDeviceResponse object describing the details of the device.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_device(
        DeviceId='string'
    )
    
    
    :type DeviceId: string
    :param DeviceId: [REQUIRED]
            The unique identifier of the device.
            

    :rtype: dict
    :return: {
        'DeviceDescription': {
            'Attributes': {
                'string': 'string'
            },
            'DeviceId': 'string',
            'Enabled': True|False,
            'RemainingLife': 123.0,
            'Type': 'string'
        }
    }
    
    
    """
    pass

def finalize_device_claim(DeviceId=None):
    """
    Given a device ID, finalizes the claim request for the associated device.
    See also: AWS API Documentation
    
    
    :example: response = client.finalize_device_claim(
        DeviceId='string'
    )
    
    
    :type DeviceId: string
    :param DeviceId: [REQUIRED]
            The unique identifier of the device.
            

    :rtype: dict
    :return: {
        'State': 'string'
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

def get_device_methods(DeviceId=None):
    """
    Given a device ID, returns the invokable methods associated with the device.
    See also: AWS API Documentation
    
    
    :example: response = client.get_device_methods(
        DeviceId='string'
    )
    
    
    :type DeviceId: string
    :param DeviceId: [REQUIRED]
            The unique identifier of the device.
            

    :rtype: dict
    :return: {
        'DeviceMethods': [
            {
                'DeviceType': 'string',
                'MethodName': 'string'
            },
        ]
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

def initiate_device_claim(DeviceId=None):
    """
    Given a device ID, initiates a claim request for the associated device.
    See also: AWS API Documentation
    
    
    :example: response = client.initiate_device_claim(
        DeviceId='string'
    )
    
    
    :type DeviceId: string
    :param DeviceId: [REQUIRED]
            The unique identifier of the device.
            

    :rtype: dict
    :return: {
        'State': 'string'
    }
    
    
    """
    pass

def invoke_device_method(DeviceId=None, DeviceMethod=None, DeviceMethodParameters=None):
    """
    Given a device ID, issues a request to invoke a named device method (with possible parameters). See the "Example POST" code snippet below.
    See also: AWS API Documentation
    
    
    :example: response = client.invoke_device_method(
        DeviceId='string',
        DeviceMethod={
            'DeviceType': 'string',
            'MethodName': 'string'
        },
        DeviceMethodParameters='string'
    )
    
    
    :type DeviceId: string
    :param DeviceId: [REQUIRED]
            The unique identifier of the device.
            

    :type DeviceMethod: dict
    :param DeviceMethod: The device method to invoke.
            DeviceType (string) --The type of the device, such as 'button'.
            MethodName (string) --The name of the method applicable to the deviceType.
            

    :type DeviceMethodParameters: string
    :param DeviceMethodParameters: A JSON encoded string containing the device method request parameters.

    :rtype: dict
    :return: {
        'DeviceMethodResponse': 'string'
    }
    
    
    """
    pass

def list_device_events(DeviceId=None, FromTimeStamp=None, MaxResults=None, NextToken=None, ToTimeStamp=None):
    """
    Using a device ID, returns a DeviceEventsResponse object containing an array of events for the device.
    See also: AWS API Documentation
    
    
    :example: response = client.list_device_events(
        DeviceId='string',
        FromTimeStamp=datetime(2015, 1, 1),
        MaxResults=123,
        NextToken='string',
        ToTimeStamp=datetime(2015, 1, 1)
    )
    
    
    :type DeviceId: string
    :param DeviceId: [REQUIRED]
            The unique identifier of the device.
            

    :type FromTimeStamp: datetime
    :param FromTimeStamp: [REQUIRED]
            The start date for the device event query, in ISO8061 format. For example, 2018-03-28T15:45:12.880Z
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return per request. If not set, a default value of 100 is used.

    :type NextToken: string
    :param NextToken: The token to retrieve the next set of results.

    :type ToTimeStamp: datetime
    :param ToTimeStamp: [REQUIRED]
            The end date for the device event query, in ISO8061 format. For example, 2018-03-28T15:45:12.880Z
            

    :rtype: dict
    :return: {
        'Events': [
            {
                'Device': {
                    'Attributes': {},
                    'DeviceId': 'string',
                    'Type': 'string'
                },
                'StdEvent': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_devices(DeviceType=None, MaxResults=None, NextToken=None):
    """
    Lists the 1-Click compatible devices associated with your AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_devices(
        DeviceType='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type DeviceType: string
    :param DeviceType: The type of the device, such as 'button'.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return per request. If not set, a default value of 100 is used.

    :type NextToken: string
    :param NextToken: The token to retrieve the next set of results.

    :rtype: dict
    :return: {
        'Devices': [
            {
                'Attributes': {
                    'string': 'string'
                },
                'DeviceId': 'string',
                'Enabled': True|False,
                'RemainingLife': 123.0,
                'Type': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def unclaim_device(DeviceId=None):
    """
    Disassociates a device from your AWS account using its device ID.
    See also: AWS API Documentation
    
    
    :example: response = client.unclaim_device(
        DeviceId='string'
    )
    
    
    :type DeviceId: string
    :param DeviceId: [REQUIRED]
            The unique identifier of the device.
            

    :rtype: dict
    :return: {
        'State': 'string'
    }
    
    
    """
    pass

def update_device_state(DeviceId=None, Enabled=None):
    """
    Using a Boolean value (true or false), this operation enables or disables the device given a device ID.
    See also: AWS API Documentation
    
    
    :example: response = client.update_device_state(
        DeviceId='string',
        Enabled=True|False
    )
    
    
    :type DeviceId: string
    :param DeviceId: [REQUIRED]
            The unique identifier of the device.
            

    :type Enabled: boolean
    :param Enabled: If true, the device is enabled. If false, the device is disabled.

    :rtype: dict
    :return: {}
    
    
    """
    pass

