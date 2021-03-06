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

def create_cluster(clusterName=None, tags=None):
    """
    Creates a new Amazon ECS cluster. By default, your account receives a default cluster when you launch your first container instance. However, you can create your own cluster with a unique name with the CreateCluster action.
    See also: AWS API Documentation
    
    Examples
    This example creates a cluster in your default region.
    Expected Output:
    
    :example: response = client.create_cluster(
        clusterName='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type clusterName: string
    :param clusterName: The name of your cluster. If you do not specify a name for your cluster, you create a cluster named default . Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.

    :type tags: list
    :param tags: The metadata that you apply to the cluster to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
            (dict) --The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
            key (string) --One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.
            value (string) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).
            
            

    :rtype: dict
    :return: {
        'cluster': {
            'clusterArn': 'string',
            'clusterName': 'string',
            'status': 'string',
            'registeredContainerInstancesCount': 123,
            'runningTasksCount': 123,
            'pendingTasksCount': 123,
            'activeServicesCount': 123,
            'statistics': [
                {
                    'name': 'string',
                    'value': 'string'
                },
            ],
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    runningEC2TasksCount
    RunningFargateTasksCount
    pendingEC2TasksCount
    pendingFargateTasksCount
    activeEC2ServiceCount
    activeFargateServiceCount
    drainingEC2ServiceCount
    drainingFargateServiceCount
    
    """
    pass

def create_service(cluster=None, serviceName=None, taskDefinition=None, loadBalancers=None, serviceRegistries=None, desiredCount=None, clientToken=None, launchType=None, platformVersion=None, role=None, deploymentConfiguration=None, placementConstraints=None, placementStrategy=None, networkConfiguration=None, healthCheckGracePeriodSeconds=None, schedulingStrategy=None, deploymentController=None, tags=None, enableECSManagedTags=None, propagateTags=None):
    """
    Runs and maintains a desired number of tasks from a specified task definition. If the number of tasks running in a service drops below desiredCount , Amazon ECS spawns another copy of the task in the specified cluster. To update an existing service, see  UpdateService .
    In addition to maintaining the desired count of tasks in your service, you can optionally run your service behind a load balancer. The load balancer distributes traffic across the tasks that are associated with the service. For more information, see Service Load Balancing in the Amazon Elastic Container Service Developer Guide .
    You can optionally specify a deployment configuration for your service. The deployment is triggered by changing properties, such as the task definition or the desired count of a service, with an  UpdateService operation.
    If a service is using the ECS deployment controller, the minimum healthy percent represents a lower limit on the number of tasks in a service that must remain in the RUNNING state during a deployment, as a percentage of the desired number of tasks (rounded up to the nearest integer), and while any container instances are in the DRAINING state if the service contains tasks using the EC2 launch type. This parameter enables you to deploy without using additional cluster capacity. For example, if your service has a desired number of four tasks and a minimum healthy percent of 50%, the scheduler may stop two existing tasks to free up cluster capacity before starting two new tasks. Tasks for services that do not use a load balancer are considered healthy if they are in the RUNNING state; tasks for services that do use a load balancer are considered healthy if they are in the RUNNING state and they are reported as healthy by the load balancer. The default value for minimum healthy percent is 100%.
    If a service is using the ECS deployment controller, the maximum percent parameter represents an upper limit on the number of tasks in a service that are allowed in the RUNNING or PENDING state during a deployment, as a percentage of the desired number of tasks (rounded down to the nearest integer), and while any container instances are in the DRAINING state if the service contains tasks using the EC2 launch type. This parameter enables you to define the deployment batch size. For example, if your service has a desired number of four tasks and a maximum percent value of 200%, the scheduler may start four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available). The default value for maximum percent is 200%.
    If a service is using the CODE_DEPLOY deployment controller and tasks that use the EC2 launch type, the minimum healthy percent and maximum percent values are only used to define the lower and upper limit on the number of the tasks in the service that remain in the RUNNING state while the container instances are in the DRAINING state. If the tasks in the service use the Fargate launch type, the minimum healthy percent and maximum percent values are not used, although they are currently visible when describing your service.
    Tasks for services that do not use a load balancer are considered healthy if they are in the RUNNING state. Tasks for services that do use a load balancer are considered healthy if they are in the RUNNING state and the container instance they are hosted on is reported as healthy by the load balancer. The default value for a replica service for minimumHealthyPercent is 100%. The default value for a daemon service for minimumHealthyPercent is 0%.
    When the service scheduler launches new tasks, it determines task placement in your cluster using the following logic:
    See also: AWS API Documentation
    
    Examples
    This example creates a service in your default region called ecs-simple-service. The service uses the hello_world task definition and it maintains 10 copies of that task.
    Expected Output:
    This example creates a service in your default region called ecs-simple-service-elb. The service uses the ecs-demo task definition and it maintains 10 copies of that task. You must reference an existing load balancer in the same region by its name.
    Expected Output:
    
    :example: response = client.create_service(
        cluster='string',
        serviceName='string',
        taskDefinition='string',
        loadBalancers=[
            {
                'targetGroupArn': 'string',
                'loadBalancerName': 'string',
                'containerName': 'string',
                'containerPort': 123
            },
        ],
        serviceRegistries=[
            {
                'registryArn': 'string',
                'port': 123,
                'containerName': 'string',
                'containerPort': 123
            },
        ],
        desiredCount=123,
        clientToken='string',
        launchType='EC2'|'FARGATE',
        platformVersion='string',
        role='string',
        deploymentConfiguration={
            'maximumPercent': 123,
            'minimumHealthyPercent': 123
        },
        placementConstraints=[
            {
                'type': 'distinctInstance'|'memberOf',
                'expression': 'string'
            },
        ],
        placementStrategy=[
            {
                'type': 'random'|'spread'|'binpack',
                'field': 'string'
            },
        ],
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': [
                    'string',
                ],
                'securityGroups': [
                    'string',
                ],
                'assignPublicIp': 'ENABLED'|'DISABLED'
            }
        },
        healthCheckGracePeriodSeconds=123,
        schedulingStrategy='REPLICA'|'DAEMON',
        deploymentController={
            'type': 'ECS'|'CODE_DEPLOY'
        },
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        enableECSManagedTags=True|False,
        propagateTags='TASK_DEFINITION'|'SERVICE'
    )
    
    
    :type cluster: string
    :param cluster: The short name or full Amazon Resource Name (ARN) of the cluster on which to run your service. If you do not specify a cluster, the default cluster is assumed.

    :type serviceName: string
    :param serviceName: [REQUIRED]
            The name of your service. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. Service names must be unique within a cluster, but you can have similarly named services in multiple clusters within a Region or across multiple Regions.
            

    :type taskDefinition: string
    :param taskDefinition: [REQUIRED]
            The family and revision (family:revision ) or full ARN of the task definition to run in your service. If a revision is not specified, the latest ACTIVE revision is used.
            

    :type loadBalancers: list
    :param loadBalancers: A load balancer object representing the load balancer to use with your service.
            If the service is using the ECS deployment controller, you are limited to one load balancer or target group.
            If the service is using the CODE_DEPLOY deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When creating an AWS CodeDeploy deployment group, you specify two target groups (referred to as a targetGroupPair ). During a deployment, AWS CodeDeploy determines which task set in your service has the status PRIMARY and associates one target group with it, and then associates the other target group with the replacement task set. The load balancer can also have up to two listeners: a required listener for production traffic and an optional listener that allows you perform validation tests with Lambda functions before routing production traffic to it.
            After you create a service using the ECS deployment controller, the load balancer name or target group ARN, container name, and container port specified in the service definition are immutable. If you are using the CODE_DEPLOY deployment controller, these values can be changed when updating the service.
            For Classic Load Balancers, this object must contain the load balancer name, the container name (as it appears in a container definition), and the container port to access from the load balancer. When a task from this service is placed on a container instance, the container instance is registered with the load balancer specified here.
            For Application Load Balancers and Network Load Balancers, this object must contain the load balancer target group ARN, the container name (as it appears in a container definition), and the container port to access from the load balancer. When a task from this service is placed on a container instance, the container instance and port combination is registered as a target in the target group specified here.
            Services with tasks that use the awsvpc network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers are not supported. Also, when you create any target groups for these services, you must choose ip as the target type, not instance , because tasks that use the awsvpc network mode are associated with an elastic network interface, not an Amazon EC2 instance.
            (dict) --Details on a load balancer that is used with a service.
            If the service is using the ECS deployment controller, you are limited to one load balancer or target group.
            If the service is using the CODE_DEPLOY deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When you are creating an AWS CodeDeploy deployment group, you specify two target groups (referred to as a targetGroupPair ). Each target group binds to a separate task set in the deployment. The load balancer can also have up to two listeners, a required listener for production traffic and an optional listener that allows you to test new revisions of the service before routing production traffic to it.
            Services with tasks that use the awsvpc network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers are not supported. Also, when you create any target groups for these services, you must choose ip as the target type, not instance . Tasks that use the awsvpc network mode are associated with an elastic network interface, not an Amazon EC2 instance.
            targetGroupArn (string) --The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group or groups associated with a service. For services using the ECS deployment controller, you are limited to one target group. For services using the CODE_DEPLOY deployment controller, you are required to define two target groups for the load balancer.
            Warning
            If your service's task definition uses the awsvpc network mode (which is required for the Fargate launch type), you must choose ip as the target type, not instance , because tasks that use the awsvpc network mode are associated with an elastic network interface, not an Amazon EC2 instance.
            loadBalancerName (string) --The name of a load balancer.
            containerName (string) --The name of the container (as it appears in a container definition) to associate with the load balancer.
            containerPort (integer) --The port on the container to associate with the load balancer. This port must correspond to a containerPort in the service's task definition. Your container instances must allow ingress traffic on the hostPort of the port mapping.
            
            

    :type serviceRegistries: list
    :param serviceRegistries: The details of the service discovery registries to assign to this service. For more information, see Service Discovery .
            Note
            Service discovery is supported for Fargate tasks if you are using platform version v1.1.0 or later. For more information, see AWS Fargate Platform Versions .
            (dict) --Details of the service registry.
            registryArn (string) --The Amazon Resource Name (ARN) of the service registry. The currently supported service registry is Amazon Route 53 Auto Naming. For more information, see Service .
            port (integer) --The port value used if your service discovery service specified an SRV record. This field may be used if both the awsvpc network mode and SRV records are used.
            containerName (string) --The container name value, already specified in the task definition, to be used for your service discovery service. If the task definition that your service task specifies uses the bridge or host network mode, you must specify a containerName and containerPort combination from the task definition. If the task definition that your service task specifies uses the awsvpc network mode and a type SRV DNS record is used, you must specify either a containerName and containerPort combination or a port value, but not both.
            containerPort (integer) --The port value, already specified in the task definition, to be used for your service discovery service. If the task definition your service task specifies uses the bridge or host network mode, you must specify a containerName and containerPort combination from the task definition. If the task definition your service task specifies uses the awsvpc network mode and a type SRV DNS record is used, you must specify either a containerName and containerPort combination or a port value, but not both.
            
            

    :type desiredCount: integer
    :param desiredCount: The number of instantiations of the specified task definition to place and keep running on your cluster.

    :type clientToken: string
    :param clientToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 32 ASCII characters are allowed.

    :type launchType: string
    :param launchType: The launch type on which to run your service. For more information, see Amazon ECS Launch Types in the Amazon Elastic Container Service Developer Guide .

    :type platformVersion: string
    :param platformVersion: The platform version on which your tasks in the service are running. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the LATEST platform version is used by default. For more information, see AWS Fargate Platform Versions in the Amazon Elastic Container Service Developer Guide .

    :type role: string
    :param role: The name or full Amazon Resource Name (ARN) of the IAM role that allows Amazon ECS to make calls to your load balancer on your behalf. This parameter is only permitted if you are using a load balancer with your service and your task definition does not use the awsvpc network mode. If you specify the role parameter, you must also specify a load balancer object with the loadBalancers parameter.
            Warning
            If your account has already created the Amazon ECS service-linked role, that role is used by default for your service unless you specify a role here. The service-linked role is required if your task definition uses the awsvpc network mode, in which case you should not specify a role here. For more information, see Using Service-Linked Roles for Amazon ECS in the Amazon Elastic Container Service Developer Guide .
            If your specified role has a path other than / , then you must either specify the full role ARN (this is recommended) or prefix the role name with the path. For example, if a role with the name bar has a path of /foo/ then you would specify /foo/bar as the role name. For more information, see Friendly Names and Paths in the IAM User Guide .
            

    :type deploymentConfiguration: dict
    :param deploymentConfiguration: Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.
            maximumPercent (integer) --If a service is using the rolling update (ECS ) deployment type, the maximum percent parameter represents an upper limit on the number of tasks in a service that are allowed in the RUNNING or PENDING state during a deployment, as a percentage of the desired number of tasks (rounded down to the nearest integer), and while any container instances are in the DRAINING state if the service contains tasks using the EC2 launch type. This parameter enables you to define the deployment batch size. For example, if your service has a desired number of four tasks and a maximum percent value of 200%, the scheduler may start four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available). The default value for maximum percent is 200%.
            If a service is using the blue/green (CODE_DEPLOY ) deployment type and tasks that use the EC2 launch type, the maximum percent value is set to the default value and is used to define the upper limit on the number of the tasks in the service that remain in the RUNNING state while the container instances are in the DRAINING state. If the tasks in the service use the Fargate launch type, the maximum percent value is not used, although it is returned when describing your service.
            minimumHealthyPercent (integer) --If a service is using the rolling update (ECS ) deployment type, the minimum healthy percent represents a lower limit on the number of tasks in a service that must remain in the RUNNING state during a deployment, as a percentage of the desired number of tasks (rounded up to the nearest integer), and while any container instances are in the DRAINING state if the service contains tasks using the EC2 launch type. This parameter enables you to deploy without using additional cluster capacity. For example, if your service has a desired number of four tasks and a minimum healthy percent of 50%, the scheduler may stop two existing tasks to free up cluster capacity before starting two new tasks. Tasks for services that do not use a load balancer are considered healthy if they are in the RUNNING state; tasks for services that do use a load balancer are considered healthy if they are in the RUNNING state and they are reported as healthy by the load balancer. The default value for minimum healthy percent is 100%.
            If a service is using the blue/green (CODE_DEPLOY ) deployment type and tasks that use the EC2 launch type, the minimum healthy percent value is set to the default value and is used to define the lower limit on the number of the tasks in the service that remain in the RUNNING state while the container instances are in the DRAINING state. If the tasks in the service use the Fargate launch type, the minimum healthy percent value is not used, although it is returned when describing your service.
            

    :type placementConstraints: list
    :param placementConstraints: An array of placement constraint objects to use for tasks in your service. You can specify a maximum of 10 constraints per task (this limit includes constraints in the task definition and those specified at runtime).
            (dict) --An object representing a constraint on task placement. For more information, see Task Placement Constraints in the Amazon Elastic Container Service Developer Guide .
            type (string) --The type of constraint. Use distinctInstance to ensure that each task in a particular group is running on a different container instance. Use memberOf to restrict the selection to a group of valid candidates. The value distinctInstance is not supported in task definitions.
            expression (string) --A cluster query language expression to apply to the constraint. You cannot specify an expression if the constraint type is distinctInstance . For more information, see Cluster Query Language in the Amazon Elastic Container Service Developer Guide .
            
            

    :type placementStrategy: list
    :param placementStrategy: The placement strategy objects to use for tasks in your service. You can specify a maximum of five strategy rules per service.
            (dict) --The task placement strategy for a task or service. For more information, see Task Placement Strategies in the Amazon Elastic Container Service Developer Guide .
            type (string) --The type of placement strategy. The random placement strategy randomly places tasks on available candidates. The spread placement strategy spreads placement across available candidates evenly based on the field parameter. The binpack strategy places tasks on available candidates that have the least available amount of the resource that is specified with the field parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task).
            field (string) --The field to apply the placement strategy against. For the spread placement strategy, valid values are instanceId (or host , which has the same effect), or any platform or custom attribute that is applied to a container instance, such as attribute:ecs.availability-zone . For the binpack placement strategy, valid values are cpu and memory . For the random placement strategy, this field is not used.
            
            

    :type networkConfiguration: dict
    :param networkConfiguration: The network configuration for the service. This parameter is required for task definitions that use the awsvpc network mode to receive their own elastic network interface, and it is not supported for other network modes. For more information, see Task Networking in the Amazon Elastic Container Service Developer Guide .
            awsvpcConfiguration (dict) --The VPC subnets and security groups associated with a task.
            Note
            All specified subnets and security groups must be from the same VPC.
            subnets (list) -- [REQUIRED]The subnets associated with the task or service. There is a limit of 16 subnets able to be specified per AwsVpcConfiguration .
            Note
            All specified subnets must be from the same VPC.
            (string) --
            securityGroups (list) --The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of five security groups able to be specified per AwsVpcConfiguration .
            Note
            All specified security groups must be from the same VPC.
            (string) --
            assignPublicIp (string) --Whether the task's elastic network interface receives a public IP address. The default value is DISABLED .
            
            

    :type healthCheckGracePeriodSeconds: integer
    :param healthCheckGracePeriodSeconds: The period of time, in seconds, that the Amazon ECS service scheduler should ignore unhealthy Elastic Load Balancing target health checks after a task has first started. This is only valid if your service is configured to use a load balancer. If your service's tasks take a while to start and respond to Elastic Load Balancing health checks, you can specify a health check grace period of up to 7,200 seconds. During that time, the ECS service scheduler ignores health check status. This grace period can prevent the ECS service scheduler from marking tasks as unhealthy and stopping them before they have time to come up.

    :type schedulingStrategy: string
    :param schedulingStrategy: The scheduling strategy to use for the service. For more information, see Services .
            There are two service scheduler strategies available:
            REPLICA -The replica scheduling strategy places and maintains the desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions. This scheduler strategy is required if using the CODE_DEPLOY deployment controller.
            DAEMON -The daemon scheduling strategy deploys exactly one task on each active container instance that meets all of the task placement constraints that you specify in your cluster. When you are using this strategy, there is no need to specify a desired number of tasks, a task placement strategy, or use Service Auto Scaling policies.
            Note
            Tasks using the Fargate launch type or the CODE_DEPLOY deploymenet controller do not support the DAEMON scheduling strategy.
            

    :type deploymentController: dict
    :param deploymentController: The deployment controller to use for the service.
            type (string) -- [REQUIRED]The deployment controller type to use.
            There are two deployment controller types available:
            ECS
            The rolling update (ECS ) deployment type involves replacing the current running version of the container with the latest version. The number of containers Amazon ECS adds or removes from the service during a rolling update is controlled by adjusting the minimum and maximum number of healthy tasks allowed during a service deployment, as specified in the DeploymentConfiguration .
            CODE_DEPLOY
            The blue/green (CODE_DEPLOY ) deployment type uses the blue/green deployment model powered by AWS CodeDeploy, which allows you to verify a new deployment of a service before sending production traffic to it. For more information, see Amazon ECS Deployment Types in the Amazon Elastic Container Service Developer Guide .
            

    :type tags: list
    :param tags: The metadata that you apply to the service to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. When a service is deleted, the tags are deleted as well. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
            (dict) --The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
            key (string) --One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.
            value (string) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).
            
            

    :type enableECSManagedTags: boolean
    :param enableECSManagedTags: Specifies whether to enable Amazon ECS managed tags for the tasks within the service. For more information, see Tagging Your Amazon ECS Resources in the Amazon Elastic Container Service Developer Guide .

    :type propagateTags: string
    :param propagateTags: Specifies whether to propagate the tags from the task definition or the service to the tasks. If no value is specified, the tags are not propagated. Tags can only be propagated to the tasks within the service during service creation. To add tags to a task after service creation, use the TagResource API action.

    :rtype: dict
    :return: {
        'service': {
            'serviceArn': 'string',
            'serviceName': 'string',
            'clusterArn': 'string',
            'loadBalancers': [
                {
                    'targetGroupArn': 'string',
                    'loadBalancerName': 'string',
                    'containerName': 'string',
                    'containerPort': 123
                },
            ],
            'serviceRegistries': [
                {
                    'registryArn': 'string',
                    'port': 123,
                    'containerName': 'string',
                    'containerPort': 123
                },
            ],
            'status': 'string',
            'desiredCount': 123,
            'runningCount': 123,
            'pendingCount': 123,
            'launchType': 'EC2'|'FARGATE',
            'platformVersion': 'string',
            'taskDefinition': 'string',
            'deploymentConfiguration': {
                'maximumPercent': 123,
                'minimumHealthyPercent': 123
            },
            'taskSets': [
                {
                    'id': 'string',
                    'taskSetArn': 'string',
                    'startedBy': 'string',
                    'externalId': 'string',
                    'status': 'string',
                    'taskDefinition': 'string',
                    'computedDesiredCount': 123,
                    'pendingCount': 123,
                    'runningCount': 123,
                    'createdAt': datetime(2015, 1, 1),
                    'updatedAt': datetime(2015, 1, 1),
                    'launchType': 'EC2'|'FARGATE',
                    'platformVersion': 'string',
                    'networkConfiguration': {
                        'awsvpcConfiguration': {
                            'subnets': [
                                'string',
                            ],
                            'securityGroups': [
                                'string',
                            ],
                            'assignPublicIp': 'ENABLED'|'DISABLED'
                        }
                    },
                    'loadBalancers': [
                        {
                            'targetGroupArn': 'string',
                            'loadBalancerName': 'string',
                            'containerName': 'string',
                            'containerPort': 123
                        },
                    ],
                    'scale': {
                        'value': 123.0,
                        'unit': 'PERCENT'
                    },
                    'stabilityStatus': 'STEADY_STATE'|'STABILIZING',
                    'stabilityStatusAt': datetime(2015, 1, 1)
                },
            ],
            'deployments': [
                {
                    'id': 'string',
                    'status': 'string',
                    'taskDefinition': 'string',
                    'desiredCount': 123,
                    'pendingCount': 123,
                    'runningCount': 123,
                    'createdAt': datetime(2015, 1, 1),
                    'updatedAt': datetime(2015, 1, 1),
                    'launchType': 'EC2'|'FARGATE',
                    'platformVersion': 'string',
                    'networkConfiguration': {
                        'awsvpcConfiguration': {
                            'subnets': [
                                'string',
                            ],
                            'securityGroups': [
                                'string',
                            ],
                            'assignPublicIp': 'ENABLED'|'DISABLED'
                        }
                    }
                },
            ],
            'roleArn': 'string',
            'events': [
                {
                    'id': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'message': 'string'
                },
            ],
            'createdAt': datetime(2015, 1, 1),
            'placementConstraints': [
                {
                    'type': 'distinctInstance'|'memberOf',
                    'expression': 'string'
                },
            ],
            'placementStrategy': [
                {
                    'type': 'random'|'spread'|'binpack',
                    'field': 'string'
                },
            ],
            'networkConfiguration': {
                'awsvpcConfiguration': {
                    'subnets': [
                        'string',
                    ],
                    'securityGroups': [
                        'string',
                    ],
                    'assignPublicIp': 'ENABLED'|'DISABLED'
                }
            },
            'healthCheckGracePeriodSeconds': 123,
            'schedulingStrategy': 'REPLICA'|'DAEMON',
            'deploymentController': {
                'type': 'ECS'|'CODE_DEPLOY'
            },
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'createdBy': 'string',
            'enableECSManagedTags': True|False,
            'propagateTags': 'TASK_DEFINITION'|'SERVICE'
        }
    }
    
    
    :returns: 
    cluster (string) -- The short name or full Amazon Resource Name (ARN) of the cluster on which to run your service. If you do not specify a cluster, the default cluster is assumed.
    serviceName (string) -- [REQUIRED]
    The name of your service. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. Service names must be unique within a cluster, but you can have similarly named services in multiple clusters within a Region or across multiple Regions.
    
    taskDefinition (string) -- [REQUIRED]
    The family and revision (family:revision ) or full ARN of the task definition to run in your service. If a revision is not specified, the latest ACTIVE revision is used.
    
    loadBalancers (list) -- A load balancer object representing the load balancer to use with your service.
    If the service is using the ECS deployment controller, you are limited to one load balancer or target group.
    If the service is using the CODE_DEPLOY deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When creating an AWS CodeDeploy deployment group, you specify two target groups (referred to as a targetGroupPair ). During a deployment, AWS CodeDeploy determines which task set in your service has the status PRIMARY and associates one target group with it, and then associates the other target group with the replacement task set. The load balancer can also have up to two listeners: a required listener for production traffic and an optional listener that allows you perform validation tests with Lambda functions before routing production traffic to it.
    After you create a service using the ECS deployment controller, the load balancer name or target group ARN, container name, and container port specified in the service definition are immutable. If you are using the CODE_DEPLOY deployment controller, these values can be changed when updating the service.
    For Classic Load Balancers, this object must contain the load balancer name, the container name (as it appears in a container definition), and the container port to access from the load balancer. When a task from this service is placed on a container instance, the container instance is registered with the load balancer specified here.
    For Application Load Balancers and Network Load Balancers, this object must contain the load balancer target group ARN, the container name (as it appears in a container definition), and the container port to access from the load balancer. When a task from this service is placed on a container instance, the container instance and port combination is registered as a target in the target group specified here.
    Services with tasks that use the awsvpc network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers are not supported. Also, when you create any target groups for these services, you must choose ip as the target type, not instance , because tasks that use the awsvpc network mode are associated with an elastic network interface, not an Amazon EC2 instance.
    
    (dict) --Details on a load balancer that is used with a service.
    If the service is using the ECS deployment controller, you are limited to one load balancer or target group.
    If the service is using the CODE_DEPLOY deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When you are creating an AWS CodeDeploy deployment group, you specify two target groups (referred to as a targetGroupPair ). Each target group binds to a separate task set in the deployment. The load balancer can also have up to two listeners, a required listener for production traffic and an optional listener that allows you to test new revisions of the service before routing production traffic to it.
    Services with tasks that use the awsvpc network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers are not supported. Also, when you create any target groups for these services, you must choose ip as the target type, not instance . Tasks that use the awsvpc network mode are associated with an elastic network interface, not an Amazon EC2 instance.
    
    targetGroupArn (string) --The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group or groups associated with a service. For services using the ECS deployment controller, you are limited to one target group. For services using the CODE_DEPLOY deployment controller, you are required to define two target groups for the load balancer.
    
    Warning
    If your service's task definition uses the awsvpc network mode (which is required for the Fargate launch type), you must choose ip as the target type, not instance , because tasks that use the awsvpc network mode are associated with an elastic network interface, not an Amazon EC2 instance.
    
    
    loadBalancerName (string) --The name of a load balancer.
    
    containerName (string) --The name of the container (as it appears in a container definition) to associate with the load balancer.
    
    containerPort (integer) --The port on the container to associate with the load balancer. This port must correspond to a containerPort in the service's task definition. Your container instances must allow ingress traffic on the hostPort of the port mapping.
    
    
    
    
    
    serviceRegistries (list) -- The details of the service discovery registries to assign to this service. For more information, see Service Discovery .
    
    Note
    Service discovery is supported for Fargate tasks if you are using platform version v1.1.0 or later. For more information, see AWS Fargate Platform Versions .
    
    
    (dict) --Details of the service registry.
    
    registryArn (string) --The Amazon Resource Name (ARN) of the service registry. The currently supported service registry is Amazon Route 53 Auto Naming. For more information, see Service .
    
    port (integer) --The port value used if your service discovery service specified an SRV record. This field may be used if both the awsvpc network mode and SRV records are used.
    
    containerName (string) --The container name value, already specified in the task definition, to be used for your service discovery service. If the task definition that your service task specifies uses the bridge or host network mode, you must specify a containerName and containerPort combination from the task definition. If the task definition that your service task specifies uses the awsvpc network mode and a type SRV DNS record is used, you must specify either a containerName and containerPort combination or a port value, but not both.
    
    containerPort (integer) --The port value, already specified in the task definition, to be used for your service discovery service. If the task definition your service task specifies uses the bridge or host network mode, you must specify a containerName and containerPort combination from the task definition. If the task definition your service task specifies uses the awsvpc network mode and a type SRV DNS record is used, you must specify either a containerName and containerPort combination or a port value, but not both.
    
    
    
    
    
    desiredCount (integer) -- The number of instantiations of the specified task definition to place and keep running on your cluster.
    clientToken (string) -- Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 32 ASCII characters are allowed.
    launchType (string) -- The launch type on which to run your service. For more information, see Amazon ECS Launch Types in the Amazon Elastic Container Service Developer Guide .
    platformVersion (string) -- The platform version on which your tasks in the service are running. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the LATEST platform version is used by default. For more information, see AWS Fargate Platform Versions in the Amazon Elastic Container Service Developer Guide .
    role (string) -- The name or full Amazon Resource Name (ARN) of the IAM role that allows Amazon ECS to make calls to your load balancer on your behalf. This parameter is only permitted if you are using a load balancer with your service and your task definition does not use the awsvpc network mode. If you specify the role parameter, you must also specify a load balancer object with the loadBalancers parameter.
    
    Warning
    If your account has already created the Amazon ECS service-linked role, that role is used by default for your service unless you specify a role here. The service-linked role is required if your task definition uses the awsvpc network mode, in which case you should not specify a role here. For more information, see Using Service-Linked Roles for Amazon ECS in the Amazon Elastic Container Service Developer Guide .
    
    If your specified role has a path other than / , then you must either specify the full role ARN (this is recommended) or prefix the role name with the path. For example, if a role with the name bar has a path of /foo/ then you would specify /foo/bar as the role name. For more information, see Friendly Names and Paths in the IAM User Guide .
    
    deploymentConfiguration (dict) -- Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.
    
    maximumPercent (integer) --If a service is using the rolling update (ECS ) deployment type, the maximum percent parameter represents an upper limit on the number of tasks in a service that are allowed in the RUNNING or PENDING state during a deployment, as a percentage of the desired number of tasks (rounded down to the nearest integer), and while any container instances are in the DRAINING state if the service contains tasks using the EC2 launch type. This parameter enables you to define the deployment batch size. For example, if your service has a desired number of four tasks and a maximum percent value of 200%, the scheduler may start four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available). The default value for maximum percent is 200%.
    If a service is using the blue/green (CODE_DEPLOY ) deployment type and tasks that use the EC2 launch type, the maximum percent value is set to the default value and is used to define the upper limit on the number of the tasks in the service that remain in the RUNNING state while the container instances are in the DRAINING state. If the tasks in the service use the Fargate launch type, the maximum percent value is not used, although it is returned when describing your service.
    
    minimumHealthyPercent (integer) --If a service is using the rolling update (ECS ) deployment type, the minimum healthy percent represents a lower limit on the number of tasks in a service that must remain in the RUNNING state during a deployment, as a percentage of the desired number of tasks (rounded up to the nearest integer), and while any container instances are in the DRAINING state if the service contains tasks using the EC2 launch type. This parameter enables you to deploy without using additional cluster capacity. For example, if your service has a desired number of four tasks and a minimum healthy percent of 50%, the scheduler may stop two existing tasks to free up cluster capacity before starting two new tasks. Tasks for services that do not use a load balancer are considered healthy if they are in the RUNNING state; tasks for services that do use a load balancer are considered healthy if they are in the RUNNING state and they are reported as healthy by the load balancer. The default value for minimum healthy percent is 100%.
    If a service is using the blue/green (CODE_DEPLOY ) deployment type and tasks that use the EC2 launch type, the minimum healthy percent value is set to the default value and is used to define the lower limit on the number of the tasks in the service that remain in the RUNNING state while the container instances are in the DRAINING state. If the tasks in the service use the Fargate launch type, the minimum healthy percent value is not used, although it is returned when describing your service.
    
    
    
    placementConstraints (list) -- An array of placement constraint objects to use for tasks in your service. You can specify a maximum of 10 constraints per task (this limit includes constraints in the task definition and those specified at runtime).
    
    (dict) --An object representing a constraint on task placement. For more information, see Task Placement Constraints in the Amazon Elastic Container Service Developer Guide .
    
    type (string) --The type of constraint. Use distinctInstance to ensure that each task in a particular group is running on a different container instance. Use memberOf to restrict the selection to a group of valid candidates. The value distinctInstance is not supported in task definitions.
    
    expression (string) --A cluster query language expression to apply to the constraint. You cannot specify an expression if the constraint type is distinctInstance . For more information, see Cluster Query Language in the Amazon Elastic Container Service Developer Guide .
    
    
    
    
    
    placementStrategy (list) -- The placement strategy objects to use for tasks in your service. You can specify a maximum of five strategy rules per service.
    
    (dict) --The task placement strategy for a task or service. For more information, see Task Placement Strategies in the Amazon Elastic Container Service Developer Guide .
    
    type (string) --The type of placement strategy. The random placement strategy randomly places tasks on available candidates. The spread placement strategy spreads placement across available candidates evenly based on the field parameter. The binpack strategy places tasks on available candidates that have the least available amount of the resource that is specified with the field parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task).
    
    field (string) --The field to apply the placement strategy against. For the spread placement strategy, valid values are instanceId (or host , which has the same effect), or any platform or custom attribute that is applied to a container instance, such as attribute:ecs.availability-zone . For the binpack placement strategy, valid values are cpu and memory . For the random placement strategy, this field is not used.
    
    
    
    
    
    networkConfiguration (dict) -- The network configuration for the service. This parameter is required for task definitions that use the awsvpc network mode to receive their own elastic network interface, and it is not supported for other network modes. For more information, see Task Networking in the Amazon Elastic Container Service Developer Guide .
    
    awsvpcConfiguration (dict) --The VPC subnets and security groups associated with a task.
    
    Note
    All specified subnets and security groups must be from the same VPC.
    
    
    subnets (list) -- [REQUIRED]The subnets associated with the task or service. There is a limit of 16 subnets able to be specified per AwsVpcConfiguration .
    
    Note
    All specified subnets must be from the same VPC.
    
    
    (string) --
    
    
    securityGroups (list) --The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of five security groups able to be specified per AwsVpcConfiguration .
    
    Note
    All specified security groups must be from the same VPC.
    
    
    (string) --
    
    
    assignPublicIp (string) --Whether the task's elastic network interface receives a public IP address. The default value is DISABLED .
    
    
    
    
    
    healthCheckGracePeriodSeconds (integer) -- The period of time, in seconds, that the Amazon ECS service scheduler should ignore unhealthy Elastic Load Balancing target health checks after a task has first started. This is only valid if your service is configured to use a load balancer. If your service's tasks take a while to start and respond to Elastic Load Balancing health checks, you can specify a health check grace period of up to 7,200 seconds. During that time, the ECS service scheduler ignores health check status. This grace period can prevent the ECS service scheduler from marking tasks as unhealthy and stopping them before they have time to come up.
    schedulingStrategy (string) -- The scheduling strategy to use for the service. For more information, see Services .
    There are two service scheduler strategies available:
    
    REPLICA -The replica scheduling strategy places and maintains the desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions. This scheduler strategy is required if using the CODE_DEPLOY deployment controller.
    DAEMON -The daemon scheduling strategy deploys exactly one task on each active container instance that meets all of the task placement constraints that you specify in your cluster. When you are using this strategy, there is no need to specify a desired number of tasks, a task placement strategy, or use Service Auto Scaling policies.
    
    
    Note
    Tasks using the Fargate launch type or the CODE_DEPLOY deploymenet controller do not support the DAEMON scheduling strategy.
    
    
    deploymentController (dict) -- The deployment controller to use for the service.
    
    type (string) -- [REQUIRED]The deployment controller type to use.
    There are two deployment controller types available:
    
    ECS
    The rolling update (ECS ) deployment type involves replacing the current running version of the container with the latest version. The number of containers Amazon ECS adds or removes from the service during a rolling update is controlled by adjusting the minimum and maximum number of healthy tasks allowed during a service deployment, as specified in the  DeploymentConfiguration .
    
    CODE_DEPLOY
    The blue/green (CODE_DEPLOY ) deployment type uses the blue/green deployment model powered by AWS CodeDeploy, which allows you to verify a new deployment of a service before sending production traffic to it. For more information, see Amazon ECS Deployment Types in the Amazon Elastic Container Service Developer Guide .
    
    
    
    tags (list) -- The metadata that you apply to the service to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. When a service is deleted, the tags are deleted as well. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
    
    (dict) --The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
    
    key (string) --One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.
    
    value (string) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).
    
    
    
    
    
    enableECSManagedTags (boolean) -- Specifies whether to enable Amazon ECS managed tags for the tasks within the service. For more information, see Tagging Your Amazon ECS Resources in the Amazon Elastic Container Service Developer Guide .
    propagateTags (string) -- Specifies whether to propagate the tags from the task definition or the service to the tasks. If no value is specified, the tags are not propagated. Tags can only be propagated to the tasks within the service during service creation. To add tags to a task after service creation, use the  TagResource API action.
    
    """
    pass

