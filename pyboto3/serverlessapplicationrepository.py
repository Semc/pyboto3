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

def create_application(Author=None, Description=None, HomePageUrl=None, Labels=None, LicenseBody=None, LicenseUrl=None, Name=None, ReadmeBody=None, ReadmeUrl=None, SemanticVersion=None, SourceCodeUrl=None, SpdxLicenseId=None, TemplateBody=None, TemplateUrl=None):
    """
    Creates an application, optionally including an AWS SAM file to create the first application version in the same call.
    See also: AWS API Documentation
    
    
    :example: response = client.create_application(
        Author='string',
        Description='string',
        HomePageUrl='string',
        Labels=[
            'string',
        ],
        LicenseBody='string',
        LicenseUrl='string',
        Name='string',
        ReadmeBody='string',
        ReadmeUrl='string',
        SemanticVersion='string',
        SourceCodeUrl='string',
        SpdxLicenseId='string',
        TemplateBody='string',
        TemplateUrl='string'
    )
    
    
    :type Author: string
    :param Author: [REQUIRED]
            The name of the author publishing the app.
            Minimum length=1. Maximum length=127.
            Pattern '^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$';
            

    :type Description: string
    :param Description: [REQUIRED]
            The description of the application.
            Minimum length=1. Maximum length=256
            

    :type HomePageUrl: string
    :param HomePageUrl: A URL with more information about the application, for example the location of your GitHub repository for the application.

    :type Labels: list
    :param Labels: Labels to improve discovery of apps in search results.
            Minimum length=1. Maximum length=127. Maximum number of labels: 10
            Pattern: '^[a-zA-Z0-9+\-_:\/@]+$';
            (string) --
            

    :type LicenseBody: string
    :param LicenseBody: A local text file that contains the license of the app that matches the spdxLicenseID value of your application. The file has the format file://<path>/<filename>.
            Maximum size 5 MB
            You can specify only one of licenseBody and licenseUrl; otherwise, an error results.
            

    :type LicenseUrl: string
    :param LicenseUrl: A link to the S3 object that contains the license of the app that matches the spdxLicenseID value of your application.
            Maximum size 5 MB
            You can specify only one of licenseBody and licenseUrl; otherwise, an error results.
            

    :type Name: string
    :param Name: [REQUIRED]
            The name of the application that you want to publish.
            Minimum length=1. Maximum length=140
            Pattern: '[a-zA-Z0-9\-]+';
            

    :type ReadmeBody: string
    :param ReadmeBody: A local text readme file in Markdown language that contains a more detailed description of the application and how it works. The file has the format file://<path>/<filename>.
            Maximum size 5 MB
            You can specify only one of readmeBody and readmeUrl; otherwise, an error results.
            

    :type ReadmeUrl: string
    :param ReadmeUrl: A link to the S3 object in Markdown language that contains a more detailed description of the application and how it works.
            Maximum size 5 MB
            You can specify only one of readmeBody and readmeUrl; otherwise, an error results.
            

    :type SemanticVersion: string
    :param SemanticVersion: The semantic version of the application:
            https://semver.org/
            

    :type SourceCodeUrl: string
    :param SourceCodeUrl: A link to a public repository for the source code of your application.

    :type SpdxLicenseId: string
    :param SpdxLicenseId: A valid identifier from https://spdx.org/licenses/ .

    :type TemplateBody: string
    :param TemplateBody: The local raw packaged AWS SAM template file of your application. The file has the format file://<path>/<filename>.
            You can specify only one of templateBody and templateUrl; otherwise an error results.
            

    :type TemplateUrl: string
    :param TemplateUrl: A link to the S3 object containing the packaged AWS SAM template of your application.
            You can specify only one of templateBody and templateUrl; otherwise an error results.
            

    :rtype: dict
    :return: {
        'ApplicationId': 'string',
        'Author': 'string',
        'CreationTime': 'string',
        'Description': 'string',
        'HomePageUrl': 'string',
        'Labels': [
            'string',
        ],
        'LicenseUrl': 'string',
        'Name': 'string',
        'ReadmeUrl': 'string',
        'SpdxLicenseId': 'string',
        'Version': {
            'ApplicationId': 'string',
            'CreationTime': 'string',
            'ParameterDefinitions': [
                {
                    'AllowedPattern': 'string',
                    'AllowedValues': [
                        'string',
                    ],
                    'ConstraintDescription': 'string',
                    'DefaultValue': 'string',
                    'Description': 'string',
                    'MaxLength': 123,
                    'MaxValue': 123,
                    'MinLength': 123,
                    'MinValue': 123,
                    'Name': 'string',
                    'NoEcho': True|False,
                    'ReferencedByResources': [
                        'string',
                    ],
                    'Type': 'string'
                },
            ],
            'RequiredCapabilities': [
                'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND'|'CAPABILITY_RESOURCE_POLICY',
            ],
            'ResourcesSupported': True|False,
            'SemanticVersion': 'string',
            'SourceCodeUrl': 'string',
            'TemplateUrl': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_application_version(ApplicationId=None, SemanticVersion=None, SourceCodeUrl=None, TemplateBody=None, TemplateUrl=None):
    """
    Creates an application version.
    See also: AWS API Documentation
    
    
    :example: response = client.create_application_version(
        ApplicationId='string',
        SemanticVersion='string',
        SourceCodeUrl='string',
        TemplateBody='string',
        TemplateUrl='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]
            The Amazon Resource Name (ARN) of the application.
            

    :type SemanticVersion: string
    :param SemanticVersion: [REQUIRED]
            The semantic version of the new version.
            

    :type SourceCodeUrl: string
    :param SourceCodeUrl: A link to a public repository for the source code of your application.

    :type TemplateBody: string
    :param TemplateBody: The raw packaged AWS SAM template of your application.

    :type TemplateUrl: string
    :param TemplateUrl: A link to the packaged AWS SAM template of your application.

    :rtype: dict
    :return: {
        'ApplicationId': 'string',
        'CreationTime': 'string',
        'ParameterDefinitions': [
            {
                'AllowedPattern': 'string',
                'AllowedValues': [
                    'string',
                ],
                'ConstraintDescription': 'string',
                'DefaultValue': 'string',
                'Description': 'string',
                'MaxLength': 123,
                'MaxValue': 123,
                'MinLength': 123,
                'MinValue': 123,
                'Name': 'string',
                'NoEcho': True|False,
                'ReferencedByResources': [
                    'string',
                ],
                'Type': 'string'
            },
        ],
        'RequiredCapabilities': [
            'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND'|'CAPABILITY_RESOURCE_POLICY',
        ],
        'ResourcesSupported': True|False,
        'SemanticVersion': 'string',
        'SourceCodeUrl': 'string',
        'TemplateUrl': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_cloud_formation_change_set(ApplicationId=None, Capabilities=None, ChangeSetName=None, ClientToken=None, Description=None, NotificationArns=None, ParameterOverrides=None, ResourceTypes=None, RollbackConfiguration=None, SemanticVersion=None, StackName=None, Tags=None, TemplateId=None):
    """
    Creates an AWS CloudFormation change set for the given application.
    See also: AWS API Documentation
    
    
    :example: response = client.create_cloud_formation_change_set(
        ApplicationId='string',
        Capabilities=[
            'string',
        ],
        ChangeSetName='string',
        ClientToken='string',
        Description='string',
        NotificationArns=[
            'string',
        ],
        ParameterOverrides=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ],
        ResourceTypes=[
            'string',
        ],
        RollbackConfiguration={
            'MonitoringTimeInMinutes': 123,
            'RollbackTriggers': [
                {
                    'Arn': 'string',
                    'Type': 'string'
                },
            ]
        },
        SemanticVersion='string',
        StackName='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        TemplateId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]
            The Amazon Resource Name (ARN) of the application.
            

    :type Capabilities: list
    :param Capabilities: A list of values that you must specify before you can deploy certain applications. Some applications might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those applications, you must explicitly acknowledge their capabilities by specifying this parameter.
            The only valid values are CAPABILITY_IAM, CAPABILITY_NAMED_IAM, and CAPABILITY_RESOURCE_POLICY.
            The following resources require you to specify CAPABILITY_IAM or CAPABILITY_NAMED_IAM: AWS::IAM::Group , AWS::IAM::InstanceProfile , AWS::IAM::Policy , and AWS::IAM::Role . If the application contains IAM resources, you can specify either CAPABILITY_IAM or CAPABILITY_NAMED_IAM. If the application contains IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM.
            The following resources require you to specify CAPABILITY_RESOURCE_POLICY: AWS::Lambda::Permission , AWS::IAM:Policy , AWS::ApplicationAutoScaling::ScalingPolicy , AWS::S3::BucketPolicy , AWS::SQS::QueuePolicy , and AWS::SNS:TopicPolicy .
            If your application template contains any of the above resources, we recommend that you review all permissions associated with the application before deploying. If you don't specify this parameter for an application that requires capabilities, the call will fail.
            Valid values: CAPABILITY_IAM | CAPABILITY_NAMED_IAM | CAPABILITY_RESOURCE_POLICY
            (string) --
            

    :type ChangeSetName: string
    :param ChangeSetName: This property corresponds to the parameter of the same name for the AWS CloudFormation `CreateChangeSet <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet>`__ API.

    :type ClientToken: string
    :param ClientToken: This property corresponds to the parameter of the same name for the AWS CloudFormation `CreateChangeSet <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet>`__ API.

    :type Description: string
    :param Description: This property corresponds to the parameter of the same name for the AWS CloudFormation `CreateChangeSet <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet>`__ API.

    :type NotificationArns: list
    :param NotificationArns: This property corresponds to the parameter of the same name for the AWS CloudFormation `CreateChangeSet <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet>`__ API.
            (string) --
            

    :type ParameterOverrides: list
    :param ParameterOverrides: A list of parameter values for the parameters of the application.
            (dict) --Parameter value of the application.
            Name (string) -- [REQUIRED]The key associated with the parameter. If you don't specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.
            Value (string) -- [REQUIRED]The input value associated with the parameter.
            
            

    :type ResourceTypes: list
    :param ResourceTypes: This property corresponds to the parameter of the same name for the AWS CloudFormation `CreateChangeSet <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet>`__ API.
            (string) --
            

    :type RollbackConfiguration: dict
    :param RollbackConfiguration: This property corresponds to the parameter of the same name for the AWS CloudFormation `CreateChangeSet <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet>`__ API.
            MonitoringTimeInMinutes (integer) --This property corresponds to the content of the same name for the AWS CloudFormation `RollbackConfiguration <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackConfiguration>`__ Data Type.
            RollbackTriggers (list) --This property corresponds to the content of the same name for the AWS CloudFormation `RollbackConfiguration <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackConfiguration>`__ Data Type.
            (dict) --This property corresponds to the AWS CloudFormation `RollbackTrigger <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackTrigger>`__ Data Type.
            Arn (string) -- [REQUIRED]This property corresponds to the content of the same name for the AWS CloudFormation `RollbackTrigger <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackTrigger>`__ Data Type.
            Type (string) -- [REQUIRED]This property corresponds to the content of the same name for the AWS CloudFormation `RollbackTrigger <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackTrigger>`__ Data Type.
            
            

    :type SemanticVersion: string
    :param SemanticVersion: The semantic version of the application:
            https://semver.org/
            

    :type StackName: string
    :param StackName: [REQUIRED]
            This property corresponds to the parameter of the same name for the AWS CloudFormation `CreateChangeSet <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet>`__ API.
            

    :type Tags: list
    :param Tags: This property corresponds to the parameter of the same name for the AWS CloudFormation `CreateChangeSet <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet>`__ API.
            (dict) --This property corresponds to the AWS CloudFormation `Tag <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/Tag>`__ Data Type.
            Key (string) -- [REQUIRED]This property corresponds to the content of the same name for the AWS CloudFormation `Tag <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/Tag>`__ Data Type.
            Value (string) -- [REQUIRED]This property corresponds to the content of the same name for the *AWS CloudFormation Tag * Data Type.
            
            

    :type TemplateId: string
    :param TemplateId: The UUID returned by CreateCloudFormationTemplate.
            Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}
            

    :rtype: dict
    :return: {
        'ApplicationId': 'string',
        'ChangeSetId': 'string',
        'SemanticVersion': 'string',
        'StackId': 'string'
    }
    
    
    """
    pass

def create_cloud_formation_template(ApplicationId=None, SemanticVersion=None):
    """
    Creates an AWS CloudFormation template.
    See also: AWS API Documentation
    
    
    :example: response = client.create_cloud_formation_template(
        ApplicationId='string',
        SemanticVersion='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]
            The Amazon Resource Name (ARN) of the application.
            

    :type SemanticVersion: string
    :param SemanticVersion: The semantic version of the application:
            https://semver.org/
            

    :rtype: dict
    :return: {
        'ApplicationId': 'string',
        'CreationTime': 'string',
        'ExpirationTime': 'string',
        'SemanticVersion': 'string',
        'Status': 'PREPARING'|'ACTIVE'|'EXPIRED',
        'TemplateId': 'string',
        'TemplateUrl': 'string'
    }
    
    
    """
    pass

def delete_application(ApplicationId=None):
    """
    Deletes the specified application.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_application(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]
            The Amazon Resource Name (ARN) of the application.
            

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

def get_application(ApplicationId=None, SemanticVersion=None):
    """
    Gets the specified application.
    See also: AWS API Documentation
    
    
    :example: response = client.get_application(
        ApplicationId='string',
        SemanticVersion='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]
            The Amazon Resource Name (ARN) of the application.
            

    :type SemanticVersion: string
    :param SemanticVersion: The semantic version of the application to get.

    :rtype: dict
    :return: {
        'ApplicationId': 'string',
        'Author': 'string',
        'CreationTime': 'string',
        'Description': 'string',
        'HomePageUrl': 'string',
        'Labels': [
            'string',
        ],
        'LicenseUrl': 'string',
        'Name': 'string',
        'ReadmeUrl': 'string',
        'SpdxLicenseId': 'string',
        'Version': {
            'ApplicationId': 'string',
            'CreationTime': 'string',
            'ParameterDefinitions': [
                {
                    'AllowedPattern': 'string',
                    'AllowedValues': [
                        'string',
                    ],
                    'ConstraintDescription': 'string',
                    'DefaultValue': 'string',
                    'Description': 'string',
                    'MaxLength': 123,
                    'MaxValue': 123,
                    'MinLength': 123,
                    'MinValue': 123,
                    'Name': 'string',
                    'NoEcho': True|False,
                    'ReferencedByResources': [
                        'string',
                    ],
                    'Type': 'string'
                },
            ],
            'RequiredCapabilities': [
                'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND'|'CAPABILITY_RESOURCE_POLICY',
            ],
            'ResourcesSupported': True|False,
            'SemanticVersion': 'string',
            'SourceCodeUrl': 'string',
            'TemplateUrl': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_application_policy(ApplicationId=None):
    """
    Retrieves the policy for the application.
    See also: AWS API Documentation
    
    
    :example: response = client.get_application_policy(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]
            The Amazon Resource Name (ARN) of the application.
            

    :rtype: dict
    :return: {
        'Statements': [
            {
                'Actions': [
                    'string',
                ],
                'Principals': [
                    'string',
                ],
                'StatementId': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_cloud_formation_template(ApplicationId=None, TemplateId=None):
    """
    Gets the specified AWS CloudFormation template.
    See also: AWS API Documentation
    
    
    :example: response = client.get_cloud_formation_template(
        ApplicationId='string',
        TemplateId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]
            The Amazon Resource Name (ARN) of the application.
            

    :type TemplateId: string
    :param TemplateId: [REQUIRED]
            The UUID returned by CreateCloudFormationTemplate.
            Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}
            

    :rtype: dict
    :return: {
        'ApplicationId': 'string',
        'CreationTime': 'string',
        'ExpirationTime': 'string',
        'SemanticVersion': 'string',
        'Status': 'PREPARING'|'ACTIVE'|'EXPIRED',
        'TemplateId': 'string',
        'TemplateUrl': 'string'
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

def list_application_dependencies(ApplicationId=None, MaxItems=None, NextToken=None, SemanticVersion=None):
    """
    Retrieves the list of applications nested in the containing application.
    See also: AWS API Documentation
    
    
    :example: response = client.list_application_dependencies(
        ApplicationId='string',
        MaxItems=123,
        NextToken='string',
        SemanticVersion='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]
            The Amazon Resource Name (ARN) of the application.
            

    :type MaxItems: integer
    :param MaxItems: The total number of items to return.

    :type NextToken: string
    :param NextToken: A token to specify where to start paginating.

    :type SemanticVersion: string
    :param SemanticVersion: The semantic version of the application to get.

    :rtype: dict
    :return: {
        'Dependencies': [
            {
                'ApplicationId': 'string',
                'SemanticVersion': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_application_versions(ApplicationId=None, MaxItems=None, NextToken=None):
    """
    Lists versions for the specified application.
    See also: AWS API Documentation
    
    
    :example: response = client.list_application_versions(
        ApplicationId='string',
        MaxItems=123,
        NextToken='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]
            The Amazon Resource Name (ARN) of the application.
            

    :type MaxItems: integer
    :param MaxItems: The total number of items to return.

    :type NextToken: string
    :param NextToken: A token to specify where to start paginating.

    :rtype: dict
    :return: {
        'NextToken': 'string',
        'Versions': [
            {
                'ApplicationId': 'string',
                'CreationTime': 'string',
                'SemanticVersion': 'string',
                'SourceCodeUrl': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_applications(MaxItems=None, NextToken=None):
    """
    Lists applications owned by the requester.
    See also: AWS API Documentation
    
    
    :example: response = client.list_applications(
        MaxItems=123,
        NextToken='string'
    )
    
    
    :type MaxItems: integer
    :param MaxItems: The total number of items to return.

    :type NextToken: string
    :param NextToken: A token to specify where to start paginating.

    :rtype: dict
    :return: {
        'Applications': [
            {
                'ApplicationId': 'string',
                'Author': 'string',
                'CreationTime': 'string',
                'Description': 'string',
                'HomePageUrl': 'string',
                'Labels': [
                    'string',
                ],
                'Name': 'string',
                'SpdxLicenseId': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def put_application_policy(ApplicationId=None, Statements=None):
    """
    Sets the permission policy for an application. For the list of actions supported for this operation, see Application Permissions .
    See also: AWS API Documentation
    
    
    :example: response = client.put_application_policy(
        ApplicationId='string',
        Statements=[
            {
                'Actions': [
                    'string',
                ],
                'Principals': [
                    'string',
                ],
                'StatementId': 'string'
            },
        ]
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]
            The Amazon Resource Name (ARN) of the application.
            

    :type Statements: list
    :param Statements: [REQUIRED]
            An array of policy statements applied to the application.
            (dict) --Policy statement applied to the application.
            Actions (list) -- [REQUIRED]For the list of actions supported for this operation, see Application Permissions .
            (string) --
            Principals (list) -- [REQUIRED]An AWS account ID, or * to make the application public.
            (string) --
            StatementId (string) --A unique ID for the statement.
            
            

    :rtype: dict
    :return: {
        'Statements': [
            {
                'Actions': [
                    'string',
                ],
                'Principals': [
                    'string',
                ],
                'StatementId': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_application(ApplicationId=None, Author=None, Description=None, HomePageUrl=None, Labels=None, ReadmeBody=None, ReadmeUrl=None):
    """
    Updates the specified application.
    See also: AWS API Documentation
    
    
    :example: response = client.update_application(
        ApplicationId='string',
        Author='string',
        Description='string',
        HomePageUrl='string',
        Labels=[
            'string',
        ],
        ReadmeBody='string',
        ReadmeUrl='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]
            The Amazon Resource Name (ARN) of the application.
            

    :type Author: string
    :param Author: The name of the author publishing the app.
            Minimum length=1. Maximum length=127.
            Pattern '^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$';
            

    :type Description: string
    :param Description: The description of the application.
            Minimum length=1. Maximum length=256
            

    :type HomePageUrl: string
    :param HomePageUrl: A URL with more information about the application, for example the location of your GitHub repository for the application.

    :type Labels: list
    :param Labels: Labels to improve discovery of apps in search results.
            Minimum length=1. Maximum length=127. Maximum number of labels: 10
            Pattern: '^[a-zA-Z0-9+\-_:\/@]+$';
            (string) --
            

    :type ReadmeBody: string
    :param ReadmeBody: A text readme file in Markdown language that contains a more detailed description of the application and how it works.
            Maximum size 5 MB
            

    :type ReadmeUrl: string
    :param ReadmeUrl: A link to the readme file in Markdown language that contains a more detailed description of the application and how it works.
            Maximum size 5 MB
            

    :rtype: dict
    :return: {
        'ApplicationId': 'string',
        'Author': 'string',
        'CreationTime': 'string',
        'Description': 'string',
        'HomePageUrl': 'string',
        'Labels': [
            'string',
        ],
        'LicenseUrl': 'string',
        'Name': 'string',
        'ReadmeUrl': 'string',
        'SpdxLicenseId': 'string',
        'Version': {
            'ApplicationId': 'string',
            'CreationTime': 'string',
            'ParameterDefinitions': [
                {
                    'AllowedPattern': 'string',
                    'AllowedValues': [
                        'string',
                    ],
                    'ConstraintDescription': 'string',
                    'DefaultValue': 'string',
                    'Description': 'string',
                    'MaxLength': 123,
                    'MaxValue': 123,
                    'MinLength': 123,
                    'MinValue': 123,
                    'Name': 'string',
                    'NoEcho': True|False,
                    'ReferencedByResources': [
                        'string',
                    ],
                    'Type': 'string'
                },
            ],
            'RequiredCapabilities': [
                'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND'|'CAPABILITY_RESOURCE_POLICY',
            ],
            'ResourcesSupported': True|False,
            'SemanticVersion': 'string',
            'SourceCodeUrl': 'string',
            'TemplateUrl': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

