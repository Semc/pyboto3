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

def execute_sql(awsSecretStoreArn=None, database=None, dbClusterOrInstanceArn=None, schema=None, sqlStatements=None):
    """
    Executes any SQL statement on the target database synchronously
    See also: AWS API Documentation
    
    
    :example: response = client.execute_sql(
        awsSecretStoreArn='string',
        database='string',
        dbClusterOrInstanceArn='string',
        schema='string',
        sqlStatements='string'
    )
    
    
    :type awsSecretStoreArn: string
    :param awsSecretStoreArn: [REQUIRED] ARN of the db credentials in AWS Secret Store or the friendly secret name

    :type database: string
    :param database: Target DB name

    :type dbClusterOrInstanceArn: string
    :param dbClusterOrInstanceArn: [REQUIRED] ARN of the target db cluster or instance

    :type schema: string
    :param schema: Target Schema name

    :type sqlStatements: string
    :param sqlStatements: [REQUIRED] SQL statement(s) to be executed. Statements can be chained by using semicolons

    :rtype: dict
    :return: {
        'sqlStatementResults': [
            {
                'numberOfRecordsUpdated': 123,
                'resultFrame': {
                    'records': [
                        {
                            'values': [
                                {
                                    'arrayValues': [
                                        {'... recursive ...'},
                                    ],
                                    'bigIntValue': 123,
                                    'bitValue': True|False,
                                    'blobValue': b'bytes',
                                    'doubleValue': 123.0,
                                    'intValue': 123,
                                    'isNull': True|False,
                                    'realValue': ...,
                                    'stringValue': 'string',
                                    'structValue': {
                                        'attributes': [
                                            {'... recursive ...'},
                                        ]
                                    }
                                },
                            ]
                        },
                    ],
                    'resultSetMetadata': {
                        'columnCount': 123,
                        'columnMetadata': [
                            {
                                'arrayBaseColumnType': 123,
                                'isAutoIncrement': True|False,
                                'isCaseSensitive': True|False,
                                'isCurrency': True|False,
                                'isSigned': True|False,
                                'label': 'string',
                                'name': 'string',
                                'nullable': 123,
                                'precision': 123,
                                'scale': 123,
                                'schemaName': 'string',
                                'tableName': 'string',
                                'type': 123,
                                'typeName': 'string'
                            },
                        ]
                    }
                }
            },
        ]
    }
    
    
    :returns: 
    (dict) -- Execute SQL response
    sqlStatementResults (list) -- Results returned by executing the sql statement(s)
    (dict) -- SQL statement execution result
    numberOfRecordsUpdated (integer) -- Number of rows updated.
    resultFrame (dict) -- ResultFrame returned by executing the sql statement
    records (list) -- ResultSet Metadata.
    (dict) -- Row or Record
    values (list) -- Record
    (dict) -- Column value
    arrayValues (list) -- Arbitrarily nested arrays
    (dict) -- Column value
    
    
    bigIntValue (integer) -- Long value
    bitValue (boolean) -- Bit value
    blobValue (bytes) -- Blob value
    doubleValue (float) -- Double value
    intValue (integer) -- Integer value
    isNull (boolean) -- Is column null
    realValue (float) -- Float value
    stringValue (string) -- String value
    structValue (dict) -- Struct or UDT
    attributes (list) -- Struct or UDT
    (dict) -- Column value
    
    
    
    
    
    
    
    
    
    
    
    
    resultSetMetadata (dict) -- ResultSet Metadata.
    columnCount (integer) -- Number of columns
    columnMetadata (list) -- List of columns and their types
    (dict) -- Column Metadata
    arrayBaseColumnType (integer) -- Homogenous array base SQL type from java.sql.Types.
    isAutoIncrement (boolean) -- Whether the designated column is automatically numbered
    isCaseSensitive (boolean) -- Whether values in the designated column's case matters
    isCurrency (boolean) -- Whether values in the designated column is a cash value
    isSigned (boolean) -- Whether values in the designated column are signed numbers
    label (string) -- Usually specified by the SQL AS. If not specified, return column name.
    name (string) -- Name of the column.
    nullable (integer) -- Indicates the nullability of values in the designated column. One of columnNoNulls (0), columnNullable (1), columnNullableUnknown (2)
    precision (integer) -- Get the designated column's specified column size.For numeric data, this is the maximum precision. For character data, this is the length in characters. For datetime datatypes, this is the length in characters of the String representation (assuming the maximum allowed precision of the fractional seconds component). For binary data, this is the length in bytes. For the ROWID datatype, this is the length in bytes. 0 is returned for data types where the column size is not applicable.
    scale (integer) -- Designated column's number of digits to right of the decimal point. 0 is returned for data types where the scale is not applicable.
    schemaName (string) -- Designated column's table's schema
    tableName (string) -- Designated column's table name
    type (integer) -- SQL type from java.sql.Types.
    typeName (string) -- Database-specific type name.
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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