def delete_account_setting(name=None, principalArn=None):
    """
    Modifies the ARN and resource ID format of a resource for a specified IAM user, IAM role, or the root user for an account. You can specify whether the new ARN and resource ID format are disabled for new resources that are created.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_account_setting(
        name='serviceLongArnFormat'|'taskLongArnFormat'|'containerInstanceLongArnFormat',
        principalArn='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The resource name for which to disable the new format. If serviceLongArnFormat is specified, the ARN for your Amazon ECS services is affected. If taskLongArnFormat is specified, the ARN and resource ID for your Amazon ECS tasks is affected. If containerInstanceLongArnFormat is specified, the ARN and resource ID for your Amazon ECS container instances is affected.
            

    :type principalArn: string
    :param principalArn: The ARN of the principal, which can be an IAM user, IAM role, or the root user. If you specify the root user, it modifies the ARN and resource ID format for all IAM users, IAM roles, and the root user of the account unless an IAM user or role explicitly overrides these settings for themselves. If this field is omitted, the setting are changed only for the authenticated user.

    :rtype: dict
    :return: {
        'setting': {
            'name': 'serviceLongArnFormat'|'taskLongArnFormat'|'containerInstanceLongArnFormat',
            'value': 'string',
            'principalArn': 'string'
        }
    }
    
    
    """
    pass

def delete_attributes(cluster=None, attributes=None):
    """
    Deletes one or more custom attributes from an Amazon ECS resource.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_attributes(
        cluster='string',
        attributes=[
            {
                'name': 'string',
                'value': 'string',
                'targetType': 'container-instance',
                'targetId': 'string'
            },
        ]
    )
    
    
    :type cluster: string
    :param cluster: The short name or full Amazon Resource Name (ARN) of the cluster that contains the resource to delete attributes. If you do not specify a cluster, the default cluster is assumed.

    :type attributes: list
    :param attributes: [REQUIRED]
            The attributes to delete from your resource. You can specify up to 10 attributes per request. For custom attributes, specify the attribute name and target ID, but do not specify the value. If you specify the target ID using the short form, you must also specify the target type.
            (dict) --An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see Attributes in the Amazon Elastic Container Service Developer Guide .
            name (string) -- [REQUIRED]The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.
            value (string) --The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.
            targetType (string) --The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.
            targetId (string) --The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).
            
            

    :rtype: dict
    :return: {
        'attributes': [
            {
                'name': 'string',
                'value': 'string',
                'targetType': 'container-instance',
                'targetId': 'string'
            },
        ]
    }
    
    
    """
    pass

