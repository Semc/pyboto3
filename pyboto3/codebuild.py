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

def batch_delete_builds(ids=None):
    """
    Deletes one or more builds.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_delete_builds(
        ids=[
            'string',
        ]
    )
    
    
    :type ids: list
    :param ids: [REQUIRED]
            The IDs of the builds to delete.
            (string) --
            

    :rtype: dict
    :return: {
        'buildsDeleted': [
            'string',
        ],
        'buildsNotDeleted': [
            {
                'id': 'string',
                'statusCode': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def batch_get_builds(ids=None):
    """
    Gets information about builds.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_get_builds(
        ids=[
            'string',
        ]
    )
    
    
    :type ids: list
    :param ids: [REQUIRED]
            The IDs of the builds.
            (string) --
            

    :rtype: dict
    :return: {
        'builds': [
            {
                'id': 'string',
                'arn': 'string',
                'startTime': datetime(2015, 1, 1),
                'endTime': datetime(2015, 1, 1),
                'currentPhase': 'string',
                'buildStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',
                'sourceVersion': 'string',
                'resolvedSourceVersion': 'string',
                'projectName': 'string',
                'phases': [
                    {
                        'phaseType': 'SUBMITTED'|'QUEUED'|'PROVISIONING'|'DOWNLOAD_SOURCE'|'INSTALL'|'PRE_BUILD'|'BUILD'|'POST_BUILD'|'UPLOAD_ARTIFACTS'|'FINALIZING'|'COMPLETED',
                        'phaseStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',
                        'startTime': datetime(2015, 1, 1),
                        'endTime': datetime(2015, 1, 1),
                        'durationInSeconds': 123,
                        'contexts': [
                            {
                                'statusCode': 'string',
                                'message': 'string'
                            },
                        ]
                    },
                ],
                'source': {
                    'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                    'location': 'string',
                    'gitCloneDepth': 123,
                    'buildspec': 'string',
                    'auth': {
                        'type': 'OAUTH',
                        'resource': 'string'
                    },
                    'reportBuildStatus': True|False,
                    'insecureSsl': True|False,
                    'sourceIdentifier': 'string'
                },
                'secondarySources': [
                    {
                        'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                        'location': 'string',
                        'gitCloneDepth': 123,
                        'buildspec': 'string',
                        'auth': {
                            'type': 'OAUTH',
                            'resource': 'string'
                        },
                        'reportBuildStatus': True|False,
                        'insecureSsl': True|False,
                        'sourceIdentifier': 'string'
                    },
                ],
                'secondarySourceVersions': [
                    {
                        'sourceIdentifier': 'string',
                        'sourceVersion': 'string'
                    },
                ],
                'artifacts': {
                    'location': 'string',
                    'sha256sum': 'string',
                    'md5sum': 'string',
                    'overrideArtifactName': True|False,
                    'encryptionDisabled': True|False,
                    'artifactIdentifier': 'string'
                },
                'secondaryArtifacts': [
                    {
                        'location': 'string',
                        'sha256sum': 'string',
                        'md5sum': 'string',
                        'overrideArtifactName': True|False,
                        'encryptionDisabled': True|False,
                        'artifactIdentifier': 'string'
                    },
                ],
                'cache': {
                    'type': 'NO_CACHE'|'S3',
                    'location': 'string'
                },
                'environment': {
                    'type': 'WINDOWS_CONTAINER'|'LINUX_CONTAINER',
                    'image': 'string',
                    'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE',
                    'environmentVariables': [
                        {
                            'name': 'string',
                            'value': 'string',
                            'type': 'PLAINTEXT'|'PARAMETER_STORE'
                        },
                    ],
                    'privilegedMode': True|False,
                    'certificate': 'string'
                },
                'serviceRole': 'string',
                'logs': {
                    'groupName': 'string',
                    'streamName': 'string',
                    'deepLink': 'string',
                    's3DeepLink': 'string',
                    'cloudWatchLogs': {
                        'status': 'ENABLED'|'DISABLED',
                        'groupName': 'string',
                        'streamName': 'string'
                    },
                    's3Logs': {
                        'status': 'ENABLED'|'DISABLED',
                        'location': 'string'
                    }
                },
                'timeoutInMinutes': 123,
                'queuedTimeoutInMinutes': 123,
                'buildComplete': True|False,
                'initiator': 'string',
                'vpcConfig': {
                    'vpcId': 'string',
                    'subnets': [
                        'string',
                    ],
                    'securityGroupIds': [
                        'string',
                    ]
                },
                'networkInterface': {
                    'subnetId': 'string',
                    'networkInterfaceId': 'string'
                },
                'encryptionKey': 'string'
            },
        ],
        'buildsNotFound': [
            'string',
        ]
    }
    
    
    :returns: 
    FAILED : The build failed.
    FAULT : The build faulted.
    IN_PROGRESS : The build is still in progress.
    STOPPED : The build stopped.
    SUCCEEDED : The build succeeded.
    TIMED_OUT : The build timed out.
    
    """
    pass

def batch_get_projects(names=None):
    """
    Gets information about build projects.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_get_projects(
        names=[
            'string',
        ]
    )
    
    
    :type names: list
    :param names: [REQUIRED]
            The names of the build projects.
            (string) --
            

    :rtype: dict
    :return: {
        'projects': [
            {
                'name': 'string',
                'arn': 'string',
                'description': 'string',
                'source': {
                    'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                    'location': 'string',
                    'gitCloneDepth': 123,
                    'buildspec': 'string',
                    'auth': {
                        'type': 'OAUTH',
                        'resource': 'string'
                    },
                    'reportBuildStatus': True|False,
                    'insecureSsl': True|False,
                    'sourceIdentifier': 'string'
                },
                'secondarySources': [
                    {
                        'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                        'location': 'string',
                        'gitCloneDepth': 123,
                        'buildspec': 'string',
                        'auth': {
                            'type': 'OAUTH',
                            'resource': 'string'
                        },
                        'reportBuildStatus': True|False,
                        'insecureSsl': True|False,
                        'sourceIdentifier': 'string'
                    },
                ],
                'artifacts': {
                    'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                    'location': 'string',
                    'path': 'string',
                    'namespaceType': 'NONE'|'BUILD_ID',
                    'name': 'string',
                    'packaging': 'NONE'|'ZIP',
                    'overrideArtifactName': True|False,
                    'encryptionDisabled': True|False,
                    'artifactIdentifier': 'string'
                },
                'secondaryArtifacts': [
                    {
                        'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                        'location': 'string',
                        'path': 'string',
                        'namespaceType': 'NONE'|'BUILD_ID',
                        'name': 'string',
                        'packaging': 'NONE'|'ZIP',
                        'overrideArtifactName': True|False,
                        'encryptionDisabled': True|False,
                        'artifactIdentifier': 'string'
                    },
                ],
                'cache': {
                    'type': 'NO_CACHE'|'S3',
                    'location': 'string'
                },
                'environment': {
                    'type': 'WINDOWS_CONTAINER'|'LINUX_CONTAINER',
                    'image': 'string',
                    'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE',
                    'environmentVariables': [
                        {
                            'name': 'string',
                            'value': 'string',
                            'type': 'PLAINTEXT'|'PARAMETER_STORE'
                        },
                    ],
                    'privilegedMode': True|False,
                    'certificate': 'string'
                },
                'serviceRole': 'string',
                'timeoutInMinutes': 123,
                'queuedTimeoutInMinutes': 123,
                'encryptionKey': 'string',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'created': datetime(2015, 1, 1),
                'lastModified': datetime(2015, 1, 1),
                'webhook': {
                    'url': 'string',
                    'payloadUrl': 'string',
                    'secret': 'string',
                    'branchFilter': 'string',
                    'lastModifiedSecret': datetime(2015, 1, 1)
                },
                'vpcConfig': {
                    'vpcId': 'string',
                    'subnets': [
                        'string',
                    ],
                    'securityGroupIds': [
                        'string',
                    ]
                },
                'badge': {
                    'badgeEnabled': True|False,
                    'badgeRequestUrl': 'string'
                },
                'logsConfig': {
                    'cloudWatchLogs': {
                        'status': 'ENABLED'|'DISABLED',
                        'groupName': 'string',
                        'streamName': 'string'
                    },
                    's3Logs': {
                        'status': 'ENABLED'|'DISABLED',
                        'location': 'string'
                    }
                }
            },
        ],
        'projectsNotFound': [
            'string',
        ]
    }
    
    
    :returns: 
    BITBUCKET : The source code is in a Bitbucket repository.
    CODECOMMIT : The source code is in an AWS CodeCommit repository.
    CODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.
    GITHUB : The source code is in a GitHub repository.
    NO_SOURCE : The project does not have input source code.
    S3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.
    
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

