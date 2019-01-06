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

def batch_detect_dominant_language(TextList=None):
    """
    Determines the dominant language of the input text for a batch of documents. For a list of languages that Amazon Comprehend can detect, see Amazon Comprehend Supported Languages .
    See also: AWS API Documentation
    
    
    :example: response = client.batch_detect_dominant_language(
        TextList=[
            'string',
        ]
    )
    
    
    :type TextList: list
    :param TextList: [REQUIRED]
            A list containing the text of the input documents. The list can contain a maximum of 25 documents. Each document should contain at least 20 characters and must contain fewer than 5,000 bytes of UTF-8 encoded characters.
            (string) --
            

    :rtype: dict
    :return: {
        'ResultList': [
            {
                'Index': 123,
                'Languages': [
                    {
                        'LanguageCode': 'string',
                        'Score': ...
                    },
                ]
            },
        ],
        'ErrorList': [
            {
                'Index': 123,
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def batch_detect_entities(TextList=None, LanguageCode=None):
    """
    Inspects the text of a batch of documents for named entities and returns information about them. For more information about named entities, see  how-entities
    See also: AWS API Documentation
    
    
    :example: response = client.batch_detect_entities(
        TextList=[
            'string',
        ],
        LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt'
    )
    
    
    :type TextList: list
    :param TextList: [REQUIRED]
            A list containing the text of the input documents. The list can contain a maximum of 25 documents. Each document must contain fewer than 5,000 bytes of UTF-8 encoded characters.
            (string) --
            

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]
            The language of the input documents. You can specify English ('en') or Spanish ('es'). All documents must be in the same language.
            

    :rtype: dict
    :return: {
        'ResultList': [
            {
                'Index': 123,
                'Entities': [
                    {
                        'Score': ...,
                        'Type': 'PERSON'|'LOCATION'|'ORGANIZATION'|'COMMERCIAL_ITEM'|'EVENT'|'DATE'|'QUANTITY'|'TITLE'|'OTHER',
                        'Text': 'string',
                        'BeginOffset': 123,
                        'EndOffset': 123
                    },
                ]
            },
        ],
        'ErrorList': [
            {
                'Index': 123,
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def batch_detect_key_phrases(TextList=None, LanguageCode=None):
    """
    Detects the key noun phrases found in a batch of documents.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_detect_key_phrases(
        TextList=[
            'string',
        ],
        LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt'
    )
    
    
    :type TextList: list
    :param TextList: [REQUIRED]
            A list containing the text of the input documents. The list can contain a maximum of 25 documents. Each document must contain fewer that 5,000 bytes of UTF-8 encoded characters.
            (string) --
            

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]
            The language of the input documents. You can specify English ('en') or Spanish ('es'). All documents must be in the same language.
            

    :rtype: dict
    :return: {
        'ResultList': [
            {
                'Index': 123,
                'KeyPhrases': [
                    {
                        'Score': ...,
                        'Text': 'string',
                        'BeginOffset': 123,
                        'EndOffset': 123
                    },
                ]
            },
        ],
        'ErrorList': [
            {
                'Index': 123,
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def batch_detect_sentiment(TextList=None, LanguageCode=None):
    """
    Inspects a batch of documents and returns an inference of the prevailing sentiment, POSITIVE , NEUTRAL , MIXED , or NEGATIVE , in each one.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_detect_sentiment(
        TextList=[
            'string',
        ],
        LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt'
    )
    
    
    :type TextList: list
    :param TextList: [REQUIRED]
            A list containing the text of the input documents. The list can contain a maximum of 25 documents. Each document must contain fewer that 5,000 bytes of UTF-8 encoded characters.
            (string) --
            

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]
            The language of the input documents. You can specify English ('en') or Spanish ('es'). All documents must be in the same language.
            

    :rtype: dict
    :return: {
        'ResultList': [
            {
                'Index': 123,
                'Sentiment': 'POSITIVE'|'NEGATIVE'|'NEUTRAL'|'MIXED',
                'SentimentScore': {
                    'Positive': ...,
                    'Negative': ...,
                    'Neutral': ...,
                    'Mixed': ...
                }
            },
        ],
        'ErrorList': [
            {
                'Index': 123,
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def batch_detect_syntax(TextList=None, LanguageCode=None):
    """
    Inspects the text of a batch of documents for the syntax and part of speech of the words in the document and returns information about them. For more information, see  how-syntax .
    See also: AWS API Documentation
    
    
    :example: response = client.batch_detect_syntax(
        TextList=[
            'string',
        ],
        LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt'
    )
    
    
    :type TextList: list
    :param TextList: [REQUIRED]
            A list containing the text of the input documents. The list can contain a maximum of 25 documents. Each document must contain fewer that 5,000 bytes of UTF-8 encoded characters.
            (string) --
            

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]
            The language of the input documents. You can specify English ('en') or Spanish ('es'). All documents must be in the same language.
            

    :rtype: dict
    :return: {
        'ResultList': [
            {
                'Index': 123,
                'SyntaxTokens': [
                    {
                        'TokenId': 123,
                        'Text': 'string',
                        'BeginOffset': 123,
                        'EndOffset': 123,
                        'PartOfSpeech': {
                            'Tag': 'ADJ'|'ADP'|'ADV'|'AUX'|'CONJ'|'CCONJ'|'DET'|'INTJ'|'NOUN'|'NUM'|'O'|'PART'|'PRON'|'PROPN'|'PUNCT'|'SCONJ'|'SYM'|'VERB',
                            'Score': ...
                        }
                    },
                ]
            },
        ],
        'ErrorList': [
            {
                'Index': 123,
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
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

def create_document_classifier(DocumentClassifierName=None, DataAccessRoleArn=None, InputDataConfig=None, ClientRequestToken=None, LanguageCode=None):
    """
    Creates a new document classifier that you can use to categorize documents. To create a classifier you provide a set of training documents that labeled with the categories that you want to use. After the classifier is trained you can use it to categorize a set of labeled documents into the categories. For more information, see  how-document-classification .
    See also: AWS API Documentation
    
    
    :example: response = client.create_document_classifier(
        DocumentClassifierName='string',
        DataAccessRoleArn='string',
        InputDataConfig={
            'S3Uri': 'string'
        },
        ClientRequestToken='string',
        LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt'
    )
    
    
    :type DocumentClassifierName: string
    :param DocumentClassifierName: [REQUIRED]
            The name of the document classifier.
            

    :type DataAccessRoleArn: string
    :param DataAccessRoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that grants Amazon Comprehend read access to your input data.
            

    :type InputDataConfig: dict
    :param InputDataConfig: [REQUIRED]
            Specifies the format and location of the input data for the job.
            S3Uri (string) -- [REQUIRED]The Amazon S3 URI for the input data. The S3 bucket must be in the same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of input files.
            For example, if you use the URI S3://bucketName/prefix , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.
            

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.
            This field is autopopulated if not provided.
            

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]
            The language of the input documents. You can specify English ('en') or Spanish ('es'). All documents must be in the same language.
            

    :rtype: dict
    :return: {
        'DocumentClassifierArn': 'string'
    }
    
    
    """
    pass

def create_entity_recognizer(RecognizerName=None, DataAccessRoleArn=None, InputDataConfig=None, ClientRequestToken=None, LanguageCode=None):
    """
    Creates an entity recognizer using submitted files. After your CreateEntityRecognizer request is submitted, you can check job status using the API.
    See also: AWS API Documentation
    
    
    :example: response = client.create_entity_recognizer(
        RecognizerName='string',
        DataAccessRoleArn='string',
        InputDataConfig={
            'EntityTypes': [
                {
                    'Type': 'string'
                },
            ],
            'Documents': {
                'S3Uri': 'string'
            },
            'Annotations': {
                'S3Uri': 'string'
            },
            'EntityList': {
                'S3Uri': 'string'
            }
        },
        ClientRequestToken='string',
        LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt'
    )
    
    
    :type RecognizerName: string
    :param RecognizerName: [REQUIRED]
            The name given to the newly created recognizer. Recognizer names can be a maximum of 256 characters. Alphanumeric characters, hyphens (-) and underscores (_) are allowed. The name must be unique in the account/region.
            

    :type DataAccessRoleArn: string
    :param DataAccessRoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that grants Amazon Comprehend read access to your input data.
            

    :type InputDataConfig: dict
    :param InputDataConfig: [REQUIRED]
            Specifies the format and location of the input data. The S3 bucket containing the input data must be located in the same region as the entity recognizer being created.
            EntityTypes (list) -- [REQUIRED]The entity types in the input data for an entity recognizer.
            (dict) --Information about an individual item on a list of entity types.
            Type (string) -- [REQUIRED]Entity type of an item on an entity type list.
            
            Documents (dict) -- [REQUIRED]S3 location of the documents folder for an entity recognizer
            S3Uri (string) -- [REQUIRED]Specifies the Amazon S3 location where the training documents for an entity recognizer are located. The URI must be in the same region as the API endpoint that you are calling.
            Annotations (dict) --S3 location of the annotations file for an entity recognizer.
            S3Uri (string) -- [REQUIRED]Specifies the Amazon S3 location where the annotations for an entity recognizer are located. The URI must be in the same region as the API endpoint that you are calling.
            EntityList (dict) --S3 location of the entity list for an entity recognizer.
            S3Uri (string) -- [REQUIRED]Specifies the Amazon S3 location where the entity list is located. The URI must be in the same region as the API endpoint that you are calling.
            
            

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.
            This field is autopopulated if not provided.
            

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]
            The language of the input documents. All documents must be in the same language. Only English ('en') is currently supported.
            

    :rtype: dict
    :return: {
        'EntityRecognizerArn': 'string'
    }
    
    
    """
    pass

def delete_document_classifier(DocumentClassifierArn=None):
    """
    Deletes a previously created document classifier
    Only those classifiers that are in terminated states (IN_ERROR, TRAINED) will be deleted. If an active inference job is using the model, a ResourceInUseException will be returned.
    This is an asynchronous action that puts the classifier into a DELETING state, and it is then removed by a background job. Once removed, the classifier disappears from your account and is no longer available for use.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_document_classifier(
        DocumentClassifierArn='string'
    )
    
    
    :type DocumentClassifierArn: string
    :param DocumentClassifierArn: [REQUIRED]
            The Amazon Resource Name (ARN) that identifies the document classifier.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_entity_recognizer(EntityRecognizerArn=None):
    """
    Deletes an entity recognizer.
    Only those recognizers that are in terminated states (IN_ERROR, TRAINED) will be deleted. If an active inference job is using the model, a ResourceInUseException will be returned.
    This is an asynchronous action that puts the recognizer into a DELETING state, and it is then removed by a background job. Once removed, the recognizer disappears from your account and is no longer available for use.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_entity_recognizer(
        EntityRecognizerArn='string'
    )
    
    
    :type EntityRecognizerArn: string
    :param EntityRecognizerArn: [REQUIRED]
            The Amazon Resource Name (ARN) that identifies the entity recognizer.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_document_classification_job(JobId=None):
    """
    Gets the properties associated with a document classification job. Use this operation to get the status of a classification job.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_document_classification_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]
            The identifier that Amazon Comprehend generated for the job. The operation returns this identifier in its response.
            

    :rtype: dict
    :return: {
        'DocumentClassificationJobProperties': {
            'JobId': 'string',
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'Message': 'string',
            'SubmitTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'DocumentClassifierArn': 'string',
            'InputDataConfig': {
                'S3Uri': 'string',
                'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
            },
            'OutputDataConfig': {
                'S3Uri': 'string'
            },
            'DataAccessRoleArn': 'string'
        }
    }
    
    
    """
    pass

def describe_document_classifier(DocumentClassifierArn=None):
    """
    Gets the properties associated with a document classifier.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_document_classifier(
        DocumentClassifierArn='string'
    )
    
    
    :type DocumentClassifierArn: string
    :param DocumentClassifierArn: [REQUIRED]
            The Amazon Resource Name (ARN) that identifies the document classifier. The operation returns this identifier in its response.
            

    :rtype: dict
    :return: {
        'DocumentClassifierProperties': {
            'DocumentClassifierArn': 'string',
            'LanguageCode': 'en'|'es'|'fr'|'de'|'it'|'pt',
            'Status': 'SUBMITTED'|'TRAINING'|'DELETING'|'STOP_REQUESTED'|'STOPPED'|'IN_ERROR'|'TRAINED',
            'Message': 'string',
            'SubmitTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'TrainingStartTime': datetime(2015, 1, 1),
            'TrainingEndTime': datetime(2015, 1, 1),
            'InputDataConfig': {
                'S3Uri': 'string'
            },
            'ClassifierMetadata': {
                'NumberOfLabels': 123,
                'NumberOfTrainedDocuments': 123,
                'NumberOfTestDocuments': 123,
                'EvaluationMetrics': {
                    'Accuracy': 123.0,
                    'Precision': 123.0,
                    'Recall': 123.0,
                    'F1Score': 123.0
                }
            },
            'DataAccessRoleArn': 'string'
        }
    }
    
    
    """
    pass

def describe_dominant_language_detection_job(JobId=None):
    """
    Gets the properties associated with a dominant language detection job. Use this operation to get the status of a detection job.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_dominant_language_detection_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]
            The identifier that Amazon Comprehend generated for the job. The operation returns this identifier in its response.
            

    :rtype: dict
    :return: {
        'DominantLanguageDetectionJobProperties': {
            'JobId': 'string',
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'Message': 'string',
            'SubmitTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'InputDataConfig': {
                'S3Uri': 'string',
                'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
            },
            'OutputDataConfig': {
                'S3Uri': 'string'
            },
            'DataAccessRoleArn': 'string'
        }
    }
    
    
    """
    pass

def describe_entities_detection_job(JobId=None):
    """
    Gets the properties associated with an entities detection job. Use this operation to get the status of a detection job.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_entities_detection_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]
            The identifier that Amazon Comprehend generated for the job. The operation returns this identifier in its response.
            

    :rtype: dict
    :return: {
        'EntitiesDetectionJobProperties': {
            'JobId': 'string',
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'Message': 'string',
            'SubmitTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'EntityRecognizerArn': 'string',
            'InputDataConfig': {
                'S3Uri': 'string',
                'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
            },
            'OutputDataConfig': {
                'S3Uri': 'string'
            },
            'LanguageCode': 'en'|'es'|'fr'|'de'|'it'|'pt',
            'DataAccessRoleArn': 'string'
        }
    }
    
    
    """
    pass

def describe_entity_recognizer(EntityRecognizerArn=None):
    """
    Provides details about an entity recognizer including status, S3 buckets containing training data, recognizer metadata, metrics, and so on.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_entity_recognizer(
        EntityRecognizerArn='string'
    )
    
    
    :type EntityRecognizerArn: string
    :param EntityRecognizerArn: [REQUIRED]
            The Amazon Resource Name (ARN) that identifies the entity recognizer.
            

    :rtype: dict
    :return: {
        'EntityRecognizerProperties': {
            'EntityRecognizerArn': 'string',
            'LanguageCode': 'en'|'es'|'fr'|'de'|'it'|'pt',
            'Status': 'SUBMITTED'|'TRAINING'|'DELETING'|'STOP_REQUESTED'|'STOPPED'|'IN_ERROR'|'TRAINED',
            'Message': 'string',
            'SubmitTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'TrainingStartTime': datetime(2015, 1, 1),
            'TrainingEndTime': datetime(2015, 1, 1),
            'InputDataConfig': {
                'EntityTypes': [
                    {
                        'Type': 'string'
                    },
                ],
                'Documents': {
                    'S3Uri': 'string'
                },
                'Annotations': {
                    'S3Uri': 'string'
                },
                'EntityList': {
                    'S3Uri': 'string'
                }
            },
            'RecognizerMetadata': {
                'NumberOfTrainedDocuments': 123,
                'NumberOfTestDocuments': 123,
                'EvaluationMetrics': {
                    'Precision': 123.0,
                    'Recall': 123.0,
                    'F1Score': 123.0
                },
                'EntityTypes': [
                    {
                        'Type': 'string'
                    },
                ]
            },
            'DataAccessRoleArn': 'string'
        }
    }
    
    
    """
    pass

def describe_key_phrases_detection_job(JobId=None):
    """
    Gets the properties associated with a key phrases detection job. Use this operation to get the status of a detection job.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_key_phrases_detection_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]
            The identifier that Amazon Comprehend generated for the job. The operation returns this identifier in its response.
            

    :rtype: dict
    :return: {
        'KeyPhrasesDetectionJobProperties': {
            'JobId': 'string',
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'Message': 'string',
            'SubmitTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'InputDataConfig': {
                'S3Uri': 'string',
                'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
            },
            'OutputDataConfig': {
                'S3Uri': 'string'
            },
            'LanguageCode': 'en'|'es'|'fr'|'de'|'it'|'pt',
            'DataAccessRoleArn': 'string'
        }
    }
    
    
    """
    pass

def describe_sentiment_detection_job(JobId=None):
    """
    Gets the properties associated with a sentiment detection job. Use this operation to get the status of a detection job.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_sentiment_detection_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]
            The identifier that Amazon Comprehend generated for the job. The operation returns this identifier in its response.
            

    :rtype: dict
    :return: {
        'SentimentDetectionJobProperties': {
            'JobId': 'string',
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'Message': 'string',
            'SubmitTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'InputDataConfig': {
                'S3Uri': 'string',
                'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
            },
            'OutputDataConfig': {
                'S3Uri': 'string'
            },
            'LanguageCode': 'en'|'es'|'fr'|'de'|'it'|'pt',
            'DataAccessRoleArn': 'string'
        }
    }
    
    
    """
    pass

def describe_topics_detection_job(JobId=None):
    """
    Gets the properties associated with a topic detection job. Use this operation to get the status of a detection job.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_topics_detection_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]
            The identifier assigned by the user to the detection job.
            

    :rtype: dict
    :return: {
        'TopicsDetectionJobProperties': {
            'JobId': 'string',
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'Message': 'string',
            'SubmitTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'InputDataConfig': {
                'S3Uri': 'string',
                'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
            },
            'OutputDataConfig': {
                'S3Uri': 'string'
            },
            'NumberOfTopics': 123
        }
    }
    
    
    """
    pass

def detect_dominant_language(Text=None):
    """
    Determines the dominant language of the input text. For a list of languages that Amazon Comprehend can detect, see Amazon Comprehend Supported Languages .
    See also: AWS API Documentation
    
    
    :example: response = client.detect_dominant_language(
        Text='string'
    )
    
    
    :type Text: string
    :param Text: [REQUIRED]
            A UTF-8 text string. Each string should contain at least 20 characters and must contain fewer that 5,000 bytes of UTF-8 encoded characters.
            

    :rtype: dict
    :return: {
        'Languages': [
            {
                'LanguageCode': 'string',
                'Score': ...
            },
        ]
    }
    
    
    """
    pass

def detect_entities(Text=None, LanguageCode=None):
    """
    Inspects text for named entities, and returns information about them. For more information, about named entities, see  how-entities .
    See also: AWS API Documentation
    
    
    :example: response = client.detect_entities(
        Text='string',
        LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt'
    )
    
    
    :type Text: string
    :param Text: [REQUIRED]
            A UTF-8 text string. Each string must contain fewer that 5,000 bytes of UTF-8 encoded characters.
            

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]
            The language of the input documents. You can specify English ('en') or Spanish ('es'). All documents must be in the same language.
            

    :rtype: dict
    :return: {
        'Entities': [
            {
                'Score': ...,
                'Type': 'PERSON'|'LOCATION'|'ORGANIZATION'|'COMMERCIAL_ITEM'|'EVENT'|'DATE'|'QUANTITY'|'TITLE'|'OTHER',
                'Text': 'string',
                'BeginOffset': 123,
                'EndOffset': 123
            },
        ]
    }
    
    
    """
    pass

def detect_key_phrases(Text=None, LanguageCode=None):
    """
    Detects the key noun phrases found in the text.
    See also: AWS API Documentation
    
    
    :example: response = client.detect_key_phrases(
        Text='string',
        LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt'
    )
    
    
    :type Text: string
    :param Text: [REQUIRED]
            A UTF-8 text string. Each string must contain fewer that 5,000 bytes of UTF-8 encoded characters.
            

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]
            The language of the input documents. You can specify English ('en') or Spanish ('es'). All documents must be in the same language.
            

    :rtype: dict
    :return: {
        'KeyPhrases': [
            {
                'Score': ...,
                'Text': 'string',
                'BeginOffset': 123,
                'EndOffset': 123
            },
        ]
    }
    
    
    """
    pass

def detect_sentiment(Text=None, LanguageCode=None):
    """
    Inspects text and returns an inference of the prevailing sentiment (POSITIVE , NEUTRAL , MIXED , or NEGATIVE ).
    See also: AWS API Documentation
    
    
    :example: response = client.detect_sentiment(
        Text='string',
        LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt'
    )
    
    
    :type Text: string
    :param Text: [REQUIRED]
            A UTF-8 text string. Each string must contain fewer that 5,000 bytes of UTF-8 encoded characters.
            

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]
            The language of the input documents. You can specify English ('en') or Spanish ('es'). All documents must be in the same language.
            

    :rtype: dict
    :return: {
        'Sentiment': 'POSITIVE'|'NEGATIVE'|'NEUTRAL'|'MIXED',
        'SentimentScore': {
            'Positive': ...,
            'Negative': ...,
            'Neutral': ...,
            'Mixed': ...
        }
    }
    
    
    """
    pass

def detect_syntax(Text=None, LanguageCode=None):
    """
    Inspects text for syntax and the part of speech of words in the document. For more information,  how-syntax .
    See also: AWS API Documentation
    
    
    :example: response = client.detect_syntax(
        Text='string',
        LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt'
    )
    
    
    :type Text: string
    :param Text: [REQUIRED]
            A UTF-8 string. Each string must contain fewer that 5,000 bytes of UTF encoded characters.
            

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]
            The language code of the input documents. You can specify English ('en') or Spanish ('es').
            

    :rtype: dict
    :return: {
        'SyntaxTokens': [
            {
                'TokenId': 123,
                'Text': 'string',
                'BeginOffset': 123,
                'EndOffset': 123,
                'PartOfSpeech': {
                    'Tag': 'ADJ'|'ADP'|'ADV'|'AUX'|'CONJ'|'CCONJ'|'DET'|'INTJ'|'NOUN'|'NUM'|'O'|'PART'|'PRON'|'PROPN'|'PUNCT'|'SCONJ'|'SYM'|'VERB',
                    'Score': ...
                }
            },
        ]
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

def list_document_classification_jobs(Filter=None, NextToken=None, MaxResults=None):
    """
    Gets a list of the documentation classification jobs that you have submitted.
    See also: AWS API Documentation
    
    
    :example: response = client.list_document_classification_jobs(
        Filter={
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'SubmitTimeBefore': datetime(2015, 1, 1),
            'SubmitTimeAfter': datetime(2015, 1, 1)
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filter: dict
    :param Filter: Filters the jobs that are returned. You can filter jobs on their names, status, or the date and time that they were submitted. You can only set one filter at a time.
            JobName (string) --Filters on the name of the job.
            JobStatus (string) --Filters the list based on job status. Returns only jobs with the specified status.
            SubmitTimeBefore (datetime) --Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted after the specified time. Jobs are returned in ascending order, oldest to newest.
            SubmitTimeAfter (datetime) --Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted before the specified time. Jobs are returned in descending order, newest to oldest.
            

    :type NextToken: string
    :param NextToken: Identifies the next page of results to return.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in each page. The default is 100.

    :rtype: dict
    :return: {
        'DocumentClassificationJobPropertiesList': [
            {
                'JobId': 'string',
                'JobName': 'string',
                'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
                'Message': 'string',
                'SubmitTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'DocumentClassifierArn': 'string',
                'InputDataConfig': {
                    'S3Uri': 'string',
                    'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
                },
                'OutputDataConfig': {
                    'S3Uri': 'string'
                },
                'DataAccessRoleArn': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ONE_DOC_PER_FILE - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers.
    ONE_DOC_PER_LINE - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages.
    
    """
    pass

def list_document_classifiers(Filter=None, NextToken=None, MaxResults=None):
    """
    Gets a list of the document classifiers that you have created.
    See also: AWS API Documentation
    
    
    :example: response = client.list_document_classifiers(
        Filter={
            'Status': 'SUBMITTED'|'TRAINING'|'DELETING'|'STOP_REQUESTED'|'STOPPED'|'IN_ERROR'|'TRAINED',
            'SubmitTimeBefore': datetime(2015, 1, 1),
            'SubmitTimeAfter': datetime(2015, 1, 1)
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filter: dict
    :param Filter: Filters the jobs that are returned. You can filter jobs on their name, status, or the date and time that they were submitted. You can only set one filter at a time.
            Status (string) --Filters the list of classifiers based on status.
            SubmitTimeBefore (datetime) --Filters the list of classifiers based on the time that the classifier was submitted for processing. Returns only classifiers submitted before the specified time. Classifiers are returned in ascending order, oldest to newest.
            SubmitTimeAfter (datetime) --Filters the list of classifiers based on the time that the classifier was submitted for processing. Returns only classifiers submitted after the specified time. Classifiers are returned in descending order, newest to oldest.
            

    :type NextToken: string
    :param NextToken: Identifies the next page of results to return.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in each page. The default is 100.

    :rtype: dict
    :return: {
        'DocumentClassifierPropertiesList': [
            {
                'DocumentClassifierArn': 'string',
                'LanguageCode': 'en'|'es'|'fr'|'de'|'it'|'pt',
                'Status': 'SUBMITTED'|'TRAINING'|'DELETING'|'STOP_REQUESTED'|'STOPPED'|'IN_ERROR'|'TRAINED',
                'Message': 'string',
                'SubmitTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'TrainingStartTime': datetime(2015, 1, 1),
                'TrainingEndTime': datetime(2015, 1, 1),
                'InputDataConfig': {
                    'S3Uri': 'string'
                },
                'ClassifierMetadata': {
                    'NumberOfLabels': 123,
                    'NumberOfTrainedDocuments': 123,
                    'NumberOfTestDocuments': 123,
                    'EvaluationMetrics': {
                        'Accuracy': 123.0,
                        'Precision': 123.0,
                        'Recall': 123.0,
                        'F1Score': 123.0
                    }
                },
                'DataAccessRoleArn': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_dominant_language_detection_jobs(Filter=None, NextToken=None, MaxResults=None):
    """
    Gets a list of the dominant language detection jobs that you have submitted.
    See also: AWS API Documentation
    
    
    :example: response = client.list_dominant_language_detection_jobs(
        Filter={
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'SubmitTimeBefore': datetime(2015, 1, 1),
            'SubmitTimeAfter': datetime(2015, 1, 1)
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filter: dict
    :param Filter: Filters that jobs that are returned. You can filter jobs on their name, status, or the date and time that they were submitted. You can only set one filter at a time.
            JobName (string) --Filters on the name of the job.
            JobStatus (string) --Filters the list of jobs based on job status. Returns only jobs with the specified status.
            SubmitTimeBefore (datetime) --Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to newest.
            SubmitTimeAfter (datetime) --Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted after the specified time. Jobs are returned in descending order, newest to oldest.
            

    :type NextToken: string
    :param NextToken: Identifies the next page of results to return.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in each page. The default is 100.

    :rtype: dict
    :return: {
        'DominantLanguageDetectionJobPropertiesList': [
            {
                'JobId': 'string',
                'JobName': 'string',
                'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
                'Message': 'string',
                'SubmitTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'InputDataConfig': {
                    'S3Uri': 'string',
                    'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
                },
                'OutputDataConfig': {
                    'S3Uri': 'string'
                },
                'DataAccessRoleArn': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ONE_DOC_PER_FILE - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers.
    ONE_DOC_PER_LINE - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages.
    
    """
    pass

def list_entities_detection_jobs(Filter=None, NextToken=None, MaxResults=None):
    """
    Gets a list of the entity detection jobs that you have submitted.
    See also: AWS API Documentation
    
    
    :example: response = client.list_entities_detection_jobs(
        Filter={
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'SubmitTimeBefore': datetime(2015, 1, 1),
            'SubmitTimeAfter': datetime(2015, 1, 1)
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filter: dict
    :param Filter: Filters the jobs that are returned. You can filter jobs on their name, status, or the date and time that they were submitted. You can only set one filter at a time.
            JobName (string) --Filters on the name of the job.
            JobStatus (string) --Filters the list of jobs based on job status. Returns only jobs with the specified status.
            SubmitTimeBefore (datetime) --Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to newest.
            SubmitTimeAfter (datetime) --Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted after the specified time. Jobs are returned in descending order, newest to oldest.
            

    :type NextToken: string
    :param NextToken: Identifies the next page of results to return.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in each page. The default is 100.

    :rtype: dict
    :return: {
        'EntitiesDetectionJobPropertiesList': [
            {
                'JobId': 'string',
                'JobName': 'string',
                'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
                'Message': 'string',
                'SubmitTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'EntityRecognizerArn': 'string',
                'InputDataConfig': {
                    'S3Uri': 'string',
                    'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
                },
                'OutputDataConfig': {
                    'S3Uri': 'string'
                },
                'LanguageCode': 'en'|'es'|'fr'|'de'|'it'|'pt',
                'DataAccessRoleArn': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ONE_DOC_PER_FILE - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers.
    ONE_DOC_PER_LINE - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages.
    
    """
    pass

def list_entity_recognizers(Filter=None, NextToken=None, MaxResults=None):
    """
    Gets a list of the properties of all entity recognizers that you created, including recognizers currently in training. Allows you to filter the list of recognizers based on criteria such as status and submission time. This call returns up to 500 entity recognizers in the list, with a default number of 100 recognizers in the list.
    The results of this list are not in any particular order. Please get the list and sort locally if needed.
    See also: AWS API Documentation
    
    
    :example: response = client.list_entity_recognizers(
        Filter={
            'Status': 'SUBMITTED'|'TRAINING'|'DELETING'|'STOP_REQUESTED'|'STOPPED'|'IN_ERROR'|'TRAINED',
            'SubmitTimeBefore': datetime(2015, 1, 1),
            'SubmitTimeAfter': datetime(2015, 1, 1)
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filter: dict
    :param Filter: Filters the list of entities returned. You can filter on Status , SubmitTimeBefore , or SubmitTimeAfter . You can only set one filter at a time.
            Status (string) --The status of an entity recognizer.
            SubmitTimeBefore (datetime) --Filters the list of entities based on the time that the list was submitted for processing. Returns only jobs submitted before the specified time. Jobs are returned in descending order, newest to oldest.
            SubmitTimeAfter (datetime) --Filters the list of entities based on the time that the list was submitted for processing. Returns only jobs submitted after the specified time. Jobs are returned in ascending order, oldest to newest.
            

    :type NextToken: string
    :param NextToken: Identifies the next page of results to return.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return on each page. The default is 100.

    :rtype: dict
    :return: {
        'EntityRecognizerPropertiesList': [
            {
                'EntityRecognizerArn': 'string',
                'LanguageCode': 'en'|'es'|'fr'|'de'|'it'|'pt',
                'Status': 'SUBMITTED'|'TRAINING'|'DELETING'|'STOP_REQUESTED'|'STOPPED'|'IN_ERROR'|'TRAINED',
                'Message': 'string',
                'SubmitTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'TrainingStartTime': datetime(2015, 1, 1),
                'TrainingEndTime': datetime(2015, 1, 1),
                'InputDataConfig': {
                    'EntityTypes': [
                        {
                            'Type': 'string'
                        },
                    ],
                    'Documents': {
                        'S3Uri': 'string'
                    },
                    'Annotations': {
                        'S3Uri': 'string'
                    },
                    'EntityList': {
                        'S3Uri': 'string'
                    }
                },
                'RecognizerMetadata': {
                    'NumberOfTrainedDocuments': 123,
                    'NumberOfTestDocuments': 123,
                    'EvaluationMetrics': {
                        'Precision': 123.0,
                        'Recall': 123.0,
                        'F1Score': 123.0
                    },
                    'EntityTypes': [
                        {
                            'Type': 'string'
                        },
                    ]
                },
                'DataAccessRoleArn': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_key_phrases_detection_jobs(Filter=None, NextToken=None, MaxResults=None):
    """
    Get a list of key phrase detection jobs that you have submitted.
    See also: AWS API Documentation
    
    
    :example: response = client.list_key_phrases_detection_jobs(
        Filter={
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'SubmitTimeBefore': datetime(2015, 1, 1),
            'SubmitTimeAfter': datetime(2015, 1, 1)
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filter: dict
    :param Filter: Filters the jobs that are returned. You can filter jobs on their name, status, or the date and time that they were submitted. You can only set one filter at a time.
            JobName (string) --Filters on the name of the job.
            JobStatus (string) --Filters the list of jobs based on job status. Returns only jobs with the specified status.
            SubmitTimeBefore (datetime) --Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to newest.
            SubmitTimeAfter (datetime) --Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted after the specified time. Jobs are returned in descending order, newest to oldest.
            

    :type NextToken: string
    :param NextToken: Identifies the next page of results to return.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in each page. The default is 100.

    :rtype: dict
    :return: {
        'KeyPhrasesDetectionJobPropertiesList': [
            {
                'JobId': 'string',
                'JobName': 'string',
                'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
                'Message': 'string',
                'SubmitTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'InputDataConfig': {
                    'S3Uri': 'string',
                    'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
                },
                'OutputDataConfig': {
                    'S3Uri': 'string'
                },
                'LanguageCode': 'en'|'es'|'fr'|'de'|'it'|'pt',
                'DataAccessRoleArn': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ONE_DOC_PER_FILE - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers.
    ONE_DOC_PER_LINE - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages.
    
    """
    pass

def list_sentiment_detection_jobs(Filter=None, NextToken=None, MaxResults=None):
    """
    Gets a list of sentiment detection jobs that you have submitted.
    See also: AWS API Documentation
    
    
    :example: response = client.list_sentiment_detection_jobs(
        Filter={
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'SubmitTimeBefore': datetime(2015, 1, 1),
            'SubmitTimeAfter': datetime(2015, 1, 1)
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filter: dict
    :param Filter: Filters the jobs that are returned. You can filter jobs on their name, status, or the date and time that they were submitted. You can only set one filter at a time.
            JobName (string) --Filters on the name of the job.
            JobStatus (string) --Filters the list of jobs based on job status. Returns only jobs with the specified status.
            SubmitTimeBefore (datetime) --Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to newest.
            SubmitTimeAfter (datetime) --Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted after the specified time. Jobs are returned in descending order, newest to oldest.
            

    :type NextToken: string
    :param NextToken: Identifies the next page of results to return.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in each page. The default is 100.

    :rtype: dict
    :return: {
        'SentimentDetectionJobPropertiesList': [
            {
                'JobId': 'string',
                'JobName': 'string',
                'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
                'Message': 'string',
                'SubmitTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'InputDataConfig': {
                    'S3Uri': 'string',
                    'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
                },
                'OutputDataConfig': {
                    'S3Uri': 'string'
                },
                'LanguageCode': 'en'|'es'|'fr'|'de'|'it'|'pt',
                'DataAccessRoleArn': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ONE_DOC_PER_FILE - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers.
    ONE_DOC_PER_LINE - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages.
    
    """
    pass

def list_topics_detection_jobs(Filter=None, NextToken=None, MaxResults=None):
    """
    Gets a list of the topic detection jobs that you have submitted.
    See also: AWS API Documentation
    
    
    :example: response = client.list_topics_detection_jobs(
        Filter={
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'SubmitTimeBefore': datetime(2015, 1, 1),
            'SubmitTimeAfter': datetime(2015, 1, 1)
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filter: dict
    :param Filter: Filters the jobs that are returned. Jobs can be filtered on their name, status, or the date and time that they were submitted. You can set only one filter at a time.
            JobName (string) --
            JobStatus (string) --Filters the list of topic detection jobs based on job status. Returns only jobs with the specified status.
            SubmitTimeBefore (datetime) --Filters the list of jobs based on the time that the job was submitted for processing. Only returns jobs submitted before the specified time. Jobs are returned in descending order, newest to oldest.
            SubmitTimeAfter (datetime) --Filters the list of jobs based on the time that the job was submitted for processing. Only returns jobs submitted after the specified time. Jobs are returned in ascending order, oldest to newest.
            

    :type NextToken: string
    :param NextToken: Identifies the next page of results to return.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in each page. The default is 100.

    :rtype: dict
    :return: {
        'TopicsDetectionJobPropertiesList': [
            {
                'JobId': 'string',
                'JobName': 'string',
                'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
                'Message': 'string',
                'SubmitTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'InputDataConfig': {
                    'S3Uri': 'string',
                    'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
                },
                'OutputDataConfig': {
                    'S3Uri': 'string'
                },
                'NumberOfTopics': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ONE_DOC_PER_FILE - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers.
    ONE_DOC_PER_LINE - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages.
    
    """
    pass

def start_document_classification_job(JobName=None, DocumentClassifierArn=None, InputDataConfig=None, OutputDataConfig=None, DataAccessRoleArn=None, ClientRequestToken=None):
    """
    Starts an asynchronous document classification job. Use the operation to track the progress of the job.
    See also: AWS API Documentation
    
    
    :example: response = client.start_document_classification_job(
        JobName='string',
        DocumentClassifierArn='string',
        InputDataConfig={
            'S3Uri': 'string',
            'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
        },
        OutputDataConfig={
            'S3Uri': 'string'
        },
        DataAccessRoleArn='string',
        ClientRequestToken='string'
    )
    
    
    :type JobName: string
    :param JobName: The identifier of the job.

    :type DocumentClassifierArn: string
    :param DocumentClassifierArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the document classifier to use to process the job.
            

    :type InputDataConfig: dict
    :param InputDataConfig: [REQUIRED]
            Specifies the format and location of the input data for the job.
            S3Uri (string) -- [REQUIRED]The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files.
            For example, if you use the URI S3://bucketName/prefix , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.
            InputFormat (string) --Specifies how the text in an input file should be processed:
            ONE_DOC_PER_FILE - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers.
            ONE_DOC_PER_LINE - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages.
            

    :type OutputDataConfig: dict
    :param OutputDataConfig: [REQUIRED]
            Specifies where to send the output files.
            S3Uri (string) -- [REQUIRED]When you use the OutputDataConfig object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.
            When the topic detection job is finished, the service creates an output file in a directory specific to the job. The S3Uri field contains the location of the output file, called output.tar.gz . It is a compressed archive that contains the ouput of the operation.
            

    :type DataAccessRoleArn: string
    :param DataAccessRoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data.
            

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for the request. If you do not set the client request token, Amazon Comprehend generates one.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'JobId': 'string',
        'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED'
    }
    
    
    :returns: 
    SUBMITTED - The job has been received and queued for processing.
    IN_PROGRESS - Amazon Comprehend is processing the job.
    COMPLETED - The job was successfully completed and the output is available.
    FAILED - The job did not complete. For details, use the operation.
    STOP_REQUESTED - Amazon Comprehend has received a stop request for the job and is processing the request.
    STOPPED - The job was successfully stopped without completing.
    
    """
    pass

def start_dominant_language_detection_job(InputDataConfig=None, OutputDataConfig=None, DataAccessRoleArn=None, JobName=None, ClientRequestToken=None):
    """
    Starts an asynchronous dominant language detection job for a collection of documents. Use the operation to track the status of a job.
    See also: AWS API Documentation
    
    
    :example: response = client.start_dominant_language_detection_job(
        InputDataConfig={
            'S3Uri': 'string',
            'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
        },
        OutputDataConfig={
            'S3Uri': 'string'
        },
        DataAccessRoleArn='string',
        JobName='string',
        ClientRequestToken='string'
    )
    
    
    :type InputDataConfig: dict
    :param InputDataConfig: [REQUIRED]
            Specifies the format and location of the input data for the job.
            S3Uri (string) -- [REQUIRED]The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files.
            For example, if you use the URI S3://bucketName/prefix , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.
            InputFormat (string) --Specifies how the text in an input file should be processed:
            ONE_DOC_PER_FILE - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers.
            ONE_DOC_PER_LINE - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages.
            

    :type OutputDataConfig: dict
    :param OutputDataConfig: [REQUIRED]
            Specifies where to send the output files.
            S3Uri (string) -- [REQUIRED]When you use the OutputDataConfig object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.
            When the topic detection job is finished, the service creates an output file in a directory specific to the job. The S3Uri field contains the location of the output file, called output.tar.gz . It is a compressed archive that contains the ouput of the operation.
            

    :type DataAccessRoleArn: string
    :param DataAccessRoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data. For more information, see https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions .
            

    :type JobName: string
    :param JobName: An identifier for the job.

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for the request. If you do not set the client request token, Amazon Comprehend generates one.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'JobId': 'string',
        'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED'
    }
    
    
    :returns: 
    SUBMITTED - The job has been received and is queued for processing.
    IN_PROGRESS - Amazon Comprehend is processing the job.
    COMPLETED - The job was successfully completed and the output is available.
    FAILED - The job did not complete. To get details, use the operation.
    
    """
    pass

def start_entities_detection_job(InputDataConfig=None, OutputDataConfig=None, DataAccessRoleArn=None, JobName=None, EntityRecognizerArn=None, LanguageCode=None, ClientRequestToken=None):
    """
    Starts an asynchronous entity detection job for a collection of documents. Use the operation to track the status of a job.
    This API can be used for either standard entity detection or custom entity recognition. In order to be used for custom entity recognition, the optional EntityRecognizerArn must be used in order to provide access to the recognizer being used to detect the custom entity.
    See also: AWS API Documentation
    
    
    :example: response = client.start_entities_detection_job(
        InputDataConfig={
            'S3Uri': 'string',
            'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
        },
        OutputDataConfig={
            'S3Uri': 'string'
        },
        DataAccessRoleArn='string',
        JobName='string',
        EntityRecognizerArn='string',
        LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt',
        ClientRequestToken='string'
    )
    
    
    :type InputDataConfig: dict
    :param InputDataConfig: [REQUIRED]
            Specifies the format and location of the input data for the job.
            S3Uri (string) -- [REQUIRED]The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files.
            For example, if you use the URI S3://bucketName/prefix , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.
            InputFormat (string) --Specifies how the text in an input file should be processed:
            ONE_DOC_PER_FILE - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers.
            ONE_DOC_PER_LINE - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages.
            

    :type OutputDataConfig: dict
    :param OutputDataConfig: [REQUIRED]
            Specifies where to send the output files.
            S3Uri (string) -- [REQUIRED]When you use the OutputDataConfig object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.
            When the topic detection job is finished, the service creates an output file in a directory specific to the job. The S3Uri field contains the location of the output file, called output.tar.gz . It is a compressed archive that contains the ouput of the operation.
            

    :type DataAccessRoleArn: string
    :param DataAccessRoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data. For more information, see https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions .
            

    :type JobName: string
    :param JobName: The identifier of the job.

    :type EntityRecognizerArn: string
    :param EntityRecognizerArn: The Amazon Resource Name (ARN) that identifies the specific entity recognizer to be used by the StartEntitiesDetectionJob . This ARN is optional and is only used for a custom entity recognition job.

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]
            The language of the input documents. All documents must be in the same language. You can specify any of the languages supported by Amazon Comprehend: English ('en'), Spanish ('es'), French ('fr'), German ('de'), Italian ('it'), or Portuguese ('pt'). If custom entities recognition is used, this parameter is ignored and the language used for training the model is used instead.
            

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'JobId': 'string',
        'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED'
    }
    
    
    :returns: 
    SUBMITTED - The job has been received and is queued for processing.
    IN_PROGRESS - Amazon Comprehend is processing the job.
    COMPLETED - The job was successfully completed and the output is available.
    FAILED - The job did not complete. To get details, use the operation.
    STOP_REQUESTED - Amazon Comprehend has received a stop request for the job and is processing the request.
    STOPPED - The job was successfully stopped without completing.
    
    """
    pass

def start_key_phrases_detection_job(InputDataConfig=None, OutputDataConfig=None, DataAccessRoleArn=None, JobName=None, LanguageCode=None, ClientRequestToken=None):
    """
    Starts an asynchronous key phrase detection job for a collection of documents. Use the operation to track the status of a job.
    See also: AWS API Documentation
    
    
    :example: response = client.start_key_phrases_detection_job(
        InputDataConfig={
            'S3Uri': 'string',
            'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
        },
        OutputDataConfig={
            'S3Uri': 'string'
        },
        DataAccessRoleArn='string',
        JobName='string',
        LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt',
        ClientRequestToken='string'
    )
    
    
    :type InputDataConfig: dict
    :param InputDataConfig: [REQUIRED]
            Specifies the format and location of the input data for the job.
            S3Uri (string) -- [REQUIRED]The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files.
            For example, if you use the URI S3://bucketName/prefix , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.
            InputFormat (string) --Specifies how the text in an input file should be processed:
            ONE_DOC_PER_FILE - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers.
            ONE_DOC_PER_LINE - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages.
            

    :type OutputDataConfig: dict
    :param OutputDataConfig: [REQUIRED]
            Specifies where to send the output files.
            S3Uri (string) -- [REQUIRED]When you use the OutputDataConfig object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.
            When the topic detection job is finished, the service creates an output file in a directory specific to the job. The S3Uri field contains the location of the output file, called output.tar.gz . It is a compressed archive that contains the ouput of the operation.
            

    :type DataAccessRoleArn: string
    :param DataAccessRoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data. For more information, see https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions .
            

    :type JobName: string
    :param JobName: The identifier of the job.

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]
            The language of the input documents. You can specify English ('en') or Spanish ('es'). All documents must be in the same language.
            

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'JobId': 'string',
        'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED'
    }
    
    
    :returns: 
    SUBMITTED - The job has been received and is queued for processing.
    IN_PROGRESS - Amazon Comprehend is processing the job.
    COMPLETED - The job was successfully completed and the output is available.
    FAILED - The job did not complete. To get details, use the operation.
    
    """
    pass

def start_sentiment_detection_job(InputDataConfig=None, OutputDataConfig=None, DataAccessRoleArn=None, JobName=None, LanguageCode=None, ClientRequestToken=None):
    """
    Starts an asynchronous sentiment detection job for a collection of documents. use the operation to track the status of a job.
    See also: AWS API Documentation
    
    
    :example: response = client.start_sentiment_detection_job(
        InputDataConfig={
            'S3Uri': 'string',
            'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
        },
        OutputDataConfig={
            'S3Uri': 'string'
        },
        DataAccessRoleArn='string',
        JobName='string',
        LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt',
        ClientRequestToken='string'
    )
    
    
    :type InputDataConfig: dict
    :param InputDataConfig: [REQUIRED]
            Specifies the format and location of the input data for the job.
            S3Uri (string) -- [REQUIRED]The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files.
            For example, if you use the URI S3://bucketName/prefix , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.
            InputFormat (string) --Specifies how the text in an input file should be processed:
            ONE_DOC_PER_FILE - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers.
            ONE_DOC_PER_LINE - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages.
            

    :type OutputDataConfig: dict
    :param OutputDataConfig: [REQUIRED]
            Specifies where to send the output files.
            S3Uri (string) -- [REQUIRED]When you use the OutputDataConfig object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.
            When the topic detection job is finished, the service creates an output file in a directory specific to the job. The S3Uri field contains the location of the output file, called output.tar.gz . It is a compressed archive that contains the ouput of the operation.
            

    :type DataAccessRoleArn: string
    :param DataAccessRoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data. For more information, see https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions .
            

    :type JobName: string
    :param JobName: The identifier of the job.

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]
            The language of the input documents. You can specify English ('en') or Spanish ('es'). All documents must be in the same language.
            

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'JobId': 'string',
        'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED'
    }
    
    
    :returns: 
    SUBMITTED - The job has been received and is queued for processing.
    IN_PROGRESS - Amazon Comprehend is processing the job.
    COMPLETED - The job was successfully completed and the output is available.
    FAILED - The job did not complete. To get details, use the operation.
    
    """
    pass

def start_topics_detection_job(InputDataConfig=None, OutputDataConfig=None, DataAccessRoleArn=None, JobName=None, NumberOfTopics=None, ClientRequestToken=None):
    """
    Starts an asynchronous topic detection job. Use the DescribeTopicDetectionJob operation to track the status of a job.
    See also: AWS API Documentation
    
    
    :example: response = client.start_topics_detection_job(
        InputDataConfig={
            'S3Uri': 'string',
            'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
        },
        OutputDataConfig={
            'S3Uri': 'string'
        },
        DataAccessRoleArn='string',
        JobName='string',
        NumberOfTopics=123,
        ClientRequestToken='string'
    )
    
    
    :type InputDataConfig: dict
    :param InputDataConfig: [REQUIRED]
            Specifies the format and location of the input data for the job.
            S3Uri (string) -- [REQUIRED]The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files.
            For example, if you use the URI S3://bucketName/prefix , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.
            InputFormat (string) --Specifies how the text in an input file should be processed:
            ONE_DOC_PER_FILE - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers.
            ONE_DOC_PER_LINE - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages.
            

    :type OutputDataConfig: dict
    :param OutputDataConfig: [REQUIRED]
            Specifies where to send the output files. The output is a compressed archive with two files, topic-terms.csv that lists the terms associated with each topic, and doc-topics.csv that lists the documents associated with each topic
            S3Uri (string) -- [REQUIRED]When you use the OutputDataConfig object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.
            When the topic detection job is finished, the service creates an output file in a directory specific to the job. The S3Uri field contains the location of the output file, called output.tar.gz . It is a compressed archive that contains the ouput of the operation.
            

    :type DataAccessRoleArn: string
    :param DataAccessRoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data. For more information, see https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions .
            

    :type JobName: string
    :param JobName: The identifier of the job.

    :type NumberOfTopics: integer
    :param NumberOfTopics: The number of topics to detect.

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for the request. If you do not set the client request token, Amazon Comprehend generates one.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'JobId': 'string',
        'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED'
    }
    
    
    :returns: 
    SUBMITTED - The job has been received and is queued for processing.
    IN_PROGRESS - Amazon Comprehend is processing the job.
    COMPLETED - The job was successfully completed and the output is available.
    FAILED - The job did not complete. To get details, use the DescribeTopicDetectionJob operation.
    
    """
    pass

def stop_dominant_language_detection_job(JobId=None):
    """
    Stops a dominant language detection job in progress.
    If the job state is IN_PROGRESS the job is marked for termination and put into the STOP_REQUESTED state. If the job completes before it can be stopped, it is put into the COMPLETED state; otherwise the job is stopped and put into the STOPPED state.
    If the job is in the COMPLETED or FAILED state when you call the StopDominantLanguageDetectionJob operation, the operation returns a 400 Internal Request Exception.
    When a job is stopped, any documents already processed are written to the output location.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_dominant_language_detection_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]
            The identifier of the dominant language detection job to stop.
            

    :rtype: dict
    :return: {
        'JobId': 'string',
        'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED'
    }
    
    
    """
    pass

def stop_entities_detection_job(JobId=None):
    """
    Stops an entities detection job in progress.
    If the job state is IN_PROGRESS the job is marked for termination and put into the STOP_REQUESTED state. If the job completes before it can be stopped, it is put into the COMPLETED state; otherwise the job is stopped and put into the STOPPED state.
    If the job is in the COMPLETED or FAILED state when you call the StopDominantLanguageDetectionJob operation, the operation returns a 400 Internal Request Exception.
    When a job is stopped, any documents already processed are written to the output location.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_entities_detection_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]
            The identifier of the entities detection job to stop.
            

    :rtype: dict
    :return: {
        'JobId': 'string',
        'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED'
    }
    
    
    """
    pass

def stop_key_phrases_detection_job(JobId=None):
    """
    Stops a key phrases detection job in progress.
    If the job state is IN_PROGRESS the job is marked for termination and put into the STOP_REQUESTED state. If the job completes before it can be stopped, it is put into the COMPLETED state; otherwise the job is stopped and put into the STOPPED state.
    If the job is in the COMPLETED or FAILED state when you call the StopDominantLanguageDetectionJob operation, the operation returns a 400 Internal Request Exception.
    When a job is stopped, any documents already processed are written to the output location.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_key_phrases_detection_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]
            The identifier of the key phrases detection job to stop.
            

    :rtype: dict
    :return: {
        'JobId': 'string',
        'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED'
    }
    
    
    """
    pass

def stop_sentiment_detection_job(JobId=None):
    """
    Stops a sentiment detection job in progress.
    If the job state is IN_PROGRESS the job is marked for termination and put into the STOP_REQUESTED state. If the job completes before it can be stopped, it is put into the COMPLETED state; otherwise the job is be stopped and put into the STOPPED state.
    If the job is in the COMPLETED or FAILED state when you call the StopDominantLanguageDetectionJob operation, the operation returns a 400 Internal Request Exception.
    When a job is stopped, any documents already processed are written to the output location.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_sentiment_detection_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]
            The identifier of the sentiment detection job to stop.
            

    :rtype: dict
    :return: {
        'JobId': 'string',
        'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED'
    }
    
    
    """
    pass

def stop_training_document_classifier(DocumentClassifierArn=None):
    """
    Stops a document classifier training job while in progress.
    If the training job state is TRAINING , the job is marked for termination and put into the STOP_REQUESTED state. If the training job completes before it can be stopped, it is put into the TRAINED ; otherwise the training job is stopped and put into the STOPPED state and the service sends back an HTTP 200 response with an empty HTTP body.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_training_document_classifier(
        DocumentClassifierArn='string'
    )
    
    
    :type DocumentClassifierArn: string
    :param DocumentClassifierArn: [REQUIRED]
            The Amazon Resource Name (ARN) that identifies the document classifier currently being trained.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def stop_training_entity_recognizer(EntityRecognizerArn=None):
    """
    Stops an entity recognizer training job while in progress.
    If the training job state is TRAINING , the job is marked for termination and put into the STOP_REQUESTED state. If the training job completes before it can be stopped, it is put into the TRAINED ; otherwise the training job is stopped and putted into the STOPPED state and the service sends back an HTTP 200 response with an empty HTTP body.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_training_entity_recognizer(
        EntityRecognizerArn='string'
    )
    
    
    :type EntityRecognizerArn: string
    :param EntityRecognizerArn: [REQUIRED]
            The Amazon Resource Name (ARN) that identifies the entity recognizer currently being trained.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

