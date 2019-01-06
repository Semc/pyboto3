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

def create_mesh(clientToken=None, meshName=None):
    """
    Creates a new service mesh. A service mesh is a logical boundary for network traffic between the services that reside within it.
    After you create your service mesh, you can create virtual nodes, virtual routers, and routes to distribute traffic between the applications in your mesh.
    See also: AWS API Documentation
    
    
    :example: response = client.create_mesh(
        clientToken='string',
        meshName='string'
    )
    
    
    :type clientToken: string
    :param clientToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.
            This field is autopopulated if not provided.
            

    :type meshName: string
    :param meshName: [REQUIRED]
            The name to use for the service mesh.
            

    :rtype: dict
    :return: {
        'mesh': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'uid': 'string',
                'version': 123
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            }
        }
    }
    
    
    """
    pass

def create_route(clientToken=None, meshName=None, routeName=None, spec=None, virtualRouterName=None):
    """
    Creates a new route that is associated with a virtual router.
    You can use the prefix parameter in your route specification for path-based routing of requests. For example, if your virtual router service name is my-service.local , and you want the route to match requests to my-service.local/metrics , then your prefix should be /metrics .
    If your route matches a request, you can distribute traffic to one or more target virtual nodes with relative weighting.
    See also: AWS API Documentation
    
    
    :example: response = client.create_route(
        clientToken='string',
        meshName='string',
        routeName='string',
        spec={
            'httpRoute': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                },
                'match': {
                    'prefix': 'string'
                }
            }
        },
        virtualRouterName='string'
    )
    
    
    :type clientToken: string
    :param clientToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.
            This field is autopopulated if not provided.
            

    :type meshName: string
    :param meshName: [REQUIRED]
            The name of the service mesh in which to create the route.
            

    :type routeName: string
    :param routeName: [REQUIRED]
            The name to use for the route.
            

    :type spec: dict
    :param spec: [REQUIRED]
            The route specification to apply.
            httpRoute (dict) --The HTTP routing information for the route.
            action (dict) --The action to take if a match is determined.
            weightedTargets (list) --The targets that traffic is routed to when a request matches the route. You can specify one or more targets and their relative weights with which to distribute traffic.
            (dict) --An object representing a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10.
            virtualNode (string) --The virtual node to associate with the weighted target.
            weight (integer) --The relative weight of the weighted target.
            
            match (dict) --The criteria for determining an HTTP request match.
            prefix (string) --Specifies the path with which to match requests. This parameter must always start with / , which by itself matches all requests to the virtual router service name. You can also match for path-based routing of requests. For example, if your virtual router service name is my-service.local , and you want the route to match requests to my-service.local/metrics , then your prefix should be /metrics .
            
            

    :type virtualRouterName: string
    :param virtualRouterName: [REQUIRED]
            The name of the virtual router in which to create the route.
            

    :rtype: dict
    :return: {
        'route': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'uid': 'string',
                'version': 123
            },
            'routeName': 'string',
            'spec': {
                'httpRoute': {
                    'action': {
                        'weightedTargets': [
                            {
                                'virtualNode': 'string',
                                'weight': 123
                            },
                        ]
                    },
                    'match': {
                        'prefix': 'string'
                    }
                }
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualRouterName': 'string'
        }
    }
    
    
    """
    pass

