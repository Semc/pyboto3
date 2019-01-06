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

def batch_put_message(channelName=None, messages=None):
    """
    Sends messages to a channel.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_put_message(
        channelName='string',
        messages=[
            {
                'messageId': 'string',
                'payload': b'bytes'
            },
        ]
    )
    
    
    :type channelName: string
    :param channelName: [REQUIRED]
            The name of the channel where the messages are sent.
            

    :type messages: list
    :param messages: [REQUIRED]
            The list of messages to be sent. Each message has format: '{ 'messageId': 'string', 'payload': 'string'}'.
            Note that the field names of message payloads (data) that you send to AWS IoT Analytics:
            Must contain only alphanumeric characters and undescores (_); no other special characters are allowed.
            Must begin with an alphabetic character or single underscore (_).
            Cannot contain hyphens (-).
            In regular expression terms: '^[A-Za-z_]([A-Za-z0-9]*|[A-Za-z0-9][A-Za-z0-9_]*)$'.
            Cannot be greater than 255 characters.
            Are case-insensitive. (Fields named 'foo' and 'FOO' in the same payload are considered duplicates.)
            For example, {'temp_01': 29} or {'_temp_01': 29} are valid, but {'temp-01': 29}, {'01_temp': 29} or {'__temp_01': 29} are invalid in message payloads.
            (dict) --Information about a message.
            messageId (string) -- [REQUIRED]The ID you wish to assign to the message. Each 'messageId' must be unique within each batch sent.
            payload (bytes) -- [REQUIRED]The payload of the message. This may be a JSON string or a Base64-encoded string representing binary data (in which case you must decode it by means of a pipeline activity).
            
            

    :rtype: dict
    :return: {
        'batchPutMessageErrorEntries': [
            {
                'messageId': 'string',
                'errorCode': 'string',
                'errorMessage': 'string'
            },
        ]
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

def cancel_pipeline_reprocessing(pipelineName=None, reprocessingId=None):
    """
    Cancels the reprocessing of data through the pipeline.
    See also: AWS API Documentation
    
    
    :example: response = client.cancel_pipeline_reprocessing(
        pipelineName='string',
        reprocessingId='string'
    )
    
    
    :type pipelineName: string
    :param pipelineName: [REQUIRED]
            The name of pipeline for which data reprocessing is canceled.
            

    :type reprocessingId: string
    :param reprocessingId: [REQUIRED]
            The ID of the reprocessing task (returned by 'StartPipelineReprocessing').
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_channel(channelName=None, retentionPeriod=None, tags=None):
    """
    Creates a channel. A channel collects data from an MQTT topic and archives the raw, unprocessed messages before publishing the data to a pipeline.
    See also: AWS API Documentation
    
    
    :example: response = client.create_channel(
        channelName='string',
        retentionPeriod={
            'unlimited': True|False,
            'numberOfDays': 123
        },
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type channelName: string
    :param channelName: [REQUIRED]
            The name of the channel.
            

    :type retentionPeriod: dict
    :param retentionPeriod: How long, in days, message data is kept for the channel.
            unlimited (boolean) --If true, message data is kept indefinitely.
            numberOfDays (integer) --The number of days that message data is kept. The 'unlimited' parameter must be false.
            

    :type tags: list
    :param tags: Metadata which can be used to manage the channel.
            (dict) --A set of key/value pairs which are used to manage the resource.
            key (string) -- [REQUIRED]The tag's key.
            value (string) -- [REQUIRED]The tag's value.
            
            

    :rtype: dict
    :return: {
        'channelName': 'string',
        'channelArn': 'string',
        'retentionPeriod': {
            'unlimited': True|False,
            'numberOfDays': 123
        }
    }
    
    
    """
    pass

