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

def detect_entities(Text=None):
    """
    Inspects the clinical text for a variety of medical entities and returns specific information about them such as entity category, location, and confidence score on that information .
    See also: AWS API Documentation
    
    
    :example: response = client.detect_entities(
        Text='string'
    )
    
    
    :type Text: string
    :param Text: [REQUIRED]
            A UTF-8 text string containing the clinical content being examined for entities. Each string must contain fewer than 20,000 bytes of characters.
            

    :rtype: dict
    :return: {
        'Entities': [
            {
                'Id': 123,
                'BeginOffset': 123,
                'EndOffset': 123,
                'Score': ...,
                'Text': 'string',
                'Category': 'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'|'TEST_TREATMENT_PROCEDURE'|'ANATOMY',
                'Type': 'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY',
                'Traits': [
                    {
                        'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                        'Score': ...
                    },
                ],
                'Attributes': [
                    {
                        'Type': 'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY',
                        'Score': ...,
                        'RelationshipScore': ...,
                        'Id': 123,
                        'BeginOffset': 123,
                        'EndOffset': 123,
                        'Text': 'string',
                        'Traits': [
                            {
                                'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                                'Score': ...
                            },
                        ]
                    },
                ]
            },
        ],
        'UnmappedAttributes': [
            {
                'Type': 'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'|'TEST_TREATMENT_PROCEDURE'|'ANATOMY',
                'Attribute': {
                    'Type': 'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY',
                    'Score': ...,
                    'RelationshipScore': ...,
                    'Id': 123,
                    'BeginOffset': 123,
                    'EndOffset': 123,
                    'Text': 'string',
                    'Traits': [
                        {
                            'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                            'Score': ...
                        },
                    ]
                }
            },
        ],
        'PaginationToken': 'string'
    }
    
    
    """
    pass

def detect_phi(Text=None):
    """
    Inspects the clinical text for personal health information (PHI) entities and entity category, location, and confidence score on that information.
    See also: AWS API Documentation
    
    
    :example: response = client.detect_phi(
        Text='string'
    )
    
    
    :type Text: string
    :param Text: [REQUIRED]
            A UTF-8 text string containing the clinical content being examined for PHI entities. Each string must contain fewer than 20,000 bytes of characters.
            

    :rtype: dict
    :return: {
        'Entities': [
            {
                'Id': 123,
                'BeginOffset': 123,
                'EndOffset': 123,
                'Score': ...,
                'Text': 'string',
                'Category': 'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'|'TEST_TREATMENT_PROCEDURE'|'ANATOMY',
                'Type': 'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY',
                'Traits': [
                    {
                        'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                        'Score': ...
                    },
                ],
                'Attributes': [
                    {
                        'Type': 'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY',
                        'Score': ...,
                        'RelationshipScore': ...,
                        'Id': 123,
                        'BeginOffset': 123,
                        'EndOffset': 123,
                        'Text': 'string',
                        'Traits': [
                            {
                                'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                                'Score': ...
                            },
                        ]
                    },
                ]
            },
        ],
        'PaginationToken': 'string'
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

