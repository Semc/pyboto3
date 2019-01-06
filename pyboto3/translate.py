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

def delete_terminology(Name=None):
    """
    A synchronous action that deletes a custom terminology.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_terminology(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the custom terminology being deleted.
            

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

def get_terminology(Name=None, TerminologyDataFormat=None):
    """
    Retrieves a custom terminology.
    See also: AWS API Documentation
    
    
    :example: response = client.get_terminology(
        Name='string',
        TerminologyDataFormat='CSV'|'TMX'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the custom terminology being retrieved.
            

    :type TerminologyDataFormat: string
    :param TerminologyDataFormat: [REQUIRED]
            The data format of the custom terminology being retrieved, either CSV or TMX.
            

    :rtype: dict
    :return: {
        'TerminologyProperties': {
            'Name': 'string',
            'Description': 'string',
            'Arn': 'string',
            'SourceLanguageCode': 'string',
            'TargetLanguageCodes': [
                'string',
            ],
            'EncryptionKey': {
                'Type': 'KMS',
                'Id': 'string'
            },
            'SizeBytes': 123,
            'TermCount': 123,
            'CreatedAt': datetime(2015, 1, 1),
            'LastUpdatedAt': datetime(2015, 1, 1)
        },
        'TerminologyDataLocation': {
            'RepositoryType': 'string',
            'Location': 'string'
        }
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

def import_terminology(Name=None, MergeStrategy=None, Description=None, TerminologyData=None, EncryptionKey=None):
    """
    Creates or updates a custom terminology, depending on whether or not one already exists for the given terminology name. Importing a terminology with the same name as an existing one will merge the terminologies based on the chosen merge strategy. Currently, the only supported merge strategy is OVERWRITE, and so the imported terminology will overwrite an existing terminology of the same name.
    If you import a terminology that overwrites an existing one, the new terminology take up to 10 minutes to fully propagate and be available for use in a translation due to cache policies with the DataPlane service that performs the translations.
    See also: AWS API Documentation
    
    
    :example: response = client.import_terminology(
        Name='string',
        MergeStrategy='OVERWRITE',
        Description='string',
        TerminologyData={
            'File': b'bytes',
            'Format': 'CSV'|'TMX'
        },
        EncryptionKey={
            'Type': 'KMS',
            'Id': 'string'
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the custom terminology being imported.
            

    :type MergeStrategy: string
    :param MergeStrategy: [REQUIRED]
            The merge strategy of the custom terminology being imported. Currently, only the OVERWRITE merge strategy is supported. In this case, the imported terminology will overwrite an existing terminology of the same name.
            

    :type Description: string
    :param Description: The description of the custom terminology being imported.

    :type TerminologyData: dict
    :param TerminologyData: [REQUIRED]
            The terminology data for the custom terminology being imported.
            File (bytes) -- [REQUIRED]The file containing the custom terminology data.
            Format (string) -- [REQUIRED]The data format of the custom terminology. Either CSV or TMX.
            

    :type EncryptionKey: dict
    :param EncryptionKey: The encryption key for the custom terminology being imported.
            Type (string) -- [REQUIRED]The type of encryption key used by Amazon Translate to encrypt custom terminologies.
            Id (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the encryption key being used to encrypt the custom terminology.
            

    :rtype: dict
    :return: {
        'TerminologyProperties': {
            'Name': 'string',
            'Description': 'string',
            'Arn': 'string',
            'SourceLanguageCode': 'string',
            'TargetLanguageCodes': [
                'string',
            ],
            'EncryptionKey': {
                'Type': 'KMS',
                'Id': 'string'
            },
            'SizeBytes': 123,
            'TermCount': 123,
            'CreatedAt': datetime(2015, 1, 1),
            'LastUpdatedAt': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_terminologies(NextToken=None, MaxResults=None):
    """
    Provides a list of custom terminologies associated with your account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_terminologies(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: If the result of the request to ListTerminologies was truncated, include the NextToken to fetch the next group of custom terminologies.

    :type MaxResults: integer
    :param MaxResults: The maximum number of custom terminologies returned per list request.

    :rtype: dict
    :return: {
        'TerminologyPropertiesList': [
            {
                'Name': 'string',
                'Description': 'string',
                'Arn': 'string',
                'SourceLanguageCode': 'string',
                'TargetLanguageCodes': [
                    'string',
                ],
                'EncryptionKey': {
                    'Type': 'KMS',
                    'Id': 'string'
                },
                'SizeBytes': 123,
                'TermCount': 123,
                'CreatedAt': datetime(2015, 1, 1),
                'LastUpdatedAt': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def translate_text(Text=None, TerminologyNames=None, SourceLanguageCode=None, TargetLanguageCode=None):
    """
    Translates input text from the source language to the target language. It is not necessary to use English (en) as either the source or the target language but not all language combinations are supported by Amazon Translate. For more information, see Supported Language Pairs .
    To have Amazon Translate determine the source language of your text, you can specify auto in the SourceLanguageCode field. If you specify auto , Amazon Translate will call Amazon Comprehend to determine the source language.
    See also: AWS API Documentation
    
    
    :example: response = client.translate_text(
        Text='string',
        TerminologyNames=[
            'string',
        ],
        SourceLanguageCode='string',
        TargetLanguageCode='string'
    )
    
    
    :type Text: string
    :param Text: [REQUIRED]
            The text to translate. The text string can be a maximum of 5,000 bytes long. Depending on your character set, this may be fewer than 5,000 characters.
            

    :type TerminologyNames: list
    :param TerminologyNames: The TerminologyNames list that is taken as input to the TranslateText request. This has a minimum length of 0 and a maximum length of 1.
            (string) --
            

    :type SourceLanguageCode: string
    :param SourceLanguageCode: [REQUIRED]
            The language code for the language of the source text. The language must be a language supported by Amazon Translate.
            To have Amazon Translate determine the source language of your text, you can specify auto in the SourceLanguageCode field. If you specify auto , Amazon Translate will call Amazon Comprehend to determine the source language.
            

    :type TargetLanguageCode: string
    :param TargetLanguageCode: [REQUIRED]
            The language code requested for the language of the target text. The language must be a language supported by Amazon Translate.
            

    :rtype: dict
    :return: {
        'TranslatedText': 'string',
        'SourceLanguageCode': 'string',
        'TargetLanguageCode': 'string',
        'AppliedTerminologies': [
            {
                'Name': 'string',
                'Terms': [
                    {
                        'SourceText': 'string',
                        'TargetText': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    Text (string) -- [REQUIRED]
    The text to translate. The text string can be a maximum of 5,000 bytes long. Depending on your character set, this may be fewer than 5,000 characters.
    
    TerminologyNames (list) -- The TerminologyNames list that is taken as input to the TranslateText request. This has a minimum length of 0 and a maximum length of 1.
    
    (string) --
    
    
    SourceLanguageCode (string) -- [REQUIRED]
    The language code for the language of the source text. The language must be a language supported by Amazon Translate.
    To have Amazon Translate determine the source language of your text, you can specify auto in the SourceLanguageCode field. If you specify auto , Amazon Translate will call Amazon Comprehend to determine the source language.
    
    TargetLanguageCode (string) -- [REQUIRED]
    The language code requested for the language of the target text. The language must be a language supported by Amazon Translate.
    
    
    """
    pass

