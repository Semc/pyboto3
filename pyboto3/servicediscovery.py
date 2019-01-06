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

def create_http_namespace(Name=None, CreatorRequestId=None, Description=None):
    """
    Creates an HTTP namespace. Service instances that you register using an HTTP namespace can be discovered using a DiscoverInstances request but can't be discovered using DNS.
    For the current limit on the number of namespaces that you can create using the same AWS account, see AWS Cloud Map Limits in the AWS Cloud Map Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_http_namespace(
        Name='string',
        CreatorRequestId='string',
        Description='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name that you want to assign to this namespace.
            

    :type CreatorRequestId: string
    :param CreatorRequestId: A unique string that identifies the request and that allows failed CreateHttpNamespace requests to be retried without the risk of executing the operation twice. CreatorRequestId can be any unique string, for example, a date/time stamp.
            This field is autopopulated if not provided.
            

    :type Description: string
    :param Description: A description for the namespace.

    :rtype: dict
    :return: {
        'OperationId': 'string'
    }
    
    
    """
    pass

def create_private_dns_namespace(Name=None, CreatorRequestId=None, Description=None, Vpc=None):
    """
    Creates a private namespace based on DNS, which will be visible only inside a specified Amazon VPC. The namespace defines your service naming scheme. For example, if you name your namespace example.com and name your service backend , the resulting DNS name for the service will be backend.example.com . For the current limit on the number of namespaces that you can create using the same AWS account, see AWS Cloud Map Limits in the AWS Cloud Map Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_private_dns_namespace(
        Name='string',
        CreatorRequestId='string',
        Description='string',
        Vpc='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name that you want to assign to this namespace. When you create a private DNS namespace, AWS Cloud Map automatically creates an Amazon Route 53 private hosted zone that has the same name as the namespace.
            

    :type CreatorRequestId: string
    :param CreatorRequestId: A unique string that identifies the request and that allows failed CreatePrivateDnsNamespace requests to be retried without the risk of executing the operation twice. CreatorRequestId can be any unique string, for example, a date/time stamp.
            This field is autopopulated if not provided.
            

    :type Description: string
    :param Description: A description for the namespace.

    :type Vpc: string
    :param Vpc: [REQUIRED]
            The ID of the Amazon VPC that you want to associate the namespace with.
            

    :rtype: dict
    :return: {
        'OperationId': 'string'
    }
    
    
    """
    pass

def create_public_dns_namespace(Name=None, CreatorRequestId=None, Description=None):
    """
    Creates a public namespace based on DNS, which will be visible on the internet. The namespace defines your service naming scheme. For example, if you name your namespace example.com and name your service backend , the resulting DNS name for the service will be backend.example.com . For the current limit on the number of namespaces that you can create using the same AWS account, see AWS Cloud Map Limits in the AWS Cloud Map Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_public_dns_namespace(
        Name='string',
        CreatorRequestId='string',
        Description='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name that you want to assign to this namespace.
            

    :type CreatorRequestId: string
    :param CreatorRequestId: A unique string that identifies the request and that allows failed CreatePublicDnsNamespace requests to be retried without the risk of executing the operation twice. CreatorRequestId can be any unique string, for example, a date/time stamp.
            This field is autopopulated if not provided.
            

    :type Description: string
    :param Description: A description for the namespace.

    :rtype: dict
    :return: {
        'OperationId': 'string'
    }
    
    
    """
    pass