def create_dataset(datasetName=None, actions=None, triggers=None, contentDeliveryRules=None, retentionPeriod=None, tags=None):
    """
    Creates a data set. A data set stores data retrieved from a data store by applying a "queryAction" (a SQL query) or a "containerAction" (executing a containerized application). This operation creates the skeleton of a data set. The data set can be populated manually by calling "CreateDatasetContent" or automatically according to a "trigger" you specify.
    See also: AWS API Documentation
    
    
    :example: response = client.create_dataset(
        datasetName='string',
        actions=[
            {
                'actionName': 'string',
                'queryAction': {
                    'sqlQuery': 'string',
                    'filters': [
                        {
                            'deltaTime': {
                                'offsetSeconds': 123,
                                'timeExpression': 'string'
                            }
                        },
                    ]
                },
                'containerAction': {
                    'image': 'string',
                    'executionRoleArn': 'string',
                    'resourceConfiguration': {
                        'computeType': 'ACU_1'|'ACU_2',
                        'volumeSizeInGB': 123
                    },
                    'variables': [
                        {
                            'name': 'string',
                            'stringValue': 'string',
                            'doubleValue': 123.0,
                            'datasetContentVersionValue': {
                                'datasetName': 'string'
                            },
                            'outputFileUriValue': {
                                'fileName': 'string'
                            }
                        },
                    ]
                }
            },
        ],
        triggers=[
            {
                'schedule': {
                    'expression': 'string'
                },
                'dataset': {
                    'name': 'string'
                }
            },
        ],
        contentDeliveryRules=[
            {
                'entryName': 'string',
                'destination': {
                    'iotEventsDestinationConfiguration': {
                        'inputName': 'string',
                        'roleArn': 'string'
                    }
                }
            },
        ],
        retentionPeriod={
            'unlimited': True|False,
            'numberOfDays': 123
        },
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type datasetName: string
    :param datasetName: [REQUIRED]
            The name of the data set.
            

    :type actions: list
    :param actions: [REQUIRED]
            A list of actions that create the data set contents.
            (dict) --A 'DatasetAction' object that specifies how data set contents are automatically created.
            actionName (string) --The name of the data set action by which data set contents are automatically created.
            queryAction (dict) --An 'SqlQueryDatasetAction' object that uses an SQL query to automatically create data set contents.
            sqlQuery (string) -- [REQUIRED]A SQL query string.
            filters (list) --Pre-filters applied to message data.
            (dict) --Information which is used to filter message data, to segregate it according to the time frame in which it arrives.
            deltaTime (dict) --Used to limit data to that which has arrived since the last execution of the action.
            offsetSeconds (integer) -- [REQUIRED]The number of seconds of estimated 'in flight' lag time of message data. When you create data set contents using message data from a specified time frame, some message data may still be 'in flight' when processing begins, and so will not arrive in time to be processed. Use this field to make allowances for the 'in flight' time of your message data, so that data not processed from a previous time frame will be included with the next time frame. Without this, missed message data would be excluded from processing during the next time frame as well, because its timestamp places it within the previous time frame.
            timeExpression (string) -- [REQUIRED]An expression by which the time of the message data may be determined. This may be the name of a timestamp field, or a SQL expression which is used to derive the time the message data was generated.
            
            
            containerAction (dict) --Information which allows the system to run a containerized application in order to create the data set contents. The application must be in a Docker container along with any needed support libraries.
            image (string) -- [REQUIRED]The ARN of the Docker container stored in your account. The Docker container contains an application and needed support libraries and is used to generate data set contents.
            executionRoleArn (string) -- [REQUIRED]The ARN of the role which gives permission to the system to access needed resources in order to run the 'containerAction'. This includes, at minimum, permission to retrieve the data set contents which are the input to the containerized application.
            resourceConfiguration (dict) -- [REQUIRED]Configuration of the resource which executes the 'containerAction'.
            computeType (string) -- [REQUIRED]The type of the compute resource used to execute the 'containerAction'. Possible values are: ACU_1 (vCPU=4, memory=16GiB) or ACU_2 (vCPU=8, memory=32GiB).
            volumeSizeInGB (integer) -- [REQUIRED]The size (in GB) of the persistent storage available to the resource instance used to execute the 'containerAction' (min: 1, max: 50).
            variables (list) --The values of variables used within the context of the execution of the containerized application (basically, parameters passed to the application). Each variable must have a name and a value given by one of 'stringValue', 'datasetContentVersionValue', or 'outputFileUriValue'.
            (dict) --An instance of a variable to be passed to the 'containerAction' execution. Each variable must have a name and a value given by one of 'stringValue', 'datasetContentVersionValue', or 'outputFileUriValue'.
            name (string) -- [REQUIRED]The name of the variable.
            stringValue (string) --The value of the variable as a string.
            doubleValue (float) --The value of the variable as a double (numeric).
            datasetContentVersionValue (dict) --The value of the variable as a structure that specifies a data set content version.
            datasetName (string) -- [REQUIRED]The name of the data set whose latest contents are used as input to the notebook or application.
            outputFileUriValue (dict) --The value of the variable as a structure that specifies an output file URI.
            fileName (string) -- [REQUIRED]The URI of the location where data set contents are stored, usually the URI of a file in an S3 bucket.
            
            
            
            

    :type triggers: list
    :param triggers: A list of triggers. A trigger causes data set contents to be populated at a specified time interval or when another data set's contents are created. The list of triggers can be empty or contain up to five DataSetTrigger objects.
            (dict) --The 'DatasetTrigger' that specifies when the data set is automatically updated.
            schedule (dict) --The 'Schedule' when the trigger is initiated.
            expression (string) --The expression that defines when to trigger an update. For more information, see Schedule Expressions for Rules in the Amazon CloudWatch documentation.
            dataset (dict) --The data set whose content creation triggers the creation of this data set's contents.
            name (string) -- [REQUIRED]The name of the data set whose content generation triggers the new data set content generation.
            
            

    :type contentDeliveryRules: list
    :param contentDeliveryRules: When data set contents are created they are delivered to destinations specified here.
            (dict) --When data set contents are created they are delivered to destination specified here.
            entryName (string) --The name of the data set content delivery rules entry.
            destination (dict) -- [REQUIRED]The destination to which data set contents are delivered.
            iotEventsDestinationConfiguration (dict) --Configuration information for delivery of data set contents to AWS IoT Events.
            inputName (string) -- [REQUIRED]The name of the AWS IoT Events input to which data set contents are delivered.
            roleArn (string) -- [REQUIRED]The ARN of the role which grants AWS IoT Analytics permission to deliver data set contents to an AWS IoT Events input.
            
            
            

    :type retentionPeriod: dict
    :param retentionPeriod: [Optional] How long, in days, message data is kept for the data set. If not given or set to null, the latest version of the dataset content plus the latest succeeded version (if they are different) are retained for at most 90 days.
            unlimited (boolean) --If true, message data is kept indefinitely.
            numberOfDays (integer) --The number of days that message data is kept. The 'unlimited' parameter must be false.
            

    :type tags: list
    :param tags: Metadata which can be used to manage the data set.
            (dict) --A set of key/value pairs which are used to manage the resource.
            key (string) -- [REQUIRED]The tag's key.
            value (string) -- [REQUIRED]The tag's value.
            
            

    :rtype: dict
    :return: {
        'datasetName': 'string',
        'datasetArn': 'string',
        'retentionPeriod': {
            'unlimited': True|False,
            'numberOfDays': 123
        }
    }
    
    
    """
    pass

def create_dataset_content(datasetName=None):
    """
    Creates the content of a data set by applying a "queryAction" (a SQL query) or a "containerAction" (executing a containerized application).
    See also: AWS API Documentation
    
    
    :example: response = client.create_dataset_content(
        datasetName='string'
    )
    
    
    :type datasetName: string
    :param datasetName: [REQUIRED]
            The name of the data set.
            

    :rtype: dict
    :return: {
        'versionId': 'string'
    }
    
    
    """
    pass

def create_datastore(datastoreName=None, retentionPeriod=None, tags=None):
    """
    Creates a data store, which is a repository for messages.
    See also: AWS API Documentation
    
    
    :example: response = client.create_datastore(
        datastoreName='string',
        retentionPeriod={
            'unlimited': True|False,
            'numberOfDays': 123
        },
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type datastoreName: string
    :param datastoreName: [REQUIRED]
            The name of the data store.
            

    :type retentionPeriod: dict
    :param retentionPeriod: How long, in days, message data is kept for the data store.
            unlimited (boolean) --If true, message data is kept indefinitely.
            numberOfDays (integer) --The number of days that message data is kept. The 'unlimited' parameter must be false.
            

    :type tags: list
    :param tags: Metadata which can be used to manage the data store.
            (dict) --A set of key/value pairs which are used to manage the resource.
            key (string) -- [REQUIRED]The tag's key.
            value (string) -- [REQUIRED]The tag's value.
            
            

    :rtype: dict
    :return: {
        'datastoreName': 'string',
        'datastoreArn': 'string',
        'retentionPeriod': {
            'unlimited': True|False,
            'numberOfDays': 123
        }
    }
    
    
    """
    pass

