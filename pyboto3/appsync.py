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

def create_api_key(apiId=None, description=None, expires=None):
    """
    Creates a unique key that you can distribute to clients who are executing your API.
    See also: AWS API Documentation
    
    
    :example: response = client.create_api_key(
        apiId='string',
        description='string',
        expires=123
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The ID for your GraphQL API.
            

    :type description: string
    :param description: A description of the purpose of the API key.

    :type expires: integer
    :param expires: The time from creation time after which the API key expires. The date is represented as seconds since the epoch, rounded down to the nearest hour. The default value for this parameter is 7 days from creation time. For more information, see .

    :rtype: dict
    :return: {
        'apiKey': {
            'id': 'string',
            'description': 'string',
            'expires': 123
        }
    }
    
    
    """
    pass

def create_data_source(apiId=None, name=None, description=None, type=None, serviceRoleArn=None, dynamodbConfig=None, lambdaConfig=None, elasticsearchConfig=None, httpConfig=None, relationalDatabaseConfig=None):
    """
    Creates a DataSource object.
    See also: AWS API Documentation
    
    
    :example: response = client.create_data_source(
        apiId='string',
        name='string',
        description='string',
        type='AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE'|'HTTP'|'RELATIONAL_DATABASE',
        serviceRoleArn='string',
        dynamodbConfig={
            'tableName': 'string',
            'awsRegion': 'string',
            'useCallerCredentials': True|False
        },
        lambdaConfig={
            'lambdaFunctionArn': 'string'
        },
        elasticsearchConfig={
            'endpoint': 'string',
            'awsRegion': 'string'
        },
        httpConfig={
            'endpoint': 'string',
            'authorizationConfig': {
                'authorizationType': 'AWS_IAM',
                'awsIamConfig': {
                    'signingRegion': 'string',
                    'signingServiceName': 'string'
                }
            }
        },
        relationalDatabaseConfig={
            'relationalDatabaseSourceType': 'RDS_HTTP_ENDPOINT',
            'rdsHttpEndpointConfig': {
                'awsRegion': 'string',
                'dbClusterIdentifier': 'string',
                'databaseName': 'string',
                'schema': 'string',
                'awsSecretStoreArn': 'string'
            }
        }
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID for the GraphQL API for the DataSource .
            

    :type name: string
    :param name: [REQUIRED]
            A user-supplied name for the DataSource .
            

    :type description: string
    :param description: A description of the DataSource .

    :type type: string
    :param type: [REQUIRED]
            The type of the DataSource .
            

    :type serviceRoleArn: string
    :param serviceRoleArn: The AWS IAM service role ARN for the data source. The system assumes this role when accessing the data source.

    :type dynamodbConfig: dict
    :param dynamodbConfig: Amazon DynamoDB settings.
            tableName (string) -- [REQUIRED]The table name.
            awsRegion (string) -- [REQUIRED]The AWS Region.
            useCallerCredentials (boolean) --Set to TRUE to use Amazon Cognito credentials with this data source.
            

    :type lambdaConfig: dict
    :param lambdaConfig: AWS Lambda settings.
            lambdaFunctionArn (string) -- [REQUIRED]The ARN for the Lambda function.
            

    :type elasticsearchConfig: dict
    :param elasticsearchConfig: Amazon Elasticsearch Service settings.
            endpoint (string) -- [REQUIRED]The endpoint.
            awsRegion (string) -- [REQUIRED]The AWS Region.
            

    :type httpConfig: dict
    :param httpConfig: HTTP endpoint settings.
            endpoint (string) --The HTTP URL endpoint. You can either specify the domain name or IP, and port combination, and the URL scheme must be HTTP or HTTPS. If the port is not specified, AWS AppSync uses the default port 80 for the HTTP endpoint and port 443 for HTTPS endpoints.
            authorizationConfig (dict) --The authorization config in case the HTTP endpoint requires authorization.
            authorizationType (string) -- [REQUIRED]The authorization type required by the HTTP endpoint.
            AWS_IAM : The authorization type is Sigv4.
            awsIamConfig (dict) --The AWS IAM settings.
            signingRegion (string) --The signing region for AWS IAM authorization.
            signingServiceName (string) --The signing service name for AWS IAM authorization.
            
            

    :type relationalDatabaseConfig: dict
    :param relationalDatabaseConfig: Relational database settings.
            relationalDatabaseSourceType (string) --Source type for the relational database.
            RDS_HTTP_ENDPOINT : The relational database source type is an Amazon RDS HTTP endpoint.
            rdsHttpEndpointConfig (dict) --Amazon RDS HTTP endpoint settings.
            awsRegion (string) --AWS Region for RDS HTTP endpoint.
            dbClusterIdentifier (string) --Amazon RDS cluster identifier.
            databaseName (string) --Logical database name.
            schema (string) --Logical schema name.
            awsSecretStoreArn (string) --AWS secret store ARN for database credentials.
            
            

    :rtype: dict
    :return: {
        'dataSource': {
            'dataSourceArn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE'|'HTTP'|'RELATIONAL_DATABASE',
            'serviceRoleArn': 'string',
            'dynamodbConfig': {
                'tableName': 'string',
                'awsRegion': 'string',
                'useCallerCredentials': True|False
            },
            'lambdaConfig': {
                'lambdaFunctionArn': 'string'
            },
            'elasticsearchConfig': {
                'endpoint': 'string',
                'awsRegion': 'string'
            },
            'httpConfig': {
                'endpoint': 'string',
                'authorizationConfig': {
                    'authorizationType': 'AWS_IAM',
                    'awsIamConfig': {
                        'signingRegion': 'string',
                        'signingServiceName': 'string'
                    }
                }
            },
            'relationalDatabaseConfig': {
                'relationalDatabaseSourceType': 'RDS_HTTP_ENDPOINT',
                'rdsHttpEndpointConfig': {
                    'awsRegion': 'string',
                    'dbClusterIdentifier': 'string',
                    'databaseName': 'string',
                    'schema': 'string',
                    'awsSecretStoreArn': 'string'
                }
            }
        }
    }
    
    
    :returns: 
    AMAZON_DYNAMODB : The data source is an Amazon DynamoDB table.
    AMAZON_ELASTICSEARCH : The data source is an Amazon Elasticsearch Service domain.
    AWS_LAMBDA : The data source is an AWS Lambda function.
    NONE : There is no data source. This type is used when you wish to invoke a GraphQL operation without connecting to a data source, such as performing data transformation with resolvers or triggering a subscription to be invoked from a mutation.
    HTTP : The data source is an HTTP endpoint.
    RELATIONAL_DATABASE : The data source is a relational database.
    
    """
    pass