def create_project(name=None, description=None, source=None, secondarySources=None, artifacts=None, secondaryArtifacts=None, cache=None, environment=None, serviceRole=None, timeoutInMinutes=None, queuedTimeoutInMinutes=None, encryptionKey=None, tags=None, vpcConfig=None, badgeEnabled=None, logsConfig=None):
    """
    Creates a build project.
    See also: AWS API Documentation
    
    
    :example: response = client.create_project(
        name='string',
        description='string',
        source={
            'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
            'location': 'string',
            'gitCloneDepth': 123,
            'buildspec': 'string',
            'auth': {
                'type': 'OAUTH',
                'resource': 'string'
            },
            'reportBuildStatus': True|False,
            'insecureSsl': True|False,
            'sourceIdentifier': 'string'
        },
        secondarySources=[
            {
                'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                'location': 'string',
                'gitCloneDepth': 123,
                'buildspec': 'string',
                'auth': {
                    'type': 'OAUTH',
                    'resource': 'string'
                },
                'reportBuildStatus': True|False,
                'insecureSsl': True|False,
                'sourceIdentifier': 'string'
            },
        ],
        artifacts={
            'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
            'location': 'string',
            'path': 'string',
            'namespaceType': 'NONE'|'BUILD_ID',
            'name': 'string',
            'packaging': 'NONE'|'ZIP',
            'overrideArtifactName': True|False,
            'encryptionDisabled': True|False,
            'artifactIdentifier': 'string'
        },
        secondaryArtifacts=[
            {
                'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                'location': 'string',
                'path': 'string',
                'namespaceType': 'NONE'|'BUILD_ID',
                'name': 'string',
                'packaging': 'NONE'|'ZIP',
                'overrideArtifactName': True|False,
                'encryptionDisabled': True|False,
                'artifactIdentifier': 'string'
            },
        ],
        cache={
            'type': 'NO_CACHE'|'S3',
            'location': 'string'
        },
        environment={
            'type': 'WINDOWS_CONTAINER'|'LINUX_CONTAINER',
            'image': 'string',
            'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE',
            'environmentVariables': [
                {
                    'name': 'string',
                    'value': 'string',
                    'type': 'PLAINTEXT'|'PARAMETER_STORE'
                },
            ],
            'privilegedMode': True|False,
            'certificate': 'string'
        },
        serviceRole='string',
        timeoutInMinutes=123,
        queuedTimeoutInMinutes=123,
        encryptionKey='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        vpcConfig={
            'vpcId': 'string',
            'subnets': [
                'string',
            ],
            'securityGroupIds': [
                'string',
            ]
        },
        badgeEnabled=True|False,
        logsConfig={
            'cloudWatchLogs': {
                'status': 'ENABLED'|'DISABLED',
                'groupName': 'string',
                'streamName': 'string'
            },
            's3Logs': {
                'status': 'ENABLED'|'DISABLED',
                'location': 'string'
            }
        }
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the build project.
            

    :type description: string
    :param description: A description that makes the build project easy to identify.

    :type source: dict
    :param source: [REQUIRED]
            Information about the build input source code for the build project.
            type (string) -- [REQUIRED]The type of repository that contains the source code to be built. Valid values include:
            BITBUCKET : The source code is in a Bitbucket repository.
            CODECOMMIT : The source code is in an AWS CodeCommit repository.
            CODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.
            GITHUB : The source code is in a GitHub repository.
            NO_SOURCE : The project does not have input source code.
            S3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.
            location (string) --Information about the location of the source code to be built. Valid values include:
            For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, location should not be specified. If it is specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a pipeline's source action instead of this value.
            For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/repo-name `` ).
            For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.
            The path to the ZIP file that contains the source code (for example, `` bucket-name /path /to /object-name .zip`` ).
            The path to the folder that contains the source code (for example, `` bucket-name /path /to /source-code /folder /`` ).
            For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. You must connect your AWS account to your GitHub account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub Authorize application page, for Organization access , choose Request access next to each repository you want to allow AWS CodeBuild to have access to, and then choose Authorize application . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object's type value to OAUTH .
            For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. You must connect your AWS account to your Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket Confirm access to your account page, choose Grant access . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object's type value to OAUTH .
            gitCloneDepth (integer) --Information about the git clone depth for the build project.
            buildspec (string) --The build spec declaration to use for the builds in this build project.
            If this value is not specified, a build spec must be included along with the source code to be built.
            auth (dict) --Information about the authorization settings for AWS CodeBuild to access the source code to be built.
            This information is for the AWS CodeBuild console's use only. Your code should not get or set this information directly.
            type (string) -- [REQUIRED]
            Note
            This data type is deprecated and is no longer accurate or used.
            The authorization type to use. The only valid value is OAUTH , which represents the OAuth authorization type.
            resource (string) --The resource value that applies to the specified authorization type.
            reportBuildStatus (boolean) --Set to true to report the status of a build's start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown.
            insecureSsl (boolean) --Enable this flag to ignore SSL warnings while connecting to the project source code.
            sourceIdentifier (string) --An identifier for this project source.
            

    :type secondarySources: list
    :param secondarySources: An array of ProjectSource objects.
            (dict) --Information about the build input source code for the build project.
            type (string) -- [REQUIRED]The type of repository that contains the source code to be built. Valid values include:
            BITBUCKET : The source code is in a Bitbucket repository.
            CODECOMMIT : The source code is in an AWS CodeCommit repository.
            CODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.
            GITHUB : The source code is in a GitHub repository.
            NO_SOURCE : The project does not have input source code.
            S3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.
            location (string) --Information about the location of the source code to be built. Valid values include:
            For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, location should not be specified. If it is specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a pipeline's source action instead of this value.
            For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/repo-name `` ).
            For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.
            The path to the ZIP file that contains the source code (for example, `` bucket-name /path /to /object-name .zip`` ).
            The path to the folder that contains the source code (for example, `` bucket-name /path /to /source-code /folder /`` ).
            For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. You must connect your AWS account to your GitHub account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub Authorize application page, for Organization access , choose Request access next to each repository you want to allow AWS CodeBuild to have access to, and then choose Authorize application . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object's type value to OAUTH .
            For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. You must connect your AWS account to your Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket Confirm access to your account page, choose Grant access . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object's type value to OAUTH .
            gitCloneDepth (integer) --Information about the git clone depth for the build project.
            buildspec (string) --The build spec declaration to use for the builds in this build project.
            If this value is not specified, a build spec must be included along with the source code to be built.
            auth (dict) --Information about the authorization settings for AWS CodeBuild to access the source code to be built.
            This information is for the AWS CodeBuild console's use only. Your code should not get or set this information directly.
            type (string) -- [REQUIRED]
            Note
            This data type is deprecated and is no longer accurate or used.
            The authorization type to use. The only valid value is OAUTH , which represents the OAuth authorization type.
            resource (string) --The resource value that applies to the specified authorization type.
            reportBuildStatus (boolean) --Set to true to report the status of a build's start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown.
            insecureSsl (boolean) --Enable this flag to ignore SSL warnings while connecting to the project source code.
            sourceIdentifier (string) --An identifier for this project source.
            
            

    :type artifacts: dict
    :param artifacts: [REQUIRED]
            Information about the build output artifacts for the build project.
            type (string) -- [REQUIRED]The type of build output artifact. Valid values include:
            CODEPIPELINE : The build project has build output generated through AWS CodePipeline.
            NO_ARTIFACTS : The build project does not produce any build output.
            S3 : The build project stores build output in Amazon Simple Storage Service (Amazon S3).
            location (string) --Information about the build output artifact location:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , this is the name of the output bucket.
            path (string) --Along with namespaceType and name , the pattern that AWS CodeBuild uses to name and store the output artifact:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , this is the path to the output artifact. If path is not specified, path is not used.
            For example, if path is set to MyArtifacts , namespaceType is set to NONE , and name is set to MyArtifact.zip , the output artifact is stored in the output bucket at MyArtifacts/MyArtifact.zip .
            namespaceType (string) --Along with path and name , the pattern that AWS CodeBuild uses to determine the name and location to store the output artifact:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , valid values include:
            BUILD_ID : Include the build ID in the location of the build output artifact.
            NONE : Do not include the build ID. This is the default if namespaceType is not specified.
            For example, if path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .
            name (string) --Along with path and namespaceType , the pattern that AWS CodeBuild uses to name and store the output artifact:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , this is the name of the output artifact object. If you set the name to be a forward slash ('/'), the artifact is stored in the root of the output bucket.
            For example:
            If path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , then the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .
            If path is empty, namespaceType is set to NONE , and name is set to '/ ', the output artifact is stored in the root of the output bucket.
            If path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to '/ ', the output artifact is stored in ``MyArtifacts/build-ID `` .
            packaging (string) --The type of build output artifact to create:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , valid values include:
            NONE : AWS CodeBuild creates in the output bucket a folder that contains the build output. This is the default if packaging is not specified.
            ZIP : AWS CodeBuild creates in the output bucket a ZIP file that contains the build output.
            
            overrideArtifactName (boolean) --If this flag is set, a name specified in the build spec file overrides the artifact name. The name specified in a build spec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.
            encryptionDisabled (boolean) --Set to true if you do not want your output artifacts encrypted. This option is valid only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with another artifacts type, an invalidInputException is thrown.
            artifactIdentifier (string) --An identifier for this artifact definition.
            

    :type secondaryArtifacts: list
    :param secondaryArtifacts: An array of ProjectArtifacts objects.
            (dict) --Information about the build output artifacts for the build project.
            type (string) -- [REQUIRED]The type of build output artifact. Valid values include:
            CODEPIPELINE : The build project has build output generated through AWS CodePipeline.
            NO_ARTIFACTS : The build project does not produce any build output.
            S3 : The build project stores build output in Amazon Simple Storage Service (Amazon S3).
            location (string) --Information about the build output artifact location:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , this is the name of the output bucket.
            path (string) --Along with namespaceType and name , the pattern that AWS CodeBuild uses to name and store the output artifact:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , this is the path to the output artifact. If path is not specified, path is not used.
            For example, if path is set to MyArtifacts , namespaceType is set to NONE , and name is set to MyArtifact.zip , the output artifact is stored in the output bucket at MyArtifacts/MyArtifact.zip .
            namespaceType (string) --Along with path and name , the pattern that AWS CodeBuild uses to determine the name and location to store the output artifact:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , valid values include:
            BUILD_ID : Include the build ID in the location of the build output artifact.
            NONE : Do not include the build ID. This is the default if namespaceType is not specified.
            For example, if path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .
            name (string) --Along with path and namespaceType , the pattern that AWS CodeBuild uses to name and store the output artifact:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , this is the name of the output artifact object. If you set the name to be a forward slash ('/'), the artifact is stored in the root of the output bucket.
            For example:
            If path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , then the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .
            If path is empty, namespaceType is set to NONE , and name is set to '/ ', the output artifact is stored in the root of the output bucket.
            If path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to '/ ', the output artifact is stored in ``MyArtifacts/build-ID `` .
            packaging (string) --The type of build output artifact to create:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , valid values include:
            NONE : AWS CodeBuild creates in the output bucket a folder that contains the build output. This is the default if packaging is not specified.
            ZIP : AWS CodeBuild creates in the output bucket a ZIP file that contains the build output.
            
            overrideArtifactName (boolean) --If this flag is set, a name specified in the build spec file overrides the artifact name. The name specified in a build spec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.
            encryptionDisabled (boolean) --Set to true if you do not want your output artifacts encrypted. This option is valid only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with another artifacts type, an invalidInputException is thrown.
            artifactIdentifier (string) --An identifier for this artifact definition.
            
            

    :type cache: dict
    :param cache: Stores recently used information so that it can be quickly accessed at a later time.
            type (string) -- [REQUIRED]The type of cache used by the build project. Valid values include:
            NO_CACHE : The build project does not use any cache.
            S3 : The build project reads and writes from and to S3.
            location (string) --Information about the cache location:
            NO_CACHE : This value is ignored.
            S3 : This is the S3 bucket name/prefix.
            

    :type environment: dict
    :param environment: [REQUIRED]
            Information about the build environment for the build project.
            type (string) -- [REQUIRED]The type of build environment to use for related builds.
            image (string) -- [REQUIRED]The ID of the Docker image to use for this build project.
            computeType (string) -- [REQUIRED]Information about the compute resources the build project uses. Available values include:
            BUILD_GENERAL1_SMALL : Use up to 3 GB memory and 2 vCPUs for builds.
            BUILD_GENERAL1_MEDIUM : Use up to 7 GB memory and 4 vCPUs for builds.
            BUILD_GENERAL1_LARGE : Use up to 15 GB memory and 8 vCPUs for builds.
            environmentVariables (list) --A set of environment variables to make available to builds for this build project.
            (dict) --Information about an environment variable for a build project or a build.
            name (string) -- [REQUIRED]The name or key of the environment variable.
            value (string) -- [REQUIRED]The value of the environment variable.
            Warning
            We strongly discourage the use of environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. Environment variables can be displayed in plain text using the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI).
            type (string) --The type of environment variable. Valid values include:
            PARAMETER_STORE : An environment variable stored in Amazon EC2 Systems Manager Parameter Store.
            PLAINTEXT : An environment variable in plaintext format.
            
            privilegedMode (boolean) --Enables running the Docker daemon inside a Docker container. Set to true only if the build project is be used to build Docker images, and the specified build environment image is not provided by AWS CodeBuild with Docker support. Otherwise, all associated builds that attempt to interact with the Docker daemon fail. You must also start the Docker daemon so that builds can interact with it. One way to do this is to initialize the Docker daemon during the install phase of your build spec by running the following build commands. (Do not run these commands if the specified build environment image is provided by AWS CodeBuild with Docker support.)
            If the operating system's base image is Ubuntu Linux:
            - nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout 15 sh -c 'until docker info; do echo .; sleep 1; done'
            If the operating system's base image is Alpine Linux, add the -t argument to timeout :
            - nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout 15 -t sh -c 'until docker info; do echo .; sleep 1; done'
            certificate (string) --The certificate to use with this build project.
            

    :type serviceRole: string
    :param serviceRole: [REQUIRED]
            The ARN of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
            

    :type timeoutInMinutes: integer
    :param timeoutInMinutes: How long, in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait before it times out any build that has not been marked as completed. The default is 60 minutes.

    :type queuedTimeoutInMinutes: integer
    :param queuedTimeoutInMinutes: The number of minutes a build is allowed to be queued before it times out.

    :type encryptionKey: string
    :param encryptionKey: The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build output artifacts.
            You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK's alias (using the format ``alias/alias-name `` ).
            

    :type tags: list
    :param tags: A set of tags for this build project.
            These tags are available for use by AWS services that support AWS CodeBuild build project tags.
            (dict) --A tag, consisting of a key and a value.
            This tag is available for use by AWS services that support tags in AWS CodeBuild.
            key (string) --The tag's key.
            value (string) --The tag's value.
            
            

    :type vpcConfig: dict
    :param vpcConfig: VpcConfig enables AWS CodeBuild to access resources in an Amazon VPC.
            vpcId (string) --The ID of the Amazon VPC.
            subnets (list) --A list of one or more subnet IDs in your Amazon VPC.
            (string) --
            securityGroupIds (list) --A list of one or more security groups IDs in your Amazon VPC.
            (string) --
            

    :type badgeEnabled: boolean
    :param badgeEnabled: Set this to true to generate a publicly accessible URL for your project's build badge.

    :type logsConfig: dict
    :param logsConfig: Information about logs for the build project. These can be logs in Amazon CloudWatch Logs, logs uploaded to a specified S3 bucket, or both.
            cloudWatchLogs (dict) --Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are enabled by default.
            status (string) -- [REQUIRED]The current status of the logs in Amazon CloudWatch Logs for a build project. Valid values are:
            ENABLED : Amazon CloudWatch Logs are enabled for this build project.
            DISABLED : Amazon CloudWatch Logs are not enabled for this build project.
            groupName (string) --The group name of the logs in Amazon CloudWatch Logs. For more information, see Working with Log Groups and Log Streams .
            streamName (string) --The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see Working with Log Groups and Log Streams .
            s3Logs (dict) --Information about logs built to an S3 bucket for a build project. S3 logs are not enabled by default.
            status (string) -- [REQUIRED]The current status of the S3 build logs. Valid values are:
            ENABLED : S3 build logs are enabled for this build project.
            DISABLED : S3 build logs are not enabled for this build project.
            location (string) --The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is my-bucket , and your path prefix is build-log , then acceptable formats are my-bucket/build-log or arn:aws:s3:::my-bucket/build-log .
            
            

    :rtype: dict
    :return: {
        'project': {
            'name': 'string',
            'arn': 'string',
            'description': 'string',
            'source': {
                'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                'location': 'string',
                'gitCloneDepth': 123,
                'buildspec': 'string',
                'auth': {
                    'type': 'OAUTH',
                    'resource': 'string'
                },
                'reportBuildStatus': True|False,
                'insecureSsl': True|False,
                'sourceIdentifier': 'string'
            },
            'secondarySources': [
                {
                    'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                    'location': 'string',
                    'gitCloneDepth': 123,
                    'buildspec': 'string',
                    'auth': {
                        'type': 'OAUTH',
                        'resource': 'string'
                    },
                    'reportBuildStatus': True|False,
                    'insecureSsl': True|False,
                    'sourceIdentifier': 'string'
                },
            ],
            'artifacts': {
                'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                'location': 'string',
                'path': 'string',
                'namespaceType': 'NONE'|'BUILD_ID',
                'name': 'string',
                'packaging': 'NONE'|'ZIP',
                'overrideArtifactName': True|False,
                'encryptionDisabled': True|False,
                'artifactIdentifier': 'string'
            },
            'secondaryArtifacts': [
                {
                    'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                    'location': 'string',
                    'path': 'string',
                    'namespaceType': 'NONE'|'BUILD_ID',
                    'name': 'string',
                    'packaging': 'NONE'|'ZIP',
                    'overrideArtifactName': True|False,
                    'encryptionDisabled': True|False,
                    'artifactIdentifier': 'string'
                },
            ],
            'cache': {
                'type': 'NO_CACHE'|'S3',
                'location': 'string'
            },
            'environment': {
                'type': 'WINDOWS_CONTAINER'|'LINUX_CONTAINER',
                'image': 'string',
                'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE',
                'environmentVariables': [
                    {
                        'name': 'string',
                        'value': 'string',
                        'type': 'PLAINTEXT'|'PARAMETER_STORE'
                    },
                ],
                'privilegedMode': True|False,
                'certificate': 'string'
            },
            'serviceRole': 'string',
            'timeoutInMinutes': 123,
            'queuedTimeoutInMinutes': 123,
            'encryptionKey': 'string',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'created': datetime(2015, 1, 1),
            'lastModified': datetime(2015, 1, 1),
            'webhook': {
                'url': 'string',
                'payloadUrl': 'string',
                'secret': 'string',
                'branchFilter': 'string',
                'lastModifiedSecret': datetime(2015, 1, 1)
            },
            'vpcConfig': {
                'vpcId': 'string',
                'subnets': [
                    'string',
                ],
                'securityGroupIds': [
                    'string',
                ]
            },
            'badge': {
                'badgeEnabled': True|False,
                'badgeRequestUrl': 'string'
            },
            'logsConfig': {
                'cloudWatchLogs': {
                    'status': 'ENABLED'|'DISABLED',
                    'groupName': 'string',
                    'streamName': 'string'
                },
                's3Logs': {
                    'status': 'ENABLED'|'DISABLED',
                    'location': 'string'
                }
            }
        }
    }
    
    
    :returns: 
    BITBUCKET : The source code is in a Bitbucket repository.
    CODECOMMIT : The source code is in an AWS CodeCommit repository.
    CODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.
    GITHUB : The source code is in a GitHub repository.
    NO_SOURCE : The project does not have input source code.
    S3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.
    
    """
    pass