def create_pipeline(pipelineName=None, pipelineActivities=None, tags=None):
    """
    Creates a pipeline. A pipeline consumes messages from one or more channels and allows you to process the messages before storing them in a data store.
    See also: AWS API Documentation
    
    
    :example: response = client.create_pipeline(
        pipelineName='string',
        pipelineActivities=[
            {
                'channel': {
                    'name': 'string',
                    'channelName': 'string',
                    'next': 'string'
                },
                'lambda': {
                    'name': 'string',
                    'lambdaName': 'string',
                    'batchSize': 123,
                    'next': 'string'
                },
                'datastore': {
                    'name': 'string',
                    'datastoreName': 'string'
                },
                'addAttributes': {
                    'name': 'string',
                    'attributes': {
                        'string': 'string'
                    },
                    'next': 'string'
                },
                'removeAttributes': {
                    'name': 'string',
                    'attributes': [
                        'string',
                    ],
                    'next': 'string'
                },
                'selectAttributes': {
                    'name': 'string',
                    'attributes': [
                        'string',
                    ],
                    'next': 'string'
                },
                'filter': {
                    'name': 'string',
                    'filter': 'string',
                    'next': 'string'
                },
                'math': {
                    'name': 'string',
                    'attribute': 'string',
                    'math': 'string',
                    'next': 'string'
                },
                'deviceRegistryEnrich': {
                    'name': 'string',
                    'attribute': 'string',
                    'thingName': 'string',
                    'roleArn': 'string',
                    'next': 'string'
                },
                'deviceShadowEnrich': {
                    'name': 'string',
                    'attribute': 'string',
                    'thingName': 'string',
                    'roleArn': 'string',
                    'next': 'string'
                }
            },
        ],
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type pipelineName: string
    :param pipelineName: [REQUIRED]
            The name of the pipeline.
            

    :type pipelineActivities: list
    :param pipelineActivities: [REQUIRED]
            A list of pipeline activities.
            The list can be 1-25 PipelineActivity objects. Activities perform transformations on your messages, such as removing, renaming, or adding message attributes; filtering messages based on attribute values; invoking your Lambda functions on messages for advanced processing; or performing mathematical transformations to normalize device data.
            (dict) --An activity that performs a transformation on a message.
            channel (dict) --Determines the source of the messages to be processed.
            name (string) -- [REQUIRED]The name of the 'channel' activity.
            channelName (string) -- [REQUIRED]The name of the channel from which the messages are processed.
            next (string) --The next activity in the pipeline.
            lambda (dict) --Runs a Lambda function to modify the message.
            name (string) -- [REQUIRED]The name of the 'lambda' activity.
            lambdaName (string) -- [REQUIRED]The name of the Lambda function that is run on the message.
            batchSize (integer) -- [REQUIRED]The number of messages passed to the Lambda function for processing.
            The AWS Lambda function must be able to process all of these messages within five minutes, which is the maximum timeout duration for Lambda functions.
            next (string) --The next activity in the pipeline.
            datastore (dict) --Specifies where to store the processed message data.
            name (string) -- [REQUIRED]The name of the 'datastore' activity.
            datastoreName (string) -- [REQUIRED]The name of the data store where processed messages are stored.
            addAttributes (dict) --Adds other attributes based on existing attributes in the message.
            name (string) -- [REQUIRED]The name of the 'addAttributes' activity.
            attributes (dict) -- [REQUIRED]A list of 1-50 'AttributeNameMapping' objects that map an existing attribute to a new attribute.
            Note
            The existing attributes remain in the message, so if you want to remove the originals, use 'RemoveAttributeActivity'.
            (string) --
            (string) --
            
            next (string) --The next activity in the pipeline.
            removeAttributes (dict) --Removes attributes from a message.
            name (string) -- [REQUIRED]The name of the 'removeAttributes' activity.
            attributes (list) -- [REQUIRED]A list of 1-50 attributes to remove from the message.
            (string) --
            next (string) --The next activity in the pipeline.
            selectAttributes (dict) --Creates a new message using only the specified attributes from the original message.
            name (string) -- [REQUIRED]The name of the 'selectAttributes' activity.
            attributes (list) -- [REQUIRED]A list of the attributes to select from the message.
            (string) --
            next (string) --The next activity in the pipeline.
            filter (dict) --Filters a message based on its attributes.
            name (string) -- [REQUIRED]The name of the 'filter' activity.
            filter (string) -- [REQUIRED]An expression that looks like a SQL WHERE clause that must return a Boolean value.
            next (string) --The next activity in the pipeline.
            math (dict) --Computes an arithmetic expression using the message's attributes and adds it to the message.
            name (string) -- [REQUIRED]The name of the 'math' activity.
            attribute (string) -- [REQUIRED]The name of the attribute that contains the result of the math operation.
            math (string) -- [REQUIRED]An expression that uses one or more existing attributes and must return an integer value.
            next (string) --The next activity in the pipeline.
            deviceRegistryEnrich (dict) --Adds data from the AWS IoT device registry to your message.
            name (string) -- [REQUIRED]The name of the 'deviceRegistryEnrich' activity.
            attribute (string) -- [REQUIRED]The name of the attribute that is added to the message.
            thingName (string) -- [REQUIRED]The name of the IoT device whose registry information is added to the message.
            roleArn (string) -- [REQUIRED]The ARN of the role that allows access to the device's registry information.
            next (string) --The next activity in the pipeline.
            deviceShadowEnrich (dict) --Adds information from the AWS IoT Device Shadows service to a message.
            name (string) -- [REQUIRED]The name of the 'deviceShadowEnrich' activity.
            attribute (string) -- [REQUIRED]The name of the attribute that is added to the message.
            thingName (string) -- [REQUIRED]The name of the IoT device whose shadow information is added to the message.
            roleArn (string) -- [REQUIRED]The ARN of the role that allows access to the device's shadow.
            next (string) --The next activity in the pipeline.
            
            

    :type tags: list
    :param tags: Metadata which can be used to manage the pipeline.
            (dict) --A set of key/value pairs which are used to manage the resource.
            key (string) -- [REQUIRED]The tag's key.
            value (string) -- [REQUIRED]The tag's value.
            
            

    :rtype: dict
    :return: {
        'pipelineName': 'string',
        'pipelineArn': 'string'
    }
    
    
    """
    pass

def delete_channel(channelName=None):
    """
    Deletes the specified channel.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_channel(
        channelName='string'
    )
    
    
    :type channelName: string
    :param channelName: [REQUIRED]
            The name of the channel to delete.
            

    """
    pass

def delete_dataset(datasetName=None):
    """
    Deletes the specified data set.
    You do not have to delete the content of the data set before you perform this operation.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_dataset(
        datasetName='string'
    )
    
    
    :type datasetName: string
    :param datasetName: [REQUIRED]
            The name of the data set to delete.
            

    """
    pass

def delete_dataset_content(datasetName=None, versionId=None):
    """
    Deletes the content of the specified data set.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_dataset_content(
        datasetName='string',
        versionId='string'
    )
    
    
    :type datasetName: string
    :param datasetName: [REQUIRED]
            The name of the data set whose content is deleted.
            

    :type versionId: string
    :param versionId: The version of the data set whose content is deleted. You can also use the strings '$LATEST' or '$LATEST_SUCCEEDED' to delete the latest or latest successfully completed data set. If not specified, '$LATEST_SUCCEEDED' is the default.

    """
    pass

def delete_datastore(datastoreName=None):
    """
    Deletes the specified data store.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_datastore(
        datastoreName='string'
    )
    
    
    :type datastoreName: string
    :param datastoreName: [REQUIRED]
            The name of the data store to delete.
            

    """
    pass

def delete_pipeline(pipelineName=None):
    """
    Deletes the specified pipeline.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_pipeline(
        pipelineName='string'
    )
    
    
    :type pipelineName: string
    :param pipelineName: [REQUIRED]
            The name of the pipeline to delete.
            

    """
    pass