def delete_cluster(cluster=None):
    """
    Deletes the specified cluster. You must deregister all container instances from this cluster before you may delete it. You can list the container instances in a cluster with  ListContainerInstances and deregister them with  DeregisterContainerInstance .
    See also: AWS API Documentation
    
    Examples
    This example deletes an empty cluster in your default region.
    Expected Output:
    
    :example: response = client.delete_cluster(
        cluster='string'
    )
    
    
    :type cluster: string
    :param cluster: [REQUIRED]
            The short name or full Amazon Resource Name (ARN) of the cluster to delete.
            

    :rtype: dict
    :return: {
        'cluster': {
            'clusterArn': 'string',
            'clusterName': 'string',
            'status': 'string',
            'registeredContainerInstancesCount': 123,
            'runningTasksCount': 123,
            'pendingTasksCount': 123,
            'activeServicesCount': 123,
            'statistics': [
                {
                    'name': 'string',
                    'value': 'string'
                },
            ],
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def delete_service(cluster=None, service=None, force=None):
    """
    Deletes a specified service within a cluster. You can delete a service if you have no running tasks in it and the desired task count is zero. If the service is actively maintaining tasks, you cannot delete it, and you must update the service to a desired task count of zero. For more information, see  UpdateService .
    See also: AWS API Documentation
    
    Examples
    This example deletes the my-http-service service. The service must have a desired count and running count of 0 before you can delete it.
    Expected Output:
    
    :example: response = client.delete_service(
        cluster='string',
        service='string',
        force=True|False
    )
    
    
    :type cluster: string
    :param cluster: The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to delete. If you do not specify a cluster, the default cluster is assumed.

    :type service: string
    :param service: [REQUIRED]
            The name of the service to delete.
            

    :type force: boolean
    :param force: If true , allows you to delete a service even if it has not been scaled down to zero tasks. It is only necessary to use this if the service is using the REPLICA scheduling strategy.

    :rtype: dict
    :return: {
        'service': {
            'serviceArn': 'string',
            'serviceName': 'string',
            'clusterArn': 'string',
            'loadBalancers': [
                {
                    'targetGroupArn': 'string',
                    'loadBalancerName': 'string',
                    'containerName': 'string',
                    'containerPort': 123
                },
            ],
            'serviceRegistries': [
                {
                    'registryArn': 'string',
                    'port': 123,
                    'containerName': 'string',
                    'containerPort': 123
                },
            ],
            'status': 'string',
            'desiredCount': 123,
            'runningCount': 123,
            'pendingCount': 123,
            'launchType': 'EC2'|'FARGATE',
            'platformVersion': 'string',
            'taskDefinition': 'string',
            'deploymentConfiguration': {
                'maximumPercent': 123,
                'minimumHealthyPercent': 123
            },
            'taskSets': [
                {
                    'id': 'string',
                    'taskSetArn': 'string',
                    'startedBy': 'string',
                    'externalId': 'string',
                    'status': 'string',
                    'taskDefinition': 'string',
                    'computedDesiredCount': 123,
                    'pendingCount': 123,
                    'runningCount': 123,
                    'createdAt': datetime(2015, 1, 1),
                    'updatedAt': datetime(2015, 1, 1),
                    'launchType': 'EC2'|'FARGATE',
                    'platformVersion': 'string',
                    'networkConfiguration': {
                        'awsvpcConfiguration': {
                            'subnets': [
                                'string',
                            ],
                            'securityGroups': [
                                'string',
                            ],
                            'assignPublicIp': 'ENABLED'|'DISABLED'
                        }
                    },
                    'loadBalancers': [
                        {
                            'targetGroupArn': 'string',
                            'loadBalancerName': 'string',
                            'containerName': 'string',
                            'containerPort': 123
                        },
                    ],
                    'scale': {
                        'value': 123.0,
                        'unit': 'PERCENT'
                    },
                    'stabilityStatus': 'STEADY_STATE'|'STABILIZING',
                    'stabilityStatusAt': datetime(2015, 1, 1)
                },
            ],
            'deployments': [
                {
                    'id': 'string',
                    'status': 'string',
                    'taskDefinition': 'string',
                    'desiredCount': 123,
                    'pendingCount': 123,
                    'runningCount': 123,
                    'createdAt': datetime(2015, 1, 1),
                    'updatedAt': datetime(2015, 1, 1),
                    'launchType': 'EC2'|'FARGATE',
                    'platformVersion': 'string',
                    'networkConfiguration': {
                        'awsvpcConfiguration': {
                            'subnets': [
                                'string',
                            ],
                            'securityGroups': [
                                'string',
                            ],
                            'assignPublicIp': 'ENABLED'|'DISABLED'
                        }
                    }
                },
            ],
            'roleArn': 'string',
            'events': [
                {
                    'id': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'message': 'string'
                },
            ],
            'createdAt': datetime(2015, 1, 1),
            'placementConstraints': [
                {
                    'type': 'distinctInstance'|'memberOf',
                    'expression': 'string'
                },
            ],
            'placementStrategy': [
                {
                    'type': 'random'|'spread'|'binpack',
                    'field': 'string'
                },
            ],
            'networkConfiguration': {
                'awsvpcConfiguration': {
                    'subnets': [
                        'string',
                    ],
                    'securityGroups': [
                        'string',
                    ],
                    'assignPublicIp': 'ENABLED'|'DISABLED'
                }
            },
            'healthCheckGracePeriodSeconds': 123,
            'schedulingStrategy': 'REPLICA'|'DAEMON',
            'deploymentController': {
                'type': 'ECS'|'CODE_DEPLOY'
            },
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'createdBy': 'string',
            'enableECSManagedTags': True|False,
            'propagateTags': 'TASK_DEFINITION'|'SERVICE'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def deregister_container_instance(cluster=None, containerInstance=None, force=None):
    """
    Deregisters an Amazon ECS container instance from the specified cluster. This instance is no longer available to run tasks.
    If you intend to use the container instance for some other purpose after deregistration, you should stop all of the tasks running on the container instance before deregistration. That prevents any orphaned tasks from consuming resources.
    Deregistering a container instance removes the instance from a cluster, but it does not terminate the EC2 instance. If you are finished using the instance, be sure to terminate it in the Amazon EC2 console to stop billing.
    See also: AWS API Documentation
    
    Examples
    This example deregisters a container instance from the specified cluster in your default region. If there are still tasks running on the container instance, you must either stop those tasks before deregistering, or use the force option.
    Expected Output:
    
    :example: response = client.deregister_container_instance(
        cluster='string',
        containerInstance='string',
        force=True|False
    )
    
    
    :type cluster: string
    :param cluster: The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instance to deregister. If you do not specify a cluster, the default cluster is assumed.

    :type containerInstance: string
    :param containerInstance: [REQUIRED]
            The container instance ID or full ARN of the container instance to deregister. The ARN contains the arn:aws:ecs namespace, followed by the Region of the container instance, the AWS account ID of the container instance owner, the container-instance namespace, and then the container instance ID. For example, ``arn:aws:ecs:region :aws_account_id :container-instance/container_instance_ID `` .
            

    :type force: boolean
    :param force: Forces the deregistration of the container instance. If you have tasks running on the container instance when you deregister it with the force option, these tasks remain running until you terminate the instance or the tasks stop through some other means, but they are orphaned (no longer monitored or accounted for by Amazon ECS). If an orphaned task on your container instance is part of an Amazon ECS service, then the service scheduler starts another copy of that task, on a different container instance if possible.
            Any containers in orphaned service tasks that are registered with a Classic Load Balancer or an Application Load Balancer target group are deregistered. They begin connection draining according to the settings on the load balancer or target group.
            

    :rtype: dict
    :return: {
        'containerInstance': {
            'containerInstanceArn': 'string',
            'ec2InstanceId': 'string',
            'version': 123,
            'versionInfo': {
                'agentVersion': 'string',
                'agentHash': 'string',
                'dockerVersion': 'string'
            },
            'remainingResources': [
                {
                    'name': 'string',
                    'type': 'string',
                    'doubleValue': 123.0,
                    'longValue': 123,
                    'integerValue': 123,
                    'stringSetValue': [
                        'string',
                    ]
                },
            ],
            'registeredResources': [
                {
                    'name': 'string',
                    'type': 'string',
                    'doubleValue': 123.0,
                    'longValue': 123,
                    'integerValue': 123,
                    'stringSetValue': [
                        'string',
                    ]
                },
            ],
            'status': 'string',
            'agentConnected': True|False,
            'runningTasksCount': 123,
            'pendingTasksCount': 123,
            'agentUpdateStatus': 'PENDING'|'STAGING'|'STAGED'|'UPDATING'|'UPDATED'|'FAILED',
            'attributes': [
                {
                    'name': 'string',
                    'value': 'string',
                    'targetType': 'container-instance',
                    'targetId': 'string'
                },
            ],
            'registeredAt': datetime(2015, 1, 1),
            'attachments': [
                {
                    'id': 'string',
                    'type': 'string',
                    'status': 'string',
                    'details': [
                        {
                            'name': 'string',
                            'value': 'string'
                        },
                    ]
                },
            ],
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def deregister_task_definition(taskDefinition=None):
    """
    Deregisters the specified task definition by family and revision. Upon deregistration, the task definition is marked as INACTIVE . Existing tasks and services that reference an INACTIVE task definition continue to run without disruption. Existing services that reference an INACTIVE task definition can still scale up or down by modifying the service's desired count.
    You cannot use an INACTIVE task definition to run new tasks or create new services, and you cannot update an existing service to reference an INACTIVE task definition. However, there may be up to a 10-minute window following deregistration where these restrictions have not yet taken effect.
    See also: AWS API Documentation
    
    
    :example: response = client.deregister_task_definition(
        taskDefinition='string'
    )
    
    
    :type taskDefinition: string
    :param taskDefinition: [REQUIRED]
            The family and revision (family:revision ) or full Amazon Resource Name (ARN) of the task definition to deregister. You must specify a revision .
            

    :rtype: dict
    :return: {
        'taskDefinition': {
            'taskDefinitionArn': 'string',
            'containerDefinitions': [
                {
                    'name': 'string',
                    'image': 'string',
                    'repositoryCredentials': {
                        'credentialsParameter': 'string'
                    },
                    'cpu': 123,
                    'memory': 123,
                    'memoryReservation': 123,
                    'links': [
                        'string',
                    ],
                    'portMappings': [
                        {
                            'containerPort': 123,
                            'hostPort': 123,
                            'protocol': 'tcp'|'udp'
                        },
                    ],
                    'essential': True|False,
                    'entryPoint': [
                        'string',
                    ],
                    'command': [
                        'string',
                    ],
                    'environment': [
                        {
                            'name': 'string',
                            'value': 'string'
                        },
                    ],
                    'mountPoints': [
                        {
                            'sourceVolume': 'string',
                            'containerPath': 'string',
                            'readOnly': True|False
                        },
                    ],
                    'volumesFrom': [
                        {
                            'sourceContainer': 'string',
                            'readOnly': True|False
                        },
                    ],
                    'linuxParameters': {
                        'capabilities': {
                            'add': [
                                'string',
                            ],
                            'drop': [
                                'string',
                            ]
                        },
                        'devices': [
                            {
                                'hostPath': 'string',
                                'containerPath': 'string',
                                'permissions': [
                                    'read'|'write'|'mknod',
                                ]
                            },
                        ],
                        'initProcessEnabled': True|False,
                        'sharedMemorySize': 123,
                        'tmpfs': [
                            {
                                'containerPath': 'string',
                                'size': 123,
                                'mountOptions': [
                                    'string',
                                ]
                            },
                        ]
                    },
                    'secrets': [
                        {
                            'name': 'string',
                            'valueFrom': 'string'
                        },
                    ],
                    'hostname': 'string',
                    'user': 'string',
                    'workingDirectory': 'string',
                    'disableNetworking': True|False,
                    'privileged': True|False,
                    'readonlyRootFilesystem': True|False,
                    'dnsServers': [
                        'string',
                    ],
                    'dnsSearchDomains': [
                        'string',
                    ],
                    'extraHosts': [
                        {
                            'hostname': 'string',
                            'ipAddress': 'string'
                        },
                    ],
                    'dockerSecurityOptions': [
                        'string',
                    ],
                    'interactive': True|False,
                    'pseudoTerminal': True|False,
                    'dockerLabels': {
                        'string': 'string'
                    },
                    'ulimits': [
                        {
                            'name': 'core'|'cpu'|'data'|'fsize'|'locks'|'memlock'|'msgqueue'|'nice'|'nofile'|'nproc'|'rss'|'rtprio'|'rttime'|'sigpending'|'stack',
                            'softLimit': 123,
                            'hardLimit': 123
                        },
                    ],
                    'logConfiguration': {
                        'logDriver': 'json-file'|'syslog'|'journald'|'gelf'|'fluentd'|'awslogs'|'splunk',
                        'options': {
                            'string': 'string'
                        }
                    },
                    'healthCheck': {
                        'command': [
                            'string',
                        ],
                        'interval': 123,
                        'timeout': 123,
                        'retries': 123,
                        'startPeriod': 123
                    },
                    'systemControls': [
                        {
                            'namespace': 'string',
                            'value': 'string'
                        },
                    ]
                },
            ],
            'family': 'string',
            'taskRoleArn': 'string',
            'executionRoleArn': 'string',
            'networkMode': 'bridge'|'host'|'awsvpc'|'none',
            'revision': 123,
            'volumes': [
                {
                    'name': 'string',
                    'host': {
                        'sourcePath': 'string'
                    },
                    'dockerVolumeConfiguration': {
                        'scope': 'task'|'shared',
                        'autoprovision': True|False,
                        'driver': 'string',
                        'driverOpts': {
                            'string': 'string'
                        },
                        'labels': {
                            'string': 'string'
                        }
                    }
                },
            ],
            'status': 'ACTIVE'|'INACTIVE',
            'requiresAttributes': [
                {
                    'name': 'string',
                    'value': 'string',
                    'targetType': 'container-instance',
                    'targetId': 'string'
                },
            ],
            'placementConstraints': [
                {
                    'type': 'memberOf',
                    'expression': 'string'
                },
            ],
            'compatibilities': [
                'EC2'|'FARGATE',
            ],
            'requiresCompatibilities': [
                'EC2'|'FARGATE',
            ],
            'cpu': 'string',
            'memory': 'string',
            'pidMode': 'host'|'task',
            'ipcMode': 'host'|'task'|'none'
        }
    }
    
    
    :returns: 
    Agent versions less than or equal to 1.1.0: Null and zero CPU values are passed to Docker as 0, which Docker then converts to 1,024 CPU shares. CPU values of 1 are passed to Docker as 1, which the Linux kernel converts to two CPU shares.
    Agent versions greater than or equal to 1.2.0: Null, zero, and CPU values of 1 are passed to Docker as 2.
    
    """
    pass

def describe_clusters(clusters=None, include=None):
    """
    Describes one or more of your clusters.
    See also: AWS API Documentation
    
    Examples
    This example provides a description of the specified cluster in your default region.
    Expected Output:
    
    :example: response = client.describe_clusters(
        clusters=[
            'string',
        ],
        include=[
            'STATISTICS'|'TAGS',
        ]
    )
    
    
    :type clusters: list
    :param clusters: A list of up to 100 cluster names or full cluster Amazon Resource Name (ARN) entries. If you do not specify a cluster, the default cluster is assumed.
            (string) --
            

    :type include: list
    :param include: Additional information about your clusters to be separated by launch type, including:
            runningEC2TasksCount
            runningFargateTasksCount
            pendingEC2TasksCount
            pendingFargateTasksCount
            activeEC2ServiceCount
            activeFargateServiceCount
            drainingEC2ServiceCount
            drainingFargateServiceCount
            (string) --
            

    :rtype: dict
    :return: {
        'clusters': [
            {
                'clusterArn': 'string',
                'clusterName': 'string',
                'status': 'string',
                'registeredContainerInstancesCount': 123,
                'runningTasksCount': 123,
                'pendingTasksCount': 123,
                'activeServicesCount': 123,
                'statistics': [
                    {
                        'name': 'string',
                        'value': 'string'
                    },
                ],
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ]
            },
        ],
        'failures': [
            {
                'arn': 'string',
                'reason': 'string'
            },
        ]
    }
    
    
    :returns: 
    runningEC2TasksCount
    RunningFargateTasksCount
    pendingEC2TasksCount
    pendingFargateTasksCount
    activeEC2ServiceCount
    activeFargateServiceCount
    drainingEC2ServiceCount
    drainingFargateServiceCount
    
    """
    pass

def describe_container_instances(cluster=None, containerInstances=None, include=None):
    """
    Describes Amazon Elastic Container Service container instances. Returns metadata about registered and remaining resources on each container instance requested.
    See also: AWS API Documentation
    
    Examples
    This example provides a description of the specified container instance in your default region, using the container instance UUID as an identifier.
    Expected Output:
    
    :example: response = client.describe_container_instances(
        cluster='string',
        containerInstances=[
            'string',
        ],
        include=[
            'TAGS',
        ]
    )
    
    
    :type cluster: string
    :param cluster: The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instances to describe. If you do not specify a cluster, the default cluster is assumed.

    :type containerInstances: list
    :param containerInstances: [REQUIRED]
            A list of up to 100 container instance IDs or full Amazon Resource Name (ARN) entries.
            (string) --
            

    :type include: list
    :param include: Specifies whether you want to see the resource tags for the container instance. If TAGS is specified, the tags are included in the response. If this field is omitted, tags are not included in the response.
            (string) --
            

    :rtype: dict
    :return: {
        'containerInstances': [
            {
                'containerInstanceArn': 'string',
                'ec2InstanceId': 'string',
                'version': 123,
                'versionInfo': {
                    'agentVersion': 'string',
                    'agentHash': 'string',
                    'dockerVersion': 'string'
                },
                'remainingResources': [
                    {
                        'name': 'string',
                        'type': 'string',
                        'doubleValue': 123.0,
                        'longValue': 123,
                        'integerValue': 123,
                        'stringSetValue': [
                            'string',
                        ]
                    },
                ],
                'registeredResources': [
                    {
                        'name': 'string',
                        'type': 'string',
                        'doubleValue': 123.0,
                        'longValue': 123,
                        'integerValue': 123,
                        'stringSetValue': [
                            'string',
                        ]
                    },
                ],
                'status': 'string',
                'agentConnected': True|False,
                'runningTasksCount': 123,
                'pendingTasksCount': 123,
                'agentUpdateStatus': 'PENDING'|'STAGING'|'STAGED'|'UPDATING'|'UPDATED'|'FAILED',
                'attributes': [
                    {
                        'name': 'string',
                        'value': 'string',
                        'targetType': 'container-instance',
                        'targetId': 'string'
                    },
                ],
                'registeredAt': datetime(2015, 1, 1),
                'attachments': [
                    {
                        'id': 'string',
                        'type': 'string',
                        'status': 'string',
                        'details': [
                            {
                                'name': 'string',
                                'value': 'string'
                            },
                        ]
                    },
                ],
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ]
            },
        ],
        'failures': [
            {
                'arn': 'string',
                'reason': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_services(cluster=None, services=None, include=None):
    """
    Describes the specified services running in your cluster.
    See also: AWS API Documentation
    
    Examples
    This example provides descriptive information about the service named ecs-simple-service.
    Expected Output:
    
    :example: response = client.describe_services(
        cluster='string',
        services=[
            'string',
        ],
        include=[
            'TAGS',
        ]
    )
    
    
    :type cluster: string
    :param cluster: The short name or full Amazon Resource Name (ARN)the cluster that hosts the service to describe. If you do not specify a cluster, the default cluster is assumed.

    :type services: list
    :param services: [REQUIRED]
            A list of services to describe. You may specify up to 10 services to describe in a single operation.
            (string) --
            

    :type include: list
    :param include: Specifies whether you want to see the resource tags for the service. If TAGS is specified, the tags are included in the response. If this field is omitted, tags are not included in the response.
            (string) --
            

    :rtype: dict
    :return: {
        'services': [
            {
                'serviceArn': 'string',
                'serviceName': 'string',
                'clusterArn': 'string',
                'loadBalancers': [
                    {
                        'targetGroupArn': 'string',
                        'loadBalancerName': 'string',
                        'containerName': 'string',
                        'containerPort': 123
                    },
                ],
                'serviceRegistries': [
                    {
                        'registryArn': 'string',
                        'port': 123,
                        'containerName': 'string',
                        'containerPort': 123
                    },
                ],
                'status': 'string',
                'desiredCount': 123,
                'runningCount': 123,
                'pendingCount': 123,
                'launchType': 'EC2'|'FARGATE',
                'platformVersion': 'string',
                'taskDefinition': 'string',
                'deploymentConfiguration': {
                    'maximumPercent': 123,
                    'minimumHealthyPercent': 123
                },
                'taskSets': [
                    {
                        'id': 'string',
                        'taskSetArn': 'string',
                        'startedBy': 'string',
                        'externalId': 'string',
                        'status': 'string',
                        'taskDefinition': 'string',
                        'computedDesiredCount': 123,
                        'pendingCount': 123,
                        'runningCount': 123,
                        'createdAt': datetime(2015, 1, 1),
                        'updatedAt': datetime(2015, 1, 1),
                        'launchType': 'EC2'|'FARGATE',
                        'platformVersion': 'string',
                        'networkConfiguration': {
                            'awsvpcConfiguration': {
                                'subnets': [
                                    'string',
                                ],
                                'securityGroups': [
                                    'string',
                                ],
                                'assignPublicIp': 'ENABLED'|'DISABLED'
                            }
                        },
                        'loadBalancers': [
                            {
                                'targetGroupArn': 'string',
                                'loadBalancerName': 'string',
                                'containerName': 'string',
                                'containerPort': 123
                            },
                        ],
                        'scale': {
                            'value': 123.0,
                            'unit': 'PERCENT'
                        },
                        'stabilityStatus': 'STEADY_STATE'|'STABILIZING',
                        'stabilityStatusAt': datetime(2015, 1, 1)
                    },
                ],
                'deployments': [
                    {
                        'id': 'string',
                        'status': 'string',
                        'taskDefinition': 'string',
                        'desiredCount': 123,
                        'pendingCount': 123,
                        'runningCount': 123,
                        'createdAt': datetime(2015, 1, 1),
                        'updatedAt': datetime(2015, 1, 1),
                        'launchType': 'EC2'|'FARGATE',
                        'platformVersion': 'string',
                        'networkConfiguration': {
                            'awsvpcConfiguration': {
                                'subnets': [
                                    'string',
                                ],
                                'securityGroups': [
                                    'string',
                                ],
                                'assignPublicIp': 'ENABLED'|'DISABLED'
                            }
                        }
                    },
                ],
                'roleArn': 'string',
                'events': [
                    {
                        'id': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'message': 'string'
                    },
                ],
                'createdAt': datetime(2015, 1, 1),
                'placementConstraints': [
                    {
                        'type': 'distinctInstance'|'memberOf',
                        'expression': 'string'
                    },
                ],
                'placementStrategy': [
                    {
                        'type': 'random'|'spread'|'binpack',
                        'field': 'string'
                    },
                ],
                'networkConfiguration': {
                    'awsvpcConfiguration': {
                        'subnets': [
                            'string',
                        ],
                        'securityGroups': [
                            'string',
                        ],
                        'assignPublicIp': 'ENABLED'|'DISABLED'
                    }
                },
                'healthCheckGracePeriodSeconds': 123,
                'schedulingStrategy': 'REPLICA'|'DAEMON',
                'deploymentController': {
                    'type': 'ECS'|'CODE_DEPLOY'
                },
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'createdBy': 'string',
                'enableECSManagedTags': True|False,
                'propagateTags': 'TASK_DEFINITION'|'SERVICE'
            },
        ],
        'failures': [
            {
                'arn': 'string',
                'reason': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_task_definition(taskDefinition=None, include=None):
    """
    Describes a task definition. You can specify a family and revision to find information about a specific task definition, or you can simply specify the family to find the latest ACTIVE revision in that family.
    See also: AWS API Documentation
    
    Examples
    This example provides a description of the specified task definition.
    Expected Output:
    
    :example: response = client.describe_task_definition(
        taskDefinition='string',
        include=[
            'TAGS',
        ]
    )
    
    
    :type taskDefinition: string
    :param taskDefinition: [REQUIRED]
            The family for the latest ACTIVE revision, family and revision (family:revision ) for a specific revision in the family, or full Amazon Resource Name (ARN) of the task definition to describe.
            

    :type include: list
    :param include: Specifies whether to see the resource tags for the task definition. If TAGS is specified, the tags are included in the response. If this field is omitted, tags are not included in the response.
            (string) --
            

    :rtype: dict
    :return: {
        'taskDefinition': {
            'taskDefinitionArn': 'string',
            'containerDefinitions': [
                {
                    'name': 'string',
                    'image': 'string',
                    'repositoryCredentials': {
                        'credentialsParameter': 'string'
                    },
                    'cpu': 123,
                    'memory': 123,
                    'memoryReservation': 123,
                    'links': [
                        'string',
                    ],
                    'portMappings': [
                        {
                            'containerPort': 123,
                            'hostPort': 123,
                            'protocol': 'tcp'|'udp'
                        },
                    ],
                    'essential': True|False,
                    'entryPoint': [
                        'string',
                    ],
                    'command': [
                        'string',
                    ],
                    'environment': [
                        {
                            'name': 'string',
                            'value': 'string'
                        },
                    ],
                    'mountPoints': [
                        {
                            'sourceVolume': 'string',
                            'containerPath': 'string',
                            'readOnly': True|False
                        },
                    ],
                    'volumesFrom': [
                        {
                            'sourceContainer': 'string',
                            'readOnly': True|False
                        },
                    ],
                    'linuxParameters': {
                        'capabilities': {
                            'add': [
                                'string',
                            ],
                            'drop': [
                                'string',
                            ]
                        },
                        'devices': [
                            {
                                'hostPath': 'string',
                                'containerPath': 'string',
                                'permissions': [
                                    'read'|'write'|'mknod',
                                ]
                            },
                        ],
                        'initProcessEnabled': True|False,
                        'sharedMemorySize': 123,
                        'tmpfs': [
                            {
                                'containerPath': 'string',
                                'size': 123,
                                'mountOptions': [
                                    'string',
                                ]
                            },
                        ]
                    },
                    'secrets': [
                        {
                            'name': 'string',
                            'valueFrom': 'string'
                        },
                    ],
                    'hostname': 'string',
                    'user': 'string',
                    'workingDirectory': 'string',
                    'disableNetworking': True|False,
                    'privileged': True|False,
                    'readonlyRootFilesystem': True|False,
                    'dnsServers': [
                        'string',
                    ],
                    'dnsSearchDomains': [
                        'string',
                    ],
                    'extraHosts': [
                        {
                            'hostname': 'string',
                            'ipAddress': 'string'
                        },
                    ],
                    'dockerSecurityOptions': [
                        'string',
                    ],
                    'interactive': True|False,
                    'pseudoTerminal': True|False,
                    'dockerLabels': {
                        'string': 'string'
                    },
                    'ulimits': [
                        {
                            'name': 'core'|'cpu'|'data'|'fsize'|'locks'|'memlock'|'msgqueue'|'nice'|'nofile'|'nproc'|'rss'|'rtprio'|'rttime'|'sigpending'|'stack',
                            'softLimit': 123,
                            'hardLimit': 123
                        },
                    ],
                    'logConfiguration': {
                        'logDriver': 'json-file'|'syslog'|'journald'|'gelf'|'fluentd'|'awslogs'|'splunk',
                        'options': {
                            'string': 'string'
                        }
                    },
                    'healthCheck': {
                        'command': [
                            'string',
                        ],
                        'interval': 123,
                        'timeout': 123,
                        'retries': 123,
                        'startPeriod': 123
                    },
                    'systemControls': [
                        {
                            'namespace': 'string',
                            'value': 'string'
                        },
                    ]
                },
            ],
            'family': 'string',
            'taskRoleArn': 'string',
            'executionRoleArn': 'string',
            'networkMode': 'bridge'|'host'|'awsvpc'|'none',
            'revision': 123,
            'volumes': [
                {
                    'name': 'string',
                    'host': {
                        'sourcePath': 'string'
                    },
                    'dockerVolumeConfiguration': {
                        'scope': 'task'|'shared',
                        'autoprovision': True|False,
                        'driver': 'string',
                        'driverOpts': {
                            'string': 'string'
                        },
                        'labels': {
                            'string': 'string'
                        }
                    }
                },
            ],
            'status': 'ACTIVE'|'INACTIVE',
            'requiresAttributes': [
                {
                    'name': 'string',
                    'value': 'string',
                    'targetType': 'container-instance',
                    'targetId': 'string'
                },
            ],
            'placementConstraints': [
                {
                    'type': 'memberOf',
                    'expression': 'string'
                },
            ],
            'compatibilities': [
                'EC2'|'FARGATE',
            ],
            'requiresCompatibilities': [
                'EC2'|'FARGATE',
            ],
            'cpu': 'string',
            'memory': 'string',
            'pidMode': 'host'|'task',
            'ipcMode': 'host'|'task'|'none'
        },
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    }
    
    
    :returns: 
    When a new task starts, the Amazon ECS container agent pulls the latest version of the specified image and tag for the container to use. However, subsequent updates to a repository image are not propagated to already running tasks.
    Images in Amazon ECR repositories can be specified by either using the full registry/repository:tag or registry/repository@digest . For example, 012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>:latest or 012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>@sha256:94afd1f2e64d908bc90dbca0035a5b567EXAMPLE .
    Images in official repositories on Docker Hub use a single name (for example, ubuntu or mongo ).
    Images in other repositories on Docker Hub are qualified with an organization name (for example, amazon/amazon-ecs-agent ).
    Images in other online repositories are qualified further by a domain name (for example, quay.io/assemblyline/ubuntu ).
    
    """
    pass

def describe_tasks(cluster=None, tasks=None, include=None):
    """
    Describes a specified task or tasks.
    See also: AWS API Documentation
    
    Examples
    This example provides a description of the specified task, using the task UUID as an identifier.
    Expected Output:
    
    :example: response = client.describe_tasks(
        cluster='string',
        tasks=[
            'string',
        ],
        include=[
            'TAGS',
        ]
    )
    
    
    :type cluster: string
    :param cluster: The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task to describe. If you do not specify a cluster, the default cluster is assumed.

    :type tasks: list
    :param tasks: [REQUIRED]
            A list of up to 100 task IDs or full ARN entries.
            (string) --
            

    :type include: list
    :param include: Specifies whether you want to see the resource tags for the task. If TAGS is specified, the tags are included in the response. If this field is omitted, tags are not included in the response.
            (string) --
            

    :rtype: dict
    :return: {
        'tasks': [
            {
                'taskArn': 'string',
                'clusterArn': 'string',
                'taskDefinitionArn': 'string',
                'containerInstanceArn': 'string',
                'overrides': {
                    'containerOverrides': [
                        {
                            'name': 'string',
                            'command': [
                                'string',
                            ],
                            'environment': [
                                {
                                    'name': 'string',
                                    'value': 'string'
                                },
                            ],
                            'cpu': 123,
                            'memory': 123,
                            'memoryReservation': 123
                        },
                    ],
                    'taskRoleArn': 'string',
                    'executionRoleArn': 'string'
                },
                'lastStatus': 'string',
                'desiredStatus': 'string',
                'cpu': 'string',
                'memory': 'string',
                'containers': [
                    {
                        'containerArn': 'string',
                        'taskArn': 'string',
                        'name': 'string',
                        'lastStatus': 'string',
                        'exitCode': 123,
                        'reason': 'string',
                        'networkBindings': [
                            {
                                'bindIP': 'string',
                                'containerPort': 123,
                                'hostPort': 123,
                                'protocol': 'tcp'|'udp'
                            },
                        ],
                        'networkInterfaces': [
                            {
                                'attachmentId': 'string',
                                'privateIpv4Address': 'string',
                                'ipv6Address': 'string'
                            },
                        ],
                        'healthStatus': 'HEALTHY'|'UNHEALTHY'|'UNKNOWN'
                    },
                ],
                'startedBy': 'string',
                'version': 123,
                'stoppedReason': 'string',
                'stopCode': 'TaskFailedToStart'|'EssentialContainerExited'|'UserInitiated',
                'connectivity': 'CONNECTED'|'DISCONNECTED',
                'connectivityAt': datetime(2015, 1, 1),
                'pullStartedAt': datetime(2015, 1, 1),
                'pullStoppedAt': datetime(2015, 1, 1),
                'executionStoppedAt': datetime(2015, 1, 1),
                'createdAt': datetime(2015, 1, 1),
                'startedAt': datetime(2015, 1, 1),
                'stoppingAt': datetime(2015, 1, 1),
                'stoppedAt': datetime(2015, 1, 1),
                'group': 'string',
                'launchType': 'EC2'|'FARGATE',
                'platformVersion': 'string',
                'attachments': [
                    {
                        'id': 'string',
                        'type': 'string',
                        'status': 'string',
                        'details': [
                            {
                                'name': 'string',
                                'value': 'string'
                            },
                        ]
                    },
                ],
                'healthStatus': 'HEALTHY'|'UNHEALTHY'|'UNKNOWN',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ]
            },
        ],
        'failures': [
            {
                'arn': 'string',
                'reason': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def discover_poll_endpoint(containerInstance=None, cluster=None):
    """
    Returns an endpoint for the Amazon ECS agent to poll for updates.
    See also: AWS API Documentation
    
    
    :example: response = client.discover_poll_endpoint(
        containerInstance='string',
        cluster='string'
    )
    
    
    :type containerInstance: string
    :param containerInstance: The container instance ID or full ARN of the container instance. The ARN contains the arn:aws:ecs namespace, followed by the Region of the container instance, the AWS account ID of the container instance owner, the container-instance namespace, and then the container instance ID. For example, ``arn:aws:ecs:region :aws_account_id :container-instance/container_instance_ID `` .

    :type cluster: string
    :param cluster: The short name or full Amazon Resource Name (ARN) of the cluster to which the container instance belongs.

    :rtype: dict
    :return: {
        'endpoint': 'string',
        'telemetryEndpoint': 'string'
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

def list_account_settings(name=None, value=None, principalArn=None, effectiveSettings=None, nextToken=None, maxResults=None):
    """
    Lists the account settings for an Amazon ECS resource for a specified principal.
    See also: AWS API Documentation
    
    
    :example: response = client.list_account_settings(
        name='serviceLongArnFormat'|'taskLongArnFormat'|'containerInstanceLongArnFormat',
        value='string',
        principalArn='string',
        effectiveSettings=True|False,
        nextToken='string',
        maxResults=123
    )
    
    
    :type name: string
    :param name: The resource name you want to list the account settings for.

    :type value: string
    :param value: The value of the account settings with which to filter results. You must also specify an account setting name to use this parameter.

    :type principalArn: string
    :param principalArn: The ARN of the principal, which can be an IAM user, IAM role, or the root user. If this field is omitted, the account settings are listed only for the authenticated user.

    :type effectiveSettings: boolean
    :param effectiveSettings: Specifies whether to return the effective settings. If true , the account settings for the root user or the default setting for the principalArn . If false , the account settings for the principalArn are returned if they are set. Otherwise, no account settings are returned.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListAccountSettings request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            

    :type maxResults: integer
    :param maxResults: The maximum number of account setting results returned by ListAccountSettings in paginated output. When this parameter is used, ListAccountSettings only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListAccountSettings request with the returned nextToken value. This value can be between 1 and 10. If this parameter is not used, then ListAccountSettings returns up to 10 results and a nextToken value if applicable.

    :rtype: dict
    :return: {
        'settings': [
            {
                'name': 'serviceLongArnFormat'|'taskLongArnFormat'|'containerInstanceLongArnFormat',
                'value': 'string',
                'principalArn': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_attributes(cluster=None, targetType=None, attributeName=None, attributeValue=None, nextToken=None, maxResults=None):
    """
    Lists the attributes for Amazon ECS resources within a specified target type and cluster. When you specify a target type and cluster, ListAttributes returns a list of attribute objects, one for each attribute on each resource. You can filter the list of results to a single attribute name to only return results that have that name. You can also filter the results by attribute name and value, for example, to see which container instances in a cluster are running a Linux AMI (ecs.os-type=linux ).
    See also: AWS API Documentation
    
    
    :example: response = client.list_attributes(
        cluster='string',
        targetType='container-instance',
        attributeName='string',
        attributeValue='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type cluster: string
    :param cluster: The short name or full Amazon Resource Name (ARN) of the cluster to list attributes. If you do not specify a cluster, the default cluster is assumed.

    :type targetType: string
    :param targetType: [REQUIRED]
            The type of the target with which to list attributes.
            

    :type attributeName: string
    :param attributeName: The name of the attribute with which to filter the results.

    :type attributeValue: string
    :param attributeValue: The value of the attribute with which to filter results. You must also specify an attribute name to use this parameter.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListAttributes request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            

    :type maxResults: integer
    :param maxResults: The maximum number of cluster results returned by ListAttributes in paginated output. When this parameter is used, ListAttributes only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListAttributes request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListAttributes returns up to 100 results and a nextToken value if applicable.

    :rtype: dict
    :return: {
        'attributes': [
            {
                'name': 'string',
                'value': 'string',
                'targetType': 'container-instance',
                'targetId': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_clusters(nextToken=None, maxResults=None):
    """
    Returns a list of existing clusters.
    See also: AWS API Documentation
    
    Examples
    This example lists all of your available clusters in your default region.
    Expected Output:
    
    :example: response = client.list_clusters(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListClusters request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            

    :type maxResults: integer
    :param maxResults: The maximum number of cluster results returned by ListClusters in paginated output. When this parameter is used, ListClusters only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListClusters request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListClusters returns up to 100 results and a nextToken value if applicable.

    :rtype: dict
    :return: {
        'clusterArns': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_container_instances(cluster=None, filter=None, nextToken=None, maxResults=None, status=None):
    """
    Returns a list of container instances in a specified cluster. You can filter the results of a ListContainerInstances operation with cluster query language statements inside the filter parameter. For more information, see Cluster Query Language in the Amazon Elastic Container Service Developer Guide .
    See also: AWS API Documentation
    
    Examples
    This example lists all of your available container instances in the specified cluster in your default region.
    Expected Output:
    
    :example: response = client.list_container_instances(
        cluster='string',
        filter='string',
        nextToken='string',
        maxResults=123,
        status='ACTIVE'|'DRAINING'
    )
    
    
    :type cluster: string
    :param cluster: The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instances to list. If you do not specify a cluster, the default cluster is assumed.

    :type filter: string
    :param filter: You can filter the results of a ListContainerInstances operation with cluster query language statements. For more information, see Cluster Query Language in the Amazon Elastic Container Service Developer Guide .

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListContainerInstances request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            

    :type maxResults: integer
    :param maxResults: The maximum number of container instance results returned by ListContainerInstances in paginated output. When this parameter is used, ListContainerInstances only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListContainerInstances request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListContainerInstances returns up to 100 results and a nextToken value if applicable.

    :type status: string
    :param status: Filters the container instances by status. For example, if you specify the DRAINING status, the results include only container instances that have been set to DRAINING using UpdateContainerInstancesState . If you do not specify this parameter, the default is to include container instances set to ACTIVE and DRAINING .

    :rtype: dict
    :return: {
        'containerInstanceArns': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_services(cluster=None, nextToken=None, maxResults=None, launchType=None, schedulingStrategy=None):
    """
    Lists the services that are running in a specified cluster.
    See also: AWS API Documentation
    
    Examples
    This example lists the services running in the default cluster for an account.
    Expected Output:
    
    :example: response = client.list_services(
        cluster='string',
        nextToken='string',
        maxResults=123,
        launchType='EC2'|'FARGATE',
        schedulingStrategy='REPLICA'|'DAEMON'
    )
    
    
    :type cluster: string
    :param cluster: The short name or full Amazon Resource Name (ARN) of the cluster that hosts the services to list. If you do not specify a cluster, the default cluster is assumed.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListServices request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            

    :type maxResults: integer
    :param maxResults: The maximum number of service results returned by ListServices in paginated output. When this parameter is used, ListServices only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListServices request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListServices returns up to 10 results and a nextToken value if applicable.

    :type launchType: string
    :param launchType: The launch type for the services to list.

    :type schedulingStrategy: string
    :param schedulingStrategy: The scheduling strategy for services to list.

    :rtype: dict
    :return: {
        'serviceArns': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tags_for_resource(resourceArn=None):
    """
    List the tags for an Amazon ECS resource.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) that identifies the resource for which to list the tags. Currently, the supported resources are Amazon ECS tasks, services, task definitions, clusters, and container instances.
            

    :rtype: dict
    :return: {
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_task_definition_families(familyPrefix=None, status=None, nextToken=None, maxResults=None):
    """
    Returns a list of task definition families that are registered to your account (which may include task definition families that no longer have any ACTIVE task definition revisions).
    You can filter out task definition families that do not contain any ACTIVE task definition revisions by setting the status parameter to ACTIVE . You can also filter the results with the familyPrefix parameter.
    See also: AWS API Documentation
    
    Examples
    This example lists all of your registered task definition families.
    Expected Output:
    This example lists the task definition revisions that start with "hpcc".
    Expected Output:
    
    :example: response = client.list_task_definition_families(
        familyPrefix='string',
        status='ACTIVE'|'INACTIVE'|'ALL',
        nextToken='string',
        maxResults=123
    )
    
    
    :type familyPrefix: string
    :param familyPrefix: The familyPrefix is a string that is used to filter the results of ListTaskDefinitionFamilies . If you specify a familyPrefix , only task definition family names that begin with the familyPrefix string are returned.

    :type status: string
    :param status: The task definition family status with which to filter the ListTaskDefinitionFamilies results. By default, both ACTIVE and INACTIVE task definition families are listed. If this parameter is set to ACTIVE , only task definition families that have an ACTIVE task definition revision are returned. If this parameter is set to INACTIVE , only task definition families that do not have any ACTIVE task definition revisions are returned. If you paginate the resulting output, be sure to keep the status value constant in each subsequent request.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListTaskDefinitionFamilies request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            

    :type maxResults: integer
    :param maxResults: The maximum number of task definition family results returned by ListTaskDefinitionFamilies in paginated output. When this parameter is used, ListTaskDefinitions only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListTaskDefinitionFamilies request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListTaskDefinitionFamilies returns up to 100 results and a nextToken value if applicable.

    :rtype: dict
    :return: {
        'families': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_task_definitions(familyPrefix=None, status=None, sort=None, nextToken=None, maxResults=None):
    """
    Returns a list of task definitions that are registered to your account. You can filter the results by family name with the familyPrefix parameter or by status with the status parameter.
    See also: AWS API Documentation
    
    Examples
    This example lists all of your registered task definitions.
    Expected Output:
    This example lists the task definition revisions of a specified family.
    Expected Output:
    
    :example: response = client.list_task_definitions(
        familyPrefix='string',
        status='ACTIVE'|'INACTIVE',
        sort='ASC'|'DESC',
        nextToken='string',
        maxResults=123
    )
    
    
    :type familyPrefix: string
    :param familyPrefix: The full family name with which to filter the ListTaskDefinitions results. Specifying a familyPrefix limits the listed task definitions to task definition revisions that belong to that family.

    :type status: string
    :param status: The task definition status with which to filter the ListTaskDefinitions results. By default, only ACTIVE task definitions are listed. By setting this parameter to INACTIVE , you can view task definitions that are INACTIVE as long as an active task or service still references them. If you paginate the resulting output, be sure to keep the status value constant in each subsequent request.

    :type sort: string
    :param sort: The order in which to sort the results. Valid values are ASC and DESC . By default (ASC ), task definitions are listed lexicographically by family name and in ascending numerical order by revision so that the newest task definitions in a family are listed last. Setting this parameter to DESC reverses the sort order on family name and revision so that the newest task definitions in a family are listed first.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListTaskDefinitions request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            

    :type maxResults: integer
    :param maxResults: The maximum number of task definition results returned by ListTaskDefinitions in paginated output. When this parameter is used, ListTaskDefinitions only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListTaskDefinitions request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListTaskDefinitions returns up to 100 results and a nextToken value if applicable.

    :rtype: dict
    :return: {
        'taskDefinitionArns': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tasks(cluster=None, containerInstance=None, family=None, nextToken=None, maxResults=None, startedBy=None, serviceName=None, desiredStatus=None, launchType=None):
    """
    Returns a list of tasks for a specified cluster. You can filter the results by family name, by a particular container instance, or by the desired status of the task with the family , containerInstance , and desiredStatus parameters.
    Recently stopped tasks might appear in the returned results. Currently, stopped tasks appear in the returned results for at least one hour.
    See also: AWS API Documentation
    
    Examples
    This example lists all of the tasks in a cluster.
    Expected Output:
    This example lists the tasks of a specified container instance. Specifying a containerInstance value limits  the  results  to  tasks  that belong to that container instance.
    Expected Output:
    
    :example: response = client.list_tasks(
        cluster='string',
        containerInstance='string',
        family='string',
        nextToken='string',
        maxResults=123,
        startedBy='string',
        serviceName='string',
        desiredStatus='RUNNING'|'PENDING'|'STOPPED',
        launchType='EC2'|'FARGATE'
    )
    
    
    :type cluster: string
    :param cluster: The short name or full Amazon Resource Name (ARN) of the cluster that hosts the tasks to list. If you do not specify a cluster, the default cluster is assumed.

    :type containerInstance: string
    :param containerInstance: The container instance ID or full ARN of the container instance with which to filter the ListTasks results. Specifying a containerInstance limits the results to tasks that belong to that container instance.

    :type family: string
    :param family: The name of the family with which to filter the ListTasks results. Specifying a family limits the results to tasks that belong to that family.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListTasks request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            

    :type maxResults: integer
    :param maxResults: The maximum number of task results returned by ListTasks in paginated output. When this parameter is used, ListTasks only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListTasks request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListTasks returns up to 100 results and a nextToken value if applicable.

    :type startedBy: string
    :param startedBy: The startedBy value with which to filter the task results. Specifying a startedBy value limits the results to tasks that were started with that value.

    :type serviceName: string
    :param serviceName: The name of the service with which to filter the ListTasks results. Specifying a serviceName limits the results to tasks that belong to that service.

    :type desiredStatus: string
    :param desiredStatus: The task desired status with which to filter the ListTasks results. Specifying a desiredStatus of STOPPED limits the results to tasks that Amazon ECS has set the desired status to STOPPED . This can be useful for debugging tasks that are not starting properly or have died or finished. The default status filter is RUNNING , which shows tasks that Amazon ECS has set the desired status to RUNNING .
            Note
            Although you can filter results based on a desired status of PENDING , this does not return any results. Amazon ECS never sets the desired status of a task to that value (only a task's lastStatus may have a value of PENDING ).
            

    :type launchType: string
    :param launchType: The launch type for services to list.

    :rtype: dict
    :return: {
        'taskArns': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def put_account_setting(name=None, value=None, principalArn=None):
    """
    Modifies the ARN and resource ID format of a resource for a specified IAM user, IAM role, or the root user for an account. You can specify whether the new ARN and resource ID format are enabled for new resources that are created. Enabling this setting is required to use new Amazon ECS features such as resource tagging.
    See also: AWS API Documentation
    
    
    :example: response = client.put_account_setting(
        name='serviceLongArnFormat'|'taskLongArnFormat'|'containerInstanceLongArnFormat',
        value='string',
        principalArn='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The resource name for which to enable the new format. If serviceLongArnFormat is specified, the ARN for your Amazon ECS services is affected. If taskLongArnFormat is specified, the ARN and resource ID for your Amazon ECS tasks is affected. If containerInstanceLongArnFormat is specified, the ARN and resource ID for your Amazon ECS container instances is affected.
            

    :type value: string
    :param value: [REQUIRED]
            The account setting value for the specified principal ARN. Accepted values are enabled and disabled .
            

    :type principalArn: string
    :param principalArn: The ARN of the principal, which can be an IAM user, IAM role, or the root user. If you specify the root user, it modifies the ARN and resource ID format for all IAM users, IAM roles, and the root user of the account unless an IAM user or role explicitly overrides these settings for themselves. If this field is omitted, the setting are changed only for the authenticated user.

    :rtype: dict
    :return: {
        'setting': {
            'name': 'serviceLongArnFormat'|'taskLongArnFormat'|'containerInstanceLongArnFormat',
            'value': 'string',
            'principalArn': 'string'
        }
    }
    
    
    """
    pass

def put_attributes(cluster=None, attributes=None):
    """
    Create or update an attribute on an Amazon ECS resource. If the attribute does not exist, it is created. If the attribute exists, its value is replaced with the specified value. To delete an attribute, use  DeleteAttributes . For more information, see Attributes in the Amazon Elastic Container Service Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.put_attributes(
        cluster='string',
        attributes=[
            {
                'name': 'string',
                'value': 'string',
                'targetType': 'container-instance',
                'targetId': 'string'
            },
        ]
    )
    
    
    :type cluster: string
    :param cluster: The short name or full Amazon Resource Name (ARN) of the cluster that contains the resource to apply attributes. If you do not specify a cluster, the default cluster is assumed.

    :type attributes: list
    :param attributes: [REQUIRED]
            The attributes to apply to your resource. You can specify up to 10 custom attributes per resource. You can specify up to 10 attributes in a single call.
            (dict) --An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see Attributes in the Amazon Elastic Container Service Developer Guide .
            name (string) -- [REQUIRED]The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.
            value (string) --The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.
            targetType (string) --The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.
            targetId (string) --The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).
            
            

    :rtype: dict
    :return: {
        'attributes': [
            {
                'name': 'string',
                'value': 'string',
                'targetType': 'container-instance',
                'targetId': 'string'
            },
        ]
    }
    
    
    """
    pass

def register_container_instance(cluster=None, instanceIdentityDocument=None, instanceIdentityDocumentSignature=None, totalResources=None, versionInfo=None, containerInstanceArn=None, attributes=None, tags=None):
    """
    Registers an EC2 instance into the specified cluster. This instance becomes available to place containers on.
    See also: AWS API Documentation
    
    
    :example: response = client.register_container_instance(
        cluster='string',
        instanceIdentityDocument='string',
        instanceIdentityDocumentSignature='string',
        totalResources=[
            {
                'name': 'string',
                'type': 'string',
                'doubleValue': 123.0,
                'longValue': 123,
                'integerValue': 123,
                'stringSetValue': [
                    'string',
                ]
            },
        ],
        versionInfo={
            'agentVersion': 'string',
            'agentHash': 'string',
            'dockerVersion': 'string'
        },
        containerInstanceArn='string',
        attributes=[
            {
                'name': 'string',
                'value': 'string',
                'targetType': 'container-instance',
                'targetId': 'string'
            },
        ],
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type cluster: string
    :param cluster: The short name or full Amazon Resource Name (ARN) of the cluster with which to register your container instance. If you do not specify a cluster, the default cluster is assumed.

    :type instanceIdentityDocument: string
    :param instanceIdentityDocument: The instance identity document for the EC2 instance to register. This document can be found by running the following command from the instance: curl http://169.254.169.254/latest/dynamic/instance-identity/document/

    :type instanceIdentityDocumentSignature: string
    :param instanceIdentityDocumentSignature: The instance identity document signature for the EC2 instance to register. This signature can be found by running the following command from the instance: curl http://169.254.169.254/latest/dynamic/instance-identity/signature/

    :type totalResources: list
    :param totalResources: The resources available on the instance.
            (dict) --Describes the resources available for a container instance.
            name (string) --The name of the resource, such as CPU , MEMORY , PORTS , PORTS_UDP , or a user-defined resource.
            type (string) --The type of the resource, such as INTEGER , DOUBLE , LONG , or STRINGSET .
            doubleValue (float) --When the doubleValue type is set, the value of the resource must be a double precision floating-point type.
            longValue (integer) --When the longValue type is set, the value of the resource must be an extended precision floating-point type.
            integerValue (integer) --When the integerValue type is set, the value of the resource must be an integer.
            stringSetValue (list) --When the stringSetValue type is set, the value of the resource must be a string type.
            (string) --
            
            

    :type versionInfo: dict
    :param versionInfo: The version information for the Amazon ECS container agent and Docker daemon running on the container instance.
            agentVersion (string) --The version number of the Amazon ECS container agent.
            agentHash (string) --The Git commit hash for the Amazon ECS container agent build on the amazon-ecs-agent GitHub repository.
            dockerVersion (string) --The Docker version running on the container instance.
            

    :type containerInstanceArn: string
    :param containerInstanceArn: The ARN of the container instance (if it was previously registered).

    :type attributes: list
    :param attributes: The container instance attributes that this container instance supports.
            (dict) --An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see Attributes in the Amazon Elastic Container Service Developer Guide .
            name (string) -- [REQUIRED]The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.
            value (string) --The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.
            targetType (string) --The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.
            targetId (string) --The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).
            
            

    :type tags: list
    :param tags: The metadata that you apply to the container instance to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
            (dict) --The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
            key (string) --One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.
            value (string) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).
            
            

    :rtype: dict
    :return: {
        'containerInstance': {
            'containerInstanceArn': 'string',
            'ec2InstanceId': 'string',
            'version': 123,
            'versionInfo': {
                'agentVersion': 'string',
                'agentHash': 'string',
                'dockerVersion': 'string'
            },
            'remainingResources': [
                {
                    'name': 'string',
                    'type': 'string',
                    'doubleValue': 123.0,
                    'longValue': 123,
                    'integerValue': 123,
                    'stringSetValue': [
                        'string',
                    ]
                },
            ],
            'registeredResources': [
                {
                    'name': 'string',
                    'type': 'string',
                    'doubleValue': 123.0,
                    'longValue': 123,
                    'integerValue': 123,
                    'stringSetValue': [
                        'string',
                    ]
                },
            ],
            'status': 'string',
            'agentConnected': True|False,
            'runningTasksCount': 123,
            'pendingTasksCount': 123,
            'agentUpdateStatus': 'PENDING'|'STAGING'|'STAGED'|'UPDATING'|'UPDATED'|'FAILED',
            'attributes': [
                {
                    'name': 'string',
                    'value': 'string',
                    'targetType': 'container-instance',
                    'targetId': 'string'
                },
            ],
            'registeredAt': datetime(2015, 1, 1),
            'attachments': [
                {
                    'id': 'string',
                    'type': 'string',
                    'status': 'string',
                    'details': [
                        {
                            'name': 'string',
                            'value': 'string'
                        },
                    ]
                },
            ],
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def register_task_definition(family=None, taskRoleArn=None, executionRoleArn=None, networkMode=None, containerDefinitions=None, volumes=None, placementConstraints=None, requiresCompatibilities=None, cpu=None, memory=None, tags=None, pidMode=None, ipcMode=None):
    """
    Registers a new task definition from the supplied family and containerDefinitions . Optionally, you can add data volumes to your containers with the volumes parameter. For more information about task definition parameters and defaults, see Amazon ECS Task Definitions in the Amazon Elastic Container Service Developer Guide .
    You can specify an IAM role for your task with the taskRoleArn parameter. When you specify an IAM role for a task, its containers can then use the latest versions of the AWS CLI or SDKs to make API requests to the AWS services that are specified in the IAM policy associated with the role. For more information, see IAM Roles for Tasks in the Amazon Elastic Container Service Developer Guide .
    You can specify a Docker networking mode for the containers in your task definition with the networkMode parameter. The available network modes correspond to those described in Network settings in the Docker run reference. If you specify the awsvpc network mode, the task is allocated an elastic network interface, and you must specify a  NetworkConfiguration when you create a service or run a task with the task definition. For more information, see Task Networking in the Amazon Elastic Container Service Developer Guide .
    See also: AWS API Documentation
    
    Examples
    This example registers a task definition to the specified family.
    Expected Output:
    
    :example: response = client.register_task_definition(
        family='string',
        taskRoleArn='string',
        executionRoleArn='string',
        networkMode='bridge'|'host'|'awsvpc'|'none',
        containerDefinitions=[
            {
                'name': 'string',
                'image': 'string',
                'repositoryCredentials': {
                    'credentialsParameter': 'string'
                },
                'cpu': 123,
                'memory': 123,
                'memoryReservation': 123,
                'links': [
                    'string',
                ],
                'portMappings': [
                    {
                        'containerPort': 123,
                        'hostPort': 123,
                        'protocol': 'tcp'|'udp'
                    },
                ],
                'essential': True|False,
                'entryPoint': [
                    'string',
                ],
                'command': [
                    'string',
                ],
                'environment': [
                    {
                        'name': 'string',
                        'value': 'string'
                    },
                ],
                'mountPoints': [
                    {
                        'sourceVolume': 'string',
                        'containerPath': 'string',
                        'readOnly': True|False
                    },
                ],
                'volumesFrom': [
                    {
                        'sourceContainer': 'string',
                        'readOnly': True|False
                    },
                ],
                'linuxParameters': {
                    'capabilities': {
                        'add': [
                            'string',
                        ],
                        'drop': [
                            'string',
                        ]
                    },
                    'devices': [
                        {
                            'hostPath': 'string',
                            'containerPath': 'string',
                            'permissions': [
                                'read'|'write'|'mknod',
                            ]
                        },
                    ],
                    'initProcessEnabled': True|False,
                    'sharedMemorySize': 123,
                    'tmpfs': [
                        {
                            'containerPath': 'string',
                            'size': 123,
                            'mountOptions': [
                                'string',
                            ]
                        },
                    ]
                },
                'secrets': [
                    {
                        'name': 'string',
                        'valueFrom': 'string'
                    },
                ],
                'hostname': 'string',
                'user': 'string',
                'workingDirectory': 'string',
                'disableNetworking': True|False,
                'privileged': True|False,
                'readonlyRootFilesystem': True|False,
                'dnsServers': [
                    'string',
                ],
                'dnsSearchDomains': [
                    'string',
                ],
                'extraHosts': [
                    {
                        'hostname': 'string',
                        'ipAddress': 'string'
                    },
                ],
                'dockerSecurityOptions': [
                    'string',
                ],
                'interactive': True|False,
                'pseudoTerminal': True|False,
                'dockerLabels': {
                    'string': 'string'
                },
                'ulimits': [
                    {
                        'name': 'core'|'cpu'|'data'|'fsize'|'locks'|'memlock'|'msgqueue'|'nice'|'nofile'|'nproc'|'rss'|'rtprio'|'rttime'|'sigpending'|'stack',
                        'softLimit': 123,
                        'hardLimit': 123
                    },
                ],
                'logConfiguration': {
                    'logDriver': 'json-file'|'syslog'|'journald'|'gelf'|'fluentd'|'awslogs'|'splunk',
                    'options': {
                        'string': 'string'
                    }
                },
                'healthCheck': {
                    'command': [
                        'string',
                    ],
                    'interval': 123,
                    'timeout': 123,
                    'retries': 123,
                    'startPeriod': 123
                },
                'systemControls': [
                    {
                        'namespace': 'string',
                        'value': 'string'
                    },
                ]
            },
        ],
        volumes=[
            {
                'name': 'string',
                'host': {
                    'sourcePath': 'string'
                },
                'dockerVolumeConfiguration': {
                    'scope': 'task'|'shared',
                    'autoprovision': True|False,
                    'driver': 'string',
                    'driverOpts': {
                        'string': 'string'
                    },
                    'labels': {
                        'string': 'string'
                    }
                }
            },
        ],
        placementConstraints=[
            {
                'type': 'memberOf',
                'expression': 'string'
            },
        ],
        requiresCompatibilities=[
            'EC2'|'FARGATE',
        ],
        cpu='string',
        memory='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        pidMode='host'|'task',
        ipcMode='host'|'task'|'none'
    )
    
    
    :type family: string
    :param family: [REQUIRED]
            You must specify a family for a task definition, which allows you to track multiple versions of the same task definition. The family is used as a name for your task definition. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.
            

    :type taskRoleArn: string
    :param taskRoleArn: The short name or full Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role. For more information, see IAM Roles for Tasks in the Amazon Elastic Container Service Developer Guide .

    :type executionRoleArn: string
    :param executionRoleArn: The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.

    :type networkMode: string
    :param networkMode: The Docker networking mode to use for the containers in the task. The valid values are none , bridge , awsvpc , and host . The default Docker network mode is bridge . If you are using the Fargate launch type, the awsvpc network mode is required. If you are using the EC2 launch type, any network mode can be used. If the network mode is set to none , you cannot specify port mappings in your container definitions, and the tasks containers do not have external connectivity. The host and awsvpc network modes offer the highest networking performance for containers because they use the EC2 network stack instead of the virtualized network stack provided by the bridge mode.
            With the host and awsvpc network modes, exposed container ports are mapped directly to the corresponding host port (for the host network mode) or the attached elastic network interface port (for the awsvpc network mode), so you cannot take advantage of dynamic host port mappings.
            If the network mode is awsvpc , the task is allocated an elastic network interface, and you must specify a NetworkConfiguration value when you create a service or run a task with the task definition. For more information, see Task Networking in the Amazon Elastic Container Service Developer Guide .
            Note
            Currently, only Amazon ECS-optimized AMIs, other Amazon Linux variants with the ecs-init package, or AWS Fargate infrastructure support the awsvpc network mode.
            If the network mode is host , you cannot run multiple instantiations of the same task on a single container instance when port mappings are used.
            Docker for Windows uses different network modes than Docker for Linux. When you register a task definition with Windows containers, you must not specify a network mode. If you use the console to register a task definition with Windows containers, you must choose the <default> network mode object.
            For more information, see Network settings in the Docker run reference .
            

    :type containerDefinitions: list
    :param containerDefinitions: [REQUIRED]
            A list of container definitions in JSON format that describe the different containers that make up your task.
            (dict) --Container definitions are used in task definitions to describe the different containers that are launched as part of a task.
            name (string) --The name of a container. If you are linking multiple containers together in a task definition, the name of one container can be entered in the links of another container to connect the containers. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This parameter maps to name in the Create a container section of the Docker Remote API and the --name option to docker run .
            image (string) --The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with either `` repository-url /image :tag `` or `` repository-url /image @*digest* `` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to Image in the Create a container section of the Docker Remote API and the IMAGE parameter of docker run .
            When a new task starts, the Amazon ECS container agent pulls the latest version of the specified image and tag for the container to use. However, subsequent updates to a repository image are not propagated to already running tasks.
            Images in Amazon ECR repositories can be specified by either using the full registry/repository:tag or registry/repository@digest . For example, 012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>:latest or 012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>@sha256:94afd1f2e64d908bc90dbca0035a5b567EXAMPLE .
            Images in official repositories on Docker Hub use a single name (for example, ubuntu or mongo ).
            Images in other repositories on Docker Hub are qualified with an organization name (for example, amazon/amazon-ecs-agent ).
            Images in other online repositories are qualified further by a domain name (for example, quay.io/assemblyline/ubuntu ).
            repositoryCredentials (dict) --The private repository authentication credentials to use.
            credentialsParameter (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the secret containing the private repository credentials.
            Note
            When you are using the Amazon ECS API, AWS CLI, or AWS SDK, if the secret exists in the same Region as the task that you are launching then you can use either the full ARN or the name of the secret. When you are using the AWS Management Console, you must specify the full ARN of the secret.
            
            cpu (integer) --The number of cpu units reserved for the container. This parameter maps to CpuShares in the Create a container section of the Docker Remote API and the --cpu-shares option to docker run .
            This field is optional for tasks using the Fargate launch type, and the only requirement is that the total amount of CPU reserved for all containers within a task be lower than the task-level cpu value.
            Note
            You can determine the number of CPU units that are available per EC2 instance type by multiplying the vCPUs listed for that instance type on the Amazon EC2 Instances detail page by 1,024.
            For example, if you run a single-container task on a single-core instance type with 512 CPU units specified for that container, and that is the only task running on the container instance, that container could use the full 1,024 CPU unit share at any given time. However, if you launched another copy of the same task on that container instance, each task would be guaranteed a minimum of 512 CPU units when needed, and each container could float to higher CPU usage if the other container was not using it, but if both tasks were 100% active all of the time, they would be limited to 512 CPU units.
            Linux containers share unallocated CPU units with other containers on the container instance with the same ratio as their allocated amount. For example, if you run a single-container task on a single-core instance type with 512 CPU units specified for that container, and that is the only task running on the container instance, that container could use the full 1,024 CPU unit share at any given time. However, if you launched another copy of the same task on that container instance, each task would be guaranteed a minimum of 512 CPU units when needed, and each container could float to higher CPU usage if the other container was not using it, but if both tasks were 100% active all of the time, they would be limited to 512 CPU units.
            On Linux container instances, the Docker daemon on the container instance uses the CPU value to calculate the relative CPU share ratios for running containers. For more information, see CPU share constraint in the Docker documentation. The minimum valid CPU share value that the Linux kernel allows is 2. However, the CPU parameter is not required, and you can use CPU values below 2 in your container definitions. For CPU values below 2 (including null), the behavior varies based on your Amazon ECS container agent version:
            Agent versions less than or equal to 1.1.0: Null and zero CPU values are passed to Docker as 0, which Docker then converts to 1,024 CPU shares. CPU values of 1 are passed to Docker as 1, which the Linux kernel converts to two CPU shares.
            Agent versions greater than or equal to 1.2.0: Null, zero, and CPU values of 1 are passed to Docker as 2.
            On Windows container instances, the CPU limit is enforced as an absolute limit, or a quota. Windows containers only have access to the specified amount of CPU that is described in the task definition.
            memory (integer) --The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. This parameter maps to Memory in the Create a container section of the Docker Remote API and the --memory option to docker run .
            If your containers are part of a task using the Fargate launch type, this field is optional and the only requirement is that the total amount of memory reserved for all containers within a task be lower than the task memory value.
            For containers that are part of a task using the EC2 launch type, you must specify a non-zero integer for one or both of memory or memoryReservation in container definitions. If you specify both, memory must be greater than memoryReservation . If you specify memoryReservation , then that value is subtracted from the available memory resources for the container instance on which the container is placed. Otherwise, the value of memory is used.
            The Docker daemon reserves a minimum of 4 MiB of memory for a container, so you should not specify fewer than 4 MiB of memory for your containers.
            memoryReservation (integer) --The soft limit (in MiB) of memory to reserve for the container. When system memory is under heavy contention, Docker attempts to keep the container memory to this soft limit. However, your container can consume more memory when it needs to, up to either the hard limit specified with the memory parameter (if applicable), or all of the available memory on the container instance, whichever comes first. This parameter maps to MemoryReservation in the Create a container section of the Docker Remote API and the --memory-reservation option to docker run .
            You must specify a non-zero integer for one or both of memory or memoryReservation in container definitions. If you specify both, memory must be greater than memoryReservation . If you specify memoryReservation , then that value is subtracted from the available memory resources for the container instance on which the container is placed. Otherwise, the value of memory is used.
            For example, if your container normally uses 128 MiB of memory, but occasionally bursts to 256 MiB of memory for short periods of time, you can set a memoryReservation of 128 MiB, and a memory hard limit of 300 MiB. This configuration would allow the container to only reserve 128 MiB of memory from the remaining resources on the container instance, but also allow the container to consume more memory resources when needed.
            The Docker daemon reserves a minimum of 4 MiB of memory for a container, so you should not specify fewer than 4 MiB of memory for your containers.
            links (list) --The link parameter allows containers to communicate with each other without the need for port mappings. Only supported if the network mode of a task definition is set to bridge . The name:internalName construct is analogous to name:alias in Docker links. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. For more information about linking Docker containers, go to https://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/ . This parameter maps to Links in the Create a container section of the Docker Remote API and the --link option to ` docker run https://docs.docker.com/engine/reference/commandline/run/`__ .
            Note
            This parameter is not supported for Windows containers.
            Warning
            Containers that are collocated on a single container instance may be able to communicate with each other without requiring links or host port mappings. Network isolation is achieved on the container instance using security groups and VPC settings.
            (string) --
            portMappings (list) --The list of port mappings for the container. Port mappings allow containers to access ports on the host container instance to send or receive traffic.
            For task definitions that use the awsvpc network mode, you should only specify the containerPort . The hostPort can be left blank or it must be the same value as the containerPort .
            Port mappings on Windows use the NetNAT gateway address rather than localhost . There is no loopback for port mappings on Windows, so you cannot access a container's mapped port from the host itself.
            This parameter maps to PortBindings in the Create a container section of the Docker Remote API and the --publish option to docker run . If the network mode of a task definition is set to none , then you can't specify port mappings. If the network mode of a task definition is set to host , then host ports must either be undefined or they must match the container port in the port mapping.
            Note
            After a task reaches the RUNNING status, manual and automatic host and container port assignments are visible in the Network Bindings section of a container description for a selected task in the Amazon ECS console. The assignments are also visible in the networkBindings section DescribeTasks responses.
            (dict) --Port mappings allow containers to access ports on the host container instance to send or receive traffic. Port mappings are specified as part of the container definition.
            If you are using containers in a task with the awsvpc or host network mode, exposed ports should be specified using containerPort . The hostPort can be left blank or it must be the same value as the containerPort .
            After a task reaches the RUNNING status, manual and automatic host and container port assignments are visible in the networkBindings section of DescribeTasks API responses.
            containerPort (integer) --The port number on the container that is bound to the user-specified or automatically assigned host port.
            If you are using containers in a task with the awsvpc or host network mode, exposed ports should be specified using containerPort .
            If you are using containers in a task with the bridge network mode and you specify a container port and not a host port, your container automatically receives a host port in the ephemeral port range. For more information, see hostPort . Port mappings that are automatically assigned in this way do not count toward the 100 reserved ports limit of a container instance.
            hostPort (integer) --The port number on the container instance to reserve for your container.
            If you are using containers in a task with the awsvpc or host network mode, the hostPort can either be left blank or set to the same value as the containerPort .
            If you are using containers in a task with the bridge network mode, you can specify a non-reserved host port for your container port mapping, or you can omit the hostPort (or set it to 0 ) while specifying a containerPort and your container automatically receives a port in the ephemeral port range for your container instance operating system and Docker version.
            The default ephemeral port range for Docker version 1.6.0 and later is listed on the instance under /proc/sys/net/ipv4/ip_local_port_range . If this kernel parameter is unavailable, the default ephemeral port range from 49153 through 65535 is used. Do not attempt to specify a host port in the ephemeral port range as these are reserved for automatic assignment. In general, ports below 32768 are outside of the ephemeral port range.
            Note
            The default ephemeral port range from 49153 through 65535 is always used for Docker versions before 1.6.0.
            The default reserved ports are 22 for SSH, the Docker ports 2375 and 2376, and the Amazon ECS container agent ports 51678 and 51679. Any host port that was previously specified in a running task is also reserved while the task is running (after a task stops, the host port is released). The current reserved ports are displayed in the remainingResources of DescribeContainerInstances output. A container instance may have up to 100 reserved ports at a time, including the default reserved ports. Aautomatically assigned ports do not count toward the 100 reserved ports limit.
            protocol (string) --The protocol used for the port mapping. Valid values are tcp and udp . The default is tcp .
            
            essential (boolean) --If the essential parameter of a container is marked as true , and that container fails or stops for any reason, all other containers that are part of the task are stopped. If the essential parameter of a container is marked as false , then its failure does not affect the rest of the containers in a task. If this parameter is omitted, a container is assumed to be essential.
            All tasks must have at least one essential container. If you have an application that is composed of multiple containers, you should group containers that are used for a common purpose into components, and separate the different components into multiple task definitions. For more information, see Application Architecture in the Amazon Elastic Container Service Developer Guide .
            entryPoint (list) --
            Warning
            Early versions of the Amazon ECS container agent do not properly handle entryPoint parameters. If you have problems using entryPoint , update your container agent or enter your commands and arguments as command array items instead.
            The entry point that is passed to the container. This parameter maps to Entrypoint in the Create a container section of the Docker Remote API and the --entrypoint option to docker run . For more information, see https://docs.docker.com/engine/reference/builder/#entrypoint .
            (string) --
            command (list) --The command that is passed to the container. This parameter maps to Cmd in the Create a container section of the Docker Remote API and the COMMAND parameter to docker run . For more information, see https://docs.docker.com/engine/reference/builder/#cmd .
            (string) --
            environment (list) --The environment variables to pass to a container. This parameter maps to Env in the Create a container section of the Docker Remote API and the --env option to docker run .
            Warning
            We do not recommend using plaintext environment variables for sensitive information, such as credential data.
            (dict) --A key-value pair object.
            name (string) --The name of the key-value pair. For environment variables, this is the name of the environment variable.
            value (string) --The value of the key-value pair. For environment variables, this is the value of the environment variable.
            
            mountPoints (list) --The mount points for data volumes in your container.
            This parameter maps to Volumes in the Create a container section of the Docker Remote API and the --volume option to docker run .
            Windows containers can mount whole directories on the same drive as $env:ProgramData . Windows containers cannot mount directories on a different drive, and mount point cannot be across drives.
            (dict) --Details on a volume mount point that is used in a container definition.
            sourceVolume (string) --The name of the volume to mount. Must be a volume name referenced in the name parameter of task definition volume .
            containerPath (string) --The path on the container to mount the host volume at.
            readOnly (boolean) --If this value is true , the container has read-only access to the volume. If this value is false , then the container can write to the volume. The default value is false .
            
            volumesFrom (list) --Data volumes to mount from another container. This parameter maps to VolumesFrom in the Create a container section of the Docker Remote API and the --volumes-from option to docker run .
            (dict) --Details on a data volume from another container in the same task definition.
            sourceContainer (string) --The name of another container within the same task definition from which to mount volumes.
            readOnly (boolean) --If this value is true , the container has read-only access to the volume. If this value is false , then the container can write to the volume. The default value is false .
            
            linuxParameters (dict) --Linux-specific modifications that are applied to the container, such as Linux KernelCapabilities .
            Note
            This parameter is not supported for Windows containers.
            capabilities (dict) --The Linux capabilities for the container that are added to or dropped from the default configuration provided by Docker.
            Note
            If you are using tasks that use the Fargate launch type, capabilities is supported but the add parameter is not supported.
            add (list) --The Linux capabilities for the container that have been added to the default configuration provided by Docker. This parameter maps to CapAdd in the Create a container section of the Docker Remote API and the --cap-add option to docker run .
            Note
            If you are using tasks that use the Fargate launch type, the add parameter is not supported.
            Valid values: 'ALL' | 'AUDIT_CONTROL' | 'AUDIT_WRITE' | 'BLOCK_SUSPEND' | 'CHOWN' | 'DAC_OVERRIDE' | 'DAC_READ_SEARCH' | 'FOWNER' | 'FSETID' | 'IPC_LOCK' | 'IPC_OWNER' | 'KILL' | 'LEASE' | 'LINUX_IMMUTABLE' | 'MAC_ADMIN' | 'MAC_OVERRIDE' | 'MKNOD' | 'NET_ADMIN' | 'NET_BIND_SERVICE' | 'NET_BROADCAST' | 'NET_RAW' | 'SETFCAP' | 'SETGID' | 'SETPCAP' | 'SETUID' | 'SYS_ADMIN' | 'SYS_BOOT' | 'SYS_CHROOT' | 'SYS_MODULE' | 'SYS_NICE' | 'SYS_PACCT' | 'SYS_PTRACE' | 'SYS_RAWIO' | 'SYS_RESOURCE' | 'SYS_TIME' | 'SYS_TTY_CONFIG' | 'SYSLOG' | 'WAKE_ALARM'
            (string) --
            drop (list) --The Linux capabilities for the container that have been removed from the default configuration provided by Docker. This parameter maps to CapDrop in the Create a container section of the Docker Remote API and the --cap-drop option to docker run .
            Valid values: 'ALL' | 'AUDIT_CONTROL' | 'AUDIT_WRITE' | 'BLOCK_SUSPEND' | 'CHOWN' | 'DAC_OVERRIDE' | 'DAC_READ_SEARCH' | 'FOWNER' | 'FSETID' | 'IPC_LOCK' | 'IPC_OWNER' | 'KILL' | 'LEASE' | 'LINUX_IMMUTABLE' | 'MAC_ADMIN' | 'MAC_OVERRIDE' | 'MKNOD' | 'NET_ADMIN' | 'NET_BIND_SERVICE' | 'NET_BROADCAST' | 'NET_RAW' | 'SETFCAP' | 'SETGID' | 'SETPCAP' | 'SETUID' | 'SYS_ADMIN' | 'SYS_BOOT' | 'SYS_CHROOT' | 'SYS_MODULE' | 'SYS_NICE' | 'SYS_PACCT' | 'SYS_PTRACE' | 'SYS_RAWIO' | 'SYS_RESOURCE' | 'SYS_TIME' | 'SYS_TTY_CONFIG' | 'SYSLOG' | 'WAKE_ALARM'
            (string) --
            
            devices (list) --Any host devices to expose to the container. This parameter maps to Devices in the Create a container section of the Docker Remote API and the --device option to docker run .
            Note
            If you are using tasks that use the Fargate launch type, the devices parameter is not supported.
            (dict) --An object representing a container instance host device.
            hostPath (string) -- [REQUIRED]The path for the device on the host container instance.
            containerPath (string) --The path inside the container at which to expose the host device.
            permissions (list) --The explicit permissions to provide to the container for the device. By default, the container has permissions for read , write , and mknod for the device.
            (string) --
            
            initProcessEnabled (boolean) --Run an init process inside the container that forwards signals and reaps processes. This parameter maps to the --init option to docker run . This parameter requires version 1.25 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: sudo docker version --format '{{.Server.APIVersion}}'
            sharedMemorySize (integer) --The value for the size (in MiB) of the /dev/shm volume. This parameter maps to the --shm-size option to docker run .
            Note
            If you are using tasks that use the Fargate launch type, the sharedMemorySize parameter is not supported.
            tmpfs (list) --The container path, mount options, and size (in MiB) of the tmpfs mount. This parameter maps to the --tmpfs option to docker run .
            Note
            If you are using tasks that use the Fargate launch type, the tmpfs parameter is not supported.
            (dict) --The container path, mount options, and size of the tmpfs mount.
            containerPath (string) -- [REQUIRED]The absolute file path where the tmpfs volume is to be mounted.
            size (integer) -- [REQUIRED]The size (in MiB) of the tmpfs volume.
            mountOptions (list) --The list of tmpfs volume mount options.
            Valid values: 'defaults' | 'ro' | 'rw' | 'suid' | 'nosuid' | 'dev' | 'nodev' | 'exec' | 'noexec' | 'sync' | 'async' | 'dirsync' | 'remount' | 'mand' | 'nomand' | 'atime' | 'noatime' | 'diratime' | 'nodiratime' | 'bind' | 'rbind' | 'unbindable' | 'runbindable' | 'private' | 'rprivate' | 'shared' | 'rshared' | 'slave' | 'rslave' | 'relatime' | 'norelatime' | 'strictatime' | 'nostrictatime' | 'mode' | 'uid' | 'gid' | 'nr_inodes' | 'nr_blocks' | 'mpol'
            (string) --
            
            
            secrets (list) --The secrets to pass to the container.
            (dict) --An object representing the secret to expose to your container.
            name (string) -- [REQUIRED]The value to set as the environment variable on the container.
            valueFrom (string) -- [REQUIRED]The secret to expose to the container. Supported values are either the full ARN or the name of the parameter in the AWS Systems Manager Parameter Store.
            
            hostname (string) --The hostname to use for your container. This parameter maps to Hostname in the Create a container section of the Docker Remote API and the --hostname option to docker run .
            Note
            The hostname parameter is not supported if you are using the awsvpc network mode.
            user (string) --The user name to use inside the container. This parameter maps to User in the Create a container section of the Docker Remote API and the --user option to docker run .
            Note
            This parameter is not supported for Windows containers.
            workingDirectory (string) --The working directory in which to run commands inside the container. This parameter maps to WorkingDir in the Create a container section of the Docker Remote API and the --workdir option to docker run .
            disableNetworking (boolean) --When this parameter is true, networking is disabled within the container. This parameter maps to NetworkDisabled in the Create a container section of the Docker Remote API .
            Note
            This parameter is not supported for Windows containers.
            privileged (boolean) --When this parameter is true, the container is given elevated privileges on the host container instance (similar to the root user). This parameter maps to Privileged in the Create a container section of the Docker Remote API and the --privileged option to docker run .
            Note
            This parameter is not supported for Windows containers or tasks using the Fargate launch type.
            readonlyRootFilesystem (boolean) --When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ReadonlyRootfs in the Create a container section of the Docker Remote API and the --read-only option to docker run .
            Note
            This parameter is not supported for Windows containers.
            dnsServers (list) --A list of DNS servers that are presented to the container. This parameter maps to Dns in the Create a container section of the Docker Remote API and the --dns option to docker run .
            Note
            This parameter is not supported for Windows containers.
            (string) --
            dnsSearchDomains (list) --A list of DNS search domains that are presented to the container. This parameter maps to DnsSearch in the Create a container section of the Docker Remote API and the --dns-search option to docker run .
            Note
            This parameter is not supported for Windows containers.
            (string) --
            extraHosts (list) --A list of hostnames and IP address mappings to append to the /etc/hosts file on the container. This parameter maps to ExtraHosts in the Create a container section of the Docker Remote API and the --add-host option to docker run .
            Note
            This parameter is not supported for Windows containers or tasks that use the awsvpc network mode.
            (dict) --Hostnames and IP address entries that are added to the /etc/hosts file of a container via the extraHosts parameter of its ContainerDefinition .
            hostname (string) -- [REQUIRED]The hostname to use in the /etc/hosts entry.
            ipAddress (string) -- [REQUIRED]The IP address to use in the /etc/hosts entry.
            
            dockerSecurityOptions (list) --A list of strings to provide custom labels for SELinux and AppArmor multi-level security systems. This field is not valid for containers in tasks using the Fargate launch type.
            This parameter maps to SecurityOpt in the Create a container section of the Docker Remote API and the --security-opt option to docker run .
            Note
            The Amazon ECS container agent running on a container instance must register with the ECS_SELINUX_CAPABLE=true or ECS_APPARMOR_CAPABLE=true environment variables before containers placed on that instance can use these security options. For more information, see Amazon ECS Container Agent Configuration in the Amazon Elastic Container Service Developer Guide .
            This parameter is not supported for Windows containers.
            (string) --
            interactive (boolean) --When this parameter is true , this allows you to deploy containerized applications that require stdin or a tty to be allocated. This parameter maps to OpenStdin in the Create a container section of the Docker Remote API and the --interactive option to docker run .
            pseudoTerminal (boolean) --When this parameter is true , a TTY is allocated. This parameter maps to Tty in the Create a container section of the Docker Remote API and the --tty option to docker run .
            dockerLabels (dict) --A key/value map of labels to add to the container. This parameter maps to Labels in the Create a container section of the Docker Remote API and the --label option to docker run . This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: sudo docker version --format '{{.Server.APIVersion}}'
            (string) --
            (string) --
            
            ulimits (list) --A list of ulimits to set in the container. This parameter maps to Ulimits in the Create a container section of the Docker Remote API and the --ulimit option to docker run . Valid naming values are displayed in the Ulimit data type. This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: sudo docker version --format '{{.Server.APIVersion}}'
            Note
            This parameter is not supported for Windows containers.
            (dict) --The ulimit settings to pass to the container.
            name (string) -- [REQUIRED]The type of the ulimit .
            softLimit (integer) -- [REQUIRED]The soft limit for the ulimit type.
            hardLimit (integer) -- [REQUIRED]The hard limit for the ulimit type.
            
            logConfiguration (dict) --The log configuration specification for the container.
            If you are using the Fargate launch type, the only supported value is awslogs .
            This parameter maps to LogConfig in the Create a container section of the Docker Remote API and the --log-driver option to docker run . By default, containers use the same logging driver that the Docker daemon uses. However the container may use a different logging driver than the Docker daemon by specifying a log driver with this parameter in the container definition. To use a different logging driver for a container, the log system must be configured properly on the container instance (or on a different log server for remote logging options). For more information on the options for different supported log drivers, see Configure logging drivers in the Docker documentation.
            Note
            Amazon ECS currently supports a subset of the logging drivers available to the Docker daemon (shown in the LogConfiguration data type). Additional log drivers may be available in future releases of the Amazon ECS container agent.
            This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: sudo docker version --format '{{.Server.APIVersion}}'
            Note
            The Amazon ECS container agent running on a container instance must register the logging drivers available on that instance with the ECS_AVAILABLE_LOGGING_DRIVERS environment variable before containers placed on that instance can use these log configuration options. For more information, see Amazon ECS Container Agent Configuration in the Amazon Elastic Container Service Developer Guide .
            logDriver (string) -- [REQUIRED]The log driver to use for the container. The valid values listed for this parameter are log drivers that the Amazon ECS container agent can communicate with by default. If you are using the Fargate launch type, the only supported value is awslogs . For more information about using the awslogs driver, see Using the awslogs Log Driver in the Amazon Elastic Container Service Developer Guide .
            Note
            If you have a custom driver that is not listed above that you would like to work with the Amazon ECS container agent, you can fork the Amazon ECS container agent project that is available on GitHub and customize it to work with that driver. We encourage you to submit pull requests for changes that you would like to have included. However, Amazon Web Services does not currently support running modified copies of this software.
            This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: sudo docker version --format '{{.Server.APIVersion}}'
            options (dict) --The configuration options to send to the log driver. This parameter requires version 1.19 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: sudo docker version --format '{{.Server.APIVersion}}'
            (string) --
            (string) --
            
            healthCheck (dict) --The health check command and associated configuration parameters for the container. This parameter maps to HealthCheck in the Create a container section of the Docker Remote API and the HEALTHCHECK parameter of docker run .
            command (list) -- [REQUIRED]A string array representing the command that the container runs to determine if it is healthy. The string array must start with CMD to execute the command arguments directly, or CMD-SHELL to run the command with the container's default shell. For example:
            [ 'CMD-SHELL', 'curl -f http://localhost/ || exit 1' ]
            An exit code of 0 indicates success, and non-zero exit code indicates failure. For more information, see HealthCheck in the Create a container section of the Docker Remote API .
            (string) --
            interval (integer) --The time period in seconds between each health check execution. You may specify between 5 and 300 seconds. The default value is 30 seconds.
            timeout (integer) --The time period in seconds to wait for a health check to succeed before it is considered a failure. You may specify between 2 and 60 seconds. The default value is 5.
            retries (integer) --The number of times to retry a failed health check before the container is considered unhealthy. You may specify between 1 and 10 retries. The default value is 3.
            startPeriod (integer) --The optional grace period within which to provide containers time to bootstrap before failed health checks count towards the maximum number of retries. You may specify between 0 and 300 seconds. The startPeriod is disabled by default.
            Note
            If a health check succeeds within the startPeriod , then the container is considered healthy and any subsequent failures count toward the maximum number of retries.
            
            systemControls (list) --A list of namespaced kernel parameters to set in the container. This parameter maps to Sysctls in the Create a container section of the Docker Remote API and the --sysctl option to docker run .
            Note
            It is not recommended that you specify network-related systemControls parameters for multiple containers in a single task that also uses either the awsvpc or host network modes. For tasks that use the awsvpc network mode, the container that is started last determines which systemControls parameters take effect. For tasks that use the host network mode, it changes the container instance's namespaced kernel parameters as well as the containers.
            (dict) --A list of namespaced kernel parameters to set in the container. This parameter maps to Sysctls in the Create a container section of the Docker Remote API and the --sysctl option to docker run .
            It is not recommended that you specify network-related systemControls parameters for multiple containers in a single task that also uses either the awsvpc or host network mode for the following reasons:
            For tasks that use the awsvpc network mode, if you set systemControls for any container, it applies to all containers in the task. If you set different systemControls for multiple containers in a single task, the container that is started last determines which systemControls take effect.
            For tasks that use the host network mode, the systemControls parameter applies to the container instance's kernel parameter as well as that of all containers of any tasks running on that container instance.
            namespace (string) --The namespaced kernel parameter for which to set a value .
            value (string) --The value for the namespaced kernel parameter specified in namespace .
            
            
            

    :type volumes: list
    :param volumes: A list of volume definitions in JSON format that containers in your task may use.
            (dict) --A data volume used in a task definition. For tasks that use a Docker volume, specify a DockerVolumeConfiguration . For tasks that use a bind mount host volume, specify a host and optional sourcePath . For more information, see Using Data Volumes in Tasks .
            name (string) --The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the sourceVolume parameter of container definition mountPoints .
            host (dict) --This parameter is specified when you are using bind mount host volumes. Bind mount host volumes are supported when you are using either the EC2 or Fargate launch types. The contents of the host parameter determine whether your bind mount host volume persists on the host container instance and where it is stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data is not guaranteed to persist after the containers associated with it stop running.
            Windows containers can mount whole directories on the same drive as $env:ProgramData . Windows containers cannot mount directories on a different drive, and mount point cannot be across drives. For example, you can mount C:\my\path:C:\my\path and D:\:D:\ , but not D:\my\path:C:\my\path or D:\:C:\my\path .
            sourcePath (string) --When the host parameter is used, specify a sourcePath to declare the path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If the host parameter contains a sourcePath file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the sourcePath value does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.
            If you are using the Fargate launch type, the sourcePath parameter is not supported.
            dockerVolumeConfiguration (dict) --This parameter is specified when you are using Docker volumes. Docker volumes are only supported when you are using the EC2 launch type. Windows containers only support the use of the local driver. To use bind mounts, specify a host instead.
            scope (string) --The scope for the Docker volume that determines its lifecycle. Docker volumes that are scoped to a task are automatically provisioned when the task starts and destroyed when the task stops. Docker volumes that are scoped as shared persist after the task stops.
            autoprovision (boolean) --If this value is true , the Docker volume is created if it does not already exist.
            Note
            This field is only used if the scope is shared .
            driver (string) --The Docker volume driver to use. The driver value must match the driver name provided by Docker because it is used for task placement. If the driver was installed using the Docker plugin CLI, use docker plugin ls to retrieve the driver name from your container instance. If the driver was installed using another method, use Docker plugin discovery to retrieve the driver name. For more information, see Docker plugin discovery . This parameter maps to Driver in the Create a volume section of the Docker Remote API and the xxdriver option to ` docker volume create https://docs.docker.com/engine/reference/commandline/volume_create/`__ .
            driverOpts (dict) --A map of Docker driver-specific options passed through. This parameter maps to DriverOpts in the Create a volume section of the Docker Remote API and the xxopt option to ` docker volume create https://docs.docker.com/engine/reference/commandline/volume_create/`__ .
            (string) --
            (string) --
            
            labels (dict) --Custom metadata to add to your Docker volume. This parameter maps to Labels in the Create a volume section of the Docker Remote API and the xxlabel option to ` docker volume create https://docs.docker.com/engine/reference/commandline/volume_create/`__ .
            (string) --
            (string) --
            
            
            

    :type placementConstraints: list
    :param placementConstraints: An array of placement constraint objects to use for the task. You can specify a maximum of 10 constraints per task (this limit includes constraints in the task definition and those specified at runtime).
            (dict) --An object representing a constraint on task placement in the task definition.
            If you are using the Fargate launch type, task placement constraints are not supported.
            For more information, see Task Placement Constraints in the Amazon Elastic Container Service Developer Guide .
            type (string) --The type of constraint. The DistinctInstance constraint ensures that each task in a particular group is running on a different container instance. The MemberOf constraint restricts selection to be from a group of valid candidates.
            expression (string) --A cluster query language expression to apply to the constraint. For more information, see Cluster Query Language in the Amazon Elastic Container Service Developer Guide .
            
            

    :type requiresCompatibilities: list
    :param requiresCompatibilities: The launch type required by the task. If no value is specified, it defaults to EC2 .
            (string) --
            

    :type cpu: string
    :param cpu: The number of CPU units used by the task. It can be expressed as an integer using CPU units, for example 1024 , or as a string using vCPUs, for example 1 vCPU or 1 vcpu , in a task definition. String values are converted to an integer indicating the CPU units when the task definition is registered.
            Note
            Task-level CPU and memory parameters are ignored for Windows containers. We recommend specifying container-level resources for Windows containers.
            If you are using the EC2 launch type, this field is optional. Supported values are between 128 CPU units (0.125 vCPUs) and 10240 CPU units (10 vCPUs).
            If you are using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of supported values for the memory parameter:
            256 (.25 vCPU) - Available memory values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB)
            512 (.5 vCPU) - Available memory values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB)
            1024 (1 vCPU) - Available memory values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB)
            2048 (2 vCPU) - Available memory values: Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB)
            4096 (4 vCPU) - Available memory values: Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB)
            

    :type memory: string
    :param memory: The amount of memory (in MiB) used by the task. It can be expressed as an integer using MiB, for example 1024 , or as a string using GB, for example 1GB or 1 GB , in a task definition. String values are converted to an integer indicating the MiB when the task definition is registered.
            Note
            Task-level CPU and memory parameters are ignored for Windows containers. We recommend specifying container-level resources for Windows containers.
            If using the EC2 launch type, this field is optional.
            If using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of supported values for the cpu parameter:
            512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available cpu values: 256 (.25 vCPU)
            1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available cpu values: 512 (.5 vCPU)
            2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available cpu values: 1024 (1 vCPU)
            Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available cpu values: 2048 (2 vCPU)
            Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available cpu values: 4096 (4 vCPU)
            

    :type tags: list
    :param tags: The metadata that you apply to the task definition to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
            (dict) --The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
            key (string) --One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.
            value (string) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).
            
            

    :type pidMode: string
    :param pidMode: The process namespace to use for the containers in the task. The valid values are host or task . If host is specified, then all containers within the tasks that specified the host PID mode on the same container instance share the same IPC resources with the host Amazon EC2 instance. If task is specified, all containers within the specified task share the same process namespace. If no value is specified, the default is a private namespace. For more information, see PID settings in the Docker run reference .
            If the host PID mode is used, be aware that there is a heightened risk of undesired process namespace expose. For more information, see Docker security .
            Note
            This parameter is not supported for Windows containers or tasks using the Fargate launch type.
            

    :type ipcMode: string
    :param ipcMode: The IPC resource namespace to use for the containers in the task. The valid values are host , task , or none . If host is specified, then all containers within the tasks that specified the host IPC mode on the same container instance share the same IPC resources with the host Amazon EC2 instance. If task is specified, all containers within the specified task share the same IPC resources. If none is specified, then IPC resources within the containers of a task are private and not shared with other containers in a task or on the container instance. If no value is specified, then the IPC resource namespace sharing depends on the Docker daemon setting on the container instance. For more information, see IPC settings in the Docker run reference .
            If the host IPC mode is used, be aware that there is a heightened risk of undesired IPC namespace expose. For more information, see Docker security .
            If you are setting namespaced kernel parameters using systemControls for the containers in the task, the following will apply to your IPC resource namespace. For more information, see System Controls in the Amazon Elastic Container Service Developer Guide .
            For tasks that use the host IPC mode, IPC namespace related systemControls are not supported.
            For tasks that use the task IPC mode, IPC namespace related systemControls will apply to all containers within a task.
            Note
            This parameter is not supported for Windows containers or tasks using the Fargate launch type.
            

    :rtype: dict
    :return: {
        'taskDefinition': {
            'taskDefinitionArn': 'string',
            'containerDefinitions': [
                {
                    'name': 'string',
                    'image': 'string',
                    'repositoryCredentials': {
                        'credentialsParameter': 'string'
                    },
                    'cpu': 123,
                    'memory': 123,
                    'memoryReservation': 123,
                    'links': [
                        'string',
                    ],
                    'portMappings': [
                        {
                            'containerPort': 123,
                            'hostPort': 123,
                            'protocol': 'tcp'|'udp'
                        },
                    ],
                    'essential': True|False,
                    'entryPoint': [
                        'string',
                    ],
                    'command': [
                        'string',
                    ],
                    'environment': [
                        {
                            'name': 'string',
                            'value': 'string'
                        },
                    ],
                    'mountPoints': [
                        {
                            'sourceVolume': 'string',
                            'containerPath': 'string',
                            'readOnly': True|False
                        },
                    ],
                    'volumesFrom': [
                        {
                            'sourceContainer': 'string',
                            'readOnly': True|False
                        },
                    ],
                    'linuxParameters': {
                        'capabilities': {
                            'add': [
                                'string',
                            ],
                            'drop': [
                                'string',
                            ]
                        },
                        'devices': [
                            {
                                'hostPath': 'string',
                                'containerPath': 'string',
                                'permissions': [
                                    'read'|'write'|'mknod',
                                ]
                            },
                        ],
                        'initProcessEnabled': True|False,
                        'sharedMemorySize': 123,
                        'tmpfs': [
                            {
                                'containerPath': 'string',
                                'size': 123,
                                'mountOptions': [
                                    'string',
                                ]
                            },
                        ]
                    },
                    'secrets': [
                        {
                            'name': 'string',
                            'valueFrom': 'string'
                        },
                    ],
                    'hostname': 'string',
                    'user': 'string',
                    'workingDirectory': 'string',
                    'disableNetworking': True|False,
                    'privileged': True|False,
                    'readonlyRootFilesystem': True|False,
                    'dnsServers': [
                        'string',
                    ],
                    'dnsSearchDomains': [
                        'string',
                    ],
                    'extraHosts': [
                        {
                            'hostname': 'string',
                            'ipAddress': 'string'
                        },
                    ],
                    'dockerSecurityOptions': [
                        'string',
                    ],
                    'interactive': True|False,
                    'pseudoTerminal': True|False,
                    'dockerLabels': {
                        'string': 'string'
                    },
                    'ulimits': [
                        {
                            'name': 'core'|'cpu'|'data'|'fsize'|'locks'|'memlock'|'msgqueue'|'nice'|'nofile'|'nproc'|'rss'|'rtprio'|'rttime'|'sigpending'|'stack',
                            'softLimit': 123,
                            'hardLimit': 123
                        },
                    ],
                    'logConfiguration': {
                        'logDriver': 'json-file'|'syslog'|'journald'|'gelf'|'fluentd'|'awslogs'|'splunk',
                        'options': {
                            'string': 'string'
                        }
                    },
                    'healthCheck': {
                        'command': [
                            'string',
                        ],
                        'interval': 123,
                        'timeout': 123,
                        'retries': 123,
                        'startPeriod': 123
                    },
                    'systemControls': [
                        {
                            'namespace': 'string',
                            'value': 'string'
                        },
                    ]
                },
            ],
            'family': 'string',
            'taskRoleArn': 'string',
            'executionRoleArn': 'string',
            'networkMode': 'bridge'|'host'|'awsvpc'|'none',
            'revision': 123,
            'volumes': [
                {
                    'name': 'string',
                    'host': {
                        'sourcePath': 'string'
                    },
                    'dockerVolumeConfiguration': {
                        'scope': 'task'|'shared',
                        'autoprovision': True|False,
                        'driver': 'string',
                        'driverOpts': {
                            'string': 'string'
                        },
                        'labels': {
                            'string': 'string'
                        }
                    }
                },
            ],
            'status': 'ACTIVE'|'INACTIVE',
            'requiresAttributes': [
                {
                    'name': 'string',
                    'value': 'string',
                    'targetType': 'container-instance',
                    'targetId': 'string'
                },
            ],
            'placementConstraints': [
                {
                    'type': 'memberOf',
                    'expression': 'string'
                },
            ],
            'compatibilities': [
                'EC2'|'FARGATE',
            ],
            'requiresCompatibilities': [
                'EC2'|'FARGATE',
            ],
            'cpu': 'string',
            'memory': 'string',
            'pidMode': 'host'|'task',
            'ipcMode': 'host'|'task'|'none'
        },
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    }
    
    
    :returns: 
    When a new task starts, the Amazon ECS container agent pulls the latest version of the specified image and tag for the container to use. However, subsequent updates to a repository image are not propagated to already running tasks.
    Images in Amazon ECR repositories can be specified by either using the full registry/repository:tag or registry/repository@digest . For example, 012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>:latest or 012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>@sha256:94afd1f2e64d908bc90dbca0035a5b567EXAMPLE .
    Images in official repositories on Docker Hub use a single name (for example, ubuntu or mongo ).
    Images in other repositories on Docker Hub are qualified with an organization name (for example, amazon/amazon-ecs-agent ).
    Images in other online repositories are qualified further by a domain name (for example, quay.io/assemblyline/ubuntu ).
    
    """
    pass

def run_task(cluster=None, taskDefinition=None, overrides=None, count=None, startedBy=None, group=None, placementConstraints=None, placementStrategy=None, launchType=None, platformVersion=None, networkConfiguration=None, tags=None, enableECSManagedTags=None, propagateTags=None):
    """
    Starts a new task using the specified task definition.
    You can allow Amazon ECS to place tasks for you, or you can customize how Amazon ECS places tasks using placement constraints and placement strategies. For more information, see Scheduling Tasks in the Amazon Elastic Container Service Developer Guide .
    Alternatively, you can use  StartTask to use your own scheduler or place tasks manually on specific container instances.
    The Amazon ECS API follows an eventual consistency model, due to the distributed nature of the system supporting the API. This means that the result of an API command you run that affects your Amazon ECS resources might not be immediately visible to all subsequent commands you run. Keep this in mind when you carry out an API command that immediately follows a previous API command.
    To manage eventual consistency, you can do the following:
    See also: AWS API Documentation
    
    Examples
    This example runs the specified task definition on your default cluster.
    Expected Output:
    
    :example: response = client.run_task(
        cluster='string',
        taskDefinition='string',
        overrides={
            'containerOverrides': [
                {
                    'name': 'string',
                    'command': [
                        'string',
                    ],
                    'environment': [
                        {
                            'name': 'string',
                            'value': 'string'
                        },
                    ],
                    'cpu': 123,
                    'memory': 123,
                    'memoryReservation': 123
                },
            ],
            'taskRoleArn': 'string',
            'executionRoleArn': 'string'
        },
        count=123,
        startedBy='string',
        group='string',
        placementConstraints=[
            {
                'type': 'distinctInstance'|'memberOf',
                'expression': 'string'
            },
        ],
        placementStrategy=[
            {
                'type': 'random'|'spread'|'binpack',
                'field': 'string'
            },
        ],
        launchType='EC2'|'FARGATE',
        platformVersion='string',
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': [
                    'string',
                ],
                'securityGroups': [
                    'string',
                ],
                'assignPublicIp': 'ENABLED'|'DISABLED'
            }
        },
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        enableECSManagedTags=True|False,
        propagateTags='TASK_DEFINITION'|'SERVICE'
    )
    
    
    :type cluster: string
    :param cluster: The short name or full Amazon Resource Name (ARN) of the cluster on which to run your task. If you do not specify a cluster, the default cluster is assumed.

    :type taskDefinition: string
    :param taskDefinition: [REQUIRED]
            The family and revision (family:revision ) or full ARN of the task definition to run. If a revision is not specified, the latest ACTIVE revision is used.
            

    :type overrides: dict
    :param overrides: A list of container overrides in JSON format that specify the name of a container in the specified task definition and the overrides it should receive. You can override the default command for a container (that is specified in the task definition or Docker image) with a command override. You can also override existing environment variables (that are specified in the task definition or Docker image) on a container or add new environment variables to it with an environment override.
            Note
            A total of 8192 characters are allowed for overrides. This limit includes the JSON formatting characters of the override structure.
            containerOverrides (list) --One or more container overrides sent to a task.
            (dict) --The overrides that should be sent to a container.
            name (string) --The name of the container that receives the override. This parameter is required if any override is specified.
            command (list) --The command to send to the container that overrides the default command from the Docker image or the task definition. You must also specify a container name.
            (string) --
            environment (list) --The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.
            (dict) --A key-value pair object.
            name (string) --The name of the key-value pair. For environment variables, this is the name of the environment variable.
            value (string) --The value of the key-value pair. For environment variables, this is the value of the environment variable.
            
            cpu (integer) --The number of cpu units reserved for the container, instead of the default value from the task definition. You must also specify a container name.
            memory (integer) --The hard limit (in MiB) of memory to present to the container, instead of the default value from the task definition. If your container attempts to exceed the memory specified here, the container is killed. You must also specify a container name.
            memoryReservation (integer) --The soft limit (in MiB) of memory to reserve for the container, instead of the default value from the task definition. You must also specify a container name.
            
            taskRoleArn (string) --The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role.
            executionRoleArn (string) --The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.
            

    :type count: integer
    :param count: The number of instantiations of the specified task to place on your cluster. You can specify up to 10 tasks per call.

    :type startedBy: string
    :param startedBy: An optional tag specified when a task is started. For example, if you automatically trigger a task to run a batch process job, you could apply a unique identifier for that job to your task with the startedBy parameter. You can then identify which tasks belong to that job by filtering the results of a ListTasks call with the startedBy value. Up to 36 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.
            If a task is started by an Amazon ECS service, then the startedBy parameter contains the deployment ID of the service that starts it.
            

    :type group: string
    :param group: The name of the task group to associate with the task. The default value is the family name of the task definition (for example, family:my-family-name).

    :type placementConstraints: list
    :param placementConstraints: An array of placement constraint objects to use for the task. You can specify up to 10 constraints per task (including constraints in the task definition and those specified at runtime).
            (dict) --An object representing a constraint on task placement. For more information, see Task Placement Constraints in the Amazon Elastic Container Service Developer Guide .
            type (string) --The type of constraint. Use distinctInstance to ensure that each task in a particular group is running on a different container instance. Use memberOf to restrict the selection to a group of valid candidates. The value distinctInstance is not supported in task definitions.
            expression (string) --A cluster query language expression to apply to the constraint. You cannot specify an expression if the constraint type is distinctInstance . For more information, see Cluster Query Language in the Amazon Elastic Container Service Developer Guide .
            
            

    :type placementStrategy: list
    :param placementStrategy: The placement strategy objects to use for the task. You can specify a maximum of five strategy rules per task.
            (dict) --The task placement strategy for a task or service. For more information, see Task Placement Strategies in the Amazon Elastic Container Service Developer Guide .
            type (string) --The type of placement strategy. The random placement strategy randomly places tasks on available candidates. The spread placement strategy spreads placement across available candidates evenly based on the field parameter. The binpack strategy places tasks on available candidates that have the least available amount of the resource that is specified with the field parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task).
            field (string) --The field to apply the placement strategy against. For the spread placement strategy, valid values are instanceId (or host , which has the same effect), or any platform or custom attribute that is applied to a container instance, such as attribute:ecs.availability-zone . For the binpack placement strategy, valid values are cpu and memory . For the random placement strategy, this field is not used.
            
            

    :type launchType: string
    :param launchType: The launch type on which to run your task. For more information, see Amazon ECS Launch Types in the Amazon Elastic Container Service Developer Guide .

    :type platformVersion: string
    :param platformVersion: The platform version the task should run. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the LATEST platform version is used by default. For more information, see AWS Fargate Platform Versions in the Amazon Elastic Container Service Developer Guide .

    :type networkConfiguration: dict
    :param networkConfiguration: The network configuration for the task. This parameter is required for task definitions that use the awsvpc network mode to receive their own elastic network interface, and it is not supported for other network modes. For more information, see Task Networking in the Amazon Elastic Container Service Developer Guide .
            awsvpcConfiguration (dict) --The VPC subnets and security groups associated with a task.
            Note
            All specified subnets and security groups must be from the same VPC.
            subnets (list) -- [REQUIRED]The subnets associated with the task or service. There is a limit of 16 subnets able to be specified per AwsVpcConfiguration .
            Note
            All specified subnets must be from the same VPC.
            (string) --
            securityGroups (list) --The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of five security groups able to be specified per AwsVpcConfiguration .
            Note
            All specified security groups must be from the same VPC.
            (string) --
            assignPublicIp (string) --Whether the task's elastic network interface receives a public IP address. The default value is DISABLED .
            
            

    :type tags: list
    :param tags: The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
            (dict) --The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
            key (string) --One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.
            value (string) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).
            
            

    :type enableECSManagedTags: boolean
    :param enableECSManagedTags: Specifies whether to enable Amazon ECS managed tags for the task. For more information, see Tagging Your Amazon ECS Resources in the Amazon Elastic Container Service Developer Guide .

    :type propagateTags: string
    :param propagateTags: Specifies whether to propagate the tags from the task definition or the service to the task. If no value is specified, the tags are not propagated.

    :rtype: dict
    :return: {
        'tasks': [
            {
                'taskArn': 'string',
                'clusterArn': 'string',
                'taskDefinitionArn': 'string',
                'containerInstanceArn': 'string',
                'overrides': {
                    'containerOverrides': [
                        {
                            'name': 'string',
                            'command': [
                                'string',
                            ],
                            'environment': [
                                {
                                    'name': 'string',
                                    'value': 'string'
                                },
                            ],
                            'cpu': 123,
                            'memory': 123,
                            'memoryReservation': 123
                        },
                    ],
                    'taskRoleArn': 'string',
                    'executionRoleArn': 'string'
                },
                'lastStatus': 'string',
                'desiredStatus': 'string',
                'cpu': 'string',
                'memory': 'string',
                'containers': [
                    {
                        'containerArn': 'string',
                        'taskArn': 'string',
                        'name': 'string',
                        'lastStatus': 'string',
                        'exitCode': 123,
                        'reason': 'string',
                        'networkBindings': [
                            {
                                'bindIP': 'string',
                                'containerPort': 123,
                                'hostPort': 123,
                                'protocol': 'tcp'|'udp'
                            },
                        ],
                        'networkInterfaces': [
                            {
                                'attachmentId': 'string',
                                'privateIpv4Address': 'string',
                                'ipv6Address': 'string'
                            },
                        ],
                        'healthStatus': 'HEALTHY'|'UNHEALTHY'|'UNKNOWN'
                    },
                ],
                'startedBy': 'string',
                'version': 123,
                'stoppedReason': 'string',
                'stopCode': 'TaskFailedToStart'|'EssentialContainerExited'|'UserInitiated',
                'connectivity': 'CONNECTED'|'DISCONNECTED',
                'connectivityAt': datetime(2015, 1, 1),
                'pullStartedAt': datetime(2015, 1, 1),
                'pullStoppedAt': datetime(2015, 1, 1),
                'executionStoppedAt': datetime(2015, 1, 1),
                'createdAt': datetime(2015, 1, 1),
                'startedAt': datetime(2015, 1, 1),
                'stoppingAt': datetime(2015, 1, 1),
                'stoppedAt': datetime(2015, 1, 1),
                'group': 'string',
                'launchType': 'EC2'|'FARGATE',
                'platformVersion': 'string',
                'attachments': [
                    {
                        'id': 'string',
                        'type': 'string',
                        'status': 'string',
                        'details': [
                            {
                                'name': 'string',
                                'value': 'string'
                            },
                        ]
                    },
                ],
                'healthStatus': 'HEALTHY'|'UNHEALTHY'|'UNKNOWN',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ]
            },
        ],
        'failures': [
            {
                'arn': 'string',
                'reason': 'string'
            },
        ]
    }
    
    
    :returns: 
    cluster (string) -- The short name or full Amazon Resource Name (ARN) of the cluster on which to run your task. If you do not specify a cluster, the default cluster is assumed.
    taskDefinition (string) -- [REQUIRED]
    The family and revision (family:revision ) or full ARN of the task definition to run. If a revision is not specified, the latest ACTIVE revision is used.
    
    overrides (dict) -- A list of container overrides in JSON format that specify the name of a container in the specified task definition and the overrides it should receive. You can override the default command for a container (that is specified in the task definition or Docker image) with a command override. You can also override existing environment variables (that are specified in the task definition or Docker image) on a container or add new environment variables to it with an environment override.
    
    Note
    A total of 8192 characters are allowed for overrides. This limit includes the JSON formatting characters of the override structure.
    
    
    containerOverrides (list) --One or more container overrides sent to a task.
    
    (dict) --The overrides that should be sent to a container.
    
    name (string) --The name of the container that receives the override. This parameter is required if any override is specified.
    
    command (list) --The command to send to the container that overrides the default command from the Docker image or the task definition. You must also specify a container name.
    
    (string) --
    
    
    environment (list) --The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.
    
    (dict) --A key-value pair object.
    
    name (string) --The name of the key-value pair. For environment variables, this is the name of the environment variable.
    
    value (string) --The value of the key-value pair. For environment variables, this is the value of the environment variable.
    
    
    
    
    
    cpu (integer) --The number of cpu units reserved for the container, instead of the default value from the task definition. You must also specify a container name.
    
    memory (integer) --The hard limit (in MiB) of memory to present to the container, instead of the default value from the task definition. If your container attempts to exceed the memory specified here, the container is killed. You must also specify a container name.
    
    memoryReservation (integer) --The soft limit (in MiB) of memory to reserve for the container, instead of the default value from the task definition. You must also specify a container name.
    
    
    
    
    
    taskRoleArn (string) --The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role.
    
    executionRoleArn (string) --The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.
    
    
    
    count (integer) -- The number of instantiations of the specified task to place on your cluster. You can specify up to 10 tasks per call.
    startedBy (string) -- An optional tag specified when a task is started. For example, if you automatically trigger a task to run a batch process job, you could apply a unique identifier for that job to your task with the startedBy parameter. You can then identify which tasks belong to that job by filtering the results of a  ListTasks call with the startedBy value. Up to 36 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.
    If a task is started by an Amazon ECS service, then the startedBy parameter contains the deployment ID of the service that starts it.
    
    group (string) -- The name of the task group to associate with the task. The default value is the family name of the task definition (for example, family:my-family-name).
    placementConstraints (list) -- An array of placement constraint objects to use for the task. You can specify up to 10 constraints per task (including constraints in the task definition and those specified at runtime).
    
    (dict) --An object representing a constraint on task placement. For more information, see Task Placement Constraints in the Amazon Elastic Container Service Developer Guide .
    
    type (string) --The type of constraint. Use distinctInstance to ensure that each task in a particular group is running on a different container instance. Use memberOf to restrict the selection to a group of valid candidates. The value distinctInstance is not supported in task definitions.
    
    expression (string) --A cluster query language expression to apply to the constraint. You cannot specify an expression if the constraint type is distinctInstance . For more information, see Cluster Query Language in the Amazon Elastic Container Service Developer Guide .
    
    
    
    
    
    placementStrategy (list) -- The placement strategy objects to use for the task. You can specify a maximum of five strategy rules per task.
    
    (dict) --The task placement strategy for a task or service. For more information, see Task Placement Strategies in the Amazon Elastic Container Service Developer Guide .
    
    type (string) --The type of placement strategy. The random placement strategy randomly places tasks on available candidates. The spread placement strategy spreads placement across available candidates evenly based on the field parameter. The binpack strategy places tasks on available candidates that have the least available amount of the resource that is specified with the field parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task).
    
    field (string) --The field to apply the placement strategy against. For the spread placement strategy, valid values are instanceId (or host , which has the same effect), or any platform or custom attribute that is applied to a container instance, such as attribute:ecs.availability-zone . For the binpack placement strategy, valid values are cpu and memory . For the random placement strategy, this field is not used.
    
    
    
    
    
    launchType (string) -- The launch type on which to run your task. For more information, see Amazon ECS Launch Types in the Amazon Elastic Container Service Developer Guide .
    platformVersion (string) -- The platform version the task should run. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the LATEST platform version is used by default. For more information, see AWS Fargate Platform Versions in the Amazon Elastic Container Service Developer Guide .
    networkConfiguration (dict) -- The network configuration for the task. This parameter is required for task definitions that use the awsvpc network mode to receive their own elastic network interface, and it is not supported for other network modes. For more information, see Task Networking in the Amazon Elastic Container Service Developer Guide .
    
    awsvpcConfiguration (dict) --The VPC subnets and security groups associated with a task.
    
    Note
    All specified subnets and security groups must be from the same VPC.
    
    
    subnets (list) -- [REQUIRED]The subnets associated with the task or service. There is a limit of 16 subnets able to be specified per AwsVpcConfiguration .
    
    Note
    All specified subnets must be from the same VPC.
    
    
    (string) --
    
    
    securityGroups (list) --The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of five security groups able to be specified per AwsVpcConfiguration .
    
    Note
    All specified security groups must be from the same VPC.
    
    
    (string) --
    
    
    assignPublicIp (string) --Whether the task's elastic network interface receives a public IP address. The default value is DISABLED .
    
    
    
    
    
    tags (list) -- The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
    
    (dict) --The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
    
    key (string) --One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.
    
    value (string) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).
    
    
    
    
    
    enableECSManagedTags (boolean) -- Specifies whether to enable Amazon ECS managed tags for the task. For more information, see Tagging Your Amazon ECS Resources in the Amazon Elastic Container Service Developer Guide .
    propagateTags (string) -- Specifies whether to propagate the tags from the task definition or the service to the task. If no value is specified, the tags are not propagated.
    
    """
    pass

def start_task(cluster=None, taskDefinition=None, overrides=None, containerInstances=None, startedBy=None, group=None, networkConfiguration=None, tags=None, enableECSManagedTags=None, propagateTags=None):
    """
    Starts a new task from the specified task definition on the specified container instance or instances.
    Alternatively, you can use  RunTask to place tasks for you. For more information, see Scheduling Tasks in the Amazon Elastic Container Service Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.start_task(
        cluster='string',
        taskDefinition='string',
        overrides={
            'containerOverrides': [
                {
                    'name': 'string',
                    'command': [
                        'string',
                    ],
                    'environment': [
                        {
                            'name': 'string',
                            'value': 'string'
                        },
                    ],
                    'cpu': 123,
                    'memory': 123,
                    'memoryReservation': 123
                },
            ],
            'taskRoleArn': 'string',
            'executionRoleArn': 'string'
        },
        containerInstances=[
            'string',
        ],
        startedBy='string',
        group='string',
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': [
                    'string',
                ],
                'securityGroups': [
                    'string',
                ],
                'assignPublicIp': 'ENABLED'|'DISABLED'
            }
        },
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        enableECSManagedTags=True|False,
        propagateTags='TASK_DEFINITION'|'SERVICE'
    )
    
    
    :type cluster: string
    :param cluster: The short name or full Amazon Resource Name (ARN) of the cluster on which to start your task. If you do not specify a cluster, the default cluster is assumed.

    :type taskDefinition: string
    :param taskDefinition: [REQUIRED]
            The family and revision (family:revision ) or full ARN of the task definition to start. If a revision is not specified, the latest ACTIVE revision is used.
            

    :type overrides: dict
    :param overrides: A list of container overrides in JSON format that specify the name of a container in the specified task definition and the overrides it should receive. You can override the default command for a container (that is specified in the task definition or Docker image) with a command override. You can also override existing environment variables (that are specified in the task definition or Docker image) on a container or add new environment variables to it with an environment override.
            Note
            A total of 8192 characters are allowed for overrides. This limit includes the JSON formatting characters of the override structure.
            containerOverrides (list) --One or more container overrides sent to a task.
            (dict) --The overrides that should be sent to a container.
            name (string) --The name of the container that receives the override. This parameter is required if any override is specified.
            command (list) --The command to send to the container that overrides the default command from the Docker image or the task definition. You must also specify a container name.
            (string) --
            environment (list) --The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.
            (dict) --A key-value pair object.
            name (string) --The name of the key-value pair. For environment variables, this is the name of the environment variable.
            value (string) --The value of the key-value pair. For environment variables, this is the value of the environment variable.
            
            cpu (integer) --The number of cpu units reserved for the container, instead of the default value from the task definition. You must also specify a container name.
            memory (integer) --The hard limit (in MiB) of memory to present to the container, instead of the default value from the task definition. If your container attempts to exceed the memory specified here, the container is killed. You must also specify a container name.
            memoryReservation (integer) --The soft limit (in MiB) of memory to reserve for the container, instead of the default value from the task definition. You must also specify a container name.
            
            taskRoleArn (string) --The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role.
            executionRoleArn (string) --The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.
            

    :type containerInstances: list
    :param containerInstances: [REQUIRED]
            The container instance IDs or full ARN entries for the container instances on which you would like to place your task. You can specify up to 10 container instances.
            (string) --
            

    :type startedBy: string
    :param startedBy: An optional tag specified when a task is started. For example, if you automatically trigger a task to run a batch process job, you could apply a unique identifier for that job to your task with the startedBy parameter. You can then identify which tasks belong to that job by filtering the results of a ListTasks call with the startedBy value. Up to 36 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.
            If a task is started by an Amazon ECS service, then the startedBy parameter contains the deployment ID of the service that starts it.
            

    :type group: string
    :param group: The name of the task group to associate with the task. The default value is the family name of the task definition (for example, family:my-family-name).

    :type networkConfiguration: dict
    :param networkConfiguration: The VPC subnet and security group configuration for tasks that receive their own elastic network interface by using the awsvpc networking mode.
            awsvpcConfiguration (dict) --The VPC subnets and security groups associated with a task.
            Note
            All specified subnets and security groups must be from the same VPC.
            subnets (list) -- [REQUIRED]The subnets associated with the task or service. There is a limit of 16 subnets able to be specified per AwsVpcConfiguration .
            Note
            All specified subnets must be from the same VPC.
            (string) --
            securityGroups (list) --The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of five security groups able to be specified per AwsVpcConfiguration .
            Note
            All specified security groups must be from the same VPC.
            (string) --
            assignPublicIp (string) --Whether the task's elastic network interface receives a public IP address. The default value is DISABLED .
            
            

    :type tags: list
    :param tags: The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
            (dict) --The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
            key (string) --One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.
            value (string) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).
            
            

    :type enableECSManagedTags: boolean
    :param enableECSManagedTags: Specifies whether to enable Amazon ECS managed tags for the task. For more information, see Tagging Your Amazon ECS Resources in the Amazon Elastic Container Service Developer Guide .

    :type propagateTags: string
    :param propagateTags: Specifies whether to propagate the tags from the task definition or the service to the task. If no value is specified, the tags are not propagated.

    :rtype: dict
    :return: {
        'tasks': [
            {
                'taskArn': 'string',
                'clusterArn': 'string',
                'taskDefinitionArn': 'string',
                'containerInstanceArn': 'string',
                'overrides': {
                    'containerOverrides': [
                        {
                            'name': 'string',
                            'command': [
                                'string',
                            ],
                            'environment': [
                                {
                                    'name': 'string',
                                    'value': 'string'
                                },
                            ],
                            'cpu': 123,
                            'memory': 123,
                            'memoryReservation': 123
                        },
                    ],
                    'taskRoleArn': 'string',
                    'executionRoleArn': 'string'
                },
                'lastStatus': 'string',
                'desiredStatus': 'string',
                'cpu': 'string',
                'memory': 'string',
                'containers': [
                    {
                        'containerArn': 'string',
                        'taskArn': 'string',
                        'name': 'string',
                        'lastStatus': 'string',
                        'exitCode': 123,
                        'reason': 'string',
                        'networkBindings': [
                            {
                                'bindIP': 'string',
                                'containerPort': 123,
                                'hostPort': 123,
                                'protocol': 'tcp'|'udp'
                            },
                        ],
                        'networkInterfaces': [
                            {
                                'attachmentId': 'string',
                                'privateIpv4Address': 'string',
                                'ipv6Address': 'string'
                            },
                        ],
                        'healthStatus': 'HEALTHY'|'UNHEALTHY'|'UNKNOWN'
                    },
                ],
                'startedBy': 'string',
                'version': 123,
                'stoppedReason': 'string',
                'stopCode': 'TaskFailedToStart'|'EssentialContainerExited'|'UserInitiated',
                'connectivity': 'CONNECTED'|'DISCONNECTED',
                'connectivityAt': datetime(2015, 1, 1),
                'pullStartedAt': datetime(2015, 1, 1),
                'pullStoppedAt': datetime(2015, 1, 1),
                'executionStoppedAt': datetime(2015, 1, 1),
                'createdAt': datetime(2015, 1, 1),
                'startedAt': datetime(2015, 1, 1),
                'stoppingAt': datetime(2015, 1, 1),
                'stoppedAt': datetime(2015, 1, 1),
                'group': 'string',
                'launchType': 'EC2'|'FARGATE',
                'platformVersion': 'string',
                'attachments': [
                    {
                        'id': 'string',
                        'type': 'string',
                        'status': 'string',
                        'details': [
                            {
                                'name': 'string',
                                'value': 'string'
                            },
                        ]
                    },
                ],
                'healthStatus': 'HEALTHY'|'UNHEALTHY'|'UNKNOWN',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ]
            },
        ],
        'failures': [
            {
                'arn': 'string',
                'reason': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def stop_task(cluster=None, task=None, reason=None):
    """
    Stops a running task. Any tags associated with the task will be deleted.
    When  StopTask is called on a task, the equivalent of docker stop is issued to the containers running in the task. This results in a SIGTERM value and a default 30-second timeout, after which the SIGKILL value is sent and the containers are forcibly stopped. If the container handles the SIGTERM value gracefully and exits within 30 seconds from receiving it, no SIGKILL value is sent.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_task(
        cluster='string',
        task='string',
        reason='string'
    )
    
    
    :type cluster: string
    :param cluster: The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task to stop. If you do not specify a cluster, the default cluster is assumed.

    :type task: string
    :param task: [REQUIRED]
            The task ID or full ARN entry of the task to stop.
            

    :type reason: string
    :param reason: An optional message specified when a task is stopped. For example, if you are using a custom scheduler, you can use this parameter to specify the reason for stopping the task here, and the message appears in subsequent DescribeTasks API operations on this task. Up to 255 characters are allowed in this message.

    :rtype: dict
    :return: {
        'task': {
            'taskArn': 'string',
            'clusterArn': 'string',
            'taskDefinitionArn': 'string',
            'containerInstanceArn': 'string',
            'overrides': {
                'containerOverrides': [
                    {
                        'name': 'string',
                        'command': [
                            'string',
                        ],
                        'environment': [
                            {
                                'name': 'string',
                                'value': 'string'
                            },
                        ],
                        'cpu': 123,
                        'memory': 123,
                        'memoryReservation': 123
                    },
                ],
                'taskRoleArn': 'string',
                'executionRoleArn': 'string'
            },
            'lastStatus': 'string',
            'desiredStatus': 'string',
            'cpu': 'string',
            'memory': 'string',
            'containers': [
                {
                    'containerArn': 'string',
                    'taskArn': 'string',
                    'name': 'string',
                    'lastStatus': 'string',
                    'exitCode': 123,
                    'reason': 'string',
                    'networkBindings': [
                        {
                            'bindIP': 'string',
                            'containerPort': 123,
                            'hostPort': 123,
                            'protocol': 'tcp'|'udp'
                        },
                    ],
                    'networkInterfaces': [
                        {
                            'attachmentId': 'string',
                            'privateIpv4Address': 'string',
                            'ipv6Address': 'string'
                        },
                    ],
                    'healthStatus': 'HEALTHY'|'UNHEALTHY'|'UNKNOWN'
                },
            ],
            'startedBy': 'string',
            'version': 123,
            'stoppedReason': 'string',
            'stopCode': 'TaskFailedToStart'|'EssentialContainerExited'|'UserInitiated',
            'connectivity': 'CONNECTED'|'DISCONNECTED',
            'connectivityAt': datetime(2015, 1, 1),
            'pullStartedAt': datetime(2015, 1, 1),
            'pullStoppedAt': datetime(2015, 1, 1),
            'executionStoppedAt': datetime(2015, 1, 1),
            'createdAt': datetime(2015, 1, 1),
            'startedAt': datetime(2015, 1, 1),
            'stoppingAt': datetime(2015, 1, 1),
            'stoppedAt': datetime(2015, 1, 1),
            'group': 'string',
            'launchType': 'EC2'|'FARGATE',
            'platformVersion': 'string',
            'attachments': [
                {
                    'id': 'string',
                    'type': 'string',
                    'status': 'string',
                    'details': [
                        {
                            'name': 'string',
                            'value': 'string'
                        },
                    ]
                },
            ],
            'healthStatus': 'HEALTHY'|'UNHEALTHY'|'UNKNOWN',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def submit_container_state_change(cluster=None, task=None, containerName=None, status=None, exitCode=None, reason=None, networkBindings=None):
    """
    Sent to acknowledge that a container changed states.
    See also: AWS API Documentation
    
    
    :example: response = client.submit_container_state_change(
        cluster='string',
        task='string',
        containerName='string',
        status='string',
        exitCode=123,
        reason='string',
        networkBindings=[
            {
                'bindIP': 'string',
                'containerPort': 123,
                'hostPort': 123,
                'protocol': 'tcp'|'udp'
            },
        ]
    )
    
    
    :type cluster: string
    :param cluster: The short name or full ARN of the cluster that hosts the container.

    :type task: string
    :param task: The task ID or full Amazon Resource Name (ARN) of the task that hosts the container.

    :type containerName: string
    :param containerName: The name of the container.

    :type status: string
    :param status: The status of the state change request.

    :type exitCode: integer
    :param exitCode: The exit code returned for the state change request.

    :type reason: string
    :param reason: The reason for the state change request.

    :type networkBindings: list
    :param networkBindings: The network bindings of the container.
            (dict) --Details on the network bindings between a container and its host container instance. After a task reaches the RUNNING status, manual and automatic host and container port assignments are visible in the networkBindings section of DescribeTasks API responses.
            bindIP (string) --The IP address that the container is bound to on the container instance.
            containerPort (integer) --The port number on the container that is used with the network binding.
            hostPort (integer) --The port number on the host that is used with the network binding.
            protocol (string) --The protocol used for the network binding.
            
            

    :rtype: dict
    :return: {
        'acknowledgment': 'string'
    }
    
    
    """
    pass

def submit_task_state_change(cluster=None, task=None, status=None, reason=None, containers=None, attachments=None, pullStartedAt=None, pullStoppedAt=None, executionStoppedAt=None):
    """
    Sent to acknowledge that a task changed states.
    See also: AWS API Documentation
    
    
    :example: response = client.submit_task_state_change(
        cluster='string',
        task='string',
        status='string',
        reason='string',
        containers=[
            {
                'containerName': 'string',
                'exitCode': 123,
                'networkBindings': [
                    {
                        'bindIP': 'string',
                        'containerPort': 123,
                        'hostPort': 123,
                        'protocol': 'tcp'|'udp'
                    },
                ],
                'reason': 'string',
                'status': 'string'
            },
        ],
        attachments=[
            {
                'attachmentArn': 'string',
                'status': 'string'
            },
        ],
        pullStartedAt=datetime(2015, 1, 1),
        pullStoppedAt=datetime(2015, 1, 1),
        executionStoppedAt=datetime(2015, 1, 1)
    )
    
    
    :type cluster: string
    :param cluster: The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task.

    :type task: string
    :param task: The task ID or full ARN of the task in the state change request.

    :type status: string
    :param status: The status of the state change request.

    :type reason: string
    :param reason: The reason for the state change request.

    :type containers: list
    :param containers: Any containers associated with the state change request.
            (dict) --An object representing a change in state for a container.
            containerName (string) --The name of the container.
            exitCode (integer) --The exit code for the container, if the state change is a result of the container exiting.
            networkBindings (list) --Any network bindings associated with the container.
            (dict) --Details on the network bindings between a container and its host container instance. After a task reaches the RUNNING status, manual and automatic host and container port assignments are visible in the networkBindings section of DescribeTasks API responses.
            bindIP (string) --The IP address that the container is bound to on the container instance.
            containerPort (integer) --The port number on the container that is used with the network binding.
            hostPort (integer) --The port number on the host that is used with the network binding.
            protocol (string) --The protocol used for the network binding.
            
            reason (string) --The reason for the state change.
            status (string) --The status of the container.
            
            

    :type attachments: list
    :param attachments: Any attachments associated with the state change request.
            (dict) --An object representing a change in state for a task attachment.
            attachmentArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the attachment.
            status (string) -- [REQUIRED]The status of the attachment.
            
            

    :type pullStartedAt: datetime
    :param pullStartedAt: The Unix timestamp for when the container image pull began.

    :type pullStoppedAt: datetime
    :param pullStoppedAt: The Unix timestamp for when the container image pull completed.

    :type executionStoppedAt: datetime
    :param executionStoppedAt: The Unix timestamp for when the task execution stopped.

    :rtype: dict
    :return: {
        'acknowledgment': 'string'
    }
    
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Associates the specified tags to a resource with the specified resourceArn . If existing tags on a resource are not specified in the request parameters, they are not changed. When a resource is deleted, the tags associated with that resource are deleted as well.
    See also: AWS API Documentation
    
    
    :example: response = client.tag_resource(
        resourceArn='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource to which to add tags. Currently, the supported resources are Amazon ECS tasks, services, task definitions, clusters, and container instances.
            

    :type tags: list
    :param tags: [REQUIRED]
            The tags to add to the resource. A tag is an array of key-value pairs. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
            (dict) --The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
            key (string) --One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.
            value (string) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Deletes specified tags from a resource.
    See also: AWS API Documentation
    
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource from which to delete tags. Currently, the supported resources are Amazon ECS tasks, services, task definitions, clusters, and container instances.
            

    :type tagKeys: list
    :param tagKeys: [REQUIRED]
            The keys of the tags to be removed.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_container_agent(cluster=None, containerInstance=None):
    """
    Updates the Amazon ECS container agent on a specified container instance. Updating the Amazon ECS container agent does not interrupt running tasks or services on the container instance. The process for updating the agent differs depending on whether your container instance was launched with the Amazon ECS-optimized AMI or another operating system.
    See also: AWS API Documentation
    
    
    :example: response = client.update_container_agent(
        cluster='string',
        containerInstance='string'
    )
    
    
    :type cluster: string
    :param cluster: The short name or full Amazon Resource Name (ARN) of the cluster that your container instance is running on. If you do not specify a cluster, the default cluster is assumed.

    :type containerInstance: string
    :param containerInstance: [REQUIRED]
            The container instance ID or full ARN entries for the container instance on which you would like to update the Amazon ECS container agent.
            

    :rtype: dict
    :return: {
        'containerInstance': {
            'containerInstanceArn': 'string',
            'ec2InstanceId': 'string',
            'version': 123,
            'versionInfo': {
                'agentVersion': 'string',
                'agentHash': 'string',
                'dockerVersion': 'string'
            },
            'remainingResources': [
                {
                    'name': 'string',
                    'type': 'string',
                    'doubleValue': 123.0,
                    'longValue': 123,
                    'integerValue': 123,
                    'stringSetValue': [
                        'string',
                    ]
                },
            ],
            'registeredResources': [
                {
                    'name': 'string',
                    'type': 'string',
                    'doubleValue': 123.0,
                    'longValue': 123,
                    'integerValue': 123,
                    'stringSetValue': [
                        'string',
                    ]
                },
            ],
            'status': 'string',
            'agentConnected': True|False,
            'runningTasksCount': 123,
            'pendingTasksCount': 123,
            'agentUpdateStatus': 'PENDING'|'STAGING'|'STAGED'|'UPDATING'|'UPDATED'|'FAILED',
            'attributes': [
                {
                    'name': 'string',
                    'value': 'string',
                    'targetType': 'container-instance',
                    'targetId': 'string'
                },
            ],
            'registeredAt': datetime(2015, 1, 1),
            'attachments': [
                {
                    'id': 'string',
                    'type': 'string',
                    'status': 'string',
                    'details': [
                        {
                            'name': 'string',
                            'value': 'string'
                        },
                    ]
                },
            ],
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_container_instances_state(cluster=None, containerInstances=None, status=None):
    """
    Modifies the status of an Amazon ECS container instance.
    You can change the status of a container instance to DRAINING to manually remove an instance from a cluster, for example to perform system updates, update the Docker daemon, or scale down the cluster size.
    When you set a container instance to DRAINING , Amazon ECS prevents new tasks from being scheduled for placement on the container instance and replacement service tasks are started on other container instances in the cluster if the resources are available. Service tasks on the container instance that are in the PENDING state are stopped immediately.
    Service tasks on the container instance that are in the RUNNING state are stopped and replaced according to the service's deployment configuration parameters, minimumHealthyPercent and maximumPercent . You can change the deployment configuration of your service using  UpdateService .
    Any PENDING or RUNNING tasks that do not belong to a service are not affected. You must wait for them to finish or stop them manually.
    A container instance has completed draining when it has no more RUNNING tasks. You can verify this using  ListTasks .
    When you set a container instance to ACTIVE , the Amazon ECS scheduler can begin scheduling tasks on the instance again.
    See also: AWS API Documentation
    
    
    :example: response = client.update_container_instances_state(
        cluster='string',
        containerInstances=[
            'string',
        ],
        status='ACTIVE'|'DRAINING'
    )
    
    
    :type cluster: string
    :param cluster: The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instance to update. If you do not specify a cluster, the default cluster is assumed.

    :type containerInstances: list
    :param containerInstances: [REQUIRED]
            A list of container instance IDs or full ARN entries.
            (string) --
            

    :type status: string
    :param status: [REQUIRED]
            The container instance state with which to update the container instance.
            

    :rtype: dict
    :return: {
        'containerInstances': [
            {
                'containerInstanceArn': 'string',
                'ec2InstanceId': 'string',
                'version': 123,
                'versionInfo': {
                    'agentVersion': 'string',
                    'agentHash': 'string',
                    'dockerVersion': 'string'
                },
                'remainingResources': [
                    {
                        'name': 'string',
                        'type': 'string',
                        'doubleValue': 123.0,
                        'longValue': 123,
                        'integerValue': 123,
                        'stringSetValue': [
                            'string',
                        ]
                    },
                ],
                'registeredResources': [
                    {
                        'name': 'string',
                        'type': 'string',
                        'doubleValue': 123.0,
                        'longValue': 123,
                        'integerValue': 123,
                        'stringSetValue': [
                            'string',
                        ]
                    },
                ],
                'status': 'string',
                'agentConnected': True|False,
                'runningTasksCount': 123,
                'pendingTasksCount': 123,
                'agentUpdateStatus': 'PENDING'|'STAGING'|'STAGED'|'UPDATING'|'UPDATED'|'FAILED',
                'attributes': [
                    {
                        'name': 'string',
                        'value': 'string',
                        'targetType': 'container-instance',
                        'targetId': 'string'
                    },
                ],
                'registeredAt': datetime(2015, 1, 1),
                'attachments': [
                    {
                        'id': 'string',
                        'type': 'string',
                        'status': 'string',
                        'details': [
                            {
                                'name': 'string',
                                'value': 'string'
                            },
                        ]
                    },
                ],
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ]
            },
        ],
        'failures': [
            {
                'arn': 'string',
                'reason': 'string'
            },
        ]
    }
    
    
    :returns: 
    cluster (string) -- The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instance to update. If you do not specify a cluster, the default cluster is assumed.
    containerInstances (list) -- [REQUIRED]
    A list of container instance IDs or full ARN entries.
    
    (string) --
    
    
    status (string) -- [REQUIRED]
    The container instance state with which to update the container instance.
    
    
    """
    pass

def update_service(cluster=None, service=None, desiredCount=None, taskDefinition=None, deploymentConfiguration=None, networkConfiguration=None, platformVersion=None, forceNewDeployment=None, healthCheckGracePeriodSeconds=None):
    """
    Modifies the parameters of a service.
    For services using the rolling update (ECS ) deployment controller, the desired count, deployment configuration, network configuration, or task definition used can be updated.
    For services using the blue/green (CODE_DEPLOY ) deployment controller, only the desired count, deployment configuration, and health check grace period can be updated using this API. If the network configuration, platform version, or task definition need to be updated, a new AWS CodeDeploy deployment should be created. For more information, see CreateDeployment in the AWS CodeDeploy API Reference .
    You can add to or subtract from the number of instantiations of a task definition in a service by specifying the cluster that the service is running in and a new desiredCount parameter.
    If you have updated the Docker image of your application, you can create a new task definition with that image and deploy it to your service. The service scheduler uses the minimum healthy percent and maximum percent parameters (in the service's deployment configuration) to determine the deployment strategy.
    You can also update the deployment configuration of a service. When a deployment is triggered by updating the task definition of a service, the service scheduler uses the deployment configuration parameters, minimumHealthyPercent and maximumPercent , to determine the deployment strategy.
    When  UpdateService stops a task during a deployment, the equivalent of docker stop is issued to the containers running in the task. This results in a SIGTERM and a 30-second timeout, after which SIGKILL is sent and the containers are forcibly stopped. If the container handles the SIGTERM gracefully and exits within 30 seconds from receiving it, no SIGKILL is sent.
    When the service scheduler launches new tasks, it determines task placement in your cluster with the following logic:
    When the service scheduler stops running tasks, it attempts to maintain balance across the Availability Zones in your cluster using the following logic:
    See also: AWS API Documentation
    
    Examples
    This example updates the my-http-service service to use the amazon-ecs-sample task definition.
    Expected Output:
    This example updates the desired count of the my-http-service service to 10.
    Expected Output:
    
    :example: response = client.update_service(
        cluster='string',
        service='string',
        desiredCount=123,
        taskDefinition='string',
        deploymentConfiguration={
            'maximumPercent': 123,
            'minimumHealthyPercent': 123
        },
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': [
                    'string',
                ],
                'securityGroups': [
                    'string',
                ],
                'assignPublicIp': 'ENABLED'|'DISABLED'
            }
        },
        platformVersion='string',
        forceNewDeployment=True|False,
        healthCheckGracePeriodSeconds=123
    )
    
    
    :type cluster: string
    :param cluster: The short name or full Amazon Resource Name (ARN) of the cluster that your service is running on. If you do not specify a cluster, the default cluster is assumed.

    :type service: string
    :param service: [REQUIRED]
            The name of the service to update.
            

    :type desiredCount: integer
    :param desiredCount: The number of instantiations of the task to place and keep running in your service.

    :type taskDefinition: string
    :param taskDefinition: The family and revision (family:revision ) or full ARN of the task definition to run in your service. If a revision is not specified, the latest ACTIVE revision is used. If you modify the task definition with UpdateService , Amazon ECS spawns a task with the new version of the task definition and then stops an old task after the new version is running.

    :type deploymentConfiguration: dict
    :param deploymentConfiguration: Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.
            maximumPercent (integer) --If a service is using the rolling update (ECS ) deployment type, the maximum percent parameter represents an upper limit on the number of tasks in a service that are allowed in the RUNNING or PENDING state during a deployment, as a percentage of the desired number of tasks (rounded down to the nearest integer), and while any container instances are in the DRAINING state if the service contains tasks using the EC2 launch type. This parameter enables you to define the deployment batch size. For example, if your service has a desired number of four tasks and a maximum percent value of 200%, the scheduler may start four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available). The default value for maximum percent is 200%.
            If a service is using the blue/green (CODE_DEPLOY ) deployment type and tasks that use the EC2 launch type, the maximum percent value is set to the default value and is used to define the upper limit on the number of the tasks in the service that remain in the RUNNING state while the container instances are in the DRAINING state. If the tasks in the service use the Fargate launch type, the maximum percent value is not used, although it is returned when describing your service.
            minimumHealthyPercent (integer) --If a service is using the rolling update (ECS ) deployment type, the minimum healthy percent represents a lower limit on the number of tasks in a service that must remain in the RUNNING state during a deployment, as a percentage of the desired number of tasks (rounded up to the nearest integer), and while any container instances are in the DRAINING state if the service contains tasks using the EC2 launch type. This parameter enables you to deploy without using additional cluster capacity. For example, if your service has a desired number of four tasks and a minimum healthy percent of 50%, the scheduler may stop two existing tasks to free up cluster capacity before starting two new tasks. Tasks for services that do not use a load balancer are considered healthy if they are in the RUNNING state; tasks for services that do use a load balancer are considered healthy if they are in the RUNNING state and they are reported as healthy by the load balancer. The default value for minimum healthy percent is 100%.
            If a service is using the blue/green (CODE_DEPLOY ) deployment type and tasks that use the EC2 launch type, the minimum healthy percent value is set to the default value and is used to define the lower limit on the number of the tasks in the service that remain in the RUNNING state while the container instances are in the DRAINING state. If the tasks in the service use the Fargate launch type, the minimum healthy percent value is not used, although it is returned when describing your service.
            

    :type networkConfiguration: dict
    :param networkConfiguration: The network configuration for the service. This parameter is required for task definitions that use the awsvpc network mode to receive their own elastic network interface, and it is not supported for other network modes. For more information, see Task Networking in the Amazon Elastic Container Service Developer Guide .
            Note
            Updating a service to add a subnet to a list of existing subnets does not trigger a service deployment. For example, if your network configuration change is to keep the existing subnets and simply add another subnet to the network configuration, this does not trigger a new service deployment.
            awsvpcConfiguration (dict) --The VPC subnets and security groups associated with a task.
            Note
            All specified subnets and security groups must be from the same VPC.
            subnets (list) -- [REQUIRED]The subnets associated with the task or service. There is a limit of 16 subnets able to be specified per AwsVpcConfiguration .
            Note
            All specified subnets must be from the same VPC.
            (string) --
            securityGroups (list) --The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of five security groups able to be specified per AwsVpcConfiguration .
            Note
            All specified security groups must be from the same VPC.
            (string) --
            assignPublicIp (string) --Whether the task's elastic network interface receives a public IP address. The default value is DISABLED .
            
            

    :type platformVersion: string
    :param platformVersion: The platform version on which your tasks in the service are running. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the LATEST platform version is used by default. For more information, see AWS Fargate Platform Versions in the Amazon Elastic Container Service Developer Guide .

    :type forceNewDeployment: boolean
    :param forceNewDeployment: Whether to force a new deployment of the service. Deployments are not forced by default. You can use this option to trigger a new deployment with no service definition changes. For example, you can update a service's tasks to use a newer Docker image with the same image/tag combination (my_image:latest ) or to roll Fargate tasks onto a newer platform version.

    :type healthCheckGracePeriodSeconds: integer
    :param healthCheckGracePeriodSeconds: The period of time, in seconds, that the Amazon ECS service scheduler should ignore unhealthy Elastic Load Balancing target health checks after a task has first started. This is only valid if your service is configured to use a load balancer. If your service's tasks take a while to start and respond to Elastic Load Balancing health checks, you can specify a health check grace period of up to 1,800 seconds. During that time, the ECS service scheduler ignores the Elastic Load Balancing health check status. This grace period can prevent the ECS service scheduler from marking tasks as unhealthy and stopping them before they have time to come up.

    :rtype: dict
    :return: {
        'service': {
            'serviceArn': 'string',
            'serviceName': 'string',
            'clusterArn': 'string',
            'loadBalancers': [
                {
                    'targetGroupArn': 'string',
                    'loadBalancerName': 'string',
                    'containerName': 'string',
                    'containerPort': 123
                },
            ],
            'serviceRegistries': [
                {
                    'registryArn': 'string',
                    'port': 123,
                    'containerName': 'string',
                    'containerPort': 123
                },
            ],
            'status': 'string',
            'desiredCount': 123,
            'runningCount': 123,
            'pendingCount': 123,
            'launchType': 'EC2'|'FARGATE',
            'platformVersion': 'string',
            'taskDefinition': 'string',
            'deploymentConfiguration': {
                'maximumPercent': 123,
                'minimumHealthyPercent': 123
            },
            'taskSets': [
                {
                    'id': 'string',
                    'taskSetArn': 'string',
                    'startedBy': 'string',
                    'externalId': 'string',
                    'status': 'string',
                    'taskDefinition': 'string',
                    'computedDesiredCount': 123,
                    'pendingCount': 123,
                    'runningCount': 123,
                    'createdAt': datetime(2015, 1, 1),
                    'updatedAt': datetime(2015, 1, 1),
                    'launchType': 'EC2'|'FARGATE',
                    'platformVersion': 'string',
                    'networkConfiguration': {
                        'awsvpcConfiguration': {
                            'subnets': [
                                'string',
                            ],
                            'securityGroups': [
                                'string',
                            ],
                            'assignPublicIp': 'ENABLED'|'DISABLED'
                        }
                    },
                    'loadBalancers': [
                        {
                            'targetGroupArn': 'string',
                            'loadBalancerName': 'string',
                            'containerName': 'string',
                            'containerPort': 123
                        },
                    ],
                    'scale': {
                        'value': 123.0,
                        'unit': 'PERCENT'
                    },
                    'stabilityStatus': 'STEADY_STATE'|'STABILIZING',
                    'stabilityStatusAt': datetime(2015, 1, 1)
                },
            ],
            'deployments': [
                {
                    'id': 'string',
                    'status': 'string',
                    'taskDefinition': 'string',
                    'desiredCount': 123,
                    'pendingCount': 123,
                    'runningCount': 123,
                    'createdAt': datetime(2015, 1, 1),
                    'updatedAt': datetime(2015, 1, 1),
                    'launchType': 'EC2'|'FARGATE',
                    'platformVersion': 'string',
                    'networkConfiguration': {
                        'awsvpcConfiguration': {
                            'subnets': [
                                'string',
                            ],
                            'securityGroups': [
                                'string',
                            ],
                            'assignPublicIp': 'ENABLED'|'DISABLED'
                        }
                    }
                },
            ],
            'roleArn': 'string',
            'events': [
                {
                    'id': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'message': 'string'
                },
            ],
            'createdAt': datetime(2015, 1, 1),
            'placementConstraints': [
                {
                    'type': 'distinctInstance'|'memberOf',
                    'expression': 'string'
                },
            ],
            'placementStrategy': [
                {
                    'type': 'random'|'spread'|'binpack',
                    'field': 'string'
                },
            ],
            'networkConfiguration': {
                'awsvpcConfiguration': {
                    'subnets': [
                        'string',
                    ],
                    'securityGroups': [
                        'string',
                    ],
                    'assignPublicIp': 'ENABLED'|'DISABLED'
                }
            },
            'healthCheckGracePeriodSeconds': 123,
            'schedulingStrategy': 'REPLICA'|'DAEMON',
            'deploymentController': {
                'type': 'ECS'|'CODE_DEPLOY'
            },
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'createdBy': 'string',
            'enableECSManagedTags': True|False,
            'propagateTags': 'TASK_DEFINITION'|'SERVICE'
        }
    }
    
    
    :returns: 
    Determine which of the container instances in your cluster can support your service's task definition (for example, they have the required CPU, memory, ports, and container instance attributes).
    By default, the service scheduler attempts to balance tasks across Availability Zones in this manner (although you can choose a different placement strategy):
    Sort the valid container instances by the fewest number of running tasks for this service in the same Availability Zone as the instance. For example, if zone A has one running service task and zones B and C each have zero, valid container instances in either zone B or C are considered optimal for placement.
    Place the new service task on a valid container instance in an optimal Availability Zone (based on the previous steps), favoring container instances with the fewest number of running tasks for this service.
    
    
    
    """
    pass