def create_function(apiId=None, name=None, description=None, dataSourceName=None, requestMappingTemplate=None, responseMappingTemplate=None, functionVersion=None):
    """
    Creates a Function object.
    A function is a reusable entity. Multiple functions can be used to compose the resolver logic.
    See also: AWS API Documentation
    
    
    :example: response = client.create_function(
        apiId='string',
        name='string',
        description='string',
        dataSourceName='string',
        requestMappingTemplate='string',
        responseMappingTemplate='string',
        functionVersion='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The GraphQL API ID.
            

    :type name: string
    :param name: [REQUIRED]
            The Function name. The function name does not have to be unique.
            

    :type description: string
    :param description: The Function description.

    :type dataSourceName: string
    :param dataSourceName: [REQUIRED]
            The Function DataSource name.
            

    :type requestMappingTemplate: string
    :param requestMappingTemplate: [REQUIRED]
            The Function request mapping template. Functions support only the 2018-05-29 version of the request mapping template.
            

    :type responseMappingTemplate: string
    :param responseMappingTemplate: The Function response mapping template.

    :type functionVersion: string
    :param functionVersion: [REQUIRED]
            The version of the request mapping template. Currently the supported value is 2018-05-29.
            

    :rtype: dict
    :return: {
        'functionConfiguration': {
            'functionId': 'string',
            'functionArn': 'string',
            'name': 'string',
            'description': 'string',
            'dataSourceName': 'string',
            'requestMappingTemplate': 'string',
            'responseMappingTemplate': 'string',
            'functionVersion': 'string'
        }
    }
    
    
    """
    pass

def create_graphql_api(name=None, logConfig=None, authenticationType=None, userPoolConfig=None, openIDConnectConfig=None):
    """
    Creates a GraphqlApi object.
    See also: AWS API Documentation
    
    
    :example: response = client.create_graphql_api(
        name='string',
        logConfig={
            'fieldLogLevel': 'NONE'|'ERROR'|'ALL',
            'cloudWatchLogsRoleArn': 'string'
        },
        authenticationType='API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
        userPoolConfig={
            'userPoolId': 'string',
            'awsRegion': 'string',
            'defaultAction': 'ALLOW'|'DENY',
            'appIdClientRegex': 'string'
        },
        openIDConnectConfig={
            'issuer': 'string',
            'clientId': 'string',
            'iatTTL': 123,
            'authTTL': 123
        }
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            A user-supplied name for the GraphqlApi .
            

    :type logConfig: dict
    :param logConfig: The Amazon CloudWatch Logs configuration.
            fieldLogLevel (string) -- [REQUIRED]The field logging level. Values can be NONE, ERROR, or ALL.
            NONE : No field-level logs are captured.
            ERROR : Logs the following information only for the fields that are in error:
            The error section in the server response.
            Field-level errors.
            The generated request/response functions that got resolved for error fields.
            ALL : The following information is logged for all fields in the query:
            Field-level tracing information.
            The generated request/response functions that got resolved for each field.
            
            cloudWatchLogsRoleArn (string) -- [REQUIRED]The service role that AWS AppSync will assume to publish to Amazon CloudWatch logs in your account.
            

    :type authenticationType: string
    :param authenticationType: [REQUIRED]
            The authentication type: API key, AWS IAM, or Amazon Cognito user pools.
            

    :type userPoolConfig: dict
    :param userPoolConfig: The Amazon Cognito user pool configuration.
            userPoolId (string) -- [REQUIRED]The user pool ID.
            awsRegion (string) -- [REQUIRED]The AWS Region in which the user pool was created.
            defaultAction (string) -- [REQUIRED]The action that you want your GraphQL API to take when a request that uses Amazon Cognito user pool authentication doesn't match the Amazon Cognito user pool configuration.
            appIdClientRegex (string) --A regular expression for validating the incoming Amazon Cognito user pool app client ID.
            

    :type openIDConnectConfig: dict
    :param openIDConnectConfig: The OpenID Connect configuration.
            issuer (string) -- [REQUIRED]The issuer for the OpenID Connect configuration. The issuer returned by discovery must exactly match the value of iss in the ID token.
            clientId (string) --The client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.
            iatTTL (integer) --The number of milliseconds a token is valid after being issued to a user.
            authTTL (integer) --The number of milliseconds a token is valid after being authenticated.
            

    :rtype: dict
    :return: {
        'graphqlApi': {
            'name': 'string',
            'apiId': 'string',
            'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
            'logConfig': {
                'fieldLogLevel': 'NONE'|'ERROR'|'ALL',
                'cloudWatchLogsRoleArn': 'string'
            },
            'userPoolConfig': {
                'userPoolId': 'string',
                'awsRegion': 'string',
                'defaultAction': 'ALLOW'|'DENY',
                'appIdClientRegex': 'string'
            },
            'openIDConnectConfig': {
                'issuer': 'string',
                'clientId': 'string',
                'iatTTL': 123,
                'authTTL': 123
            },
            'arn': 'string',
            'uris': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    NONE : No field-level logs are captured.
    ERROR : Logs the following information only for the fields that are in error:
    The error section in the server response.
    Field-level errors.
    The generated request/response functions that got resolved for error fields.
    
    
    ALL : The following information is logged for all fields in the query:
    Field-level tracing information.
    The generated request/response functions that got resolved for each field.
    
    
    
    """
    pass

