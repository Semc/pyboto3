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

def associate_device_with_placement(projectName=None, placementName=None, deviceId=None, deviceTemplateName=None):
    """
    Associates a physical device with a placement.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_device_with_placement(
        projectName='string',
        placementName='string',
        deviceId='string',
        deviceTemplateName='string'
    )
    
    
    :type projectName: string
    :param projectName: [REQUIRED]
            The name of the project containing the placement in which to associate the device.
            

    :type placementName: string
    :param placementName: [REQUIRED]
            The name of the placement in which to associate the device.
            

    :type deviceId: string
    :param deviceId: [REQUIRED]
            The ID of the physical device to be associated with the given placement in the project. Note that a mandatory 4 character prefix is required for all deviceId values.
            

    :type deviceTemplateName: string
    :param deviceTemplateName: [REQUIRED]
            The device template name to associate with the device ID.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
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

def create_placement(placementName=None, projectName=None, attributes=None):
    """
    Creates an empty placement.
    See also: AWS API Documentation
    
    
    :example: response = client.create_placement(
        placementName='string',
        projectName='string',
        attributes={
            'string': 'string'
        }
    )
    
    
    :type placementName: string
    :param placementName: [REQUIRED]
            The name of the placement to be created.
            

    :type projectName: string
    :param projectName: [REQUIRED]
            The name of the project in which to create the placement.
            

    :type attributes: dict
    :param attributes: Optional user-defined key/value pairs providing contextual data (such as location or function) for the placement.
            (string) --
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_project(projectName=None, description=None, placementTemplate=None):
    """
    Creates an empty project with a placement template. A project contains zero or more placements that adhere to the placement template defined in the project.
    See also: AWS API Documentation
    
    
    :example: response = client.create_project(
        projectName='string',
        description='string',
        placementTemplate={
            'defaultAttributes': {
                'string': 'string'
            },
            'deviceTemplates': {
                'string': {
                    'deviceType': 'string',
                    'callbackOverrides': {
                        'string': 'string'
                    }
                }
            }
        }
    )
    
    
    :type projectName: string
    :param projectName: [REQUIRED]
            The name of the project to create.
            

    :type description: string
    :param description: An optional description for the project.

    :type placementTemplate: dict
    :param placementTemplate: The schema defining the placement to be created. A placement template defines placement default attributes and device templates. You cannot add or remove device templates after the project has been created. However, you can update callbackOverrides for the device templates using the UpdateProject API.
            defaultAttributes (dict) --The default attributes (key/value pairs) to be applied to all placements using this template.
            (string) --
            (string) --
            
            deviceTemplates (dict) --An object specifying the DeviceTemplate for all placements using this ( PlacementTemplate ) template.
            (string) --
            (dict) --An object representing a device for a placement template (see PlacementTemplate ).
            deviceType (string) --The device type, which currently must be 'button' .
            callbackOverrides (dict) --An optional Lambda function to invoke instead of the default Lambda function provided by the placement template.
            (string) --
            (string) --
            
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_placement(placementName=None, projectName=None):
    """
    Deletes a placement. To delete a placement, it must not have any devices associated with it.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_placement(
        placementName='string',
        projectName='string'
    )
    
    
    :type placementName: string
    :param placementName: [REQUIRED]
            The name of the empty placement to delete.
            

    :type projectName: string
    :param projectName: [REQUIRED]
            The project containing the empty placement to delete.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_project(projectName=None):
    """
    Deletes a project. To delete a project, it must not have any placements associated with it.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_project(
        projectName='string'
    )
    
    
    :type projectName: string
    :param projectName: [REQUIRED]
            The name of the empty project to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_placement(placementName=None, projectName=None):
    """
    Describes a placement in a project.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_placement(
        placementName='string',
        projectName='string'
    )
    
    
    :type placementName: string
    :param placementName: [REQUIRED]
            The name of the placement within a project.
            

    :type projectName: string
    :param projectName: [REQUIRED]
            The project containing the placement to be described.
            

    :rtype: dict
    :return: {
        'placement': {
            'projectName': 'string',
            'placementName': 'string',
            'attributes': {
                'string': 'string'
            },
            'createdDate': datetime(2015, 1, 1),
            'updatedDate': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_project(projectName=None):
    """
    Returns an object describing a project.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_project(
        projectName='string'
    )
    
    
    :type projectName: string
    :param projectName: [REQUIRED]
            The name of the project to be described.
            

    :rtype: dict
    :return: {
        'project': {
            'projectName': 'string',
            'description': 'string',
            'createdDate': datetime(2015, 1, 1),
            'updatedDate': datetime(2015, 1, 1),
            'placementTemplate': {
                'defaultAttributes': {
                    'string': 'string'
                },
                'deviceTemplates': {
                    'string': {
                        'deviceType': 'string',
                        'callbackOverrides': {
                            'string': 'string'
                        }
                    }
                }
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def disassociate_device_from_placement(projectName=None, placementName=None, deviceTemplateName=None):
    """
    Removes a physical device from a placement.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_device_from_placement(
        projectName='string',
        placementName='string',
        deviceTemplateName='string'
    )
    
    
    :type projectName: string
    :param projectName: [REQUIRED]
            The name of the project that contains the placement.
            

    :type placementName: string
    :param placementName: [REQUIRED]
            The name of the placement that the device should be removed from.
            

    :type deviceTemplateName: string
    :param deviceTemplateName: [REQUIRED]
            The device ID that should be removed from the placement.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
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

def get_devices_in_placement(projectName=None, placementName=None):
    """
    Returns an object enumerating the devices in a placement.
    See also: AWS API Documentation
    
    
    :example: response = client.get_devices_in_placement(
        projectName='string',
        placementName='string'
    )
    
    
    :type projectName: string
    :param projectName: [REQUIRED]
            The name of the project containing the placement.
            

    :type placementName: string
    :param placementName: [REQUIRED]
            The name of the placement to get the devices from.
            

    :rtype: dict
    :return: {
        'devices': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
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

def list_placements(projectName=None, nextToken=None, maxResults=None):
    """
    Lists the placement(s) of a project.
    See also: AWS API Documentation
    
    
    :example: response = client.list_placements(
        projectName='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type projectName: string
    :param projectName: [REQUIRED]
            The project containing the placements to be listed.
            

    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return per request. If not set, a default value of 100 is used.

    :rtype: dict
    :return: {
        'placements': [
            {
                'projectName': 'string',
                'placementName': 'string',
                'createdDate': datetime(2015, 1, 1),
                'updatedDate': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_projects(nextToken=None, maxResults=None):
    """
    Lists the AWS IoT 1-Click project(s) associated with your AWS account and region.
    See also: AWS API Documentation
    
    
    :example: response = client.list_projects(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return per request. If not set, a default value of 100 is used.

    :rtype: dict
    :return: {
        'projects': [
            {
                'projectName': 'string',
                'createdDate': datetime(2015, 1, 1),
                'updatedDate': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def update_placement(placementName=None, projectName=None, attributes=None):
    """
    Updates a placement with the given attributes. To clear an attribute, pass an empty value (i.e., "").
    See also: AWS API Documentation
    
    
    :example: response = client.update_placement(
        placementName='string',
        projectName='string',
        attributes={
            'string': 'string'
        }
    )
    
    
    :type placementName: string
    :param placementName: [REQUIRED]
            The name of the placement to update.
            

    :type projectName: string
    :param projectName: [REQUIRED]
            The name of the project containing the placement to be updated.
            

    :type attributes: dict
    :param attributes: The user-defined object of attributes used to update the placement. The maximum number of key/value pairs is 50.
            (string) --
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_project(projectName=None, description=None, placementTemplate=None):
    """
    Updates a project associated with your AWS account and region. With the exception of device template names, you can pass just the values that need to be updated because the update request will change only the values that are provided. To clear a value, pass the empty string (i.e., "" ).
    See also: AWS API Documentation
    
    
    :example: response = client.update_project(
        projectName='string',
        description='string',
        placementTemplate={
            'defaultAttributes': {
                'string': 'string'
            },
            'deviceTemplates': {
                'string': {
                    'deviceType': 'string',
                    'callbackOverrides': {
                        'string': 'string'
                    }
                }
            }
        }
    )
    
    
    :type projectName: string
    :param projectName: [REQUIRED]
            The name of the project to be updated.
            

    :type description: string
    :param description: An optional user-defined description for the project.

    :type placementTemplate: dict
    :param placementTemplate: An object defining the project update. Once a project has been created, you cannot add device template names to the project. However, for a given placementTemplate , you can update the associated callbackOverrides for the device definition using this API.
            defaultAttributes (dict) --The default attributes (key/value pairs) to be applied to all placements using this template.
            (string) --
            (string) --
            
            deviceTemplates (dict) --An object specifying the DeviceTemplate for all placements using this ( PlacementTemplate ) template.
            (string) --
            (dict) --An object representing a device for a placement template (see PlacementTemplate ).
            deviceType (string) --The device type, which currently must be 'button' .
            callbackOverrides (dict) --An optional Lambda function to invoke instead of the default Lambda function provided by the placement template.
            (string) --
            (string) --
            
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

