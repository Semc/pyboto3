'''

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

'''

def add_tags_to_stream(StreamName=None, Tags=None):
    """
    Adds or updates tags for the specified Amazon Kinesis stream. Each stream can have up to 10 tags.
    If tags have already been assigned to the stream, AddTagsToStream overwrites any existing tags that correspond to the specified tag keys.
    
    
    :example: response = client.add_tags_to_stream(
        StreamName='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]
            The name of the stream.
            

    :type Tags: dict
    :param Tags: [REQUIRED]
            The set of key-value pairs to use to create the tags.
            (string) --
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

def create_stream(StreamName=None, ShardCount=None):
    """
    Creates an Amazon Kinesis stream. A stream captures and transports data records that are continuously emitted from different data sources or producers . Scale-out within a stream is explicitly supported by means of shards, which are uniquely identified groups of data records in a stream.
    You specify and control the number of shards that a stream is composed of. Each shard can support reads up to 5 transactions per second, up to a maximum data read total of 2 MB per second. Each shard can support writes up to 1,000 records per second, up to a maximum data write total of 1 MB per second. You can add shards to a stream if the amount of data input increases and you can remove shards if the amount of data input decreases.
    The stream name identifies the stream. The name is scoped to the AWS account used by the application. It is also scoped by region. That is, two streams in two different accounts can have the same name, and two streams in the same account, but in two different regions, can have the same name.
    CreateStream is an asynchronous operation. Upon receiving a CreateStream request, Amazon Kinesis immediately returns and sets the stream status to CREATING . After the stream is created, Amazon Kinesis sets the stream status to ACTIVE . You should perform read and write operations only on an ACTIVE stream.
    You receive a LimitExceededException when making a CreateStream request if you try to do one of the following:
    For the default shard limit for an AWS account, see Streams Limits in the Amazon Kinesis Streams Developer Guide . If you need to increase this limit, contact AWS Support .
    You can use DescribeStream to check the stream status, which is returned in StreamStatus .
    
    
    :example: response = client.create_stream(
        StreamName='string',
        ShardCount=123
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]
            A name to identify the stream. The stream name is scoped to the AWS account used by the application that creates the stream. It is also scoped by region. That is, two streams in two different AWS accounts can have the same name, and two streams in the same AWS account but in two different regions can have the same name.
            

    :type ShardCount: integer
    :param ShardCount: [REQUIRED]
            The number of shards that the stream will use. The throughput of the stream is a function of the number of shards; more shards are required for greater provisioned throughput.
            DefaultShardLimit;
            

    :returns: 
    StreamName (string) -- [REQUIRED]
    A name to identify the stream. The stream name is scoped to the AWS account used by the application that creates the stream. It is also scoped by region. That is, two streams in two different AWS accounts can have the same name, and two streams in the same AWS account but in two different regions can have the same name.
    
    ShardCount (integer) -- [REQUIRED]
    The number of shards that the stream will use. The throughput of the stream is a function of the number of shards; more shards are required for greater provisioned throughput.
    DefaultShardLimit;
    
    
    """
    pass

def decrease_stream_retention_period(StreamName=None, RetentionPeriodHours=None):
    """
    Decreases the Amazon Kinesis stream's retention period, which is the length of time data records are accessible after they are added to the stream. The minimum value of a stream's retention period is 24 hours.
    This operation may result in lost data. For example, if the stream's retention period is 48 hours and is decreased to 24 hours, any data already in the stream that is older than 24 hours is inaccessible.
    
    
    :example: response = client.decrease_stream_retention_period(
        StreamName='string',
        RetentionPeriodHours=123
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]
            The name of the stream to modify.
            

    :type RetentionPeriodHours: integer
    :param RetentionPeriodHours: [REQUIRED]
            The new retention period of the stream, in hours. Must be less than the current retention period.
            

    """
    pass

def delete_stream(StreamName=None):
    """
    Deletes an Amazon Kinesis stream and all its shards and data. You must shut down any applications that are operating on the stream before you delete the stream. If an application attempts to operate on a deleted stream, it will receive the exception ResourceNotFoundException .
    If the stream is in the ACTIVE state, you can delete it. After a DeleteStream request, the specified stream is in the DELETING state until Amazon Kinesis completes the deletion.
    Note: Amazon Kinesis might continue to accept data read and write operations, such as  PutRecord ,  PutRecords , and  GetRecords , on a stream in the DELETING state until the stream deletion is complete.
    When you delete a stream, any shards in that stream are also deleted, and any tags are dissociated from the stream.
    You can use the  DescribeStream operation to check the state of the stream, which is returned in StreamStatus .
    
    
    :example: response = client.delete_stream(
        StreamName='string'
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]
            The name of the stream to delete.
            

    """
    pass

def describe_stream(StreamName=None, Limit=None, ExclusiveStartShardId=None):
    """
    Describes the specified Amazon Kinesis stream.
    The information about the stream includes its current status, its Amazon Resource Name (ARN), and an array of shard objects. For each shard object, there is information about the hash key and sequence number ranges that the shard spans, and the IDs of any earlier shards that played in a role in creating the shard. A sequence number is the identifier associated with every record ingested in the stream. The sequence number is assigned when a record is put into the stream.
    You can limit the number of returned shards using the Limit parameter. The number of shards in a stream may be too large to return from a single call to DescribeStream . You can detect this by using the HasMoreShards flag in the returned output. HasMoreShards is set to true when there is more data available.
    DescribeStream is a paginated operation. If there are more shards available, you can request them using the shard ID of the last shard returned. Specify this ID in the ExclusiveStartShardId parameter in a subsequent request to DescribeStream .
    There are no guarantees about the chronological order shards returned in DescribeStream results. If you want to process shards in chronological order, use ParentShardId to track lineage to the oldest shard.
    
    
    :example: response = client.describe_stream(
        StreamName='string',
        Limit=123,
        ExclusiveStartShardId='string'
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]
            The name of the stream to describe.
            

    :type Limit: integer
    :param Limit: The maximum number of shards to return.

    :type ExclusiveStartShardId: string
    :param ExclusiveStartShardId: The shard ID of the shard to start with.

    :rtype: dict
    :return: {
        'StreamDescription': {
            'StreamName': 'string',
            'StreamARN': 'string',
            'StreamStatus': 'CREATING'|'DELETING'|'ACTIVE'|'UPDATING',
            'Shards': [
                {
                    'ShardId': 'string',
                    'ParentShardId': 'string',
                    'AdjacentParentShardId': 'string',
                    'HashKeyRange': {
                        'StartingHashKey': 'string',
                        'EndingHashKey': 'string'
                    },
                    'SequenceNumberRange': {
                        'StartingSequenceNumber': 'string',
                        'EndingSequenceNumber': 'string'
                    }
                },
            ],
            'HasMoreShards': True|False,
            'RetentionPeriodHours': 123,
            'EnhancedMonitoring': [
                {
                    'ShardLevelMetrics': [
                        'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
                    ]
                },
            ]
        }
    }
    
    
    :returns: 
    CREATING - The stream is being created. Amazon Kinesis immediately returns and sets StreamStatus to CREATING .
    DELETING - The stream is being deleted. The specified stream is in the DELETING state until Amazon Kinesis completes the deletion.
    ACTIVE - The stream exists and is ready for read and write operations or deletion. You should perform read and write operations only on an ACTIVE stream.
    UPDATING - Shards in the stream are being merged or split. Read and write operations continue to work while the stream is in the UPDATING state.
    
    """
    pass

def disable_enhanced_monitoring(StreamName=None, ShardLevelMetrics=None):
    """
    Disables enhanced monitoring.
    
    
    :example: response = client.disable_enhanced_monitoring(
        StreamName='string',
        ShardLevelMetrics=[
            'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
        ]
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]
            The name of the Amazon Kinesis stream for which to disable enhanced monitoring.
            

    :type ShardLevelMetrics: list
    :param ShardLevelMetrics: [REQUIRED]
            List of shard-level metrics to disable.
            The following are the valid shard-level metrics. The value 'ALL ' disables every metric.
            IncomingBytes
            IncomingRecords
            OutgoingBytes
            OutgoingRecords
            WriteProvisionedThroughputExceeded
            ReadProvisionedThroughputExceeded
            IteratorAgeMilliseconds
            ALL
            For more information, see Monitoring the Amazon Kinesis Streams Service with Amazon CloudWatch in the Amazon Kinesis Streams Developer Guide .
            (string) --
            

    :rtype: dict
    :return: {
        'StreamName': 'string',
        'CurrentShardLevelMetrics': [
            'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
        ],
        'DesiredShardLevelMetrics': [
            'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def enable_enhanced_monitoring(StreamName=None, ShardLevelMetrics=None):
    """
    Enables enhanced Amazon Kinesis stream monitoring for shard-level metrics.
    
    
    :example: response = client.enable_enhanced_monitoring(
        StreamName='string',
        ShardLevelMetrics=[
            'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
        ]
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]
            The name of the stream for which to enable enhanced monitoring.
            

    :type ShardLevelMetrics: list
    :param ShardLevelMetrics: [REQUIRED]
            List of shard-level metrics to enable.
            The following are the valid shard-level metrics. The value 'ALL ' enables every metric.
            IncomingBytes
            IncomingRecords
            OutgoingBytes
            OutgoingRecords
            WriteProvisionedThroughputExceeded
            ReadProvisionedThroughputExceeded
            IteratorAgeMilliseconds
            ALL
            For more information, see Monitoring the Amazon Kinesis Streams Service with Amazon CloudWatch in the Amazon Kinesis Streams Developer Guide .
            (string) --
            

    :rtype: dict
    :return: {
        'StreamName': 'string',
        'CurrentShardLevelMetrics': [
            'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
        ],
        'DesiredShardLevelMetrics': [
            'IncomingBytes'|'IncomingRecords'|'OutgoingBytes'|'OutgoingRecords'|'WriteProvisionedThroughputExceeded'|'ReadProvisionedThroughputExceeded'|'IteratorAgeMilliseconds'|'ALL',
        ]
    }
    
    
    :returns: 
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

def get_records(ShardIterator=None, Limit=None):
    """
    Gets data records from an Amazon Kinesis stream's shard.
    Specify a shard iterator using the ShardIterator parameter. The shard iterator specifies the position in the shard from which you want to start reading data records sequentially. If there are no records available in the portion of the shard that the iterator points to,  GetRecords returns an empty list. Note that it might take multiple calls to get to a portion of the shard that contains records.
    You can scale by provisioning multiple shards per stream while considering service limits (for more information, see Streams Limits in the Amazon Kinesis Streams Developer Guide ). Your application should have one thread per shard, each reading continuously from its stream. To read from a stream continually, call  GetRecords in a loop. Use  GetShardIterator to get the shard iterator to specify in the first  GetRecords call.  GetRecords returns a new shard iterator in NextShardIterator . Specify the shard iterator returned in NextShardIterator in subsequent calls to  GetRecords . Note that if the shard has been closed, the shard iterator can't return more data and  GetRecords returns null in NextShardIterator . You can terminate the loop when the shard is closed, or when the shard iterator reaches the record with the sequence number or other attribute that marks it as the last record to process.
    Each data record can be up to 1 MB in size, and each shard can read up to 2 MB per second. You can ensure that your calls don't exceed the maximum supported size or throughput by using the Limit parameter to specify the maximum number of records that  GetRecords can return. Consider your average record size when determining this limit.
    The size of the data returned by  GetRecords varies depending on the utilization of the shard. The maximum size of data that  GetRecords can return is 10 MB. If a call returns this amount of data, subsequent calls made within the next 5 seconds throw ProvisionedThroughputExceededException . If there is insufficient provisioned throughput on the shard, subsequent calls made within the next 1 second throw ProvisionedThroughputExceededException . Note that  GetRecords won't return any data when it throws an exception. For this reason, we recommend that you wait one second between calls to  GetRecords ; however, it's possible that the application will get exceptions for longer than 1 second.
    To detect whether the application is falling behind in processing, you can use the MillisBehindLatest response attribute. You can also monitor the stream using CloudWatch metrics and other mechanisms (see Monitoring in the Amazon Kinesis Streams Developer Guide ).
    Each Amazon Kinesis record includes a value, ApproximateArrivalTimestamp , that is set when a stream successfully receives and stores a record. This is commonly referred to as a server-side timestamp, whereas a client-side timestamp is set when a data producer creates or sends the record to a stream (a data producer is any data source putting data records into a stream, for example with  PutRecords ). The timestamp has millisecond precision. There are no guarantees about the timestamp accuracy, or that the timestamp is always increasing. For example, records in a shard or across a stream might have timestamps that are out of order.
    
    
    :example: response = client.get_records(
        ShardIterator='string',
        Limit=123
    )
    
    
    :type ShardIterator: string
    :param ShardIterator: [REQUIRED]
            The position in the shard from which you want to start sequentially reading data records. A shard iterator specifies this position using the sequence number of a data record in the shard.
            

    :type Limit: integer
    :param Limit: The maximum number of records to return. Specify a value of up to 10,000. If you specify a value that is greater than 10,000, GetRecords throws InvalidArgumentException .

    :rtype: dict
    :return: {
        'Records': [
            {
                'SequenceNumber': 'string',
                'ApproximateArrivalTimestamp': datetime(2015, 1, 1),
                'Data': b'bytes',
                'PartitionKey': 'string'
            },
        ],
        'NextShardIterator': 'string',
        'MillisBehindLatest': 123
    }
    
    
    """
    pass

def get_shard_iterator(StreamName=None, ShardId=None, ShardIteratorType=None, StartingSequenceNumber=None, Timestamp=None):
    """
    Gets an Amazon Kinesis shard iterator. A shard iterator expires five minutes after it is returned to the requester.
    A shard iterator specifies the shard position from which to start reading data records sequentially. The position is specified using the sequence number of a data record in a shard. A sequence number is the identifier associated with every record ingested in the stream, and is assigned when a record is put into the stream. Each stream has one or more shards.
    You must specify the shard iterator type. For example, you can set the ShardIteratorType parameter to read exactly from the position denoted by a specific sequence number by using the AT_SEQUENCE_NUMBER shard iterator type, or right after the sequence number by using the AFTER_SEQUENCE_NUMBER shard iterator type, using sequence numbers returned by earlier calls to  PutRecord ,  PutRecords ,  GetRecords , or  DescribeStream . In the request, you can specify the shard iterator type AT_TIMESTAMP to read records from an arbitrary point in time, TRIM_HORIZON to cause ShardIterator to point to the last untrimmed record in the shard in the system (the oldest data record in the shard), or LATEST so that you always read the most recent data in the shard.
    When you read repeatedly from a stream, use a  GetShardIterator request to get the first shard iterator for use in your first  GetRecords request and for subsequent reads use the shard iterator returned by the  GetRecords request in NextShardIterator . A new shard iterator is returned by every  GetRecords request in NextShardIterator , which you use in the ShardIterator parameter of the next  GetRecords request.
    If a  GetShardIterator request is made too often, you receive a ProvisionedThroughputExceededException . For more information about throughput limits, see  GetRecords , and Streams Limits in the Amazon Kinesis Streams Developer Guide .
    If the shard is closed,  GetShardIterator returns a valid iterator for the last sequence number of the shard. Note that a shard can be closed as a result of using  SplitShard or  MergeShards .
    
    
    :example: response = client.get_shard_iterator(
        StreamName='string',
        ShardId='string',
        ShardIteratorType='AT_SEQUENCE_NUMBER'|'AFTER_SEQUENCE_NUMBER'|'TRIM_HORIZON'|'LATEST'|'AT_TIMESTAMP',
        StartingSequenceNumber='string',
        Timestamp=datetime(2015, 1, 1)
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]
            The name of the Amazon Kinesis stream.
            

    :type ShardId: string
    :param ShardId: [REQUIRED]
            The shard ID of the Amazon Kinesis shard to get the iterator for.
            

    :type ShardIteratorType: string
    :param ShardIteratorType: [REQUIRED]
            Determines how the shard iterator is used to start reading data records from the shard.
            The following are the valid Amazon Kinesis shard iterator types:
            AT_SEQUENCE_NUMBER - Start reading from the position denoted by a specific sequence number, provided in the value StartingSequenceNumber .
            AFTER_SEQUENCE_NUMBER - Start reading right after the position denoted by a specific sequence number, provided in the value StartingSequenceNumber .
            AT_TIMESTAMP - Start reading from the position denoted by a specific timestamp, provided in the value Timestamp .
            TRIM_HORIZON - Start reading at the last untrimmed record in the shard in the system, which is the oldest data record in the shard.
            LATEST - Start reading just after the most recent record in the shard, so that you always read the most recent data in the shard.
            

    :type StartingSequenceNumber: string
    :param StartingSequenceNumber: The sequence number of the data record in the shard from which to start reading. Used with shard iterator type AT_SEQUENCE_NUMBER and AFTER_SEQUENCE_NUMBER.

    :type Timestamp: datetime
    :param Timestamp: The timestamp of the data record from which to start reading. Used with shard iterator type AT_TIMESTAMP. A timestamp is the Unix epoch date with precision in milliseconds. For example, 2016-04-04T19:58:46.480-00:00 or 1459799926.480 . If a record with this exact timestamp does not exist, the iterator returned is for the next (later) record. If the timestamp is older than the current trim horizon, the iterator returned is for the oldest untrimmed data record (TRIM_HORIZON).

    :rtype: dict
    :return: {
        'ShardIterator': 'string'
    }
    
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def increase_stream_retention_period(StreamName=None, RetentionPeriodHours=None):
    """
    Increases the Amazon Kinesis stream's retention period, which is the length of time data records are accessible after they are added to the stream. The maximum value of a stream's retention period is 168 hours (7 days).
    Upon choosing a longer stream retention period, this operation will increase the time period records are accessible that have not yet expired. However, it will not make previous data that has expired (older than the stream's previous retention period) accessible after the operation has been called. For example, if a stream's retention period is set to 24 hours and is increased to 168 hours, any data that is older than 24 hours will remain inaccessible to consumer applications.
    
    
    :example: response = client.increase_stream_retention_period(
        StreamName='string',
        RetentionPeriodHours=123
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]
            The name of the stream to modify.
            

    :type RetentionPeriodHours: integer
    :param RetentionPeriodHours: [REQUIRED]
            The new retention period of the stream, in hours. Must be more than the current retention period.
            

    """
    pass

def list_streams(Limit=None, ExclusiveStartStreamName=None):
    """
    Lists your Amazon Kinesis streams.
    The number of streams may be too large to return from a single call to ListStreams . You can limit the number of returned streams using the Limit parameter. If you do not specify a value for the Limit parameter, Amazon Kinesis uses the default limit, which is currently 10.
    You can detect if there are more streams available to list by using the HasMoreStreams flag from the returned output. If there are more streams available, you can request more streams by using the name of the last stream returned by the ListStreams request in the ExclusiveStartStreamName parameter in a subsequent request to ListStreams . The group of stream names returned by the subsequent request is then added to the list. You can continue this process until all the stream names have been collected in the list.
    
    
    :example: response = client.list_streams(
        Limit=123,
        ExclusiveStartStreamName='string'
    )
    
    
    :type Limit: integer
    :param Limit: The maximum number of streams to list.

    :type ExclusiveStartStreamName: string
    :param ExclusiveStartStreamName: The name of the stream to start the list with.

    :rtype: dict
    :return: {
        'StreamNames': [
            'string',
        ],
        'HasMoreStreams': True|False
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tags_for_stream(StreamName=None, ExclusiveStartTagKey=None, Limit=None):
    """
    Lists the tags for the specified Amazon Kinesis stream.
    
    
    :example: response = client.list_tags_for_stream(
        StreamName='string',
        ExclusiveStartTagKey='string',
        Limit=123
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]
            The name of the stream.
            

    :type ExclusiveStartTagKey: string
    :param ExclusiveStartTagKey: The key to use as the starting point for the list of tags. If this parameter is set, ListTagsForStream gets all tags that occur after ExclusiveStartTagKey .

    :type Limit: integer
    :param Limit: The number of tags to return. If this number is less than the total number of tags associated with the stream, HasMoreTags is set to true . To list additional tags, set ExclusiveStartTagKey to the last key in the response.

    :rtype: dict
    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'HasMoreTags': True|False
    }
    
    
    """
    pass

def merge_shards(StreamName=None, ShardToMerge=None, AdjacentShardToMerge=None):
    """
    Merges two adjacent shards in an Amazon Kinesis stream and combines them into a single shard to reduce the stream's capacity to ingest and transport data. Two shards are considered adjacent if the union of the hash key ranges for the two shards form a contiguous set with no gaps. For example, if you have two shards, one with a hash key range of 276...381 and the other with a hash key range of 382...454, then you could merge these two shards into a single shard that would have a hash key range of 276...454. After the merge, the single child shard receives data for all hash key values covered by the two parent shards.
    MergeShards is called when there is a need to reduce the overall capacity of a stream because of excess capacity that is not being used. You must specify the shard to be merged and the adjacent shard for a stream. For more information about merging shards, see Merge Two Shards in the Amazon Kinesis Streams Developer Guide .
    If the stream is in the ACTIVE state, you can call MergeShards . If a stream is in the CREATING , UPDATING , or DELETING state, MergeShards returns a ResourceInUseException . If the specified stream does not exist, MergeShards returns a ResourceNotFoundException .
    You can use  DescribeStream to check the state of the stream, which is returned in StreamStatus .
    MergeShards is an asynchronous operation. Upon receiving a MergeShards request, Amazon Kinesis immediately returns a response and sets the StreamStatus to UPDATING . After the operation is completed, Amazon Kinesis sets the StreamStatus to ACTIVE . Read and write operations continue to work while the stream is in the UPDATING state.
    You use  DescribeStream to determine the shard IDs that are specified in the MergeShards request.
    If you try to operate on too many streams in parallel using  CreateStream ,  DeleteStream , MergeShards or  SplitShard , you will receive a LimitExceededException .
    MergeShards has limit of 5 transactions per second per account.
    
    
    :example: response = client.merge_shards(
        StreamName='string',
        ShardToMerge='string',
        AdjacentShardToMerge='string'
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]
            The name of the stream for the merge.
            

    :type ShardToMerge: string
    :param ShardToMerge: [REQUIRED]
            The shard ID of the shard to combine with the adjacent shard for the merge.
            

    :type AdjacentShardToMerge: string
    :param AdjacentShardToMerge: [REQUIRED]
            The shard ID of the adjacent shard for the merge.
            

    """
    pass

def put_record(StreamName=None, Data=None, PartitionKey=None, ExplicitHashKey=None, SequenceNumberForOrdering=None):
    """
    Writes a single data record into an Amazon Kinesis stream. Call PutRecord to send data into the stream for real-time ingestion and subsequent processing, one record at a time. Each shard can support writes up to 1,000 records per second, up to a maximum data write total of 1 MB per second.
    You must specify the name of the stream that captures, stores, and transports the data; a partition key; and the data blob itself.
    The data blob can be any type of data; for example, a segment from a log file, geographic/location data, website clickstream data, and so on.
    The partition key is used by Amazon Kinesis to distribute data across shards. Amazon Kinesis segregates the data records that belong to a stream into multiple shards, using the partition key associated with each data record to determine which shard a given data record belongs to.
    Partition keys are Unicode strings, with a maximum length limit of 256 characters for each key. An MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards using the hash key ranges of the shards. You can override hashing the partition key to determine the shard by explicitly specifying a hash value using the ExplicitHashKey parameter. For more information, see Adding Data to a Stream in the Amazon Kinesis Streams Developer Guide .
    PutRecord returns the shard ID of where the data record was placed and the sequence number that was assigned to the data record.
    Sequence numbers increase over time and are specific to a shard within a stream, not across all shards within a stream. To guarantee strictly increasing ordering, write serially to a shard and use the SequenceNumberForOrdering parameter. For more information, see Adding Data to a Stream in the Amazon Kinesis Streams Developer Guide .
    If a PutRecord request cannot be processed because of insufficient provisioned throughput on the shard involved in the request, PutRecord throws ProvisionedThroughputExceededException .
    Data records are accessible for only 24 hours from the time that they are added to a stream.
    
    
    :example: response = client.put_record(
        StreamName='string',
        Data=b'bytes',
        PartitionKey='string',
        ExplicitHashKey='string',
        SequenceNumberForOrdering='string'
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]
            The name of the stream to put the data record into.
            

    :type Data: bytes
    :param Data: [REQUIRED]
            The data blob to put into the record, which is base64-encoded when the blob is serialized. When the data blob (the payload before base64-encoding) is added to the partition key size, the total size must not exceed the maximum record size (1 MB).
            

    :type PartitionKey: string
    :param PartitionKey: [REQUIRED]
            Determines which shard in the stream the data record is assigned to. Partition keys are Unicode strings with a maximum length limit of 256 characters for each key. Amazon Kinesis uses the partition key as input to a hash function that maps the partition key and associated data to a specific shard. Specifically, an MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream.
            

    :type ExplicitHashKey: string
    :param ExplicitHashKey: The hash value used to explicitly determine the shard the data record is assigned to by overriding the partition key hash.

    :type SequenceNumberForOrdering: string
    :param SequenceNumberForOrdering: Guarantees strictly increasing sequence numbers, for puts from the same client and to the same partition key. Usage: set the SequenceNumberForOrdering of record n to the sequence number of record n-1 (as returned in the result when putting record n-1 ). If this parameter is not set, records will be coarsely ordered based on arrival time.

    :rtype: dict
    :return: {
        'ShardId': 'string',
        'SequenceNumber': 'string'
    }
    
    
    """
    pass

def put_records(Records=None, StreamName=None):
    """
    Writes multiple data records into an Amazon Kinesis stream in a single call (also referred to as a PutRecords request). Use this operation to send data into the stream for data ingestion and processing.
    Each PutRecords request can support up to 500 records. Each record in the request can be as large as 1 MB, up to a limit of 5 MB for the entire request, including partition keys. Each shard can support writes up to 1,000 records per second, up to a maximum data write total of 1 MB per second.
    You must specify the name of the stream that captures, stores, and transports the data; and an array of request Records , with each record in the array requiring a partition key and data blob. The record size limit applies to the total size of the partition key and data blob.
    The data blob can be any type of data; for example, a segment from a log file, geographic/location data, website clickstream data, and so on.
    The partition key is used by Amazon Kinesis as input to a hash function that maps the partition key and associated data to a specific shard. An MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream. For more information, see Adding Data to a Stream in the Amazon Kinesis Streams Developer Guide .
    Each record in the Records array may include an optional parameter, ExplicitHashKey , which overrides the partition key to shard mapping. This parameter allows a data producer to determine explicitly the shard where the record is stored. For more information, see Adding Multiple Records with PutRecords in the Amazon Kinesis Streams Developer Guide .
    The PutRecords response includes an array of response Records . Each record in the response array directly correlates with a record in the request array using natural ordering, from the top to the bottom of the request and response. The response Records array always includes the same number of records as the request array.
    The response Records array includes both successfully and unsuccessfully processed records. Amazon Kinesis attempts to process all records in each PutRecords request. A single record failure does not stop the processing of subsequent records.
    A successfully-processed record includes ShardId and SequenceNumber values. The ShardId parameter identifies the shard in the stream where the record is stored. The SequenceNumber parameter is an identifier assigned to the put record, unique to all records in the stream.
    An unsuccessfully-processed record includes ErrorCode and ErrorMessage values. ErrorCode reflects the type of error and can be one of the following values: ProvisionedThroughputExceededException or InternalFailure . ErrorMessage provides more detailed information about the ProvisionedThroughputExceededException exception including the account ID, stream name, and shard ID of the record that was throttled. For more information about partially successful responses, see Adding Multiple Records with PutRecords in the Amazon Kinesis Streams Developer Guide .
    By default, data records are accessible for only 24 hours from the time that they are added to an Amazon Kinesis stream. This retention period can be modified using the  DecreaseStreamRetentionPeriod and  IncreaseStreamRetentionPeriod operations.
    
    
    :example: response = client.put_records(
        Records=[
            {
                'Data': b'bytes',
                'ExplicitHashKey': 'string',
                'PartitionKey': 'string'
            },
        ],
        StreamName='string'
    )
    
    
    :type Records: list
    :param Records: [REQUIRED]
            The records associated with the request.
            (dict) --Represents the output for PutRecords .
            Data (bytes) -- [REQUIRED]The data blob to put into the record, which is base64-encoded when the blob is serialized. When the data blob (the payload before base64-encoding) is added to the partition key size, the total size must not exceed the maximum record size (1 MB).
            ExplicitHashKey (string) --The hash value used to determine explicitly the shard that the data record is assigned to by overriding the partition key hash.
            PartitionKey (string) -- [REQUIRED]Determines which shard in the stream the data record is assigned to. Partition keys are Unicode strings with a maximum length limit of 256 characters for each key. Amazon Kinesis uses the partition key as input to a hash function that maps the partition key and associated data to a specific shard. Specifically, an MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream.
            
            

    :type StreamName: string
    :param StreamName: [REQUIRED]
            The stream name associated with the request.
            

    :rtype: dict
    :return: {
        'FailedRecordCount': 123,
        'Records': [
            {
                'SequenceNumber': 'string',
                'ShardId': 'string',
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def remove_tags_from_stream(StreamName=None, TagKeys=None):
    """
    Removes tags from the specified Amazon Kinesis stream. Removed tags are deleted and cannot be recovered after this operation successfully completes.
    If you specify a tag that does not exist, it is ignored.
    
    
    :example: response = client.remove_tags_from_stream(
        StreamName='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]
            The name of the stream.
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            A list of tag keys. Each corresponding tag is removed from the stream.
            (string) --
            

    """
    pass

def split_shard(StreamName=None, ShardToSplit=None, NewStartingHashKey=None):
    """
    Splits a shard into two new shards in the Amazon Kinesis stream to increase the stream's capacity to ingest and transport data. SplitShard is called when there is a need to increase the overall capacity of a stream because of an expected increase in the volume of data records being ingested.
    You can also use SplitShard when a shard appears to be approaching its maximum utilization; for example, the producers sending data into the specific shard are suddenly sending more than previously anticipated. You can also call SplitShard to increase stream capacity, so that more Amazon Kinesis applications can simultaneously read data from the stream for real-time processing.
    You must specify the shard to be split and the new hash key, which is the position in the shard where the shard gets split in two. In many cases, the new hash key might simply be the average of the beginning and ending hash key, but it can be any hash key value in the range being mapped into the shard. For more information about splitting shards, see Split a Shard in the Amazon Kinesis Streams Developer Guide .
    You can use  DescribeStream to determine the shard ID and hash key values for the ShardToSplit and NewStartingHashKey parameters that are specified in the SplitShard request.
    SplitShard is an asynchronous operation. Upon receiving a SplitShard request, Amazon Kinesis immediately returns a response and sets the stream status to UPDATING . After the operation is completed, Amazon Kinesis sets the stream status to ACTIVE . Read and write operations continue to work while the stream is in the UPDATING state.
    You can use DescribeStream to check the status of the stream, which is returned in StreamStatus . If the stream is in the ACTIVE state, you can call SplitShard . If a stream is in CREATING or UPDATING or DELETING states, DescribeStream returns a ResourceInUseException .
    If the specified stream does not exist, DescribeStream returns a ResourceNotFoundException . If you try to create more shards than are authorized for your account, you receive a LimitExceededException .
    For the default shard limit for an AWS account, see Streams Limits in the Amazon Kinesis Streams Developer Guide . If you need to increase this limit, contact AWS Support .
    If you try to operate on too many streams simultaneously using  CreateStream ,  DeleteStream ,  MergeShards , and/or  SplitShard , you receive a LimitExceededException .
    SplitShard has limit of 5 transactions per second per account.
    
    
    :example: response = client.split_shard(
        StreamName='string',
        ShardToSplit='string',
        NewStartingHashKey='string'
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]
            The name of the stream for the shard split.
            

    :type ShardToSplit: string
    :param ShardToSplit: [REQUIRED]
            The shard ID of the shard to split.
            

    :type NewStartingHashKey: string
    :param NewStartingHashKey: [REQUIRED]
            A hash key value for the starting hash key of one of the child shards created by the split. The hash key range for a given shard constitutes a set of ordered contiguous positive integers. The value for NewStartingHashKey must be in the range of hash keys being mapped into the shard. The NewStartingHashKey hash key value and all higher hash key values in hash key range are distributed to one of the child shards. All the lower hash key values in the range are distributed to the other child shard.
            

    """
    pass