def create_webhook(projectName=None, branchFilter=None):
    """
    For an existing AWS CodeBuild build project that has its source code stored in a GitHub or Bitbucket repository, enables AWS CodeBuild to start rebuilding the source code every time a code change is pushed to the repository.
    See also: AWS API Documentation
    
    
    :example: response = client.create_webhook(
        projectName='string',
        branchFilter='string'
    )
    
    
    :type projectName: string
    :param projectName: [REQUIRED]
            The name of the AWS CodeBuild project.
            

    :type branchFilter: string
    :param branchFilter: A regular expression used to determine which repository branches are built when a webhook is triggered. If the name of a branch matches the regular expression, then it is built. If branchFilter is empty, then all branches are built.

    :rtype: dict
    :return: {
        'webhook': {
            'url': 'string',
            'payloadUrl': 'string',
            'secret': 'string',
            'branchFilter': 'string',
            'lastModifiedSecret': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def delete_project(name=None):
    """
    Deletes a build project.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_project(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the build project.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_source_credentials(arn=None):
    """
    Deletes a set of GitHub, GitHub Enterprise, or Bitbucket source credentials.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_source_credentials(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the token.
            

    :rtype: dict
    :return: {
        'arn': 'string'
    }
    
    
    """
    pass

def delete_webhook(projectName=None):
    """
    For an existing AWS CodeBuild build project that has its source code stored in a GitHub or Bitbucket repository, stops AWS CodeBuild from rebuilding the source code every time a code change is pushed to the repository.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_webhook(
        projectName='string'
    )
    
    
    :type projectName: string
    :param projectName: [REQUIRED]
            The name of the AWS CodeBuild project.
            

    :rtype: dict
    :return: {}
    
    
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

def import_source_credentials(username=None, token=None, serverType=None, authType=None):
    """
    Imports the source repository credentials for an AWS CodeBuild project that has its source code stored in a GitHub, GitHub Enterprise, or Bitbucket repository.
    See also: AWS API Documentation
    
    
    :example: response = client.import_source_credentials(
        username='string',
        token='string',
        serverType='GITHUB'|'BITBUCKET'|'GITHUB_ENTERPRISE',
        authType='OAUTH'|'BASIC_AUTH'|'PERSONAL_ACCESS_TOKEN'
    )
    
    
    :type username: string
    :param username: The Bitbucket username when the authType is BASIC_AUTH. This parameter is not valid for other types of source providers or connections.

    :type token: string
    :param token: [REQUIRED]
            For GitHub or GitHub Enterprise, this is the personal access token. For Bitbucket, this is the app password.
            

    :type serverType: string
    :param serverType: [REQUIRED]
            The source provider used for this project.
            

    :type authType: string
    :param authType: [REQUIRED]
            The type of authentication used to connect to a GitHub, GitHub Enterprise, or Bitbucket repository. An OAUTH connection is not supported by the API and must be created using the AWS CodeBuild console.
            

    :rtype: dict
    :return: {
        'arn': 'string'
    }
    
    
    """
    pass

def invalidate_project_cache(projectName=None):
    """
    Resets the cache for a project.
    See also: AWS API Documentation
    
    
    :example: response = client.invalidate_project_cache(
        projectName='string'
    )
    
    
    :type projectName: string
    :param projectName: [REQUIRED]
            The name of the AWS CodeBuild build project that the cache is reset for.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def list_builds(sortOrder=None, nextToken=None):
    """
    Gets a list of build IDs, with each build ID representing a single build.
    See also: AWS API Documentation
    
    
    :example: response = client.list_builds(
        sortOrder='ASCENDING'|'DESCENDING',
        nextToken='string'
    )
    
    
    :type sortOrder: string
    :param sortOrder: The order to list build IDs. Valid values include:
            ASCENDING : List the build IDs in ascending order by build ID.
            DESCENDING : List the build IDs in descending order by build ID.
            

    :type nextToken: string
    :param nextToken: During a previous call, if there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a next token . To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.

    :rtype: dict
    :return: {
        'ids': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_builds_for_project(projectName=None, sortOrder=None, nextToken=None):
    """
    Gets a list of build IDs for the specified build project, with each build ID representing a single build.
    See also: AWS API Documentation
    
    
    :example: response = client.list_builds_for_project(
        projectName='string',
        sortOrder='ASCENDING'|'DESCENDING',
        nextToken='string'
    )
    
    
    :type projectName: string
    :param projectName: [REQUIRED]
            The name of the AWS CodeBuild project.
            

    :type sortOrder: string
    :param sortOrder: The order to list build IDs. Valid values include:
            ASCENDING : List the build IDs in ascending order by build ID.
            DESCENDING : List the build IDs in descending order by build ID.
            

    :type nextToken: string
    :param nextToken: During a previous call, if there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a next token . To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.

    :rtype: dict
    :return: {
        'ids': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_curated_environment_images():
    """
    Gets information about Docker images that are managed by AWS CodeBuild.
    See also: AWS API Documentation
    
    
    :example: response = client.list_curated_environment_images()
    
    
    :rtype: dict
    :return: {
        'platforms': [
            {
                'platform': 'DEBIAN'|'AMAZON_LINUX'|'UBUNTU'|'WINDOWS_SERVER',
                'languages': [
                    {
                        'language': 'JAVA'|'PYTHON'|'NODE_JS'|'RUBY'|'GOLANG'|'DOCKER'|'ANDROID'|'DOTNET'|'BASE'|'PHP',
                        'images': [
                            {
                                'name': 'string',
                                'description': 'string',
                                'versions': [
                                    'string',
                                ]
                            },
                        ]
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def list_projects(sortBy=None, sortOrder=None, nextToken=None):
    """
    Gets a list of build project names, with each build project name representing a single build project.
    See also: AWS API Documentation
    
    
    :example: response = client.list_projects(
        sortBy='NAME'|'CREATED_TIME'|'LAST_MODIFIED_TIME',
        sortOrder='ASCENDING'|'DESCENDING',
        nextToken='string'
    )
    
    
    :type sortBy: string
    :param sortBy: The criterion to be used to list build project names. Valid values include:
            CREATED_TIME : List based on when each build project was created.
            LAST_MODIFIED_TIME : List based on when information about each build project was last changed.
            NAME : List based on each build project's name.
            Use sortOrder to specify in what order to list the build project names based on the preceding criteria.
            

    :type sortOrder: string
    :param sortOrder: The order in which to list build projects. Valid values include:
            ASCENDING : List in ascending order.
            DESCENDING : List in descending order.
            Use sortBy to specify the criterion to be used to list build project names.
            

    :type nextToken: string
    :param nextToken: During a previous call, if there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a next token . To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.

    :rtype: dict
    :return: {
        'nextToken': 'string',
        'projects': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_source_credentials():
    """
    Returns a list of SourceCredentialsInfo objects.
    See also: AWS API Documentation
    
    
    :example: response = client.list_source_credentials()
    
    
    :rtype: dict
    :return: {
        'sourceCredentialsInfos': [
            {
                'arn': 'string',
                'serverType': 'GITHUB'|'BITBUCKET'|'GITHUB_ENTERPRISE',
                'authType': 'OAUTH'|'BASIC_AUTH'|'PERSONAL_ACCESS_TOKEN'
            },
        ]
    }
    
    
    """
    pass

def start_build(projectName=None, secondarySourcesOverride=None, secondarySourcesVersionOverride=None, sourceVersion=None, artifactsOverride=None, secondaryArtifactsOverride=None, environmentVariablesOverride=None, sourceTypeOverride=None, sourceLocationOverride=None, sourceAuthOverride=None, gitCloneDepthOverride=None, buildspecOverride=None, insecureSslOverride=None, reportBuildStatusOverride=None, environmentTypeOverride=None, imageOverride=None, computeTypeOverride=None, certificateOverride=None, cacheOverride=None, serviceRoleOverride=None, privilegedModeOverride=None, timeoutInMinutesOverride=None, queuedTimeoutInMinutesOverride=None, idempotencyToken=None, logsConfigOverride=None):
    """
    Starts running a build.
    See also: AWS API Documentation
    
    
    :example: response = client.start_build(
        projectName='string',
        secondarySourcesOverride=[
            {
                'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                'location': 'string',
                'gitCloneDepth': 123,
                'buildspec': 'string',
                'auth': {
                    'type': 'OAUTH',
                    'resource': 'string'
                },
                'reportBuildStatus': True|False,
                'insecureSsl': True|False,
                'sourceIdentifier': 'string'
            },
        ],
        secondarySourcesVersionOverride=[
            {
                'sourceIdentifier': 'string',
                'sourceVersion': 'string'
            },
        ],
        sourceVersion='string',
        artifactsOverride={
            'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
            'location': 'string',
            'path': 'string',
            'namespaceType': 'NONE'|'BUILD_ID',
            'name': 'string',
            'packaging': 'NONE'|'ZIP',
            'overrideArtifactName': True|False,
            'encryptionDisabled': True|False,
            'artifactIdentifier': 'string'
        },
        secondaryArtifactsOverride=[
            {
                'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                'location': 'string',
                'path': 'string',
                'namespaceType': 'NONE'|'BUILD_ID',
                'name': 'string',
                'packaging': 'NONE'|'ZIP',
                'overrideArtifactName': True|False,
                'encryptionDisabled': True|False,
                'artifactIdentifier': 'string'
            },
        ],
        environmentVariablesOverride=[
            {
                'name': 'string',
                'value': 'string',
                'type': 'PLAINTEXT'|'PARAMETER_STORE'
            },
        ],
        sourceTypeOverride='CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
        sourceLocationOverride='string',
        sourceAuthOverride={
            'type': 'OAUTH',
            'resource': 'string'
        },
        gitCloneDepthOverride=123,
        buildspecOverride='string',
        insecureSslOverride=True|False,
        reportBuildStatusOverride=True|False,
        environmentTypeOverride='WINDOWS_CONTAINER'|'LINUX_CONTAINER',
        imageOverride='string',
        computeTypeOverride='BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE',
        certificateOverride='string',
        cacheOverride={
            'type': 'NO_CACHE'|'S3',
            'location': 'string'
        },
        serviceRoleOverride='string',
        privilegedModeOverride=True|False,
        timeoutInMinutesOverride=123,
        queuedTimeoutInMinutesOverride=123,
        idempotencyToken='string',
        logsConfigOverride={
            'cloudWatchLogs': {
                'status': 'ENABLED'|'DISABLED',
                'groupName': 'string',
                'streamName': 'string'
            },
            's3Logs': {
                'status': 'ENABLED'|'DISABLED',
                'location': 'string'
            }
        }
    )
    
    
    :type projectName: string
    :param projectName: [REQUIRED]
            The name of the AWS CodeBuild build project to start running a build.
            

    :type secondarySourcesOverride: list
    :param secondarySourcesOverride: An array of ProjectSource objects.
            (dict) --Information about the build input source code for the build project.
            type (string) -- [REQUIRED]The type of repository that contains the source code to be built. Valid values include:
            BITBUCKET : The source code is in a Bitbucket repository.
            CODECOMMIT : The source code is in an AWS CodeCommit repository.
            CODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.
            GITHUB : The source code is in a GitHub repository.
            NO_SOURCE : The project does not have input source code.
            S3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.
            location (string) --Information about the location of the source code to be built. Valid values include:
            For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, location should not be specified. If it is specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a pipeline's source action instead of this value.
            For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/repo-name `` ).
            For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.
            The path to the ZIP file that contains the source code (for example, `` bucket-name /path /to /object-name .zip`` ).
            The path to the folder that contains the source code (for example, `` bucket-name /path /to /source-code /folder /`` ).
            For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. You must connect your AWS account to your GitHub account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub Authorize application page, for Organization access , choose Request access next to each repository you want to allow AWS CodeBuild to have access to, and then choose Authorize application . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object's type value to OAUTH .
            For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. You must connect your AWS account to your Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket Confirm access to your account page, choose Grant access . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object's type value to OAUTH .
            gitCloneDepth (integer) --Information about the git clone depth for the build project.
            buildspec (string) --The build spec declaration to use for the builds in this build project.
            If this value is not specified, a build spec must be included along with the source code to be built.
            auth (dict) --Information about the authorization settings for AWS CodeBuild to access the source code to be built.
            This information is for the AWS CodeBuild console's use only. Your code should not get or set this information directly.
            type (string) -- [REQUIRED]
            Note
            This data type is deprecated and is no longer accurate or used.
            The authorization type to use. The only valid value is OAUTH , which represents the OAuth authorization type.
            resource (string) --The resource value that applies to the specified authorization type.
            reportBuildStatus (boolean) --Set to true to report the status of a build's start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown.
            insecureSsl (boolean) --Enable this flag to ignore SSL warnings while connecting to the project source code.
            sourceIdentifier (string) --An identifier for this project source.
            
            

    :type secondarySourcesVersionOverride: list
    :param secondarySourcesVersionOverride: An array of ProjectSourceVersion objects that specify one or more versions of the project's secondary sources to be used for this build only.
            (dict) --A source identifier and its corresponding version.
            sourceIdentifier (string) -- [REQUIRED]An identifier for a source in the build project.
            sourceVersion (string) -- [REQUIRED]The source version for the corresponding source identifier. If specified, must be one of:
            For AWS CodeCommit: the commit ID to use.
            For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format pr/pull-request-ID (for example, pr/25 ). If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.
            For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.
            For Amazon Simple Storage Service (Amazon S3): the version ID of the object that represents the build input ZIP file to use.
            
            

    :type sourceVersion: string
    :param sourceVersion: A version of the build input to be built, for this build only. If not specified, the latest version is used. If specified, must be one of:
            For AWS CodeCommit: the commit ID to use.
            For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format pr/pull-request-ID (for example pr/25 ). If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.
            For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.
            For Amazon Simple Storage Service (Amazon S3): the version ID of the object that represents the build input ZIP file to use.
            

    :type artifactsOverride: dict
    :param artifactsOverride: Build output artifact settings that override, for this build only, the latest ones already defined in the build project.
            type (string) -- [REQUIRED]The type of build output artifact. Valid values include:
            CODEPIPELINE : The build project has build output generated through AWS CodePipeline.
            NO_ARTIFACTS : The build project does not produce any build output.
            S3 : The build project stores build output in Amazon Simple Storage Service (Amazon S3).
            location (string) --Information about the build output artifact location:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , this is the name of the output bucket.
            path (string) --Along with namespaceType and name , the pattern that AWS CodeBuild uses to name and store the output artifact:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , this is the path to the output artifact. If path is not specified, path is not used.
            For example, if path is set to MyArtifacts , namespaceType is set to NONE , and name is set to MyArtifact.zip , the output artifact is stored in the output bucket at MyArtifacts/MyArtifact.zip .
            namespaceType (string) --Along with path and name , the pattern that AWS CodeBuild uses to determine the name and location to store the output artifact:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , valid values include:
            BUILD_ID : Include the build ID in the location of the build output artifact.
            NONE : Do not include the build ID. This is the default if namespaceType is not specified.
            For example, if path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .
            name (string) --Along with path and namespaceType , the pattern that AWS CodeBuild uses to name and store the output artifact:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , this is the name of the output artifact object. If you set the name to be a forward slash ('/'), the artifact is stored in the root of the output bucket.
            For example:
            If path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , then the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .
            If path is empty, namespaceType is set to NONE , and name is set to '/ ', the output artifact is stored in the root of the output bucket.
            If path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to '/ ', the output artifact is stored in ``MyArtifacts/build-ID `` .
            packaging (string) --The type of build output artifact to create:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , valid values include:
            NONE : AWS CodeBuild creates in the output bucket a folder that contains the build output. This is the default if packaging is not specified.
            ZIP : AWS CodeBuild creates in the output bucket a ZIP file that contains the build output.
            
            overrideArtifactName (boolean) --If this flag is set, a name specified in the build spec file overrides the artifact name. The name specified in a build spec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.
            encryptionDisabled (boolean) --Set to true if you do not want your output artifacts encrypted. This option is valid only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with another artifacts type, an invalidInputException is thrown.
            artifactIdentifier (string) --An identifier for this artifact definition.
            

    :type secondaryArtifactsOverride: list
    :param secondaryArtifactsOverride: An array of ProjectArtifacts objects.
            (dict) --Information about the build output artifacts for the build project.
            type (string) -- [REQUIRED]The type of build output artifact. Valid values include:
            CODEPIPELINE : The build project has build output generated through AWS CodePipeline.
            NO_ARTIFACTS : The build project does not produce any build output.
            S3 : The build project stores build output in Amazon Simple Storage Service (Amazon S3).
            location (string) --Information about the build output artifact location:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , this is the name of the output bucket.
            path (string) --Along with namespaceType and name , the pattern that AWS CodeBuild uses to name and store the output artifact:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , this is the path to the output artifact. If path is not specified, path is not used.
            For example, if path is set to MyArtifacts , namespaceType is set to NONE , and name is set to MyArtifact.zip , the output artifact is stored in the output bucket at MyArtifacts/MyArtifact.zip .
            namespaceType (string) --Along with path and name , the pattern that AWS CodeBuild uses to determine the name and location to store the output artifact:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , valid values include:
            BUILD_ID : Include the build ID in the location of the build output artifact.
            NONE : Do not include the build ID. This is the default if namespaceType is not specified.
            For example, if path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .
            name (string) --Along with path and namespaceType , the pattern that AWS CodeBuild uses to name and store the output artifact:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , this is the name of the output artifact object. If you set the name to be a forward slash ('/'), the artifact is stored in the root of the output bucket.
            For example:
            If path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , then the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .
            If path is empty, namespaceType is set to NONE , and name is set to '/ ', the output artifact is stored in the root of the output bucket.
            If path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to '/ ', the output artifact is stored in ``MyArtifacts/build-ID `` .
            packaging (string) --The type of build output artifact to create:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , valid values include:
            NONE : AWS CodeBuild creates in the output bucket a folder that contains the build output. This is the default if packaging is not specified.
            ZIP : AWS CodeBuild creates in the output bucket a ZIP file that contains the build output.
            
            overrideArtifactName (boolean) --If this flag is set, a name specified in the build spec file overrides the artifact name. The name specified in a build spec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.
            encryptionDisabled (boolean) --Set to true if you do not want your output artifacts encrypted. This option is valid only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with another artifacts type, an invalidInputException is thrown.
            artifactIdentifier (string) --An identifier for this artifact definition.
            
            

    :type environmentVariablesOverride: list
    :param environmentVariablesOverride: A set of environment variables that overrides, for this build only, the latest ones already defined in the build project.
            (dict) --Information about an environment variable for a build project or a build.
            name (string) -- [REQUIRED]The name or key of the environment variable.
            value (string) -- [REQUIRED]The value of the environment variable.
            Warning
            We strongly discourage the use of environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. Environment variables can be displayed in plain text using the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI).
            type (string) --The type of environment variable. Valid values include:
            PARAMETER_STORE : An environment variable stored in Amazon EC2 Systems Manager Parameter Store.
            PLAINTEXT : An environment variable in plaintext format.
            
            

    :type sourceTypeOverride: string
    :param sourceTypeOverride: A source input type, for this build, that overrides the source input defined in the build project.

    :type sourceLocationOverride: string
    :param sourceLocationOverride: A location that overrides, for this build, the source location for the one defined in the build project.

    :type sourceAuthOverride: dict
    :param sourceAuthOverride: An authorization type for this build that overrides the one defined in the build project. This override applies only if the build project's source is BitBucket or GitHub.
            type (string) -- [REQUIRED]
            Note
            This data type is deprecated and is no longer accurate or used.
            The authorization type to use. The only valid value is OAUTH , which represents the OAuth authorization type.
            resource (string) --The resource value that applies to the specified authorization type.
            

    :type gitCloneDepthOverride: integer
    :param gitCloneDepthOverride: The user-defined depth of history, with a minimum value of 0, that overrides, for this build only, any previous depth of history defined in the build project.

    :type buildspecOverride: string
    :param buildspecOverride: A build spec declaration that overrides, for this build only, the latest one already defined in the build project.

    :type insecureSslOverride: boolean
    :param insecureSslOverride: Enable this flag to override the insecure SSL setting that is specified in the build project. The insecure SSL setting determines whether to ignore SSL warnings while connecting to the project source code. This override applies only if the build's source is GitHub Enterprise.

    :type reportBuildStatusOverride: boolean
    :param reportBuildStatusOverride: Set to true to report to your source provider the status of a build's start and completion. If you use this option with a source provider other than GitHub, GitHub Enterprise, or Bitbucket, an invalidInputException is thrown.

    :type environmentTypeOverride: string
    :param environmentTypeOverride: A container type for this build that overrides the one specified in the build project.

    :type imageOverride: string
    :param imageOverride: The name of an image for this build that overrides the one specified in the build project.

    :type computeTypeOverride: string
    :param computeTypeOverride: The name of a compute type for this build that overrides the one specified in the build project.

    :type certificateOverride: string
    :param certificateOverride: The name of a certificate for this build that overrides the one specified in the build project.

    :type cacheOverride: dict
    :param cacheOverride: A ProjectCache object specified for this build that overrides the one defined in the build project.
            type (string) -- [REQUIRED]The type of cache used by the build project. Valid values include:
            NO_CACHE : The build project does not use any cache.
            S3 : The build project reads and writes from and to S3.
            location (string) --Information about the cache location:
            NO_CACHE : This value is ignored.
            S3 : This is the S3 bucket name/prefix.
            

    :type serviceRoleOverride: string
    :param serviceRoleOverride: The name of a service role for this build that overrides the one specified in the build project.

    :type privilegedModeOverride: boolean
    :param privilegedModeOverride: Enable this flag to override privileged mode in the build project.

    :type timeoutInMinutesOverride: integer
    :param timeoutInMinutesOverride: The number of build timeout minutes, from 5 to 480 (8 hours), that overrides, for this build only, the latest setting already defined in the build project.

    :type queuedTimeoutInMinutesOverride: integer
    :param queuedTimeoutInMinutesOverride: The number of minutes a build is allowed to be queued before it times out.

    :type idempotencyToken: string
    :param idempotencyToken: A unique, case sensitive identifier you provide to ensure the idempotency of the StartBuild request. The token is included in the StartBuild request and is valid for 12 hours. If you repeat the StartBuild request with the same token, but change a parameter, AWS CodeBuild returns a parameter mismatch error.

    :type logsConfigOverride: dict
    :param logsConfigOverride: Log settings for this build that override the log settings defined in the build project.
            cloudWatchLogs (dict) --Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are enabled by default.
            status (string) -- [REQUIRED]The current status of the logs in Amazon CloudWatch Logs for a build project. Valid values are:
            ENABLED : Amazon CloudWatch Logs are enabled for this build project.
            DISABLED : Amazon CloudWatch Logs are not enabled for this build project.
            groupName (string) --The group name of the logs in Amazon CloudWatch Logs. For more information, see Working with Log Groups and Log Streams .
            streamName (string) --The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see Working with Log Groups and Log Streams .
            s3Logs (dict) --Information about logs built to an S3 bucket for a build project. S3 logs are not enabled by default.
            status (string) -- [REQUIRED]The current status of the S3 build logs. Valid values are:
            ENABLED : S3 build logs are enabled for this build project.
            DISABLED : S3 build logs are not enabled for this build project.
            location (string) --The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is my-bucket , and your path prefix is build-log , then acceptable formats are my-bucket/build-log or arn:aws:s3:::my-bucket/build-log .
            
            

    :rtype: dict
    :return: {
        'build': {
            'id': 'string',
            'arn': 'string',
            'startTime': datetime(2015, 1, 1),
            'endTime': datetime(2015, 1, 1),
            'currentPhase': 'string',
            'buildStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',
            'sourceVersion': 'string',
            'resolvedSourceVersion': 'string',
            'projectName': 'string',
            'phases': [
                {
                    'phaseType': 'SUBMITTED'|'QUEUED'|'PROVISIONING'|'DOWNLOAD_SOURCE'|'INSTALL'|'PRE_BUILD'|'BUILD'|'POST_BUILD'|'UPLOAD_ARTIFACTS'|'FINALIZING'|'COMPLETED',
                    'phaseStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',
                    'startTime': datetime(2015, 1, 1),
                    'endTime': datetime(2015, 1, 1),
                    'durationInSeconds': 123,
                    'contexts': [
                        {
                            'statusCode': 'string',
                            'message': 'string'
                        },
                    ]
                },
            ],
            'source': {
                'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                'location': 'string',
                'gitCloneDepth': 123,
                'buildspec': 'string',
                'auth': {
                    'type': 'OAUTH',
                    'resource': 'string'
                },
                'reportBuildStatus': True|False,
                'insecureSsl': True|False,
                'sourceIdentifier': 'string'
            },
            'secondarySources': [
                {
                    'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                    'location': 'string',
                    'gitCloneDepth': 123,
                    'buildspec': 'string',
                    'auth': {
                        'type': 'OAUTH',
                        'resource': 'string'
                    },
                    'reportBuildStatus': True|False,
                    'insecureSsl': True|False,
                    'sourceIdentifier': 'string'
                },
            ],
            'secondarySourceVersions': [
                {
                    'sourceIdentifier': 'string',
                    'sourceVersion': 'string'
                },
            ],
            'artifacts': {
                'location': 'string',
                'sha256sum': 'string',
                'md5sum': 'string',
                'overrideArtifactName': True|False,
                'encryptionDisabled': True|False,
                'artifactIdentifier': 'string'
            },
            'secondaryArtifacts': [
                {
                    'location': 'string',
                    'sha256sum': 'string',
                    'md5sum': 'string',
                    'overrideArtifactName': True|False,
                    'encryptionDisabled': True|False,
                    'artifactIdentifier': 'string'
                },
            ],
            'cache': {
                'type': 'NO_CACHE'|'S3',
                'location': 'string'
            },
            'environment': {
                'type': 'WINDOWS_CONTAINER'|'LINUX_CONTAINER',
                'image': 'string',
                'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE',
                'environmentVariables': [
                    {
                        'name': 'string',
                        'value': 'string',
                        'type': 'PLAINTEXT'|'PARAMETER_STORE'
                    },
                ],
                'privilegedMode': True|False,
                'certificate': 'string'
            },
            'serviceRole': 'string',
            'logs': {
                'groupName': 'string',
                'streamName': 'string',
                'deepLink': 'string',
                's3DeepLink': 'string',
                'cloudWatchLogs': {
                    'status': 'ENABLED'|'DISABLED',
                    'groupName': 'string',
                    'streamName': 'string'
                },
                's3Logs': {
                    'status': 'ENABLED'|'DISABLED',
                    'location': 'string'
                }
            },
            'timeoutInMinutes': 123,
            'queuedTimeoutInMinutes': 123,
            'buildComplete': True|False,
            'initiator': 'string',
            'vpcConfig': {
                'vpcId': 'string',
                'subnets': [
                    'string',
                ],
                'securityGroupIds': [
                    'string',
                ]
            },
            'networkInterface': {
                'subnetId': 'string',
                'networkInterfaceId': 'string'
            },
            'encryptionKey': 'string'
        }
    }
    
    
    :returns: 
    FAILED : The build failed.
    FAULT : The build faulted.
    IN_PROGRESS : The build is still in progress.
    STOPPED : The build stopped.
    SUCCEEDED : The build succeeded.
    TIMED_OUT : The build timed out.
    
    """
    pass

def stop_build(id=None):
    """
    Attempts to stop running a build.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_build(
        id='string'
    )
    
    
    :type id: string
    :param id: [REQUIRED]
            The ID of the build.
            

    :rtype: dict
    :return: {
        'build': {
            'id': 'string',
            'arn': 'string',
            'startTime': datetime(2015, 1, 1),
            'endTime': datetime(2015, 1, 1),
            'currentPhase': 'string',
            'buildStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',
            'sourceVersion': 'string',
            'resolvedSourceVersion': 'string',
            'projectName': 'string',
            'phases': [
                {
                    'phaseType': 'SUBMITTED'|'QUEUED'|'PROVISIONING'|'DOWNLOAD_SOURCE'|'INSTALL'|'PRE_BUILD'|'BUILD'|'POST_BUILD'|'UPLOAD_ARTIFACTS'|'FINALIZING'|'COMPLETED',
                    'phaseStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',
                    'startTime': datetime(2015, 1, 1),
                    'endTime': datetime(2015, 1, 1),
                    'durationInSeconds': 123,
                    'contexts': [
                        {
                            'statusCode': 'string',
                            'message': 'string'
                        },
                    ]
                },
            ],
            'source': {
                'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                'location': 'string',
                'gitCloneDepth': 123,
                'buildspec': 'string',
                'auth': {
                    'type': 'OAUTH',
                    'resource': 'string'
                },
                'reportBuildStatus': True|False,
                'insecureSsl': True|False,
                'sourceIdentifier': 'string'
            },
            'secondarySources': [
                {
                    'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                    'location': 'string',
                    'gitCloneDepth': 123,
                    'buildspec': 'string',
                    'auth': {
                        'type': 'OAUTH',
                        'resource': 'string'
                    },
                    'reportBuildStatus': True|False,
                    'insecureSsl': True|False,
                    'sourceIdentifier': 'string'
                },
            ],
            'secondarySourceVersions': [
                {
                    'sourceIdentifier': 'string',
                    'sourceVersion': 'string'
                },
            ],
            'artifacts': {
                'location': 'string',
                'sha256sum': 'string',
                'md5sum': 'string',
                'overrideArtifactName': True|False,
                'encryptionDisabled': True|False,
                'artifactIdentifier': 'string'
            },
            'secondaryArtifacts': [
                {
                    'location': 'string',
                    'sha256sum': 'string',
                    'md5sum': 'string',
                    'overrideArtifactName': True|False,
                    'encryptionDisabled': True|False,
                    'artifactIdentifier': 'string'
                },
            ],
            'cache': {
                'type': 'NO_CACHE'|'S3',
                'location': 'string'
            },
            'environment': {
                'type': 'WINDOWS_CONTAINER'|'LINUX_CONTAINER',
                'image': 'string',
                'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE',
                'environmentVariables': [
                    {
                        'name': 'string',
                        'value': 'string',
                        'type': 'PLAINTEXT'|'PARAMETER_STORE'
                    },
                ],
                'privilegedMode': True|False,
                'certificate': 'string'
            },
            'serviceRole': 'string',
            'logs': {
                'groupName': 'string',
                'streamName': 'string',
                'deepLink': 'string',
                's3DeepLink': 'string',
                'cloudWatchLogs': {
                    'status': 'ENABLED'|'DISABLED',
                    'groupName': 'string',
                    'streamName': 'string'
                },
                's3Logs': {
                    'status': 'ENABLED'|'DISABLED',
                    'location': 'string'
                }
            },
            'timeoutInMinutes': 123,
            'queuedTimeoutInMinutes': 123,
            'buildComplete': True|False,
            'initiator': 'string',
            'vpcConfig': {
                'vpcId': 'string',
                'subnets': [
                    'string',
                ],
                'securityGroupIds': [
                    'string',
                ]
            },
            'networkInterface': {
                'subnetId': 'string',
                'networkInterfaceId': 'string'
            },
            'encryptionKey': 'string'
        }
    }
    
    
    :returns: 
    For AWS CodeCommit, GitHub, GitHub Enterprise, and BitBucket, the commit ID.
    For AWS CodePipeline, the source revision provided by AWS CodePipeline.
    For Amazon Simple Storage Service (Amazon S3), this does not apply.
    
    """
    pass

def update_project(name=None, description=None, source=None, secondarySources=None, artifacts=None, secondaryArtifacts=None, cache=None, environment=None, serviceRole=None, timeoutInMinutes=None, queuedTimeoutInMinutes=None, encryptionKey=None, tags=None, vpcConfig=None, badgeEnabled=None, logsConfig=None):
    """
    Changes the settings of a build project.
    See also: AWS API Documentation
    
    
    :example: response = client.update_project(
        name='string',
        description='string',
        source={
            'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
            'location': 'string',
            'gitCloneDepth': 123,
            'buildspec': 'string',
            'auth': {
                'type': 'OAUTH',
                'resource': 'string'
            },
            'reportBuildStatus': True|False,
            'insecureSsl': True|False,
            'sourceIdentifier': 'string'
        },
        secondarySources=[
            {
                'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                'location': 'string',
                'gitCloneDepth': 123,
                'buildspec': 'string',
                'auth': {
                    'type': 'OAUTH',
                    'resource': 'string'
                },
                'reportBuildStatus': True|False,
                'insecureSsl': True|False,
                'sourceIdentifier': 'string'
            },
        ],
        artifacts={
            'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
            'location': 'string',
            'path': 'string',
            'namespaceType': 'NONE'|'BUILD_ID',
            'name': 'string',
            'packaging': 'NONE'|'ZIP',
            'overrideArtifactName': True|False,
            'encryptionDisabled': True|False,
            'artifactIdentifier': 'string'
        },
        secondaryArtifacts=[
            {
                'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                'location': 'string',
                'path': 'string',
                'namespaceType': 'NONE'|'BUILD_ID',
                'name': 'string',
                'packaging': 'NONE'|'ZIP',
                'overrideArtifactName': True|False,
                'encryptionDisabled': True|False,
                'artifactIdentifier': 'string'
            },
        ],
        cache={
            'type': 'NO_CACHE'|'S3',
            'location': 'string'
        },
        environment={
            'type': 'WINDOWS_CONTAINER'|'LINUX_CONTAINER',
            'image': 'string',
            'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE',
            'environmentVariables': [
                {
                    'name': 'string',
                    'value': 'string',
                    'type': 'PLAINTEXT'|'PARAMETER_STORE'
                },
            ],
            'privilegedMode': True|False,
            'certificate': 'string'
        },
        serviceRole='string',
        timeoutInMinutes=123,
        queuedTimeoutInMinutes=123,
        encryptionKey='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        vpcConfig={
            'vpcId': 'string',
            'subnets': [
                'string',
            ],
            'securityGroupIds': [
                'string',
            ]
        },
        badgeEnabled=True|False,
        logsConfig={
            'cloudWatchLogs': {
                'status': 'ENABLED'|'DISABLED',
                'groupName': 'string',
                'streamName': 'string'
            },
            's3Logs': {
                'status': 'ENABLED'|'DISABLED',
                'location': 'string'
            }
        }
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the build project.
            Note
            You cannot change a build project's name.
            

    :type description: string
    :param description: A new or replacement description of the build project.

    :type source: dict
    :param source: Information to be changed about the build input source code for the build project.
            type (string) -- [REQUIRED]The type of repository that contains the source code to be built. Valid values include:
            BITBUCKET : The source code is in a Bitbucket repository.
            CODECOMMIT : The source code is in an AWS CodeCommit repository.
            CODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.
            GITHUB : The source code is in a GitHub repository.
            NO_SOURCE : The project does not have input source code.
            S3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.
            location (string) --Information about the location of the source code to be built. Valid values include:
            For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, location should not be specified. If it is specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a pipeline's source action instead of this value.
            For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/repo-name `` ).
            For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.
            The path to the ZIP file that contains the source code (for example, `` bucket-name /path /to /object-name .zip`` ).
            The path to the folder that contains the source code (for example, `` bucket-name /path /to /source-code /folder /`` ).
            For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. You must connect your AWS account to your GitHub account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub Authorize application page, for Organization access , choose Request access next to each repository you want to allow AWS CodeBuild to have access to, and then choose Authorize application . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object's type value to OAUTH .
            For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. You must connect your AWS account to your Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket Confirm access to your account page, choose Grant access . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object's type value to OAUTH .
            gitCloneDepth (integer) --Information about the git clone depth for the build project.
            buildspec (string) --The build spec declaration to use for the builds in this build project.
            If this value is not specified, a build spec must be included along with the source code to be built.
            auth (dict) --Information about the authorization settings for AWS CodeBuild to access the source code to be built.
            This information is for the AWS CodeBuild console's use only. Your code should not get or set this information directly.
            type (string) -- [REQUIRED]
            Note
            This data type is deprecated and is no longer accurate or used.
            The authorization type to use. The only valid value is OAUTH , which represents the OAuth authorization type.
            resource (string) --The resource value that applies to the specified authorization type.
            reportBuildStatus (boolean) --Set to true to report the status of a build's start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown.
            insecureSsl (boolean) --Enable this flag to ignore SSL warnings while connecting to the project source code.
            sourceIdentifier (string) --An identifier for this project source.
            

    :type secondarySources: list
    :param secondarySources: An array of ProjectSource objects.
            (dict) --Information about the build input source code for the build project.
            type (string) -- [REQUIRED]The type of repository that contains the source code to be built. Valid values include:
            BITBUCKET : The source code is in a Bitbucket repository.
            CODECOMMIT : The source code is in an AWS CodeCommit repository.
            CODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.
            GITHUB : The source code is in a GitHub repository.
            NO_SOURCE : The project does not have input source code.
            S3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.
            location (string) --Information about the location of the source code to be built. Valid values include:
            For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, location should not be specified. If it is specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a pipeline's source action instead of this value.
            For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/repo-name `` ).
            For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.
            The path to the ZIP file that contains the source code (for example, `` bucket-name /path /to /object-name .zip`` ).
            The path to the folder that contains the source code (for example, `` bucket-name /path /to /source-code /folder /`` ).
            For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec. You must connect your AWS account to your GitHub account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub Authorize application page, for Organization access , choose Request access next to each repository you want to allow AWS CodeBuild to have access to, and then choose Authorize application . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object's type value to OAUTH .
            For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec. You must connect your AWS account to your Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket Confirm access to your account page, choose Grant access . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object's type value to OAUTH .
            gitCloneDepth (integer) --Information about the git clone depth for the build project.
            buildspec (string) --The build spec declaration to use for the builds in this build project.
            If this value is not specified, a build spec must be included along with the source code to be built.
            auth (dict) --Information about the authorization settings for AWS CodeBuild to access the source code to be built.
            This information is for the AWS CodeBuild console's use only. Your code should not get or set this information directly.
            type (string) -- [REQUIRED]
            Note
            This data type is deprecated and is no longer accurate or used.
            The authorization type to use. The only valid value is OAUTH , which represents the OAuth authorization type.
            resource (string) --The resource value that applies to the specified authorization type.
            reportBuildStatus (boolean) --Set to true to report the status of a build's start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown.
            insecureSsl (boolean) --Enable this flag to ignore SSL warnings while connecting to the project source code.
            sourceIdentifier (string) --An identifier for this project source.
            
            

    :type artifacts: dict
    :param artifacts: Information to be changed about the build output artifacts for the build project.
            type (string) -- [REQUIRED]The type of build output artifact. Valid values include:
            CODEPIPELINE : The build project has build output generated through AWS CodePipeline.
            NO_ARTIFACTS : The build project does not produce any build output.
            S3 : The build project stores build output in Amazon Simple Storage Service (Amazon S3).
            location (string) --Information about the build output artifact location:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , this is the name of the output bucket.
            path (string) --Along with namespaceType and name , the pattern that AWS CodeBuild uses to name and store the output artifact:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , this is the path to the output artifact. If path is not specified, path is not used.
            For example, if path is set to MyArtifacts , namespaceType is set to NONE , and name is set to MyArtifact.zip , the output artifact is stored in the output bucket at MyArtifacts/MyArtifact.zip .
            namespaceType (string) --Along with path and name , the pattern that AWS CodeBuild uses to determine the name and location to store the output artifact:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , valid values include:
            BUILD_ID : Include the build ID in the location of the build output artifact.
            NONE : Do not include the build ID. This is the default if namespaceType is not specified.
            For example, if path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .
            name (string) --Along with path and namespaceType , the pattern that AWS CodeBuild uses to name and store the output artifact:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , this is the name of the output artifact object. If you set the name to be a forward slash ('/'), the artifact is stored in the root of the output bucket.
            For example:
            If path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , then the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .
            If path is empty, namespaceType is set to NONE , and name is set to '/ ', the output artifact is stored in the root of the output bucket.
            If path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to '/ ', the output artifact is stored in ``MyArtifacts/build-ID `` .
            packaging (string) --The type of build output artifact to create:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , valid values include:
            NONE : AWS CodeBuild creates in the output bucket a folder that contains the build output. This is the default if packaging is not specified.
            ZIP : AWS CodeBuild creates in the output bucket a ZIP file that contains the build output.
            
            overrideArtifactName (boolean) --If this flag is set, a name specified in the build spec file overrides the artifact name. The name specified in a build spec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.
            encryptionDisabled (boolean) --Set to true if you do not want your output artifacts encrypted. This option is valid only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with another artifacts type, an invalidInputException is thrown.
            artifactIdentifier (string) --An identifier for this artifact definition.
            

    :type secondaryArtifacts: list
    :param secondaryArtifacts: An array of ProjectSource objects.
            (dict) --Information about the build output artifacts for the build project.
            type (string) -- [REQUIRED]The type of build output artifact. Valid values include:
            CODEPIPELINE : The build project has build output generated through AWS CodePipeline.
            NO_ARTIFACTS : The build project does not produce any build output.
            S3 : The build project stores build output in Amazon Simple Storage Service (Amazon S3).
            location (string) --Information about the build output artifact location:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , this is the name of the output bucket.
            path (string) --Along with namespaceType and name , the pattern that AWS CodeBuild uses to name and store the output artifact:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , this is the path to the output artifact. If path is not specified, path is not used.
            For example, if path is set to MyArtifacts , namespaceType is set to NONE , and name is set to MyArtifact.zip , the output artifact is stored in the output bucket at MyArtifacts/MyArtifact.zip .
            namespaceType (string) --Along with path and name , the pattern that AWS CodeBuild uses to determine the name and location to store the output artifact:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , valid values include:
            BUILD_ID : Include the build ID in the location of the build output artifact.
            NONE : Do not include the build ID. This is the default if namespaceType is not specified.
            For example, if path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .
            name (string) --Along with path and namespaceType , the pattern that AWS CodeBuild uses to name and store the output artifact:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , this is the name of the output artifact object. If you set the name to be a forward slash ('/'), the artifact is stored in the root of the output bucket.
            For example:
            If path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , then the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .
            If path is empty, namespaceType is set to NONE , and name is set to '/ ', the output artifact is stored in the root of the output bucket.
            If path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to '/ ', the output artifact is stored in ``MyArtifacts/build-ID `` .
            packaging (string) --The type of build output artifact to create:
            If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild.
            If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
            If type is set to S3 , valid values include:
            NONE : AWS CodeBuild creates in the output bucket a folder that contains the build output. This is the default if packaging is not specified.
            ZIP : AWS CodeBuild creates in the output bucket a ZIP file that contains the build output.
            
            overrideArtifactName (boolean) --If this flag is set, a name specified in the build spec file overrides the artifact name. The name specified in a build spec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.
            encryptionDisabled (boolean) --Set to true if you do not want your output artifacts encrypted. This option is valid only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with another artifacts type, an invalidInputException is thrown.
            artifactIdentifier (string) --An identifier for this artifact definition.
            
            

    :type cache: dict
    :param cache: Stores recently used information so that it can be quickly accessed at a later time.
            type (string) -- [REQUIRED]The type of cache used by the build project. Valid values include:
            NO_CACHE : The build project does not use any cache.
            S3 : The build project reads and writes from and to S3.
            location (string) --Information about the cache location:
            NO_CACHE : This value is ignored.
            S3 : This is the S3 bucket name/prefix.
            

    :type environment: dict
    :param environment: Information to be changed about the build environment for the build project.
            type (string) -- [REQUIRED]The type of build environment to use for related builds.
            image (string) -- [REQUIRED]The ID of the Docker image to use for this build project.
            computeType (string) -- [REQUIRED]Information about the compute resources the build project uses. Available values include:
            BUILD_GENERAL1_SMALL : Use up to 3 GB memory and 2 vCPUs for builds.
            BUILD_GENERAL1_MEDIUM : Use up to 7 GB memory and 4 vCPUs for builds.
            BUILD_GENERAL1_LARGE : Use up to 15 GB memory and 8 vCPUs for builds.
            environmentVariables (list) --A set of environment variables to make available to builds for this build project.
            (dict) --Information about an environment variable for a build project or a build.
            name (string) -- [REQUIRED]The name or key of the environment variable.
            value (string) -- [REQUIRED]The value of the environment variable.
            Warning
            We strongly discourage the use of environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. Environment variables can be displayed in plain text using the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI).
            type (string) --The type of environment variable. Valid values include:
            PARAMETER_STORE : An environment variable stored in Amazon EC2 Systems Manager Parameter Store.
            PLAINTEXT : An environment variable in plaintext format.
            
            privilegedMode (boolean) --Enables running the Docker daemon inside a Docker container. Set to true only if the build project is be used to build Docker images, and the specified build environment image is not provided by AWS CodeBuild with Docker support. Otherwise, all associated builds that attempt to interact with the Docker daemon fail. You must also start the Docker daemon so that builds can interact with it. One way to do this is to initialize the Docker daemon during the install phase of your build spec by running the following build commands. (Do not run these commands if the specified build environment image is provided by AWS CodeBuild with Docker support.)
            If the operating system's base image is Ubuntu Linux:
            - nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout 15 sh -c 'until docker info; do echo .; sleep 1; done'
            If the operating system's base image is Alpine Linux, add the -t argument to timeout :
            - nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay& - timeout 15 -t sh -c 'until docker info; do echo .; sleep 1; done'
            certificate (string) --The certificate to use with this build project.
            

    :type serviceRole: string
    :param serviceRole: The replacement ARN of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.

    :type timeoutInMinutes: integer
    :param timeoutInMinutes: The replacement value in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait before timing out any related build that did not get marked as completed.

    :type queuedTimeoutInMinutes: integer
    :param queuedTimeoutInMinutes: The number of minutes a build is allowed to be queued before it times out.

    :type encryptionKey: string
    :param encryptionKey: The replacement AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build output artifacts.
            You can specify either the Amazon Resource Name (ARN)of the CMK or, if available, the CMK's alias (using the format ``alias/alias-name `` ).
            

    :type tags: list
    :param tags: The replacement set of tags for this build project.
            These tags are available for use by AWS services that support AWS CodeBuild build project tags.
            (dict) --A tag, consisting of a key and a value.
            This tag is available for use by AWS services that support tags in AWS CodeBuild.
            key (string) --The tag's key.
            value (string) --The tag's value.
            
            

    :type vpcConfig: dict
    :param vpcConfig: VpcConfig enables AWS CodeBuild to access resources in an Amazon VPC.
            vpcId (string) --The ID of the Amazon VPC.
            subnets (list) --A list of one or more subnet IDs in your Amazon VPC.
            (string) --
            securityGroupIds (list) --A list of one or more security groups IDs in your Amazon VPC.
            (string) --
            

    :type badgeEnabled: boolean
    :param badgeEnabled: Set this to true to generate a publicly accessible URL for your project's build badge.

    :type logsConfig: dict
    :param logsConfig: Information about logs for the build project. A project can create logs in Amazon CloudWatch Logs, logs in an S3 bucket, or both.
            cloudWatchLogs (dict) --Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are enabled by default.
            status (string) -- [REQUIRED]The current status of the logs in Amazon CloudWatch Logs for a build project. Valid values are:
            ENABLED : Amazon CloudWatch Logs are enabled for this build project.
            DISABLED : Amazon CloudWatch Logs are not enabled for this build project.
            groupName (string) --The group name of the logs in Amazon CloudWatch Logs. For more information, see Working with Log Groups and Log Streams .
            streamName (string) --The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see Working with Log Groups and Log Streams .
            s3Logs (dict) --Information about logs built to an S3 bucket for a build project. S3 logs are not enabled by default.
            status (string) -- [REQUIRED]The current status of the S3 build logs. Valid values are:
            ENABLED : S3 build logs are enabled for this build project.
            DISABLED : S3 build logs are not enabled for this build project.
            location (string) --The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is my-bucket , and your path prefix is build-log , then acceptable formats are my-bucket/build-log or arn:aws:s3:::my-bucket/build-log .
            
            

    :rtype: dict
    :return: {
        'project': {
            'name': 'string',
            'arn': 'string',
            'description': 'string',
            'source': {
                'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                'location': 'string',
                'gitCloneDepth': 123,
                'buildspec': 'string',
                'auth': {
                    'type': 'OAUTH',
                    'resource': 'string'
                },
                'reportBuildStatus': True|False,
                'insecureSsl': True|False,
                'sourceIdentifier': 'string'
            },
            'secondarySources': [
                {
                    'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                    'location': 'string',
                    'gitCloneDepth': 123,
                    'buildspec': 'string',
                    'auth': {
                        'type': 'OAUTH',
                        'resource': 'string'
                    },
                    'reportBuildStatus': True|False,
                    'insecureSsl': True|False,
                    'sourceIdentifier': 'string'
                },
            ],
            'artifacts': {
                'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                'location': 'string',
                'path': 'string',
                'namespaceType': 'NONE'|'BUILD_ID',
                'name': 'string',
                'packaging': 'NONE'|'ZIP',
                'overrideArtifactName': True|False,
                'encryptionDisabled': True|False,
                'artifactIdentifier': 'string'
            },
            'secondaryArtifacts': [
                {
                    'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                    'location': 'string',
                    'path': 'string',
                    'namespaceType': 'NONE'|'BUILD_ID',
                    'name': 'string',
                    'packaging': 'NONE'|'ZIP',
                    'overrideArtifactName': True|False,
                    'encryptionDisabled': True|False,
                    'artifactIdentifier': 'string'
                },
            ],
            'cache': {
                'type': 'NO_CACHE'|'S3',
                'location': 'string'
            },
            'environment': {
                'type': 'WINDOWS_CONTAINER'|'LINUX_CONTAINER',
                'image': 'string',
                'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE',
                'environmentVariables': [
                    {
                        'name': 'string',
                        'value': 'string',
                        'type': 'PLAINTEXT'|'PARAMETER_STORE'
                    },
                ],
                'privilegedMode': True|False,
                'certificate': 'string'
            },
            'serviceRole': 'string',
            'timeoutInMinutes': 123,
            'queuedTimeoutInMinutes': 123,
            'encryptionKey': 'string',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'created': datetime(2015, 1, 1),
            'lastModified': datetime(2015, 1, 1),
            'webhook': {
                'url': 'string',
                'payloadUrl': 'string',
                'secret': 'string',
                'branchFilter': 'string',
                'lastModifiedSecret': datetime(2015, 1, 1)
            },
            'vpcConfig': {
                'vpcId': 'string',
                'subnets': [
                    'string',
                ],
                'securityGroupIds': [
                    'string',
                ]
            },
            'badge': {
                'badgeEnabled': True|False,
                'badgeRequestUrl': 'string'
            },
            'logsConfig': {
                'cloudWatchLogs': {
                    'status': 'ENABLED'|'DISABLED',
                    'groupName': 'string',
                    'streamName': 'string'
                },
                's3Logs': {
                    'status': 'ENABLED'|'DISABLED',
                    'location': 'string'
                }
            }
        }
    }
    
    
    :returns: 
    BITBUCKET : The source code is in a Bitbucket repository.
    CODECOMMIT : The source code is in an AWS CodeCommit repository.
    CODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.
    GITHUB : The source code is in a GitHub repository.
    NO_SOURCE : The project does not have input source code.
    S3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.
    
    """
    pass

def update_webhook(projectName=None, branchFilter=None, rotateSecret=None):
    """
    Updates the webhook associated with an AWS CodeBuild build project.
    See also: AWS API Documentation
    
    
    :example: response = client.update_webhook(
        projectName='string',
        branchFilter='string',
        rotateSecret=True|False
    )
    
    
    :type projectName: string
    :param projectName: [REQUIRED]
            The name of the AWS CodeBuild project.
            

    :type branchFilter: string
    :param branchFilter: A regular expression used to determine which repository branches are built when a webhook is triggered. If the name of a branch matches the regular expression, then it is built. If branchFilter is empty, then all branches are built.

    :type rotateSecret: boolean
    :param rotateSecret: A boolean value that specifies whether the associated GitHub repository's secret token should be updated. If you use Bitbucket for your repository, rotateSecret is ignored.

    :rtype: dict
    :return: {
        'webhook': {
            'url': 'string',
            'payloadUrl': 'string',
            'secret': 'string',
            'branchFilter': 'string',
            'lastModifiedSecret': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

