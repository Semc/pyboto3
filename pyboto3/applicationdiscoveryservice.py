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

def associate_configuration_items_to_application(applicationConfigurationId=None, configurationIds=None):
    """
    Associates one or more configuration items with an application.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_configuration_items_to_application(
        applicationConfigurationId='string',
        configurationIds=[
            'string',
        ]
    )
    
    
    :type applicationConfigurationId: string
    :param applicationConfigurationId: [REQUIRED]
            The configuration ID of an application with which items are to be associated.
            

    :type configurationIds: list
    :param configurationIds: [REQUIRED]
            The ID of each configuration item to be associated with an application.
            (string) --
            

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

def create_application(name=None, description=None):
    """
    Creates an application with the given name and description.
    See also: AWS API Documentation
    
    
    :example: response = client.create_application(
        name='string',
        description='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            Name of the application to be created.
            

    :type description: string
    :param description: Description of the application to be created.

    :rtype: dict
    :return: {
        'configurationId': 'string'
    }
    
    
    """
    pass

def create_tags(configurationIds=None, tags=None):
    """
    Creates one or more tags for configuration items. Tags are metadata that help you categorize IT assets. This API accepts a list of multiple configuration items.
    See also: AWS API Documentation
    
    
    :example: response = client.create_tags(
        configurationIds=[
            'string',
        ],
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type configurationIds: list
    :param configurationIds: [REQUIRED]
            A list of configuration items that you want to tag.
            (string) --
            

    :type tags: list
    :param tags: [REQUIRED]
            Tags that you want to associate with one or more configuration items. Specify the tags that you want to create in a key -value format. For example:
            {'key': 'serverType', 'value': 'webServer'}
            (dict) --Metadata that help you categorize IT assets.
            key (string) -- [REQUIRED]The type of tag on which to filter.
            value (string) -- [REQUIRED]A value for a tag key on which to filter.
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_applications(configurationIds=None):
    """
    Deletes a list of applications and their associations with configuration items.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_applications(
        configurationIds=[
            'string',
        ]
    )
    
    
    :type configurationIds: list
    :param configurationIds: [REQUIRED]
            Configuration ID of an application to be deleted.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_tags(configurationIds=None, tags=None):
    """
    Deletes the association between configuration items and one or more tags. This API accepts a list of multiple configuration items.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_tags(
        configurationIds=[
            'string',
        ],
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type configurationIds: list
    :param configurationIds: [REQUIRED]
            A list of configuration items with tags that you want to delete.
            (string) --
            

    :type tags: list
    :param tags: Tags that you want to delete from one or more configuration items. Specify the tags that you want to delete in a key -value format. For example:
            {'key': 'serverType', 'value': 'webServer'}
            (dict) --Metadata that help you categorize IT assets.
            key (string) -- [REQUIRED]The type of tag on which to filter.
            value (string) -- [REQUIRED]A value for a tag key on which to filter.
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_agents(agentIds=None, filters=None, maxResults=None, nextToken=None):
    """
    Lists agents or connectors as specified by ID or other filters. All agents/connectors associated with your user account can be listed if you call DescribeAgents as is without passing any parameters.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_agents(
        agentIds=[
            'string',
        ],
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ],
                'condition': 'string'
            },
        ],
        maxResults=123,
        nextToken='string'
    )
    
    
    :type agentIds: list
    :param agentIds: The agent or the Connector IDs for which you want information. If you specify no IDs, the system returns information about all agents/Connectors associated with your AWS user account.
            (string) --
            

    :type filters: list
    :param filters: You can filter the request using various logical operators and a key -value format. For example:
            {'key': 'collectionStatus', 'value': 'STARTED'}
            (dict) --A filter that can use conditional operators.
            For more information about filters, see Querying Discovered Configuration Items .
            name (string) -- [REQUIRED]The name of the filter.
            values (list) -- [REQUIRED]A string value on which to filter. For example, if you choose the destinationServer.osVersion filter name, you could specify Ubuntu for the value.
            (string) --
            condition (string) -- [REQUIRED]A conditional operator. The following operators are valid: EQUALS, NOT_EQUALS, CONTAINS, NOT_CONTAINS. If you specify multiple filters, the system utilizes all filters as though concatenated by AND . If you specify multiple values for a particular filter, the system differentiates the values using OR . Calling either DescribeConfigurations or ListConfigurations returns attributes of matching configuration items.
            
            

    :type maxResults: integer
    :param maxResults: The total number of agents/Connectors to return in a single page of output. The maximum value is 100.

    :type nextToken: string
    :param nextToken: Token to retrieve the next set of results. For example, if you previously specified 100 IDs for DescribeAgentsRequest$agentIds but set DescribeAgentsRequest$maxResults to 10, you received a set of 10 results along with a token. Use that token in this query to get the next set of 10.

    :rtype: dict
    :return: {
        'agentsInfo': [
            {
                'agentId': 'string',
                'hostName': 'string',
                'agentNetworkInfoList': [
                    {
                        'ipAddress': 'string',
                        'macAddress': 'string'
                    },
                ],
                'connectorId': 'string',
                'version': 'string',
                'health': 'HEALTHY'|'UNHEALTHY'|'RUNNING'|'UNKNOWN'|'BLACKLISTED'|'SHUTDOWN',
                'lastHealthPingTime': 'string',
                'collectionStatus': 'string',
                'agentType': 'string',
                'registeredTime': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def describe_configurations(configurationIds=None):
    """
    Retrieves attributes for a list of configuration item IDs.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_configurations(
        configurationIds=[
            'string',
        ]
    )
    
    
    :type configurationIds: list
    :param configurationIds: [REQUIRED]
            One or more configuration IDs.
            (string) --
            

    :rtype: dict
    :return: {
        'configurations': [
            {
                'string': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_continuous_exports(exportIds=None, maxResults=None, nextToken=None):
    """
    Lists exports as specified by ID. All continuous exports associated with your user account can be listed if you call DescribeContinuousExports as is without passing any parameters.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_continuous_exports(
        exportIds=[
            'string',
        ],
        maxResults=123,
        nextToken='string'
    )
    
    
    :type exportIds: list
    :param exportIds: The unique IDs assigned to the exports.
            (string) --
            

    :type maxResults: integer
    :param maxResults: A number between 1 and 100 specifying the maximum number of continuous export descriptions returned.

    :type nextToken: string
    :param nextToken: The token from the previous call to DescribeExportTasks .

    :rtype: dict
    :return: {
        'descriptions': [
            {
                'exportId': 'string',
                'status': 'START_IN_PROGRESS'|'START_FAILED'|'ACTIVE'|'ERROR'|'STOP_IN_PROGRESS'|'STOP_FAILED'|'INACTIVE',
                'statusDetail': 'string',
                's3Bucket': 'string',
                'startTime': datetime(2015, 1, 1),
                'stopTime': datetime(2015, 1, 1),
                'dataSource': 'AGENT',
                'schemaStorageConfig': {
                    'string': 'string'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    START_IN_PROGRESS - setting up resources to start continuous export.
    START_FAILED - an error occurred setting up continuous export. To recover, call start-continuous-export again.
    ACTIVE - data is being exported to the customer bucket.
    ERROR - an error occurred during export. To fix the issue, call stop-continuous-export and start-continuous-export.
    STOP_IN_PROGRESS - stopping the export.
    STOP_FAILED - an error occurred stopping the export. To recover, call stop-continuous-export again.
    INACTIVE - the continuous export has been stopped. Data is no longer being exported to the customer bucket.
    
    """
    pass

def describe_export_configurations(exportIds=None, maxResults=None, nextToken=None):
    """
    Use instead ` DescribeExportTasks http://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeExportTasks.html`__ .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_export_configurations(
        exportIds=[
            'string',
        ],
        maxResults=123,
        nextToken='string'
    )
    
    
    :type exportIds: list
    :param exportIds: A list of continuous export ids to search for.
            (string) --
            

    :type maxResults: integer
    :param maxResults: A number between 1 and 100 specifying the maximum number of continuous export descriptions returned.

    :type nextToken: string
    :param nextToken: The token from the previous call to describe-export-tasks.

    :rtype: dict
    :return: {
        'exportsInfo': [
            {
                'exportId': 'string',
                'exportStatus': 'FAILED'|'SUCCEEDED'|'IN_PROGRESS',
                'statusMessage': 'string',
                'configurationsDownloadUrl': 'string',
                'exportRequestTime': datetime(2015, 1, 1),
                'isTruncated': True|False,
                'requestedStartTime': datetime(2015, 1, 1),
                'requestedEndTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def describe_export_tasks(exportIds=None, filters=None, maxResults=None, nextToken=None):
    """
    Retrieve status of one or more export tasks. You can retrieve the status of up to 100 export tasks.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_export_tasks(
        exportIds=[
            'string',
        ],
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ],
                'condition': 'string'
            },
        ],
        maxResults=123,
        nextToken='string'
    )
    
    
    :type exportIds: list
    :param exportIds: One or more unique identifiers used to query the status of an export request.
            (string) --
            

    :type filters: list
    :param filters: One or more filters.
            AgentId - ID of the agent whose collected data will be exported
            (dict) --Used to select which agent's data is to be exported. A single agent ID may be selected for export using the StartExportTask action.
            name (string) -- [REQUIRED]A single ExportFilter name. Supported filters: agentId .
            values (list) -- [REQUIRED]A single agentId for a Discovery Agent. An agentId can be found using the DescribeAgents action. Typically an ADS agentId is in the form o-0123456789abcdef0 .
            (string) --
            condition (string) -- [REQUIRED]Supported condition: EQUALS
            
            

    :type maxResults: integer
    :param maxResults: The maximum number of volume results returned by DescribeExportTasks in paginated output. When this parameter is used, DescribeExportTasks only returns maxResults results in a single page along with a nextToken response element.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated DescribeExportTasks request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return.

    :rtype: dict
    :return: {
        'exportsInfo': [
            {
                'exportId': 'string',
                'exportStatus': 'FAILED'|'SUCCEEDED'|'IN_PROGRESS',
                'statusMessage': 'string',
                'configurationsDownloadUrl': 'string',
                'exportRequestTime': datetime(2015, 1, 1),
                'isTruncated': True|False,
                'requestedStartTime': datetime(2015, 1, 1),
                'requestedEndTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def describe_tags(filters=None, maxResults=None, nextToken=None):
    """
    Retrieves a list of configuration items that have tags as specified by the key-value pairs, name and value, passed to the optional parameter filters .
    There are three valid tag filter names:
    Also, all configuration items associated with your user account that have tags can be listed if you call DescribeTags as is without passing any parameters.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_tags(
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ]
            },
        ],
        maxResults=123,
        nextToken='string'
    )
    
    
    :type filters: list
    :param filters: You can filter the list using a key -value format. You can separate these items by using logical operators. Allowed filters include tagKey , tagValue , and configurationId .
            (dict) --The tag filter. Valid names are: tagKey , tagValue , configurationId .
            name (string) -- [REQUIRED]A name of the tag filter.
            values (list) -- [REQUIRED]Values for the tag filter.
            (string) --
            
            

    :type maxResults: integer
    :param maxResults: The total number of items to return in a single page of output. The maximum value is 100.

    :type nextToken: string
    :param nextToken: A token to start the list. Use this token to get the next set of results.

    :rtype: dict
    :return: {
        'tags': [
            {
                'configurationType': 'SERVER'|'PROCESS'|'CONNECTION'|'APPLICATION',
                'configurationId': 'string',
                'key': 'string',
                'value': 'string',
                'timeOfCreation': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    filters (list) -- You can filter the list using a key -value format. You can separate these items by using logical operators. Allowed filters include tagKey , tagValue , and configurationId .
    
    (dict) --The tag filter. Valid names are: tagKey , tagValue , configurationId .
    
    name (string) -- [REQUIRED]A name of the tag filter.
    
    values (list) -- [REQUIRED]Values for the tag filter.
    
    (string) --
    
    
    
    
    
    
    maxResults (integer) -- The total number of items to return in a single page of output. The maximum value is 100.
    nextToken (string) -- A token to start the list. Use this token to get the next set of results.
    
    """
    pass

def disassociate_configuration_items_from_application(applicationConfigurationId=None, configurationIds=None):
    """
    Disassociates one or more configuration items from an application.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_configuration_items_from_application(
        applicationConfigurationId='string',
        configurationIds=[
            'string',
        ]
    )
    
    
    :type applicationConfigurationId: string
    :param applicationConfigurationId: [REQUIRED]
            Configuration ID of an application from which each item is disassociated.
            

    :type configurationIds: list
    :param configurationIds: [REQUIRED]
            Configuration ID of each item to be disassociated from an application.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def export_configurations():
    """
    Deprecated. Use StartExportTask instead.
    Exports all discovered configuration data to an Amazon S3 bucket or an application that enables you to view and evaluate the data. Data includes tags and tag associations, processes, connections, servers, and system performance. This API returns an export ID that you can query using the DescribeExportConfigurations API. The system imposes a limit of two configuration exports in six hours.
    See also: AWS API Documentation
    
    
    :example: response = client.export_configurations()
    
    
    :rtype: dict
    :return: {
        'exportId': 'string'
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

def get_discovery_summary():
    """
    Retrieves a short summary of discovered assets.
    This API operation takes no request parameters and is called as is at the command prompt as shown in the example.
    See also: AWS API Documentation
    
    
    :example: response = client.get_discovery_summary()
    
    
    :rtype: dict
    :return: {
        'servers': 123,
        'applications': 123,
        'serversMappedToApplications': 123,
        'serversMappedtoTags': 123,
        'agentSummary': {
            'activeAgents': 123,
            'healthyAgents': 123,
            'blackListedAgents': 123,
            'shutdownAgents': 123,
            'unhealthyAgents': 123,
            'totalAgents': 123,
            'unknownAgents': 123
        },
        'connectorSummary': {
            'activeConnectors': 123,
            'healthyConnectors': 123,
            'blackListedConnectors': 123,
            'shutdownConnectors': 123,
            'unhealthyConnectors': 123,
            'totalConnectors': 123,
            'unknownConnectors': 123
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

def get_waiter(waiter_name=None):
    """
    Returns an object that can wait for some condition.
    
    :type waiter_name: str
    :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.

    :rtype: botocore.waiter.Waiter
    """
    pass

def list_configurations(configurationType=None, filters=None, maxResults=None, nextToken=None, orderBy=None):
    """
    Retrieves a list of configuration items as specified by the value passed to the required paramater configurationType . Optional filtering may be applied to refine search results.
    See also: AWS API Documentation
    
    
    :example: response = client.list_configurations(
        configurationType='SERVER'|'PROCESS'|'CONNECTION'|'APPLICATION',
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ],
                'condition': 'string'
            },
        ],
        maxResults=123,
        nextToken='string',
        orderBy=[
            {
                'fieldName': 'string',
                'sortOrder': 'ASC'|'DESC'
            },
        ]
    )
    
    
    :type configurationType: string
    :param configurationType: [REQUIRED]
            A valid configuration identified by Application Discovery Service.
            

    :type filters: list
    :param filters: You can filter the request using various logical operators and a key -value format. For example:
            {'key': 'serverType', 'value': 'webServer'}
            For a complete list of filter options and guidance about using them with this action, see Querying Discovered Configuration Items .
            (dict) --A filter that can use conditional operators.
            For more information about filters, see Querying Discovered Configuration Items .
            name (string) -- [REQUIRED]The name of the filter.
            values (list) -- [REQUIRED]A string value on which to filter. For example, if you choose the destinationServer.osVersion filter name, you could specify Ubuntu for the value.
            (string) --
            condition (string) -- [REQUIRED]A conditional operator. The following operators are valid: EQUALS, NOT_EQUALS, CONTAINS, NOT_CONTAINS. If you specify multiple filters, the system utilizes all filters as though concatenated by AND . If you specify multiple values for a particular filter, the system differentiates the values using OR . Calling either DescribeConfigurations or ListConfigurations returns attributes of matching configuration items.
            
            

    :type maxResults: integer
    :param maxResults: The total number of items to return. The maximum value is 100.

    :type nextToken: string
    :param nextToken: Token to retrieve the next set of results. For example, if a previous call to ListConfigurations returned 100 items, but you set ListConfigurationsRequest$maxResults to 10, you received a set of 10 results along with a token. Use that token in this query to get the next set of 10.

    :type orderBy: list
    :param orderBy: Certain filter criteria return output that can be sorted in ascending or descending order. For a list of output characteristics for each filter, see Using the ListConfigurations Action .
            (dict) --A field and direction for ordered output.
            fieldName (string) -- [REQUIRED]The field on which to order.
            sortOrder (string) --Ordering direction.
            
            

    :rtype: dict
    :return: {
        'configurations': [
            {
                'string': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (dict) --
    (string) --
    (string) --
    
    
    
    
    
    """
    pass

def list_server_neighbors(configurationId=None, portInformationNeeded=None, neighborConfigurationIds=None, maxResults=None, nextToken=None):
    """
    Retrieves a list of servers that are one network hop away from a specified server.
    See also: AWS API Documentation
    
    
    :example: response = client.list_server_neighbors(
        configurationId='string',
        portInformationNeeded=True|False,
        neighborConfigurationIds=[
            'string',
        ],
        maxResults=123,
        nextToken='string'
    )
    
    
    :type configurationId: string
    :param configurationId: [REQUIRED]
            Configuration ID of the server for which neighbors are being listed.
            

    :type portInformationNeeded: boolean
    :param portInformationNeeded: Flag to indicate if port and protocol information is needed as part of the response.

    :type neighborConfigurationIds: list
    :param neighborConfigurationIds: List of configuration IDs to test for one-hop-away.
            (string) --
            

    :type maxResults: integer
    :param maxResults: Maximum number of results to return in a single page of output.

    :type nextToken: string
    :param nextToken: Token to retrieve the next set of results. For example, if you previously specified 100 IDs for ListServerNeighborsRequest$neighborConfigurationIds but set ListServerNeighborsRequest$maxResults to 10, you received a set of 10 results along with a token. Use that token in this query to get the next set of 10.

    :rtype: dict
    :return: {
        'neighbors': [
            {
                'sourceServerId': 'string',
                'destinationServerId': 'string',
                'destinationPort': 123,
                'transportProtocol': 'string',
                'connectionsCount': 123
            },
        ],
        'nextToken': 'string',
        'knownDependencyCount': 123
    }
    
    
    """
    pass

def start_continuous_export():
    """
    Start the continuous flow of agent's discovered data into Amazon Athena.
    See also: AWS API Documentation
    
    
    :example: response = client.start_continuous_export()
    
    
    :rtype: dict
    :return: {
        'exportId': 'string',
        's3Bucket': 'string',
        'startTime': datetime(2015, 1, 1),
        'dataSource': 'AGENT',
        'schemaStorageConfig': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def start_data_collection_by_agent_ids(agentIds=None):
    """
    Instructs the specified agents or connectors to start collecting data.
    See also: AWS API Documentation
    
    
    :example: response = client.start_data_collection_by_agent_ids(
        agentIds=[
            'string',
        ]
    )
    
    
    :type agentIds: list
    :param agentIds: [REQUIRED]
            The IDs of the agents or connectors from which to start collecting data. If you send a request to an agent/connector ID that you do not have permission to contact, according to your AWS account, the service does not throw an exception. Instead, it returns the error in the Description field. If you send a request to multiple agents/connectors and you do not have permission to contact some of those agents/connectors, the system does not throw an exception. Instead, the system shows Failed in the Description field.
            (string) --
            

    :rtype: dict
    :return: {
        'agentsConfigurationStatus': [
            {
                'agentId': 'string',
                'operationSucceeded': True|False,
                'description': 'string'
            },
        ]
    }
    
    
    """
    pass

def start_export_task(exportDataFormat=None, filters=None, startTime=None, endTime=None):
    """
    Begins the export of discovered data to an S3 bucket.
    If you specify agentIds in a filter, the task exports up to 72 hours of detailed data collected by the identified Application Discovery Agent, including network, process, and performance details. A time range for exported agent data may be set by using startTime and endTime . Export of detailed agent data is limited to five concurrently running exports.
    If you do not include an agentIds filter, summary data is exported that includes both AWS Agentless Discovery Connector data and summary data from AWS Discovery Agents. Export of summary data is limited to two exports per day.
    See also: AWS API Documentation
    
    
    :example: response = client.start_export_task(
        exportDataFormat=[
            'CSV'|'GRAPHML',
        ],
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ],
                'condition': 'string'
            },
        ],
        startTime=datetime(2015, 1, 1),
        endTime=datetime(2015, 1, 1)
    )
    
    
    :type exportDataFormat: list
    :param exportDataFormat: The file format for the returned export data. Default value is CSV . Note: The GRAPHML option has been deprecated.
            (string) --
            

    :type filters: list
    :param filters: If a filter is present, it selects the single agentId of the Application Discovery Agent for which data is exported. The agentId can be found in the results of the DescribeAgents API or CLI. If no filter is present, startTime and endTime are ignored and exported data includes both Agentless Discovery Connector data and summary data from Application Discovery agents.
            (dict) --Used to select which agent's data is to be exported. A single agent ID may be selected for export using the StartExportTask action.
            name (string) -- [REQUIRED]A single ExportFilter name. Supported filters: agentId .
            values (list) -- [REQUIRED]A single agentId for a Discovery Agent. An agentId can be found using the DescribeAgents action. Typically an ADS agentId is in the form o-0123456789abcdef0 .
            (string) --
            condition (string) -- [REQUIRED]Supported condition: EQUALS
            
            

    :type startTime: datetime
    :param startTime: The start timestamp for exported data from the single Application Discovery Agent selected in the filters. If no value is specified, data is exported starting from the first data collected by the agent.

    :type endTime: datetime
    :param endTime: The end timestamp for exported data from the single Application Discovery Agent selected in the filters. If no value is specified, exported data includes the most recent data collected by the agent.

    :rtype: dict
    :return: {
        'exportId': 'string'
    }
    
    
    """
    pass

def stop_continuous_export(exportId=None):
    """
    Stop the continuous flow of agent's discovered data into Amazon Athena.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_continuous_export(
        exportId='string'
    )
    
    
    :type exportId: string
    :param exportId: [REQUIRED]
            The unique ID assigned to this export.
            

    :rtype: dict
    :return: {
        'startTime': datetime(2015, 1, 1),
        'stopTime': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def stop_data_collection_by_agent_ids(agentIds=None):
    """
    Instructs the specified agents or connectors to stop collecting data.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_data_collection_by_agent_ids(
        agentIds=[
            'string',
        ]
    )
    
    
    :type agentIds: list
    :param agentIds: [REQUIRED]
            The IDs of the agents or connectors from which to stop collecting data.
            (string) --
            

    :rtype: dict
    :return: {
        'agentsConfigurationStatus': [
            {
                'agentId': 'string',
                'operationSucceeded': True|False,
                'description': 'string'
            },
        ]
    }
    
    
    """
    pass

def update_application(configurationId=None, name=None, description=None):
    """
    Updates metadata about an application.
    See also: AWS API Documentation
    
    
    :example: response = client.update_application(
        configurationId='string',
        name='string',
        description='string'
    )
    
    
    :type configurationId: string
    :param configurationId: [REQUIRED]
            Configuration ID of the application to be updated.
            

    :type name: string
    :param name: New name of the application to be updated.

    :type description: string
    :param description: New description of the application to be updated.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

