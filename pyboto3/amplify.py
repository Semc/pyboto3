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

def create_app(name=None, description=None, repository=None, platform=None, iamServiceRoleArn=None, oauthToken=None, environmentVariables=None, enableBranchAutoBuild=None, enableBasicAuth=None, basicAuthCredentials=None, customRules=None, tags=None, buildSpec=None):
    """
    Creates a new Amplify App.
    See also: AWS API Documentation
    
    
    :example: response = client.create_app(
        name='string',
        description='string',
        repository='string',
        platform='IOS'|'ANDROID'|'WEB'|'REACT_NATIVE',
        iamServiceRoleArn='string',
        oauthToken='string',
        environmentVariables={
            'string': 'string'
        },
        enableBranchAutoBuild=True|False,
        enableBasicAuth=True|False,
        basicAuthCredentials='string',
        customRules=[
            {
                'source': 'string',
                'target': 'string',
                'status': 'string',
                'condition': 'string'
            },
        ],
        tags={
            'string': 'string'
        },
        buildSpec='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            Name for the Amplify App
            

    :type description: string
    :param description: Description for an Amplify App

    :type repository: string
    :param repository: [REQUIRED]
            Repository for an Amplify App
            

    :type platform: string
    :param platform: [REQUIRED]
            Platform / framework for an Amplify App
            

    :type iamServiceRoleArn: string
    :param iamServiceRoleArn: AWS IAM service role for an Amplify App

    :type oauthToken: string
    :param oauthToken: [REQUIRED]
            OAuth token for 3rd party source control system for an Amplify App, used to create webhook and read-only deploy key. OAuth token is not stored.
            

    :type environmentVariables: dict
    :param environmentVariables: Environment variables map for an Amplify App.
            (string) --
            (string) --
            

    :type enableBranchAutoBuild: boolean
    :param enableBranchAutoBuild: Enable the auto building of branches for an Amplify App.

    :type enableBasicAuth: boolean
    :param enableBasicAuth: Enable Basic Authorization for an Amplify App, this will apply to all branches part of this App.

    :type basicAuthCredentials: string
    :param basicAuthCredentials: Credentials for Basic Authorization for an Amplify App.

    :type customRules: list
    :param customRules: Custom rewrite / redirect rules for an Amplify App.
            (dict) --Custom rewrite / redirect rule.
            source (string) -- [REQUIRED]The source pattern for a URL rewrite or redirect rule.
            target (string) -- [REQUIRED]The target pattern for a URL rewrite or redirect rule.
            status (string) --The status code for a URL rewrite or redirect rule.
            condition (string) --The condition for a URL rewrite or redirect rule, e.g. country code.
            
            

    :type tags: dict
    :param tags: Tag for an Amplify App
            (string) --
            (string) --
            

    :type buildSpec: string
    :param buildSpec: BuildSpec for an Amplify App

    :rtype: dict
    :return: {
        'app': {
            'appId': 'string',
            'appArn': 'string',
            'name': 'string',
            'tags': {
                'string': 'string'
            },
            'description': 'string',
            'repository': 'string',
            'platform': 'IOS'|'ANDROID'|'WEB'|'REACT_NATIVE',
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1),
            'iamServiceRoleArn': 'string',
            'environmentVariables': {
                'string': 'string'
            },
            'defaultDomain': 'string',
            'enableBranchAutoBuild': True|False,
            'enableBasicAuth': True|False,
            'basicAuthCredentials': 'string',
            'customRules': [
                {
                    'source': 'string',
                    'target': 'string',
                    'status': 'string',
                    'condition': 'string'
                },
            ],
            'productionBranch': {
                'lastDeployTime': datetime(2015, 1, 1),
                'status': 'string',
                'thumbnailUrl': 'string',
                'branchName': 'string'
            },
            'buildSpec': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def create_branch(appId=None, branchName=None, description=None, stage=None, framework=None, enableNotification=None, enableAutoBuild=None, environmentVariables=None, basicAuthCredentials=None, enableBasicAuth=None, tags=None, buildSpec=None, ttl=None):
    """
    Creates a new Branch for an Amplify App.
    See also: AWS API Documentation
    
    
    :example: response = client.create_branch(
        appId='string',
        branchName='string',
        description='string',
        stage='PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL',
        framework='string',
        enableNotification=True|False,
        enableAutoBuild=True|False,
        environmentVariables={
            'string': 'string'
        },
        basicAuthCredentials='string',
        enableBasicAuth=True|False,
        tags={
            'string': 'string'
        },
        buildSpec='string',
        ttl='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]
            Unique Id for an Amplify App.
            

    :type branchName: string
    :param branchName: [REQUIRED]
            Name for the branch.
            

    :type description: string
    :param description: Description for the branch.

    :type stage: string
    :param stage: Stage for the branch.

    :type framework: string
    :param framework: Framework for the branch.

    :type enableNotification: boolean
    :param enableNotification: Enables notifications for the branch.

    :type enableAutoBuild: boolean
    :param enableAutoBuild: Enables auto building for the branch.

    :type environmentVariables: dict
    :param environmentVariables: Environment Variables for the branch.
            (string) --
            (string) --
            

    :type basicAuthCredentials: string
    :param basicAuthCredentials: Basic Authorization credentials for the branch.

    :type enableBasicAuth: boolean
    :param enableBasicAuth: Enables Basic Auth for the branch.

    :type tags: dict
    :param tags: Tag for the branch.
            (string) --
            (string) --
            

    :type buildSpec: string
    :param buildSpec: BuildSpec for the branch.

    :type ttl: string
    :param ttl: The content TTL for the website in seconds.

    :rtype: dict
    :return: {
        'branch': {
            'branchArn': 'string',
            'branchName': 'string',
            'description': 'string',
            'tags': {
                'string': 'string'
            },
            'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL',
            'displayName': 'string',
            'enableNotification': True|False,
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1),
            'environmentVariables': {
                'string': 'string'
            },
            'enableAutoBuild': True|False,
            'customDomains': [
                'string',
            ],
            'framework': 'string',
            'activeJobId': 'string',
            'totalNumberOfJobs': 'string',
            'enableBasicAuth': True|False,
            'thumbnailUrl': 'string',
            'basicAuthCredentials': 'string',
            'buildSpec': 'string',
            'ttl': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def create_domain_association(appId=None, domainName=None, enableAutoSubDomain=None, subDomainSettings=None):
    """
    Create a new DomainAssociation on an App
    See also: AWS API Documentation
    
    
    :example: response = client.create_domain_association(
        appId='string',
        domainName='string',
        enableAutoSubDomain=True|False,
        subDomainSettings=[
            {
                'prefix': 'string',
                'branchName': 'string'
            },
        ]
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]
            Unique Id for an Amplify App.
            

    :type domainName: string
    :param domainName: [REQUIRED]
            Domain name for the Domain Association.
            

    :type enableAutoSubDomain: boolean
    :param enableAutoSubDomain: Enables automated creation of Subdomains for branches.

    :type subDomainSettings: list
    :param subDomainSettings: [REQUIRED]
            Setting structure for the Subdomain.
            (dict) --Setting for the Subdomain.
            prefix (string) -- [REQUIRED]Prefix setting for the Subdomain.
            branchName (string) -- [REQUIRED]Branch name setting for the Subdomain.
            
            

    :rtype: dict
    :return: {
        'domainAssociation': {
            'domainAssociationArn': 'string',
            'domainName': 'string',
            'enableAutoSubDomain': True|False,
            'domainStatus': 'PENDING_VERIFICATION'|'IN_PROGRESS'|'AVAILABLE'|'PENDING_DEPLOYMENT'|'FAILED',
            'statusReason': 'string',
            'certificateVerificationDNSRecord': 'string',
            'subDomains': [
                {
                    'subDomainSetting': {
                        'prefix': 'string',
                        'branchName': 'string'
                    },
                    'verified': True|False,
                    'dnsRecord': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def delete_app(appId=None):
    """
    Delete an existing Amplify App by appId.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_app(
        appId='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]
            Unique Id for an Amplify App.
            

    :rtype: dict
    :return: {
        'app': {
            'appId': 'string',
            'appArn': 'string',
            'name': 'string',
            'tags': {
                'string': 'string'
            },
            'description': 'string',
            'repository': 'string',
            'platform': 'IOS'|'ANDROID'|'WEB'|'REACT_NATIVE',
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1),
            'iamServiceRoleArn': 'string',
            'environmentVariables': {
                'string': 'string'
            },
            'defaultDomain': 'string',
            'enableBranchAutoBuild': True|False,
            'enableBasicAuth': True|False,
            'basicAuthCredentials': 'string',
            'customRules': [
                {
                    'source': 'string',
                    'target': 'string',
                    'status': 'string',
                    'condition': 'string'
                },
            ],
            'productionBranch': {
                'lastDeployTime': datetime(2015, 1, 1),
                'status': 'string',
                'thumbnailUrl': 'string',
                'branchName': 'string'
            },
            'buildSpec': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def delete_branch(appId=None, branchName=None):
    """
    Deletes a branch for an Amplify App.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_branch(
        appId='string',
        branchName='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]
            Unique Id for an Amplify App.
            

    :type branchName: string
    :param branchName: [REQUIRED]
            Name for the branch.
            

    :rtype: dict
    :return: {
        'branch': {
            'branchArn': 'string',
            'branchName': 'string',
            'description': 'string',
            'tags': {
                'string': 'string'
            },
            'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL',
            'displayName': 'string',
            'enableNotification': True|False,
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1),
            'environmentVariables': {
                'string': 'string'
            },
            'enableAutoBuild': True|False,
            'customDomains': [
                'string',
            ],
            'framework': 'string',
            'activeJobId': 'string',
            'totalNumberOfJobs': 'string',
            'enableBasicAuth': True|False,
            'thumbnailUrl': 'string',
            'basicAuthCredentials': 'string',
            'buildSpec': 'string',
            'ttl': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def delete_domain_association(appId=None, domainName=None):
    """
    Deletes a DomainAssociation.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_domain_association(
        appId='string',
        domainName='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]
            Unique Id for an Amplify App.
            

    :type domainName: string
    :param domainName: [REQUIRED]
            Name of the domain.
            

    :rtype: dict
    :return: {
        'domainAssociation': {
            'domainAssociationArn': 'string',
            'domainName': 'string',
            'enableAutoSubDomain': True|False,
            'domainStatus': 'PENDING_VERIFICATION'|'IN_PROGRESS'|'AVAILABLE'|'PENDING_DEPLOYMENT'|'FAILED',
            'statusReason': 'string',
            'certificateVerificationDNSRecord': 'string',
            'subDomains': [
                {
                    'subDomainSetting': {
                        'prefix': 'string',
                        'branchName': 'string'
                    },
                    'verified': True|False,
                    'dnsRecord': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def delete_job(appId=None, branchName=None, jobId=None):
    """
    Delete a job, for an Amplify branch, part of Amplify App.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_job(
        appId='string',
        branchName='string',
        jobId='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]
            Unique Id for an Amplify App.
            

    :type branchName: string
    :param branchName: [REQUIRED]
            Name for the branch, for the Job.
            

    :type jobId: string
    :param jobId: [REQUIRED]
            Unique Id for the Job.
            

    :rtype: dict
    :return: {
        'jobSummary': {
            'jobArn': 'string',
            'jobId': 'string',
            'commitId': 'string',
            'commitMessage': 'string',
            'commitTime': datetime(2015, 1, 1),
            'startTime': datetime(2015, 1, 1),
            'status': 'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
            'endTime': datetime(2015, 1, 1),
            'jobType': 'RELEASE'|'RETRY'|'WEB_HOOK'
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

def get_app(appId=None):
    """
    Retrieves an existing Amplify App by appId.
    See also: AWS API Documentation
    
    
    :example: response = client.get_app(
        appId='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]
            Unique Id for an Amplify App.
            

    :rtype: dict
    :return: {
        'app': {
            'appId': 'string',
            'appArn': 'string',
            'name': 'string',
            'tags': {
                'string': 'string'
            },
            'description': 'string',
            'repository': 'string',
            'platform': 'IOS'|'ANDROID'|'WEB'|'REACT_NATIVE',
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1),
            'iamServiceRoleArn': 'string',
            'environmentVariables': {
                'string': 'string'
            },
            'defaultDomain': 'string',
            'enableBranchAutoBuild': True|False,
            'enableBasicAuth': True|False,
            'basicAuthCredentials': 'string',
            'customRules': [
                {
                    'source': 'string',
                    'target': 'string',
                    'status': 'string',
                    'condition': 'string'
                },
            ],
            'productionBranch': {
                'lastDeployTime': datetime(2015, 1, 1),
                'status': 'string',
                'thumbnailUrl': 'string',
                'branchName': 'string'
            },
            'buildSpec': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_branch(appId=None, branchName=None):
    """
    Retrieves a branch for an Amplify App.
    See also: AWS API Documentation
    
    
    :example: response = client.get_branch(
        appId='string',
        branchName='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]
            Unique Id for an Amplify App.
            

    :type branchName: string
    :param branchName: [REQUIRED]
            Name for the branch.
            

    :rtype: dict
    :return: {
        'branch': {
            'branchArn': 'string',
            'branchName': 'string',
            'description': 'string',
            'tags': {
                'string': 'string'
            },
            'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL',
            'displayName': 'string',
            'enableNotification': True|False,
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1),
            'environmentVariables': {
                'string': 'string'
            },
            'enableAutoBuild': True|False,
            'customDomains': [
                'string',
            ],
            'framework': 'string',
            'activeJobId': 'string',
            'totalNumberOfJobs': 'string',
            'enableBasicAuth': True|False,
            'thumbnailUrl': 'string',
            'basicAuthCredentials': 'string',
            'buildSpec': 'string',
            'ttl': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_domain_association(appId=None, domainName=None):
    """
    Retrieves domain info that corresponds to an appId and domainName.
    See also: AWS API Documentation
    
    
    :example: response = client.get_domain_association(
        appId='string',
        domainName='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]
            Unique Id for an Amplify App.
            

    :type domainName: string
    :param domainName: [REQUIRED]
            Name of the domain.
            

    :rtype: dict
    :return: {
        'domainAssociation': {
            'domainAssociationArn': 'string',
            'domainName': 'string',
            'enableAutoSubDomain': True|False,
            'domainStatus': 'PENDING_VERIFICATION'|'IN_PROGRESS'|'AVAILABLE'|'PENDING_DEPLOYMENT'|'FAILED',
            'statusReason': 'string',
            'certificateVerificationDNSRecord': 'string',
            'subDomains': [
                {
                    'subDomainSetting': {
                        'prefix': 'string',
                        'branchName': 'string'
                    },
                    'verified': True|False,
                    'dnsRecord': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def get_job(appId=None, branchName=None, jobId=None):
    """
    Get a job for a branch, part of an Amplify App.
    See also: AWS API Documentation
    
    
    :example: response = client.get_job(
        appId='string',
        branchName='string',
        jobId='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]
            Unique Id for an Amplify App.
            

    :type branchName: string
    :param branchName: [REQUIRED]
            Name for the branch, for the Job.
            

    :type jobId: string
    :param jobId: [REQUIRED]
            Unique Id for the Job.
            

    :rtype: dict
    :return: {
        'job': {
            'summary': {
                'jobArn': 'string',
                'jobId': 'string',
                'commitId': 'string',
                'commitMessage': 'string',
                'commitTime': datetime(2015, 1, 1),
                'startTime': datetime(2015, 1, 1),
                'status': 'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
                'endTime': datetime(2015, 1, 1),
                'jobType': 'RELEASE'|'RETRY'|'WEB_HOOK'
            },
            'steps': [
                {
                    'stepName': 'string',
                    'startTime': datetime(2015, 1, 1),
                    'status': 'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
                    'endTime': datetime(2015, 1, 1),
                    'logUrl': 'string',
                    'artifactsUrl': 'string',
                    'screenshots': {
                        'string': 'string'
                    }
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
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

def list_apps(nextToken=None, maxResults=None):
    """
    Lists existing Amplify Apps.
    See also: AWS API Documentation
    
    
    :example: response = client.list_apps(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: Pagination token. If non-null pagination token is returned in a result, then pass its value in another request to fetch more entries.

    :type maxResults: integer
    :param maxResults: Maximum number of records to list in a single response.

    :rtype: dict
    :return: {
        'apps': [
            {
                'appId': 'string',
                'appArn': 'string',
                'name': 'string',
                'tags': {
                    'string': 'string'
                },
                'description': 'string',
                'repository': 'string',
                'platform': 'IOS'|'ANDROID'|'WEB'|'REACT_NATIVE',
                'createTime': datetime(2015, 1, 1),
                'updateTime': datetime(2015, 1, 1),
                'iamServiceRoleArn': 'string',
                'environmentVariables': {
                    'string': 'string'
                },
                'defaultDomain': 'string',
                'enableBranchAutoBuild': True|False,
                'enableBasicAuth': True|False,
                'basicAuthCredentials': 'string',
                'customRules': [
                    {
                        'source': 'string',
                        'target': 'string',
                        'status': 'string',
                        'condition': 'string'
                    },
                ],
                'productionBranch': {
                    'lastDeployTime': datetime(2015, 1, 1),
                    'status': 'string',
                    'thumbnailUrl': 'string',
                    'branchName': 'string'
                },
                'buildSpec': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_branches(appId=None, nextToken=None, maxResults=None):
    """
    Lists branches for an Amplify App.
    See also: AWS API Documentation
    
    
    :example: response = client.list_branches(
        appId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]
            Unique Id for an Amplify App.
            

    :type nextToken: string
    :param nextToken: Pagination token. Set to null to start listing branches from start. If a non-null pagination token is returned in a result, then pass its value in here to list more branches.

    :type maxResults: integer
    :param maxResults: Maximum number of records to list in a single response.

    :rtype: dict
    :return: {
        'branches': [
            {
                'branchArn': 'string',
                'branchName': 'string',
                'description': 'string',
                'tags': {
                    'string': 'string'
                },
                'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL',
                'displayName': 'string',
                'enableNotification': True|False,
                'createTime': datetime(2015, 1, 1),
                'updateTime': datetime(2015, 1, 1),
                'environmentVariables': {
                    'string': 'string'
                },
                'enableAutoBuild': True|False,
                'customDomains': [
                    'string',
                ],
                'framework': 'string',
                'activeJobId': 'string',
                'totalNumberOfJobs': 'string',
                'enableBasicAuth': True|False,
                'thumbnailUrl': 'string',
                'basicAuthCredentials': 'string',
                'buildSpec': 'string',
                'ttl': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_domain_associations(appId=None, nextToken=None, maxResults=None):
    """
    List domains with an app
    See also: AWS API Documentation
    
    
    :example: response = client.list_domain_associations(
        appId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]
            Unique Id for an Amplify App.
            

    :type nextToken: string
    :param nextToken: Pagination token. Set to null to start listing Apps from start. If non-null pagination token is returned in a result, then pass its value in here to list more projects.

    :type maxResults: integer
    :param maxResults: Maximum number of records to list in a single response.

    :rtype: dict
    :return: {
        'domainAssociations': [
            {
                'domainAssociationArn': 'string',
                'domainName': 'string',
                'enableAutoSubDomain': True|False,
                'domainStatus': 'PENDING_VERIFICATION'|'IN_PROGRESS'|'AVAILABLE'|'PENDING_DEPLOYMENT'|'FAILED',
                'statusReason': 'string',
                'certificateVerificationDNSRecord': 'string',
                'subDomains': [
                    {
                        'subDomainSetting': {
                            'prefix': 'string',
                            'branchName': 'string'
                        },
                        'verified': True|False,
                        'dnsRecord': 'string'
                    },
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_jobs(appId=None, branchName=None, nextToken=None, maxResults=None):
    """
    List Jobs for a branch, part of an Amplify App.
    See also: AWS API Documentation
    
    
    :example: response = client.list_jobs(
        appId='string',
        branchName='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]
            Unique Id for an Amplify App.
            

    :type branchName: string
    :param branchName: [REQUIRED]
            Name for a branch.
            

    :type nextToken: string
    :param nextToken: Pagination token. Set to null to start listing steps from start. If a non-null pagination token is returned in a result, then pass its value in here to list more steps.

    :type maxResults: integer
    :param maxResults: Maximum number of records to list in a single response.

    :rtype: dict
    :return: {
        'jobSummaries': [
            {
                'jobArn': 'string',
                'jobId': 'string',
                'commitId': 'string',
                'commitMessage': 'string',
                'commitTime': datetime(2015, 1, 1),
                'startTime': datetime(2015, 1, 1),
                'status': 'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
                'endTime': datetime(2015, 1, 1),
                'jobType': 'RELEASE'|'RETRY'|'WEB_HOOK'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def start_job(appId=None, branchName=None, jobId=None, jobType=None, jobReason=None, commitId=None, commitMessage=None, commitTime=None):
    """
    Starts a new job for a branch, part of an Amplify App.
    See also: AWS API Documentation
    
    
    :example: response = client.start_job(
        appId='string',
        branchName='string',
        jobId='string',
        jobType='RELEASE'|'RETRY'|'WEB_HOOK',
        jobReason='string',
        commitId='string',
        commitMessage='string',
        commitTime=datetime(2015, 1, 1)
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]
            Unique Id for an Amplify App.
            

    :type branchName: string
    :param branchName: [REQUIRED]
            Name for the branch, for the Job.
            

    :type jobId: string
    :param jobId: Unique Id for the Job.

    :type jobType: string
    :param jobType: [REQUIRED]
            Type for the Job.
            

    :type jobReason: string
    :param jobReason: Reason for the Job.

    :type commitId: string
    :param commitId: Commit Id from 3rd party repository provider for the Job.

    :type commitMessage: string
    :param commitMessage: Commit message from 3rd party repository provider for the Job.

    :type commitTime: datetime
    :param commitTime: Commit date / time for the Job.

    :rtype: dict
    :return: {
        'jobSummary': {
            'jobArn': 'string',
            'jobId': 'string',
            'commitId': 'string',
            'commitMessage': 'string',
            'commitTime': datetime(2015, 1, 1),
            'startTime': datetime(2015, 1, 1),
            'status': 'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
            'endTime': datetime(2015, 1, 1),
            'jobType': 'RELEASE'|'RETRY'|'WEB_HOOK'
        }
    }
    
    
    """
    pass

def stop_job(appId=None, branchName=None, jobId=None):
    """
    Stop a job that is in progress, for an Amplify branch, part of Amplify App.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_job(
        appId='string',
        branchName='string',
        jobId='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]
            Unique Id for an Amplify App.
            

    :type branchName: string
    :param branchName: [REQUIRED]
            Name for the branch, for the Job.
            

    :type jobId: string
    :param jobId: [REQUIRED]
            Unique Id for the Job.
            

    :rtype: dict
    :return: {
        'jobSummary': {
            'jobArn': 'string',
            'jobId': 'string',
            'commitId': 'string',
            'commitMessage': 'string',
            'commitTime': datetime(2015, 1, 1),
            'startTime': datetime(2015, 1, 1),
            'status': 'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
            'endTime': datetime(2015, 1, 1),
            'jobType': 'RELEASE'|'RETRY'|'WEB_HOOK'
        }
    }
    
    
    """
    pass

def update_app(appId=None, name=None, description=None, platform=None, iamServiceRoleArn=None, environmentVariables=None, enableBranchAutoBuild=None, enableBasicAuth=None, basicAuthCredentials=None, customRules=None, buildSpec=None):
    """
    Updates an existing Amplify App.
    See also: AWS API Documentation
    
    
    :example: response = client.update_app(
        appId='string',
        name='string',
        description='string',
        platform='IOS'|'ANDROID'|'WEB'|'REACT_NATIVE',
        iamServiceRoleArn='string',
        environmentVariables={
            'string': 'string'
        },
        enableBranchAutoBuild=True|False,
        enableBasicAuth=True|False,
        basicAuthCredentials='string',
        customRules=[
            {
                'source': 'string',
                'target': 'string',
                'status': 'string',
                'condition': 'string'
            },
        ],
        buildSpec='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]
            Unique Id for an Amplify App.
            

    :type name: string
    :param name: Name for an Amplify App.

    :type description: string
    :param description: Description for an Amplify App.

    :type platform: string
    :param platform: Platform for an Amplify App.

    :type iamServiceRoleArn: string
    :param iamServiceRoleArn: IAM service role for an Amplify App.

    :type environmentVariables: dict
    :param environmentVariables: Environment Variables for an Amplify App.
            (string) --
            (string) --
            

    :type enableBranchAutoBuild: boolean
    :param enableBranchAutoBuild: Enables branch auto-building for an Amplify App.

    :type enableBasicAuth: boolean
    :param enableBasicAuth: Enables Basic Authorization for an Amplify App.

    :type basicAuthCredentials: string
    :param basicAuthCredentials: Basic Authorization credentials for an Amplify App.

    :type customRules: list
    :param customRules: Custom redirect / rewrite rules for an Amplify App.
            (dict) --Custom rewrite / redirect rule.
            source (string) -- [REQUIRED]The source pattern for a URL rewrite or redirect rule.
            target (string) -- [REQUIRED]The target pattern for a URL rewrite or redirect rule.
            status (string) --The status code for a URL rewrite or redirect rule.
            condition (string) --The condition for a URL rewrite or redirect rule, e.g. country code.
            
            

    :type buildSpec: string
    :param buildSpec: BuildSpec for an Amplify App.

    :rtype: dict
    :return: {
        'app': {
            'appId': 'string',
            'appArn': 'string',
            'name': 'string',
            'tags': {
                'string': 'string'
            },
            'description': 'string',
            'repository': 'string',
            'platform': 'IOS'|'ANDROID'|'WEB'|'REACT_NATIVE',
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1),
            'iamServiceRoleArn': 'string',
            'environmentVariables': {
                'string': 'string'
            },
            'defaultDomain': 'string',
            'enableBranchAutoBuild': True|False,
            'enableBasicAuth': True|False,
            'basicAuthCredentials': 'string',
            'customRules': [
                {
                    'source': 'string',
                    'target': 'string',
                    'status': 'string',
                    'condition': 'string'
                },
            ],
            'productionBranch': {
                'lastDeployTime': datetime(2015, 1, 1),
                'status': 'string',
                'thumbnailUrl': 'string',
                'branchName': 'string'
            },
            'buildSpec': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def update_branch(appId=None, branchName=None, description=None, framework=None, stage=None, enableNotification=None, enableAutoBuild=None, environmentVariables=None, basicAuthCredentials=None, enableBasicAuth=None, buildSpec=None, ttl=None):
    """
    Updates a branch for an Amplify App.
    See also: AWS API Documentation
    
    
    :example: response = client.update_branch(
        appId='string',
        branchName='string',
        description='string',
        framework='string',
        stage='PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL',
        enableNotification=True|False,
        enableAutoBuild=True|False,
        environmentVariables={
            'string': 'string'
        },
        basicAuthCredentials='string',
        enableBasicAuth=True|False,
        buildSpec='string',
        ttl='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]
            Unique Id for an Amplify App.
            

    :type branchName: string
    :param branchName: [REQUIRED]
            Name for the branch.
            

    :type description: string
    :param description: Description for the branch.

    :type framework: string
    :param framework: Framework for the branch.

    :type stage: string
    :param stage: Stage for the branch.

    :type enableNotification: boolean
    :param enableNotification: Enables notifications for the branch.

    :type enableAutoBuild: boolean
    :param enableAutoBuild: Enables auto building for the branch.

    :type environmentVariables: dict
    :param environmentVariables: Environment Variables for the branch.
            (string) --
            (string) --
            

    :type basicAuthCredentials: string
    :param basicAuthCredentials: Basic Authorization credentials for the branch.

    :type enableBasicAuth: boolean
    :param enableBasicAuth: Enables Basic Auth for the branch.

    :type buildSpec: string
    :param buildSpec: BuildSpec for the branch.

    :type ttl: string
    :param ttl: The content TTL for the website in seconds.

    :rtype: dict
    :return: {
        'branch': {
            'branchArn': 'string',
            'branchName': 'string',
            'description': 'string',
            'tags': {
                'string': 'string'
            },
            'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL',
            'displayName': 'string',
            'enableNotification': True|False,
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1),
            'environmentVariables': {
                'string': 'string'
            },
            'enableAutoBuild': True|False,
            'customDomains': [
                'string',
            ],
            'framework': 'string',
            'activeJobId': 'string',
            'totalNumberOfJobs': 'string',
            'enableBasicAuth': True|False,
            'thumbnailUrl': 'string',
            'basicAuthCredentials': 'string',
            'buildSpec': 'string',
            'ttl': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def update_domain_association(appId=None, domainName=None, enableAutoSubDomain=None, subDomainSettings=None):
    """
    Create a new DomainAssociation on an App
    See also: AWS API Documentation
    
    
    :example: response = client.update_domain_association(
        appId='string',
        domainName='string',
        enableAutoSubDomain=True|False,
        subDomainSettings=[
            {
                'prefix': 'string',
                'branchName': 'string'
            },
        ]
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]
            Unique Id for an Amplify App.
            

    :type domainName: string
    :param domainName: [REQUIRED]
            Name of the domain.
            

    :type enableAutoSubDomain: boolean
    :param enableAutoSubDomain: Enables automated creation of Subdomains for branches.

    :type subDomainSettings: list
    :param subDomainSettings: [REQUIRED]
            Setting structure for the Subdomain.
            (dict) --Setting for the Subdomain.
            prefix (string) -- [REQUIRED]Prefix setting for the Subdomain.
            branchName (string) -- [REQUIRED]Branch name setting for the Subdomain.
            
            

    :rtype: dict
    :return: {
        'domainAssociation': {
            'domainAssociationArn': 'string',
            'domainName': 'string',
            'enableAutoSubDomain': True|False,
            'domainStatus': 'PENDING_VERIFICATION'|'IN_PROGRESS'|'AVAILABLE'|'PENDING_DEPLOYMENT'|'FAILED',
            'statusReason': 'string',
            'certificateVerificationDNSRecord': 'string',
            'subDomains': [
                {
                    'subDomainSetting': {
                        'prefix': 'string',
                        'branchName': 'string'
                    },
                    'verified': True|False,
                    'dnsRecord': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

