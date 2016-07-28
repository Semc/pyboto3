"""
The MIT License (MIT)

Copyright (c) 2016 Gehad Shaat

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
"""

import boto3


class Logs(object):
    def __init__(self):
        self.client = boto3.client('Logs')

    def can_paginate(self, operation_name=None):
        """
        :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').
            ReturnsTrue if the operation can be paginated,
            False otherwise.
            
        :type operation_name: string
        """
        self.client.can_paginate(operation_name=operation_name)

    def cancel_export_task(self, taskId=None):
        """
        :param taskId: [REQUIRED]
            Id of the export task to cancel.
            ReturnsNone
            
        :type taskId: string
        """
        self.client.cancel_export_task(taskId=taskId)

    def create_export_task(self, taskName=None, logGroupName=None, logStreamNamePrefix=None, fromTime=None, to=None,
                           destination=None, destinationPrefix=None):
        """
        :param taskName: The name of the export task.
        :type taskName: string
        :param logGroupName: [REQUIRED]
            The name of the log group to export.
            
        :type logGroupName: string
        :param logStreamNamePrefix: Will only export log streams that match the provided logStreamNamePrefix. If you don't specify a value, no prefix filter is applied.
        :type logStreamNamePrefix: string
        :param fromTime: [REQUIRED]
            A point in time expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC. It indicates the start time of the range for the request. Events with a timestamp prior to this time will not be exported.
            
        :type fromTime: integer
        :param to: [REQUIRED]
            A point in time expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC. It indicates the end time of the range for the request. Events with a timestamp later than this time will not be exported.
            
        :type to: integer
        :param destination: [REQUIRED]
            Name of Amazon S3 bucket to which the log data will be exported.
            Note: Only buckets in the same AWS region are supported.
            
        :type destination: string
        :param destinationPrefix: Prefix that will be used as the start of Amazon S3 key for every object exported. If not specified, this defaults to 'exportedlogs'.
        :type destinationPrefix: string
        """
        self.client.create_export_task(taskName=taskName, logGroupName=logGroupName,
                                       logStreamNamePrefix=logStreamNamePrefix, fromTime=fromTime, to=to,
                                       destination=destination, destinationPrefix=destinationPrefix)

    def create_log_group(self, logGroupName=None):
        """
        :param logGroupName: [REQUIRED]
            The name of the log group to create.
            ReturnsNone
            
        :type logGroupName: string
        """
        self.client.create_log_group(logGroupName=logGroupName)

    def create_log_stream(self, logGroupName=None, logStreamName=None):
        """
        :param logGroupName: [REQUIRED]
            The name of the log group under which the log stream is to be created.
            
        :type logGroupName: string
        :param logStreamName: [REQUIRED]
            The name of the log stream to create.
            
        :type logStreamName: string
        """
        self.client.create_log_stream(logGroupName=logGroupName, logStreamName=logStreamName)

    def delete_destination(self, destinationName=None):
        """
        :param destinationName: [REQUIRED]
            The name of destination to delete.
            ReturnsNone
            
        :type destinationName: string
        """
        self.client.delete_destination(destinationName=destinationName)

    def delete_log_group(self, logGroupName=None):
        """
        :param logGroupName: [REQUIRED]
            The name of the log group to delete.
            ReturnsNone
            
        :type logGroupName: string
        """
        self.client.delete_log_group(logGroupName=logGroupName)

    def delete_log_stream(self, logGroupName=None, logStreamName=None):
        """
        :param logGroupName: [REQUIRED]
            The name of the log group under which the log stream to delete belongs.
            
        :type logGroupName: string
        :param logStreamName: [REQUIRED]
            The name of the log stream to delete.
            
        :type logStreamName: string
        """
        self.client.delete_log_stream(logGroupName=logGroupName, logStreamName=logStreamName)

    def delete_metric_filter(self, logGroupName=None, filterName=None):
        """
        :param logGroupName: [REQUIRED]
            The name of the log group that is associated with the metric filter to delete.
            
        :type logGroupName: string
        :param filterName: [REQUIRED]
            The name of the metric filter to delete.
            
        :type filterName: string
        """
        self.client.delete_metric_filter(logGroupName=logGroupName, filterName=filterName)

    def delete_retention_policy(self, logGroupName=None):
        """
        :param logGroupName: [REQUIRED]
            The name of the log group that is associated with the retention policy to delete.
            ReturnsNone
            
        :type logGroupName: string
        """
        self.client.delete_retention_policy(logGroupName=logGroupName)

    def delete_subscription_filter(self, logGroupName=None, filterName=None):
        """
        :param logGroupName: [REQUIRED]
            The name of the log group that is associated with the subscription filter to delete.
            
        :type logGroupName: string
        :param filterName: [REQUIRED]
            The name of the subscription filter to delete.
            
        :type filterName: string
        """
        self.client.delete_subscription_filter(logGroupName=logGroupName, filterName=filterName)

    def describe_destinations(self, DestinationNamePrefix=None, nextToken=None, limit=None):
        """
        :param DestinationNamePrefix: Will only return destinations that match the provided destinationNamePrefix. If you don't specify a value, no prefix is applied.
        :type DestinationNamePrefix: string
        :param nextToken: A string token used for pagination that points to the next page of results. It must be a value obtained from the response of the previous request. The token expires after 24 hours.
        :type nextToken: string
        :param limit: The maximum number of results to return.
        :type limit: integer
        """
        self.client.describe_destinations(DestinationNamePrefix=DestinationNamePrefix, nextToken=nextToken, limit=limit)

    def describe_export_tasks(self, taskId=None, statusCode=None, nextToken=None, limit=None):
        """
        :param taskId: Export task that matches the specified task Id will be returned. This can result in zero or one export task.
        :type taskId: string
        :param statusCode: All export tasks that matches the specified status code will be returned. This can return zero or more export tasks.
        :type statusCode: string
        :param nextToken: A string token used for pagination that points to the next page of results. It must be a value obtained from the response of the previous DescribeExportTasks request.
        :type nextToken: string
        :param limit: The maximum number of items returned in the response. If you don't specify a value, the request would return up to 50 items.
        :type limit: integer
        """
        self.client.describe_export_tasks(taskId=taskId, statusCode=statusCode, nextToken=nextToken, limit=limit)

    def describe_log_groups(self, logGroupNamePrefix=None, nextToken=None, limit=None):
        """
        :param logGroupNamePrefix: Will only return log groups that match the provided logGroupNamePrefix. If you don't specify a value, no prefix filter is applied.
        :type logGroupNamePrefix: string
        :param nextToken: A string token used for pagination that points to the next page of results. It must be a value obtained from the response of the previous DescribeLogGroups request.
        :type nextToken: string
        :param limit: The maximum number of items returned in the response. If you don't specify a value, the request would return up to 50 items.
        :type limit: integer
        """
        self.client.describe_log_groups(logGroupNamePrefix=logGroupNamePrefix, nextToken=nextToken, limit=limit)

    def describe_log_streams(self, logGroupName=None, logStreamNamePrefix=None, orderBy=None, descending=None,
                             nextToken=None, limit=None):
        """
        :param logGroupName: [REQUIRED]
            The log group name for which log streams are to be listed.
            
        :type logGroupName: string
        :param logStreamNamePrefix: Will only return log streams that match the provided logStreamNamePrefix. If you don't specify a value, no prefix filter is applied.
        :type logStreamNamePrefix: string
        :param orderBy: Specifies what to order the returned log streams by. Valid arguments are 'LogStreamName' or 'LastEventTime'. If you don't specify a value, results are ordered by LogStreamName. If 'LastEventTime' is chosen, the request cannot also contain a logStreamNamePrefix.
        :type orderBy: string
        :param descending: If set to true, results are returned in descending order. If you don't specify a value or set it to false, results are returned in ascending order.
        :type descending: boolean
        :param nextToken: A string token used for pagination that points to the next page of results. It must be a value obtained from the response of the previous DescribeLogStreams request.
        :type nextToken: string
        :param limit: The maximum number of items returned in the response. If you don't specify a value, the request would return up to 50 items.
        :type limit: integer
        """
        self.client.describe_log_streams(logGroupName=logGroupName, logStreamNamePrefix=logStreamNamePrefix,
                                         orderBy=orderBy, descending=descending, nextToken=nextToken, limit=limit)

    def describe_metric_filters(self, logGroupName=None, filterNamePrefix=None, nextToken=None, limit=None):
        """
        :param logGroupName: [REQUIRED]
            The log group name for which metric filters are to be listed.
            
        :type logGroupName: string
        :param filterNamePrefix: Will only return metric filters that match the provided filterNamePrefix. If you don't specify a value, no prefix filter is applied.
        :type filterNamePrefix: string
        :param nextToken: A string token used for pagination that points to the next page of results. It must be a value obtained from the response of the previous DescribeMetricFilters request.
        :type nextToken: string
        :param limit: The maximum number of items returned in the response. If you don't specify a value, the request would return up to 50 items.
        :type limit: integer
        """
        self.client.describe_metric_filters(logGroupName=logGroupName, filterNamePrefix=filterNamePrefix,
                                            nextToken=nextToken, limit=limit)

    def describe_subscription_filters(self, logGroupName=None, filterNamePrefix=None, nextToken=None, limit=None):
        """
        :param logGroupName: [REQUIRED]
            The log group name for which subscription filters are to be listed.
            
        :type logGroupName: string
        :param filterNamePrefix: Will only return subscription filters that match the provided filterNamePrefix. If you don't specify a value, no prefix filter is applied.
        :type filterNamePrefix: string
        :param nextToken: A string token used for pagination that points to the next page of results. It must be a value obtained from the response of the previous request. The token expires after 24 hours.
        :type nextToken: string
        :param limit: The maximum number of results to return.
        :type limit: integer
        """
        self.client.describe_subscription_filters(logGroupName=logGroupName, filterNamePrefix=filterNamePrefix,
                                                  nextToken=nextToken, limit=limit)

    def filter_log_events(self, logGroupName=None, logStreamNames=None, startTime=None, endTime=None,
                          filterPattern=None, nextToken=None, limit=None, interleaved=None):
        """
        :param logGroupName: [REQUIRED]
            The name of the log group to query.
            
        :type logGroupName: string
        :param logStreamNames: Optional list of log stream names within the specified log group to search. Defaults to all the log streams in the log group.
            (string) --
            
        :type logStreamNames: list
        :param startTime: A point in time expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC. If provided, events with a timestamp prior to this time are not returned.
        :type startTime: integer
        :param endTime: A point in time expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC. If provided, events with a timestamp later than this time are not returned.
        :type endTime: integer
        :param filterPattern: A valid CloudWatch Logs filter pattern to use for filtering the response. If not provided, all the events are matched.
        :type filterPattern: string
        :param nextToken: A pagination token obtained from a FilterLogEvents response to continue paginating the FilterLogEvents results. This token is omitted from the response when there are no other events to display.
        :type nextToken: string
        :param limit: The maximum number of events to return in a page of results. Default is 10,000 events.
        :type limit: integer
        :param interleaved: If provided, the API will make a best effort to provide responses that contain events from multiple log streams within the log group interleaved in a single response. If not provided, all the matched log events in the first log stream will be searched first, then those in the next log stream, etc.
        :type interleaved: boolean
        """
        self.client.filter_log_events(logGroupName=logGroupName, logStreamNames=logStreamNames, startTime=startTime,
                                      endTime=endTime, filterPattern=filterPattern, nextToken=nextToken, limit=limit,
                                      interleaved=interleaved)

    def generate_presigned_url(self, ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
        """
        :param ClientMethod: The client method to presign for
        :type ClientMethod: string
        :param Params: The parameters normally passed to
            ClientMethod.
        :type Params: dict
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)
        :type ExpiresIn: int
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.
        :type HttpMethod: string
        """
        self.client.generate_presigned_url(ClientMethod=ClientMethod, Params=Params, ExpiresIn=ExpiresIn,
                                           HttpMethod=HttpMethod)

    def get_log_events(self, logGroupName=None, logStreamName=None, startTime=None, endTime=None, nextToken=None,
                       limit=None, startFromHead=None):
        """
        :param logGroupName: [REQUIRED]
            The name of the log group to query.
            
        :type logGroupName: string
        :param logStreamName: [REQUIRED]
            The name of the log stream to query.
            
        :type logStreamName: string
        :param startTime: A point in time expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.
        :type startTime: integer
        :param endTime: A point in time expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.
        :type endTime: integer
        :param nextToken: A string token used for pagination that points to the next page of results. It must be a value obtained from the nextForwardToken or nextBackwardToken fields in the response of the previous GetLogEvents request.
        :type nextToken: string
        :param limit: The maximum number of log events returned in the response. If you don't specify a value, the request would return as many log events as can fit in a response size of 1MB, up to 10,000 log events.
        :type limit: integer
        :param startFromHead: If set to true, the earliest log events would be returned first. The default is false (the latest log events are returned first).
        :type startFromHead: boolean
        """
        self.client.get_log_events(logGroupName=logGroupName, logStreamName=logStreamName, startTime=startTime,
                                   endTime=endTime, nextToken=nextToken, limit=limit, startFromHead=startFromHead)

    def get_paginator(self, operation_name=None):
        """
        :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').
            Raises OperationNotPageableErrorRaised if the operation is not
            pageable. You can use the client.can_paginate method to
            check if an operation is pageable.
            Return typeL{botocore.paginate.Paginator}
            ReturnsA paginator object.
            
        :type operation_name: string
        """
        self.client.get_paginator(operation_name=operation_name)

    def get_waiter(self):
        """
        """
        self.client.get_waiter()

    def put_destination(self, destinationName=None, targetArn=None, roleArn=None):
        """
        :param destinationName: [REQUIRED]
            A name for the destination.
            
        :type destinationName: string
        :param targetArn: [REQUIRED]
            The ARN of an Amazon Kinesis stream to deliver matching log events to.
            
        :type targetArn: string
        :param roleArn: [REQUIRED]
            The ARN of an IAM role that grants CloudWatch Logs permissions to do Amazon Kinesis PutRecord requests on the desitnation stream.
            
        :type roleArn: string
        """
        self.client.put_destination(destinationName=destinationName, targetArn=targetArn, roleArn=roleArn)

    def put_destination_policy(self, destinationName=None, accessPolicy=None):
        """
        :param destinationName: [REQUIRED]
            A name for an existing destination.
            
        :type destinationName: string
        :param accessPolicy: [REQUIRED]
            An IAM policy document that authorizes cross-account users to deliver their log events to associated destination.
            
        :type accessPolicy: string
        """
        self.client.put_destination_policy(destinationName=destinationName, accessPolicy=accessPolicy)

    def put_log_events(self, logGroupName=None, logStreamName=None, logEvents=None, sequenceToken=None):
        """
        :param logGroupName: [REQUIRED]
            The name of the log group to put log events to.
            
        :type logGroupName: string
        :param logStreamName: [REQUIRED]
            The name of the log stream to put log events to.
            
        :type logStreamName: string
        :param logEvents: [REQUIRED]
            A list of log events belonging to a log stream.
            (dict) --A log event is a record of some activity that was recorded by the application or resource being monitored. The log event record that CloudWatch Logs understands contains two properties: the timestamp of when the event occurred, and the raw event message.
            timestamp (integer) -- [REQUIRED]A point in time expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.
            message (string) -- [REQUIRED]
            
        :type logEvents: list
        :param sequenceToken: A string token that must be obtained from the response of the previous PutLogEvents request.
        :type sequenceToken: string
        """
        self.client.put_log_events(logGroupName=logGroupName, logStreamName=logStreamName, logEvents=logEvents,
                                   sequenceToken=sequenceToken)

    def put_metric_filter(self, logGroupName=None, filterName=None, filterPattern=None, metricTransformations=None):
        """
        :param logGroupName: [REQUIRED]
            The name of the log group to associate the metric filter with.
            
        :type logGroupName: string
        :param filterName: [REQUIRED]
            A name for the metric filter.
            
        :type filterName: string
        :param filterPattern: [REQUIRED]
            A valid CloudWatch Logs filter pattern for extracting metric data out of ingested log events.
            
        :type filterPattern: string
        :param metricTransformations: [REQUIRED]
            A collection of information needed to define how metric data gets emitted.
            (dict) --
            metricName (string) -- [REQUIRED]The name of the CloudWatch metric to which the monitored log information should be published. For example, you may publish to a metric called ErrorCount.
            metricNamespace (string) -- [REQUIRED]The destination namespace of the new CloudWatch metric.
            metricValue (string) -- [REQUIRED]What to publish to the metric. For example, if you're counting the occurrences of a particular term like 'Error', the value will be '1' for each occurrence. If you're counting the bytes transferred the published value will be the value in the log event.
            
            
        :type metricTransformations: list
        """
        self.client.put_metric_filter(logGroupName=logGroupName, filterName=filterName, filterPattern=filterPattern,
                                      metricTransformations=metricTransformations)

    def put_retention_policy(self, logGroupName=None, retentionInDays=None):
        """
        :param logGroupName: [REQUIRED]
            The name of the log group to associate the retention policy with.
            
        :type logGroupName: string
        :param retentionInDays: [REQUIRED]
            Specifies the number of days you want to retain log events in the specified log group. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, 3653.
            
        :type retentionInDays: integer
        """
        self.client.put_retention_policy(logGroupName=logGroupName, retentionInDays=retentionInDays)

    def put_subscription_filter(self, logGroupName=None, filterName=None, filterPattern=None, destinationArn=None,
                                roleArn=None):
        """
        :param logGroupName: [REQUIRED]
            The name of the log group to associate the subscription filter with.
            
        :type logGroupName: string
        :param filterName: [REQUIRED]
            A name for the subscription filter.
            
        :type filterName: string
        :param filterPattern: [REQUIRED]
            A valid CloudWatch Logs filter pattern for subscribing to a filtered stream of log events.
            
        :type filterPattern: string
        :param destinationArn: [REQUIRED]
            The ARN of the destination to deliver matching log events to. Currently, the supported destinations are:
            An Amazon Kinesis stream belonging to the same account as the subscription filter, for same-account delivery.
            A logical destination (used via an ARN of Destination ) belonging to a different account, for cross-account delivery.
            An Amazon Kinesis Firehose stream belonging to the same account as the subscription filter, for same-account delivery.
            An AWS Lambda function belonging to the same account as the subscription filter, for same-account delivery.
            
        :type destinationArn: string
        :param roleArn: The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination (used via an ARN of Destination ) for cross-account delivery.
        :type roleArn: string
        """
        self.client.put_subscription_filter(logGroupName=logGroupName, filterName=filterName,
                                            filterPattern=filterPattern, destinationArn=destinationArn, roleArn=roleArn)

    def test_metric_filter(self, filterPattern=None, logEventMessages=None):
        """
        :param filterPattern: [REQUIRED]
            A symbolic description of how CloudWatch Logs should interpret the data in each log event. For example, a log event may contain timestamps, IP addresses, strings, and so on. You use the filter pattern to specify what to look for in the log event message.
            
        :type filterPattern: string
        :param logEventMessages: [REQUIRED]
            A list of log event messages to test.
            (string) --
            
        :type logEventMessages: list
        """
        self.client.test_metric_filter(filterPattern=filterPattern, logEventMessages=logEventMessages)