def create_resolver(apiId=None, typeName=None, fieldName=None, dataSourceName=None, requestMappingTemplate=None, responseMappingTemplate=None, kind=None, pipelineConfig=None):
    """
    Creates a Resolver object.
    A resolver converts incoming requests into a format that a data source can understand and converts the data source's responses into GraphQL.
    See also: AWS API Documentation
    
    
    :example: response = client.create_resolver(
        apiId='string',
        typeName='string',
        fieldName='string',
        dataSourceName='string',
        requestMappingTemplate='string',
        responseMappingTemplate='string',
        kind='UNIT'|'PIPELINE',
        pipelineConfig={
            'functions': [
                'string',
            ]
        }
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The ID for the GraphQL API for which the resolver is being created.
            

    :type typeName: string
    :param typeName: [REQUIRED]
            The name of the Type .
            

    :type fieldName: string
    :param fieldName: [REQUIRED]
            The name of the field to attach the resolver to.
            

    :type dataSourceName: string
    :param dataSourceName: The name of the data source for which the resolver is being created.

    :type requestMappingTemplate: string
    :param requestMappingTemplate: [REQUIRED]
            The mapping template to be used for requests.
            A resolver uses a request mapping template to convert a GraphQL expression into a format that a data source can understand. Mapping templates are written in Apache Velocity Template Language (VTL).
            

    :type responseMappingTemplate: string
    :param responseMappingTemplate: The mapping template to be used for responses from the data source.

    :type kind: string
    :param kind: The resolver type.
            UNIT : A UNIT resolver type. A UNIT resolver is the default resolver type. A UNIT resolver enables you to execute a GraphQL query against a single data source.
            PIPELINE : A PIPELINE resolver type. A PIPELINE resolver enables you to execute a series of Function in a serial manner. You can use a pipeline resolver to execute a GraphQL query against multiple data sources.
            

    :type pipelineConfig: dict
    :param pipelineConfig: The PipelineConfig .
            functions (list) --A list of Function objects.
            (string) --
            

    :rtype: dict
    :return: {
        'resolver': {
            'typeName': 'string',
            'fieldName': 'string',
            'dataSourceName': 'string',
            'resolverArn': 'string',
            'requestMappingTemplate': 'string',
            'responseMappingTemplate': 'string',
            'kind': 'UNIT'|'PIPELINE',
            'pipelineConfig': {
                'functions': [
                    'string',
                ]
            }
        }
    }
    
    
    :returns: 
    UNIT : A UNIT resolver type. A UNIT resolver is the default resolver type. A UNIT resolver enables you to execute a GraphQL query against a single data source.
    PIPELINE : A PIPELINE resolver type. A PIPELINE resolver enables you to execute a series of Function in a serial manner. You can use a pipeline resolver to execute a GraphQL query against multiple data sources.
    
    """
    pass

def create_type(apiId=None, definition=None, format=None):
    """
    Creates a Type object.
    See also: AWS API Documentation
    
    
    :example: response = client.create_type(
        apiId='string',
        definition='string',
        format='SDL'|'JSON'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type definition: string
    :param definition: [REQUIRED]
            The type definition, in GraphQL Schema Definition Language (SDL) format.
            For more information, see the GraphQL SDL documentation .
            

    :type format: string
    :param format: [REQUIRED]
            The type format: SDL or JSON.
            

    :rtype: dict
    :return: {
        'type': {
            'name': 'string',
            'description': 'string',
            'arn': 'string',
            'definition': 'string',
            'format': 'SDL'|'JSON'
        }
    }
    
    
    """
    pass

