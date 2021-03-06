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

def get_cost_and_usage(TimePeriod=None, Granularity=None, Filter=None, Metrics=None, GroupBy=None, NextPageToken=None):
    """
    Retrieves cost and usage metrics for your account. You can specify which cost and usage-related metric, such as BlendedCosts or Quantity , that you want the request to return. You can also filter and group your data by various dimensions, such as SERVICE or AZ , in a specific time range. For a complete list of valid dimensions, see the GetDimensionValues operation. Master accounts in an organization in AWS Organizations have access to all member accounts.
    See also: AWS API Documentation
    
    
    :example: response = client.get_cost_and_usage(
        TimePeriod={
            'Start': 'string',
            'End': 'string'
        },
        Granularity='DAILY'|'MONTHLY'|'HOURLY',
        Filter={
            'Or': [
                {'... recursive ...'},
            ],
            'And': [
                {'... recursive ...'},
            ],
            'Not': {'... recursive ...'},
            'Dimensions': {
                'Key': 'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID',
                'Values': [
                    'string',
                ]
            },
            'Tags': {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            }
        },
        Metrics=[
            'string',
        ],
        GroupBy=[
            {
                'Type': 'DIMENSION'|'TAG',
                'Key': 'string'
            },
        ],
        NextPageToken='string'
    )
    
    
    :type TimePeriod: dict
    :param TimePeriod: Sets the start and end dates for retrieving AWS costs. The start date is inclusive, but the end date is exclusive. For example, if start is 2017-01-01 and end is 2017-05-01 , then the cost and usage data is retrieved from 2017-01-01 up to and including 2017-04-30 but not including 2017-05-01 .
            Start (string) -- [REQUIRED]The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.
            End (string) -- [REQUIRED]The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .
            

    :type Granularity: string
    :param Granularity: Sets the AWS cost granularity to MONTHLY or DAILY . If Granularity isn't set, the response object doesn't include the Granularity , either MONTHLY or DAILY .
            The GetCostAndUsageRequest operation supports only DAILY and MONTHLY granularities.
            

    :type Filter: dict
    :param Filter: Filters AWS costs by different dimensions. For example, you can specify SERVICE and LINKED_ACCOUNT and get the costs that are associated with that account's usage of that service. You can nest Expression objects to define any combination of dimension filters. For more information, see Expression .
            Or (list) --Return results that match either Dimension object.
            (dict) --Use Expression to filter by cost or by usage. There are two patterns:
            Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for INSTANCE_TYPE==m4.xlarge OR INSTANCE_TYPE==c4.large . The Expression for that looks like this: { 'Dimensions': { 'Key': 'INSTANCE_TYPE', 'Values': [ 'm4.xlarge',  c4.large  ] } }  The list of dimension values are OR'd together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.
            Compound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((INSTANCE_TYPE == m4.large OR INSTANCE_TYPE == m3.large) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'INSTANCE_TYPE', 'Values': [ 'm4.x.large', 'c4.large' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }
            Note
            Because each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.
            { 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }
            
            And (list) --Return results that match both Dimension objects.
            (dict) --Use Expression to filter by cost or by usage. There are two patterns:
            Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for INSTANCE_TYPE==m4.xlarge OR INSTANCE_TYPE==c4.large . The Expression for that looks like this: { 'Dimensions': { 'Key': 'INSTANCE_TYPE', 'Values': [ 'm4.xlarge',  c4.large  ] } }  The list of dimension values are OR'd together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.
            Compound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((INSTANCE_TYPE == m4.large OR INSTANCE_TYPE == m3.large) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'INSTANCE_TYPE', 'Values': [ 'm4.x.large', 'c4.large' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }
            Note
            Because each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.
            { 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }
            
            Not (dict) --Return results that don't match a Dimension object.
            Dimensions (dict) --The specific Dimension to use for Expression .
            Key (string) --The names of the metadata types that you can use to filter and group your results. For example, AZ returns a list of Availability Zones.
            Values (list) --The metadata values that you can use to filter and group your results. You can use GetDimensionValues to find specific values.
            Valid values for the SERVICE dimension are Amazon Elastic Compute Cloud - Compute , Amazon Elasticsearch Service , Amazon ElastiCache , Amazon Redshift , and Amazon Relational Database Service .
            (string) --
            
            Tags (dict) --The specific Tag to use for Expression .
            Key (string) --The key for the tag.
            Values (list) --The specific value of the tag.
            (string) --
            
            

    :type Metrics: list
    :param Metrics: Which metrics are returned in the query. For more information about blended and unblended rates, see Why does the 'blended' annotation appear on some line items in my bill? .
            Valid values are AmortizedCost , BlendedCost , NetAmortizedCost , NetUnblendedCost , NormalizedUsageAmount , UnblendedCost , and UsageQuantity .
            Note
            If you return the UsageQuantity metric, the service aggregates all usage numbers without taking into account the units. For example, if you aggregate usageQuantity across all of Amazon EC2, the results aren't meaningful because Amazon EC2 compute hours and data transfer are measured in different units (for example, hours vs. GB). To get more meaningful UsageQuantity metrics, filter by UsageType or UsageTypeGroups .
            Metrics is required for GetCostAndUsage requests.
            (string) --
            

    :type GroupBy: list
    :param GroupBy: You can group AWS costs using up to two different groups, either dimensions, tag keys, or both.
            When you group by tag key, you get all tag values, including empty strings.
            Valid values are AZ , INSTANCE_TYPE , LEGAL_ENTITY_NAME , LINKED_ACCOUNT , OPERATION , PLATFORM , PURCHASE_TYPE , SERVICE , TAGS , TENANCY , and USAGE_TYPE .
            (dict) --Represents a group when you specify a group by criteria or in the response to a query with a specific grouping.
            Type (string) --The string that represents the type of group.
            Key (string) --The string that represents a key for a specified group.
            
            

    :type NextPageToken: string
    :param NextPageToken: The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.

    :rtype: dict
    :return: {
        'NextPageToken': 'string',
        'GroupDefinitions': [
            {
                'Type': 'DIMENSION'|'TAG',
                'Key': 'string'
            },
        ],
        'ResultsByTime': [
            {
                'TimePeriod': {
                    'Start': 'string',
                    'End': 'string'
                },
                'Total': {
                    'string': {
                        'Amount': 'string',
                        'Unit': 'string'
                    }
                },
                'Groups': [
                    {
                        'Keys': [
                            'string',
                        ],
                        'Metrics': {
                            'string': {
                                'Amount': 'string',
                                'Unit': 'string'
                            }
                        }
                    },
                ],
                'Estimated': True|False
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_cost_forecast(TimePeriod=None, Metric=None, Granularity=None, Filter=None, PredictionIntervalLevel=None):
    """
    Retrieves a forecast for how much Amazon Web Services predicts that you will spend over the forecast time period that you select, based on your past costs.
    See also: AWS API Documentation
    
    
    :example: response = client.get_cost_forecast(
        TimePeriod={
            'Start': 'string',
            'End': 'string'
        },
        Metric='BLENDED_COST'|'UNBLENDED_COST'|'AMORTIZED_COST'|'NET_UNBLENDED_COST'|'NET_AMORTIZED_COST'|'USAGE_QUANTITY'|'NORMALIZED_USAGE_AMOUNT',
        Granularity='DAILY'|'MONTHLY'|'HOURLY',
        Filter={
            'Or': [
                {'... recursive ...'},
            ],
            'And': [
                {'... recursive ...'},
            ],
            'Not': {'... recursive ...'},
            'Dimensions': {
                'Key': 'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID',
                'Values': [
                    'string',
                ]
            },
            'Tags': {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            }
        },
        PredictionIntervalLevel=123
    )
    
    
    :type TimePeriod: dict
    :param TimePeriod: [REQUIRED]
            The period of time that you want the forecast to cover.
            Start (string) -- [REQUIRED]The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.
            End (string) -- [REQUIRED]The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .
            

    :type Metric: string
    :param Metric: [REQUIRED]
            Which metric Cost Explorer uses to create your forecast. For more information about blended and unblended rates, see Why does the 'blended' annotation appear on some line items in my bill? .
            Valid values for a GetCostForecast call are the following:
            AmortizedCost
            BlendedCost
            NetAmortizedCost
            NetUnblendedCost
            UnblendedCost
            

    :type Granularity: string
    :param Granularity: [REQUIRED]
            How granular you want the forecast to be. You can get 3 months of DAILY forecasts or 12 months of MONTHLY forecasts.
            The GetCostForecast operation supports only DAILY and MONTHLY granularities.
            

    :type Filter: dict
    :param Filter: The filters that you want to use to filter your forecast. Cost Explorer API supports all of the Cost Explorer filters.
            Or (list) --Return results that match either Dimension object.
            (dict) --Use Expression to filter by cost or by usage. There are two patterns:
            Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for INSTANCE_TYPE==m4.xlarge OR INSTANCE_TYPE==c4.large . The Expression for that looks like this: { 'Dimensions': { 'Key': 'INSTANCE_TYPE', 'Values': [ 'm4.xlarge',  c4.large  ] } }  The list of dimension values are OR'd together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.
            Compound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((INSTANCE_TYPE == m4.large OR INSTANCE_TYPE == m3.large) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'INSTANCE_TYPE', 'Values': [ 'm4.x.large', 'c4.large' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }
            Note
            Because each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.
            { 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }
            
            And (list) --Return results that match both Dimension objects.
            (dict) --Use Expression to filter by cost or by usage. There are two patterns:
            Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for INSTANCE_TYPE==m4.xlarge OR INSTANCE_TYPE==c4.large . The Expression for that looks like this: { 'Dimensions': { 'Key': 'INSTANCE_TYPE', 'Values': [ 'm4.xlarge',  c4.large  ] } }  The list of dimension values are OR'd together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.
            Compound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((INSTANCE_TYPE == m4.large OR INSTANCE_TYPE == m3.large) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'INSTANCE_TYPE', 'Values': [ 'm4.x.large', 'c4.large' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }
            Note
            Because each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.
            { 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }
            
            Not (dict) --Return results that don't match a Dimension object.
            Dimensions (dict) --The specific Dimension to use for Expression .
            Key (string) --The names of the metadata types that you can use to filter and group your results. For example, AZ returns a list of Availability Zones.
            Values (list) --The metadata values that you can use to filter and group your results. You can use GetDimensionValues to find specific values.
            Valid values for the SERVICE dimension are Amazon Elastic Compute Cloud - Compute , Amazon Elasticsearch Service , Amazon ElastiCache , Amazon Redshift , and Amazon Relational Database Service .
            (string) --
            
            Tags (dict) --The specific Tag to use for Expression .
            Key (string) --The key for the tag.
            Values (list) --The specific value of the tag.
            (string) --
            
            

    :type PredictionIntervalLevel: integer
    :param PredictionIntervalLevel: Cost Explorer always returns the mean forecast as a single point. You can request a prediction interval around the mean by specifying a confidence level. The higher the confidence level, the more confident Cost Explorer is about the actual value falling in the prediction interval. Higher confidence levels result in wider prediction intervals.

    :rtype: dict
    :return: {
        'Total': {
            'Amount': 'string',
            'Unit': 'string'
        },
        'ForecastResultsByTime': [
            {
                'TimePeriod': {
                    'Start': 'string',
                    'End': 'string'
                },
                'MeanValue': 'string',
                'PredictionIntervalLowerBound': 'string',
                'PredictionIntervalUpperBound': 'string'
            },
        ]
    }
    
    
    """
    pass

def get_dimension_values(SearchString=None, TimePeriod=None, Dimension=None, Context=None, NextPageToken=None):
    """
    Retrieves all available filter values for a specified filter over a period of time. You can search the dimension values for an arbitrary string.
    See also: AWS API Documentation
    
    
    :example: response = client.get_dimension_values(
        SearchString='string',
        TimePeriod={
            'Start': 'string',
            'End': 'string'
        },
        Dimension='AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID',
        Context='COST_AND_USAGE'|'RESERVATIONS',
        NextPageToken='string'
    )
    
    
    :type SearchString: string
    :param SearchString: The value that you want to search the filter values for.

    :type TimePeriod: dict
    :param TimePeriod: [REQUIRED]
            The start and end dates for retrieving the dimension values. The start date is inclusive, but the end date is exclusive. For example, if start is 2017-01-01 and end is 2017-05-01 , then the cost and usage data is retrieved from 2017-01-01 up to and including 2017-04-30 but not including 2017-05-01 .
            Start (string) -- [REQUIRED]The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.
            End (string) -- [REQUIRED]The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .
            

    :type Dimension: string
    :param Dimension: [REQUIRED]
            The name of the dimension. Each Dimension is available for a different Context . For more information, see Context .
            

    :type Context: string
    :param Context: The context for the call to GetDimensionValues . This can be RESERVATIONS or COST_AND_USAGE . The default value is COST_AND_USAGE . If the context is set to RESERVATIONS , the resulting dimension values can be used in the GetReservationUtilization operation. If the context is set to COST_AND_USAGE , the resulting dimension values can be used in the GetCostAndUsage operation.
            If you set the context to COST_AND_USAGE , you can use the following dimensions for searching:
            AZ - The Availability Zone. An example is us-east-1a .
            DATABASE_ENGINE - The Amazon Relational Database Service database. Examples are Aurora or MySQL.
            INSTANCE_TYPE - The type of Amazon EC2 instance. An example is m4.xlarge .
            LEGAL_ENTITY_NAME - The name of the organization that sells you AWS services, such as Amazon Web Services.
            LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account.
            OPERATING_SYSTEM - The operating system. Examples are Windows or Linux.
            OPERATION - The action performed. Examples include RunInstance and CreateBucket .
            PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.
            PURCHASE_TYPE - The reservation type of the purchase to which this usage is related. Examples include On-Demand Instances and Standard Reserved Instances.
            SERVICE - The AWS service such as Amazon DynamoDB.
            USAGE_TYPE - The type of usage. An example is DataTransfer-In-Bytes. The response for the GetDimensionValues operation includes a unit attribute. Examples include GB and Hrs.
            USAGE_TYPE_GROUP - The grouping of common usage types. An example is Amazon EC2: CloudWatch   Alarms. The response for this operation includes a unit attribute.
            RECORD_TYPE - The different types of charges such as RI fees, usage costs, tax refunds, and credits.
            If you set the context to RESERVATIONS , you can use the following dimensions for searching:
            AZ - The Availability Zone. An example is us-east-1a .
            CACHE_ENGINE - The Amazon ElastiCache operating system. Examples are Windows or Linux.
            DEPLOYMENT_OPTION - The scope of Amazon Relational Database Service deployments. Valid values are SingleAZ and MultiAZ .
            INSTANCE_TYPE - The type of Amazon EC2 instance. An example is m4.xlarge .
            LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account.
            PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.
            REGION - The AWS Region.
            SCOPE (Utilization only) - The scope of a Reserved Instance (RI). Values are regional or a single Availability Zone.
            TAG (Coverage only) - The tags that are associated with a Reserved Instance (RI).
            TENANCY - The tenancy of a resource. Examples are shared or dedicated.
            

    :type NextPageToken: string
    :param NextPageToken: The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.

    :rtype: dict
    :return: {
        'DimensionValues': [
            {
                'Value': 'string',
                'Attributes': {
                    'string': 'string'
                }
            },
        ],
        'ReturnSize': 123,
        'TotalSize': 123,
        'NextPageToken': 'string'
    }
    
    
    :returns: 
    AZ - The Availability Zone. An example is us-east-1a .
    DATABASE_ENGINE - The Amazon Relational Database Service database. Examples are Aurora or MySQL.
    INSTANCE_TYPE - The type of Amazon EC2 instance. An example is m4.xlarge .
    LEGAL_ENTITY_NAME - The name of the organization that sells you AWS services, such as Amazon Web Services.
    LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account.
    OPERATING_SYSTEM - The operating system. Examples are Windows or Linux.
    OPERATION - The action performed. Examples include RunInstance and CreateBucket .
    PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.
    PURCHASE_TYPE - The reservation type of the purchase to which this usage is related. Examples include On-Demand Instances and Standard Reserved Instances.
    SERVICE - The AWS service such as Amazon DynamoDB.
    USAGE_TYPE - The type of usage. An example is DataTransfer-In-Bytes. The response for the GetDimensionValues operation includes a unit attribute. Examples include GB and Hrs.
    USAGE_TYPE_GROUP - The grouping of common usage types. An example is Amazon EC2: CloudWatch  Alarms. The response for this operation includes a unit attribute.
    RECORD_TYPE - The different types of charges such as RI fees, usage costs, tax refunds, and credits.
    
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

def get_reservation_coverage(TimePeriod=None, GroupBy=None, Granularity=None, Filter=None, Metrics=None, NextPageToken=None):
    """
    Retrieves the reservation coverage for your account. This enables you to see how much of your Amazon Elastic Compute Cloud, Amazon ElastiCache, Amazon Relational Database Service, or Amazon Redshift usage is covered by a reservation. An organization's master account can see the coverage of the associated member accounts. For any time period, you can filter data about reservation usage by the following dimensions:
    To determine valid values for a dimension, use the GetDimensionValues operation.
    See also: AWS API Documentation
    
    
    :example: response = client.get_reservation_coverage(
        TimePeriod={
            'Start': 'string',
            'End': 'string'
        },
        GroupBy=[
            {
                'Type': 'DIMENSION'|'TAG',
                'Key': 'string'
            },
        ],
        Granularity='DAILY'|'MONTHLY'|'HOURLY',
        Filter={
            'Or': [
                {'... recursive ...'},
            ],
            'And': [
                {'... recursive ...'},
            ],
            'Not': {'... recursive ...'},
            'Dimensions': {
                'Key': 'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID',
                'Values': [
                    'string',
                ]
            },
            'Tags': {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            }
        },
        Metrics=[
            'string',
        ],
        NextPageToken='string'
    )
    
    
    :type TimePeriod: dict
    :param TimePeriod: [REQUIRED]
            The start and end dates of the period that you want to retrieve data about reservation coverage for. You can retrieve data for a maximum of 13 months: the last 12 months and the current month. The start date is inclusive, but the end date is exclusive. For example, if start is 2017-01-01 and end is 2017-05-01 , then the cost and usage data is retrieved from 2017-01-01 up to and including 2017-04-30 but not including 2017-05-01 .
            Start (string) -- [REQUIRED]The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.
            End (string) -- [REQUIRED]The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .
            

    :type GroupBy: list
    :param GroupBy: You can group the data by the following attributes:
            AZ
            CACHE_ENGINE
            DATABASE_ENGINE
            DEPLOYMENT_OPTION
            INSTANCE_TYPE
            LINKED_ACCOUNT
            OPERATING_SYSTEM
            PLATFORM
            REGION
            TAG
            TENANCY
            (dict) --Represents a group when you specify a group by criteria or in the response to a query with a specific grouping.
            Type (string) --The string that represents the type of group.
            Key (string) --The string that represents a key for a specified group.
            
            

    :type Granularity: string
    :param Granularity: The granularity of the AWS cost data for the reservation. Valid values are MONTHLY and DAILY .
            If GroupBy is set, Granularity can't be set. If Granularity isn't set, the response object doesn't include Granularity , either MONTHLY or DAILY .
            The GetReservationCoverage operation supports only DAILY and MONTHLY granularities.
            

    :type Filter: dict
    :param Filter: Filters utilization data by dimensions. You can filter by the following dimensions:
            AZ
            CACHE_ENGINE
            DATABASE_ENGINE
            DEPLOYMENT_OPTION
            INSTANCE_TYPE
            LINKED_ACCOUNT
            OPERATING_SYSTEM
            PLATFORM
            REGION
            SERVICE
            TAG
            TENANCY
            GetReservationCoverage uses the same Expression object as the other operations, but only AND is supported among each dimension. You can nest only one level deep. If there are multiple values for a dimension, they are OR'd together.
            If you don't provide a SERVICE filter, Cost Explorer defaults to EC2.
            Or (list) --Return results that match either Dimension object.
            (dict) --Use Expression to filter by cost or by usage. There are two patterns:
            Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for INSTANCE_TYPE==m4.xlarge OR INSTANCE_TYPE==c4.large . The Expression for that looks like this: { 'Dimensions': { 'Key': 'INSTANCE_TYPE', 'Values': [ 'm4.xlarge',  c4.large  ] } }  The list of dimension values are OR'd together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.
            Compound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((INSTANCE_TYPE == m4.large OR INSTANCE_TYPE == m3.large) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'INSTANCE_TYPE', 'Values': [ 'm4.x.large', 'c4.large' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }
            Note
            Because each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.
            { 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }
            
            And (list) --Return results that match both Dimension objects.
            (dict) --Use Expression to filter by cost or by usage. There are two patterns:
            Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for INSTANCE_TYPE==m4.xlarge OR INSTANCE_TYPE==c4.large . The Expression for that looks like this: { 'Dimensions': { 'Key': 'INSTANCE_TYPE', 'Values': [ 'm4.xlarge',  c4.large  ] } }  The list of dimension values are OR'd together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.
            Compound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((INSTANCE_TYPE == m4.large OR INSTANCE_TYPE == m3.large) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'INSTANCE_TYPE', 'Values': [ 'm4.x.large', 'c4.large' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }
            Note
            Because each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.
            { 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }
            
            Not (dict) --Return results that don't match a Dimension object.
            Dimensions (dict) --The specific Dimension to use for Expression .
            Key (string) --The names of the metadata types that you can use to filter and group your results. For example, AZ returns a list of Availability Zones.
            Values (list) --The metadata values that you can use to filter and group your results. You can use GetDimensionValues to find specific values.
            Valid values for the SERVICE dimension are Amazon Elastic Compute Cloud - Compute , Amazon Elasticsearch Service , Amazon ElastiCache , Amazon Redshift , and Amazon Relational Database Service .
            (string) --
            
            Tags (dict) --The specific Tag to use for Expression .
            Key (string) --The key for the tag.
            Values (list) --The specific value of the tag.
            (string) --
            
            

    :type Metrics: list
    :param Metrics: 
            (string) --
            

    :type NextPageToken: string
    :param NextPageToken: The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.

    :rtype: dict
    :return: {
        'CoveragesByTime': [
            {
                'TimePeriod': {
                    'Start': 'string',
                    'End': 'string'
                },
                'Groups': [
                    {
                        'Attributes': {
                            'string': 'string'
                        },
                        'Coverage': {
                            'CoverageHours': {
                                'OnDemandHours': 'string',
                                'ReservedHours': 'string',
                                'TotalRunningHours': 'string',
                                'CoverageHoursPercentage': 'string'
                            },
                            'CoverageNormalizedUnits': {
                                'OnDemandNormalizedUnits': 'string',
                                'ReservedNormalizedUnits': 'string',
                                'TotalRunningNormalizedUnits': 'string',
                                'CoverageNormalizedUnitsPercentage': 'string'
                            },
                            'CoverageCost': {
                                'OnDemandCost': 'string'
                            }
                        }
                    },
                ],
                'Total': {
                    'CoverageHours': {
                        'OnDemandHours': 'string',
                        'ReservedHours': 'string',
                        'TotalRunningHours': 'string',
                        'CoverageHoursPercentage': 'string'
                    },
                    'CoverageNormalizedUnits': {
                        'OnDemandNormalizedUnits': 'string',
                        'ReservedNormalizedUnits': 'string',
                        'TotalRunningNormalizedUnits': 'string',
                        'CoverageNormalizedUnitsPercentage': 'string'
                    },
                    'CoverageCost': {
                        'OnDemandCost': 'string'
                    }
                }
            },
        ],
        'Total': {
            'CoverageHours': {
                'OnDemandHours': 'string',
                'ReservedHours': 'string',
                'TotalRunningHours': 'string',
                'CoverageHoursPercentage': 'string'
            },
            'CoverageNormalizedUnits': {
                'OnDemandNormalizedUnits': 'string',
                'ReservedNormalizedUnits': 'string',
                'TotalRunningNormalizedUnits': 'string',
                'CoverageNormalizedUnitsPercentage': 'string'
            },
            'CoverageCost': {
                'OnDemandCost': 'string'
            }
        },
        'NextPageToken': 'string'
    }
    
    
    :returns: 
    TimePeriod (dict) -- [REQUIRED]
    The start and end dates of the period that you want to retrieve data about reservation coverage for. You can retrieve data for a maximum of 13 months: the last 12 months and the current month. The start date is inclusive, but the end date is exclusive. For example, if start is 2017-01-01 and end is 2017-05-01 , then the cost and usage data is retrieved from 2017-01-01 up to and including 2017-04-30 but not including 2017-05-01 .
    
    Start (string) -- [REQUIRED]The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.
    
    End (string) -- [REQUIRED]The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .
    
    
    
    GroupBy (list) -- You can group the data by the following attributes:
    
    AZ
    CACHE_ENGINE
    DATABASE_ENGINE
    DEPLOYMENT_OPTION
    INSTANCE_TYPE
    LINKED_ACCOUNT
    OPERATING_SYSTEM
    PLATFORM
    REGION
    TAG
    TENANCY
    
    
    (dict) --Represents a group when you specify a group by criteria or in the response to a query with a specific grouping.
    
    Type (string) --The string that represents the type of group.
    
    Key (string) --The string that represents a key for a specified group.
    
    
    
    
    
    Granularity (string) -- The granularity of the AWS cost data for the reservation. Valid values are MONTHLY and DAILY .
    If GroupBy is set, Granularity can't be set. If Granularity isn't set, the response object doesn't include Granularity , either MONTHLY or DAILY .
    The GetReservationCoverage operation supports only DAILY and MONTHLY granularities.
    
    Filter (dict) -- Filters utilization data by dimensions. You can filter by the following dimensions:
    
    AZ
    CACHE_ENGINE
    DATABASE_ENGINE
    DEPLOYMENT_OPTION
    INSTANCE_TYPE
    LINKED_ACCOUNT
    OPERATING_SYSTEM
    PLATFORM
    REGION
    SERVICE
    TAG
    TENANCY
    
    
    GetReservationCoverage uses the same Expression object as the other operations, but only AND is supported among each dimension. You can nest only one level deep. If there are multiple values for a dimension, they are OR'd together.
    If you don't provide a SERVICE filter, Cost Explorer defaults to EC2.
    
    Or (list) --Return results that match either Dimension object.
    
    (dict) --Use Expression to filter by cost or by usage. There are two patterns:
    
    Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for INSTANCE_TYPE==m4.xlarge OR INSTANCE_TYPE==c4.large . The Expression for that looks like this:  { "Dimensions": { "Key": "INSTANCE_TYPE", "Values": [ "m4.xlarge", c4.large ] } }   The list of dimension values are OR'd together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.
    Compound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((INSTANCE_TYPE == m4.large OR INSTANCE_TYPE == m3.large) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this:  { "And": [ {"Or": [ {"Dimensions": { "Key": "INSTANCE_TYPE", "Values": [ "m4.x.large", "c4.large" ] }}, {"Tags": { "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE", "Values": ["DataTransfer"] }}} ] }
    
    
    Note
    
    Because each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.
    { "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [ "DataTransfer" ] } }
    
    
    
    
    And (list) --Return results that match both Dimension objects.
    
    (dict) --Use Expression to filter by cost or by usage. There are two patterns:
    
    Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for INSTANCE_TYPE==m4.xlarge OR INSTANCE_TYPE==c4.large . The Expression for that looks like this:  { "Dimensions": { "Key": "INSTANCE_TYPE", "Values": [ "m4.xlarge", c4.large ] } }   The list of dimension values are OR'd together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.
    Compound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((INSTANCE_TYPE == m4.large OR INSTANCE_TYPE == m3.large) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this:  { "And": [ {"Or": [ {"Dimensions": { "Key": "INSTANCE_TYPE", "Values": [ "m4.x.large", "c4.large" ] }}, {"Tags": { "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE", "Values": ["DataTransfer"] }}} ] }
    
    
    Note
    
    Because each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.
    { "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [ "DataTransfer" ] } }
    
    
    
    
    Not (dict) --Return results that don't match a Dimension object.
    
    Dimensions (dict) --The specific Dimension to use for Expression .
    
    Key (string) --The names of the metadata types that you can use to filter and group your results. For example, AZ returns a list of Availability Zones.
    
    Values (list) --The metadata values that you can use to filter and group your results. You can use GetDimensionValues to find specific values.
    Valid values for the SERVICE dimension are Amazon Elastic Compute Cloud - Compute , Amazon Elasticsearch Service , Amazon ElastiCache , Amazon Redshift , and Amazon Relational Database Service .
    
    (string) --
    
    
    
    
    Tags (dict) --The specific Tag to use for Expression .
    
    Key (string) --The key for the tag.
    
    Values (list) --The specific value of the tag.
    
    (string) --
    
    
    
    
    
    
    Metrics (list) -- 
    (string) --
    
    
    NextPageToken (string) -- The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.
    
    """
    pass

def get_reservation_purchase_recommendation(AccountId=None, Service=None, AccountScope=None, LookbackPeriodInDays=None, TermInYears=None, PaymentOption=None, ServiceSpecification=None, PageSize=None, NextPageToken=None):
    """
    Gets recommendations for which reservations to purchase. These recommendations could help you reduce your costs. Reservations provide a discounted hourly rate (up to 75%) compared to On-Demand pricing.
    AWS generates your recommendations by identifying your On-Demand usage during a specific time period and collecting your usage into categories that are eligible for a reservation. After AWS has these categories, it simulates every combination of reservations in each category of usage to identify the best number of each type of RI to purchase to maximize your estimated savings.
    For example, AWS automatically aggregates your Amazon EC2 Linux, shared tenancy, and c4 family usage in the US West (Oregon) Region and recommends that you buy size-flexible regional reservations to apply to the c4 family usage. AWS recommends the smallest size instance in an instance family. This makes it easier to purchase a size-flexible RI. AWS also shows the equal number of normalized units so that you can purchase any instance size that you want. For this example, your RI recommendation would be for c4.large because that is the smallest size instance in the c4 instance family.
    See also: AWS API Documentation
    
    
    :example: response = client.get_reservation_purchase_recommendation(
        AccountId='string',
        Service='string',
        AccountScope='PAYER'|'LINKED',
        LookbackPeriodInDays='SEVEN_DAYS'|'THIRTY_DAYS'|'SIXTY_DAYS',
        TermInYears='ONE_YEAR'|'THREE_YEARS',
        PaymentOption='NO_UPFRONT'|'PARTIAL_UPFRONT'|'ALL_UPFRONT'|'LIGHT_UTILIZATION'|'MEDIUM_UTILIZATION'|'HEAVY_UTILIZATION',
        ServiceSpecification={
            'EC2Specification': {
                'OfferingClass': 'STANDARD'|'CONVERTIBLE'
            }
        },
        PageSize=123,
        NextPageToken='string'
    )
    
    
    :type AccountId: string
    :param AccountId: The account ID that is associated with the recommendation.

    :type Service: string
    :param Service: [REQUIRED]
            The specific service that you want recommendations for.
            

    :type AccountScope: string
    :param AccountScope: The account scope that you want recommendations for. PAYER means that AWS includes the master account and any member accounts when it calculates its recommendations. LINKED means that AWS includes only member accounts when it calculates its recommendations.
            Valid values are PAYER and LINKED .
            

    :type LookbackPeriodInDays: string
    :param LookbackPeriodInDays: The number of previous days that you want AWS to consider when it calculates your recommendations.

    :type TermInYears: string
    :param TermInYears: The reservation term that you want recommendations for.

    :type PaymentOption: string
    :param PaymentOption: The reservation purchase option that you want recommendations for.

    :type ServiceSpecification: dict
    :param ServiceSpecification: The hardware specifications for the service instances that you want recommendations for, such as standard or convertible Amazon EC2 instances.
            EC2Specification (dict) --The Amazon EC2 hardware specifications that you want AWS to provide recommendations for.
            OfferingClass (string) --Whether you want a recommendation for standard or convertible reservations.
            
            

    :type PageSize: integer
    :param PageSize: The number of recommendations that you want returned in a single response object.

    :type NextPageToken: string
    :param NextPageToken: The pagination token that indicates the next set of results that you want to retrieve.

    :rtype: dict
    :return: {
        'Metadata': {
            'RecommendationId': 'string',
            'GenerationTimestamp': 'string'
        },
        'Recommendations': [
            {
                'AccountScope': 'PAYER'|'LINKED',
                'LookbackPeriodInDays': 'SEVEN_DAYS'|'THIRTY_DAYS'|'SIXTY_DAYS',
                'TermInYears': 'ONE_YEAR'|'THREE_YEARS',
                'PaymentOption': 'NO_UPFRONT'|'PARTIAL_UPFRONT'|'ALL_UPFRONT'|'LIGHT_UTILIZATION'|'MEDIUM_UTILIZATION'|'HEAVY_UTILIZATION',
                'ServiceSpecification': {
                    'EC2Specification': {
                        'OfferingClass': 'STANDARD'|'CONVERTIBLE'
                    }
                },
                'RecommendationDetails': [
                    {
                        'AccountId': 'string',
                        'InstanceDetails': {
                            'EC2InstanceDetails': {
                                'Family': 'string',
                                'InstanceType': 'string',
                                'Region': 'string',
                                'AvailabilityZone': 'string',
                                'Platform': 'string',
                                'Tenancy': 'string',
                                'CurrentGeneration': True|False,
                                'SizeFlexEligible': True|False
                            },
                            'RDSInstanceDetails': {
                                'Family': 'string',
                                'InstanceType': 'string',
                                'Region': 'string',
                                'DatabaseEngine': 'string',
                                'DatabaseEdition': 'string',
                                'DeploymentOption': 'string',
                                'LicenseModel': 'string',
                                'CurrentGeneration': True|False,
                                'SizeFlexEligible': True|False
                            },
                            'RedshiftInstanceDetails': {
                                'Family': 'string',
                                'NodeType': 'string',
                                'Region': 'string',
                                'CurrentGeneration': True|False,
                                'SizeFlexEligible': True|False
                            },
                            'ElastiCacheInstanceDetails': {
                                'Family': 'string',
                                'NodeType': 'string',
                                'Region': 'string',
                                'ProductDescription': 'string',
                                'CurrentGeneration': True|False,
                                'SizeFlexEligible': True|False
                            },
                            'ESInstanceDetails': {
                                'InstanceClass': 'string',
                                'InstanceSize': 'string',
                                'Region': 'string',
                                'CurrentGeneration': True|False,
                                'SizeFlexEligible': True|False
                            }
                        },
                        'RecommendedNumberOfInstancesToPurchase': 'string',
                        'RecommendedNormalizedUnitsToPurchase': 'string',
                        'MinimumNumberOfInstancesUsedPerHour': 'string',
                        'MinimumNormalizedUnitsUsedPerHour': 'string',
                        'MaximumNumberOfInstancesUsedPerHour': 'string',
                        'MaximumNormalizedUnitsUsedPerHour': 'string',
                        'AverageNumberOfInstancesUsedPerHour': 'string',
                        'AverageNormalizedUnitsUsedPerHour': 'string',
                        'AverageUtilization': 'string',
                        'EstimatedBreakEvenInMonths': 'string',
                        'CurrencyCode': 'string',
                        'EstimatedMonthlySavingsAmount': 'string',
                        'EstimatedMonthlySavingsPercentage': 'string',
                        'EstimatedMonthlyOnDemandCost': 'string',
                        'EstimatedReservationCostForLookbackPeriod': 'string',
                        'UpfrontCost': 'string',
                        'RecurringStandardMonthlyCost': 'string'
                    },
                ],
                'RecommendationSummary': {
                    'TotalEstimatedMonthlySavingsAmount': 'string',
                    'TotalEstimatedMonthlySavingsPercentage': 'string',
                    'CurrencyCode': 'string'
                }
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    """
    pass

def get_reservation_utilization(TimePeriod=None, GroupBy=None, Granularity=None, Filter=None, NextPageToken=None):
    """
    Retrieves the reservation utilization for your account. Master accounts in an organization have access to member accounts. You can filter data by dimensions in a time period. You can use GetDimensionValues to determine the possible dimension values. Currently, you can group only by SUBSCRIPTION_ID .
    See also: AWS API Documentation
    
    
    :example: response = client.get_reservation_utilization(
        TimePeriod={
            'Start': 'string',
            'End': 'string'
        },
        GroupBy=[
            {
                'Type': 'DIMENSION'|'TAG',
                'Key': 'string'
            },
        ],
        Granularity='DAILY'|'MONTHLY'|'HOURLY',
        Filter={
            'Or': [
                {'... recursive ...'},
            ],
            'And': [
                {'... recursive ...'},
            ],
            'Not': {'... recursive ...'},
            'Dimensions': {
                'Key': 'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID',
                'Values': [
                    'string',
                ]
            },
            'Tags': {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            }
        },
        NextPageToken='string'
    )
    
    
    :type TimePeriod: dict
    :param TimePeriod: [REQUIRED]
            Sets the start and end dates for retrieving RI utilization. The start date is inclusive, but the end date is exclusive. For example, if start is 2017-01-01 and end is 2017-05-01 , then the cost and usage data is retrieved from 2017-01-01 up to and including 2017-04-30 but not including 2017-05-01 .
            Start (string) -- [REQUIRED]The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.
            End (string) -- [REQUIRED]The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .
            

    :type GroupBy: list
    :param GroupBy: Groups only by SUBSCRIPTION_ID . Metadata is included.
            (dict) --Represents a group when you specify a group by criteria or in the response to a query with a specific grouping.
            Type (string) --The string that represents the type of group.
            Key (string) --The string that represents a key for a specified group.
            
            

    :type Granularity: string
    :param Granularity: If GroupBy is set, Granularity can't be set. If Granularity isn't set, the response object doesn't include Granularity , either MONTHLY or DAILY . If both GroupBy and Granularity aren't set, GetReservationUtilization defaults to DAILY .
            The GetReservationUtilization operation supports only DAILY and MONTHLY granularities.
            

    :type Filter: dict
    :param Filter: Filters utilization data by dimensions. You can filter by the following dimensions:
            AZ
            CACHE_ENGINE
            DATABASE_ENGINE
            DEPLOYMENT_OPTION
            INSTANCE_TYPE
            LINKED_ACCOUNT
            OPERATING_SYSTEM
            PLATFORM
            REGION
            SERVICE
            SCOPE
            TENANCY
            GetReservationUtilization uses the same Expression object as the other operations, but only AND is supported among each dimension, and nesting is supported up to only one level deep. If there are multiple values for a dimension, they are OR'd together.
            Or (list) --Return results that match either Dimension object.
            (dict) --Use Expression to filter by cost or by usage. There are two patterns:
            Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for INSTANCE_TYPE==m4.xlarge OR INSTANCE_TYPE==c4.large . The Expression for that looks like this: { 'Dimensions': { 'Key': 'INSTANCE_TYPE', 'Values': [ 'm4.xlarge',  c4.large  ] } }  The list of dimension values are OR'd together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.
            Compound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((INSTANCE_TYPE == m4.large OR INSTANCE_TYPE == m3.large) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'INSTANCE_TYPE', 'Values': [ 'm4.x.large', 'c4.large' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }
            Note
            Because each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.
            { 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }
            
            And (list) --Return results that match both Dimension objects.
            (dict) --Use Expression to filter by cost or by usage. There are two patterns:
            Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for INSTANCE_TYPE==m4.xlarge OR INSTANCE_TYPE==c4.large . The Expression for that looks like this: { 'Dimensions': { 'Key': 'INSTANCE_TYPE', 'Values': [ 'm4.xlarge',  c4.large  ] } }  The list of dimension values are OR'd together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.
            Compound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((INSTANCE_TYPE == m4.large OR INSTANCE_TYPE == m3.large) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'INSTANCE_TYPE', 'Values': [ 'm4.x.large', 'c4.large' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }
            Note
            Because each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.
            { 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }
            
            Not (dict) --Return results that don't match a Dimension object.
            Dimensions (dict) --The specific Dimension to use for Expression .
            Key (string) --The names of the metadata types that you can use to filter and group your results. For example, AZ returns a list of Availability Zones.
            Values (list) --The metadata values that you can use to filter and group your results. You can use GetDimensionValues to find specific values.
            Valid values for the SERVICE dimension are Amazon Elastic Compute Cloud - Compute , Amazon Elasticsearch Service , Amazon ElastiCache , Amazon Redshift , and Amazon Relational Database Service .
            (string) --
            
            Tags (dict) --The specific Tag to use for Expression .
            Key (string) --The key for the tag.
            Values (list) --The specific value of the tag.
            (string) --
            
            

    :type NextPageToken: string
    :param NextPageToken: The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.

    :rtype: dict
    :return: {
        'UtilizationsByTime': [
            {
                'TimePeriod': {
                    'Start': 'string',
                    'End': 'string'
                },
                'Groups': [
                    {
                        'Key': 'string',
                        'Value': 'string',
                        'Attributes': {
                            'string': 'string'
                        },
                        'Utilization': {
                            'UtilizationPercentage': 'string',
                            'UtilizationPercentageInUnits': 'string',
                            'PurchasedHours': 'string',
                            'PurchasedUnits': 'string',
                            'TotalActualHours': 'string',
                            'TotalActualUnits': 'string',
                            'UnusedHours': 'string',
                            'UnusedUnits': 'string',
                            'OnDemandCostOfRIHoursUsed': 'string',
                            'NetRISavings': 'string',
                            'TotalPotentialRISavings': 'string',
                            'AmortizedUpfrontFee': 'string',
                            'AmortizedRecurringFee': 'string',
                            'TotalAmortizedFee': 'string'
                        }
                    },
                ],
                'Total': {
                    'UtilizationPercentage': 'string',
                    'UtilizationPercentageInUnits': 'string',
                    'PurchasedHours': 'string',
                    'PurchasedUnits': 'string',
                    'TotalActualHours': 'string',
                    'TotalActualUnits': 'string',
                    'UnusedHours': 'string',
                    'UnusedUnits': 'string',
                    'OnDemandCostOfRIHoursUsed': 'string',
                    'NetRISavings': 'string',
                    'TotalPotentialRISavings': 'string',
                    'AmortizedUpfrontFee': 'string',
                    'AmortizedRecurringFee': 'string',
                    'TotalAmortizedFee': 'string'
                }
            },
        ],
        'Total': {
            'UtilizationPercentage': 'string',
            'UtilizationPercentageInUnits': 'string',
            'PurchasedHours': 'string',
            'PurchasedUnits': 'string',
            'TotalActualHours': 'string',
            'TotalActualUnits': 'string',
            'UnusedHours': 'string',
            'UnusedUnits': 'string',
            'OnDemandCostOfRIHoursUsed': 'string',
            'NetRISavings': 'string',
            'TotalPotentialRISavings': 'string',
            'AmortizedUpfrontFee': 'string',
            'AmortizedRecurringFee': 'string',
            'TotalAmortizedFee': 'string'
        },
        'NextPageToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_tags(SearchString=None, TimePeriod=None, TagKey=None, NextPageToken=None):
    """
    Queries for available tag keys and tag values for a specified period. You can search the tag values for an arbitrary string.
    See also: AWS API Documentation
    
    
    :example: response = client.get_tags(
        SearchString='string',
        TimePeriod={
            'Start': 'string',
            'End': 'string'
        },
        TagKey='string',
        NextPageToken='string'
    )
    
    
    :type SearchString: string
    :param SearchString: The value that you want to search for.

    :type TimePeriod: dict
    :param TimePeriod: [REQUIRED]
            The start and end dates for retrieving the dimension values. The start date is inclusive, but the end date is exclusive. For example, if start is 2017-01-01 and end is 2017-05-01 , then the cost and usage data is retrieved from 2017-01-01 up to and including 2017-04-30 but not including 2017-05-01 .
            Start (string) -- [REQUIRED]The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.
            End (string) -- [REQUIRED]The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .
            

    :type TagKey: string
    :param TagKey: The key of the tag that you want to return values for.

    :type NextPageToken: string
    :param NextPageToken: The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.

    :rtype: dict
    :return: {
        'NextPageToken': 'string',
        'Tags': [
            'string',
        ],
        'ReturnSize': 123,
        'TotalSize': 123
    }
    
    
    :returns: 
    (string) --
    
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