def create_service(Name=None, NamespaceId=None, CreatorRequestId=None, Description=None, DnsConfig=None, HealthCheckConfig=None, HealthCheckCustomConfig=None):
    """
    Creates a service, which defines the configuration for the following entities:
    After you create the service, you can submit a  RegisterInstance request, and AWS Cloud Map uses the values in the configuration to create the specified entities.
    For the current limit on the number of instances that you can register using the same namespace and using the same service, see AWS Cloud Map Limits in the AWS Cloud Map Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_service(
        Name='string',
        NamespaceId='string',
        CreatorRequestId='string',
        Description='string',
        DnsConfig={
            'NamespaceId': 'string',
            'RoutingPolicy': 'MULTIVALUE'|'WEIGHTED',
            'DnsRecords': [
                {
                    'Type': 'SRV'|'A'|'AAAA'|'CNAME',
                    'TTL': 123
                },
            ]
        },
        HealthCheckConfig={
            'Type': 'HTTP'|'HTTPS'|'TCP',
            'ResourcePath': 'string',
            'FailureThreshold': 123
        },
        HealthCheckCustomConfig={
            'FailureThreshold': 123
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name that you want to assign to the service.
            

    :type NamespaceId: string
    :param NamespaceId: The ID of the namespace that you want to use to create the service.

    :type CreatorRequestId: string
    :param CreatorRequestId: A unique string that identifies the request and that allows failed CreateService requests to be retried without the risk of executing the operation twice. CreatorRequestId can be any unique string, for example, a date/time stamp.
            This field is autopopulated if not provided.
            

    :type Description: string
    :param Description: A description for the service.

    :type DnsConfig: dict
    :param DnsConfig: A complex type that contains information about the Amazon Route 53 records that you want AWS Cloud Map to create when you register an instance.
            NamespaceId (string) --The ID of the namespace to use for DNS configuration.
            RoutingPolicy (string) --The routing policy that you want to apply to all Route 53 DNS records that AWS Cloud Map creates when you register an instance and specify this service.
            Note
            If you want to use this service to register instances that create alias records, specify WEIGHTED for the routing policy.
            You can specify the following values:
            MULTIVALUE
            If you define a health check for the service and the health check is healthy, Route 53 returns the applicable value for up to eight instances.
            For example, suppose the service includes configurations for one A record and a health check, and you use the service to register 10 instances. Route 53 responds to DNS queries with IP addresses for up to eight healthy instances. If fewer than eight instances are healthy, Route 53 responds to every DNS query with the IP addresses for all of the healthy instances.
            If you don't define a health check for the service, Route 53 assumes that all instances are healthy and returns the values for up to eight instances.
            For more information about the multivalue routing policy, see Multivalue Answer Routing in the Route 53 Developer Guide .
            WEIGHTED
            Route 53 returns the applicable value from one randomly selected instance from among the instances that you registered using the same service. Currently, all records have the same weight, so you can't route more or less traffic to any instances.
            For example, suppose the service includes configurations for one A record and a health check, and you use the service to register 10 instances. Route 53 responds to DNS queries with the IP address for one randomly selected instance from among the healthy instances. If no instances are healthy, Route 53 responds to DNS queries as if all of the instances were healthy.
            If you don't define a health check for the service, Route 53 assumes that all instances are healthy and returns the applicable value for one randomly selected instance.
            For more information about the weighted routing policy, see Weighted Routing in the Route 53 Developer Guide .
            DnsRecords (list) -- [REQUIRED]An array that contains one DnsRecord object for each Route 53 DNS record that you want AWS Cloud Map to create when you register an instance.
            (dict) --A complex type that contains information about the Route 53 DNS records that you want AWS Cloud Map to create when you register an instance.
            Type (string) -- [REQUIRED]The type of the resource, which indicates the type of value that Route 53 returns in response to DNS queries.
            Note the following:
            A, AAAA, and SRV records: You can specify settings for a maximum of one A, one AAAA, and one SRV record. You can specify them in any combination.
            CNAME records: If you specify CNAME for Type , you can't define any other records. This is a limitation of DNS: you can't create a CNAME record and any other type of record that has the same name as a CNAME record.
            Alias records: If you want AWS Cloud Map to create a Route 53 alias record when you register an instance, specify A or AAAA for Type .
            All records: You specify settings other than TTL and Type when you register an instance.
            The following values are supported:
            A
            Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.
            AAAA
            Route 53 returns the IP address of the resource in IPv6 format, such as 2001:0db8:85a3:0000:0000:abcd:0001:2345.
            CNAME
            Route 53 returns the domain name of the resource, such as www.example.com. Note the following:
            You specify the domain name that you want to route traffic to when you register an instance. For more information, see RegisterInstanceRequest$Attributes .
            You must specify WEIGHTED for the value of RoutingPolicy .
            You can't specify both CNAME for Type and settings for HealthCheckConfig . If you do, the request will fail with an InvalidInput error.
            SRV
            Route 53 returns the value for an SRV record. The value for an SRV record uses the following values:
            priority weight port service-hostname
            Note the following about the values:
            The values of priority and weight are both set to 1 and can't be changed.
            The value of port comes from the value that you specify for the AWS_INSTANCE_PORT attribute when you submit a RegisterInstance request.
            The value of service-hostname is a concatenation of the following values:
            The value that you specify for InstanceId when you register an instance.
            The name of the service.
            The name of the namespace.
            For example, if the value of InstanceId is test , the name of the service is backend , and the name of the namespace is example.com , the value of service-hostname is:
            test.backend.example.com
            If you specify settings for an SRV record and if you specify values for AWS_INSTANCE_IPV4 , AWS_INSTANCE_IPV6 , or both in the RegisterInstance request, AWS Cloud Map automatically creates A and/or AAAA records that have the same name as the value of service-hostname in the SRV record. You can ignore these records.
            TTL (integer) -- [REQUIRED]The amount of time, in seconds, that you want DNS resolvers to cache the settings for this record.
            Note
            Alias records don't include a TTL because Route 53 uses the TTL for the AWS resource that an alias record routes traffic to. If you include the AWS_ALIAS_DNS_NAME attribute when you submit a RegisterInstance request, the TTL value is ignored. Always specify a TTL for the service; you can use a service to register instances that create either alias or non-alias records.
            
            

    :type HealthCheckConfig: dict
    :param HealthCheckConfig: 
            Public DNS namespaces only. A complex type that contains settings for an optional Route 53 health check. If you specify settings for a health check, AWS Cloud Map associates the health check with all the Route 53 DNS records that you specify in DnsConfig .
            Warning
            If you specify a health check configuration, you can specify either HealthCheckCustomConfig or HealthCheckConfig but not both.
            For information about the charges for health checks, see AWS Cloud Map Pricing .
            Type (string) -- [REQUIRED]The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy.
            Warning
            You can't change the value of Type after you create a health check.
            You can create the following types of health checks:
            HTTP : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400.
            HTTPS : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400.
            Warning
            If you specify HTTPS for the value of Type , the endpoint must support TLS v1.0 or later.
            TCP : Route 53 tries to establish a TCP connection. If you specify TCP for Type , don't specify a value for ResourcePath .
            For more information, see How Route 53 Determines Whether an Endpoint Is Healthy in the Route 53 Developer Guide .
            ResourcePath (string) --The path that you want Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, such as the file /docs/route53-health-check.html . Route 53 automatically adds the DNS name for the service. If you don't specify a value for ResourcePath , the default value is / .
            If you specify TCP for Type , you must not specify a value for ResourcePath .
            FailureThreshold (integer) --The number of consecutive health checks that an endpoint must pass or fail for Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see How Route 53 Determines Whether an Endpoint Is Healthy in the Route 53 Developer Guide .
            

    :type HealthCheckCustomConfig: dict
    :param HealthCheckCustomConfig: A complex type that contains information about an optional custom health check.
            Warning
            If you specify a health check configuration, you can specify either HealthCheckCustomConfig or HealthCheckConfig but not both.
            FailureThreshold (integer) --The number of 30-second intervals that you want Cloud Map to wait after receiving an UpdateInstanceCustomHealthStatus request before it changes the health status of a service instance. For example, suppose you specify a value of 2 for FailureTheshold , and then your application sends an UpdateInstanceCustomHealthStatus request. Cloud Map waits for approximately 60 seconds (2 x 30) before changing the status of the service instance based on that request.
            Sending a second or subsequent UpdateInstanceCustomHealthStatus request with the same value before FailureThreshold x 30 seconds has passed doesn't accelerate the change. Cloud Map still waits FailureThreshold x 30 seconds after the first request to make the change.
            

    :rtype: dict
    :return: {
        'Service': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string',
            'NamespaceId': 'string',
            'Description': 'string',
            'InstanceCount': 123,
            'DnsConfig': {
                'NamespaceId': 'string',
                'RoutingPolicy': 'MULTIVALUE'|'WEIGHTED',
                'DnsRecords': [
                    {
                        'Type': 'SRV'|'A'|'AAAA'|'CNAME',
                        'TTL': 123
                    },
                ]
            },
            'HealthCheckConfig': {
                'Type': 'HTTP'|'HTTPS'|'TCP',
                'ResourcePath': 'string',
                'FailureThreshold': 123
            },
            'HealthCheckCustomConfig': {
                'FailureThreshold': 123
            },
            'CreateDate': datetime(2015, 1, 1),
            'CreatorRequestId': 'string'
        }
    }
    
    
    :returns: 
    Name (string) -- [REQUIRED]
    The name that you want to assign to the service.
    
    NamespaceId (string) -- The ID of the namespace that you want to use to create the service.
    CreatorRequestId (string) -- A unique string that identifies the request and that allows failed CreateService requests to be retried without the risk of executing the operation twice. CreatorRequestId can be any unique string, for example, a date/time stamp.
    This field is autopopulated if not provided.
    
    Description (string) -- A description for the service.
    DnsConfig (dict) -- A complex type that contains information about the Amazon Route 53 records that you want AWS Cloud Map to create when you register an instance.
    
    NamespaceId (string) --The ID of the namespace to use for DNS configuration.
    
    RoutingPolicy (string) --The routing policy that you want to apply to all Route 53 DNS records that AWS Cloud Map creates when you register an instance and specify this service.
    
    Note
    If you want to use this service to register instances that create alias records, specify WEIGHTED for the routing policy.
    
    You can specify the following values:
    
    MULTIVALUE
    If you define a health check for the service and the health check is healthy, Route 53 returns the applicable value for up to eight instances.
    For example, suppose the service includes configurations for one A record and a health check, and you use the service to register 10 instances. Route 53 responds to DNS queries with IP addresses for up to eight healthy instances. If fewer than eight instances are healthy, Route 53 responds to every DNS query with the IP addresses for all of the healthy instances.
    If you don't define a health check for the service, Route 53 assumes that all instances are healthy and returns the values for up to eight instances.
    For more information about the multivalue routing policy, see Multivalue Answer Routing in the Route 53 Developer Guide .
    
    WEIGHTED
    Route 53 returns the applicable value from one randomly selected instance from among the instances that you registered using the same service. Currently, all records have the same weight, so you can't route more or less traffic to any instances.
    For example, suppose the service includes configurations for one A record and a health check, and you use the service to register 10 instances. Route 53 responds to DNS queries with the IP address for one randomly selected instance from among the healthy instances. If no instances are healthy, Route 53 responds to DNS queries as if all of the instances were healthy.
    If you don't define a health check for the service, Route 53 assumes that all instances are healthy and returns the applicable value for one randomly selected instance.
    For more information about the weighted routing policy, see Weighted Routing in the Route 53 Developer Guide .
    
    DnsRecords (list) -- [REQUIRED]An array that contains one DnsRecord object for each Route 53 DNS record that you want AWS Cloud Map to create when you register an instance.
    
    (dict) --A complex type that contains information about the Route 53 DNS records that you want AWS Cloud Map to create when you register an instance.
    
    Type (string) -- [REQUIRED]The type of the resource, which indicates the type of value that Route 53 returns in response to DNS queries.
    Note the following:
    
    A, AAAA, and SRV records: You can specify settings for a maximum of one A, one AAAA, and one SRV record. You can specify them in any combination.
    CNAME records: If you specify CNAME for Type , you can't define any other records. This is a limitation of DNS: you can't create a CNAME record and any other type of record that has the same name as a CNAME record.
    Alias records: If you want AWS Cloud Map to create a Route 53 alias record when you register an instance, specify A or AAAA for Type .
    All records: You specify settings other than TTL and Type when you register an instance.
    
    The following values are supported:
    
    A
    Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.
    
    AAAA
    Route 53 returns the IP address of the resource in IPv6 format, such as 2001:0db8:85a3:0000:0000:abcd:0001:2345.
    
    CNAME
    Route 53 returns the domain name of the resource, such as www.example.com. Note the following:
    
    You specify the domain name that you want to route traffic to when you register an instance. For more information, see  RegisterInstanceRequest$Attributes .
    You must specify WEIGHTED for the value of RoutingPolicy .
    You can't specify both CNAME for Type and settings for HealthCheckConfig . If you do, the request will fail with an InvalidInput error.
    
    
    SRV
    Route 53 returns the value for an SRV record. The value for an SRV record uses the following values:
    
    priority weight port service-hostname
    Note the following about the values:
    
    The values of priority and weight are both set to 1 and can't be changed.
    The value of port comes from the value that you specify for the AWS_INSTANCE_PORT attribute when you submit a  RegisterInstance request.
    The value of service-hostname is a concatenation of the following values:
    The value that you specify for InstanceId when you register an instance.
    The name of the service.
    The name of the namespace.
    
    
    
    For example, if the value of InstanceId is test , the name of the service is backend , and the name of the namespace is example.com , the value of service-hostname is:
    
    test.backend.example.com
    If you specify settings for an SRV record and if you specify values for AWS_INSTANCE_IPV4 , AWS_INSTANCE_IPV6 , or both in the RegisterInstance request, AWS Cloud Map automatically creates A and/or AAAA records that have the same name as the value of service-hostname in the SRV record. You can ignore these records.
    
    TTL (integer) -- [REQUIRED]The amount of time, in seconds, that you want DNS resolvers to cache the settings for this record.
    
    Note
    Alias records don't include a TTL because Route 53 uses the TTL for the AWS resource that an alias record routes traffic to. If you include the AWS_ALIAS_DNS_NAME attribute when you submit a  RegisterInstance request, the TTL value is ignored. Always specify a TTL for the service; you can use a service to register instances that create either alias or non-alias records.
    
    
    
    
    
    
    
    
    HealthCheckConfig (dict) -- 
    Public DNS namespaces only. A complex type that contains settings for an optional Route 53 health check. If you specify settings for a health check, AWS Cloud Map associates the health check with all the Route 53 DNS records that you specify in DnsConfig .
    
    Warning
    If you specify a health check configuration, you can specify either HealthCheckCustomConfig or HealthCheckConfig but not both.
    
    For information about the charges for health checks, see AWS Cloud Map Pricing .
    
    Type (string) -- [REQUIRED]The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy.
    
    Warning
    You can't change the value of Type after you create a health check.
    
    You can create the following types of health checks:
    
    HTTP : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400.
    HTTPS : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400.
    
    
    Warning
    If you specify HTTPS for the value of Type , the endpoint must support TLS v1.0 or later.
    
    
    TCP : Route 53 tries to establish a TCP connection. If you specify TCP for Type , don't specify a value for ResourcePath .
    
    For more information, see How Route 53 Determines Whether an Endpoint Is Healthy in the Route 53 Developer Guide .
    
    ResourcePath (string) --The path that you want Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, such as the file /docs/route53-health-check.html . Route 53 automatically adds the DNS name for the service. If you don't specify a value for ResourcePath , the default value is / .
    If you specify TCP for Type , you must not specify a value for ResourcePath .
    
    FailureThreshold (integer) --The number of consecutive health checks that an endpoint must pass or fail for Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see How Route 53 Determines Whether an Endpoint Is Healthy in the Route 53 Developer Guide .
    
    
    
    HealthCheckCustomConfig (dict) -- A complex type that contains information about an optional custom health check.
    
    Warning
    If you specify a health check configuration, you can specify either HealthCheckCustomConfig or HealthCheckConfig but not both.
    
    
    FailureThreshold (integer) --The number of 30-second intervals that you want Cloud Map to wait after receiving an UpdateInstanceCustomHealthStatus request before it changes the health status of a service instance. For example, suppose you specify a value of 2 for FailureTheshold , and then your application sends an UpdateInstanceCustomHealthStatus request. Cloud Map waits for approximately 60 seconds (2 x 30) before changing the status of the service instance based on that request.
    Sending a second or subsequent UpdateInstanceCustomHealthStatus request with the same value before FailureThreshold x 30 seconds has passed doesn't accelerate the change. Cloud Map still waits FailureThreshold x 30 seconds after the first request to make the change.
    
    
    
    
    """
    pass