def delete_api_key(apiId=None, id=None):
    """
    Deletes an API key.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_api_key(
        apiId='string',
        id='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type id: string
    :param id: [REQUIRED]
            The ID for the API key.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_data_source(apiId=None, name=None):
    """
    Deletes a DataSource object.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_data_source(
        apiId='string',
        name='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type name: string
    :param name: [REQUIRED]
            The name of the data source.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_function(apiId=None, functionId=None):
    """
    Deletes a Function .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_function(
        apiId='string',
        functionId='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The GraphQL API ID.
            

    :type functionId: string
    :param functionId: [REQUIRED]
            The Function ID.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_graphql_api(apiId=None):
    """
    Deletes a GraphqlApi object.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_graphql_api(
        apiId='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_resolver(apiId=None, typeName=None, fieldName=None):
    """
    Deletes a Resolver object.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_resolver(
        apiId='string',
        typeName='string',
        fieldName='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type typeName: string
    :param typeName: [REQUIRED]
            The name of the resolver type.
            

    :type fieldName: string
    :param fieldName: [REQUIRED]
            The resolver field name.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_type(apiId=None, typeName=None):
    """
    Deletes a Type object.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_type(
        apiId='string',
        typeName='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type typeName: string
    :param typeName: [REQUIRED]
            The type name.
            

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

def get_data_source(apiId=None, name=None):
    """
    Retrieves a DataSource object.
    See also: AWS API Documentation
    
    
    :example: response = client.get_data_source(
        apiId='string',
        name='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type name: string
    :param name: [REQUIRED]
            The name of the data source.
            

    :rtype: dict
    :return: {
        'dataSource': {
            'dataSourceArn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE'|'HTTP'|'RELATIONAL_DATABASE',
            'serviceRoleArn': 'string',
            'dynamodbConfig': {
                'tableName': 'string',
                'awsRegion': 'string',
                'useCallerCredentials': True|False
            },
            'lambdaConfig': {
                'lambdaFunctionArn': 'string'
            },
            'elasticsearchConfig': {
                'endpoint': 'string',
                'awsRegion': 'string'
            },
            'httpConfig': {
                'endpoint': 'string',
                'authorizationConfig': {
                    'authorizationType': 'AWS_IAM',
                    'awsIamConfig': {
                        'signingRegion': 'string',
                        'signingServiceName': 'string'
                    }
                }
            },
            'relationalDatabaseConfig': {
                'relationalDatabaseSourceType': 'RDS_HTTP_ENDPOINT',
                'rdsHttpEndpointConfig': {
                    'awsRegion': 'string',
                    'dbClusterIdentifier': 'string',
                    'databaseName': 'string',
                    'schema': 'string',
                    'awsSecretStoreArn': 'string'
                }
            }
        }
    }
    
    
    :returns: 
    AMAZON_DYNAMODB : The data source is an Amazon DynamoDB table.
    AMAZON_ELASTICSEARCH : The data source is an Amazon Elasticsearch Service domain.
    AWS_LAMBDA : The data source is an AWS Lambda function.
    NONE : There is no data source. This type is used when you wish to invoke a GraphQL operation without connecting to a data source, such as performing data transformation with resolvers or triggering a subscription to be invoked from a mutation.
    HTTP : The data source is an HTTP endpoint.
    RELATIONAL_DATABASE : The data source is a relational database.
    
    """
    pass

def get_function(apiId=None, functionId=None):
    """
    Get a Function .
    See also: AWS API Documentation
    
    
    :example: response = client.get_function(
        apiId='string',
        functionId='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The GraphQL API ID.
            

    :type functionId: string
    :param functionId: [REQUIRED]
            The Function ID.
            

    :rtype: dict
    :return: {
        'functionConfiguration': {
            'functionId': 'string',
            'functionArn': 'string',
            'name': 'string',
            'description': 'string',
            'dataSourceName': 'string',
            'requestMappingTemplate': 'string',
            'responseMappingTemplate': 'string',
            'functionVersion': 'string'
        }
    }
    
    
    """
    pass

def get_graphql_api(apiId=None):
    """
    Retrieves a GraphqlApi object.
    See also: AWS API Documentation
    
    
    :example: response = client.get_graphql_api(
        apiId='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID for the GraphQL API.
            

    :rtype: dict
    :return: {
        'graphqlApi': {
            'name': 'string',
            'apiId': 'string',
            'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
            'logConfig': {
                'fieldLogLevel': 'NONE'|'ERROR'|'ALL',
                'cloudWatchLogsRoleArn': 'string'
            },
            'userPoolConfig': {
                'userPoolId': 'string',
                'awsRegion': 'string',
                'defaultAction': 'ALLOW'|'DENY',
                'appIdClientRegex': 'string'
            },
            'openIDConnectConfig': {
                'issuer': 'string',
                'clientId': 'string',
                'iatTTL': 123,
                'authTTL': 123
            },
            'arn': 'string',
            'uris': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_introspection_schema(apiId=None, format=None):
    """
    Retrieves the introspection schema for a GraphQL API.
    See also: AWS API Documentation
    
    
    :example: response = client.get_introspection_schema(
        apiId='string',
        format='SDL'|'JSON'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type format: string
    :param format: [REQUIRED]
            The schema format: SDL or JSON.
            

    :rtype: dict
    :return: {
        'schema': StreamingBody()
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

def get_resolver(apiId=None, typeName=None, fieldName=None):
    """
    Retrieves a Resolver object.
    See also: AWS API Documentation
    
    
    :example: response = client.get_resolver(
        apiId='string',
        typeName='string',
        fieldName='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type typeName: string
    :param typeName: [REQUIRED]
            The resolver type name.
            

    :type fieldName: string
    :param fieldName: [REQUIRED]
            The resolver field name.
            

    :rtype: dict
    :return: {
        'resolver': {
            'typeName': 'string',
            'fieldName': 'string',
            'dataSourceName': 'string',
            'resolverArn': 'string',
            'requestMappingTemplate': 'string',
            'responseMappingTemplate': 'string',
            'kind': 'UNIT'|'PIPELINE',
            'pipelineConfig': {
                'functions': [
                    'string',
                ]
            }
        }
    }
    
    
    :returns: 
    UNIT : A UNIT resolver type. A UNIT resolver is the default resolver type. A UNIT resolver enables you to execute a GraphQL query against a single data source.
    PIPELINE : A PIPELINE resolver type. A PIPELINE resolver enables you to execute a series of Function in a serial manner. You can use a pipeline resolver to execute a GraphQL query against multiple data sources.
    
    """
    pass

def get_schema_creation_status(apiId=None):
    """
    Retrieves the current status of a schema creation operation.
    See also: AWS API Documentation
    
    
    :example: response = client.get_schema_creation_status(
        apiId='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :rtype: dict
    :return: {
        'status': 'PROCESSING'|'ACTIVE'|'DELETING',
        'details': 'string'
    }
    
    
    """
    pass

def get_type(apiId=None, typeName=None, format=None):
    """
    Retrieves a Type object.
    See also: AWS API Documentation
    
    
    :example: response = client.get_type(
        apiId='string',
        typeName='string',
        format='SDL'|'JSON'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type typeName: string
    :param typeName: [REQUIRED]
            The type name.
            

    :type format: string
    :param format: [REQUIRED]
            The type format: SDL or JSON.
            

    :rtype: dict
    :return: {
        'type': {
            'name': 'string',
            'description': 'string',
            'arn': 'string',
            'definition': 'string',
            'format': 'SDL'|'JSON'
        }
    }
    
    
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

def list_api_keys(apiId=None, nextToken=None, maxResults=None):
    """
    Lists the API keys for a given API.
    See also: AWS API Documentation
    
    
    :example: response = client.list_api_keys(
        apiId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :type maxResults: integer
    :param maxResults: The maximum number of results you want the request to return.

    :rtype: dict
    :return: {
        'apiKeys': [
            {
                'id': 'string',
                'description': 'string',
                'expires': 123
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    ListApiKeys returns the expiration time in milliseconds.
    CreateApiKey returns the expiration time in milliseconds.
    UpdateApiKey is not available for this key version.
    DeleteApiKey deletes the item from the table.
    Expiration is stored in Amazon DynamoDB as milliseconds. This results in a bug where keys are not automatically deleted because DynamoDB expects the TTL to be stored in seconds. As a one-time action, we will delete these keys from the table after February 21, 2018.
    
    """
    pass

def list_data_sources(apiId=None, nextToken=None, maxResults=None):
    """
    Lists the data sources for a given API.
    See also: AWS API Documentation
    
    
    :example: response = client.list_data_sources(
        apiId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :type maxResults: integer
    :param maxResults: The maximum number of results you want the request to return.

    :rtype: dict
    :return: {
        'dataSources': [
            {
                'dataSourceArn': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE'|'HTTP'|'RELATIONAL_DATABASE',
                'serviceRoleArn': 'string',
                'dynamodbConfig': {
                    'tableName': 'string',
                    'awsRegion': 'string',
                    'useCallerCredentials': True|False
                },
                'lambdaConfig': {
                    'lambdaFunctionArn': 'string'
                },
                'elasticsearchConfig': {
                    'endpoint': 'string',
                    'awsRegion': 'string'
                },
                'httpConfig': {
                    'endpoint': 'string',
                    'authorizationConfig': {
                        'authorizationType': 'AWS_IAM',
                        'awsIamConfig': {
                            'signingRegion': 'string',
                            'signingServiceName': 'string'
                        }
                    }
                },
                'relationalDatabaseConfig': {
                    'relationalDatabaseSourceType': 'RDS_HTTP_ENDPOINT',
                    'rdsHttpEndpointConfig': {
                        'awsRegion': 'string',
                        'dbClusterIdentifier': 'string',
                        'databaseName': 'string',
                        'schema': 'string',
                        'awsSecretStoreArn': 'string'
                    }
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    AMAZON_DYNAMODB : The data source is an Amazon DynamoDB table.
    AMAZON_ELASTICSEARCH : The data source is an Amazon Elasticsearch Service domain.
    AWS_LAMBDA : The data source is an AWS Lambda function.
    NONE : There is no data source. This type is used when you wish to invoke a GraphQL operation without connecting to a data source, such as performing data transformation with resolvers or triggering a subscription to be invoked from a mutation.
    HTTP : The data source is an HTTP endpoint.
    RELATIONAL_DATABASE : The data source is a relational database.
    
    """
    pass

def list_functions(apiId=None, nextToken=None, maxResults=None):
    """
    List multiple functions.
    See also: AWS API Documentation
    
    
    :example: response = client.list_functions(
        apiId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The GraphQL API ID.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :type maxResults: integer
    :param maxResults: The maximum number of results you want the request to return.

    :rtype: dict
    :return: {
        'functions': [
            {
                'functionId': 'string',
                'functionArn': 'string',
                'name': 'string',
                'description': 'string',
                'dataSourceName': 'string',
                'requestMappingTemplate': 'string',
                'responseMappingTemplate': 'string',
                'functionVersion': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_graphql_apis(nextToken=None, maxResults=None):
    """
    Lists your GraphQL APIs.
    See also: AWS API Documentation
    
    
    :example: response = client.list_graphql_apis(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :type maxResults: integer
    :param maxResults: The maximum number of results you want the request to return.

    :rtype: dict
    :return: {
        'graphqlApis': [
            {
                'name': 'string',
                'apiId': 'string',
                'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
                'logConfig': {
                    'fieldLogLevel': 'NONE'|'ERROR'|'ALL',
                    'cloudWatchLogsRoleArn': 'string'
                },
                'userPoolConfig': {
                    'userPoolId': 'string',
                    'awsRegion': 'string',
                    'defaultAction': 'ALLOW'|'DENY',
                    'appIdClientRegex': 'string'
                },
                'openIDConnectConfig': {
                    'issuer': 'string',
                    'clientId': 'string',
                    'iatTTL': 123,
                    'authTTL': 123
                },
                'arn': 'string',
                'uris': {
                    'string': 'string'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    NONE : No field-level logs are captured.
    ERROR : Logs the following information only for the fields that are in error:
    The error section in the server response.
    Field-level errors.
    The generated request/response functions that got resolved for error fields.
    
    
    ALL : The following information is logged for all fields in the query:
    Field-level tracing information.
    The generated request/response functions that got resolved for each field.
    
    
    
    """
    pass

def list_resolvers(apiId=None, typeName=None, nextToken=None, maxResults=None):
    """
    Lists the resolvers for a given API and type.
    See also: AWS API Documentation
    
    
    :example: response = client.list_resolvers(
        apiId='string',
        typeName='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type typeName: string
    :param typeName: [REQUIRED]
            The type name.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :type maxResults: integer
    :param maxResults: The maximum number of results you want the request to return.

    :rtype: dict
    :return: {
        'resolvers': [
            {
                'typeName': 'string',
                'fieldName': 'string',
                'dataSourceName': 'string',
                'resolverArn': 'string',
                'requestMappingTemplate': 'string',
                'responseMappingTemplate': 'string',
                'kind': 'UNIT'|'PIPELINE',
                'pipelineConfig': {
                    'functions': [
                        'string',
                    ]
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    UNIT : A UNIT resolver type. A UNIT resolver is the default resolver type. A UNIT resolver enables you to execute a GraphQL query against a single data source.
    PIPELINE : A PIPELINE resolver type. A PIPELINE resolver enables you to execute a series of Function in a serial manner. You can use a pipeline resolver to execute a GraphQL query against multiple data sources.
    
    """
    pass

def list_resolvers_by_function(apiId=None, functionId=None, nextToken=None, maxResults=None):
    """
    List the resolvers that are associated with a specific function.
    See also: AWS API Documentation
    
    
    :example: response = client.list_resolvers_by_function(
        apiId='string',
        functionId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type functionId: string
    :param functionId: [REQUIRED]
            The Function ID.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.

    :type maxResults: integer
    :param maxResults: The maximum number of results you want the request to return.

    :rtype: dict
    :return: {
        'resolvers': [
            {
                'typeName': 'string',
                'fieldName': 'string',
                'dataSourceName': 'string',
                'resolverArn': 'string',
                'requestMappingTemplate': 'string',
                'responseMappingTemplate': 'string',
                'kind': 'UNIT'|'PIPELINE',
                'pipelineConfig': {
                    'functions': [
                        'string',
                    ]
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    UNIT : A UNIT resolver type. A UNIT resolver is the default resolver type. A UNIT resolver enables you to execute a GraphQL query against a single data source.
    PIPELINE : A PIPELINE resolver type. A PIPELINE resolver enables you to execute a series of Function in a serial manner. You can use a pipeline resolver to execute a GraphQL query against multiple data sources.
    
    """
    pass

def list_types(apiId=None, format=None, nextToken=None, maxResults=None):
    """
    Lists the types for a given API.
    See also: AWS API Documentation
    
    
    :example: response = client.list_types(
        apiId='string',
        format='SDL'|'JSON',
        nextToken='string',
        maxResults=123
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type format: string
    :param format: [REQUIRED]
            The type format: SDL or JSON.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :type maxResults: integer
    :param maxResults: The maximum number of results you want the request to return.

    :rtype: dict
    :return: {
        'types': [
            {
                'name': 'string',
                'description': 'string',
                'arn': 'string',
                'definition': 'string',
                'format': 'SDL'|'JSON'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def start_schema_creation(apiId=None, definition=None):
    """
    Adds a new schema to your GraphQL API.
    This operation is asynchronous. Use to determine when it has completed.
    See also: AWS API Documentation
    
    
    :example: response = client.start_schema_creation(
        apiId='string',
        definition=b'bytes'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type definition: bytes
    :param definition: [REQUIRED]
            The schema definition, in GraphQL schema language format.
            

    :rtype: dict
    :return: {
        'status': 'PROCESSING'|'ACTIVE'|'DELETING'
    }
    
    
    """
    pass

def update_api_key(apiId=None, id=None, description=None, expires=None):
    """
    Updates an API key.
    See also: AWS API Documentation
    
    
    :example: response = client.update_api_key(
        apiId='string',
        id='string',
        description='string',
        expires=123
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The ID for the GraphQL API.
            

    :type id: string
    :param id: [REQUIRED]
            The API key ID.
            

    :type description: string
    :param description: A description of the purpose of the API key.

    :type expires: integer
    :param expires: The time from update time after which the API key expires. The date is represented as seconds since the epoch. For more information, see .

    :rtype: dict
    :return: {
        'apiKey': {
            'id': 'string',
            'description': 'string',
            'expires': 123
        }
    }
    
    
    """
    pass

def update_data_source(apiId=None, name=None, description=None, type=None, serviceRoleArn=None, dynamodbConfig=None, lambdaConfig=None, elasticsearchConfig=None, httpConfig=None, relationalDatabaseConfig=None):
    """
    Updates a DataSource object.
    See also: AWS API Documentation
    
    
    :example: response = client.update_data_source(
        apiId='string',
        name='string',
        description='string',
        type='AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE'|'HTTP'|'RELATIONAL_DATABASE',
        serviceRoleArn='string',
        dynamodbConfig={
            'tableName': 'string',
            'awsRegion': 'string',
            'useCallerCredentials': True|False
        },
        lambdaConfig={
            'lambdaFunctionArn': 'string'
        },
        elasticsearchConfig={
            'endpoint': 'string',
            'awsRegion': 'string'
        },
        httpConfig={
            'endpoint': 'string',
            'authorizationConfig': {
                'authorizationType': 'AWS_IAM',
                'awsIamConfig': {
                    'signingRegion': 'string',
                    'signingServiceName': 'string'
                }
            }
        },
        relationalDatabaseConfig={
            'relationalDatabaseSourceType': 'RDS_HTTP_ENDPOINT',
            'rdsHttpEndpointConfig': {
                'awsRegion': 'string',
                'dbClusterIdentifier': 'string',
                'databaseName': 'string',
                'schema': 'string',
                'awsSecretStoreArn': 'string'
            }
        }
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type name: string
    :param name: [REQUIRED]
            The new name for the data source.
            

    :type description: string
    :param description: The new description for the data source.

    :type type: string
    :param type: [REQUIRED]
            The new data source type.
            

    :type serviceRoleArn: string
    :param serviceRoleArn: The new service role ARN for the data source.

    :type dynamodbConfig: dict
    :param dynamodbConfig: The new Amazon DynamoDB configuration.
            tableName (string) -- [REQUIRED]The table name.
            awsRegion (string) -- [REQUIRED]The AWS Region.
            useCallerCredentials (boolean) --Set to TRUE to use Amazon Cognito credentials with this data source.
            

    :type lambdaConfig: dict
    :param lambdaConfig: The new AWS Lambda configuration.
            lambdaFunctionArn (string) -- [REQUIRED]The ARN for the Lambda function.
            

    :type elasticsearchConfig: dict
    :param elasticsearchConfig: The new Elasticsearch Service configuration.
            endpoint (string) -- [REQUIRED]The endpoint.
            awsRegion (string) -- [REQUIRED]The AWS Region.
            

    :type httpConfig: dict
    :param httpConfig: The new HTTP endpoint configuration.
            endpoint (string) --The HTTP URL endpoint. You can either specify the domain name or IP, and port combination, and the URL scheme must be HTTP or HTTPS. If the port is not specified, AWS AppSync uses the default port 80 for the HTTP endpoint and port 443 for HTTPS endpoints.
            authorizationConfig (dict) --The authorization config in case the HTTP endpoint requires authorization.
            authorizationType (string) -- [REQUIRED]The authorization type required by the HTTP endpoint.
            AWS_IAM : The authorization type is Sigv4.
            awsIamConfig (dict) --The AWS IAM settings.
            signingRegion (string) --The signing region for AWS IAM authorization.
            signingServiceName (string) --The signing service name for AWS IAM authorization.
            
            

    :type relationalDatabaseConfig: dict
    :param relationalDatabaseConfig: The new relational database configuration.
            relationalDatabaseSourceType (string) --Source type for the relational database.
            RDS_HTTP_ENDPOINT : The relational database source type is an Amazon RDS HTTP endpoint.
            rdsHttpEndpointConfig (dict) --Amazon RDS HTTP endpoint settings.
            awsRegion (string) --AWS Region for RDS HTTP endpoint.
            dbClusterIdentifier (string) --Amazon RDS cluster identifier.
            databaseName (string) --Logical database name.
            schema (string) --Logical schema name.
            awsSecretStoreArn (string) --AWS secret store ARN for database credentials.
            
            

    :rtype: dict
    :return: {
        'dataSource': {
            'dataSourceArn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE'|'HTTP'|'RELATIONAL_DATABASE',
            'serviceRoleArn': 'string',
            'dynamodbConfig': {
                'tableName': 'string',
                'awsRegion': 'string',
                'useCallerCredentials': True|False
            },
            'lambdaConfig': {
                'lambdaFunctionArn': 'string'
            },
            'elasticsearchConfig': {
                'endpoint': 'string',
                'awsRegion': 'string'
            },
            'httpConfig': {
                'endpoint': 'string',
                'authorizationConfig': {
                    'authorizationType': 'AWS_IAM',
                    'awsIamConfig': {
                        'signingRegion': 'string',
                        'signingServiceName': 'string'
                    }
                }
            },
            'relationalDatabaseConfig': {
                'relationalDatabaseSourceType': 'RDS_HTTP_ENDPOINT',
                'rdsHttpEndpointConfig': {
                    'awsRegion': 'string',
                    'dbClusterIdentifier': 'string',
                    'databaseName': 'string',
                    'schema': 'string',
                    'awsSecretStoreArn': 'string'
                }
            }
        }
    }
    
    
    :returns: 
    AMAZON_DYNAMODB : The data source is an Amazon DynamoDB table.
    AMAZON_ELASTICSEARCH : The data source is an Amazon Elasticsearch Service domain.
    AWS_LAMBDA : The data source is an AWS Lambda function.
    NONE : There is no data source. This type is used when you wish to invoke a GraphQL operation without connecting to a data source, such as performing data transformation with resolvers or triggering a subscription to be invoked from a mutation.
    HTTP : The data source is an HTTP endpoint.
    RELATIONAL_DATABASE : The data source is a relational database.
    
    """
    pass

def update_function(apiId=None, name=None, description=None, functionId=None, dataSourceName=None, requestMappingTemplate=None, responseMappingTemplate=None, functionVersion=None):
    """
    Updates a Function object.
    See also: AWS API Documentation
    
    
    :example: response = client.update_function(
        apiId='string',
        name='string',
        description='string',
        functionId='string',
        dataSourceName='string',
        requestMappingTemplate='string',
        responseMappingTemplate='string',
        functionVersion='string'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The GraphQL API ID.
            

    :type name: string
    :param name: [REQUIRED]
            The Function name.
            

    :type description: string
    :param description: The Function description.

    :type functionId: string
    :param functionId: [REQUIRED]
            The function ID.
            

    :type dataSourceName: string
    :param dataSourceName: [REQUIRED]
            The Function DataSource name.
            

    :type requestMappingTemplate: string
    :param requestMappingTemplate: [REQUIRED]
            The Function request mapping template. Functions support only the 2018-05-29 version of the request mapping template.
            

    :type responseMappingTemplate: string
    :param responseMappingTemplate: The Function request mapping template.

    :type functionVersion: string
    :param functionVersion: [REQUIRED]
            The version of the request mapping template. Currently the supported value is 2018-05-29.
            

    :rtype: dict
    :return: {
        'functionConfiguration': {
            'functionId': 'string',
            'functionArn': 'string',
            'name': 'string',
            'description': 'string',
            'dataSourceName': 'string',
            'requestMappingTemplate': 'string',
            'responseMappingTemplate': 'string',
            'functionVersion': 'string'
        }
    }
    
    
    """
    pass

def update_graphql_api(apiId=None, name=None, logConfig=None, authenticationType=None, userPoolConfig=None, openIDConnectConfig=None):
    """
    Updates a GraphqlApi object.
    See also: AWS API Documentation
    
    
    :example: response = client.update_graphql_api(
        apiId='string',
        name='string',
        logConfig={
            'fieldLogLevel': 'NONE'|'ERROR'|'ALL',
            'cloudWatchLogsRoleArn': 'string'
        },
        authenticationType='API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
        userPoolConfig={
            'userPoolId': 'string',
            'awsRegion': 'string',
            'defaultAction': 'ALLOW'|'DENY',
            'appIdClientRegex': 'string'
        },
        openIDConnectConfig={
            'issuer': 'string',
            'clientId': 'string',
            'iatTTL': 123,
            'authTTL': 123
        }
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type name: string
    :param name: [REQUIRED]
            The new name for the GraphqlApi object.
            

    :type logConfig: dict
    :param logConfig: The Amazon CloudWatch Logs configuration for the GraphqlApi object.
            fieldLogLevel (string) -- [REQUIRED]The field logging level. Values can be NONE, ERROR, or ALL.
            NONE : No field-level logs are captured.
            ERROR : Logs the following information only for the fields that are in error:
            The error section in the server response.
            Field-level errors.
            The generated request/response functions that got resolved for error fields.
            ALL : The following information is logged for all fields in the query:
            Field-level tracing information.
            The generated request/response functions that got resolved for each field.
            
            cloudWatchLogsRoleArn (string) -- [REQUIRED]The service role that AWS AppSync will assume to publish to Amazon CloudWatch logs in your account.
            

    :type authenticationType: string
    :param authenticationType: The new authentication type for the GraphqlApi object.

    :type userPoolConfig: dict
    :param userPoolConfig: The new Amazon Cognito user pool configuration for the GraphqlApi object.
            userPoolId (string) -- [REQUIRED]The user pool ID.
            awsRegion (string) -- [REQUIRED]The AWS Region in which the user pool was created.
            defaultAction (string) -- [REQUIRED]The action that you want your GraphQL API to take when a request that uses Amazon Cognito user pool authentication doesn't match the Amazon Cognito user pool configuration.
            appIdClientRegex (string) --A regular expression for validating the incoming Amazon Cognito user pool app client ID.
            

    :type openIDConnectConfig: dict
    :param openIDConnectConfig: The OpenID Connect configuration for the GraphqlApi object.
            issuer (string) -- [REQUIRED]The issuer for the OpenID Connect configuration. The issuer returned by discovery must exactly match the value of iss in the ID token.
            clientId (string) --The client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.
            iatTTL (integer) --The number of milliseconds a token is valid after being issued to a user.
            authTTL (integer) --The number of milliseconds a token is valid after being authenticated.
            

    :rtype: dict
    :return: {
        'graphqlApi': {
            'name': 'string',
            'apiId': 'string',
            'authenticationType': 'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'|'OPENID_CONNECT',
            'logConfig': {
                'fieldLogLevel': 'NONE'|'ERROR'|'ALL',
                'cloudWatchLogsRoleArn': 'string'
            },
            'userPoolConfig': {
                'userPoolId': 'string',
                'awsRegion': 'string',
                'defaultAction': 'ALLOW'|'DENY',
                'appIdClientRegex': 'string'
            },
            'openIDConnectConfig': {
                'issuer': 'string',
                'clientId': 'string',
                'iatTTL': 123,
                'authTTL': 123
            },
            'arn': 'string',
            'uris': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    NONE : No field-level logs are captured.
    ERROR : Logs the following information only for the fields that are in error:
    The error section in the server response.
    Field-level errors.
    The generated request/response functions that got resolved for error fields.
    
    
    ALL : The following information is logged for all fields in the query:
    Field-level tracing information.
    The generated request/response functions that got resolved for each field.
    
    
    
    """
    pass

def update_resolver(apiId=None, typeName=None, fieldName=None, dataSourceName=None, requestMappingTemplate=None, responseMappingTemplate=None, kind=None, pipelineConfig=None):
    """
    Updates a Resolver object.
    See also: AWS API Documentation
    
    
    :example: response = client.update_resolver(
        apiId='string',
        typeName='string',
        fieldName='string',
        dataSourceName='string',
        requestMappingTemplate='string',
        responseMappingTemplate='string',
        kind='UNIT'|'PIPELINE',
        pipelineConfig={
            'functions': [
                'string',
            ]
        }
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type typeName: string
    :param typeName: [REQUIRED]
            The new type name.
            

    :type fieldName: string
    :param fieldName: [REQUIRED]
            The new field name.
            

    :type dataSourceName: string
    :param dataSourceName: The new data source name.

    :type requestMappingTemplate: string
    :param requestMappingTemplate: [REQUIRED]
            The new request mapping template.
            

    :type responseMappingTemplate: string
    :param responseMappingTemplate: The new response mapping template.

    :type kind: string
    :param kind: The resolver type.
            UNIT : A UNIT resolver type. A UNIT resolver is the default resolver type. A UNIT resolver enables you to execute a GraphQL query against a single data source.
            PIPELINE : A PIPELINE resolver type. A PIPELINE resolver enables you to execute a series of Function in a serial manner. You can use a pipeline resolver to execute a GraphQL query against multiple data sources.
            

    :type pipelineConfig: dict
    :param pipelineConfig: The PipelineConfig .
            functions (list) --A list of Function objects.
            (string) --
            

    :rtype: dict
    :return: {
        'resolver': {
            'typeName': 'string',
            'fieldName': 'string',
            'dataSourceName': 'string',
            'resolverArn': 'string',
            'requestMappingTemplate': 'string',
            'responseMappingTemplate': 'string',
            'kind': 'UNIT'|'PIPELINE',
            'pipelineConfig': {
                'functions': [
                    'string',
                ]
            }
        }
    }
    
    
    :returns: 
    UNIT : A UNIT resolver type. A UNIT resolver is the default resolver type. A UNIT resolver enables you to execute a GraphQL query against a single data source.
    PIPELINE : A PIPELINE resolver type. A PIPELINE resolver enables you to execute a series of Function in a serial manner. You can use a pipeline resolver to execute a GraphQL query against multiple data sources.
    
    """
    pass

def update_type(apiId=None, typeName=None, definition=None, format=None):
    """
    Updates a Type object.
    See also: AWS API Documentation
    
    
    :example: response = client.update_type(
        apiId='string',
        typeName='string',
        definition='string',
        format='SDL'|'JSON'
    )
    
    
    :type apiId: string
    :param apiId: [REQUIRED]
            The API ID.
            

    :type typeName: string
    :param typeName: [REQUIRED]
            The new type name.
            

    :type definition: string
    :param definition: The new definition.

    :type format: string
    :param format: [REQUIRED]
            The new type format: SDL or JSON.
            

    :rtype: dict
    :return: {
        'type': {
            'name': 'string',
            'description': 'string',
            'arn': 'string',
            'definition': 'string',
            'format': 'SDL'|'JSON'
        }
    }
    
    
    """
    pass

