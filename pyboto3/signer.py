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

def cancel_signing_profile(profileName=None):
    """
    Changes the state of an ACTIVE signing profile to CANCELED . A canceled profile is still viewable with the ListSigningProfiles operation, but it cannot perform new signing jobs, and is deleted two years after cancelation.
    See also: AWS API Documentation
    
    
    :example: response = client.cancel_signing_profile(
        profileName='string'
    )
    
    
    :type profileName: string
    :param profileName: [REQUIRED]
            The name of the signing profile to be canceled.
            

    """
    pass

def describe_signing_job(jobId=None):
    """
    Returns information about a specific code signing job. You specify the job by using the jobId value that is returned by the  StartSigningJob operation.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_signing_job(
        jobId='string'
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]
            The ID of the signing job on input.
            

    :rtype: dict
    :return: {
        'jobId': 'string',
        'source': {
            's3': {
                'bucketName': 'string',
                'key': 'string',
                'version': 'string'
            }
        },
        'signingMaterial': {
            'certificateArn': 'string'
        },
        'platformId': 'string',
        'profileName': 'string',
        'overrides': {
            'signingConfiguration': {
                'encryptionAlgorithm': 'RSA'|'ECDSA',
                'hashAlgorithm': 'SHA1'|'SHA256'
            }
        },
        'signingParameters': {
            'string': 'string'
        },
        'createdAt': datetime(2015, 1, 1),
        'completedAt': datetime(2015, 1, 1),
        'requestedBy': 'string',
        'status': 'InProgress'|'Failed'|'Succeeded',
        'statusReason': 'string',
        'signedObject': {
            's3': {
                'bucketName': 'string',
                'key': 'string'
            }
        }
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

def get_signing_platform(platformId=None):
    """
    Returns information on a specific signing platform.
    See also: AWS API Documentation
    
    
    :example: response = client.get_signing_platform(
        platformId='string'
    )
    
    
    :type platformId: string
    :param platformId: [REQUIRED]
            The ID of the target signing platform.
            

    :rtype: dict
    :return: {
        'platformId': 'string',
        'displayName': 'string',
        'partner': 'string',
        'target': 'string',
        'category': 'AWSIoT',
        'signingConfiguration': {
            'encryptionAlgorithmOptions': {
                'allowedValues': [
                    'RSA'|'ECDSA',
                ],
                'defaultValue': 'RSA'|'ECDSA'
            },
            'hashAlgorithmOptions': {
                'allowedValues': [
                    'SHA1'|'SHA256',
                ],
                'defaultValue': 'SHA1'|'SHA256'
            }
        },
        'signingImageFormat': {
            'supportedFormats': [
                'JSON',
            ],
            'defaultFormat': 'JSON'
        },
        'maxSizeInMB': 123
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_signing_profile(profileName=None):
    """
    Returns information on a specific signing profile.
    See also: AWS API Documentation
    
    
    :example: response = client.get_signing_profile(
        profileName='string'
    )
    
    
    :type profileName: string
    :param profileName: [REQUIRED]
            The name of the target signing profile.
            

    :rtype: dict
    :return: {
        'profileName': 'string',
        'signingMaterial': {
            'certificateArn': 'string'
        },
        'platformId': 'string',
        'overrides': {
            'signingConfiguration': {
                'encryptionAlgorithm': 'RSA'|'ECDSA',
                'hashAlgorithm': 'SHA1'|'SHA256'
            }
        },
        'signingParameters': {
            'string': 'string'
        },
        'status': 'Active'|'Canceled'
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

def list_signing_jobs(status=None, platformId=None, requestedBy=None, maxResults=None, nextToken=None):
    """
    Lists all your signing jobs. You can use the maxResults parameter to limit the number of signing jobs that are returned in the response. If additional jobs remain to be listed, AWS Signer returns a nextToken value. Use this value in subsequent calls to ListSigningJobs to fetch the remaining values. You can continue calling ListSigningJobs with your maxResults parameter and with new values that AWS Signer returns in the nextToken parameter until all of your signing jobs have been returned.
    See also: AWS API Documentation
    
    
    :example: response = client.list_signing_jobs(
        status='InProgress'|'Failed'|'Succeeded',
        platformId='string',
        requestedBy='string',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type status: string
    :param status: A status value with which to filter your results.

    :type platformId: string
    :param platformId: The ID of microcontroller platform that you specified for the distribution of your code image.

    :type requestedBy: string
    :param requestedBy: The IAM principal that requested the signing job.

    :type maxResults: integer
    :param maxResults: Specifies the maximum number of items to return in the response. Use this parameter when paginating results. If additional items exist beyond the number you specify, the nextToken element is set in the response. Use the nextToken value in a subsequent request to retrieve additional items.

    :type nextToken: string
    :param nextToken: String for specifying the next set of paginated results to return. After you receive a response with truncated results, use this parameter in a subsequent request. Set it to the value of nextToken from the response that you just received.

    :rtype: dict
    :return: {
        'jobs': [
            {
                'jobId': 'string',
                'source': {
                    's3': {
                        'bucketName': 'string',
                        'key': 'string',
                        'version': 'string'
                    }
                },
                'signedObject': {
                    's3': {
                        'bucketName': 'string',
                        'key': 'string'
                    }
                },
                'signingMaterial': {
                    'certificateArn': 'string'
                },
                'createdAt': datetime(2015, 1, 1),
                'status': 'InProgress'|'Failed'|'Succeeded'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_signing_platforms(category=None, partner=None, target=None, maxResults=None, nextToken=None):
    """
    Lists all signing platforms available in AWS Signer that match the request parameters. If additional jobs remain to be listed, AWS Signer returns a nextToken value. Use this value in subsequent calls to ListSigningJobs to fetch the remaining values. You can continue calling ListSigningJobs with your maxResults parameter and with new values that AWS Signer returns in the nextToken parameter until all of your signing jobs have been returned.
    See also: AWS API Documentation
    
    
    :example: response = client.list_signing_platforms(
        category='string',
        partner='string',
        target='string',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type category: string
    :param category: The category type of a signing platform.

    :type partner: string
    :param partner: Any partner entities connected to a signing platform.

    :type target: string
    :param target: The validation template that is used by the target signing platform.

    :type maxResults: integer
    :param maxResults: The maximum number of results to be returned by this operation.

    :type nextToken: string
    :param nextToken: Value for specifying the next set of paginated results to return. After you receive a response with truncated results, use this parameter in a subsequent request. Set it to the value of nextToken from the response that you just received.

    :rtype: dict
    :return: {
        'platforms': [
            {
                'platformId': 'string',
                'displayName': 'string',
                'partner': 'string',
                'target': 'string',
                'category': 'AWSIoT',
                'signingConfiguration': {
                    'encryptionAlgorithmOptions': {
                        'allowedValues': [
                            'RSA'|'ECDSA',
                        ],
                        'defaultValue': 'RSA'|'ECDSA'
                    },
                    'hashAlgorithmOptions': {
                        'allowedValues': [
                            'SHA1'|'SHA256',
                        ],
                        'defaultValue': 'SHA1'|'SHA256'
                    }
                },
                'signingImageFormat': {
                    'supportedFormats': [
                        'JSON',
                    ],
                    'defaultFormat': 'JSON'
                },
                'maxSizeInMB': 123
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_signing_profiles(includeCanceled=None, maxResults=None, nextToken=None):
    """
    Lists all available signing profiles in your AWS account. Returns only profiles with an ACTIVE status unless the includeCanceled request field is set to true . If additional jobs remain to be listed, AWS Signer returns a nextToken value. Use this value in subsequent calls to ListSigningJobs to fetch the remaining values. You can continue calling ListSigningJobs with your maxResults parameter and with new values that AWS Signer returns in the nextToken parameter until all of your signing jobs have been returned.
    See also: AWS API Documentation
    
    
    :example: response = client.list_signing_profiles(
        includeCanceled=True|False,
        maxResults=123,
        nextToken='string'
    )
    
    
    :type includeCanceled: boolean
    :param includeCanceled: Designates whether to include profiles with the status of CANCELED .

    :type maxResults: integer
    :param maxResults: The maximum number of profiles to be returned.

    :type nextToken: string
    :param nextToken: Value for specifying the next set of paginated results to return. After you receive a response with truncated results, use this parameter in a subsequent request. Set it to the value of nextToken from the response that you just received.

    :rtype: dict
    :return: {
        'profiles': [
            {
                'profileName': 'string',
                'signingMaterial': {
                    'certificateArn': 'string'
                },
                'platformId': 'string',
                'signingParameters': {
                    'string': 'string'
                },
                'status': 'Active'|'Canceled'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def put_signing_profile(profileName=None, signingMaterial=None, platformId=None, overrides=None, signingParameters=None):
    """
    Creates a signing profile. A signing profile is an AWS Signer template that can be used to carry out a pre-defined signing job. For more information, see http://docs.aws.amazon.com/signer/latest/developerguide/gs-profile.html
    See also: AWS API Documentation
    
    
    :example: response = client.put_signing_profile(
        profileName='string',
        signingMaterial={
            'certificateArn': 'string'
        },
        platformId='string',
        overrides={
            'signingConfiguration': {
                'encryptionAlgorithm': 'RSA'|'ECDSA',
                'hashAlgorithm': 'SHA1'|'SHA256'
            }
        },
        signingParameters={
            'string': 'string'
        }
    )
    
    
    :type profileName: string
    :param profileName: [REQUIRED]
            The name of the signing profile to be created.
            

    :type signingMaterial: dict
    :param signingMaterial: [REQUIRED]
            The AWS Certificate Manager certificate that will be used to sign code with the new signing profile.
            certificateArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the certificates that is used to sign your code.
            

    :type platformId: string
    :param platformId: [REQUIRED]
            The ID of the signing profile to be created.
            

    :type overrides: dict
    :param overrides: A subfield of platform . This specifies any different configuration options that you want to apply to the chosen platform (such as a different hash-algorithm or signing-algorithm ).
            signingConfiguration (dict) --A signing configuration that overrides the default encryption or hash algorithm of a signing job.
            encryptionAlgorithm (string) --A specified override of the default encryption algorithm that is used in an AWS Signer job.
            hashAlgorithm (string) --A specified override of the default hash algorithm that is used in an AWS Signer job.
            
            

    :type signingParameters: dict
    :param signingParameters: Map of key-value pairs for signing. These can include any information that you want to use during signing.
            (string) --
            (string) --
            

    :rtype: dict
    :return: {
        'arn': 'string'
    }
    
    
    """
    pass

def start_signing_job(source=None, destination=None, profileName=None, clientRequestToken=None):
    """
    Initiates a signing job to be performed on the code provided. Signing jobs are viewable by the ListSigningJobs operation for two years after they are performed. Note the following requirements:
    You can call the  DescribeSigningJob and the  ListSigningJobs actions after you call StartSigningJob .
    For a Java example that shows how to use this action, see http://docs.aws.amazon.com/acm/latest/userguide/
    See also: AWS API Documentation
    
    
    :example: response = client.start_signing_job(
        source={
            's3': {
                'bucketName': 'string',
                'key': 'string',
                'version': 'string'
            }
        },
        destination={
            's3': {
                'bucketName': 'string',
                'prefix': 'string'
            }
        },
        profileName='string',
        clientRequestToken='string'
    )
    
    
    :type source: dict
    :param source: [REQUIRED]
            The S3 bucket that contains the object to sign or a BLOB that contains your raw code.
            s3 (dict) --The S3Source object.
            bucketName (string) -- [REQUIRED]Name of the S3 bucket.
            key (string) -- [REQUIRED]Key name of the bucket object that contains your unsigned code.
            version (string) -- [REQUIRED]Version of your source image in your version enabled S3 bucket.
            
            

    :type destination: dict
    :param destination: [REQUIRED]
            The S3 bucket in which to save your signed object. The destination contains the name of your bucket and an optional prefix.
            s3 (dict) --The S3Destination object.
            bucketName (string) --Name of the S3 bucket.
            prefix (string) --An Amazon S3 prefix that you can use to limit responses to those that begin with the specified prefix.
            
            

    :type profileName: string
    :param profileName: The name of the signing profile.

    :type clientRequestToken: string
    :param clientRequestToken: [REQUIRED]
            String that identifies the signing request. All calls after the first that use this token return the same response as the first call.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'jobId': 'string'
    }
    
    
    :returns: 
    source (dict) -- [REQUIRED]
    The S3 bucket that contains the object to sign or a BLOB that contains your raw code.
    
    s3 (dict) --The S3Source object.
    
    bucketName (string) -- [REQUIRED]Name of the S3 bucket.
    
    key (string) -- [REQUIRED]Key name of the bucket object that contains your unsigned code.
    
    version (string) -- [REQUIRED]Version of your source image in your version enabled S3 bucket.
    
    
    
    
    
    destination (dict) -- [REQUIRED]
    The S3 bucket in which to save your signed object. The destination contains the name of your bucket and an optional prefix.
    
    s3 (dict) --The S3Destination object.
    
    bucketName (string) --Name of the S3 bucket.
    
    prefix (string) --An Amazon S3 prefix that you can use to limit responses to those that begin with the specified prefix.
    
    
    
    
    
    profileName (string) -- The name of the signing profile.
    clientRequestToken (string) -- [REQUIRED]
    String that identifies the signing request. All calls after the first that use this token return the same response as the first call.
    This field is autopopulated if not provided.
    
    
    """
    pass