def create_virtual_node(clientToken=None, meshName=None, spec=None, virtualNodeName=None):
    """
    Creates a new virtual node within a service mesh.
    A virtual node acts as logical pointer to a particular task group, such as an Amazon ECS service or a Kubernetes deployment. When you create a virtual node, you must specify the DNS service discovery name for your task group.
    Any inbound traffic that your virtual node expects should be specified as a listener . Any outbound traffic that your virtual node expects to reach should be specified as a backend .
    The response metadata for your new virtual node contains the arn that is associated with the virtual node. Set this value (either the full ARN or the truncated resource name, for example, mesh/default/virtualNode/simpleapp , as the APPMESH_VIRTUAL_NODE_NAME environment variable for your task group's Envoy proxy container in your task definition or pod spec. This is then mapped to the node.id and node.cluster Envoy parameters.
    See also: AWS API Documentation
    
    
    :example: response = client.create_virtual_node(
        clientToken='string',
        meshName='string',
        spec={
            'backends': [
                'string',
            ],
            'listeners': [
                {
                    'healthCheck': {
                        'healthyThreshold': 123,
                        'intervalMillis': 123,
                        'path': 'string',
                        'port': 123,
                        'protocol': 'http'|'tcp',
                        'timeoutMillis': 123,
                        'unhealthyThreshold': 123
                    },
                    'portMapping': {
                        'port': 123,
                        'protocol': 'http'|'tcp'
                    }
                },
            ],
            'serviceDiscovery': {
                'dns': {
                    'serviceName': 'string'
                }
            }
        },
        virtualNodeName='string'
    )
    
    
    :type clientToken: string
    :param clientToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.
            This field is autopopulated if not provided.
            

    :type meshName: string
    :param meshName: [REQUIRED]
            The name of the service mesh in which to create the virtual node.
            

    :type spec: dict
    :param spec: [REQUIRED]
            The virtual node specification to apply.
            backends (list) --The backends to which the virtual node is expected to send outbound traffic.
            (string) --
            listeners (list) --The listeners from which the virtual node is expected to receive inbound traffic.
            (dict) --An object representing a listener for a virtual node.
            healthCheck (dict) --The health check information for the listener.
            Note
            Listener health checks are not available during the App Mesh preview.
            healthyThreshold (integer) --The number of consecutive successful health checks that must occur before declaring listener healthy.
            intervalMillis (integer) --The time period in milliseconds between each health check execution.
            path (string) --The destination path for the health check request.
            port (integer) --The destination port for the health check request.
            protocol (string) --The protocol for the health check request.
            timeoutMillis (integer) --The amount of time to wait when receiving a response from the health check, in milliseconds.
            unhealthyThreshold (integer) --The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy.
            portMapping (dict) --The port mapping information for the listener.
            port (integer) --The port used for the port mapping.
            protocol (string) --The protocol used for the port mapping.
            
            serviceDiscovery (dict) --The service discovery information for the virtual node.
            dns (dict) --Specifies the DNS service name for the virtual node.
            serviceName (string) --The DNS service name for your virtual node.
            
            

    :type virtualNodeName: string
    :param virtualNodeName: [REQUIRED]
            The name to use for the virtual node.
            

    :rtype: dict
    :return: {
        'virtualNode': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'uid': 'string',
                'version': 123
            },
            'spec': {
                'backends': [
                    'string',
                ],
                'listeners': [
                    {
                        'healthCheck': {
                            'healthyThreshold': 123,
                            'intervalMillis': 123,
                            'path': 'string',
                            'port': 123,
                            'protocol': 'http'|'tcp',
                            'timeoutMillis': 123,
                            'unhealthyThreshold': 123
                        },
                        'portMapping': {
                            'port': 123,
                            'protocol': 'http'|'tcp'
                        }
                    },
                ],
                'serviceDiscovery': {
                    'dns': {
                        'serviceName': 'string'
                    }
                }
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualNodeName': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_virtual_router(clientToken=None, meshName=None, spec=None, virtualRouterName=None):
    """
    Creates a new virtual router within a service mesh.
    Virtual routers handle traffic for one or more service names within your mesh. After you create your virtual router, create and associate routes for your virtual router that direct incoming requests to different virtual nodes.
    See also: AWS API Documentation
    
    
    :example: response = client.create_virtual_router(
        clientToken='string',
        meshName='string',
        spec={
            'serviceNames': [
                'string',
            ]
        },
        virtualRouterName='string'
    )
    
    
    :type clientToken: string
    :param clientToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.
            This field is autopopulated if not provided.
            

    :type meshName: string
    :param meshName: [REQUIRED]
            The name of the service mesh in which to create the virtual router.
            

    :type spec: dict
    :param spec: [REQUIRED]
            The virtual router specification to apply.
            serviceNames (list) --The service mesh service names to associate with the virtual router.
            (string) --
            

    :type virtualRouterName: string
    :param virtualRouterName: [REQUIRED]
            The name to use for the virtual router.
            

    :rtype: dict
    :return: {
        'virtualRouter': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'uid': 'string',
                'version': 123
            },
            'spec': {
                'serviceNames': [
                    'string',
                ]
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualRouterName': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_mesh(meshName=None):
    """
    Deletes an existing service mesh.
    You must delete all resources (routes, virtual routers, virtual nodes) in the service mesh before you can delete the mesh itself.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_mesh(
        meshName='string'
    )
    
    
    :type meshName: string
    :param meshName: [REQUIRED]
            The name of the service mesh to delete.
            

    :rtype: dict
    :return: {
        'mesh': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'uid': 'string',
                'version': 123
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            }
        }
    }
    
    
    """
    pass

def delete_route(meshName=None, routeName=None, virtualRouterName=None):
    """
    Deletes an existing route.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_route(
        meshName='string',
        routeName='string',
        virtualRouterName='string'
    )
    
    
    :type meshName: string
    :param meshName: [REQUIRED]
            The name of the service mesh in which to delete the route.
            

    :type routeName: string
    :param routeName: [REQUIRED]
            The name of the route to delete.
            

    :type virtualRouterName: string
    :param virtualRouterName: [REQUIRED]
            The name of the virtual router in which to delete the route.
            

    :rtype: dict
    :return: {
        'route': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'uid': 'string',
                'version': 123
            },
            'routeName': 'string',
            'spec': {
                'httpRoute': {
                    'action': {
                        'weightedTargets': [
                            {
                                'virtualNode': 'string',
                                'weight': 123
                            },
                        ]
                    },
                    'match': {
                        'prefix': 'string'
                    }
                }
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualRouterName': 'string'
        }
    }
    
    
    """
    pass

def delete_virtual_node(meshName=None, virtualNodeName=None):
    """
    Deletes an existing virtual node.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_virtual_node(
        meshName='string',
        virtualNodeName='string'
    )
    
    
    :type meshName: string
    :param meshName: [REQUIRED]
            The name of the service mesh in which to delete the virtual node.
            

    :type virtualNodeName: string
    :param virtualNodeName: [REQUIRED]
            The name of the virtual node to delete.
            

    :rtype: dict
    :return: {
        'virtualNode': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'uid': 'string',
                'version': 123
            },
            'spec': {
                'backends': [
                    'string',
                ],
                'listeners': [
                    {
                        'healthCheck': {
                            'healthyThreshold': 123,
                            'intervalMillis': 123,
                            'path': 'string',
                            'port': 123,
                            'protocol': 'http'|'tcp',
                            'timeoutMillis': 123,
                            'unhealthyThreshold': 123
                        },
                        'portMapping': {
                            'port': 123,
                            'protocol': 'http'|'tcp'
                        }
                    },
                ],
                'serviceDiscovery': {
                    'dns': {
                        'serviceName': 'string'
                    }
                }
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualNodeName': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_virtual_router(meshName=None, virtualRouterName=None):
    """
    Deletes an existing virtual router.
    You must delete any routes associated with the virtual router before you can delete the router itself.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_virtual_router(
        meshName='string',
        virtualRouterName='string'
    )
    
    
    :type meshName: string
    :param meshName: [REQUIRED]
            The name of the service mesh in which to delete the virtual router.
            

    :type virtualRouterName: string
    :param virtualRouterName: [REQUIRED]
            The name of the virtual router to delete.
            

    :rtype: dict
    :return: {
        'virtualRouter': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'uid': 'string',
                'version': 123
            },
            'spec': {
                'serviceNames': [
                    'string',
                ]
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualRouterName': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_mesh(meshName=None):
    """
    Describes an existing cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_mesh(
        meshName='string'
    )
    
    
    :type meshName: string
    :param meshName: [REQUIRED]
            The name of the service mesh to describe.
            

    :rtype: dict
    :return: {
        'mesh': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'uid': 'string',
                'version': 123
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            }
        }
    }
    
    
    """
    pass

def describe_route(meshName=None, routeName=None, virtualRouterName=None):
    """
    Describes an existing route.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_route(
        meshName='string',
        routeName='string',
        virtualRouterName='string'
    )
    
    
    :type meshName: string
    :param meshName: [REQUIRED]
            The name of the service mesh in which the route resides.
            

    :type routeName: string
    :param routeName: [REQUIRED]
            The name of the route to describe.
            

    :type virtualRouterName: string
    :param virtualRouterName: [REQUIRED]
            The name of the virtual router with which the route is associated.
            

    :rtype: dict
    :return: {
        'route': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'uid': 'string',
                'version': 123
            },
            'routeName': 'string',
            'spec': {
                'httpRoute': {
                    'action': {
                        'weightedTargets': [
                            {
                                'virtualNode': 'string',
                                'weight': 123
                            },
                        ]
                    },
                    'match': {
                        'prefix': 'string'
                    }
                }
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualRouterName': 'string'
        }
    }
    
    
    """
    pass

def describe_virtual_node(meshName=None, virtualNodeName=None):
    """
    Describes an existing virtual node.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_virtual_node(
        meshName='string',
        virtualNodeName='string'
    )
    
    
    :type meshName: string
    :param meshName: [REQUIRED]
            The name of the service mesh in which the virtual node resides.
            

    :type virtualNodeName: string
    :param virtualNodeName: [REQUIRED]
            The name of the virtual node to describe.
            

    :rtype: dict
    :return: {
        'virtualNode': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'uid': 'string',
                'version': 123
            },
            'spec': {
                'backends': [
                    'string',
                ],
                'listeners': [
                    {
                        'healthCheck': {
                            'healthyThreshold': 123,
                            'intervalMillis': 123,
                            'path': 'string',
                            'port': 123,
                            'protocol': 'http'|'tcp',
                            'timeoutMillis': 123,
                            'unhealthyThreshold': 123
                        },
                        'portMapping': {
                            'port': 123,
                            'protocol': 'http'|'tcp'
                        }
                    },
                ],
                'serviceDiscovery': {
                    'dns': {
                        'serviceName': 'string'
                    }
                }
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualNodeName': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_virtual_router(meshName=None, virtualRouterName=None):
    """
    Describes an existing virtual router.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_virtual_router(
        meshName='string',
        virtualRouterName='string'
    )
    
    
    :type meshName: string
    :param meshName: [REQUIRED]
            The name of the service mesh in which the virtual router resides.
            

    :type virtualRouterName: string
    :param virtualRouterName: [REQUIRED]
            The name of the virtual router to describe.
            

    :rtype: dict
    :return: {
        'virtualRouter': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'uid': 'string',
                'version': 123
            },
            'spec': {
                'serviceNames': [
                    'string',
                ]
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualRouterName': 'string'
        }
    }
    
    
    :returns: 
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

def list_meshes(limit=None, nextToken=None):
    """
    Returns a list of existing service meshes.
    See also: AWS API Documentation
    
    
    :example: response = client.list_meshes(
        limit=123,
        nextToken='string'
    )
    
    
    :type limit: integer
    :param limit: The maximum number of mesh results returned by ListMeshes in paginated output. When this parameter is used, ListMeshes only returns limit results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListMeshes request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListMeshes returns up to 100 results and a nextToken value if applicable.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListMeshes request where limit was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            

    :rtype: dict
    :return: {
        'meshes': [
            {
                'arn': 'string',
                'meshName': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_routes(limit=None, meshName=None, nextToken=None, virtualRouterName=None):
    """
    Returns a list of existing routes in a service mesh.
    See also: AWS API Documentation
    
    
    :example: response = client.list_routes(
        limit=123,
        meshName='string',
        nextToken='string',
        virtualRouterName='string'
    )
    
    
    :type limit: integer
    :param limit: The maximum number of mesh results returned by ListRoutes in paginated output. When this parameter is used, ListRoutes only returns limit results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListRoutes request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListRoutes returns up to 100 results and a nextToken value if applicable.

    :type meshName: string
    :param meshName: [REQUIRED]
            The name of the service mesh in which to list routes.
            

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListRoutes request where limit was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.

    :type virtualRouterName: string
    :param virtualRouterName: [REQUIRED]
            The name of the virtual router in which to list routes.
            

    :rtype: dict
    :return: {
        'nextToken': 'string',
        'routes': [
            {
                'arn': 'string',
                'meshName': 'string',
                'routeName': 'string',
                'virtualRouterName': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_virtual_nodes(limit=None, meshName=None, nextToken=None):
    """
    Returns a list of existing virtual nodes.
    See also: AWS API Documentation
    
    
    :example: response = client.list_virtual_nodes(
        limit=123,
        meshName='string',
        nextToken='string'
    )
    
    
    :type limit: integer
    :param limit: The maximum number of mesh results returned by ListVirtualNodes in paginated output. When this parameter is used, ListVirtualNodes only returns limit results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListVirtualNodes request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListVirtualNodes returns up to 100 results and a nextToken value if applicable.

    :type meshName: string
    :param meshName: [REQUIRED]
            The name of the service mesh in which to list virtual nodes.
            

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListVirtualNodes request where limit was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.

    :rtype: dict
    :return: {
        'nextToken': 'string',
        'virtualNodes': [
            {
                'arn': 'string',
                'meshName': 'string',
                'virtualNodeName': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_virtual_routers(limit=None, meshName=None, nextToken=None):
    """
    Returns a list of existing virtual routers in a service mesh.
    See also: AWS API Documentation
    
    
    :example: response = client.list_virtual_routers(
        limit=123,
        meshName='string',
        nextToken='string'
    )
    
    
    :type limit: integer
    :param limit: The maximum number of mesh results returned by ListVirtualRouters in paginated output. When this parameter is used, ListVirtualRouters only returns limit results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListVirtualRouters request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListVirtualRouters returns up to 100 results and a nextToken value if applicable.

    :type meshName: string
    :param meshName: [REQUIRED]
            The name of the service mesh in which to list virtual routers.
            

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListVirtualRouters request where limit was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.

    :rtype: dict
    :return: {
        'nextToken': 'string',
        'virtualRouters': [
            {
                'arn': 'string',
                'meshName': 'string',
                'virtualRouterName': 'string'
            },
        ]
    }
    
    
    """
    pass

def update_route(clientToken=None, meshName=None, routeName=None, spec=None, virtualRouterName=None):
    """
    Updates an existing route for a specified service mesh and virtual router.
    See also: AWS API Documentation
    
    
    :example: response = client.update_route(
        clientToken='string',
        meshName='string',
        routeName='string',
        spec={
            'httpRoute': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                },
                'match': {
                    'prefix': 'string'
                }
            }
        },
        virtualRouterName='string'
    )
    
    
    :type clientToken: string
    :param clientToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.
            This field is autopopulated if not provided.
            

    :type meshName: string
    :param meshName: [REQUIRED]
            The name of the service mesh in which the route resides.
            

    :type routeName: string
    :param routeName: [REQUIRED]
            The name of the route to update.
            

    :type spec: dict
    :param spec: [REQUIRED]
            The new route specification to apply. This overwrites the existing data.
            httpRoute (dict) --The HTTP routing information for the route.
            action (dict) --The action to take if a match is determined.
            weightedTargets (list) --The targets that traffic is routed to when a request matches the route. You can specify one or more targets and their relative weights with which to distribute traffic.
            (dict) --An object representing a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10.
            virtualNode (string) --The virtual node to associate with the weighted target.
            weight (integer) --The relative weight of the weighted target.
            
            match (dict) --The criteria for determining an HTTP request match.
            prefix (string) --Specifies the path with which to match requests. This parameter must always start with / , which by itself matches all requests to the virtual router service name. You can also match for path-based routing of requests. For example, if your virtual router service name is my-service.local , and you want the route to match requests to my-service.local/metrics , then your prefix should be /metrics .
            
            

    :type virtualRouterName: string
    :param virtualRouterName: [REQUIRED]
            The name of the virtual router with which the route is associated.
            

    :rtype: dict
    :return: {
        'route': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'uid': 'string',
                'version': 123
            },
            'routeName': 'string',
            'spec': {
                'httpRoute': {
                    'action': {
                        'weightedTargets': [
                            {
                                'virtualNode': 'string',
                                'weight': 123
                            },
                        ]
                    },
                    'match': {
                        'prefix': 'string'
                    }
                }
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualRouterName': 'string'
        }
    }
    
    
    """
    pass

def update_virtual_node(clientToken=None, meshName=None, spec=None, virtualNodeName=None):
    """
    Updates an existing virtual node in a specified service mesh.
    See also: AWS API Documentation
    
    
    :example: response = client.update_virtual_node(
        clientToken='string',
        meshName='string',
        spec={
            'backends': [
                'string',
            ],
            'listeners': [
                {
                    'healthCheck': {
                        'healthyThreshold': 123,
                        'intervalMillis': 123,
                        'path': 'string',
                        'port': 123,
                        'protocol': 'http'|'tcp',
                        'timeoutMillis': 123,
                        'unhealthyThreshold': 123
                    },
                    'portMapping': {
                        'port': 123,
                        'protocol': 'http'|'tcp'
                    }
                },
            ],
            'serviceDiscovery': {
                'dns': {
                    'serviceName': 'string'
                }
            }
        },
        virtualNodeName='string'
    )
    
    
    :type clientToken: string
    :param clientToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.
            This field is autopopulated if not provided.
            

    :type meshName: string
    :param meshName: [REQUIRED]
            The name of the service mesh in which the virtual node resides.
            

    :type spec: dict
    :param spec: [REQUIRED]
            The new virtual node specification to apply. This overwrites the existing data.
            backends (list) --The backends to which the virtual node is expected to send outbound traffic.
            (string) --
            listeners (list) --The listeners from which the virtual node is expected to receive inbound traffic.
            (dict) --An object representing a listener for a virtual node.
            healthCheck (dict) --The health check information for the listener.
            Note
            Listener health checks are not available during the App Mesh preview.
            healthyThreshold (integer) --The number of consecutive successful health checks that must occur before declaring listener healthy.
            intervalMillis (integer) --The time period in milliseconds between each health check execution.
            path (string) --The destination path for the health check request.
            port (integer) --The destination port for the health check request.
            protocol (string) --The protocol for the health check request.
            timeoutMillis (integer) --The amount of time to wait when receiving a response from the health check, in milliseconds.
            unhealthyThreshold (integer) --The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy.
            portMapping (dict) --The port mapping information for the listener.
            port (integer) --The port used for the port mapping.
            protocol (string) --The protocol used for the port mapping.
            
            serviceDiscovery (dict) --The service discovery information for the virtual node.
            dns (dict) --Specifies the DNS service name for the virtual node.
            serviceName (string) --The DNS service name for your virtual node.
            
            

    :type virtualNodeName: string
    :param virtualNodeName: [REQUIRED]
            The name of the virtual node to update.
            

    :rtype: dict
    :return: {
        'virtualNode': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'uid': 'string',
                'version': 123
            },
            'spec': {
                'backends': [
                    'string',
                ],
                'listeners': [
                    {
                        'healthCheck': {
                            'healthyThreshold': 123,
                            'intervalMillis': 123,
                            'path': 'string',
                            'port': 123,
                            'protocol': 'http'|'tcp',
                            'timeoutMillis': 123,
                            'unhealthyThreshold': 123
                        },
                        'portMapping': {
                            'port': 123,
                            'protocol': 'http'|'tcp'
                        }
                    },
                ],
                'serviceDiscovery': {
                    'dns': {
                        'serviceName': 'string'
                    }
                }
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualNodeName': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_virtual_router(clientToken=None, meshName=None, spec=None, virtualRouterName=None):
    """
    Updates an existing virtual router in a specified service mesh.
    See also: AWS API Documentation
    
    
    :example: response = client.update_virtual_router(
        clientToken='string',
        meshName='string',
        spec={
            'serviceNames': [
                'string',
            ]
        },
        virtualRouterName='string'
    )
    
    
    :type clientToken: string
    :param clientToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.
            This field is autopopulated if not provided.
            

    :type meshName: string
    :param meshName: [REQUIRED]
            The name of the service mesh in which the virtual router resides.
            

    :type spec: dict
    :param spec: [REQUIRED]
            The new virtual router specification to apply. This overwrites the existing data.
            serviceNames (list) --The service mesh service names to associate with the virtual router.
            (string) --
            

    :type virtualRouterName: string
    :param virtualRouterName: [REQUIRED]
            The name of the virtual router to update.
            

    :rtype: dict
    :return: {
        'virtualRouter': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'uid': 'string',
                'version': 123
            },
            'spec': {
                'serviceNames': [
                    'string',
                ]
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualRouterName': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

