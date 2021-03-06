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

def allocate_static_ip(staticIpName=None):
    """
    Allocates a static IP address.
    See also: AWS API Documentation
    
    
    :example: response = client.allocate_static_ip(
        staticIpName='string'
    )
    
    
    :type staticIpName: string
    :param staticIpName: [REQUIRED]
            The name of the static IP address.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def attach_disk(diskName=None, instanceName=None, diskPath=None):
    """
    Attaches a block storage disk to a running or stopped Lightsail instance and exposes it to the instance with the specified disk name.
    The attach disk operation supports tag-based access control via resource tags applied to the resource identified by diskName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.attach_disk(
        diskName='string',
        instanceName='string',
        diskPath='string'
    )
    
    
    :type diskName: string
    :param diskName: [REQUIRED]
            The unique Lightsail disk name (e.g., my-disk ).
            

    :type instanceName: string
    :param instanceName: [REQUIRED]
            The name of the Lightsail instance where you want to utilize the storage disk.
            

    :type diskPath: string
    :param diskPath: [REQUIRED]
            The disk path to expose to the instance (e.g., /dev/xvdf ).
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def attach_instances_to_load_balancer(loadBalancerName=None, instanceNames=None):
    """
    Attaches one or more Lightsail instances to a load balancer.
    After some time, the instances are attached to the load balancer and the health check status is available.
    The attach instances to load balancer operation supports tag-based access control via resource tags applied to the resource identified by loadBalancerName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.attach_instances_to_load_balancer(
        loadBalancerName='string',
        instanceNames=[
            'string',
        ]
    )
    
    
    :type loadBalancerName: string
    :param loadBalancerName: [REQUIRED]
            The name of the load balancer.
            

    :type instanceNames: list
    :param instanceNames: [REQUIRED]
            An array of strings representing the instance name(s) you want to attach to your load balancer.
            An instance must be running before you can attach it to your load balancer.
            There are no additional limits on the number of instances you can attach to your load balancer, aside from the limit of Lightsail instances you can create in your account (20).
            (string) --
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def attach_load_balancer_tls_certificate(loadBalancerName=None, certificateName=None):
    """
    Attaches a Transport Layer Security (TLS) certificate to your load balancer. TLS is just an updated, more secure version of Secure Socket Layer (SSL).
    Once you create and validate your certificate, you can attach it to your load balancer. You can also use this API to rotate the certificates on your account. Use the AttachLoadBalancerTlsCertificate operation with the non-attached certificate, and it will replace the existing one and become the attached certificate.
    The attach load balancer tls certificate operation supports tag-based access control via resource tags applied to the resource identified by loadBalancerName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.attach_load_balancer_tls_certificate(
        loadBalancerName='string',
        certificateName='string'
    )
    
    
    :type loadBalancerName: string
    :param loadBalancerName: [REQUIRED]
            The name of the load balancer to which you want to associate the SSL/TLS certificate.
            

    :type certificateName: string
    :param certificateName: [REQUIRED]
            The name of your SSL/TLS certificate.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def attach_static_ip(staticIpName=None, instanceName=None):
    """
    Attaches a static IP address to a specific Amazon Lightsail instance.
    See also: AWS API Documentation
    
    
    :example: response = client.attach_static_ip(
        staticIpName='string',
        instanceName='string'
    )
    
    
    :type staticIpName: string
    :param staticIpName: [REQUIRED]
            The name of the static IP.
            

    :type instanceName: string
    :param instanceName: [REQUIRED]
            The instance name to which you want to attach the static IP address.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
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

def close_instance_public_ports(portInfo=None, instanceName=None):
    """
    Closes the public ports on a specific Amazon Lightsail instance.
    The close instance public ports operation supports tag-based access control via resource tags applied to the resource identified by instanceName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.close_instance_public_ports(
        portInfo={
            'fromPort': 123,
            'toPort': 123,
            'protocol': 'tcp'|'all'|'udp'
        },
        instanceName='string'
    )
    
    
    :type portInfo: dict
    :param portInfo: [REQUIRED]
            Information about the public port you are trying to close.
            fromPort (integer) --The first port in the range.
            toPort (integer) --The last port in the range.
            protocol (string) --The protocol.
            

    :type instanceName: string
    :param instanceName: [REQUIRED]
            The name of the instance on which you're attempting to close the public ports.
            

    :rtype: dict
    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def copy_snapshot(sourceSnapshotName=None, targetSnapshotName=None, sourceRegion=None):
    """
    Copies an instance or disk snapshot from one AWS Region to another in Amazon Lightsail.
    See also: AWS API Documentation
    
    
    :example: response = client.copy_snapshot(
        sourceSnapshotName='string',
        targetSnapshotName='string',
        sourceRegion='us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
    )
    
    
    :type sourceSnapshotName: string
    :param sourceSnapshotName: [REQUIRED]
            The name of the source instance or disk snapshot to be copied.
            

    :type targetSnapshotName: string
    :param targetSnapshotName: [REQUIRED]
            The name of the new instance or disk snapshot to be created as a copy.
            

    :type sourceRegion: string
    :param sourceRegion: [REQUIRED]
            The AWS Region where the source snapshot is located.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def create_cloud_formation_stack(instances=None):
    """
    Creates an AWS CloudFormation stack, which creates a new Amazon EC2 instance from an exported Amazon Lightsail snapshot. This operation results in a CloudFormation stack record that can be used to track the AWS CloudFormation stack created. Use the get cloud formation stack records operation to get a list of the CloudFormation stacks created.
    See also: AWS API Documentation
    
    
    :example: response = client.create_cloud_formation_stack(
        instances=[
            {
                'sourceName': 'string',
                'instanceType': 'string',
                'portInfoSource': 'DEFAULT'|'INSTANCE'|'NONE',
                'userData': 'string',
                'availabilityZone': 'string'
            },
        ]
    )
    
    
    :type instances: list
    :param instances: [REQUIRED]
            An array of parameters that will be used to create the new Amazon EC2 instance. You can only pass one instance entry at a time in this array. You will get an invalid parameter error if you pass more than one instance entry in this array.
            (dict) --Describes the Amazon Elastic Compute Cloud instance and related resources to be created using the create cloud formation stack operation.
            sourceName (string) -- [REQUIRED]The name of the export snapshot record, which contains the exported Lightsail instance snapshot that will be used as the source of the new Amazon EC2 instance.
            Use the get export snapshot records operation to get a list of export snapshot records that you can use to create a CloudFormation stack.
            instanceType (string) -- [REQUIRED]The instance type (e.g., t2.micro ) to use for the new Amazon EC2 instance.
            portInfoSource (string) -- [REQUIRED]The port configuration to use for the new Amazon EC2 instance.
            The following configuration options are available:
            DEFAULT   Use the default firewall settings from the image.
            INSTANCE   Use the firewall settings from the source Lightsail instance.
            NONE   Default to Amazon EC2.
            userData (string) --A launch script you can create that configures a server with additional user data. For example, you might want to run apt-get -y update .
            Note
            Depending on the machine image you choose, the command to get software on your instance varies. Amazon Linux and CentOS use yum , Debian and Ubuntu use apt-get , and FreeBSD uses pkg .
            availabilityZone (string) -- [REQUIRED]The Availability Zone for the new Amazon EC2 instance.
            
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def create_disk(diskName=None, availabilityZone=None, sizeInGb=None, tags=None):
    """
    Creates a block storage disk that can be attached to a Lightsail instance in the same Availability Zone (e.g., us-east-2a ). The disk is created in the regional endpoint that you send the HTTP request to. For more information, see Regions and Availability Zones in Lightsail .
    The create disk operation supports tag-based access control via request tags. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_disk(
        diskName='string',
        availabilityZone='string',
        sizeInGb=123,
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type diskName: string
    :param diskName: [REQUIRED]
            The unique Lightsail disk name (e.g., my-disk ).
            

    :type availabilityZone: string
    :param availabilityZone: [REQUIRED]
            The Availability Zone where you want to create the disk (e.g., us-east-2a ). Choose the same Availability Zone as the Lightsail instance where you want to create the disk.
            Use the GetRegions operation to list the Availability Zones where Lightsail is currently available.
            

    :type sizeInGb: integer
    :param sizeInGb: [REQUIRED]
            The size of the disk in GB (e.g., 32 ).
            

    :type tags: list
    :param tags: The tag keys and optional values to add to the resource during create.
            To tag a resource after it has been created, see the tag resource operation.
            (dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
            For more information about tags in Lightsail, see the Lightsail Dev Guide .
            key (string) --The key of the tag.
            Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            value (string) --The value of the tag.
            Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def create_disk_from_snapshot(diskName=None, diskSnapshotName=None, availabilityZone=None, sizeInGb=None, tags=None):
    """
    Creates a block storage disk from a disk snapshot that can be attached to a Lightsail instance in the same Availability Zone (e.g., us-east-2a ). The disk is created in the regional endpoint that you send the HTTP request to. For more information, see Regions and Availability Zones in Lightsail .
    The create disk from snapshot operation supports tag-based access control via request tags and resource tags applied to the resource identified by diskSnapshotName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_disk_from_snapshot(
        diskName='string',
        diskSnapshotName='string',
        availabilityZone='string',
        sizeInGb=123,
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type diskName: string
    :param diskName: [REQUIRED]
            The unique Lightsail disk name (e.g., my-disk ).
            

    :type diskSnapshotName: string
    :param diskSnapshotName: [REQUIRED]
            The name of the disk snapshot (e.g., my-snapshot ) from which to create the new storage disk.
            

    :type availabilityZone: string
    :param availabilityZone: [REQUIRED]
            The Availability Zone where you want to create the disk (e.g., us-east-2a ). Choose the same Availability Zone as the Lightsail instance where you want to create the disk.
            Use the GetRegions operation to list the Availability Zones where Lightsail is currently available.
            

    :type sizeInGb: integer
    :param sizeInGb: [REQUIRED]
            The size of the disk in GB (e.g., 32 ).
            

    :type tags: list
    :param tags: The tag keys and optional values to add to the resource during create.
            To tag a resource after it has been created, see the tag resource operation.
            (dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
            For more information about tags in Lightsail, see the Lightsail Dev Guide .
            key (string) --The key of the tag.
            Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            value (string) --The value of the tag.
            Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def create_disk_snapshot(diskName=None, diskSnapshotName=None, tags=None):
    """
    Creates a snapshot of a block storage disk. You can use snapshots for backups, to make copies of disks, and to save data before shutting down a Lightsail instance.
    You can take a snapshot of an attached disk that is in use; however, snapshots only capture data that has been written to your disk at the time the snapshot command is issued. This may exclude any data that has been cached by any applications or the operating system. If you can pause any file systems on the disk long enough to take a snapshot, your snapshot should be complete. Nevertheless, if you cannot pause all file writes to the disk, you should unmount the disk from within the Lightsail instance, issue the create disk snapshot command, and then remount the disk to ensure a consistent and complete snapshot. You may remount and use your disk while the snapshot status is pending.
    The create disk snapshot operation supports tag-based access control via request tags. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_disk_snapshot(
        diskName='string',
        diskSnapshotName='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type diskName: string
    :param diskName: [REQUIRED]
            The unique name of the source disk (e.g., my-source-disk ).
            

    :type diskSnapshotName: string
    :param diskSnapshotName: [REQUIRED]
            The name of the destination disk snapshot (e.g., my-disk-snapshot ) based on the source disk.
            

    :type tags: list
    :param tags: The tag keys and optional values to add to the resource during create.
            To tag a resource after it has been created, see the tag resource operation.
            (dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
            For more information about tags in Lightsail, see the Lightsail Dev Guide .
            key (string) --The key of the tag.
            Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            value (string) --The value of the tag.
            Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def create_domain(domainName=None, tags=None):
    """
    Creates a domain resource for the specified domain (e.g., example.com).
    The create domain operation supports tag-based access control via request tags. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_domain(
        domainName='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]
            The domain name to manage (e.g., example.com ).
            Note
            You cannot register a new domain name using Lightsail. You must register a domain name using Amazon Route 53 or another domain name registrar. If you have already registered your domain, you can enter its name in this parameter to manage the DNS records for that domain.
            

    :type tags: list
    :param tags: The tag keys and optional values to add to the resource during create.
            To tag a resource after it has been created, see the tag resource operation.
            (dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
            For more information about tags in Lightsail, see the Lightsail Dev Guide .
            key (string) --The key of the tag.
            Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            value (string) --The value of the tag.
            Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            
            

    :rtype: dict
    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def create_domain_entry(domainName=None, domainEntry=None):
    """
    Creates one of the following entry records associated with the domain: A record, CNAME record, TXT record, or MX record.
    The create domain entry operation supports tag-based access control via resource tags applied to the resource identified by domainName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_domain_entry(
        domainName='string',
        domainEntry={
            'id': 'string',
            'name': 'string',
            'target': 'string',
            'isAlias': True|False,
            'type': 'string',
            'options': {
                'string': 'string'
            }
        }
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]
            The domain name (e.g., example.com ) for which you want to create the domain entry.
            

    :type domainEntry: dict
    :param domainEntry: [REQUIRED]
            An array of key-value pairs containing information about the domain entry request.
            id (string) --The ID of the domain recordset entry.
            name (string) --The name of the domain.
            target (string) --The target AWS name server (e.g., ns-111.awsdns-22.com. ).
            For Lightsail load balancers, the value looks like ab1234c56789c6b86aba6fb203d443bc-123456789.us-east-2.elb.amazonaws.com . Be sure to also set isAlias to true when setting up an A record for a load balancer.
            isAlias (boolean) --When true , specifies whether the domain entry is an alias used by the Lightsail load balancer. You can include an alias (A type) record in your request, which points to a load balancer DNS name and routes traffic to your load balancer
            type (string) --The type of domain entry (e.g., SOA or NS ).
            options (dict) --(Deprecated) The options for the domain entry.
            Note
            In releases prior to November 29, 2017, this parameter was not included in the API response. It is now deprecated.
            (string) --
            (string) --
            
            

    :rtype: dict
    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def create_instance_snapshot(instanceSnapshotName=None, instanceName=None, tags=None):
    """
    Creates a snapshot of a specific virtual private server, or instance . You can use a snapshot to create a new instance that is based on that snapshot.
    The create instance snapshot operation supports tag-based access control via request tags. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_instance_snapshot(
        instanceSnapshotName='string',
        instanceName='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type instanceSnapshotName: string
    :param instanceSnapshotName: [REQUIRED]
            The name for your new snapshot.
            

    :type instanceName: string
    :param instanceName: [REQUIRED]
            The Lightsail instance on which to base your snapshot.
            

    :type tags: list
    :param tags: The tag keys and optional values to add to the resource during create.
            To tag a resource after it has been created, see the tag resource operation.
            (dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
            For more information about tags in Lightsail, see the Lightsail Dev Guide .
            key (string) --The key of the tag.
            Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            value (string) --The value of the tag.
            Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def create_instances(instanceNames=None, availabilityZone=None, customImageName=None, blueprintId=None, bundleId=None, userData=None, keyPairName=None, tags=None):
    """
    Creates one or more Amazon Lightsail virtual private servers, or instances . Create instances using active blueprints. Inactive blueprints are listed to support customers with existing instances but are not necessarily available for launch of new instances. Blueprints are marked inactive when they become outdated due to operating system updates or new application releases. Use the get blueprints operation to return a list of available blueprints.
    The create instances operation supports tag-based access control via request tags. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_instances(
        instanceNames=[
            'string',
        ],
        availabilityZone='string',
        customImageName='string',
        blueprintId='string',
        bundleId='string',
        userData='string',
        keyPairName='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type instanceNames: list
    :param instanceNames: [REQUIRED]
            The names to use for your new Lightsail instances. Separate multiple values using quotation marks and commas, for example: ['MyFirstInstance','MySecondInstance']
            (string) --
            

    :type availabilityZone: string
    :param availabilityZone: [REQUIRED]
            The Availability Zone in which to create your instance. Use the following format: us-east-2a (case sensitive). You can get a list of Availability Zones by using the get regions operation. Be sure to add the include Availability Zones parameter to your request.
            

    :type customImageName: string
    :param customImageName: (Deprecated) The name for your custom image.
            Note
            In releases prior to June 12, 2017, this parameter was ignored by the API. It is now deprecated.
            

    :type blueprintId: string
    :param blueprintId: [REQUIRED]
            The ID for a virtual private server image (e.g., app_wordpress_4_4 or app_lamp_7_0 ). Use the get blueprints operation to return a list of available images (or blueprints ).
            

    :type bundleId: string
    :param bundleId: [REQUIRED]
            The bundle of specification information for your virtual private server (or instance ), including the pricing plan (e.g., micro_1_0 ).
            

    :type userData: string
    :param userData: A launch script you can create that configures a server with additional user data. For example, you might want to run apt-get -y update .
            Note
            Depending on the machine image you choose, the command to get software on your instance varies. Amazon Linux and CentOS use yum , Debian and Ubuntu use apt-get , and FreeBSD uses pkg . For a complete list, see the Dev Guide .
            

    :type keyPairName: string
    :param keyPairName: The name of your key pair.

    :type tags: list
    :param tags: The tag keys and optional values to add to the resource during create.
            To tag a resource after it has been created, see the tag resource operation.
            (dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
            For more information about tags in Lightsail, see the Lightsail Dev Guide .
            key (string) --The key of the tag.
            Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            value (string) --The value of the tag.
            Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def create_instances_from_snapshot(instanceNames=None, attachedDiskMapping=None, availabilityZone=None, instanceSnapshotName=None, bundleId=None, userData=None, keyPairName=None, tags=None):
    """
    Uses a specific snapshot as a blueprint for creating one or more new instances that are based on that identical configuration.
    The create instances from snapshot operation supports tag-based access control via request tags and resource tags applied to the resource identified by instanceSnapshotName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_instances_from_snapshot(
        instanceNames=[
            'string',
        ],
        attachedDiskMapping={
            'string': [
                {
                    'originalDiskPath': 'string',
                    'newDiskName': 'string'
                },
            ]
        },
        availabilityZone='string',
        instanceSnapshotName='string',
        bundleId='string',
        userData='string',
        keyPairName='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type instanceNames: list
    :param instanceNames: [REQUIRED]
            The names for your new instances.
            (string) --
            

    :type attachedDiskMapping: dict
    :param attachedDiskMapping: An object containing information about one or more disk mappings.
            (string) --
            (list) --
            (dict) --Describes a block storage disk mapping.
            originalDiskPath (string) --The original disk path exposed to the instance (for example, /dev/sdh ).
            newDiskName (string) --The new disk name (e.g., my-new-disk ).
            
            
            

    :type availabilityZone: string
    :param availabilityZone: [REQUIRED]
            The Availability Zone where you want to create your instances. Use the following formatting: us-east-2a (case sensitive). You can get a list of Availability Zones by using the get regions operation. Be sure to add the include Availability Zones parameter to your request.
            

    :type instanceSnapshotName: string
    :param instanceSnapshotName: [REQUIRED]
            The name of the instance snapshot on which you are basing your new instances. Use the get instance snapshots operation to return information about your existing snapshots.
            

    :type bundleId: string
    :param bundleId: [REQUIRED]
            The bundle of specification information for your virtual private server (or instance ), including the pricing plan (e.g., micro_1_0 ).
            

    :type userData: string
    :param userData: You can create a launch script that configures a server with additional user data. For example, apt-get -y update .
            Note
            Depending on the machine image you choose, the command to get software on your instance varies. Amazon Linux and CentOS use yum , Debian and Ubuntu use apt-get , and FreeBSD uses pkg . For a complete list, see the Dev Guide .
            

    :type keyPairName: string
    :param keyPairName: The name for your key pair.

    :type tags: list
    :param tags: The tag keys and optional values to add to the resource during create.
            To tag a resource after it has been created, see the tag resource operation.
            (dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
            For more information about tags in Lightsail, see the Lightsail Dev Guide .
            key (string) --The key of the tag.
            Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            value (string) --The value of the tag.
            Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def create_key_pair(keyPairName=None, tags=None):
    """
    Creates an SSH key pair.
    The create key pair operation supports tag-based access control via request tags. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_key_pair(
        keyPairName='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type keyPairName: string
    :param keyPairName: [REQUIRED]
            The name for your new key pair.
            

    :type tags: list
    :param tags: The tag keys and optional values to add to the resource during create.
            To tag a resource after it has been created, see the tag resource operation.
            (dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
            For more information about tags in Lightsail, see the Lightsail Dev Guide .
            key (string) --The key of the tag.
            Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            value (string) --The value of the tag.
            Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            
            

    :rtype: dict
    :return: {
        'keyPair': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'fingerprint': 'string'
        },
        'publicKeyBase64': 'string',
        'privateKeyBase64': 'string',
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def create_load_balancer(loadBalancerName=None, instancePort=None, healthCheckPath=None, certificateName=None, certificateDomainName=None, certificateAlternativeNames=None, tags=None):
    """
    Creates a Lightsail load balancer. To learn more about deciding whether to load balance your application, see Configure your Lightsail instances for load balancing . You can create up to 5 load balancers per AWS Region in your account.
    When you create a load balancer, you can specify a unique name and port settings. To change additional load balancer settings, use the UpdateLoadBalancerAttribute operation.
    The create load balancer operation supports tag-based access control via request tags. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_load_balancer(
        loadBalancerName='string',
        instancePort=123,
        healthCheckPath='string',
        certificateName='string',
        certificateDomainName='string',
        certificateAlternativeNames=[
            'string',
        ],
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type loadBalancerName: string
    :param loadBalancerName: [REQUIRED]
            The name of your load balancer.
            

    :type instancePort: integer
    :param instancePort: [REQUIRED]
            The instance port where you're creating your load balancer.
            

    :type healthCheckPath: string
    :param healthCheckPath: The path you provided to perform the load balancer health check. If you didn't specify a health check path, Lightsail uses the root path of your website (e.g., '/' ).
            You may want to specify a custom health check path other than the root of your application if your home page loads slowly or has a lot of media or scripting on it.
            

    :type certificateName: string
    :param certificateName: The name of the SSL/TLS certificate.
            If you specify certificateName , then certificateDomainName is required (and vice-versa).
            

    :type certificateDomainName: string
    :param certificateDomainName: The domain name with which your certificate is associated (e.g., example.com ).
            If you specify certificateDomainName , then certificateName is required (and vice-versa).
            

    :type certificateAlternativeNames: list
    :param certificateAlternativeNames: The optional alternative domains and subdomains to use with your SSL/TLS certificate (e.g., www.example.com , example.com , m.example.com , blog.example.com ).
            (string) --
            

    :type tags: list
    :param tags: The tag keys and optional values to add to the resource during create.
            To tag a resource after it has been created, see the tag resource operation.
            (dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
            For more information about tags in Lightsail, see the Lightsail Dev Guide .
            key (string) --The key of the tag.
            Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            value (string) --The value of the tag.
            Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def create_load_balancer_tls_certificate(loadBalancerName=None, certificateName=None, certificateDomainName=None, certificateAlternativeNames=None, tags=None):
    """
    Creates a Lightsail load balancer TLS certificate.
    TLS is just an updated, more secure version of Secure Socket Layer (SSL).
    The create load balancer tls certificate operation supports tag-based access control via resource tags applied to the resource identified by loadBalancerName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_load_balancer_tls_certificate(
        loadBalancerName='string',
        certificateName='string',
        certificateDomainName='string',
        certificateAlternativeNames=[
            'string',
        ],
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type loadBalancerName: string
    :param loadBalancerName: [REQUIRED]
            The load balancer name where you want to create the SSL/TLS certificate.
            

    :type certificateName: string
    :param certificateName: [REQUIRED]
            The SSL/TLS certificate name.
            You can have up to 10 certificates in your account at one time. Each Lightsail load balancer can have up to 2 certificates associated with it at one time. There is also an overall limit to the number of certificates that can be issue in a 365-day period. For more information, see Limits .
            

    :type certificateDomainName: string
    :param certificateDomainName: [REQUIRED]
            The domain name (e.g., example.com ) for your SSL/TLS certificate.
            

    :type certificateAlternativeNames: list
    :param certificateAlternativeNames: An array of strings listing alternative domains and subdomains for your SSL/TLS certificate. Lightsail will de-dupe the names for you. You can have a maximum of 9 alternative names (in addition to the 1 primary domain). We do not support wildcards (e.g., *.example.com ).
            (string) --
            

    :type tags: list
    :param tags: The tag keys and optional values to add to the resource during create.
            To tag a resource after it has been created, see the tag resource operation.
            (dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
            For more information about tags in Lightsail, see the Lightsail Dev Guide .
            key (string) --The key of the tag.
            Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            value (string) --The value of the tag.
            Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def create_relational_database(relationalDatabaseName=None, availabilityZone=None, relationalDatabaseBlueprintId=None, relationalDatabaseBundleId=None, masterDatabaseName=None, masterUsername=None, masterUserPassword=None, preferredBackupWindow=None, preferredMaintenanceWindow=None, publiclyAccessible=None, tags=None):
    """
    Creates a new database in Amazon Lightsail.
    The create relational database operation supports tag-based access control via request tags. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_relational_database(
        relationalDatabaseName='string',
        availabilityZone='string',
        relationalDatabaseBlueprintId='string',
        relationalDatabaseBundleId='string',
        masterDatabaseName='string',
        masterUsername='string',
        masterUserPassword='string',
        preferredBackupWindow='string',
        preferredMaintenanceWindow='string',
        publiclyAccessible=True|False,
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]
            The name to use for your new database.
            Constraints:
            Must contain from 2 to 255 alphanumeric characters, or hyphens.
            The first and last character must be a letter or number.
            

    :type availabilityZone: string
    :param availabilityZone: The Availability Zone in which to create your new database. Use the us-east-2a case-sensitive format.
            You can get a list of Availability Zones by using the get regions operation. Be sure to add the include relational database Availability Zones parameter to your request.
            

    :type relationalDatabaseBlueprintId: string
    :param relationalDatabaseBlueprintId: [REQUIRED]
            The blueprint ID for your new database. A blueprint describes the major engine version of a database.
            You can get a list of database blueprints IDs by using the get relational database blueprints operation.
            

    :type relationalDatabaseBundleId: string
    :param relationalDatabaseBundleId: [REQUIRED]
            The bundle ID for your new database. A bundle describes the performance specifications for your database.
            You can get a list of database bundle IDs by using the get relational database bundles operation.
            

    :type masterDatabaseName: string
    :param masterDatabaseName: [REQUIRED]
            The name of the master database created when the Lightsail database resource is created.
            Constraints:
            Must contain from 1 to 64 alphanumeric characters.
            Cannot be a word reserved by the specified database engine
            

    :type masterUsername: string
    :param masterUsername: [REQUIRED]
            The master user name for your new database.
            Constraints:
            Master user name is required.
            Must contain from 1 to 16 alphanumeric characters.
            The first character must be a letter.
            Cannot be a reserved word for the database engine you choose. For more information about reserved words in MySQL 5.6 or 5.7, see the Keywords and Reserved Words articles for MySQL 5.6 or MySQL 5.7 respectively.
            

    :type masterUserPassword: string
    :param masterUserPassword: The password for the master user of your new database. The password can include any printable ASCII character except '/', ''', or '@'.
            Constraints: Must contain 8 to 41 characters.
            

    :type preferredBackupWindow: string
    :param preferredBackupWindow: The daily time range during which automated backups are created for your new database if automated backups are enabled.
            The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region. For more information about the preferred backup window time blocks for each region, see the Working With Backups guide in the Amazon Relational Database Service (Amazon RDS) documentation.
            Constraints:
            Must be in the hh24:mi-hh24:mi format. Example: 16:00-16:30
            Specified in Universal Coordinated Time (UTC).
            Must not conflict with the preferred maintenance window.
            Must be at least 30 minutes.
            

    :type preferredMaintenanceWindow: string
    :param preferredMaintenanceWindow: The weekly time range during which system maintenance can occur on your new database.
            The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.
            Constraints:
            Must be in the ddd:hh24:mi-ddd:hh24:mi format.
            Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.
            Must be at least 30 minutes.
            Specified in Universal Coordinated Time (UTC).
            Example: Tue:17:00-Tue:17:30
            

    :type publiclyAccessible: boolean
    :param publiclyAccessible: Specifies the accessibility options for your new database. A value of true specifies a database that is available to resources outside of your Lightsail account. A value of false specifies a database that is available only to your Lightsail resources in the same region as your database.

    :type tags: list
    :param tags: The tag keys and optional values to add to the resource during create.
            To tag a resource after it has been created, see the tag resource operation.
            (dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
            For more information about tags in Lightsail, see the Lightsail Dev Guide .
            key (string) --The key of the tag.
            Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            value (string) --The value of the tag.
            Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def create_relational_database_from_snapshot(relationalDatabaseName=None, availabilityZone=None, publiclyAccessible=None, relationalDatabaseSnapshotName=None, relationalDatabaseBundleId=None, sourceRelationalDatabaseName=None, restoreTime=None, useLatestRestorableTime=None, tags=None):
    """
    Creates a new database from an existing database snapshot in Amazon Lightsail.
    You can create a new database from a snapshot in if something goes wrong with your original database, or to change it to a different plan, such as a high availability or standard plan.
    The create relational database from snapshot operation supports tag-based access control via request tags and resource tags applied to the resource identified by relationalDatabaseSnapshotName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_relational_database_from_snapshot(
        relationalDatabaseName='string',
        availabilityZone='string',
        publiclyAccessible=True|False,
        relationalDatabaseSnapshotName='string',
        relationalDatabaseBundleId='string',
        sourceRelationalDatabaseName='string',
        restoreTime=datetime(2015, 1, 1),
        useLatestRestorableTime=True|False,
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]
            The name to use for your new database.
            Constraints:
            Must contain from 2 to 255 alphanumeric characters, or hyphens.
            The first and last character must be a letter or number.
            

    :type availabilityZone: string
    :param availabilityZone: The Availability Zone in which to create your new database. Use the us-east-2a case-sensitive format.
            You can get a list of Availability Zones by using the get regions operation. Be sure to add the include relational database Availability Zones parameter to your request.
            

    :type publiclyAccessible: boolean
    :param publiclyAccessible: Specifies the accessibility options for your new database. A value of true specifies a database that is available to resources outside of your Lightsail account. A value of false specifies a database that is available only to your Lightsail resources in the same region as your database.

    :type relationalDatabaseSnapshotName: string
    :param relationalDatabaseSnapshotName: The name of the database snapshot from which to create your new database.

    :type relationalDatabaseBundleId: string
    :param relationalDatabaseBundleId: The bundle ID for your new database. A bundle describes the performance specifications for your database.
            You can get a list of database bundle IDs by using the get relational database bundles operation.
            When creating a new database from a snapshot, you cannot choose a bundle that is smaller than the bundle of the source database.
            

    :type sourceRelationalDatabaseName: string
    :param sourceRelationalDatabaseName: The name of the source database.

    :type restoreTime: datetime
    :param restoreTime: The date and time to restore your database from.
            Constraints:
            Must be before the latest restorable time for the database.
            Cannot be specified if the use latest restorable time parameter is true .
            Specified in Universal Coordinated Time (UTC).
            Specified in the Unix time format. For example, if you wish to use a restore time of October 1, 2018, at 8 PM UTC, then you input 1538424000 as the restore time.
            

    :type useLatestRestorableTime: boolean
    :param useLatestRestorableTime: Specifies whether your database is restored from the latest backup time. A value of true restores from the latest backup time.
            Default: false
            Constraints: Cannot be specified if the restore time parameter is provided.
            

    :type tags: list
    :param tags: The tag keys and optional values to add to the resource during create.
            To tag a resource after it has been created, see the tag resource operation.
            (dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
            For more information about tags in Lightsail, see the Lightsail Dev Guide .
            key (string) --The key of the tag.
            Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            value (string) --The value of the tag.
            Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def create_relational_database_snapshot(relationalDatabaseName=None, relationalDatabaseSnapshotName=None, tags=None):
    """
    Creates a snapshot of your database in Amazon Lightsail. You can use snapshots for backups, to make copies of a database, and to save data before deleting a database.
    The create relational database snapshot operation supports tag-based access control via request tags. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_relational_database_snapshot(
        relationalDatabaseName='string',
        relationalDatabaseSnapshotName='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]
            The name of the database on which to base your new snapshot.
            

    :type relationalDatabaseSnapshotName: string
    :param relationalDatabaseSnapshotName: [REQUIRED]
            The name for your new database snapshot.
            Constraints:
            Must contain from 2 to 255 alphanumeric characters, or hyphens.
            The first and last character must be a letter or number.
            

    :type tags: list
    :param tags: The tag keys and optional values to add to the resource during create.
            To tag a resource after it has been created, see the tag resource operation.
            (dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
            For more information about tags in Lightsail, see the Lightsail Dev Guide .
            key (string) --The key of the tag.
            Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            value (string) --The value of the tag.
            Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def delete_disk(diskName=None):
    """
    Deletes the specified block storage disk. The disk must be in the available state (not attached to a Lightsail instance).
    The delete disk operation supports tag-based access control via resource tags applied to the resource identified by diskName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_disk(
        diskName='string'
    )
    
    
    :type diskName: string
    :param diskName: [REQUIRED]
            The unique name of the disk you want to delete (e.g., my-disk ).
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def delete_disk_snapshot(diskSnapshotName=None):
    """
    Deletes the specified disk snapshot.
    When you make periodic snapshots of a disk, the snapshots are incremental, and only the blocks on the device that have changed since your last snapshot are saved in the new snapshot. When you delete a snapshot, only the data not needed for any other snapshot is removed. So regardless of which prior snapshots have been deleted, all active snapshots will have access to all the information needed to restore the disk.
    The delete disk snapshot operation supports tag-based access control via resource tags applied to the resource identified by diskSnapshotName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_disk_snapshot(
        diskSnapshotName='string'
    )
    
    
    :type diskSnapshotName: string
    :param diskSnapshotName: [REQUIRED]
            The name of the disk snapshot you want to delete (e.g., my-disk-snapshot ).
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def delete_domain(domainName=None):
    """
    Deletes the specified domain recordset and all of its domain records.
    The delete domain operation supports tag-based access control via resource tags applied to the resource identified by domainName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_domain(
        domainName='string'
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]
            The specific domain name to delete.
            

    :rtype: dict
    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def delete_domain_entry(domainName=None, domainEntry=None):
    """
    Deletes a specific domain entry.
    The delete domain entry operation supports tag-based access control via resource tags applied to the resource identified by domainName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_domain_entry(
        domainName='string',
        domainEntry={
            'id': 'string',
            'name': 'string',
            'target': 'string',
            'isAlias': True|False,
            'type': 'string',
            'options': {
                'string': 'string'
            }
        }
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]
            The name of the domain entry to delete.
            

    :type domainEntry: dict
    :param domainEntry: [REQUIRED]
            An array of key-value pairs containing information about your domain entries.
            id (string) --The ID of the domain recordset entry.
            name (string) --The name of the domain.
            target (string) --The target AWS name server (e.g., ns-111.awsdns-22.com. ).
            For Lightsail load balancers, the value looks like ab1234c56789c6b86aba6fb203d443bc-123456789.us-east-2.elb.amazonaws.com . Be sure to also set isAlias to true when setting up an A record for a load balancer.
            isAlias (boolean) --When true , specifies whether the domain entry is an alias used by the Lightsail load balancer. You can include an alias (A type) record in your request, which points to a load balancer DNS name and routes traffic to your load balancer
            type (string) --The type of domain entry (e.g., SOA or NS ).
            options (dict) --(Deprecated) The options for the domain entry.
            Note
            In releases prior to November 29, 2017, this parameter was not included in the API response. It is now deprecated.
            (string) --
            (string) --
            
            

    :rtype: dict
    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def delete_instance(instanceName=None):
    """
    Deletes a specific Amazon Lightsail virtual private server, or instance .
    The delete instance operation supports tag-based access control via resource tags applied to the resource identified by instanceName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_instance(
        instanceName='string'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]
            The name of the instance to delete.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def delete_instance_snapshot(instanceSnapshotName=None):
    """
    Deletes a specific snapshot of a virtual private server (or instance ).
    The delete instance snapshot operation supports tag-based access control via resource tags applied to the resource identified by instanceSnapshotName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_instance_snapshot(
        instanceSnapshotName='string'
    )
    
    
    :type instanceSnapshotName: string
    :param instanceSnapshotName: [REQUIRED]
            The name of the snapshot to delete.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def delete_key_pair(keyPairName=None):
    """
    Deletes a specific SSH key pair.
    The delete key pair operation supports tag-based access control via resource tags applied to the resource identified by keyPairName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_key_pair(
        keyPairName='string'
    )
    
    
    :type keyPairName: string
    :param keyPairName: [REQUIRED]
            The name of the key pair to delete.
            

    :rtype: dict
    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def delete_load_balancer(loadBalancerName=None):
    """
    Deletes a Lightsail load balancer and all its associated SSL/TLS certificates. Once the load balancer is deleted, you will need to create a new load balancer, create a new certificate, and verify domain ownership again.
    The delete load balancer operation supports tag-based access control via resource tags applied to the resource identified by loadBalancerName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_load_balancer(
        loadBalancerName='string'
    )
    
    
    :type loadBalancerName: string
    :param loadBalancerName: [REQUIRED]
            The name of the load balancer you want to delete.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def delete_load_balancer_tls_certificate(loadBalancerName=None, certificateName=None, force=None):
    """
    Deletes an SSL/TLS certificate associated with a Lightsail load balancer.
    The delete load balancer tls certificate operation supports tag-based access control via resource tags applied to the resource identified by loadBalancerName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_load_balancer_tls_certificate(
        loadBalancerName='string',
        certificateName='string',
        force=True|False
    )
    
    
    :type loadBalancerName: string
    :param loadBalancerName: [REQUIRED]
            The load balancer name.
            

    :type certificateName: string
    :param certificateName: [REQUIRED]
            The SSL/TLS certificate name.
            

    :type force: boolean
    :param force: When true , forces the deletion of an SSL/TLS certificate.
            There can be two certificates associated with a Lightsail load balancer: the primary and the backup. The force parameter is required when the primary SSL/TLS certificate is in use by an instance attached to the load balancer.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def delete_relational_database(relationalDatabaseName=None, skipFinalSnapshot=None, finalRelationalDatabaseSnapshotName=None):
    """
    Deletes a database in Amazon Lightsail.
    The delete relational database operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_relational_database(
        relationalDatabaseName='string',
        skipFinalSnapshot=True|False,
        finalRelationalDatabaseSnapshotName='string'
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]
            The name of the database that you are deleting.
            

    :type skipFinalSnapshot: boolean
    :param skipFinalSnapshot: Determines whether a final database snapshot is created before your database is deleted. If true is specified, no database snapshot is created. If false is specified, a database snapshot is created before your database is deleted.
            You must specify the final relational database snapshot name parameter if the skip final snapshot parameter is false .
            Default: false
            

    :type finalRelationalDatabaseSnapshotName: string
    :param finalRelationalDatabaseSnapshotName: The name of the database snapshot created if skip final snapshot is false , which is the default value for that parameter.
            Note
            Specifying this parameter and also specifying the skip final snapshot parameter to true results in an error.
            Constraints:
            Must contain from 2 to 255 alphanumeric characters, or hyphens.
            The first and last character must be a letter or number.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def delete_relational_database_snapshot(relationalDatabaseSnapshotName=None):
    """
    Deletes a database snapshot in Amazon Lightsail.
    The delete relational database snapshot operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_relational_database_snapshot(
        relationalDatabaseSnapshotName='string'
    )
    
    
    :type relationalDatabaseSnapshotName: string
    :param relationalDatabaseSnapshotName: [REQUIRED]
            The name of the database snapshot that you are deleting.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def detach_disk(diskName=None):
    """
    Detaches a stopped block storage disk from a Lightsail instance. Make sure to unmount any file systems on the device within your operating system before stopping the instance and detaching the disk.
    The detach disk operation supports tag-based access control via resource tags applied to the resource identified by diskName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.detach_disk(
        diskName='string'
    )
    
    
    :type diskName: string
    :param diskName: [REQUIRED]
            The unique name of the disk you want to detach from your instance (e.g., my-disk ).
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def detach_instances_from_load_balancer(loadBalancerName=None, instanceNames=None):
    """
    Detaches the specified instances from a Lightsail load balancer.
    This operation waits until the instances are no longer needed before they are detached from the load balancer.
    The detach instances from load balancer operation supports tag-based access control via resource tags applied to the resource identified by loadBalancerName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.detach_instances_from_load_balancer(
        loadBalancerName='string',
        instanceNames=[
            'string',
        ]
    )
    
    
    :type loadBalancerName: string
    :param loadBalancerName: [REQUIRED]
            The name of the Lightsail load balancer.
            

    :type instanceNames: list
    :param instanceNames: [REQUIRED]
            An array of strings containing the names of the instances you want to detach from the load balancer.
            (string) --
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def detach_static_ip(staticIpName=None):
    """
    Detaches a static IP from the Amazon Lightsail instance to which it is attached.
    See also: AWS API Documentation
    
    
    :example: response = client.detach_static_ip(
        staticIpName='string'
    )
    
    
    :type staticIpName: string
    :param staticIpName: [REQUIRED]
            The name of the static IP to detach from the instance.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def download_default_key_pair():
    """
    Downloads the default SSH key pair from the user's account.
    See also: AWS API Documentation
    
    
    :example: response = client.download_default_key_pair()
    
    
    :rtype: dict
    :return: {
        'publicKeyBase64': 'string',
        'privateKeyBase64': 'string'
    }
    
    
    """
    pass

def export_snapshot(sourceSnapshotName=None):
    """
    Exports a Amazon Lightsail instance or block storage disk snapshot to Amazon Elastic Compute Cloud (Amazon EC2). This operation results in an export snapshot record that can be used with the create cloud formation stack operation to create new Amazon EC2 instances.
    Exported instance snapshots appear in Amazon EC2 as Amazon Machine Images (AMIs), and the instance system disk appears as an Amazon Elastic Block Store (Amazon EBS) volume. Exported disk snapshots appear in Amazon EC2 as Amazon EBS volumes. Snapshots are exported to the same Amazon Web Services Region in Amazon EC2 as the source Lightsail snapshot.
    The export snapshot operation supports tag-based access control via resource tags applied to the resource identified by sourceSnapshotName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.export_snapshot(
        sourceSnapshotName='string'
    )
    
    
    :type sourceSnapshotName: string
    :param sourceSnapshotName: [REQUIRED]
            The name of the instance or disk snapshot to be exported to Amazon EC2.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
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

def get_active_names(pageToken=None):
    """
    Returns the names of all active (not deleted) resources.
    See also: AWS API Documentation
    
    
    :example: response = client.get_active_names(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: A token used for paginating results from your get active names request.

    :rtype: dict
    :return: {
        'activeNames': [
            'string',
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_blueprints(includeInactive=None, pageToken=None):
    """
    Returns the list of available instance images, or blueprints . You can use a blueprint to create a new virtual private server already running a specific operating system, as well as a preinstalled app or development stack. The software each instance is running depends on the blueprint image you choose.
    See also: AWS API Documentation
    
    
    :example: response = client.get_blueprints(
        includeInactive=True|False,
        pageToken='string'
    )
    
    
    :type includeInactive: boolean
    :param includeInactive: A Boolean value indicating whether to include inactive results in your request.

    :type pageToken: string
    :param pageToken: A token used for advancing to the next page of results from your get blueprints request.

    :rtype: dict
    :return: {
        'blueprints': [
            {
                'blueprintId': 'string',
                'name': 'string',
                'group': 'string',
                'type': 'os'|'app',
                'description': 'string',
                'isActive': True|False,
                'minPower': 123,
                'version': 'string',
                'versionCode': 'string',
                'productUrl': 'string',
                'licenseUrl': 'string',
                'platform': 'LINUX_UNIX'|'WINDOWS'
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_bundles(includeInactive=None, pageToken=None):
    """
    Returns the list of bundles that are available for purchase. A bundle describes the specs for your virtual private server (or instance ).
    See also: AWS API Documentation
    
    
    :example: response = client.get_bundles(
        includeInactive=True|False,
        pageToken='string'
    )
    
    
    :type includeInactive: boolean
    :param includeInactive: A Boolean value that indicates whether to include inactive bundle results in your request.

    :type pageToken: string
    :param pageToken: A token used for advancing to the next page of results from your get bundles request.

    :rtype: dict
    :return: {
        'bundles': [
            {
                'price': ...,
                'cpuCount': 123,
                'diskSizeInGb': 123,
                'bundleId': 'string',
                'instanceType': 'string',
                'isActive': True|False,
                'name': 'string',
                'power': 123,
                'ramSizeInGb': ...,
                'transferPerMonthInGb': 123,
                'supportedPlatforms': [
                    'LINUX_UNIX'|'WINDOWS',
                ]
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_cloud_formation_stack_records(pageToken=None):
    """
    Returns the CloudFormation stack record created as a result of the create cloud formation stack operation.
    An AWS CloudFormation stack is used to create a new Amazon EC2 instance from an exported Lightsail snapshot.
    See also: AWS API Documentation
    
    
    :example: response = client.get_cloud_formation_stack_records(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: A token used for advancing to a specific page of results for your get cloud formation stack records request.

    :rtype: dict
    :return: {
        'cloudFormationStackRecords': [
            {
                'name': 'string',
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'state': 'Started'|'Succeeded'|'Failed',
                'sourceInfo': [
                    {
                        'resourceType': 'ExportSnapshotRecord',
                        'name': 'string',
                        'arn': 'string'
                    },
                ],
                'destinationInfo': {
                    'id': 'string',
                    'service': 'string'
                }
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_disk(diskName=None):
    """
    Returns information about a specific block storage disk.
    See also: AWS API Documentation
    
    
    :example: response = client.get_disk(
        diskName='string'
    )
    
    
    :type diskName: string
    :param diskName: [REQUIRED]
            The name of the disk (e.g., my-disk ).
            

    :rtype: dict
    :return: {
        'disk': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'sizeInGb': 123,
            'isSystemDisk': True|False,
            'iops': 123,
            'path': 'string',
            'state': 'pending'|'error'|'available'|'in-use'|'unknown',
            'attachedTo': 'string',
            'isAttached': True|False,
            'attachmentState': 'string',
            'gbInUse': 123
        }
    }
    
    
    """
    pass

def get_disk_snapshot(diskSnapshotName=None):
    """
    Returns information about a specific block storage disk snapshot.
    See also: AWS API Documentation
    
    
    :example: response = client.get_disk_snapshot(
        diskSnapshotName='string'
    )
    
    
    :type diskSnapshotName: string
    :param diskSnapshotName: [REQUIRED]
            The name of the disk snapshot (e.g., my-disk-snapshot ).
            

    :rtype: dict
    :return: {
        'diskSnapshot': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'sizeInGb': 123,
            'state': 'pending'|'completed'|'error'|'unknown',
            'progress': 'string',
            'fromDiskName': 'string',
            'fromDiskArn': 'string'
        }
    }
    
    
    """
    pass

def get_disk_snapshots(pageToken=None):
    """
    Returns information about all block storage disk snapshots in your AWS account and region.
    If you are describing a long list of disk snapshots, you can paginate the output to make the list more manageable. You can use the pageToken and nextPageToken values to retrieve the next items in the list.
    See also: AWS API Documentation
    
    
    :example: response = client.get_disk_snapshots(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: A token used for advancing to the next page of results from your GetDiskSnapshots request.

    :rtype: dict
    :return: {
        'diskSnapshots': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'sizeInGb': 123,
                'state': 'pending'|'completed'|'error'|'unknown',
                'progress': 'string',
                'fromDiskName': 'string',
                'fromDiskArn': 'string'
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_disks(pageToken=None):
    """
    Returns information about all block storage disks in your AWS account and region.
    If you are describing a long list of disks, you can paginate the output to make the list more manageable. You can use the pageToken and nextPageToken values to retrieve the next items in the list.
    See also: AWS API Documentation
    
    
    :example: response = client.get_disks(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: A token used for advancing to the next page of results from your GetDisks request.

    :rtype: dict
    :return: {
        'disks': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'sizeInGb': 123,
                'isSystemDisk': True|False,
                'iops': 123,
                'path': 'string',
                'state': 'pending'|'error'|'available'|'in-use'|'unknown',
                'attachedTo': 'string',
                'isAttached': True|False,
                'attachmentState': 'string',
                'gbInUse': 123
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_domain(domainName=None):
    """
    Returns information about a specific domain recordset.
    See also: AWS API Documentation
    
    
    :example: response = client.get_domain(
        domainName='string'
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]
            The domain name for which your want to return information about.
            

    :rtype: dict
    :return: {
        'domain': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'domainEntries': [
                {
                    'id': 'string',
                    'name': 'string',
                    'target': 'string',
                    'isAlias': True|False,
                    'type': 'string',
                    'options': {
                        'string': 'string'
                    }
                },
            ]
        }
    }
    
    
    """
    pass

def get_domains(pageToken=None):
    """
    Returns a list of all domains in the user's account.
    See also: AWS API Documentation
    
    
    :example: response = client.get_domains(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: A token used for advancing to the next page of results from your get domains request.

    :rtype: dict
    :return: {
        'domains': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'domainEntries': [
                    {
                        'id': 'string',
                        'name': 'string',
                        'target': 'string',
                        'isAlias': True|False,
                        'type': 'string',
                        'options': {
                            'string': 'string'
                        }
                    },
                ]
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_export_snapshot_records(pageToken=None):
    """
    Returns the export snapshot record created as a result of the export snapshot operation.
    An export snapshot record can be used to create a new Amazon EC2 instance and its related resources with the create cloud formation stack operation.
    See also: AWS API Documentation
    
    
    :example: response = client.get_export_snapshot_records(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: A token used for advancing to a specific page of results for your get export snapshot records request.

    :rtype: dict
    :return: {
        'exportSnapshotRecords': [
            {
                'name': 'string',
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'state': 'Started'|'Succeeded'|'Failed',
                'sourceInfo': {
                    'resourceType': 'InstanceSnapshot'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'name': 'string',
                    'arn': 'string',
                    'fromResourceName': 'string',
                    'fromResourceArn': 'string',
                    'instanceSnapshotInfo': {
                        'fromBundleId': 'string',
                        'fromBlueprintId': 'string',
                        'fromDiskInfo': [
                            {
                                'name': 'string',
                                'path': 'string',
                                'sizeInGb': 123,
                                'isSystemDisk': True|False
                            },
                        ]
                    },
                    'diskSnapshotInfo': {
                        'sizeInGb': 123
                    }
                },
                'destinationInfo': {
                    'id': 'string',
                    'service': 'string'
                }
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_instance(instanceName=None):
    """
    Returns information about a specific Amazon Lightsail instance, which is a virtual private server.
    See also: AWS API Documentation
    
    
    :example: response = client.get_instance(
        instanceName='string'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]
            The name of the instance.
            

    :rtype: dict
    :return: {
        'instance': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'blueprintId': 'string',
            'blueprintName': 'string',
            'bundleId': 'string',
            'isStaticIp': True|False,
            'privateIpAddress': 'string',
            'publicIpAddress': 'string',
            'ipv6Address': 'string',
            'hardware': {
                'cpuCount': 123,
                'disks': [
                    {
                        'name': 'string',
                        'arn': 'string',
                        'supportCode': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'location': {
                            'availabilityZone': 'string',
                            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                        },
                        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'sizeInGb': 123,
                        'isSystemDisk': True|False,
                        'iops': 123,
                        'path': 'string',
                        'state': 'pending'|'error'|'available'|'in-use'|'unknown',
                        'attachedTo': 'string',
                        'isAttached': True|False,
                        'attachmentState': 'string',
                        'gbInUse': 123
                    },
                ],
                'ramSizeInGb': ...
            },
            'networking': {
                'monthlyTransfer': {
                    'gbPerMonthAllocated': 123
                },
                'ports': [
                    {
                        'fromPort': 123,
                        'toPort': 123,
                        'protocol': 'tcp'|'all'|'udp',
                        'accessFrom': 'string',
                        'accessType': 'Public'|'Private',
                        'commonName': 'string',
                        'accessDirection': 'inbound'|'outbound'
                    },
                ]
            },
            'state': {
                'code': 123,
                'name': 'string'
            },
            'username': 'string',
            'sshKeyName': 'string'
        }
    }
    
    
    """
    pass

def get_instance_access_details(instanceName=None, protocol=None):
    """
    Returns temporary SSH keys you can use to connect to a specific virtual private server, or instance .
    The get instance access details operation supports tag-based access control via resource tags applied to the resource identified by instanceName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.get_instance_access_details(
        instanceName='string',
        protocol='ssh'|'rdp'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]
            The name of the instance to access.
            

    :type protocol: string
    :param protocol: The protocol to use to connect to your instance. Defaults to ssh .

    :rtype: dict
    :return: {
        'accessDetails': {
            'certKey': 'string',
            'expiresAt': datetime(2015, 1, 1),
            'ipAddress': 'string',
            'password': 'string',
            'passwordData': {
                'ciphertext': 'string',
                'keyPairName': 'string'
            },
            'privateKey': 'string',
            'protocol': 'ssh'|'rdp',
            'instanceName': 'string',
            'username': 'string'
        }
    }
    
    
    """
    pass

def get_instance_metric_data(instanceName=None, metricName=None, period=None, startTime=None, endTime=None, unit=None, statistics=None):
    """
    Returns the data points for the specified Amazon Lightsail instance metric, given an instance name.
    See also: AWS API Documentation
    
    
    :example: response = client.get_instance_metric_data(
        instanceName='string',
        metricName='CPUUtilization'|'NetworkIn'|'NetworkOut'|'StatusCheckFailed'|'StatusCheckFailed_Instance'|'StatusCheckFailed_System',
        period=123,
        startTime=datetime(2015, 1, 1),
        endTime=datetime(2015, 1, 1),
        unit='Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
        statistics=[
            'Minimum'|'Maximum'|'Sum'|'Average'|'SampleCount',
        ]
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]
            The name of the instance for which you want to get metrics data.
            

    :type metricName: string
    :param metricName: [REQUIRED]
            The metric name to get data about.
            

    :type period: integer
    :param period: [REQUIRED]
            The granularity, in seconds, of the returned data points.
            

    :type startTime: datetime
    :param startTime: [REQUIRED]
            The start time of the time period.
            

    :type endTime: datetime
    :param endTime: [REQUIRED]
            The end time of the time period.
            

    :type unit: string
    :param unit: [REQUIRED]
            The unit. The list of valid values is below.
            

    :type statistics: list
    :param statistics: [REQUIRED]
            The instance statistics.
            (string) --
            

    :rtype: dict
    :return: {
        'metricName': 'CPUUtilization'|'NetworkIn'|'NetworkOut'|'StatusCheckFailed'|'StatusCheckFailed_Instance'|'StatusCheckFailed_System',
        'metricData': [
            {
                'average': 123.0,
                'maximum': 123.0,
                'minimum': 123.0,
                'sampleCount': 123.0,
                'sum': 123.0,
                'timestamp': datetime(2015, 1, 1),
                'unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None'
            },
        ]
    }
    
    
    """
    pass

def get_instance_port_states(instanceName=None):
    """
    Returns the port states for a specific virtual private server, or instance .
    See also: AWS API Documentation
    
    
    :example: response = client.get_instance_port_states(
        instanceName='string'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]
            The name of the instance.
            

    :rtype: dict
    :return: {
        'portStates': [
            {
                'fromPort': 123,
                'toPort': 123,
                'protocol': 'tcp'|'all'|'udp',
                'state': 'open'|'closed'
            },
        ]
    }
    
    
    """
    pass

def get_instance_snapshot(instanceSnapshotName=None):
    """
    Returns information about a specific instance snapshot.
    See also: AWS API Documentation
    
    
    :example: response = client.get_instance_snapshot(
        instanceSnapshotName='string'
    )
    
    
    :type instanceSnapshotName: string
    :param instanceSnapshotName: [REQUIRED]
            The name of the snapshot for which you are requesting information.
            

    :rtype: dict
    :return: {
        'instanceSnapshot': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'state': 'pending'|'error'|'available',
            'progress': 'string',
            'fromAttachedDisks': [
                {
                    'name': 'string',
                    'arn': 'string',
                    'supportCode': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'sizeInGb': 123,
                    'isSystemDisk': True|False,
                    'iops': 123,
                    'path': 'string',
                    'state': 'pending'|'error'|'available'|'in-use'|'unknown',
                    'attachedTo': 'string',
                    'isAttached': True|False,
                    'attachmentState': 'string',
                    'gbInUse': 123
                },
            ],
            'fromInstanceName': 'string',
            'fromInstanceArn': 'string',
            'fromBlueprintId': 'string',
            'fromBundleId': 'string',
            'sizeInGb': 123
        }
    }
    
    
    """
    pass

def get_instance_snapshots(pageToken=None):
    """
    Returns all instance snapshots for the user's account.
    See also: AWS API Documentation
    
    
    :example: response = client.get_instance_snapshots(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: A token used for advancing to the next page of results from your get instance snapshots request.

    :rtype: dict
    :return: {
        'instanceSnapshots': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'state': 'pending'|'error'|'available',
                'progress': 'string',
                'fromAttachedDisks': [
                    {
                        'name': 'string',
                        'arn': 'string',
                        'supportCode': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'location': {
                            'availabilityZone': 'string',
                            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                        },
                        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'sizeInGb': 123,
                        'isSystemDisk': True|False,
                        'iops': 123,
                        'path': 'string',
                        'state': 'pending'|'error'|'available'|'in-use'|'unknown',
                        'attachedTo': 'string',
                        'isAttached': True|False,
                        'attachmentState': 'string',
                        'gbInUse': 123
                    },
                ],
                'fromInstanceName': 'string',
                'fromInstanceArn': 'string',
                'fromBlueprintId': 'string',
                'fromBundleId': 'string',
                'sizeInGb': 123
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_instance_state(instanceName=None):
    """
    Returns the state of a specific instance. Works on one instance at a time.
    See also: AWS API Documentation
    
    
    :example: response = client.get_instance_state(
        instanceName='string'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]
            The name of the instance to get state information about.
            

    :rtype: dict
    :return: {
        'state': {
            'code': 123,
            'name': 'string'
        }
    }
    
    
    """
    pass

def get_instances(pageToken=None):
    """
    Returns information about all Amazon Lightsail virtual private servers, or instances .
    See also: AWS API Documentation
    
    
    :example: response = client.get_instances(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: A token used for advancing to the next page of results from your get instances request.

    :rtype: dict
    :return: {
        'instances': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'blueprintId': 'string',
                'blueprintName': 'string',
                'bundleId': 'string',
                'isStaticIp': True|False,
                'privateIpAddress': 'string',
                'publicIpAddress': 'string',
                'ipv6Address': 'string',
                'hardware': {
                    'cpuCount': 123,
                    'disks': [
                        {
                            'name': 'string',
                            'arn': 'string',
                            'supportCode': 'string',
                            'createdAt': datetime(2015, 1, 1),
                            'location': {
                                'availabilityZone': 'string',
                                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                            },
                            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                            'tags': [
                                {
                                    'key': 'string',
                                    'value': 'string'
                                },
                            ],
                            'sizeInGb': 123,
                            'isSystemDisk': True|False,
                            'iops': 123,
                            'path': 'string',
                            'state': 'pending'|'error'|'available'|'in-use'|'unknown',
                            'attachedTo': 'string',
                            'isAttached': True|False,
                            'attachmentState': 'string',
                            'gbInUse': 123
                        },
                    ],
                    'ramSizeInGb': ...
                },
                'networking': {
                    'monthlyTransfer': {
                        'gbPerMonthAllocated': 123
                    },
                    'ports': [
                        {
                            'fromPort': 123,
                            'toPort': 123,
                            'protocol': 'tcp'|'all'|'udp',
                            'accessFrom': 'string',
                            'accessType': 'Public'|'Private',
                            'commonName': 'string',
                            'accessDirection': 'inbound'|'outbound'
                        },
                    ]
                },
                'state': {
                    'code': 123,
                    'name': 'string'
                },
                'username': 'string',
                'sshKeyName': 'string'
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_key_pair(keyPairName=None):
    """
    Returns information about a specific key pair.
    See also: AWS API Documentation
    
    
    :example: response = client.get_key_pair(
        keyPairName='string'
    )
    
    
    :type keyPairName: string
    :param keyPairName: [REQUIRED]
            The name of the key pair for which you are requesting information.
            

    :rtype: dict
    :return: {
        'keyPair': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'fingerprint': 'string'
        }
    }
    
    
    """
    pass

def get_key_pairs(pageToken=None):
    """
    Returns information about all key pairs in the user's account.
    See also: AWS API Documentation
    
    
    :example: response = client.get_key_pairs(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: A token used for advancing to the next page of results from your get key pairs request.

    :rtype: dict
    :return: {
        'keyPairs': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'fingerprint': 'string'
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_load_balancer(loadBalancerName=None):
    """
    Returns information about the specified Lightsail load balancer.
    See also: AWS API Documentation
    
    
    :example: response = client.get_load_balancer(
        loadBalancerName='string'
    )
    
    
    :type loadBalancerName: string
    :param loadBalancerName: [REQUIRED]
            The name of the load balancer.
            

    :rtype: dict
    :return: {
        'loadBalancer': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'dnsName': 'string',
            'state': 'active'|'provisioning'|'active_impaired'|'failed'|'unknown',
            'protocol': 'HTTP_HTTPS'|'HTTP',
            'publicPorts': [
                123,
            ],
            'healthCheckPath': 'string',
            'instancePort': 123,
            'instanceHealthSummary': [
                {
                    'instanceName': 'string',
                    'instanceHealth': 'initial'|'healthy'|'unhealthy'|'unused'|'draining'|'unavailable',
                    'instanceHealthReason': 'Lb.RegistrationInProgress'|'Lb.InitialHealthChecking'|'Lb.InternalError'|'Instance.ResponseCodeMismatch'|'Instance.Timeout'|'Instance.FailedHealthChecks'|'Instance.NotRegistered'|'Instance.NotInUse'|'Instance.DeregistrationInProgress'|'Instance.InvalidState'|'Instance.IpUnusable'
                },
            ],
            'tlsCertificateSummaries': [
                {
                    'name': 'string',
                    'isAttached': True|False
                },
            ],
            'configurationOptions': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    **Lb.RegistrationInProgress ** - The target instance is in the process of being registered with the load balancer.
    **Lb.InitialHealthChecking ** - The Lightsail load balancer is still sending the target instance the minimum number of health checks required to determine its health status.
    
    """
    pass

def get_load_balancer_metric_data(loadBalancerName=None, metricName=None, period=None, startTime=None, endTime=None, unit=None, statistics=None):
    """
    Returns information about health metrics for your Lightsail load balancer.
    See also: AWS API Documentation
    
    
    :example: response = client.get_load_balancer_metric_data(
        loadBalancerName='string',
        metricName='ClientTLSNegotiationErrorCount'|'HealthyHostCount'|'UnhealthyHostCount'|'HTTPCode_LB_4XX_Count'|'HTTPCode_LB_5XX_Count'|'HTTPCode_Instance_2XX_Count'|'HTTPCode_Instance_3XX_Count'|'HTTPCode_Instance_4XX_Count'|'HTTPCode_Instance_5XX_Count'|'InstanceResponseTime'|'RejectedConnectionCount'|'RequestCount',
        period=123,
        startTime=datetime(2015, 1, 1),
        endTime=datetime(2015, 1, 1),
        unit='Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
        statistics=[
            'Minimum'|'Maximum'|'Sum'|'Average'|'SampleCount',
        ]
    )
    
    
    :type loadBalancerName: string
    :param loadBalancerName: [REQUIRED]
            The name of the load balancer.
            

    :type metricName: string
    :param metricName: [REQUIRED]
            The metric about which you want to return information. Valid values are listed below, along with the most useful statistics to include in your request.
            **ClientTLSNegotiationErrorCount ** - The number of TLS connections initiated by the client that did not establish a session with the load balancer. Possible causes include a mismatch of ciphers or protocols. Statistics : The most useful statistic is Sum .
            **HealthyHostCount ** - The number of target instances that are considered healthy. Statistics : The most useful statistic are Average , Minimum , and Maximum .
            **UnhealthyHostCount ** - The number of target instances that are considered unhealthy. Statistics : The most useful statistic are Average , Minimum , and Maximum .
            **HTTPCode_LB_4XX_Count ** - The number of HTTP 4XX client error codes that originate from the load balancer. Client errors are generated when requests are malformed or incomplete. These requests have not been received by the target instance. This count does not include any response codes generated by the target instances. Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 .
            **HTTPCode_LB_5XX_Count ** - The number of HTTP 5XX server error codes that originate from the load balancer. This count does not include any response codes generated by the target instances. Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 . Note that Minimum , Maximum , and Average all return 1 .
            **HTTPCode_Instance_2XX_Count ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer. Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 .
            **HTTPCode_Instance_3XX_Count ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.  Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 .
            **HTTPCode_Instance_4XX_Count ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer. Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 .
            **HTTPCode_Instance_5XX_Count ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer. Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 .
            **InstanceResponseTime ** - The time elapsed, in seconds, after the request leaves the load balancer until a response from the target instance is received. Statistics : The most useful statistic is Average .
            **RejectedConnectionCount ** - The number of connections that were rejected because the load balancer had reached its maximum number of connections. Statistics : The most useful statistic is Sum .
            **RequestCount ** - The number of requests processed over IPv4. This count includes only the requests with a response generated by a target instance of the load balancer. Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 .
            

    :type period: integer
    :param period: [REQUIRED]
            The granularity, in seconds, of the returned data points.
            

    :type startTime: datetime
    :param startTime: [REQUIRED]
            The start time of the period.
            

    :type endTime: datetime
    :param endTime: [REQUIRED]
            The end time of the period.
            

    :type unit: string
    :param unit: [REQUIRED]
            The unit for the time period request. Valid values are listed below.
            

    :type statistics: list
    :param statistics: [REQUIRED]
            An array of statistics that you want to request metrics for. Valid values are listed below.
            **SampleCount ** - The count (number) of data points used for the statistical calculation.
            **Average ** - The value of Sum / SampleCount during the specified period. By comparing this statistic with the Minimum and Maximum, you can determine the full scope of a metric and how close the average use is to the Minimum and Maximum. This comparison helps you to know when to increase or decrease your resources as needed.
            **Sum ** - All values submitted for the matching metric added together. This statistic can be useful for determining the total volume of a metric.
            **Minimum ** - The lowest value observed during the specified period. You can use this value to determine low volumes of activity for your application.
            **Maximum ** - The highest value observed during the specified period. You can use this value to determine high volumes of activity for your application.
            (string) --
            

    :rtype: dict
    :return: {
        'metricName': 'ClientTLSNegotiationErrorCount'|'HealthyHostCount'|'UnhealthyHostCount'|'HTTPCode_LB_4XX_Count'|'HTTPCode_LB_5XX_Count'|'HTTPCode_Instance_2XX_Count'|'HTTPCode_Instance_3XX_Count'|'HTTPCode_Instance_4XX_Count'|'HTTPCode_Instance_5XX_Count'|'InstanceResponseTime'|'RejectedConnectionCount'|'RequestCount',
        'metricData': [
            {
                'average': 123.0,
                'maximum': 123.0,
                'minimum': 123.0,
                'sampleCount': 123.0,
                'sum': 123.0,
                'timestamp': datetime(2015, 1, 1),
                'unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None'
            },
        ]
    }
    
    
    :returns: 
    **ClientTLSNegotiationErrorCount ** - The number of TLS connections initiated by the client that did not establish a session with the load balancer. Possible causes include a mismatch of ciphers or protocols.  Statistics : The most useful statistic is Sum .
    **HealthyHostCount ** - The number of target instances that are considered healthy.  Statistics : The most useful statistic are Average , Minimum , and Maximum .
    **UnhealthyHostCount ** - The number of target instances that are considered unhealthy.  Statistics : The most useful statistic are Average , Minimum , and Maximum .
    **HTTPCode_LB_4XX_Count ** - The number of HTTP 4XX client error codes that originate from the load balancer. Client errors are generated when requests are malformed or incomplete. These requests have not been received by the target instance. This count does not include any response codes generated by the target instances.  Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 .
    **HTTPCode_LB_5XX_Count ** - The number of HTTP 5XX server error codes that originate from the load balancer. This count does not include any response codes generated by the target instances.  Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 . Note that Minimum , Maximum , and Average all return 1 .
    **HTTPCode_Instance_2XX_Count ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.  Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 .
    **HTTPCode_Instance_3XX_Count ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.   Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 .
    **HTTPCode_Instance_4XX_Count ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.  Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 .
    **HTTPCode_Instance_5XX_Count ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.  Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 .
    **InstanceResponseTime ** - The time elapsed, in seconds, after the request leaves the load balancer until a response from the target instance is received.  Statistics : The most useful statistic is Average .
    **RejectedConnectionCount ** - The number of connections that were rejected because the load balancer had reached its maximum number of connections.  Statistics : The most useful statistic is Sum .
    **RequestCount ** - The number of requests processed over IPv4. This count includes only the requests with a response generated by a target instance of the load balancer.  Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 .
    
    """
    pass

def get_load_balancer_tls_certificates(loadBalancerName=None):
    """
    Returns information about the TLS certificates that are associated with the specified Lightsail load balancer.
    TLS is just an updated, more secure version of Secure Socket Layer (SSL).
    You can have a maximum of 2 certificates associated with a Lightsail load balancer. One is active and the other is inactive.
    See also: AWS API Documentation
    
    
    :example: response = client.get_load_balancer_tls_certificates(
        loadBalancerName='string'
    )
    
    
    :type loadBalancerName: string
    :param loadBalancerName: [REQUIRED]
            The name of the load balancer you associated with your SSL/TLS certificate.
            

    :rtype: dict
    :return: {
        'tlsCertificates': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'loadBalancerName': 'string',
                'isAttached': True|False,
                'status': 'PENDING_VALIDATION'|'ISSUED'|'INACTIVE'|'EXPIRED'|'VALIDATION_TIMED_OUT'|'REVOKED'|'FAILED'|'UNKNOWN',
                'domainName': 'string',
                'domainValidationRecords': [
                    {
                        'name': 'string',
                        'type': 'string',
                        'value': 'string',
                        'validationStatus': 'PENDING_VALIDATION'|'FAILED'|'SUCCESS',
                        'domainName': 'string'
                    },
                ],
                'failureReason': 'NO_AVAILABLE_CONTACTS'|'ADDITIONAL_VERIFICATION_REQUIRED'|'DOMAIN_NOT_ALLOWED'|'INVALID_PUBLIC_DOMAIN'|'OTHER',
                'issuedAt': datetime(2015, 1, 1),
                'issuer': 'string',
                'keyAlgorithm': 'string',
                'notAfter': datetime(2015, 1, 1),
                'notBefore': datetime(2015, 1, 1),
                'renewalSummary': {
                    'renewalStatus': 'PENDING_AUTO_RENEWAL'|'PENDING_VALIDATION'|'SUCCESS'|'FAILED',
                    'domainValidationOptions': [
                        {
                            'domainName': 'string',
                            'validationStatus': 'PENDING_VALIDATION'|'FAILED'|'SUCCESS'
                        },
                    ]
                },
                'revocationReason': 'UNSPECIFIED'|'KEY_COMPROMISE'|'CA_COMPROMISE'|'AFFILIATION_CHANGED'|'SUPERCEDED'|'CESSATION_OF_OPERATION'|'CERTIFICATE_HOLD'|'REMOVE_FROM_CRL'|'PRIVILEGE_WITHDRAWN'|'A_A_COMPROMISE',
                'revokedAt': datetime(2015, 1, 1),
                'serial': 'string',
                'signatureAlgorithm': 'string',
                'subject': 'string',
                'subjectAlternativeNames': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_load_balancers(pageToken=None):
    """
    Returns information about all load balancers in an account.
    If you are describing a long list of load balancers, you can paginate the output to make the list more manageable. You can use the pageToken and nextPageToken values to retrieve the next items in the list.
    See also: AWS API Documentation
    
    
    :example: response = client.get_load_balancers(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: A token used for paginating the results from your GetLoadBalancers request.

    :rtype: dict
    :return: {
        'loadBalancers': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'dnsName': 'string',
                'state': 'active'|'provisioning'|'active_impaired'|'failed'|'unknown',
                'protocol': 'HTTP_HTTPS'|'HTTP',
                'publicPorts': [
                    123,
                ],
                'healthCheckPath': 'string',
                'instancePort': 123,
                'instanceHealthSummary': [
                    {
                        'instanceName': 'string',
                        'instanceHealth': 'initial'|'healthy'|'unhealthy'|'unused'|'draining'|'unavailable',
                        'instanceHealthReason': 'Lb.RegistrationInProgress'|'Lb.InitialHealthChecking'|'Lb.InternalError'|'Instance.ResponseCodeMismatch'|'Instance.Timeout'|'Instance.FailedHealthChecks'|'Instance.NotRegistered'|'Instance.NotInUse'|'Instance.DeregistrationInProgress'|'Instance.InvalidState'|'Instance.IpUnusable'
                    },
                ],
                'tlsCertificateSummaries': [
                    {
                        'name': 'string',
                        'isAttached': True|False
                    },
                ],
                'configurationOptions': {
                    'string': 'string'
                }
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    :returns: 
    **Lb.RegistrationInProgress ** - The target instance is in the process of being registered with the load balancer.
    **Lb.InitialHealthChecking ** - The Lightsail load balancer is still sending the target instance the minimum number of health checks required to determine its health status.
    
    """
    pass

def get_operation(operationId=None):
    """
    Returns information about a specific operation. Operations include events such as when you create an instance, allocate a static IP, attach a static IP, and so on.
    See also: AWS API Documentation
    
    
    :example: response = client.get_operation(
        operationId='string'
    )
    
    
    :type operationId: string
    :param operationId: [REQUIRED]
            A GUID used to identify the operation.
            

    :rtype: dict
    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def get_operations(pageToken=None):
    """
    Returns information about all operations.
    Results are returned from oldest to newest, up to a maximum of 200. Results can be paged by making each subsequent call to GetOperations use the maximum (last) statusChangedAt value from the previous request.
    See also: AWS API Documentation
    
    
    :example: response = client.get_operations(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: A token used for advancing to the next page of results from your get operations request.

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_operations_for_resource(resourceName=None, pageToken=None):
    """
    Gets operations for a specific resource (e.g., an instance or a static IP).
    See also: AWS API Documentation
    
    
    :example: response = client.get_operations_for_resource(
        resourceName='string',
        pageToken='string'
    )
    
    
    :type resourceName: string
    :param resourceName: [REQUIRED]
            The name of the resource for which you are requesting information.
            

    :type pageToken: string
    :param pageToken: A token used for advancing to the next page of results from your get operations for resource request.

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ],
        'nextPageCount': 'string',
        'nextPageToken': 'string'
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

def get_regions(includeAvailabilityZones=None, includeRelationalDatabaseAvailabilityZones=None):
    """
    Returns a list of all valid regions for Amazon Lightsail. Use the include availability zones parameter to also return the Availability Zones in a region.
    See also: AWS API Documentation
    
    
    :example: response = client.get_regions(
        includeAvailabilityZones=True|False,
        includeRelationalDatabaseAvailabilityZones=True|False
    )
    
    
    :type includeAvailabilityZones: boolean
    :param includeAvailabilityZones: A Boolean value indicating whether to also include Availability Zones in your get regions request. Availability Zones are indicated with a letter: e.g., us-east-2a .

    :type includeRelationalDatabaseAvailabilityZones: boolean
    :param includeRelationalDatabaseAvailabilityZones: >A Boolean value indicating whether to also include Availability Zones for databases in your get regions request. Availability Zones are indicated with a letter (e.g., us-east-2a ).

    :rtype: dict
    :return: {
        'regions': [
            {
                'continentCode': 'string',
                'description': 'string',
                'displayName': 'string',
                'name': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2',
                'availabilityZones': [
                    {
                        'zoneName': 'string',
                        'state': 'string'
                    },
                ],
                'relationalDatabaseAvailabilityZones': [
                    {
                        'zoneName': 'string',
                        'state': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def get_relational_database(relationalDatabaseName=None):
    """
    Returns information about a specific database in Amazon Lightsail.
    See also: AWS API Documentation
    
    
    :example: response = client.get_relational_database(
        relationalDatabaseName='string'
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]
            The name of the database that you are looking up.
            

    :rtype: dict
    :return: {
        'relationalDatabase': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'relationalDatabaseBlueprintId': 'string',
            'relationalDatabaseBundleId': 'string',
            'masterDatabaseName': 'string',
            'hardware': {
                'cpuCount': 123,
                'diskSizeInGb': 123,
                'ramSizeInGb': ...
            },
            'state': 'string',
            'secondaryAvailabilityZone': 'string',
            'backupRetentionEnabled': True|False,
            'pendingModifiedValues': {
                'masterUserPassword': 'string',
                'engineVersion': 'string',
                'backupRetentionEnabled': True|False
            },
            'engine': 'string',
            'engineVersion': 'string',
            'latestRestorableTime': datetime(2015, 1, 1),
            'masterUsername': 'string',
            'parameterApplyStatus': 'string',
            'preferredBackupWindow': 'string',
            'preferredMaintenanceWindow': 'string',
            'publiclyAccessible': True|False,
            'masterEndpoint': {
                'port': 123,
                'address': 'string'
            },
            'pendingMaintenanceActions': [
                {
                    'action': 'string',
                    'description': 'string',
                    'currentApplyDate': datetime(2015, 1, 1)
                },
            ]
        }
    }
    
    
    """
    pass

def get_relational_database_blueprints(pageToken=None):
    """
    Returns a list of available database blueprints in Amazon Lightsail. A blueprint describes the major engine version of a database.
    You can use a blueprint ID to create a new database that runs a specific database engine.
    See also: AWS API Documentation
    
    
    :example: response = client.get_relational_database_blueprints(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: A token used for advancing to a specific page of results for your get relational database blueprints request.

    :rtype: dict
    :return: {
        'blueprints': [
            {
                'blueprintId': 'string',
                'engine': 'mysql',
                'engineVersion': 'string',
                'engineDescription': 'string',
                'engineVersionDescription': 'string',
                'isEngineDefault': True|False
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_relational_database_bundles(pageToken=None):
    """
    Returns the list of bundles that are available in Amazon Lightsail. A bundle describes the performance specifications for a database.
    You can use a bundle ID to create a new database with explicit performance specifications.
    See also: AWS API Documentation
    
    
    :example: response = client.get_relational_database_bundles(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: A token used for advancing to a specific page of results for your get relational database bundles request.

    :rtype: dict
    :return: {
        'bundles': [
            {
                'bundleId': 'string',
                'name': 'string',
                'price': ...,
                'ramSizeInGb': ...,
                'diskSizeInGb': 123,
                'transferPerMonthInGb': 123,
                'cpuCount': 123,
                'isEncrypted': True|False,
                'isActive': True|False
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_relational_database_events(relationalDatabaseName=None, durationInMinutes=None, pageToken=None):
    """
    Returns a list of events for a specific database in Amazon Lightsail.
    See also: AWS API Documentation
    
    
    :example: response = client.get_relational_database_events(
        relationalDatabaseName='string',
        durationInMinutes=123,
        pageToken='string'
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]
            The name of the database from which to get events.
            

    :type durationInMinutes: integer
    :param durationInMinutes: The number of minutes in the past from which to retrieve events. For example, to get all events from the past 2 hours, enter 120.
            Default: 60
            The minimum is 1 and the maximum is 14 days (20160 minutes).
            

    :type pageToken: string
    :param pageToken: A token used for advancing to a specific page of results from for get relational database events request.

    :rtype: dict
    :return: {
        'relationalDatabaseEvents': [
            {
                'resource': 'string',
                'createdAt': datetime(2015, 1, 1),
                'message': 'string',
                'eventCategories': [
                    'string',
                ]
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_relational_database_log_events(relationalDatabaseName=None, logStreamName=None, startTime=None, endTime=None, startFromHead=None, pageToken=None):
    """
    Returns a list of log events for a database in Amazon Lightsail.
    See also: AWS API Documentation
    
    
    :example: response = client.get_relational_database_log_events(
        relationalDatabaseName='string',
        logStreamName='string',
        startTime=datetime(2015, 1, 1),
        endTime=datetime(2015, 1, 1),
        startFromHead=True|False,
        pageToken='string'
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]
            The name of your database for which to get log events.
            

    :type logStreamName: string
    :param logStreamName: [REQUIRED]
            The name of the log stream.
            Use the get relational database log streams operation to get a list of available log streams.
            

    :type startTime: datetime
    :param startTime: The start of the time interval from which to get log events.
            Constraints:
            Specified in Universal Coordinated Time (UTC).
            Specified in the Unix time format. For example, if you wish to use a start time of October 1, 2018, at 8 PM UTC, then you input 1538424000 as the start time.
            

    :type endTime: datetime
    :param endTime: The end of the time interval from which to get log events.
            Constraints:
            Specified in Universal Coordinated Time (UTC).
            Specified in the Unix time format. For example, if you wish to use an end time of October 1, 2018, at 8 PM UTC, then you input 1538424000 as the end time.
            

    :type startFromHead: boolean
    :param startFromHead: Parameter to specify if the log should start from head or tail. If true is specified, the log event starts from the head of the log. If false is specified, the log event starts from the tail of the log.
            Default: false
            

    :type pageToken: string
    :param pageToken: A token used for advancing to a specific page of results for your get relational database log events request.

    :rtype: dict
    :return: {
        'resourceLogEvents': [
            {
                'createdAt': datetime(2015, 1, 1),
                'message': 'string'
            },
        ],
        'nextBackwardToken': 'string',
        'nextForwardToken': 'string'
    }
    
    
    """
    pass

def get_relational_database_log_streams(relationalDatabaseName=None):
    """
    Returns a list of available log streams for a specific database in Amazon Lightsail.
    See also: AWS API Documentation
    
    
    :example: response = client.get_relational_database_log_streams(
        relationalDatabaseName='string'
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]
            The name of your database for which to get log streams.
            

    :rtype: dict
    :return: {
        'logStreams': [
            'string',
        ]
    }
    
    
    """
    pass

def get_relational_database_master_user_password(relationalDatabaseName=None, passwordVersion=None):
    """
    Returns the current, previous, or pending versions of the master user password for a Lightsail database.
    The asdf operation GetRelationalDatabaseMasterUserPassword supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName.
    See also: AWS API Documentation
    
    
    :example: response = client.get_relational_database_master_user_password(
        relationalDatabaseName='string',
        passwordVersion='CURRENT'|'PREVIOUS'|'PENDING'
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]
            The name of your database for which to get the master user password.
            

    :type passwordVersion: string
    :param passwordVersion: The password version to return.
            Specifying CURRENT or PREVIOUS returns the current or previous passwords respectively. Specifying PENDING returns the newest version of the password that will rotate to CURRENT . After the PENDING password rotates to CURRENT , the PENDING password is no longer available.
            Default: CURRENT
            

    :rtype: dict
    :return: {
        'masterUserPassword': 'string',
        'createdAt': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def get_relational_database_metric_data(relationalDatabaseName=None, metricName=None, period=None, startTime=None, endTime=None, unit=None, statistics=None):
    """
    Returns the data points of the specified metric for a database in Amazon Lightsail.
    See also: AWS API Documentation
    
    
    :example: response = client.get_relational_database_metric_data(
        relationalDatabaseName='string',
        metricName='CPUUtilization'|'DatabaseConnections'|'DiskQueueDepth'|'FreeStorageSpace'|'NetworkReceiveThroughput'|'NetworkTransmitThroughput',
        period=123,
        startTime=datetime(2015, 1, 1),
        endTime=datetime(2015, 1, 1),
        unit='Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
        statistics=[
            'Minimum'|'Maximum'|'Sum'|'Average'|'SampleCount',
        ]
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]
            The name of your database from which to get metric data.
            

    :type metricName: string
    :param metricName: [REQUIRED]
            The name of the metric data to return.
            

    :type period: integer
    :param period: [REQUIRED]
            The granularity, in seconds, of the returned data points.
            

    :type startTime: datetime
    :param startTime: [REQUIRED]
            The start of the time interval from which to get metric data.
            Constraints:
            Specified in Universal Coordinated Time (UTC).
            Specified in the Unix time format. For example, if you wish to use a start time of October 1, 2018, at 8 PM UTC, then you input 1538424000 as the start time.
            

    :type endTime: datetime
    :param endTime: [REQUIRED]
            The end of the time interval from which to get metric data.
            Constraints:
            Specified in Universal Coordinated Time (UTC).
            Specified in the Unix time format. For example, if you wish to use an end time of October 1, 2018, at 8 PM UTC, then you input 1538424000 as the end time.
            

    :type unit: string
    :param unit: [REQUIRED]
            The unit for the metric data request.
            

    :type statistics: list
    :param statistics: [REQUIRED]
            The array of statistics for your metric data request.
            (string) --
            

    :rtype: dict
    :return: {
        'metricName': 'CPUUtilization'|'DatabaseConnections'|'DiskQueueDepth'|'FreeStorageSpace'|'NetworkReceiveThroughput'|'NetworkTransmitThroughput',
        'metricData': [
            {
                'average': 123.0,
                'maximum': 123.0,
                'minimum': 123.0,
                'sampleCount': 123.0,
                'sum': 123.0,
                'timestamp': datetime(2015, 1, 1),
                'unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None'
            },
        ]
    }
    
    
    """
    pass

def get_relational_database_parameters(relationalDatabaseName=None, pageToken=None):
    """
    Returns all of the runtime parameters offered by the underlying database software, or engine, for a specific database in Amazon Lightsail.
    In addition to the parameter names and values, this operation returns other information about each parameter. This information includes whether changes require a reboot, whether the parameter is modifiable, the allowed values, and the data types.
    See also: AWS API Documentation
    
    
    :example: response = client.get_relational_database_parameters(
        relationalDatabaseName='string',
        pageToken='string'
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]
            The name of your database for which to get parameters.
            

    :type pageToken: string
    :param pageToken: A token used for advancing to a specific page of results for your get relational database parameters request.

    :rtype: dict
    :return: {
        'parameters': [
            {
                'allowedValues': 'string',
                'applyMethod': 'string',
                'applyType': 'string',
                'dataType': 'string',
                'description': 'string',
                'isModifiable': True|False,
                'parameterName': 'string',
                'parameterValue': 'string'
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_relational_database_snapshot(relationalDatabaseSnapshotName=None):
    """
    Returns information about a specific database snapshot in Amazon Lightsail.
    See also: AWS API Documentation
    
    
    :example: response = client.get_relational_database_snapshot(
        relationalDatabaseSnapshotName='string'
    )
    
    
    :type relationalDatabaseSnapshotName: string
    :param relationalDatabaseSnapshotName: [REQUIRED]
            The name of the database snapshot for which to get information.
            

    :rtype: dict
    :return: {
        'relationalDatabaseSnapshot': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'engine': 'string',
            'engineVersion': 'string',
            'sizeInGb': 123,
            'state': 'string',
            'fromRelationalDatabaseName': 'string',
            'fromRelationalDatabaseArn': 'string',
            'fromRelationalDatabaseBundleId': 'string',
            'fromRelationalDatabaseBlueprintId': 'string'
        }
    }
    
    
    """
    pass

def get_relational_database_snapshots(pageToken=None):
    """
    Returns information about all of your database snapshots in Amazon Lightsail.
    See also: AWS API Documentation
    
    
    :example: response = client.get_relational_database_snapshots(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: A token used for advancing to a specific page of results for your get relational database snapshots request.

    :rtype: dict
    :return: {
        'relationalDatabaseSnapshots': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'engine': 'string',
                'engineVersion': 'string',
                'sizeInGb': 123,
                'state': 'string',
                'fromRelationalDatabaseName': 'string',
                'fromRelationalDatabaseArn': 'string',
                'fromRelationalDatabaseBundleId': 'string',
                'fromRelationalDatabaseBlueprintId': 'string'
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_relational_databases(pageToken=None):
    """
    Returns information about all of your databases in Amazon Lightsail.
    See also: AWS API Documentation
    
    
    :example: response = client.get_relational_databases(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: A token used for advancing to a specific page of results for your get relational database request.

    :rtype: dict
    :return: {
        'relationalDatabases': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'relationalDatabaseBlueprintId': 'string',
                'relationalDatabaseBundleId': 'string',
                'masterDatabaseName': 'string',
                'hardware': {
                    'cpuCount': 123,
                    'diskSizeInGb': 123,
                    'ramSizeInGb': ...
                },
                'state': 'string',
                'secondaryAvailabilityZone': 'string',
                'backupRetentionEnabled': True|False,
                'pendingModifiedValues': {
                    'masterUserPassword': 'string',
                    'engineVersion': 'string',
                    'backupRetentionEnabled': True|False
                },
                'engine': 'string',
                'engineVersion': 'string',
                'latestRestorableTime': datetime(2015, 1, 1),
                'masterUsername': 'string',
                'parameterApplyStatus': 'string',
                'preferredBackupWindow': 'string',
                'preferredMaintenanceWindow': 'string',
                'publiclyAccessible': True|False,
                'masterEndpoint': {
                    'port': 123,
                    'address': 'string'
                },
                'pendingMaintenanceActions': [
                    {
                        'action': 'string',
                        'description': 'string',
                        'currentApplyDate': datetime(2015, 1, 1)
                    },
                ]
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_static_ip(staticIpName=None):
    """
    Returns information about a specific static IP.
    See also: AWS API Documentation
    
    
    :example: response = client.get_static_ip(
        staticIpName='string'
    )
    
    
    :type staticIpName: string
    :param staticIpName: [REQUIRED]
            The name of the static IP in Lightsail.
            

    :rtype: dict
    :return: {
        'staticIp': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
            'ipAddress': 'string',
            'attachedTo': 'string',
            'isAttached': True|False
        }
    }
    
    
    """
    pass

def get_static_ips(pageToken=None):
    """
    Returns information about all static IPs in the user's account.
    See also: AWS API Documentation
    
    
    :example: response = client.get_static_ips(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: A token used for advancing to the next page of results from your get static IPs request.

    :rtype: dict
    :return: {
        'staticIps': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'ipAddress': 'string',
                'attachedTo': 'string',
                'isAttached': True|False
            },
        ],
        'nextPageToken': 'string'
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

def import_key_pair(keyPairName=None, publicKeyBase64=None):
    """
    Imports a public SSH key from a specific key pair.
    See also: AWS API Documentation
    
    
    :example: response = client.import_key_pair(
        keyPairName='string',
        publicKeyBase64='string'
    )
    
    
    :type keyPairName: string
    :param keyPairName: [REQUIRED]
            The name of the key pair for which you want to import the public key.
            

    :type publicKeyBase64: string
    :param publicKeyBase64: [REQUIRED]
            A base64-encoded public key of the ssh-rsa type.
            

    :rtype: dict
    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def is_vpc_peered():
    """
    Returns a Boolean value indicating whether your Lightsail VPC is peered.
    See also: AWS API Documentation
    
    
    :example: response = client.is_vpc_peered()
    
    
    :rtype: dict
    :return: {
        'isPeered': True|False
    }
    
    
    """
    pass

def open_instance_public_ports(portInfo=None, instanceName=None):
    """
    Adds public ports to an Amazon Lightsail instance.
    The open instance public ports operation supports tag-based access control via resource tags applied to the resource identified by instanceName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.open_instance_public_ports(
        portInfo={
            'fromPort': 123,
            'toPort': 123,
            'protocol': 'tcp'|'all'|'udp'
        },
        instanceName='string'
    )
    
    
    :type portInfo: dict
    :param portInfo: [REQUIRED]
            An array of key-value pairs containing information about the port mappings.
            fromPort (integer) --The first port in the range.
            toPort (integer) --The last port in the range.
            protocol (string) --The protocol.
            

    :type instanceName: string
    :param instanceName: [REQUIRED]
            The name of the instance for which you want to open the public ports.
            

    :rtype: dict
    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def peer_vpc():
    """
    Tries to peer the Lightsail VPC with the user's default VPC.
    See also: AWS API Documentation
    
    
    :example: response = client.peer_vpc()
    
    
    :rtype: dict
    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def put_instance_public_ports(portInfos=None, instanceName=None):
    """
    Sets the specified open ports for an Amazon Lightsail instance, and closes all ports for every protocol not included in the current request.
    The put instance public ports operation supports tag-based access control via resource tags applied to the resource identified by instanceName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.put_instance_public_ports(
        portInfos=[
            {
                'fromPort': 123,
                'toPort': 123,
                'protocol': 'tcp'|'all'|'udp'
            },
        ],
        instanceName='string'
    )
    
    
    :type portInfos: list
    :param portInfos: [REQUIRED]
            Specifies information about the public port(s).
            (dict) --Describes information about the ports on your virtual private server (or instance ).
            fromPort (integer) --The first port in the range.
            toPort (integer) --The last port in the range.
            protocol (string) --The protocol.
            
            

    :type instanceName: string
    :param instanceName: [REQUIRED]
            The Lightsail instance name of the public port(s) you are setting.
            

    :rtype: dict
    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def reboot_instance(instanceName=None):
    """
    Restarts a specific instance. When your Amazon Lightsail instance is finished rebooting, Lightsail assigns a new public IP address. To use the same IP address after restarting, create a static IP address and attach it to the instance.
    The reboot instance operation supports tag-based access control via resource tags applied to the resource identified by instanceName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.reboot_instance(
        instanceName='string'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]
            The name of the instance to reboot.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def reboot_relational_database(relationalDatabaseName=None):
    """
    Restarts a specific database in Amazon Lightsail.
    The reboot relational database operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.reboot_relational_database(
        relationalDatabaseName='string'
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]
            The name of your database to reboot.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def release_static_ip(staticIpName=None):
    """
    Deletes a specific static IP from your account.
    See also: AWS API Documentation
    
    
    :example: response = client.release_static_ip(
        staticIpName='string'
    )
    
    
    :type staticIpName: string
    :param staticIpName: [REQUIRED]
            The name of the static IP to delete.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def start_instance(instanceName=None):
    """
    Starts a specific Amazon Lightsail instance from a stopped state. To restart an instance, use the reboot instance operation.
    The start instance operation supports tag-based access control via resource tags applied to the resource identified by instanceName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.start_instance(
        instanceName='string'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]
            The name of the instance (a virtual private server) to start.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def start_relational_database(relationalDatabaseName=None):
    """
    Starts a specific database from a stopped state in Amazon Lightsail. To restart a database, use the reboot relational database operation.
    The start relational database operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.start_relational_database(
        relationalDatabaseName='string'
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]
            The name of your database to start.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def stop_instance(instanceName=None, force=None):
    """
    Stops a specific Amazon Lightsail instance that is currently running.
    The stop instance operation supports tag-based access control via resource tags applied to the resource identified by instanceName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.stop_instance(
        instanceName='string',
        force=True|False
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]
            The name of the instance (a virtual private server) to stop.
            

    :type force: boolean
    :param force: When set to True , forces a Lightsail instance that is stuck in a stopping state to stop.
            Warning
            Only use the force parameter if your instance is stuck in the stopping state. In any other state, your instance should stop normally without adding this parameter to your API request.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def stop_relational_database(relationalDatabaseName=None, relationalDatabaseSnapshotName=None):
    """
    Stops a specific database that is currently running in Amazon Lightsail.
    The stop relational database operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.stop_relational_database(
        relationalDatabaseName='string',
        relationalDatabaseSnapshotName='string'
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]
            The name of your database to stop.
            

    :type relationalDatabaseSnapshotName: string
    :param relationalDatabaseSnapshotName: The name of your new database snapshot to be created before stopping your database.

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def tag_resource(resourceName=None, tags=None):
    """
    Adds one or more tags to the specified Amazon Lightsail resource. Each resource can have a maximum of 50 tags. Each tag consists of a key and an optional value. Tag keys must be unique per resource. For more information about tags, see the Lightsail Dev Guide .
    The tag resource operation supports tag-based access control via request tags and resource tags applied to the resource identified by resourceName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.tag_resource(
        resourceName='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type resourceName: string
    :param resourceName: [REQUIRED]
            The name of the resource to which you are adding tags.
            

    :type tags: list
    :param tags: [REQUIRED]
            The tag key and optional value.
            (dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
            For more information about tags in Lightsail, see the Lightsail Dev Guide .
            key (string) --The key of the tag.
            Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            value (string) --The value of the tag.
            Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @
            
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def unpeer_vpc():
    """
    Attempts to unpeer the Lightsail VPC from the user's default VPC.
    See also: AWS API Documentation
    
    
    :example: response = client.unpeer_vpc()
    
    
    :rtype: dict
    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def untag_resource(resourceName=None, tagKeys=None):
    """
    Deletes the specified set of tag keys and their values from the specified Amazon Lightsail resource.
    The untag resource operation supports tag-based access control via request tags and resource tags applied to the resource identified by resourceName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.untag_resource(
        resourceName='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceName: string
    :param resourceName: [REQUIRED]
            The name of the resource from which you are removing a tag.
            

    :type tagKeys: list
    :param tagKeys: [REQUIRED]
            The tag keys to delete from the specified resource.
            (string) --
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def update_domain_entry(domainName=None, domainEntry=None):
    """
    Updates a domain recordset after it is created.
    The update domain entry operation supports tag-based access control via resource tags applied to the resource identified by domainName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.update_domain_entry(
        domainName='string',
        domainEntry={
            'id': 'string',
            'name': 'string',
            'target': 'string',
            'isAlias': True|False,
            'type': 'string',
            'options': {
                'string': 'string'
            }
        }
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]
            The name of the domain recordset to update.
            

    :type domainEntry: dict
    :param domainEntry: [REQUIRED]
            An array of key-value pairs containing information about the domain entry.
            id (string) --The ID of the domain recordset entry.
            name (string) --The name of the domain.
            target (string) --The target AWS name server (e.g., ns-111.awsdns-22.com. ).
            For Lightsail load balancers, the value looks like ab1234c56789c6b86aba6fb203d443bc-123456789.us-east-2.elb.amazonaws.com . Be sure to also set isAlias to true when setting up an A record for a load balancer.
            isAlias (boolean) --When true , specifies whether the domain entry is an alias used by the Lightsail load balancer. You can include an alias (A type) record in your request, which points to a load balancer DNS name and routes traffic to your load balancer
            type (string) --The type of domain entry (e.g., SOA or NS ).
            options (dict) --(Deprecated) The options for the domain entry.
            Note
            In releases prior to November 29, 2017, this parameter was not included in the API response. It is now deprecated.
            (string) --
            (string) --
            
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def update_load_balancer_attribute(loadBalancerName=None, attributeName=None, attributeValue=None):
    """
    Updates the specified attribute for a load balancer. You can only update one attribute at a time.
    The update load balancer attribute operation supports tag-based access control via resource tags applied to the resource identified by loadBalancerName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.update_load_balancer_attribute(
        loadBalancerName='string',
        attributeName='HealthCheckPath'|'SessionStickinessEnabled'|'SessionStickiness_LB_CookieDurationSeconds',
        attributeValue='string'
    )
    
    
    :type loadBalancerName: string
    :param loadBalancerName: [REQUIRED]
            The name of the load balancer that you want to modify (e.g., my-load-balancer .
            

    :type attributeName: string
    :param attributeName: [REQUIRED]
            The name of the attribute you want to update. Valid values are below.
            

    :type attributeValue: string
    :param attributeValue: [REQUIRED]
            The value that you want to specify for the attribute name.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def update_relational_database(relationalDatabaseName=None, masterUserPassword=None, rotateMasterUserPassword=None, preferredBackupWindow=None, preferredMaintenanceWindow=None, enableBackupRetention=None, disableBackupRetention=None, publiclyAccessible=None, applyImmediately=None):
    """
    Allows the update of one or more attributes of a database in Amazon Lightsail.
    Updates are applied immediately, or in cases where the updates could result in an outage, are applied during the database's predefined maintenance window.
    The update relational database operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.update_relational_database(
        relationalDatabaseName='string',
        masterUserPassword='string',
        rotateMasterUserPassword=True|False,
        preferredBackupWindow='string',
        preferredMaintenanceWindow='string',
        enableBackupRetention=True|False,
        disableBackupRetention=True|False,
        publiclyAccessible=True|False,
        applyImmediately=True|False
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]
            The name of your database to update.
            

    :type masterUserPassword: string
    :param masterUserPassword: The password for the master user of your database. The password can include any printable ASCII character except '/', ''', or '@'.
            Constraints: Must contain 8 to 41 characters.
            

    :type rotateMasterUserPassword: boolean
    :param rotateMasterUserPassword: When true , the master user password is changed to a new strong password generated by Lightsail.
            Use the get relational database master user password operation to get the new password.
            

    :type preferredBackupWindow: string
    :param preferredBackupWindow: The daily time range during which automated backups are created for your database if automated backups are enabled.
            Constraints:
            Must be in the hh24:mi-hh24:mi format. Example: 16:00-16:30
            Specified in Universal Coordinated Time (UTC).
            Must not conflict with the preferred maintenance window.
            Must be at least 30 minutes.
            

    :type preferredMaintenanceWindow: string
    :param preferredMaintenanceWindow: The weekly time range during which system maintenance can occur on your database.
            The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.
            Constraints:
            Must be in the ddd:hh24:mi-ddd:hh24:mi format.
            Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.
            Must be at least 30 minutes.
            Specified in Universal Coordinated Time (UTC).
            Example: Tue:17:00-Tue:17:30
            

    :type enableBackupRetention: boolean
    :param enableBackupRetention: When true , enables automated backup retention for your database.
            Updates are applied during the next maintenance window because this can result in an outage.
            

    :type disableBackupRetention: boolean
    :param disableBackupRetention: When true , disables automated backup retention for your database.
            Disabling backup retention deletes all automated database backups. Before disabling this, you may want to create a snapshot of your database using the create relational database snapshot operation.
            Updates are applied during the next maintenance window because this can result in an outage.
            

    :type publiclyAccessible: boolean
    :param publiclyAccessible: Specifies the accessibility options for your database. A value of true specifies a database that is available to resources outside of your Lightsail account. A value of false specifies a database that is available only to your Lightsail resources in the same region as your database.

    :type applyImmediately: boolean
    :param applyImmediately: When true , applies changes immediately. When false , applies changes during the preferred maintenance window. Some changes may cause an outage.
            Default: false
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def update_relational_database_parameters(relationalDatabaseName=None, parameters=None):
    """
    Allows the update of one or more parameters of a database in Amazon Lightsail.
    Parameter updates don't cause outages; therefore, their application is not subject to the preferred maintenance window. However, there are two ways in which paramater updates are applied: dynamic or pending-reboot . Parameters marked with a dynamic apply type are applied immediately. Parameters marked with a pending-reboot apply type are applied only after the database is rebooted using the reboot relational database operation.
    The update relational database parameters operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.update_relational_database_parameters(
        relationalDatabaseName='string',
        parameters=[
            {
                'allowedValues': 'string',
                'applyMethod': 'string',
                'applyType': 'string',
                'dataType': 'string',
                'description': 'string',
                'isModifiable': True|False,
                'parameterName': 'string',
                'parameterValue': 'string'
            },
        ]
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]
            The name of your database for which to update parameters.
            

    :type parameters: list
    :param parameters: [REQUIRED]
            The database parameters to update.
            (dict) --Describes the parameters of a database.
            allowedValues (string) --Specifies the valid range of values for the parameter.
            applyMethod (string) --Indicates when parameter updates are applied.
            Can be immediate or pending-reboot .
            applyType (string) --Specifies the engine-specific parameter type.
            dataType (string) --Specifies the valid data type for the parameter.
            description (string) --Provides a description of the parameter.
            isModifiable (boolean) --A Boolean value indicating whether the parameter can be modified.
            parameterName (string) --Specifies the name of the parameter.
            parameterValue (string) --Specifies the value of the parameter.
            
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