def describe_channel(channelName=None, includeStatistics=None):
    """
    Retrieves information about a channel.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_channel(
        channelName='string',
        includeStatistics=True|False
    )
    
    
    :type channelName: string
    :param channelName: [REQUIRED]
            The name of the channel whose information is retrieved.
            

    :type includeStatistics: boolean
    :param includeStatistics: If true, additional statistical information about the channel is included in the response.

    :rtype: dict
    :return: {
        'channel': {
            'name': 'string',
            'arn': 'string',
            'status': 'CREATING'|'ACTIVE'|'DELETING',
            'retentionPeriod': {
                'unlimited': True|False,
                'numberOfDays': 123
            },
            'creationTime': datetime(2015, 1, 1),
            'lastUpdateTime': datetime(2015, 1, 1)
        },
        'statistics': {
            'size': {
                'estimatedSizeInBytes': 123.0,
                'estimatedOn': datetime(2015, 1, 1)
            }
        }
    }
    
    
    """
    pass

def describe_dataset(datasetName=None):
    """
    Retrieves information about a data set.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_dataset(
        datasetName='string'
    )
    
    
    :type datasetName: string
    :param datasetName: [REQUIRED]
            The name of the data set whose information is retrieved.
            

    :rtype: dict
    :return: {
        'dataset': {
            'name': 'string',
            'arn': 'string',
            'actions': [
                {
                    'actionName': 'string',
                    'queryAction': {
                        'sqlQuery': 'string',
                        'filters': [
                            {
                                'deltaTime': {
                                    'offsetSeconds': 123,
                                    'timeExpression': 'string'
                                }
                            },
                        ]
                    },
                    'containerAction': {
                        'image': 'string',
                        'executionRoleArn': 'string',
                        'resourceConfiguration': {
                            'computeType': 'ACU_1'|'ACU_2',
                            'volumeSizeInGB': 123
                        },
                        'variables': [
                            {
                                'name': 'string',
                                'stringValue': 'string',
                                'doubleValue': 123.0,
                                'datasetContentVersionValue': {
                                    'datasetName': 'string'
                                },
                                'outputFileUriValue': {
                                    'fileName': 'string'
                                }
                            },
                        ]
                    }
                },
            ],
            'triggers': [
                {
                    'schedule': {
                        'expression': 'string'
                    },
                    'dataset': {
                        'name': 'string'
                    }
                },
            ],
            'contentDeliveryRules': [
                {
                    'entryName': 'string',
                    'destination': {
                        'iotEventsDestinationConfiguration': {
                            'inputName': 'string',
                            'roleArn': 'string'
                        }
                    }
                },
            ],
            'status': 'CREATING'|'ACTIVE'|'DELETING',
            'creationTime': datetime(2015, 1, 1),
            'lastUpdateTime': datetime(2015, 1, 1),
            'retentionPeriod': {
                'unlimited': True|False,
                'numberOfDays': 123
            }
        }
    }
    
    
    """
    pass

def describe_datastore(datastoreName=None, includeStatistics=None):
    """
    Retrieves information about a data store.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_datastore(
        datastoreName='string',
        includeStatistics=True|False
    )
    
    
    :type datastoreName: string
    :param datastoreName: [REQUIRED]
            The name of the data store
            

    :type includeStatistics: boolean
    :param includeStatistics: If true, additional statistical information about the datastore is included in the response.

    :rtype: dict
    :return: {
        'datastore': {
            'name': 'string',
            'arn': 'string',
            'status': 'CREATING'|'ACTIVE'|'DELETING',
            'retentionPeriod': {
                'unlimited': True|False,
                'numberOfDays': 123
            },
            'creationTime': datetime(2015, 1, 1),
            'lastUpdateTime': datetime(2015, 1, 1)
        },
        'statistics': {
            'size': {
                'estimatedSizeInBytes': 123.0,
                'estimatedOn': datetime(2015, 1, 1)
            }
        }
    }
    
    
    """
    pass

def describe_logging_options():
    """
    Retrieves the current settings of the AWS IoT Analytics logging options.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_logging_options()
    
    
    :rtype: dict
    :return: {
        'loggingOptions': {
            'roleArn': 'string',
            'level': 'ERROR',
            'enabled': True|False
        }
    }
    
    
    """
    pass