def delete_namespace(Id=None):
    """
    Deletes a namespace from the current account. If the namespace still contains one or more services, the request fails.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_namespace(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The ID of the namespace that you want to delete.
            

    :rtype: dict
    :return: {
        'OperationId': 'string'
    }
    
    
    """
    pass

def delete_service(Id=None):
    """
    Deletes a specified service. If the service still contains one or more registered instances, the request fails.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_service(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The ID of the service that you want to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def deregister_instance(ServiceId=None, InstanceId=None):
    """
    Deletes the Amazon Route 53 DNS records and health check, if any, that AWS Cloud Map created for the specified instance.
    See also: AWS API Documentation
    
    
    :example: response = client.deregister_instance(
        ServiceId='string',
        InstanceId='string'
    )
    
    
    :type ServiceId: string
    :param ServiceId: [REQUIRED]
            The ID of the service that the instance is associated with.
            

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The value that you specified for Id in the RegisterInstance request.
            

    :rtype: dict
    :return: {
        'OperationId': 'string'
    }
    
    
    """
    pass

def discover_instances(NamespaceName=None, ServiceName=None, MaxResults=None, QueryParameters=None, HealthStatus=None):
    """
    Discovers registered instances for a specified namespace and service.
    See also: AWS API Documentation
    
    
    :example: response = client.discover_instances(
        NamespaceName='string',
        ServiceName='string',
        MaxResults=123,
        QueryParameters={
            'string': 'string'
        },
        HealthStatus='HEALTHY'|'UNHEALTHY'|'ALL'
    )
    
    
    :type NamespaceName: string
    :param NamespaceName: [REQUIRED]
            The name of the namespace that you specified when you registered the instance.
            

    :type ServiceName: string
    :param ServiceName: [REQUIRED]
            The name of the service that you specified when you registered the instance.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of instances that you want Cloud Map to return in the response to a DiscoverInstances request. If you don't specify a value for MaxResults , Cloud Map returns up to 100 instances.

    :type QueryParameters: dict
    :param QueryParameters: A string map that contains attributes with values that you can use to filter instances by any custom attribute that you specified when you registered the instance. Only instances that match all the specified key/value pairs will be returned.
            (string) --
            (string) --
            

    :type HealthStatus: string
    :param HealthStatus: The health status of the instances that you want to discover.

    :rtype: dict
    :return: {
        'Instances': [
            {
                'InstanceId': 'string',
                'NamespaceName': 'string',
                'ServiceName': 'string',
                'HealthStatus': 'HEALTHY'|'UNHEALTHY'|'UNKNOWN',
                'Attributes': {
                    'string': 'string'
                }
            },
        ]
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

def get_instance(ServiceId=None, InstanceId=None):
    """
    Gets information about a specified instance.
    See also: AWS API Documentation
    
    
    :example: response = client.get_instance(
        ServiceId='string',
        InstanceId='string'
    )
    
    
    :type ServiceId: string
    :param ServiceId: [REQUIRED]
            The ID of the service that the instance is associated with.
            

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The ID of the instance that you want to get information about.
            

    :rtype: dict
    :return: {
        'Instance': {
            'Id': 'string',
            'CreatorRequestId': 'string',
            'Attributes': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    If the service that is specified by ServiceId includes settings for an SRV record, the value of InstanceId is automatically included as part of the value for the SRV record. For more information, see  DnsRecord$Type .
    You can use this value to update an existing instance.
    To register a new instance, you must specify a value that is unique among instances that you register by using the same service.
    If you specify an existing InstanceId and ServiceId , AWS Cloud Map updates the existing DNS records. If there's also an existing health check, AWS Cloud Map deletes the old health check and creates a new one.
    
    """
    pass

def get_instances_health_status(ServiceId=None, Instances=None, MaxResults=None, NextToken=None):
    """
    Gets the current health status (Healthy , Unhealthy , or Unknown ) of one or more instances that are associated with a specified service.
    See also: AWS API Documentation
    
    
    :example: response = client.get_instances_health_status(
        ServiceId='string',
        Instances=[
            'string',
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ServiceId: string
    :param ServiceId: [REQUIRED]
            The ID of the service that the instance is associated with.
            

    :type Instances: list
    :param Instances: An array that contains the IDs of all the instances that you want to get the health status for.
            If you omit Instances , AWS Cloud Map returns the health status for all the instances that are associated with the specified service.
            Note
            To get the IDs for the instances that you've registered by using a specified service, submit a ListInstances request.
            (string) --
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of instances that you want AWS Cloud Map to return in the response to a GetInstancesHealthStatus request. If you don't specify a value for MaxResults , AWS Cloud Map returns up to 100 instances.

    :type NextToken: string
    :param NextToken: For the first GetInstancesHealthStatus request, omit this value.
            If more than MaxResults instances match the specified criteria, you can submit another GetInstancesHealthStatus request to get the next group of results. Specify the value of NextToken from the previous response in the next request.
            

    :rtype: dict
    :return: {
        'Status': {
            'string': 'HEALTHY'|'UNHEALTHY'|'UNKNOWN'
        },
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_namespace(Id=None):
    """
    Gets information about a namespace.
    See also: AWS API Documentation
    
    
    :example: response = client.get_namespace(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The ID of the namespace that you want to get information about.
            

    :rtype: dict
    :return: {
        'Namespace': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string',
            'Type': 'DNS_PUBLIC'|'DNS_PRIVATE'|'HTTP',
            'Description': 'string',
            'ServiceCount': 123,
            'Properties': {
                'DnsProperties': {
                    'HostedZoneId': 'string'
                },
                'HttpProperties': {
                    'HttpName': 'string'
                }
            },
            'CreateDate': datetime(2015, 1, 1),
            'CreatorRequestId': 'string'
        }
    }
    
    
    """
    pass

def get_operation(OperationId=None):
    """
    Gets information about any operation that returns an operation ID in the response, such as a CreateService request.
    See also: AWS API Documentation
    
    
    :example: response = client.get_operation(
        OperationId='string'
    )
    
    
    :type OperationId: string
    :param OperationId: [REQUIRED]
            The ID of the operation that you want to get more information about.
            

    :rtype: dict
    :return: {
        'Operation': {
            'Id': 'string',
            'Type': 'CREATE_NAMESPACE'|'DELETE_NAMESPACE'|'UPDATE_SERVICE'|'REGISTER_INSTANCE'|'DEREGISTER_INSTANCE',
            'Status': 'SUBMITTED'|'PENDING'|'SUCCESS'|'FAIL',
            'ErrorMessage': 'string',
            'ErrorCode': 'string',
            'CreateDate': datetime(2015, 1, 1),
            'UpdateDate': datetime(2015, 1, 1),
            'Targets': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    ACCESS_DENIED
    CANNOT_CREATE_HOSTED_ZONE
    EXPIRED_TOKEN
    HOSTED_ZONE_NOT_FOUND
    INTERNAL_FAILURE
    INVALID_CHANGE_BATCH
    THROTTLED_REQUEST
    
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

def get_service(Id=None):
    """
    Gets the settings for a specified service.
    See also: AWS API Documentation
    
    
    :example: response = client.get_service(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The ID of the service that you want to get settings for.
            

    :rtype: dict
    :return: {
        'Service': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string',
            'NamespaceId': 'string',
            'Description': 'string',
            'InstanceCount': 123,
            'DnsConfig': {
                'NamespaceId': 'string',
                'RoutingPolicy': 'MULTIVALUE'|'WEIGHTED',
                'DnsRecords': [
                    {
                        'Type': 'SRV'|'A'|'AAAA'|'CNAME',
                        'TTL': 123
                    },
                ]
            },
            'HealthCheckConfig': {
                'Type': 'HTTP'|'HTTPS'|'TCP',
                'ResourcePath': 'string',
                'FailureThreshold': 123
            },
            'HealthCheckCustomConfig': {
                'FailureThreshold': 123
            },
            'CreateDate': datetime(2015, 1, 1),
            'CreatorRequestId': 'string'
        }
    }
    
    
    :returns: 
    You specify the domain name that you want to route traffic to when you register an instance. For more information, see  RegisterInstanceRequest$Attributes .
    You must specify WEIGHTED for the value of RoutingPolicy .
    You can't specify both CNAME for Type and settings for HealthCheckConfig . If you do, the request will fail with an InvalidInput error.
    
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

def list_instances(ServiceId=None, NextToken=None, MaxResults=None):
    """
    Lists summary information about the instances that you registered by using a specified service.
    See also: AWS API Documentation
    
    
    :example: response = client.list_instances(
        ServiceId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ServiceId: string
    :param ServiceId: [REQUIRED]
            The ID of the service that you want to list instances for.
            

    :type NextToken: string
    :param NextToken: For the first ListInstances request, omit this value.
            If more than MaxResults instances match the specified criteria, you can submit another ListInstances request to get the next group of results. Specify the value of NextToken from the previous response in the next request.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of instances that you want AWS Cloud Map to return in the response to a ListInstances request. If you don't specify a value for MaxResults , AWS Cloud Map returns up to 100 instances.

    :rtype: dict
    :return: {
        'Instances': [
            {
                'Id': 'string',
                'Attributes': {
                    'string': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    The attributes that are associate with the instance.
    For each attribute, the applicable value.
    
    """
    pass

def list_namespaces(NextToken=None, MaxResults=None, Filters=None):
    """
    Lists summary information about the namespaces that were created by the current AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_namespaces(
        NextToken='string',
        MaxResults=123,
        Filters=[
            {
                'Name': 'TYPE',
                'Values': [
                    'string',
                ],
                'Condition': 'EQ'|'IN'|'BETWEEN'
            },
        ]
    )
    
    
    :type NextToken: string
    :param NextToken: For the first ListNamespaces request, omit this value.
            If the response contains NextToken , submit another ListNamespaces request to get the next group of results. Specify the value of NextToken from the previous response in the next request.
            Note
            AWS Cloud Map gets MaxResults namespaces and then filters them based on the specified criteria. It's possible that no namespaces in the first MaxResults namespaces matched the specified criteria but that subsequent groups of MaxResults namespaces do contain namespaces that match the criteria.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of namespaces that you want AWS Cloud Map to return in the response to a ListNamespaces request. If you don't specify a value for MaxResults , AWS Cloud Map returns up to 100 namespaces.

    :type Filters: list
    :param Filters: A complex type that contains specifications for the namespaces that you want to list.
            If you specify more than one filter, a namespace must match all filters to be returned by ListNamespaces .
            (dict) --A complex type that identifies the namespaces that you want to list. You can choose to list public or private namespaces.
            Name (string) -- [REQUIRED]Specify TYPE .
            Values (list) -- [REQUIRED]If you specify EQ for Condition , specify either DNS_PUBLIC or DNS_PRIVATE .
            If you specify IN for Condition , you can specify DNS_PUBLIC , DNS_PRIVATE , or both.
            (string) --
            Condition (string) --The operator that you want to use to determine whether ListNamespaces returns a namespace. Valid values for condition include:
            EQ : When you specify EQ for the condition, you can choose to list only public namespaces or private namespaces, but not both. EQ is the default condition and can be omitted.
            IN : When you specify IN for the condition, you can choose to list public namespaces, private namespaces, or both.
            BETWEEN : Not applicable
            
            

    :rtype: dict
    :return: {
        'Namespaces': [
            {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string',
                'Type': 'DNS_PUBLIC'|'DNS_PRIVATE'|'HTTP',
                'Description': 'string',
                'ServiceCount': 123,
                'Properties': {
                    'DnsProperties': {
                        'HostedZoneId': 'string'
                    },
                    'HttpProperties': {
                        'HttpName': 'string'
                    }
                },
                'CreateDate': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_operations(NextToken=None, MaxResults=None, Filters=None):
    """
    Lists operations that match the criteria that you specify.
    See also: AWS API Documentation
    
    
    :example: response = client.list_operations(
        NextToken='string',
        MaxResults=123,
        Filters=[
            {
                'Name': 'NAMESPACE_ID'|'SERVICE_ID'|'STATUS'|'TYPE'|'UPDATE_DATE',
                'Values': [
                    'string',
                ],
                'Condition': 'EQ'|'IN'|'BETWEEN'
            },
        ]
    )
    
    
    :type NextToken: string
    :param NextToken: For the first ListOperations request, omit this value.
            If the response contains NextToken , submit another ListOperations request to get the next group of results. Specify the value of NextToken from the previous response in the next request.
            Note
            AWS Cloud Map gets MaxResults operations and then filters them based on the specified criteria. It's possible that no operations in the first MaxResults operations matched the specified criteria but that subsequent groups of MaxResults operations do contain operations that match the criteria.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of items that you want AWS Cloud Map to return in the response to a ListOperations request. If you don't specify a value for MaxResults , AWS Cloud Map returns up to 100 operations.

    :type Filters: list
    :param Filters: A complex type that contains specifications for the operations that you want to list, for example, operations that you started between a specified start date and end date.
            If you specify more than one filter, an operation must match all filters to be returned by ListOperations .
            (dict) --A complex type that lets you select the operations that you want to list.
            Name (string) -- [REQUIRED]Specify the operations that you want to get:
            NAMESPACE_ID : Gets operations related to specified namespaces.
            SERVICE_ID : Gets operations related to specified services.
            STATUS : Gets operations based on the status of the operations: SUBMITTED , PENDING , SUCCEED , or FAIL .
            TYPE : Gets specified types of operation.
            UPDATE_DATE : Gets operations that changed status during a specified date/time range.
            Values (list) -- [REQUIRED]Specify values that are applicable to the value that you specify for Name :
            NAMESPACE_ID : Specify one namespace ID.
            SERVICE_ID : Specify one service ID.
            STATUS : Specify one or more statuses: SUBMITTED , PENDING , SUCCEED , or FAIL .
            TYPE : Specify one or more of the following types: CREATE_NAMESPACE , DELETE_NAMESPACE , UPDATE_SERVICE , REGISTER_INSTANCE , or DEREGISTER_INSTANCE .
            UPDATE_DATE : Specify a start date and an end date in Unix date/time format and Coordinated Universal Time (UTC). The start date must be the first value.
            (string) --
            Condition (string) --The operator that you want to use to determine whether an operation matches the specified value. Valid values for condition include:
            EQ : When you specify EQ for the condition, you can specify only one value. EQ is supported for NAMESPACE_ID , SERVICE_ID , STATUS , and TYPE . EQ is the default condition and can be omitted.
            IN : When you specify IN for the condition, you can specify a list of one or more values. IN is supported for STATUS and TYPE . An operation must match one of the specified values to be returned in the response.
            BETWEEN : Specify a start date and an end date in Unix date/time format and Coordinated Universal Time (UTC). The start date must be the first value. BETWEEN is supported for UPDATE_DATE .
            
            

    :rtype: dict
    :return: {
        'Operations': [
            {
                'Id': 'string',
                'Status': 'SUBMITTED'|'PENDING'|'SUCCESS'|'FAIL'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    SUBMITTED : This is the initial state immediately after you submit a request.
    PENDING : AWS Cloud Map is performing the operation.
    SUCCESS : The operation succeeded.
    FAIL : The operation failed. For the failure reason, see ErrorMessage .
    
    """
    pass

def list_services(NextToken=None, MaxResults=None, Filters=None):
    """
    Lists summary information for all the services that are associated with one or more specified namespaces.
    See also: AWS API Documentation
    
    
    :example: response = client.list_services(
        NextToken='string',
        MaxResults=123,
        Filters=[
            {
                'Name': 'NAMESPACE_ID',
                'Values': [
                    'string',
                ],
                'Condition': 'EQ'|'IN'|'BETWEEN'
            },
        ]
    )
    
    
    :type NextToken: string
    :param NextToken: For the first ListServices request, omit this value.
            If the response contains NextToken , submit another ListServices request to get the next group of results. Specify the value of NextToken from the previous response in the next request.
            Note
            AWS Cloud Map gets MaxResults services and then filters them based on the specified criteria. It's possible that no services in the first MaxResults services matched the specified criteria but that subsequent groups of MaxResults services do contain services that match the criteria.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of services that you want AWS Cloud Map to return in the response to a ListServices request. If you don't specify a value for MaxResults , AWS Cloud Map returns up to 100 services.

    :type Filters: list
    :param Filters: A complex type that contains specifications for the namespaces that you want to list services for.
            If you specify more than one filter, an operation must match all filters to be returned by ListServices .
            (dict) --A complex type that lets you specify the namespaces that you want to list services for.
            Name (string) -- [REQUIRED]Specify NAMESPACE_ID .
            Values (list) -- [REQUIRED]The values that are applicable to the value that you specify for Condition to filter the list of services.
            (string) --
            Condition (string) --The operator that you want to use to determine whether a service is returned by ListServices . Valid values for Condition include the following:
            EQ : When you specify EQ , specify one namespace ID for Values . EQ is the default condition and can be omitted.
            IN : When you specify IN , specify a list of the IDs for the namespaces that you want ListServices to return a list of services for.
            BETWEEN : Not applicable.
            
            

    :rtype: dict
    :return: {
        'Services': [
            {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string',
                'Description': 'string',
                'InstanceCount': 123,
                'DnsConfig': {
                    'NamespaceId': 'string',
                    'RoutingPolicy': 'MULTIVALUE'|'WEIGHTED',
                    'DnsRecords': [
                        {
                            'Type': 'SRV'|'A'|'AAAA'|'CNAME',
                            'TTL': 123
                        },
                    ]
                },
                'HealthCheckConfig': {
                    'Type': 'HTTP'|'HTTPS'|'TCP',
                    'ResourcePath': 'string',
                    'FailureThreshold': 123
                },
                'HealthCheckCustomConfig': {
                    'FailureThreshold': 123
                },
                'CreateDate': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    A, AAAA, and SRV records: You can specify settings for a maximum of one A, one AAAA, and one SRV record. You can specify them in any combination.
    CNAME records: If you specify CNAME for Type , you can't define any other records. This is a limitation of DNS: you can't create a CNAME record and any other type of record that has the same name as a CNAME record.
    Alias records: If you want AWS Cloud Map to create a Route 53 alias record when you register an instance, specify A or AAAA for Type .
    All records: You specify settings other than TTL and Type when you register an instance.
    
    """
    pass

def register_instance(ServiceId=None, InstanceId=None, CreatorRequestId=None, Attributes=None):
    """
    Creates or updates one or more records and, optionally, creates a health check based on the settings in a specified service. When you submit a RegisterInstance request, the following occurs:
    For more information, see  CreateService .
    When AWS Cloud Map receives a DNS query for the specified DNS name, it returns the applicable value:
    For the current limit on the number of instances that you can register using the same namespace and using the same service, see AWS Cloud Map Limits in the AWS Cloud Map Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.register_instance(
        ServiceId='string',
        InstanceId='string',
        CreatorRequestId='string',
        Attributes={
            'string': 'string'
        }
    )
    
    
    :type ServiceId: string
    :param ServiceId: [REQUIRED]
            The ID of the service that you want to use for settings for the instance.
            

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            An identifier that you want to associate with the instance. Note the following:
            If the service that is specified by ServiceId includes settings for an SRV record, the value of InstanceId is automatically included as part of the value for the SRV record. For more information, see DnsRecord$Type .
            You can use this value to update an existing instance.
            To register a new instance, you must specify a value that is unique among instances that you register by using the same service.
            If you specify an existing InstanceId and ServiceId , AWS Cloud Map updates the existing DNS records, if any. If there's also an existing health check, AWS Cloud Map deletes the old health check and creates a new one.
            Note
            The health check isn't deleted immediately, so it will still appear for a while if you submit a ListHealthChecks request, for example.
            

    :type CreatorRequestId: string
    :param CreatorRequestId: A unique string that identifies the request and that allows failed RegisterInstance requests to be retried without the risk of executing the operation twice. You must use a unique CreatorRequestId string every time you submit a RegisterInstance request if you're registering additional instances for the same namespace and service. CreatorRequestId can be any unique string, for example, a date/time stamp.
            This field is autopopulated if not provided.
            

    :type Attributes: dict
    :param Attributes: [REQUIRED]
            A string map that contains the following information for the service that you specify in ServiceId :
            The attributes that apply to the records that are defined in the service.
            For each attribute, the applicable value.
            Supported attribute keys include the following:
            AWS_ALIAS_DNS_NAME
            If you want AWS Cloud Map to create an Amazon Route 53 alias record that routes traffic to an Elastic Load Balancing load balancer, specify the DNS name that is associated with the load balancer. For information about how to get the DNS name, see 'DNSName' in the topic AliasTarget in the Route 53 API Reference .
            Note the following:
            The configuration for the service that is specified by ServiceId must include settings for an A record, an AAAA record, or both.
            In the service that is specified by ServiceId , the value of RoutingPolicy must be WEIGHTED .
            If the service that is specified by ServiceId includes HealthCheckConfig settings, AWS Cloud Map will create the Route 53 health check, but it won't associate the health check with the alias record.
            Auto naming currently doesn't support creating alias records that route traffic to AWS resources other than ELB load balancers.
            If you specify a value for AWS_ALIAS_DNS_NAME , don't specify values for any of the AWS_INSTANCE attributes.
            AWS_INIT_HEALTH_STATUS
            If the service configuration includes HealthCheckCustomConfig , you can optionally use AWS_INIT_HEALTH_STATUS to specify the initial status of the custom health check, HEALTHY or UNHEALTHY . If you don't specify a value for AWS_INIT_HEALTH_STATUS , the initial status is HEALTHY .
            AWS_INSTANCE_CNAME
            If the service configuration includes a CNAME record, the domain name that you want Route 53 to return in response to DNS queries, for example, example.com .
            This value is required if the service specified by ServiceId includes settings for an CNAME record.
            AWS_INSTANCE_IPV4
            If the service configuration includes an A record, the IPv4 address that you want Route 53 to return in response to DNS queries, for example, 192.0.2.44 .
            This value is required if the service specified by ServiceId includes settings for an A record. If the service includes settings for an SRV record, you must specify a value for AWS_INSTANCE_IPV4 , AWS_INSTANCE_IPV6 , or both.
            AWS_INSTANCE_IPV6
            If the service configuration includes an AAAA record, the IPv6 address that you want Route 53 to return in response to DNS queries, for example, 2001:0db8:85a3:0000:0000:abcd:0001:2345 .
            This value is required if the service specified by ServiceId includes settings for an AAAA record. If the service includes settings for an SRV record, you must specify a value for AWS_INSTANCE_IPV4 , AWS_INSTANCE_IPV6 , or both.
            AWS_INSTANCE_PORT
            If the service includes an SRV record, the value that you want Route 53 to return for the port.
            If the service includes HealthCheckConfig , the port on the endpoint that you want Route 53 to send requests to.
            This value is required if you specified settings for an SRV record when you created the service.
            Custom attributes
            You can add up to 30 custom attributes. For each key-value pair, the maximum length of the attribute name is 255 characters, and the maximum length of the attribute value is 1,024 characters.
            (string) --
            (string) --
            

    :rtype: dict
    :return: {
        'OperationId': 'string'
    }
    
    
    :returns: 
    If the health check is healthy : returns all the records
    If the health check is unhealthy : returns the applicable value for the last healthy instance
    If you didn't specify a health check configuration : returns all the records
    
    """
    pass

def update_instance_custom_health_status(ServiceId=None, InstanceId=None, Status=None):
    """
    Submits a request to change the health status of a custom health check to healthy or unhealthy.
    You can use UpdateInstanceCustomHealthStatus to change the status only for custom health checks, which you define using HealthCheckCustomConfig when you create a service. You can't use it to change the status for Route 53 health checks, which you define using HealthCheckConfig .
    For more information, see  HealthCheckCustomConfig .
    See also: AWS API Documentation
    
    
    :example: response = client.update_instance_custom_health_status(
        ServiceId='string',
        InstanceId='string',
        Status='HEALTHY'|'UNHEALTHY'
    )
    
    
    :type ServiceId: string
    :param ServiceId: [REQUIRED]
            The ID of the service that includes the configuration for the custom health check that you want to change the status for.
            

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The ID of the instance that you want to change the health status for.
            

    :type Status: string
    :param Status: [REQUIRED]
            The new status of the instance, HEALTHY or UNHEALTHY .
            

    """
    pass

def update_service(Id=None, Service=None):
    """
    Submits a request to perform the following operations:
    For public and private DNS namespaces, you must specify all DnsRecords configurations (and, optionally, HealthCheckConfig ) that you want to appear in the updated service. Any current configurations that don't appear in an UpdateService request are deleted.
    When you update the TTL setting for a service, AWS Cloud Map also updates the corresponding settings in all the records and health checks that were created by using the specified service.
    See also: AWS API Documentation
    
    
    :example: response = client.update_service(
        Id='string',
        Service={
            'Description': 'string',
            'DnsConfig': {
                'DnsRecords': [
                    {
                        'Type': 'SRV'|'A'|'AAAA'|'CNAME',
                        'TTL': 123
                    },
                ]
            },
            'HealthCheckConfig': {
                'Type': 'HTTP'|'HTTPS'|'TCP',
                'ResourcePath': 'string',
                'FailureThreshold': 123
            }
        }
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The ID of the service that you want to update.
            

    :type Service: dict
    :param Service: [REQUIRED]
            A complex type that contains the new settings for the service.
            Description (string) --A description for the service.
            DnsConfig (dict) -- [REQUIRED]A complex type that contains information about the Route 53 DNS records that you want AWS Cloud Map to create when you register an instance.
            DnsRecords (list) -- [REQUIRED]An array that contains one DnsRecord object for each Route 53 record that you want AWS Cloud Map to create when you register an instance.
            (dict) --A complex type that contains information about the Route 53 DNS records that you want AWS Cloud Map to create when you register an instance.
            Type (string) -- [REQUIRED]The type of the resource, which indicates the type of value that Route 53 returns in response to DNS queries.
            Note the following:
            A, AAAA, and SRV records: You can specify settings for a maximum of one A, one AAAA, and one SRV record. You can specify them in any combination.
            CNAME records: If you specify CNAME for Type , you can't define any other records. This is a limitation of DNS: you can't create a CNAME record and any other type of record that has the same name as a CNAME record.
            Alias records: If you want AWS Cloud Map to create a Route 53 alias record when you register an instance, specify A or AAAA for Type .
            All records: You specify settings other than TTL and Type when you register an instance.
            The following values are supported:
            A
            Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.
            AAAA
            Route 53 returns the IP address of the resource in IPv6 format, such as 2001:0db8:85a3:0000:0000:abcd:0001:2345.
            CNAME
            Route 53 returns the domain name of the resource, such as www.example.com. Note the following:
            You specify the domain name that you want to route traffic to when you register an instance. For more information, see RegisterInstanceRequest$Attributes .
            You must specify WEIGHTED for the value of RoutingPolicy .
            You can't specify both CNAME for Type and settings for HealthCheckConfig . If you do, the request will fail with an InvalidInput error.
            SRV
            Route 53 returns the value for an SRV record. The value for an SRV record uses the following values:
            priority weight port service-hostname
            Note the following about the values:
            The values of priority and weight are both set to 1 and can't be changed.
            The value of port comes from the value that you specify for the AWS_INSTANCE_PORT attribute when you submit a RegisterInstance request.
            The value of service-hostname is a concatenation of the following values:
            The value that you specify for InstanceId when you register an instance.
            The name of the service.
            The name of the namespace.
            For example, if the value of InstanceId is test , the name of the service is backend , and the name of the namespace is example.com , the value of service-hostname is:
            test.backend.example.com
            If you specify settings for an SRV record and if you specify values for AWS_INSTANCE_IPV4 , AWS_INSTANCE_IPV6 , or both in the RegisterInstance request, AWS Cloud Map automatically creates A and/or AAAA records that have the same name as the value of service-hostname in the SRV record. You can ignore these records.
            TTL (integer) -- [REQUIRED]The amount of time, in seconds, that you want DNS resolvers to cache the settings for this record.
            Note
            Alias records don't include a TTL because Route 53 uses the TTL for the AWS resource that an alias record routes traffic to. If you include the AWS_ALIAS_DNS_NAME attribute when you submit a RegisterInstance request, the TTL value is ignored. Always specify a TTL for the service; you can use a service to register instances that create either alias or non-alias records.
            
            
            HealthCheckConfig (dict) --
            Public DNS namespaces only. A complex type that contains settings for an optional health check. If you specify settings for a health check, AWS Cloud Map associates the health check with the records that you specify in DnsConfig .
            Warning
            If you specify a health check configuration, you can specify either HealthCheckCustomConfig or HealthCheckConfig but not both.
            Health checks are basic Route 53 health checks that monitor an AWS endpoint. For information about pricing for health checks, see Amazon Route 53 Pricing .
            Note the following about configuring health checks.
            A and AAAA records
            If DnsConfig includes configurations for both A and AAAA records, AWS Cloud Map creates a health check that uses the IPv4 address to check the health of the resource. If the endpoint that is specified by the IPv4 address is unhealthy, Route 53 considers both the A and AAAA records to be unhealthy.
            CNAME records
            You can't specify settings for HealthCheckConfig when the DNSConfig includes CNAME for the value of Type . If you do, the CreateService request will fail with an InvalidInput error.
            Request interval
            A Route 53 health checker in each health-checking region sends a health check request to an endpoint every 30 seconds. On average, your endpoint receives a health check request about every two seconds. However, health checkers don't coordinate with one another, so you'll sometimes see several requests per second followed by a few seconds with no health checks at all.
            Health checking regions
            Health checkers perform checks from all Route 53 health-checking regions. For a list of the current regions, see Regions .
            Alias records
            When you register an instance, if you include the AWS_ALIAS_DNS_NAME attribute, AWS Cloud Map creates a Route 53 alias record. Note the following:
            Route 53 automatically sets EvaluateTargetHealth to true for alias records. When EvaluateTargetHealth is true, the alias record inherits the health of the referenced AWS resource. such as an ELB load balancer. For more information, see EvaluateTargetHealth .
            If you include HealthCheckConfig and then use the service to register an instance that creates an alias record, Route 53 doesn't create the health check.
            Charges for health checks
            Health checks are basic Route 53 health checks that monitor an AWS endpoint. For information about pricing for health checks, see Amazon Route 53 Pricing .
            Type (string) -- [REQUIRED]The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy.
            Warning
            You can't change the value of Type after you create a health check.
            You can create the following types of health checks:
            HTTP : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400.
            HTTPS : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400.
            Warning
            If you specify HTTPS for the value of Type , the endpoint must support TLS v1.0 or later.
            TCP : Route 53 tries to establish a TCP connection. If you specify TCP for Type , don't specify a value for ResourcePath .
            For more information, see How Route 53 Determines Whether an Endpoint Is Healthy in the Route 53 Developer Guide .
            ResourcePath (string) --The path that you want Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, such as the file /docs/route53-health-check.html . Route 53 automatically adds the DNS name for the service. If you don't specify a value for ResourcePath , the default value is / .
            If you specify TCP for Type , you must not specify a value for ResourcePath .
            FailureThreshold (integer) --The number of consecutive health checks that an endpoint must pass or fail for Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see How Route 53 Determines Whether an Endpoint Is Healthy in the Route 53 Developer Guide .
            
            

    :rtype: dict
    :return: {
        'OperationId': 'string'
    }
    
    
    :returns: 
    Id (string) -- [REQUIRED]
    The ID of the service that you want to update.
    
    Service (dict) -- [REQUIRED]
    A complex type that contains the new settings for the service.
    
    Description (string) --A description for the service.
    
    DnsConfig (dict) -- [REQUIRED]A complex type that contains information about the Route 53 DNS records that you want AWS Cloud Map to create when you register an instance.
    
    DnsRecords (list) -- [REQUIRED]An array that contains one DnsRecord object for each Route 53 record that you want AWS Cloud Map to create when you register an instance.
    
    (dict) --A complex type that contains information about the Route 53 DNS records that you want AWS Cloud Map to create when you register an instance.
    
    Type (string) -- [REQUIRED]The type of the resource, which indicates the type of value that Route 53 returns in response to DNS queries.
    Note the following:
    
    A, AAAA, and SRV records: You can specify settings for a maximum of one A, one AAAA, and one SRV record. You can specify them in any combination.
    CNAME records: If you specify CNAME for Type , you can't define any other records. This is a limitation of DNS: you can't create a CNAME record and any other type of record that has the same name as a CNAME record.
    Alias records: If you want AWS Cloud Map to create a Route 53 alias record when you register an instance, specify A or AAAA for Type .
    All records: You specify settings other than TTL and Type when you register an instance.
    
    The following values are supported:
    
    A
    Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.
    
    AAAA
    Route 53 returns the IP address of the resource in IPv6 format, such as 2001:0db8:85a3:0000:0000:abcd:0001:2345.
    
    CNAME
    Route 53 returns the domain name of the resource, such as www.example.com. Note the following:
    
    You specify the domain name that you want to route traffic to when you register an instance. For more information, see  RegisterInstanceRequest$Attributes .
    You must specify WEIGHTED for the value of RoutingPolicy .
    You can't specify both CNAME for Type and settings for HealthCheckConfig . If you do, the request will fail with an InvalidInput error.
    
    
    SRV
    Route 53 returns the value for an SRV record. The value for an SRV record uses the following values:
    
    priority weight port service-hostname
    Note the following about the values:
    
    The values of priority and weight are both set to 1 and can't be changed.
    The value of port comes from the value that you specify for the AWS_INSTANCE_PORT attribute when you submit a  RegisterInstance request.
    The value of service-hostname is a concatenation of the following values:
    The value that you specify for InstanceId when you register an instance.
    The name of the service.
    The name of the namespace.
    
    
    
    For example, if the value of InstanceId is test , the name of the service is backend , and the name of the namespace is example.com , the value of service-hostname is:
    
    test.backend.example.com
    If you specify settings for an SRV record and if you specify values for AWS_INSTANCE_IPV4 , AWS_INSTANCE_IPV6 , or both in the RegisterInstance request, AWS Cloud Map automatically creates A and/or AAAA records that have the same name as the value of service-hostname in the SRV record. You can ignore these records.
    
    TTL (integer) -- [REQUIRED]The amount of time, in seconds, that you want DNS resolvers to cache the settings for this record.
    
    Note
    Alias records don't include a TTL because Route 53 uses the TTL for the AWS resource that an alias record routes traffic to. If you include the AWS_ALIAS_DNS_NAME attribute when you submit a  RegisterInstance request, the TTL value is ignored. Always specify a TTL for the service; you can use a service to register instances that create either alias or non-alias records.
    
    
    
    
    
    
    
    
    HealthCheckConfig (dict) --
    Public DNS namespaces only. A complex type that contains settings for an optional health check. If you specify settings for a health check, AWS Cloud Map associates the health check with the records that you specify in DnsConfig .
    
    Warning
    If you specify a health check configuration, you can specify either HealthCheckCustomConfig or HealthCheckConfig but not both.
    
    Health checks are basic Route 53 health checks that monitor an AWS endpoint. For information about pricing for health checks, see Amazon Route 53 Pricing .
    Note the following about configuring health checks.
    
    A and AAAA records
    If DnsConfig includes configurations for both A and AAAA records, AWS Cloud Map creates a health check that uses the IPv4 address to check the health of the resource. If the endpoint that is specified by the IPv4 address is unhealthy, Route 53 considers both the A and AAAA records to be unhealthy.
    
    CNAME records
    You can't specify settings for HealthCheckConfig when the DNSConfig includes CNAME for the value of Type . If you do, the CreateService request will fail with an InvalidInput error.
    
    Request interval
    A Route 53 health checker in each health-checking region sends a health check request to an endpoint every 30 seconds. On average, your endpoint receives a health check request about every two seconds. However, health checkers don't coordinate with one another, so you'll sometimes see several requests per second followed by a few seconds with no health checks at all.
    
    Health checking regions
    Health checkers perform checks from all Route 53 health-checking regions. For a list of the current regions, see Regions .
    
    Alias records
    When you register an instance, if you include the AWS_ALIAS_DNS_NAME attribute, AWS Cloud Map creates a Route 53 alias record. Note the following:
    
    Route 53 automatically sets EvaluateTargetHealth to true for alias records. When EvaluateTargetHealth is true, the alias record inherits the health of the referenced AWS resource. such as an ELB load balancer. For more information, see EvaluateTargetHealth .
    If you include HealthCheckConfig and then use the service to register an instance that creates an alias record, Route 53 doesn't create the health check.
    
    
    Charges for health checks
    Health checks are basic Route 53 health checks that monitor an AWS endpoint. For information about pricing for health checks, see Amazon Route 53 Pricing .
    
    Type (string) -- [REQUIRED]The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy.
    
    Warning
    You can't change the value of Type after you create a health check.
    
    You can create the following types of health checks:
    
    HTTP : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400.
    HTTPS : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400.
    
    
    Warning
    If you specify HTTPS for the value of Type , the endpoint must support TLS v1.0 or later.
    
    
    TCP : Route 53 tries to establish a TCP connection. If you specify TCP for Type , don't specify a value for ResourcePath .
    
    For more information, see How Route 53 Determines Whether an Endpoint Is Healthy in the Route 53 Developer Guide .
    
    ResourcePath (string) --The path that you want Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, such as the file /docs/route53-health-check.html . Route 53 automatically adds the DNS name for the service. If you don't specify a value for ResourcePath , the default value is / .
    If you specify TCP for Type , you must not specify a value for ResourcePath .
    
    FailureThreshold (integer) --The number of consecutive health checks that an endpoint must pass or fail for Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see How Route 53 Determines Whether an Endpoint Is Healthy in the Route 53 Developer Guide .
    
    
    
    
    
    
    """
    pass

