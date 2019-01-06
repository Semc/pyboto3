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

def batch_get_traces(TraceIds=None, NextToken=None):
    """
    Retrieves a list of traces specified by ID. Each trace is a collection of segment documents that originates from a single request. Use GetTraceSummaries to get a list of trace IDs.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_get_traces(
        TraceIds=[
            'string',
        ],
        NextToken='string'
    )
    
    
    :type TraceIds: list
    :param TraceIds: [REQUIRED]
            Specify the trace IDs of requests for which to retrieve segments.
            (string) --
            

    :type NextToken: string
    :param NextToken: Pagination token. Not used.

    :rtype: dict
    :return: {
        'Traces': [
            {
                'Id': 'string',
                'Duration': 123.0,
                'Segments': [
                    {
                        'Id': 'string',
                        'Document': 'string'
                    },
                ]
            },
        ],
        'UnprocessedTraceIds': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
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

def create_group(GroupName=None, FilterExpression=None):
    """
    Creates a group resource with a name and a filter expression.
    See also: AWS API Documentation
    
    
    :example: response = client.create_group(
        GroupName='string',
        FilterExpression='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]
            The case-sensitive name of the new group. Default is a reserved name and names must be unique.
            

    :type FilterExpression: string
    :param FilterExpression: The filter expression defining criteria by which to group traces.

    :rtype: dict
    :return: {
        'Group': {
            'GroupName': 'string',
            'GroupARN': 'string',
            'FilterExpression': 'string'
        }
    }
    
    
    """
    pass

def create_sampling_rule(SamplingRule=None):
    """
    Creates a rule to control sampling behavior for instrumented applications. Services retrieve rules with  GetSamplingRules , and evaluate each rule in ascending order of priority for each request. If a rule matches, the service records a trace, borrowing it from the reservoir size. After 10 seconds, the service reports back to X-Ray with  GetSamplingTargets to get updated versions of each in-use rule. The updated rule contains a trace quota that the service can use instead of borrowing from the reservoir.
    See also: AWS API Documentation
    
    
    :example: response = client.create_sampling_rule(
        SamplingRule={
            'RuleName': 'string',
            'RuleARN': 'string',
            'ResourceARN': 'string',
            'Priority': 123,
            'FixedRate': 123.0,
            'ReservoirSize': 123,
            'ServiceName': 'string',
            'ServiceType': 'string',
            'Host': 'string',
            'HTTPMethod': 'string',
            'URLPath': 'string',
            'Version': 123,
            'Attributes': {
                'string': 'string'
            }
        }
    )
    
    
    :type SamplingRule: dict
    :param SamplingRule: [REQUIRED]
            The rule definition.
            RuleName (string) --The name of the sampling rule. Specify a rule by either name or ARN, but not both.
            RuleARN (string) --The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.
            ResourceARN (string) -- [REQUIRED]Matches the ARN of the AWS resource on which the service runs.
            Priority (integer) -- [REQUIRED]The priority of the sampling rule.
            FixedRate (float) -- [REQUIRED]The percentage of matching requests to instrument, after the reservoir is exhausted.
            ReservoirSize (integer) -- [REQUIRED]A fixed number of matching requests to instrument per second, prior to applying the fixed rate. The reservoir is not used directly by services, but applies to all services using the rule collectively.
            ServiceName (string) -- [REQUIRED]Matches the name that the service uses to identify itself in segments.
            ServiceType (string) -- [REQUIRED]Matches the origin that the service uses to identify its type in segments.
            Host (string) -- [REQUIRED]Matches the hostname from a request URL.
            HTTPMethod (string) -- [REQUIRED]Matches the HTTP method of a request.
            URLPath (string) -- [REQUIRED]Matches the path from a request URL.
            Version (integer) -- [REQUIRED]The version of the sampling rule format (1 ).
            Attributes (dict) --Matches attributes derived from the request.
            (string) --
            (string) --
            
            

    :rtype: dict
    :return: {
        'SamplingRuleRecord': {
            'SamplingRule': {
                'RuleName': 'string',
                'RuleARN': 'string',
                'ResourceARN': 'string',
                'Priority': 123,
                'FixedRate': 123.0,
                'ReservoirSize': 123,
                'ServiceName': 'string',
                'ServiceType': 'string',
                'Host': 'string',
                'HTTPMethod': 'string',
                'URLPath': 'string',
                'Version': 123,
                'Attributes': {
                    'string': 'string'
                }
            },
            'CreatedAt': datetime(2015, 1, 1),
            'ModifiedAt': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def delete_group(GroupName=None, GroupARN=None):
    """
    Deletes a group resource.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_group(
        GroupName='string',
        GroupARN='string'
    )
    
    
    :type GroupName: string
    :param GroupName: The case-sensitive name of the group.

    :type GroupARN: string
    :param GroupARN: The ARN of the group that was generated on creation.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_sampling_rule(RuleName=None, RuleARN=None):
    """
    Deletes a sampling rule.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_sampling_rule(
        RuleName='string',
        RuleARN='string'
    )
    
    
    :type RuleName: string
    :param RuleName: The name of the sampling rule. Specify a rule by either name or ARN, but not both.

    :type RuleARN: string
    :param RuleARN: The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.

    :rtype: dict
    :return: {
        'SamplingRuleRecord': {
            'SamplingRule': {
                'RuleName': 'string',
                'RuleARN': 'string',
                'ResourceARN': 'string',
                'Priority': 123,
                'FixedRate': 123.0,
                'ReservoirSize': 123,
                'ServiceName': 'string',
                'ServiceType': 'string',
                'Host': 'string',
                'HTTPMethod': 'string',
                'URLPath': 'string',
                'Version': 123,
                'Attributes': {
                    'string': 'string'
                }
            },
            'CreatedAt': datetime(2015, 1, 1),
            'ModifiedAt': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
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

def get_encryption_config():
    """
    Retrieves the current encryption configuration for X-Ray data.
    See also: AWS API Documentation
    
    
    :example: response = client.get_encryption_config()
    
    
    :rtype: dict
    :return: {
        'EncryptionConfig': {
            'KeyId': 'string',
            'Status': 'UPDATING'|'ACTIVE',
            'Type': 'NONE'|'KMS'
        }
    }
    
    
    """
    pass

def get_group(GroupName=None, GroupARN=None):
    """
    Retrieves group resource details.
    See also: AWS API Documentation
    
    
    :example: response = client.get_group(
        GroupName='string',
        GroupARN='string'
    )
    
    
    :type GroupName: string
    :param GroupName: The case-sensitive name of the group.

    :type GroupARN: string
    :param GroupARN: The ARN of the group that was generated on creation.

    :rtype: dict
    :return: {
        'Group': {
            'GroupName': 'string',
            'GroupARN': 'string',
            'FilterExpression': 'string'
        }
    }
    
    
    """
    pass

def get_groups(NextToken=None):
    """
    Retrieves all active group details.
    See also: AWS API Documentation
    
    
    :example: response = client.get_groups(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: Pagination token. Not used.

    :rtype: dict
    :return: {
        'Groups': [
            {
                'GroupName': 'string',
                'GroupARN': 'string',
                'FilterExpression': 'string'
            },
        ],
        'NextToken': 'string'
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

def get_sampling_rules(NextToken=None):
    """
    Retrieves all sampling rules.
    See also: AWS API Documentation
    
    
    :example: response = client.get_sampling_rules(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: Pagination token. Not used.

    :rtype: dict
    :return: {
        'SamplingRuleRecords': [
            {
                'SamplingRule': {
                    'RuleName': 'string',
                    'RuleARN': 'string',
                    'ResourceARN': 'string',
                    'Priority': 123,
                    'FixedRate': 123.0,
                    'ReservoirSize': 123,
                    'ServiceName': 'string',
                    'ServiceType': 'string',
                    'Host': 'string',
                    'HTTPMethod': 'string',
                    'URLPath': 'string',
                    'Version': 123,
                    'Attributes': {
                        'string': 'string'
                    }
                },
                'CreatedAt': datetime(2015, 1, 1),
                'ModifiedAt': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def get_sampling_statistic_summaries(NextToken=None):
    """
    Retrieves information about recent sampling results for all sampling rules.
    See also: AWS API Documentation
    
    
    :example: response = client.get_sampling_statistic_summaries(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: Pagination token. Not used.

    :rtype: dict
    :return: {
        'SamplingStatisticSummaries': [
            {
                'RuleName': 'string',
                'Timestamp': datetime(2015, 1, 1),
                'RequestCount': 123,
                'BorrowCount': 123,
                'SampledCount': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def get_sampling_targets(SamplingStatisticsDocuments=None):
    """
    Requests a sampling quota for rules that the service is using to sample requests.
    See also: AWS API Documentation
    
    
    :example: response = client.get_sampling_targets(
        SamplingStatisticsDocuments=[
            {
                'RuleName': 'string',
                'ClientID': 'string',
                'Timestamp': datetime(2015, 1, 1),
                'RequestCount': 123,
                'SampledCount': 123,
                'BorrowCount': 123
            },
        ]
    )
    
    
    :type SamplingStatisticsDocuments: list
    :param SamplingStatisticsDocuments: [REQUIRED]
            Information about rules that the service is using to sample requests.
            (dict) --Request sampling results for a single rule from a service. Results are for the last 10 seconds unless the service has been assigned a longer reporting interval after a previous call to GetSamplingTargets .
            RuleName (string) -- [REQUIRED]The name of the sampling rule.
            ClientID (string) -- [REQUIRED]A unique identifier for the service in hexadecimal.
            Timestamp (datetime) -- [REQUIRED]The current time.
            RequestCount (integer) -- [REQUIRED]The number of requests that matched the rule.
            SampledCount (integer) -- [REQUIRED]The number of requests recorded.
            BorrowCount (integer) --The number of requests recorded with borrowed reservoir quota.
            
            

    :rtype: dict
    :return: {
        'SamplingTargetDocuments': [
            {
                'RuleName': 'string',
                'FixedRate': 123.0,
                'ReservoirQuota': 123,
                'ReservoirQuotaTTL': datetime(2015, 1, 1),
                'Interval': 123
            },
        ],
        'LastRuleModification': datetime(2015, 1, 1),
        'UnprocessedStatistics': [
            {
                'RuleName': 'string',
                'ErrorCode': 'string',
                'Message': 'string'
            },
        ]
    }
    
    
    """
    pass

def get_service_graph(StartTime=None, EndTime=None, GroupName=None, GroupARN=None, NextToken=None):
    """
    Retrieves a document that describes services that process incoming requests, and downstream services that they call as a result. Root services process incoming requests and make calls to downstream services. Root services are applications that use the AWS X-Ray SDK. Downstream services can be other applications, AWS resources, HTTP web APIs, or SQL databases.
    See also: AWS API Documentation
    
    
    :example: response = client.get_service_graph(
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        GroupName='string',
        GroupARN='string',
        NextToken='string'
    )
    
    
    :type StartTime: datetime
    :param StartTime: [REQUIRED]
            The start of the time frame for which to generate a graph.
            

    :type EndTime: datetime
    :param EndTime: [REQUIRED]
            The end of the timeframe for which to generate a graph.
            

    :type GroupName: string
    :param GroupName: The name of a group to generate a graph based on.

    :type GroupARN: string
    :param GroupARN: The ARN of a group to generate a graph based on.

    :type NextToken: string
    :param NextToken: Pagination token. Not used.

    :rtype: dict
    :return: {
        'StartTime': datetime(2015, 1, 1),
        'EndTime': datetime(2015, 1, 1),
        'Services': [
            {
                'ReferenceId': 123,
                'Name': 'string',
                'Names': [
                    'string',
                ],
                'Root': True|False,
                'AccountId': 'string',
                'Type': 'string',
                'State': 'string',
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'Edges': [
                    {
                        'ReferenceId': 123,
                        'StartTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'SummaryStatistics': {
                            'OkCount': 123,
                            'ErrorStatistics': {
                                'ThrottleCount': 123,
                                'OtherCount': 123,
                                'TotalCount': 123
                            },
                            'FaultStatistics': {
                                'OtherCount': 123,
                                'TotalCount': 123
                            },
                            'TotalCount': 123,
                            'TotalResponseTime': 123.0
                        },
                        'ResponseTimeHistogram': [
                            {
                                'Value': 123.0,
                                'Count': 123
                            },
                        ],
                        'Aliases': [
                            {
                                'Name': 'string',
                                'Names': [
                                    'string',
                                ],
                                'Type': 'string'
                            },
                        ]
                    },
                ],
                'SummaryStatistics': {
                    'OkCount': 123,
                    'ErrorStatistics': {
                        'ThrottleCount': 123,
                        'OtherCount': 123,
                        'TotalCount': 123
                    },
                    'FaultStatistics': {
                        'OtherCount': 123,
                        'TotalCount': 123
                    },
                    'TotalCount': 123,
                    'TotalResponseTime': 123.0
                },
                'DurationHistogram': [
                    {
                        'Value': 123.0,
                        'Count': 123
                    },
                ],
                'ResponseTimeHistogram': [
                    {
                        'Value': 123.0,
                        'Count': 123
                    },
                ]
            },
        ],
        'ContainsOldGroupVersions': True|False,
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_trace_graph(TraceIds=None, NextToken=None):
    """
    Retrieves a service graph for one or more specific trace IDs.
    See also: AWS API Documentation
    
    
    :example: response = client.get_trace_graph(
        TraceIds=[
            'string',
        ],
        NextToken='string'
    )
    
    
    :type TraceIds: list
    :param TraceIds: [REQUIRED]
            Trace IDs of requests for which to generate a service graph.
            (string) --
            

    :type NextToken: string
    :param NextToken: Pagination token. Not used.

    :rtype: dict
    :return: {
        'Services': [
            {
                'ReferenceId': 123,
                'Name': 'string',
                'Names': [
                    'string',
                ],
                'Root': True|False,
                'AccountId': 'string',
                'Type': 'string',
                'State': 'string',
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'Edges': [
                    {
                        'ReferenceId': 123,
                        'StartTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'SummaryStatistics': {
                            'OkCount': 123,
                            'ErrorStatistics': {
                                'ThrottleCount': 123,
                                'OtherCount': 123,
                                'TotalCount': 123
                            },
                            'FaultStatistics': {
                                'OtherCount': 123,
                                'TotalCount': 123
                            },
                            'TotalCount': 123,
                            'TotalResponseTime': 123.0
                        },
                        'ResponseTimeHistogram': [
                            {
                                'Value': 123.0,
                                'Count': 123
                            },
                        ],
                        'Aliases': [
                            {
                                'Name': 'string',
                                'Names': [
                                    'string',
                                ],
                                'Type': 'string'
                            },
                        ]
                    },
                ],
                'SummaryStatistics': {
                    'OkCount': 123,
                    'ErrorStatistics': {
                        'ThrottleCount': 123,
                        'OtherCount': 123,
                        'TotalCount': 123
                    },
                    'FaultStatistics': {
                        'OtherCount': 123,
                        'TotalCount': 123
                    },
                    'TotalCount': 123,
                    'TotalResponseTime': 123.0
                },
                'DurationHistogram': [
                    {
                        'Value': 123.0,
                        'Count': 123
                    },
                ],
                'ResponseTimeHistogram': [
                    {
                        'Value': 123.0,
                        'Count': 123
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_trace_summaries(StartTime=None, EndTime=None, Sampling=None, FilterExpression=None, NextToken=None):
    """
    Retrieves IDs and metadata for traces available for a specified time frame using an optional filter. To get the full traces, pass the trace IDs to BatchGetTraces .
    A filter expression can target traced requests that hit specific service nodes or edges, have errors, or come from a known user. For example, the following filter expression targets traces that pass through api.example.com :
    This filter expression finds traces that have an annotation named account with the value 12345 :
    For a full list of indexed fields and keywords that you can use in filter expressions, see Using Filter Expressions in the AWS X-Ray Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.get_trace_summaries(
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        Sampling=True|False,
        FilterExpression='string',
        NextToken='string'
    )
    
    
    :type StartTime: datetime
    :param StartTime: [REQUIRED]
            The start of the time frame for which to retrieve traces.
            

    :type EndTime: datetime
    :param EndTime: [REQUIRED]
            The end of the time frame for which to retrieve traces.
            

    :type Sampling: boolean
    :param Sampling: Set to true to get summaries for only a subset of available traces.

    :type FilterExpression: string
    :param FilterExpression: Specify a filter expression to retrieve trace summaries for services or requests that meet certain requirements.

    :type NextToken: string
    :param NextToken: Specify the pagination token returned by a previous request to retrieve the next page of results.

    :rtype: dict
    :return: {
        'TraceSummaries': [
            {
                'Id': 'string',
                'Duration': 123.0,
                'ResponseTime': 123.0,
                'HasFault': True|False,
                'HasError': True|False,
                'HasThrottle': True|False,
                'IsPartial': True|False,
                'Http': {
                    'HttpURL': 'string',
                    'HttpStatus': 123,
                    'HttpMethod': 'string',
                    'UserAgent': 'string',
                    'ClientIp': 'string'
                },
                'Annotations': {
                    'string': [
                        {
                            'AnnotationValue': {
                                'NumberValue': 123.0,
                                'BooleanValue': True|False,
                                'StringValue': 'string'
                            },
                            'ServiceIds': [
                                {
                                    'Name': 'string',
                                    'Names': [
                                        'string',
                                    ],
                                    'AccountId': 'string',
                                    'Type': 'string'
                                },
                            ]
                        },
                    ]
                },
                'Users': [
                    {
                        'UserName': 'string',
                        'ServiceIds': [
                            {
                                'Name': 'string',
                                'Names': [
                                    'string',
                                ],
                                'AccountId': 'string',
                                'Type': 'string'
                            },
                        ]
                    },
                ],
                'ServiceIds': [
                    {
                        'Name': 'string',
                        'Names': [
                            'string',
                        ],
                        'AccountId': 'string',
                        'Type': 'string'
                    },
                ],
                'ResourceARNs': [
                    {
                        'ARN': 'string'
                    },
                ],
                'InstanceIds': [
                    {
                        'Id': 'string'
                    },
                ],
                'AvailabilityZones': [
                    {
                        'Name': 'string'
                    },
                ],
                'EntryPoint': {
                    'Name': 'string',
                    'Names': [
                        'string',
                    ],
                    'AccountId': 'string',
                    'Type': 'string'
                },
                'FaultRootCauses': [
                    {
                        'Services': [
                            {
                                'Name': 'string',
                                'Names': [
                                    'string',
                                ],
                                'Type': 'string',
                                'AccountId': 'string',
                                'EntityPath': [
                                    {
                                        'Name': 'string',
                                        'Exceptions': [
                                            {
                                                'Name': 'string',
                                                'Message': 'string'
                                            },
                                        ],
                                        'Remote': True|False
                                    },
                                ],
                                'Inferred': True|False
                            },
                        ]
                    },
                ],
                'ErrorRootCauses': [
                    {
                        'Services': [
                            {
                                'Name': 'string',
                                'Names': [
                                    'string',
                                ],
                                'Type': 'string',
                                'AccountId': 'string',
                                'EntityPath': [
                                    {
                                        'Name': 'string',
                                        'Exceptions': [
                                            {
                                                'Name': 'string',
                                                'Message': 'string'
                                            },
                                        ],
                                        'Remote': True|False
                                    },
                                ],
                                'Inferred': True|False
                            },
                        ]
                    },
                ],
                'ResponseTimeRootCauses': [
                    {
                        'Services': [
                            {
                                'Name': 'string',
                                'Names': [
                                    'string',
                                ],
                                'Type': 'string',
                                'AccountId': 'string',
                                'EntityPath': [
                                    {
                                        'Name': 'string',
                                        'Coverage': 123.0,
                                        'Remote': True|False
                                    },
                                ],
                                'Inferred': True|False
                            },
                        ]
                    },
                ],
                'Revision': 123
            },
        ],
        'ApproximateTime': datetime(2015, 1, 1),
        'TracesProcessedCount': 123,
        'NextToken': 'string'
    }
    
    
    :returns: 
    (dict) --
    Name (string) --
    Names (list) --
    (string) --
    
    
    AccountId (string) --
    Type (string) --
    
    
    
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

def put_encryption_config(KeyId=None, Type=None):
    """
    Updates the encryption configuration for X-Ray data.
    See also: AWS API Documentation
    
    
    :example: response = client.put_encryption_config(
        KeyId='string',
        Type='NONE'|'KMS'
    )
    
    
    :type KeyId: string
    :param KeyId: An AWS KMS customer master key (CMK) in one of the following formats:
            Alias - The name of the key. For example, alias/MyKey .
            Key ID - The KMS key ID of the key. For example, ae4aa6d49-a4d8-9df9-a475-4ff6d7898456 .
            ARN - The full Amazon Resource Name of the key ID or alias. For example, arn:aws:kms:us-east-2:123456789012:key/ae4aa6d49-a4d8-9df9-a475-4ff6d7898456 . Use this format to specify a key in a different account.
            Omit this key if you set Type to NONE .
            

    :type Type: string
    :param Type: [REQUIRED]
            The type of encryption. Set to KMS to use your own key for encryption. Set to NONE for default encryption.
            

    :rtype: dict
    :return: {
        'EncryptionConfig': {
            'KeyId': 'string',
            'Status': 'UPDATING'|'ACTIVE',
            'Type': 'NONE'|'KMS'
        }
    }
    
    
    """
    pass

def put_telemetry_records(TelemetryRecords=None, EC2InstanceId=None, Hostname=None, ResourceARN=None):
    """
    Used by the AWS X-Ray daemon to upload telemetry.
    See also: AWS API Documentation
    
    
    :example: response = client.put_telemetry_records(
        TelemetryRecords=[
            {
                'Timestamp': datetime(2015, 1, 1),
                'SegmentsReceivedCount': 123,
                'SegmentsSentCount': 123,
                'SegmentsSpilloverCount': 123,
                'SegmentsRejectedCount': 123,
                'BackendConnectionErrors': {
                    'TimeoutCount': 123,
                    'ConnectionRefusedCount': 123,
                    'HTTPCode4XXCount': 123,
                    'HTTPCode5XXCount': 123,
                    'UnknownHostCount': 123,
                    'OtherCount': 123
                }
            },
        ],
        EC2InstanceId='string',
        Hostname='string',
        ResourceARN='string'
    )
    
    
    :type TelemetryRecords: list
    :param TelemetryRecords: [REQUIRED]
            (dict) --
            Timestamp (datetime) -- [REQUIRED]
            SegmentsReceivedCount (integer) --
            SegmentsSentCount (integer) --
            SegmentsSpilloverCount (integer) --
            SegmentsRejectedCount (integer) --
            BackendConnectionErrors (dict) --
            TimeoutCount (integer) --
            ConnectionRefusedCount (integer) --
            HTTPCode4XXCount (integer) --
            HTTPCode5XXCount (integer) --
            UnknownHostCount (integer) --
            OtherCount (integer) --
            
            

    :type EC2InstanceId: string
    :param EC2InstanceId: 

    :type Hostname: string
    :param Hostname: 

    :type ResourceARN: string
    :param ResourceARN: 

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def put_trace_segments(TraceSegmentDocuments=None):
    """
    Uploads segment documents to AWS X-Ray. The X-Ray SDK generates segment documents and sends them to the X-Ray daemon, which uploads them in batches. A segment document can be a completed segment, an in-progress segment, or an array of subsegments.
    Segments must include the following fields. For the full segment document schema, see AWS X-Ray Segment Documents in the AWS X-Ray Developer Guide .
    A trace_id consists of three numbers separated by hyphens. For example, 1-58406520-a006649127e371903a2de979. This includes:
    See also: AWS API Documentation
    
    
    :example: response = client.put_trace_segments(
        TraceSegmentDocuments=[
            'string',
        ]
    )
    
    
    :type TraceSegmentDocuments: list
    :param TraceSegmentDocuments: [REQUIRED]
            A string containing a JSON document defining one or more segments or subsegments.
            (string) --
            

    :rtype: dict
    :return: {
        'UnprocessedTraceSegments': [
            {
                'Id': 'string',
                'ErrorCode': 'string',
                'Message': 'string'
            },
        ]
    }
    
    
    :returns: 
    The version number, i.e. 1 .
    The time of the original request, in Unix epoch time, in 8 hexadecimal digits. For example, 10:00AM December 2nd, 2016 PST in epoch time is 1480615200 seconds, or 58406520 in hexadecimal.
    A 96-bit identifier for the trace, globally unique, in 24 hexadecimal digits.
    
    """
    pass

def update_group(GroupName=None, GroupARN=None, FilterExpression=None):
    """
    Updates a group resource.
    See also: AWS API Documentation
    
    
    :example: response = client.update_group(
        GroupName='string',
        GroupARN='string',
        FilterExpression='string'
    )
    
    
    :type GroupName: string
    :param GroupName: The case-sensitive name of the group.

    :type GroupARN: string
    :param GroupARN: The ARN that was generated upon creation.

    :type FilterExpression: string
    :param FilterExpression: The updated filter expression defining criteria by which to group traces.

    :rtype: dict
    :return: {
        'Group': {
            'GroupName': 'string',
            'GroupARN': 'string',
            'FilterExpression': 'string'
        }
    }
    
    
    """
    pass

def update_sampling_rule(SamplingRuleUpdate=None):
    """
    Modifies a sampling rule's configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.update_sampling_rule(
        SamplingRuleUpdate={
            'RuleName': 'string',
            'RuleARN': 'string',
            'ResourceARN': 'string',
            'Priority': 123,
            'FixedRate': 123.0,
            'ReservoirSize': 123,
            'Host': 'string',
            'ServiceName': 'string',
            'ServiceType': 'string',
            'HTTPMethod': 'string',
            'URLPath': 'string',
            'Attributes': {
                'string': 'string'
            }
        }
    )
    
    
    :type SamplingRuleUpdate: dict
    :param SamplingRuleUpdate: [REQUIRED]
            The rule and fields to change.
            RuleName (string) --The name of the sampling rule. Specify a rule by either name or ARN, but not both.
            RuleARN (string) --The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.
            ResourceARN (string) --Matches the ARN of the AWS resource on which the service runs.
            Priority (integer) --The priority of the sampling rule.
            FixedRate (float) --The percentage of matching requests to instrument, after the reservoir is exhausted.
            ReservoirSize (integer) --A fixed number of matching requests to instrument per second, prior to applying the fixed rate. The reservoir is not used directly by services, but applies to all services using the rule collectively.
            Host (string) --Matches the hostname from a request URL.
            ServiceName (string) --Matches the name that the service uses to identify itself in segments.
            ServiceType (string) --Matches the origin that the service uses to identify its type in segments.
            HTTPMethod (string) --Matches the HTTP method of a request.
            URLPath (string) --Matches the path from a request URL.
            Attributes (dict) --Matches attributes derived from the request.
            (string) --
            (string) --
            
            

    :rtype: dict
    :return: {
        'SamplingRuleRecord': {
            'SamplingRule': {
                'RuleName': 'string',
                'RuleARN': 'string',
                'ResourceARN': 'string',
                'Priority': 123,
                'FixedRate': 123.0,
                'ReservoirSize': 123,
                'ServiceName': 'string',
                'ServiceType': 'string',
                'Host': 'string',
                'HTTPMethod': 'string',
                'URLPath': 'string',
                'Version': 123,
                'Attributes': {
                    'string': 'string'
                }
            },
            'CreatedAt': datetime(2015, 1, 1),
            'ModifiedAt': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