def describe_pipeline(pipelineName=None):
    """
    Retrieves information about a pipeline.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_pipeline(
        pipelineName='string'
    )
    
    
    :type pipelineName: string
    :param pipelineName: [REQUIRED]
            The name of the pipeline whose information is retrieved.
            

    :rtype: dict
    :return: {
        'pipeline': {
            'name': 'string',
            'arn': 'string',
            'activities': [
                {
                    'channel': {
                        'name': 'string',
                        'channelName': 'string',
                        'next': 'string'
                    },
                    'lambda': {
                        'name': 'string',
                        'lambdaName': 'string',
                        'batchSize': 123,
                        'next': 'string'
                    },
                    'datastore': {
                        'name': 'string',
                        'datastoreName': 'string'
                    },
                    'addAttributes': {
                        'name': 'string',
                        'attributes': {
                            'string': 'string'
                        },
                        'next': 'string'
                    },
                    'removeAttributes': {
                        'name': 'string',
                        'attributes': [
                            'string',
                        ],
                        'next': 'string'
                    },
                    'selectAttributes': {
                        'name': 'string',
                        'attributes': [
                            'string',
                        ],
                        'next': 'string'
                    },
                    'filter': {
                        'name': 'string',
                        'filter': 'string',
                        'next': 'string'
                    },
                    'math': {
                        'name': 'string',
                        'attribute': 'string',
                        'math': 'string',
                        'next': 'string'
                    },
                    'deviceRegistryEnrich': {
                        'name': 'string',
                        'attribute': 'string',
                        'thingName': 'string',
                        'roleArn': 'string',
                        'next': 'string'
                    },
                    'deviceShadowEnrich': {
                        'name': 'string',
                        'attribute': 'string',
                        'thingName': 'string',
                        'roleArn': 'string',
                        'next': 'string'
                    }
                },
            ],
            'reprocessingSummaries': [
                {
                    'id': 'string',
                    'status': 'RUNNING'|'SUCCEEDED'|'CANCELLED'|'FAILED',
                    'creationTime': datetime(2015, 1, 1)
                },
            ],
            'creationTime': datetime(2015, 1, 1),
            'lastUpdateTime': datetime(2015, 1, 1)
        }
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

def get_dataset_content(datasetName=None, versionId=None):
    """
    Retrieves the contents of a data set as pre-signed URIs.
    See also: AWS API Documentation
    
    
    :example: response = client.get_dataset_content(
        datasetName='string',
        versionId='string'
    )
    
    
    :type datasetName: string
    :param datasetName: [REQUIRED]
            The name of the data set whose contents are retrieved.
            

    :type versionId: string
    :param versionId: The version of the data set whose contents are retrieved. You can also use the strings '$LATEST' or '$LATEST_SUCCEEDED' to retrieve the contents of the latest or latest successfully completed data set. If not specified, '$LATEST_SUCCEEDED' is the default.

    :rtype: dict
    :return: {
        'entries': [
            {
                'entryName': 'string',
                'dataURI': 'string'
            },
        ],
        'timestamp': datetime(2015, 1, 1),
        'status': {
            'state': 'CREATING'|'SUCCEEDED'|'FAILED',
            'reason': 'string'
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

def list_channels(nextToken=None, maxResults=None):
    """
    Retrieves a list of channels.
    See also: AWS API Documentation
    
    
    :example: response = client.list_channels(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in this request.
            The default value is 100.
            

    :rtype: dict
    :return: {
        'channelSummaries': [
            {
                'channelName': 'string',
                'status': 'CREATING'|'ACTIVE'|'DELETING',
                'creationTime': datetime(2015, 1, 1),
                'lastUpdateTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_dataset_contents(datasetName=None, nextToken=None, maxResults=None, scheduledOnOrAfter=None, scheduledBefore=None):
    """
    Lists information about data set contents that have been created.
    See also: AWS API Documentation
    
    
    :example: response = client.list_dataset_contents(
        datasetName='string',
        nextToken='string',
        maxResults=123,
        scheduledOnOrAfter=datetime(2015, 1, 1),
        scheduledBefore=datetime(2015, 1, 1)
    )
    
    
    :type datasetName: string
    :param datasetName: [REQUIRED]
            The name of the data set whose contents information you want to list.
            

    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in this request.

    :type scheduledOnOrAfter: datetime
    :param scheduledOnOrAfter: A filter to limit results to those data set contents whose creation is scheduled on or after the given time. See the field triggers.schedule in the CreateDataset request. (timestamp)

    :type scheduledBefore: datetime
    :param scheduledBefore: A filter to limit results to those data set contents whose creation is scheduled before the given time. See the field triggers.schedule in the CreateDataset request. (timestamp)

    :rtype: dict
    :return: {
        'datasetContentSummaries': [
            {
                'version': 'string',
                'status': {
                    'state': 'CREATING'|'SUCCEEDED'|'FAILED',
                    'reason': 'string'
                },
                'creationTime': datetime(2015, 1, 1),
                'scheduleTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_datasets(nextToken=None, maxResults=None):
    """
    Retrieves information about data sets.
    See also: AWS API Documentation
    
    
    :example: response = client.list_datasets(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in this request.
            The default value is 100.
            

    :rtype: dict
    :return: {
        'datasetSummaries': [
            {
                'datasetName': 'string',
                'status': 'CREATING'|'ACTIVE'|'DELETING',
                'creationTime': datetime(2015, 1, 1),
                'lastUpdateTime': datetime(2015, 1, 1),
                'triggers': [
                    {
                        'schedule': {
                            'expression': 'string'
                        },
                        'dataset': {
                            'name': 'string'
                        }
                    },
                ],
                'actions': [
                    {
                        'actionName': 'string',
                        'actionType': 'QUERY'|'CONTAINER'
                    },
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_datastores(nextToken=None, maxResults=None):
    """
    Retrieves a list of data stores.
    See also: AWS API Documentation
    
    
    :example: response = client.list_datastores(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in this request.
            The default value is 100.
            

    :rtype: dict
    :return: {
        'datastoreSummaries': [
            {
                'datastoreName': 'string',
                'status': 'CREATING'|'ACTIVE'|'DELETING',
                'creationTime': datetime(2015, 1, 1),
                'lastUpdateTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_pipelines(nextToken=None, maxResults=None):
    """
    Retrieves a list of pipelines.
    See also: AWS API Documentation
    
    
    :example: response = client.list_pipelines(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in this request.
            The default value is 100.
            

    :rtype: dict
    :return: {
        'pipelineSummaries': [
            {
                'pipelineName': 'string',
                'reprocessingSummaries': [
                    {
                        'id': 'string',
                        'status': 'RUNNING'|'SUCCEEDED'|'CANCELLED'|'FAILED',
                        'creationTime': datetime(2015, 1, 1)
                    },
                ],
                'creationTime': datetime(2015, 1, 1),
                'lastUpdateTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_tags_for_resource(resourceArn=None):
    """
    Lists the tags (metadata) which you have assigned to the resource.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]
            The ARN of the resource whose tags you want to list.
            

    :rtype: dict
    :return: {
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    }
    
    
    """
    pass

def put_logging_options(loggingOptions=None):
    """
    Sets or updates the AWS IoT Analytics logging options.
    Note that if you update the value of any loggingOptions field, it takes up to one minute for the change to take effect. Also, if you change the policy attached to the role you specified in the roleArn field (for example, to correct an invalid policy) it takes up to 5 minutes for that change to take effect.
    See also: AWS API Documentation
    
    
    :example: response = client.put_logging_options(
        loggingOptions={
            'roleArn': 'string',
            'level': 'ERROR',
            'enabled': True|False
        }
    )
    
    
    :type loggingOptions: dict
    :param loggingOptions: [REQUIRED]
            The new values of the AWS IoT Analytics logging options.
            roleArn (string) -- [REQUIRED]The ARN of the role that grants permission to AWS IoT Analytics to perform logging.
            level (string) -- [REQUIRED]The logging level. Currently, only 'ERROR' is supported.
            enabled (boolean) -- [REQUIRED]If true, logging is enabled for AWS IoT Analytics.
            

    """
    pass

def run_pipeline_activity(pipelineActivity=None, payloads=None):
    """
    Simulates the results of running a pipeline activity on a message payload.
    See also: AWS API Documentation
    
    
    :example: response = client.run_pipeline_activity(
        pipelineActivity={
            'channel': {
                'name': 'string',
                'channelName': 'string',
                'next': 'string'
            },
            'lambda': {
                'name': 'string',
                'lambdaName': 'string',
                'batchSize': 123,
                'next': 'string'
            },
            'datastore': {
                'name': 'string',
                'datastoreName': 'string'
            },
            'addAttributes': {
                'name': 'string',
                'attributes': {
                    'string': 'string'
                },
                'next': 'string'
            },
            'removeAttributes': {
                'name': 'string',
                'attributes': [
                    'string',
                ],
                'next': 'string'
            },
            'selectAttributes': {
                'name': 'string',
                'attributes': [
                    'string',
                ],
                'next': 'string'
            },
            'filter': {
                'name': 'string',
                'filter': 'string',
                'next': 'string'
            },
            'math': {
                'name': 'string',
                'attribute': 'string',
                'math': 'string',
                'next': 'string'
            },
            'deviceRegistryEnrich': {
                'name': 'string',
                'attribute': 'string',
                'thingName': 'string',
                'roleArn': 'string',
                'next': 'string'
            },
            'deviceShadowEnrich': {
                'name': 'string',
                'attribute': 'string',
                'thingName': 'string',
                'roleArn': 'string',
                'next': 'string'
            }
        },
        payloads=[
            b'bytes',
        ]
    )
    
    
    :type pipelineActivity: dict
    :param pipelineActivity: [REQUIRED]
            The pipeline activity that is run. This must not be a 'channel' activity or a 'datastore' activity because these activities are used in a pipeline only to load the original message and to store the (possibly) transformed message. If a 'lambda' activity is specified, only short-running Lambda functions (those with a timeout of less than 30 seconds or less) can be used.
            channel (dict) --Determines the source of the messages to be processed.
            name (string) -- [REQUIRED]The name of the 'channel' activity.
            channelName (string) -- [REQUIRED]The name of the channel from which the messages are processed.
            next (string) --The next activity in the pipeline.
            lambda (dict) --Runs a Lambda function to modify the message.
            name (string) -- [REQUIRED]The name of the 'lambda' activity.
            lambdaName (string) -- [REQUIRED]The name of the Lambda function that is run on the message.
            batchSize (integer) -- [REQUIRED]The number of messages passed to the Lambda function for processing.
            The AWS Lambda function must be able to process all of these messages within five minutes, which is the maximum timeout duration for Lambda functions.
            next (string) --The next activity in the pipeline.
            datastore (dict) --Specifies where to store the processed message data.
            name (string) -- [REQUIRED]The name of the 'datastore' activity.
            datastoreName (string) -- [REQUIRED]The name of the data store where processed messages are stored.
            addAttributes (dict) --Adds other attributes based on existing attributes in the message.
            name (string) -- [REQUIRED]The name of the 'addAttributes' activity.
            attributes (dict) -- [REQUIRED]A list of 1-50 'AttributeNameMapping' objects that map an existing attribute to a new attribute.
            Note
            The existing attributes remain in the message, so if you want to remove the originals, use 'RemoveAttributeActivity'.
            (string) --
            (string) --
            
            next (string) --The next activity in the pipeline.
            removeAttributes (dict) --Removes attributes from a message.
            name (string) -- [REQUIRED]The name of the 'removeAttributes' activity.
            attributes (list) -- [REQUIRED]A list of 1-50 attributes to remove from the message.
            (string) --
            next (string) --The next activity in the pipeline.
            selectAttributes (dict) --Creates a new message using only the specified attributes from the original message.
            name (string) -- [REQUIRED]The name of the 'selectAttributes' activity.
            attributes (list) -- [REQUIRED]A list of the attributes to select from the message.
            (string) --
            next (string) --The next activity in the pipeline.
            filter (dict) --Filters a message based on its attributes.
            name (string) -- [REQUIRED]The name of the 'filter' activity.
            filter (string) -- [REQUIRED]An expression that looks like a SQL WHERE clause that must return a Boolean value.
            next (string) --The next activity in the pipeline.
            math (dict) --Computes an arithmetic expression using the message's attributes and adds it to the message.
            name (string) -- [REQUIRED]The name of the 'math' activity.
            attribute (string) -- [REQUIRED]The name of the attribute that contains the result of the math operation.
            math (string) -- [REQUIRED]An expression that uses one or more existing attributes and must return an integer value.
            next (string) --The next activity in the pipeline.
            deviceRegistryEnrich (dict) --Adds data from the AWS IoT device registry to your message.
            name (string) -- [REQUIRED]The name of the 'deviceRegistryEnrich' activity.
            attribute (string) -- [REQUIRED]The name of the attribute that is added to the message.
            thingName (string) -- [REQUIRED]The name of the IoT device whose registry information is added to the message.
            roleArn (string) -- [REQUIRED]The ARN of the role that allows access to the device's registry information.
            next (string) --The next activity in the pipeline.
            deviceShadowEnrich (dict) --Adds information from the AWS IoT Device Shadows service to a message.
            name (string) -- [REQUIRED]The name of the 'deviceShadowEnrich' activity.
            attribute (string) -- [REQUIRED]The name of the attribute that is added to the message.
            thingName (string) -- [REQUIRED]The name of the IoT device whose shadow information is added to the message.
            roleArn (string) -- [REQUIRED]The ARN of the role that allows access to the device's shadow.
            next (string) --The next activity in the pipeline.
            
            

    :type payloads: list
    :param payloads: [REQUIRED]
            The sample message payloads on which the pipeline activity is run.
            (bytes) --
            

    :rtype: dict
    :return: {
        'payloads': [
            b'bytes',
        ],
        'logResult': 'string'
    }
    
    
    :returns: 
    (bytes) --
    
    """
    pass

def sample_channel_data(channelName=None, maxMessages=None, startTime=None, endTime=None):
    """
    Retrieves a sample of messages from the specified channel ingested during the specified timeframe. Up to 10 messages can be retrieved.
    See also: AWS API Documentation
    
    
    :example: response = client.sample_channel_data(
        channelName='string',
        maxMessages=123,
        startTime=datetime(2015, 1, 1),
        endTime=datetime(2015, 1, 1)
    )
    
    
    :type channelName: string
    :param channelName: [REQUIRED]
            The name of the channel whose message samples are retrieved.
            

    :type maxMessages: integer
    :param maxMessages: The number of sample messages to be retrieved. The limit is 10, the default is also 10.

    :type startTime: datetime
    :param startTime: The start of the time window from which sample messages are retrieved.

    :type endTime: datetime
    :param endTime: The end of the time window from which sample messages are retrieved.

    :rtype: dict
    :return: {
        'payloads': [
            b'bytes',
        ]
    }
    
    
    :returns: 
    (bytes) --
    
    """
    pass

def start_pipeline_reprocessing(pipelineName=None, startTime=None, endTime=None):
    """
    Starts the reprocessing of raw message data through the pipeline.
    See also: AWS API Documentation
    
    
    :example: response = client.start_pipeline_reprocessing(
        pipelineName='string',
        startTime=datetime(2015, 1, 1),
        endTime=datetime(2015, 1, 1)
    )
    
    
    :type pipelineName: string
    :param pipelineName: [REQUIRED]
            The name of the pipeline on which to start reprocessing.
            

    :type startTime: datetime
    :param startTime: The start time (inclusive) of raw message data that is reprocessed.

    :type endTime: datetime
    :param endTime: The end time (exclusive) of raw message data that is reprocessed.

    :rtype: dict
    :return: {
        'reprocessingId': 'string'
    }
    
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Adds to or modifies the tags of the given resource. Tags are metadata which can be used to manage a resource.
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
            The ARN of the resource whose tags you want to modify.
            

    :type tags: list
    :param tags: [REQUIRED]
            The new or modified tags for the resource.
            (dict) --A set of key/value pairs which are used to manage the resource.
            key (string) -- [REQUIRED]The tag's key.
            value (string) -- [REQUIRED]The tag's value.
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Removes the given tags (metadata) from the resource.
    See also: AWS API Documentation
    
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]
            The ARN of the resource whose tags you want to remove.
            

    :type tagKeys: list
    :param tagKeys: [REQUIRED]
            The keys of those tags which you want to remove.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_channel(channelName=None, retentionPeriod=None):
    """
    Updates the settings of a channel.
    See also: AWS API Documentation
    
    
    :example: response = client.update_channel(
        channelName='string',
        retentionPeriod={
            'unlimited': True|False,
            'numberOfDays': 123
        }
    )
    
    
    :type channelName: string
    :param channelName: [REQUIRED]
            The name of the channel to be updated.
            

    :type retentionPeriod: dict
    :param retentionPeriod: How long, in days, message data is kept for the channel.
            unlimited (boolean) --If true, message data is kept indefinitely.
            numberOfDays (integer) --The number of days that message data is kept. The 'unlimited' parameter must be false.
            

    """
    pass

def update_dataset(datasetName=None, actions=None, triggers=None, contentDeliveryRules=None, retentionPeriod=None):
    """
    Updates the settings of a data set.
    See also: AWS API Documentation
    
    
    :example: response = client.update_dataset(
        datasetName='string',
        actions=[
            {
                'actionName': 'string',
                'queryAction': {
                    'sqlQuery': 'string',
                    'filters': [
                        {
                            'deltaTime': {
                                'offsetSeconds': 123,
                                'timeExpression': 'string'
                            }
                        },
                    ]
                },
                'containerAction': {
                    'image': 'string',
                    'executionRoleArn': 'string',
                    'resourceConfiguration': {
                        'computeType': 'ACU_1'|'ACU_2',
                        'volumeSizeInGB': 123
                    },
                    'variables': [
                        {
                            'name': 'string',
                            'stringValue': 'string',
                            'doubleValue': 123.0,
                            'datasetContentVersionValue': {
                                'datasetName': 'string'
                            },
                            'outputFileUriValue': {
                                'fileName': 'string'
                            }
                        },
                    ]
                }
            },
        ],
        triggers=[
            {
                'schedule': {
                    'expression': 'string'
                },
                'dataset': {
                    'name': 'string'
                }
            },
        ],
        contentDeliveryRules=[
            {
                'entryName': 'string',
                'destination': {
                    'iotEventsDestinationConfiguration': {
                        'inputName': 'string',
                        'roleArn': 'string'
                    }
                }
            },
        ],
        retentionPeriod={
            'unlimited': True|False,
            'numberOfDays': 123
        }
    )
    
    
    :type datasetName: string
    :param datasetName: [REQUIRED]
            The name of the data set to update.
            

    :type actions: list
    :param actions: [REQUIRED]
            A list of 'DatasetAction' objects.
            (dict) --A 'DatasetAction' object that specifies how data set contents are automatically created.
            actionName (string) --The name of the data set action by which data set contents are automatically created.
            queryAction (dict) --An 'SqlQueryDatasetAction' object that uses an SQL query to automatically create data set contents.
            sqlQuery (string) -- [REQUIRED]A SQL query string.
            filters (list) --Pre-filters applied to message data.
            (dict) --Information which is used to filter message data, to segregate it according to the time frame in which it arrives.
            deltaTime (dict) --Used to limit data to that which has arrived since the last execution of the action.
            offsetSeconds (integer) -- [REQUIRED]The number of seconds of estimated 'in flight' lag time of message data. When you create data set contents using message data from a specified time frame, some message data may still be 'in flight' when processing begins, and so will not arrive in time to be processed. Use this field to make allowances for the 'in flight' time of your message data, so that data not processed from a previous time frame will be included with the next time frame. Without this, missed message data would be excluded from processing during the next time frame as well, because its timestamp places it within the previous time frame.
            timeExpression (string) -- [REQUIRED]An expression by which the time of the message data may be determined. This may be the name of a timestamp field, or a SQL expression which is used to derive the time the message data was generated.
            
            
            containerAction (dict) --Information which allows the system to run a containerized application in order to create the data set contents. The application must be in a Docker container along with any needed support libraries.
            image (string) -- [REQUIRED]The ARN of the Docker container stored in your account. The Docker container contains an application and needed support libraries and is used to generate data set contents.
            executionRoleArn (string) -- [REQUIRED]The ARN of the role which gives permission to the system to access needed resources in order to run the 'containerAction'. This includes, at minimum, permission to retrieve the data set contents which are the input to the containerized application.
            resourceConfiguration (dict) -- [REQUIRED]Configuration of the resource which executes the 'containerAction'.
            computeType (string) -- [REQUIRED]The type of the compute resource used to execute the 'containerAction'. Possible values are: ACU_1 (vCPU=4, memory=16GiB) or ACU_2 (vCPU=8, memory=32GiB).
            volumeSizeInGB (integer) -- [REQUIRED]The size (in GB) of the persistent storage available to the resource instance used to execute the 'containerAction' (min: 1, max: 50).
            variables (list) --The values of variables used within the context of the execution of the containerized application (basically, parameters passed to the application). Each variable must have a name and a value given by one of 'stringValue', 'datasetContentVersionValue', or 'outputFileUriValue'.
            (dict) --An instance of a variable to be passed to the 'containerAction' execution. Each variable must have a name and a value given by one of 'stringValue', 'datasetContentVersionValue', or 'outputFileUriValue'.
            name (string) -- [REQUIRED]The name of the variable.
            stringValue (string) --The value of the variable as a string.
            doubleValue (float) --The value of the variable as a double (numeric).
            datasetContentVersionValue (dict) --The value of the variable as a structure that specifies a data set content version.
            datasetName (string) -- [REQUIRED]The name of the data set whose latest contents are used as input to the notebook or application.
            outputFileUriValue (dict) --The value of the variable as a structure that specifies an output file URI.
            fileName (string) -- [REQUIRED]The URI of the location where data set contents are stored, usually the URI of a file in an S3 bucket.
            
            
            
            

    :type triggers: list
    :param triggers: A list of 'DatasetTrigger' objects. The list can be empty or can contain up to five DataSetTrigger objects.
            (dict) --The 'DatasetTrigger' that specifies when the data set is automatically updated.
            schedule (dict) --The 'Schedule' when the trigger is initiated.
            expression (string) --The expression that defines when to trigger an update. For more information, see Schedule Expressions for Rules in the Amazon CloudWatch documentation.
            dataset (dict) --The data set whose content creation triggers the creation of this data set's contents.
            name (string) -- [REQUIRED]The name of the data set whose content generation triggers the new data set content generation.
            
            

    :type contentDeliveryRules: list
    :param contentDeliveryRules: When data set contents are created they are delivered to destinations specified here.
            (dict) --When data set contents are created they are delivered to destination specified here.
            entryName (string) --The name of the data set content delivery rules entry.
            destination (dict) -- [REQUIRED]The destination to which data set contents are delivered.
            iotEventsDestinationConfiguration (dict) --Configuration information for delivery of data set contents to AWS IoT Events.
            inputName (string) -- [REQUIRED]The name of the AWS IoT Events input to which data set contents are delivered.
            roleArn (string) -- [REQUIRED]The ARN of the role which grants AWS IoT Analytics permission to deliver data set contents to an AWS IoT Events input.
            
            
            

    :type retentionPeriod: dict
    :param retentionPeriod: How long, in days, message data is kept for the data set.
            unlimited (boolean) --If true, message data is kept indefinitely.
            numberOfDays (integer) --The number of days that message data is kept. The 'unlimited' parameter must be false.
            

    """
    pass

def update_datastore(datastoreName=None, retentionPeriod=None):
    """
    Updates the settings of a data store.
    See also: AWS API Documentation
    
    
    :example: response = client.update_datastore(
        datastoreName='string',
        retentionPeriod={
            'unlimited': True|False,
            'numberOfDays': 123
        }
    )
    
    
    :type datastoreName: string
    :param datastoreName: [REQUIRED]
            The name of the data store to be updated.
            

    :type retentionPeriod: dict
    :param retentionPeriod: How long, in days, message data is kept for the data store.
            unlimited (boolean) --If true, message data is kept indefinitely.
            numberOfDays (integer) --The number of days that message data is kept. The 'unlimited' parameter must be false.
            

    """
    pass

def update_pipeline(pipelineName=None, pipelineActivities=None):
    """
    Updates the settings of a pipeline.
    See also: AWS API Documentation
    
    
    :example: response = client.update_pipeline(
        pipelineName='string',
        pipelineActivities=[
            {
                'channel': {
                    'name': 'string',
                    'channelName': 'string',
                    'next': 'string'
                },
                'lambda': {
                    'name': 'string',
                    'lambdaName': 'string',
                    'batchSize': 123,
                    'next': 'string'
                },
                'datastore': {
                    'name': 'string',
                    'datastoreName': 'string'
                },
                'addAttributes': {
                    'name': 'string',
                    'attributes': {
                        'string': 'string'
                    },
                    'next': 'string'
                },
                'removeAttributes': {
                    'name': 'string',
                    'attributes': [
                        'string',
                    ],
                    'next': 'string'
                },
                'selectAttributes': {
                    'name': 'string',
                    'attributes': [
                        'string',
                    ],
                    'next': 'string'
                },
                'filter': {
                    'name': 'string',
                    'filter': 'string',
                    'next': 'string'
                },
                'math': {
                    'name': 'string',
                    'attribute': 'string',
                    'math': 'string',
                    'next': 'string'
                },
                'deviceRegistryEnrich': {
                    'name': 'string',
                    'attribute': 'string',
                    'thingName': 'string',
                    'roleArn': 'string',
                    'next': 'string'
                },
                'deviceShadowEnrich': {
                    'name': 'string',
                    'attribute': 'string',
                    'thingName': 'string',
                    'roleArn': 'string',
                    'next': 'string'
                }
            },
        ]
    )
    
    
    :type pipelineName: string
    :param pipelineName: [REQUIRED]
            The name of the pipeline to update.
            

    :type pipelineActivities: list
    :param pipelineActivities: [REQUIRED]
            A list of 'PipelineActivity' objects.
            The list can be 1-25 PipelineActivity objects. Activities perform transformations on your messages, such as removing, renaming or adding message attributes; filtering messages based on attribute values; invoking your Lambda functions on messages for advanced processing; or performing mathematical transformations to normalize device data.
            (dict) --An activity that performs a transformation on a message.
            channel (dict) --Determines the source of the messages to be processed.
            name (string) -- [REQUIRED]The name of the 'channel' activity.
            channelName (string) -- [REQUIRED]The name of the channel from which the messages are processed.
            next (string) --The next activity in the pipeline.
            lambda (dict) --Runs a Lambda function to modify the message.
            name (string) -- [REQUIRED]The name of the 'lambda' activity.
            lambdaName (string) -- [REQUIRED]The name of the Lambda function that is run on the message.
            batchSize (integer) -- [REQUIRED]The number of messages passed to the Lambda function for processing.
            The AWS Lambda function must be able to process all of these messages within five minutes, which is the maximum timeout duration for Lambda functions.
            next (string) --The next activity in the pipeline.
            datastore (dict) --Specifies where to store the processed message data.
            name (string) -- [REQUIRED]The name of the 'datastore' activity.
            datastoreName (string) -- [REQUIRED]The name of the data store where processed messages are stored.
            addAttributes (dict) --Adds other attributes based on existing attributes in the message.
            name (string) -- [REQUIRED]The name of the 'addAttributes' activity.
            attributes (dict) -- [REQUIRED]A list of 1-50 'AttributeNameMapping' objects that map an existing attribute to a new attribute.
            Note
            The existing attributes remain in the message, so if you want to remove the originals, use 'RemoveAttributeActivity'.
            (string) --
            (string) --
            
            next (string) --The next activity in the pipeline.
            removeAttributes (dict) --Removes attributes from a message.
            name (string) -- [REQUIRED]The name of the 'removeAttributes' activity.
            attributes (list) -- [REQUIRED]A list of 1-50 attributes to remove from the message.
            (string) --
            next (string) --The next activity in the pipeline.
            selectAttributes (dict) --Creates a new message using only the specified attributes from the original message.
            name (string) -- [REQUIRED]The name of the 'selectAttributes' activity.
            attributes (list) -- [REQUIRED]A list of the attributes to select from the message.
            (string) --
            next (string) --The next activity in the pipeline.
            filter (dict) --Filters a message based on its attributes.
            name (string) -- [REQUIRED]The name of the 'filter' activity.
            filter (string) -- [REQUIRED]An expression that looks like a SQL WHERE clause that must return a Boolean value.
            next (string) --The next activity in the pipeline.
            math (dict) --Computes an arithmetic expression using the message's attributes and adds it to the message.
            name (string) -- [REQUIRED]The name of the 'math' activity.
            attribute (string) -- [REQUIRED]The name of the attribute that contains the result of the math operation.
            math (string) -- [REQUIRED]An expression that uses one or more existing attributes and must return an integer value.
            next (string) --The next activity in the pipeline.
            deviceRegistryEnrich (dict) --Adds data from the AWS IoT device registry to your message.
            name (string) -- [REQUIRED]The name of the 'deviceRegistryEnrich' activity.
            attribute (string) -- [REQUIRED]The name of the attribute that is added to the message.
            thingName (string) -- [REQUIRED]The name of the IoT device whose registry information is added to the message.
            roleArn (string) -- [REQUIRED]The ARN of the role that allows access to the device's registry information.
            next (string) --The next activity in the pipeline.
            deviceShadowEnrich (dict) --Adds information from the AWS IoT Device Shadows service to a message.
            name (string) -- [REQUIRED]The name of the 'deviceShadowEnrich' activity.
            attribute (string) -- [REQUIRED]The name of the attribute that is added to the message.
            thingName (string) -- [REQUIRED]The name of the IoT device whose shadow information is added to the message.
            roleArn (string) -- [REQUIRED]The ARN of the role that allows access to the device's shadow.
            next (string) --The next activity in the pipeline.
            
            

    """
    pass

