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

def batch_describe_simulation_job(jobs=None):
    """
    Describes one or more simulation jobs.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_describe_simulation_job(
        jobs=[
            'string',
        ]
    )
    
    
    :type jobs: list
    :param jobs: [REQUIRED]
            A list of Amazon Resource Names (ARNs) of simulation jobs to describe.
            (string) --
            

    :rtype: dict
    :return: {
        'jobs': [
            {
                'arn': 'string',
                'name': 'string',
                'status': 'Pending'|'Preparing'|'Running'|'Restarting'|'Completed'|'Failed'|'RunningFailed'|'Terminating'|'Terminated'|'Canceled',
                'lastUpdatedAt': datetime(2015, 1, 1),
                'failureBehavior': 'Fail'|'Continue',
                'failureCode': 'InternalServiceError'|'RobotApplicationCrash'|'SimulationApplicationCrash'|'BadPermissionsRobotApplication'|'BadPermissionsSimulationApplication'|'BadPermissionsS3Output'|'BadPermissionsCloudwatchLogs'|'SubnetIpLimitExceeded'|'ENILimitExceeded'|'BadPermissionsUserCredentials'|'InvalidBundleRobotApplication'|'InvalidBundleSimulationApplication'|'RobotApplicationVersionMismatchedEtag'|'SimulationApplicationVersionMismatchedEtag',
                'clientRequestToken': 'string',
                'outputLocation': {
                    's3Bucket': 'string',
                    's3Prefix': 'string'
                },
                'maxJobDurationInSeconds': 123,
                'simulationTimeMillis': 123,
                'iamRole': 'string',
                'robotApplications': [
                    {
                        'application': 'string',
                        'applicationVersion': 'string',
                        'launchConfig': {
                            'packageName': 'string',
                            'launchFile': 'string',
                            'environmentVariables': {
                                'string': 'string'
                            }
                        }
                    },
                ],
                'simulationApplications': [
                    {
                        'application': 'string',
                        'applicationVersion': 'string',
                        'launchConfig': {
                            'packageName': 'string',
                            'launchFile': 'string',
                            'environmentVariables': {
                                'string': 'string'
                            }
                        }
                    },
                ],
                'vpcConfig': {
                    'subnets': [
                        'string',
                    ],
                    'securityGroups': [
                        'string',
                    ],
                    'vpcId': 'string',
                    'assignPublicIp': True|False
                }
            },
        ],
        'unprocessedJobs': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
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

def cancel_simulation_job(job=None):
    """
    Cancels the specified simulation job.
    See also: AWS API Documentation
    
    
    :example: response = client.cancel_simulation_job(
        job='string'
    )
    
    
    :type job: string
    :param job: [REQUIRED]
            The simulation job ARN to cancel.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_deployment_job(deploymentConfig=None, clientRequestToken=None, fleet=None, deploymentApplicationConfigs=None):
    """
    Creates a deployment job.
    See also: AWS API Documentation
    
    
    :example: response = client.create_deployment_job(
        deploymentConfig={
            'concurrentDeploymentPercentage': 123,
            'failureThresholdPercentage': 123
        },
        clientRequestToken='string',
        fleet='string',
        deploymentApplicationConfigs=[
            {
                'application': 'string',
                'applicationVersion': 'string',
                'launchConfig': {
                    'packageName': 'string',
                    'preLaunchFile': 'string',
                    'launchFile': 'string',
                    'postLaunchFile': 'string',
                    'environmentVariables': {
                        'string': 'string'
                    }
                }
            },
        ]
    )
    
    
    :type deploymentConfig: dict
    :param deploymentConfig: The requested deployment configuration.
            concurrentDeploymentPercentage (integer) --The percentage of robots receiving the deployment at the same time.
            failureThresholdPercentage (integer) --The percentage of deployments that need to fail before stopping deployment.
            

    :type clientRequestToken: string
    :param clientRequestToken: [REQUIRED]
            Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
            This field is autopopulated if not provided.
            

    :type fleet: string
    :param fleet: [REQUIRED]
            The Amazon Resource Name (ARN) of the fleet to deploy.
            

    :type deploymentApplicationConfigs: list
    :param deploymentApplicationConfigs: [REQUIRED]
            The deployment application configuration.
            (dict) --Information about a deployment application configuration.
            application (string) -- [REQUIRED]The application.
            applicationVersion (string) -- [REQUIRED]The version of the application.
            launchConfig (dict) -- [REQUIRED]The launch configuration, usually roslaunch .
            packageName (string) -- [REQUIRED]The package name.
            preLaunchFile (string) --The deployment pre-launch file. This file will be executed prior to the deployment launch file.
            launchFile (string) -- [REQUIRED]The deployment launch file.
            postLaunchFile (string) --The deployment post-launch file. This file will be executed after the deployment launch file.
            environmentVariables (dict) --An array of key/value pairs specifying environment variables for the deployment application.
            (string) --
            (string) --
            
            
            

    :rtype: dict
    :return: {
        'arn': 'string',
        'fleet': 'string',
        'status': 'Pending'|'Preparing'|'InProgress'|'Failed'|'Succeeded',
        'deploymentApplicationConfigs': [
            {
                'application': 'string',
                'applicationVersion': 'string',
                'launchConfig': {
                    'packageName': 'string',
                    'preLaunchFile': 'string',
                    'launchFile': 'string',
                    'postLaunchFile': 'string',
                    'environmentVariables': {
                        'string': 'string'
                    }
                }
            },
        ],
        'failureReason': 'string',
        'failureCode': 'ResourceNotFound'|'FailureThresholdBreached'|'RobotDeploymentNoResponse'|'GreengrassDeploymentFailed'|'MissingRobotArchitecture'|'MissingRobotApplicationArchitecture'|'MissingRobotDeploymentResource'|'GreengrassGroupVersionDoesNotExist'|'ExtractingBundleFailure'|'PreLaunchFileFailure'|'PostLaunchFileFailure'|'BadPermissionError'|'InternalServerError',
        'createdAt': datetime(2015, 1, 1),
        'deploymentConfig': {
            'concurrentDeploymentPercentage': 123,
            'failureThresholdPercentage': 123
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def create_fleet(name=None):
    """
    Creates a fleet, a logical group of robots running the same robot application.
    See also: AWS API Documentation
    
    
    :example: response = client.create_fleet(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the fleet.
            

    :rtype: dict
    :return: {
        'arn': 'string',
        'name': 'string',
        'createdAt': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def create_robot(name=None, architecture=None, greengrassGroupId=None):
    """
    Creates a robot.
    See also: AWS API Documentation
    
    
    :example: response = client.create_robot(
        name='string',
        architecture='X86_64'|'ARM64'|'ARMHF',
        greengrassGroupId='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name for the robot.
            

    :type architecture: string
    :param architecture: [REQUIRED]
            The target architecture of the robot.
            

    :type greengrassGroupId: string
    :param greengrassGroupId: [REQUIRED]
            The Greengrass group id.
            

    :rtype: dict
    :return: {
        'arn': 'string',
        'name': 'string',
        'createdAt': datetime(2015, 1, 1),
        'greengrassGroupId': 'string',
        'architecture': 'X86_64'|'ARM64'|'ARMHF'
    }
    
    
    """
    pass

def create_robot_application(name=None, sources=None, robotSoftwareSuite=None):
    """
    Creates a robot application.
    See also: AWS API Documentation
    
    
    :example: response = client.create_robot_application(
        name='string',
        sources=[
            {
                's3Bucket': 'string',
                's3Key': 'string',
                'architecture': 'X86_64'|'ARM64'|'ARMHF'
            },
        ],
        robotSoftwareSuite={
            'name': 'ROS',
            'version': 'Kinetic'
        }
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the robot application.
            

    :type sources: list
    :param sources: [REQUIRED]
            The sources of the robot application.
            (dict) --Information about a source configuration.
            s3Bucket (string) --The Amazon S3 bucket name.
            s3Key (string) --The s3 object key.
            architecture (string) --The target processor architecture for the application.
            
            

    :type robotSoftwareSuite: dict
    :param robotSoftwareSuite: [REQUIRED]
            The robot software suite used by the robot application.
            name (string) --The name of the robot software suite.
            version (string) --The version of the robot software suite.
            

    :rtype: dict
    :return: {
        'arn': 'string',
        'name': 'string',
        'version': 'string',
        'sources': [
            {
                's3Bucket': 'string',
                's3Key': 'string',
                'etag': 'string',
                'architecture': 'X86_64'|'ARM64'|'ARMHF'
            },
        ],
        'robotSoftwareSuite': {
            'name': 'ROS',
            'version': 'Kinetic'
        },
        'lastUpdatedAt': datetime(2015, 1, 1),
        'revisionId': 'string'
    }
    
    
    """
    pass

def create_robot_application_version(application=None, currentRevisionId=None):
    """
    Creates a version of a robot application.
    See also: AWS API Documentation
    
    
    :example: response = client.create_robot_application_version(
        application='string',
        currentRevisionId='string'
    )
    
    
    :type application: string
    :param application: [REQUIRED]
            The application information for the robot application.
            

    :type currentRevisionId: string
    :param currentRevisionId: The current revision id for the robot application. If you provide a value and it matches the latest revision ID, a new version will be created.

    :rtype: dict
    :return: {
        'arn': 'string',
        'name': 'string',
        'version': 'string',
        'sources': [
            {
                's3Bucket': 'string',
                's3Key': 'string',
                'etag': 'string',
                'architecture': 'X86_64'|'ARM64'|'ARMHF'
            },
        ],
        'robotSoftwareSuite': {
            'name': 'ROS',
            'version': 'Kinetic'
        },
        'lastUpdatedAt': datetime(2015, 1, 1),
        'revisionId': 'string'
    }
    
    
    """
    pass

def create_simulation_application(name=None, sources=None, simulationSoftwareSuite=None, robotSoftwareSuite=None, renderingEngine=None):
    """
    Creates a simulation application.
    See also: AWS API Documentation
    
    
    :example: response = client.create_simulation_application(
        name='string',
        sources=[
            {
                's3Bucket': 'string',
                's3Key': 'string',
                'architecture': 'X86_64'|'ARM64'|'ARMHF'
            },
        ],
        simulationSoftwareSuite={
            'name': 'Gazebo',
            'version': 'string'
        },
        robotSoftwareSuite={
            'name': 'ROS',
            'version': 'Kinetic'
        },
        renderingEngine={
            'name': 'OGRE',
            'version': 'string'
        }
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the simulation application.
            

    :type sources: list
    :param sources: [REQUIRED]
            The sources of the simulation application.
            (dict) --Information about a source configuration.
            s3Bucket (string) --The Amazon S3 bucket name.
            s3Key (string) --The s3 object key.
            architecture (string) --The target processor architecture for the application.
            
            

    :type simulationSoftwareSuite: dict
    :param simulationSoftwareSuite: [REQUIRED]
            The simulation software suite used by the simulation application.
            name (string) --The name of the simulation software suite.
            version (string) --The version of the simulation software suite.
            

    :type robotSoftwareSuite: dict
    :param robotSoftwareSuite: [REQUIRED]
            The robot software suite of the simulation application.
            name (string) --The name of the robot software suite.
            version (string) --The version of the robot software suite.
            

    :type renderingEngine: dict
    :param renderingEngine: [REQUIRED]
            The rendering engine for the simulation application.
            name (string) --The name of the rendering engine.
            version (string) --The version of the rendering engine.
            

    :rtype: dict
    :return: {
        'arn': 'string',
        'name': 'string',
        'version': 'string',
        'sources': [
            {
                's3Bucket': 'string',
                's3Key': 'string',
                'etag': 'string',
                'architecture': 'X86_64'|'ARM64'|'ARMHF'
            },
        ],
        'simulationSoftwareSuite': {
            'name': 'Gazebo',
            'version': 'string'
        },
        'robotSoftwareSuite': {
            'name': 'ROS',
            'version': 'Kinetic'
        },
        'renderingEngine': {
            'name': 'OGRE',
            'version': 'string'
        },
        'lastUpdatedAt': datetime(2015, 1, 1),
        'revisionId': 'string'
    }
    
    
    """
    pass

def create_simulation_application_version(application=None, currentRevisionId=None):
    """
    Creates a simulation application with a specific revision id.
    See also: AWS API Documentation
    
    
    :example: response = client.create_simulation_application_version(
        application='string',
        currentRevisionId='string'
    )
    
    
    :type application: string
    :param application: [REQUIRED]
            The application information for the simulation application.
            

    :type currentRevisionId: string
    :param currentRevisionId: The current revision id for the simulation application. If you provide a value and it matches the latest revision ID, a new version will be created.

    :rtype: dict
    :return: {
        'arn': 'string',
        'name': 'string',
        'version': 'string',
        'sources': [
            {
                's3Bucket': 'string',
                's3Key': 'string',
                'etag': 'string',
                'architecture': 'X86_64'|'ARM64'|'ARMHF'
            },
        ],
        'simulationSoftwareSuite': {
            'name': 'Gazebo',
            'version': 'string'
        },
        'robotSoftwareSuite': {
            'name': 'ROS',
            'version': 'Kinetic'
        },
        'renderingEngine': {
            'name': 'OGRE',
            'version': 'string'
        },
        'lastUpdatedAt': datetime(2015, 1, 1),
        'revisionId': 'string'
    }
    
    
    """
    pass

def create_simulation_job(clientRequestToken=None, outputLocation=None, maxJobDurationInSeconds=None, iamRole=None, failureBehavior=None, robotApplications=None, simulationApplications=None, vpcConfig=None):
    """
    Creates a simulation job.
    See also: AWS API Documentation
    
    
    :example: response = client.create_simulation_job(
        clientRequestToken='string',
        outputLocation={
            's3Bucket': 'string',
            's3Prefix': 'string'
        },
        maxJobDurationInSeconds=123,
        iamRole='string',
        failureBehavior='Fail'|'Continue',
        robotApplications=[
            {
                'application': 'string',
                'applicationVersion': 'string',
                'launchConfig': {
                    'packageName': 'string',
                    'launchFile': 'string',
                    'environmentVariables': {
                        'string': 'string'
                    }
                }
            },
        ],
        simulationApplications=[
            {
                'application': 'string',
                'applicationVersion': 'string',
                'launchConfig': {
                    'packageName': 'string',
                    'launchFile': 'string',
                    'environmentVariables': {
                        'string': 'string'
                    }
                }
            },
        ],
        vpcConfig={
            'subnets': [
                'string',
            ],
            'securityGroups': [
                'string',
            ],
            'assignPublicIp': True|False
        }
    )
    
    
    :type clientRequestToken: string
    :param clientRequestToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
            This field is autopopulated if not provided.
            

    :type outputLocation: dict
    :param outputLocation: Location for output files generated by the simulation job.
            s3Bucket (string) --The S3 bucket for output.
            s3Prefix (string) --The S3 folder in the s3Bucket where output files will be placed.
            

    :type maxJobDurationInSeconds: integer
    :param maxJobDurationInSeconds: [REQUIRED]
            The maximum simulation job duration in seconds (up to 14 days or 1,209,600 seconds. When maxJobDurationInSeconds is reached, the simulation job will status will transition to Completed .
            

    :type iamRole: string
    :param iamRole: [REQUIRED]
            The IAM role that allows the simulation instance to call the AWS APIs that are specified in its associated policies on your behalf. This is how credentials are passed in to your simulation job. See how to specify AWS security credentials for your application .
            

    :type failureBehavior: string
    :param failureBehavior: The failure behavior the simulation job.
            Continue
            Restart the simulation job in the same host instance.
            Fail
            Stop the simulation job and terminate the instance.
            

    :type robotApplications: list
    :param robotApplications: The robot application to use in the simulation job.
            (dict) --Application configuration information for a robot.
            application (string) -- [REQUIRED]The application information for the robot application.
            applicationVersion (string) --The version of the robot application.
            launchConfig (dict) -- [REQUIRED]The launch configuration for the robot application.
            packageName (string) -- [REQUIRED]The package name.
            launchFile (string) -- [REQUIRED]The launch file.
            environmentVariables (dict) --The environment variables for the application launch.
            (string) --
            (string) --
            
            
            

    :type simulationApplications: list
    :param simulationApplications: The simulation application to use in the simulation job.
            (dict) --Information about a simulation application configuration.
            application (string) -- [REQUIRED]The application information for the simulation application.
            applicationVersion (string) --The version of the simulation application.
            launchConfig (dict) -- [REQUIRED]The launch configuration for the simulation application.
            packageName (string) -- [REQUIRED]The package name.
            launchFile (string) -- [REQUIRED]The launch file.
            environmentVariables (dict) --The environment variables for the application launch.
            (string) --
            (string) --
            
            
            

    :type vpcConfig: dict
    :param vpcConfig: If your simulation job accesses resources in a VPC, you provide this parameter identifying the list of security group IDs and subnet IDs. These must belong to the same VPC. You must provide at least one security group and one subnet ID.
            subnets (list) -- [REQUIRED]A list of one or more subnet IDs in your VPC.
            (string) --
            securityGroups (list) --A list of one or more security groups IDs in your VPC.
            (string) --
            assignPublicIp (boolean) --A boolean indicating whether to assign a public IP address.
            

    :rtype: dict
    :return: {
        'arn': 'string',
        'status': 'Pending'|'Preparing'|'Running'|'Restarting'|'Completed'|'Failed'|'RunningFailed'|'Terminating'|'Terminated'|'Canceled',
        'lastUpdatedAt': datetime(2015, 1, 1),
        'failureBehavior': 'Fail'|'Continue',
        'failureCode': 'InternalServiceError'|'RobotApplicationCrash'|'SimulationApplicationCrash'|'BadPermissionsRobotApplication'|'BadPermissionsSimulationApplication'|'BadPermissionsS3Output'|'BadPermissionsCloudwatchLogs'|'SubnetIpLimitExceeded'|'ENILimitExceeded'|'BadPermissionsUserCredentials'|'InvalidBundleRobotApplication'|'InvalidBundleSimulationApplication'|'RobotApplicationVersionMismatchedEtag'|'SimulationApplicationVersionMismatchedEtag',
        'clientRequestToken': 'string',
        'outputLocation': {
            's3Bucket': 'string',
            's3Prefix': 'string'
        },
        'maxJobDurationInSeconds': 123,
        'simulationTimeMillis': 123,
        'iamRole': 'string',
        'robotApplications': [
            {
                'application': 'string',
                'applicationVersion': 'string',
                'launchConfig': {
                    'packageName': 'string',
                    'launchFile': 'string',
                    'environmentVariables': {
                        'string': 'string'
                    }
                }
            },
        ],
        'simulationApplications': [
            {
                'application': 'string',
                'applicationVersion': 'string',
                'launchConfig': {
                    'packageName': 'string',
                    'launchFile': 'string',
                    'environmentVariables': {
                        'string': 'string'
                    }
                }
            },
        ],
        'vpcConfig': {
            'subnets': [
                'string',
            ],
            'securityGroups': [
                'string',
            ],
            'vpcId': 'string',
            'assignPublicIp': True|False
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def delete_fleet(fleet=None):
    """
    Deletes a fleet.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_fleet(
        fleet='string'
    )
    
    
    :type fleet: string
    :param fleet: [REQUIRED]
            The Amazon Resource Name (ARN) of the fleet.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_robot(robot=None):
    """
    Deletes a robot.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_robot(
        robot='string'
    )
    
    
    :type robot: string
    :param robot: [REQUIRED]
            The Amazon Resource Name (ARN) of the robot.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_robot_application(application=None, applicationVersion=None):
    """
    Deletes a robot application.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_robot_application(
        application='string',
        applicationVersion='string'
    )
    
    
    :type application: string
    :param application: [REQUIRED]
            The Amazon Resource Name (ARN) of the the robot application.
            

    :type applicationVersion: string
    :param applicationVersion: The version of the robot application to delete.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_simulation_application(application=None, applicationVersion=None):
    """
    Deletes a simulation application.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_simulation_application(
        application='string',
        applicationVersion='string'
    )
    
    
    :type application: string
    :param application: [REQUIRED]
            The application information for the simulation application to delete.
            

    :type applicationVersion: string
    :param applicationVersion: The version of the simulation application to delete.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def deregister_robot(fleet=None, robot=None):
    """
    Deregisters a robot.
    See also: AWS API Documentation
    
    
    :example: response = client.deregister_robot(
        fleet='string',
        robot='string'
    )
    
    
    :type fleet: string
    :param fleet: [REQUIRED]
            The Amazon Resource Name (ARN) of the fleet.
            

    :type robot: string
    :param robot: [REQUIRED]
            The Amazon Resource Name (ARN) of the robot.
            

    :rtype: dict
    :return: {
        'fleet': 'string',
        'robot': 'string'
    }
    
    
    """
    pass

def describe_deployment_job(job=None):
    """
    Describes a deployment job. [Does it work regardless of deployment status, e.g. Failed?]
    See also: AWS API Documentation
    
    
    :example: response = client.describe_deployment_job(
        job='string'
    )
    
    
    :type job: string
    :param job: [REQUIRED]
            The Amazon Resource Name (ARN) of the deployment job.
            

    :rtype: dict
    :return: {
        'arn': 'string',
        'fleet': 'string',
        'status': 'Pending'|'Preparing'|'InProgress'|'Failed'|'Succeeded',
        'deploymentConfig': {
            'concurrentDeploymentPercentage': 123,
            'failureThresholdPercentage': 123
        },
        'deploymentApplicationConfigs': [
            {
                'application': 'string',
                'applicationVersion': 'string',
                'launchConfig': {
                    'packageName': 'string',
                    'preLaunchFile': 'string',
                    'launchFile': 'string',
                    'postLaunchFile': 'string',
                    'environmentVariables': {
                        'string': 'string'
                    }
                }
            },
        ],
        'failureReason': 'string',
        'failureCode': 'ResourceNotFound'|'FailureThresholdBreached'|'RobotDeploymentNoResponse'|'GreengrassDeploymentFailed'|'MissingRobotArchitecture'|'MissingRobotApplicationArchitecture'|'MissingRobotDeploymentResource'|'GreengrassGroupVersionDoesNotExist'|'ExtractingBundleFailure'|'PreLaunchFileFailure'|'PostLaunchFileFailure'|'BadPermissionError'|'InternalServerError',
        'createdAt': datetime(2015, 1, 1),
        'robotDeploymentSummary': [
            {
                'arn': 'string',
                'deploymentStartTime': datetime(2015, 1, 1),
                'deploymentFinishTime': datetime(2015, 1, 1),
                'status': 'Available'|'Registered'|'PendingNewDeployment'|'Deploying'|'Failed'|'InSync'|'NoResponse',
                'progressDetail': {
                    'currentProgress': 'string',
                    'targetResource': 'string'
                },
                'failureReason': 'string',
                'failureCode': 'ResourceNotFound'|'FailureThresholdBreached'|'RobotDeploymentNoResponse'|'GreengrassDeploymentFailed'|'MissingRobotArchitecture'|'MissingRobotApplicationArchitecture'|'MissingRobotDeploymentResource'|'GreengrassGroupVersionDoesNotExist'|'ExtractingBundleFailure'|'PreLaunchFileFailure'|'PostLaunchFileFailure'|'BadPermissionError'|'InternalServerError'
            },
        ]
    }
    
    
    """
    pass

def describe_fleet(fleet=None):
    """
    Describes a fleet.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_fleet(
        fleet='string'
    )
    
    
    :type fleet: string
    :param fleet: [REQUIRED]
            The Amazon Resource Name (ARN) of the fleet.
            

    :rtype: dict
    :return: {
        'name': 'string',
        'arn': 'string',
        'robots': [
            {
                'arn': 'string',
                'name': 'string',
                'fleetArn': 'string',
                'status': 'Available'|'Registered'|'PendingNewDeployment'|'Deploying'|'Failed'|'InSync'|'NoResponse',
                'greenGrassGroupId': 'string',
                'createdAt': datetime(2015, 1, 1),
                'architecture': 'X86_64'|'ARM64'|'ARMHF',
                'lastDeploymentJob': 'string',
                'lastDeploymentTime': datetime(2015, 1, 1)
            },
        ],
        'createdAt': datetime(2015, 1, 1),
        'lastDeploymentStatus': 'Pending'|'Preparing'|'InProgress'|'Failed'|'Succeeded',
        'lastDeploymentJob': 'string',
        'lastDeploymentTime': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_robot(robot=None):
    """
    Describes a robot.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_robot(
        robot='string'
    )
    
    
    :type robot: string
    :param robot: [REQUIRED]
            The Amazon Resource Name (ARN) of the robot to be described.
            

    :rtype: dict
    :return: {
        'arn': 'string',
        'name': 'string',
        'fleetArn': 'string',
        'status': 'Available'|'Registered'|'PendingNewDeployment'|'Deploying'|'Failed'|'InSync'|'NoResponse',
        'greengrassGroupId': 'string',
        'createdAt': datetime(2015, 1, 1),
        'architecture': 'X86_64'|'ARM64'|'ARMHF',
        'lastDeploymentJob': 'string',
        'lastDeploymentTime': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_robot_application(application=None, applicationVersion=None):
    """
    Describes a robot application.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_robot_application(
        application='string',
        applicationVersion='string'
    )
    
    
    :type application: string
    :param application: [REQUIRED]
            The Amazon Resource Name (ARN) of the robot application.
            

    :type applicationVersion: string
    :param applicationVersion: The version of the robot application to describe.

    :rtype: dict
    :return: {
        'arn': 'string',
        'name': 'string',
        'version': 'string',
        'sources': [
            {
                's3Bucket': 'string',
                's3Key': 'string',
                'etag': 'string',
                'architecture': 'X86_64'|'ARM64'|'ARMHF'
            },
        ],
        'robotSoftwareSuite': {
            'name': 'ROS',
            'version': 'Kinetic'
        },
        'revisionId': 'string',
        'lastUpdatedAt': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_simulation_application(application=None, applicationVersion=None):
    """
    Describes a simulation application.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_simulation_application(
        application='string',
        applicationVersion='string'
    )
    
    
    :type application: string
    :param application: [REQUIRED]
            The application information for the simulation application.
            

    :type applicationVersion: string
    :param applicationVersion: The version of the simulation application to describe.

    :rtype: dict
    :return: {
        'arn': 'string',
        'name': 'string',
        'version': 'string',
        'sources': [
            {
                's3Bucket': 'string',
                's3Key': 'string',
                'etag': 'string',
                'architecture': 'X86_64'|'ARM64'|'ARMHF'
            },
        ],
        'simulationSoftwareSuite': {
            'name': 'Gazebo',
            'version': 'string'
        },
        'robotSoftwareSuite': {
            'name': 'ROS',
            'version': 'Kinetic'
        },
        'renderingEngine': {
            'name': 'OGRE',
            'version': 'string'
        },
        'revisionId': 'string',
        'lastUpdatedAt': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_simulation_job(job=None):
    """
    Describes a simulation job.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_simulation_job(
        job='string'
    )
    
    
    :type job: string
    :param job: [REQUIRED]
            The Amazon Resource Name (ARN) of the simulation job to be described.
            

    :rtype: dict
    :return: {
        'arn': 'string',
        'name': 'string',
        'status': 'Pending'|'Preparing'|'Running'|'Restarting'|'Completed'|'Failed'|'RunningFailed'|'Terminating'|'Terminated'|'Canceled',
        'lastUpdatedAt': datetime(2015, 1, 1),
        'failureBehavior': 'Fail'|'Continue',
        'failureCode': 'InternalServiceError'|'RobotApplicationCrash'|'SimulationApplicationCrash'|'BadPermissionsRobotApplication'|'BadPermissionsSimulationApplication'|'BadPermissionsS3Output'|'BadPermissionsCloudwatchLogs'|'SubnetIpLimitExceeded'|'ENILimitExceeded'|'BadPermissionsUserCredentials'|'InvalidBundleRobotApplication'|'InvalidBundleSimulationApplication'|'RobotApplicationVersionMismatchedEtag'|'SimulationApplicationVersionMismatchedEtag',
        'clientRequestToken': 'string',
        'outputLocation': {
            's3Bucket': 'string',
            's3Prefix': 'string'
        },
        'maxJobDurationInSeconds': 123,
        'simulationTimeMillis': 123,
        'iamRole': 'string',
        'robotApplications': [
            {
                'application': 'string',
                'applicationVersion': 'string',
                'launchConfig': {
                    'packageName': 'string',
                    'launchFile': 'string',
                    'environmentVariables': {
                        'string': 'string'
                    }
                }
            },
        ],
        'simulationApplications': [
            {
                'application': 'string',
                'applicationVersion': 'string',
                'launchConfig': {
                    'packageName': 'string',
                    'launchFile': 'string',
                    'environmentVariables': {
                        'string': 'string'
                    }
                }
            },
        ],
        'vpcConfig': {
            'subnets': [
                'string',
            ],
            'securityGroups': [
                'string',
            ],
            'vpcId': 'string',
            'assignPublicIp': True|False
        }
    }
    
    
    :returns: 
    (string) --
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

def list_deployment_jobs(filters=None, nextToken=None, maxResults=None):
    """
    Returns a list of deployment jobs for a fleet. You can optionally provide filters to retrieve specific deployment jobs.
    See also: AWS API Documentation
    
    
    :example: response = client.list_deployment_jobs(
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ]
            },
        ],
        nextToken='string',
        maxResults=123
    )
    
    
    :type filters: list
    :param filters: Optional filters to limit results.
            (dict) --Information about a filter.
            name (string) --The name of the filter.
            values (list) --A list of values.
            (string) --
            
            

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListDeploymentJobs request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            

    :type maxResults: integer
    :param maxResults: The maximum number of deployment job results returned by ListDeploymentJobs in paginated output. When this parameter is used, ListDeploymentJobs only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListDeploymentJobs request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListDeploymentJobs returns up to 100 results and a nextToken value if applicable.

    :rtype: dict
    :return: {
        'deploymentJobs': [
            {
                'arn': 'string',
                'fleet': 'string',
                'status': 'Pending'|'Preparing'|'InProgress'|'Failed'|'Succeeded',
                'deploymentApplicationConfigs': [
                    {
                        'application': 'string',
                        'applicationVersion': 'string',
                        'launchConfig': {
                            'packageName': 'string',
                            'preLaunchFile': 'string',
                            'launchFile': 'string',
                            'postLaunchFile': 'string',
                            'environmentVariables': {
                                'string': 'string'
                            }
                        }
                    },
                ],
                'deploymentConfig': {
                    'concurrentDeploymentPercentage': 123,
                    'failureThresholdPercentage': 123
                },
                'failureReason': 'string',
                'failureCode': 'ResourceNotFound'|'FailureThresholdBreached'|'RobotDeploymentNoResponse'|'GreengrassDeploymentFailed'|'MissingRobotArchitecture'|'MissingRobotApplicationArchitecture'|'MissingRobotDeploymentResource'|'GreengrassGroupVersionDoesNotExist'|'ExtractingBundleFailure'|'PreLaunchFileFailure'|'PostLaunchFileFailure'|'BadPermissionError'|'InternalServerError',
                'createdAt': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_fleets(nextToken=None, maxResults=None, filters=None):
    """
    Returns a list of fleets. You can optionally provide filters to retrieve specific fleets.
    See also: AWS API Documentation
    
    
    :example: response = client.list_fleets(
        nextToken='string',
        maxResults=123,
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListFleets request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            

    :type maxResults: integer
    :param maxResults: The maximum number of deployment job results returned by ListFleets in paginated output. When this parameter is used, ListFleets only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListFleets request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListFleets returns up to 100 results and a nextToken value if applicable.

    :type filters: list
    :param filters: Optional filters to limit results.
            (dict) --Information about a filter.
            name (string) --The name of the filter.
            values (list) --A list of values.
            (string) --
            
            

    :rtype: dict
    :return: {
        'fleetDetails': [
            {
                'name': 'string',
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastDeploymentStatus': 'Pending'|'Preparing'|'InProgress'|'Failed'|'Succeeded',
                'lastDeploymentJob': 'string',
                'lastDeploymentTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_robot_applications(versionQualifier=None, nextToken=None, maxResults=None, filters=None):
    """
    Returns a list of robot application. You can optionally provide filters to retrieve specific robot applications.
    See also: AWS API Documentation
    
    
    :example: response = client.list_robot_applications(
        versionQualifier='string',
        nextToken='string',
        maxResults=123,
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type versionQualifier: string
    :param versionQualifier: The version qualifier of the robot application.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListRobotApplications request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            

    :type maxResults: integer
    :param maxResults: The maximum number of deployment job results returned by ListRobotApplications in paginated output. When this parameter is used, ListRobotApplications only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListFleets request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListRobotApplications returns up to 100 results and a nextToken value if applicable.

    :type filters: list
    :param filters: Optional filters to limit results.
            (dict) --Information about a filter.
            name (string) --The name of the filter.
            values (list) --A list of values.
            (string) --
            
            

    :rtype: dict
    :return: {
        'robotApplicationSummaries': [
            {
                'name': 'string',
                'arn': 'string',
                'version': 'string',
                'lastUpdatedAt': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_robots(nextToken=None, maxResults=None, filters=None):
    """
    Returns a list of robots. You can optionally provide filters to retrieve specific robots.
    See also: AWS API Documentation
    
    
    :example: response = client.list_robots(
        nextToken='string',
        maxResults=123,
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListRobots request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            

    :type maxResults: integer
    :param maxResults: The maximum number of deployment job results returned by ListRobots in paginated output. When this parameter is used, ListRobots only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListFleets request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListRobots returns up to 100 results and a nextToken value if applicable.

    :type filters: list
    :param filters: Optional filters to limit results.
            (dict) --Information about a filter.
            name (string) --The name of the filter.
            values (list) --A list of values.
            (string) --
            
            

    :rtype: dict
    :return: {
        'robots': [
            {
                'arn': 'string',
                'name': 'string',
                'fleetArn': 'string',
                'status': 'Available'|'Registered'|'PendingNewDeployment'|'Deploying'|'Failed'|'InSync'|'NoResponse',
                'greenGrassGroupId': 'string',
                'createdAt': datetime(2015, 1, 1),
                'architecture': 'X86_64'|'ARM64'|'ARMHF',
                'lastDeploymentJob': 'string',
                'lastDeploymentTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_simulation_applications(versionQualifier=None, nextToken=None, maxResults=None, filters=None):
    """
    Returns a list of simulation applications. You can optionally provide filters to retrieve specific simulation applications.
    See also: AWS API Documentation
    
    
    :example: response = client.list_simulation_applications(
        versionQualifier='string',
        nextToken='string',
        maxResults=123,
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type versionQualifier: string
    :param versionQualifier: The version qualifier of the simulation application.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListSimulationApplications request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            

    :type maxResults: integer
    :param maxResults: The maximum number of deployment job results returned by ListSimulationApplications in paginated output. When this parameter is used, ListSimulationApplications only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListFleets request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListSimulationApplications returns up to 100 results and a nextToken value if applicable.

    :type filters: list
    :param filters: Optional list of filters to limit results. The only valid filter name is name .
            (dict) --Information about a filter.
            name (string) --The name of the filter.
            values (list) --A list of values.
            (string) --
            
            

    :rtype: dict
    :return: {
        'simulationApplicationSummaries': [
            {
                'name': 'string',
                'arn': 'string',
                'version': 'string',
                'lastUpdatedAt': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_simulation_jobs(nextToken=None, maxResults=None, filters=None):
    """
    Returns a list of simulation jobs. You can optionally provide filters to retrieve specific simulation jobs.
    See also: AWS API Documentation
    
    
    :example: response = client.list_simulation_jobs(
        nextToken='string',
        maxResults=123,
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListSimulationJobs request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            

    :type maxResults: integer
    :param maxResults: The maximum number of deployment job results returned by ListSimulationJobs in paginated output. When this parameter is used, ListSimulationJobs only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListFleets request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListSimulationJobs returns up to 100 results and a nextToken value if applicable.

    :type filters: list
    :param filters: Optional filters to limit results.
            (dict) --Information about a filter.
            name (string) --The name of the filter.
            values (list) --A list of values.
            (string) --
            
            

    :rtype: dict
    :return: {
        'simulationJobSummaries': [
            {
                'arn': 'string',
                'lastUpdatedAt': datetime(2015, 1, 1),
                'name': 'string',
                'status': 'Pending'|'Preparing'|'Running'|'Restarting'|'Completed'|'Failed'|'RunningFailed'|'Terminating'|'Terminated'|'Canceled',
                'simulationApplicationNames': [
                    'string',
                ],
                'robotApplicationNames': [
                    'string',
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def register_robot(fleet=None, robot=None):
    """
    Registers a robot with a fleet.
    See also: AWS API Documentation
    
    
    :example: response = client.register_robot(
        fleet='string',
        robot='string'
    )
    
    
    :type fleet: string
    :param fleet: [REQUIRED]
            The Amazon Resource Name (ARN) of the fleet.
            

    :type robot: string
    :param robot: [REQUIRED]
            The Amazon Resource Name (ARN) of the robot.
            

    :rtype: dict
    :return: {
        'fleet': 'string',
        'robot': 'string'
    }
    
    
    """
    pass

def restart_simulation_job(job=None):
    """
    Restarts a running simulation job.
    See also: AWS API Documentation
    
    
    :example: response = client.restart_simulation_job(
        job='string'
    )
    
    
    :type job: string
    :param job: [REQUIRED]
            The Amazon Resource Name (ARN) of the simulation job.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def sync_deployment_job(clientRequestToken=None, fleet=None):
    """
    Syncrhonizes robots in a fleet to the latest deployment. This is helpful if robots were added after a deployment.
    See also: AWS API Documentation
    
    
    :example: response = client.sync_deployment_job(
        clientRequestToken='string',
        fleet='string'
    )
    
    
    :type clientRequestToken: string
    :param clientRequestToken: [REQUIRED]
            Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
            This field is autopopulated if not provided.
            

    :type fleet: string
    :param fleet: [REQUIRED]
            The target fleet for the synchronization.
            

    :rtype: dict
    :return: {
        'arn': 'string',
        'fleet': 'string',
        'status': 'Pending'|'Preparing'|'InProgress'|'Failed'|'Succeeded',
        'deploymentConfig': {
            'concurrentDeploymentPercentage': 123,
            'failureThresholdPercentage': 123
        },
        'deploymentApplicationConfigs': [
            {
                'application': 'string',
                'applicationVersion': 'string',
                'launchConfig': {
                    'packageName': 'string',
                    'preLaunchFile': 'string',
                    'launchFile': 'string',
                    'postLaunchFile': 'string',
                    'environmentVariables': {
                        'string': 'string'
                    }
                }
            },
        ],
        'failureReason': 'string',
        'failureCode': 'ResourceNotFound'|'FailureThresholdBreached'|'RobotDeploymentNoResponse'|'GreengrassDeploymentFailed'|'MissingRobotArchitecture'|'MissingRobotApplicationArchitecture'|'MissingRobotDeploymentResource'|'GreengrassGroupVersionDoesNotExist'|'ExtractingBundleFailure'|'PreLaunchFileFailure'|'PostLaunchFileFailure'|'BadPermissionError'|'InternalServerError',
        'createdAt': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def update_robot_application(application=None, sources=None, robotSoftwareSuite=None, currentRevisionId=None):
    """
    Updates a robot application.
    See also: AWS API Documentation
    
    
    :example: response = client.update_robot_application(
        application='string',
        sources=[
            {
                's3Bucket': 'string',
                's3Key': 'string',
                'architecture': 'X86_64'|'ARM64'|'ARMHF'
            },
        ],
        robotSoftwareSuite={
            'name': 'ROS',
            'version': 'Kinetic'
        },
        currentRevisionId='string'
    )
    
    
    :type application: string
    :param application: [REQUIRED]
            The application information for the robot application.
            

    :type sources: list
    :param sources: [REQUIRED]
            The sources of the robot application.
            (dict) --Information about a source configuration.
            s3Bucket (string) --The Amazon S3 bucket name.
            s3Key (string) --The s3 object key.
            architecture (string) --The target processor architecture for the application.
            
            

    :type robotSoftwareSuite: dict
    :param robotSoftwareSuite: [REQUIRED]
            The robot software suite used by the robot application.
            name (string) --The name of the robot software suite.
            version (string) --The version of the robot software suite.
            

    :type currentRevisionId: string
    :param currentRevisionId: The revision id for the robot application.

    :rtype: dict
    :return: {
        'arn': 'string',
        'name': 'string',
        'version': 'string',
        'sources': [
            {
                's3Bucket': 'string',
                's3Key': 'string',
                'etag': 'string',
                'architecture': 'X86_64'|'ARM64'|'ARMHF'
            },
        ],
        'robotSoftwareSuite': {
            'name': 'ROS',
            'version': 'Kinetic'
        },
        'lastUpdatedAt': datetime(2015, 1, 1),
        'revisionId': 'string'
    }
    
    
    """
    pass

def update_simulation_application(application=None, sources=None, simulationSoftwareSuite=None, robotSoftwareSuite=None, renderingEngine=None, currentRevisionId=None):
    """
    Updates a simulation application.
    See also: AWS API Documentation
    
    
    :example: response = client.update_simulation_application(
        application='string',
        sources=[
            {
                's3Bucket': 'string',
                's3Key': 'string',
                'architecture': 'X86_64'|'ARM64'|'ARMHF'
            },
        ],
        simulationSoftwareSuite={
            'name': 'Gazebo',
            'version': 'string'
        },
        robotSoftwareSuite={
            'name': 'ROS',
            'version': 'Kinetic'
        },
        renderingEngine={
            'name': 'OGRE',
            'version': 'string'
        },
        currentRevisionId='string'
    )
    
    
    :type application: string
    :param application: [REQUIRED]
            The application information for the simulation application.
            

    :type sources: list
    :param sources: [REQUIRED]
            The sources of the simulation application.
            (dict) --Information about a source configuration.
            s3Bucket (string) --The Amazon S3 bucket name.
            s3Key (string) --The s3 object key.
            architecture (string) --The target processor architecture for the application.
            
            

    :type simulationSoftwareSuite: dict
    :param simulationSoftwareSuite: [REQUIRED]
            The simulation software suite used by the simulation application.
            name (string) --The name of the simulation software suite.
            version (string) --The version of the simulation software suite.
            

    :type robotSoftwareSuite: dict
    :param robotSoftwareSuite: [REQUIRED]
            Information about the robot software suite.
            name (string) --The name of the robot software suite.
            version (string) --The version of the robot software suite.
            

    :type renderingEngine: dict
    :param renderingEngine: [REQUIRED]
            The rendering engine for the simulation application.
            name (string) --The name of the rendering engine.
            version (string) --The version of the rendering engine.
            

    :type currentRevisionId: string
    :param currentRevisionId: The revision id for the robot application.

    :rtype: dict
    :return: {
        'arn': 'string',
        'name': 'string',
        'version': 'string',
        'sources': [
            {
                's3Bucket': 'string',
                's3Key': 'string',
                'etag': 'string',
                'architecture': 'X86_64'|'ARM64'|'ARMHF'
            },
        ],
        'simulationSoftwareSuite': {
            'name': 'Gazebo',
            'version': 'string'
        },
        'robotSoftwareSuite': {
            'name': 'ROS',
            'version': 'Kinetic'
        },
        'renderingEngine': {
            'name': 'OGRE',
            'version': 'string'
        },
        'lastUpdatedAt': datetime(2015, 1, 1),
        'revisionId': 'string'
    }
    
    
    """
    pass

