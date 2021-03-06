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

def create_cloud_front_origin_access_identity(CloudFrontOriginAccessIdentityConfig=None):
    """
    Creates a new origin access identity. If you're using Amazon S3 for your origin, you can use an origin access identity to require users to access your content using a CloudFront URL instead of the Amazon S3 URL. For more information about how to use origin access identities, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_cloud_front_origin_access_identity(
        CloudFrontOriginAccessIdentityConfig={
            'CallerReference': 'string',
            'Comment': 'string'
        }
    )
    
    
    :type CloudFrontOriginAccessIdentityConfig: dict
    :param CloudFrontOriginAccessIdentityConfig: [REQUIRED]
            The current configuration information for the identity.
            CallerReference (string) -- [REQUIRED]A unique value (for example, a date-time stamp) that ensures that the request can't be replayed.
            If the value of CallerReference is new (regardless of the content of the CloudFrontOriginAccessIdentityConfig object), a new origin access identity is created.
            If the CallerReference is a value already sent in a previous identity request, and the content of the CloudFrontOriginAccessIdentityConfig is identical to the original request (ignoring white space), the response includes the same information returned to the original request.
            If the CallerReference is a value you already sent in a previous request to create an identity, but the content of the CloudFrontOriginAccessIdentityConfig is different from the original request, CloudFront returns a CloudFrontOriginAccessIdentityAlreadyExists error.
            Comment (string) -- [REQUIRED]Any comments you want to include about the origin access identity.
            

    :rtype: dict
    :return: {
        'CloudFrontOriginAccessIdentity': {
            'Id': 'string',
            'S3CanonicalUserId': 'string',
            'CloudFrontOriginAccessIdentityConfig': {
                'CallerReference': 'string',
                'Comment': 'string'
            }
        },
        'Location': 'string',
        'ETag': 'string'
    }
    
    
    """
    pass

def create_distribution(DistributionConfig=None):
    """
    Creates a new web distribution. You create a CloudFront distribution to tell CloudFront where you want content to be delivered from, and the details about how to track and manage content delivery. Send a POST request to the /*CloudFront API version* /distribution /distribution ID resource.
    If you are using Adobe Flash Media Server's RTMP protocol, you set up a different kind of CloudFront distribution. For more information, see  CreateStreamingDistribution .
    See also: AWS API Documentation
    
    
    :example: response = client.create_distribution(
        DistributionConfig={
            'CallerReference': 'string',
            'Aliases': {
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'DefaultRootObject': 'string',
            'Origins': {
                'Quantity': 123,
                'Items': [
                    {
                        'Id': 'string',
                        'DomainName': 'string',
                        'OriginPath': 'string',
                        'CustomHeaders': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'HeaderName': 'string',
                                    'HeaderValue': 'string'
                                },
                            ]
                        },
                        'S3OriginConfig': {
                            'OriginAccessIdentity': 'string'
                        },
                        'CustomOriginConfig': {
                            'HTTPPort': 123,
                            'HTTPSPort': 123,
                            'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                            'OriginSslProtocols': {
                                'Quantity': 123,
                                'Items': [
                                    'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                                ]
                            },
                            'OriginReadTimeout': 123,
                            'OriginKeepaliveTimeout': 123
                        }
                    },
                ]
            },
            'OriginGroups': {
                'Quantity': 123,
                'Items': [
                    {
                        'Id': 'string',
                        'FailoverCriteria': {
                            'StatusCodes': {
                                'Quantity': 123,
                                'Items': [
                                    123,
                                ]
                            }
                        },
                        'Members': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'OriginId': 'string'
                                },
                            ]
                        }
                    },
                ]
            },
            'DefaultCacheBehavior': {
                'TargetOriginId': 'string',
                'ForwardedValues': {
                    'QueryString': True|False,
                    'Cookies': {
                        'Forward': 'none'|'whitelist'|'all',
                        'WhitelistedNames': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'Headers': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'QueryStringCacheKeys': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
                'TrustedSigners': {
                    'Enabled': True|False,
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                'MinTTL': 123,
                'AllowedMethods': {
                    'Quantity': 123,
                    'Items': [
                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                    ],
                    'CachedMethods': {
                        'Quantity': 123,
                        'Items': [
                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                        ]
                    }
                },
                'SmoothStreaming': True|False,
                'DefaultTTL': 123,
                'MaxTTL': 123,
                'Compress': True|False,
                'LambdaFunctionAssociations': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'LambdaFunctionARN': 'string',
                            'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                            'IncludeBody': True|False
                        },
                    ]
                },
                'FieldLevelEncryptionId': 'string'
            },
            'CacheBehaviors': {
                'Quantity': 123,
                'Items': [
                    {
                        'PathPattern': 'string',
                        'TargetOriginId': 'string',
                        'ForwardedValues': {
                            'QueryString': True|False,
                            'Cookies': {
                                'Forward': 'none'|'whitelist'|'all',
                                'WhitelistedNames': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                            'Headers': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            },
                            'QueryStringCacheKeys': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'TrustedSigners': {
                            'Enabled': True|False,
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                        'MinTTL': 123,
                        'AllowedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ],
                            'CachedMethods': {
                                'Quantity': 123,
                                'Items': [
                                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                ]
                            }
                        },
                        'SmoothStreaming': True|False,
                        'DefaultTTL': 123,
                        'MaxTTL': 123,
                        'Compress': True|False,
                        'LambdaFunctionAssociations': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'LambdaFunctionARN': 'string',
                                    'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                    'IncludeBody': True|False
                                },
                            ]
                        },
                        'FieldLevelEncryptionId': 'string'
                    },
                ]
            },
            'CustomErrorResponses': {
                'Quantity': 123,
                'Items': [
                    {
                        'ErrorCode': 123,
                        'ResponsePagePath': 'string',
                        'ResponseCode': 'string',
                        'ErrorCachingMinTTL': 123
                    },
                ]
            },
            'Comment': 'string',
            'Logging': {
                'Enabled': True|False,
                'IncludeCookies': True|False,
                'Bucket': 'string',
                'Prefix': 'string'
            },
            'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
            'Enabled': True|False,
            'ViewerCertificate': {
                'CloudFrontDefaultCertificate': True|False,
                'IAMCertificateId': 'string',
                'ACMCertificateArn': 'string',
                'SSLSupportMethod': 'sni-only'|'vip',
                'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
                'Certificate': 'string',
                'CertificateSource': 'cloudfront'|'iam'|'acm'
            },
            'Restrictions': {
                'GeoRestriction': {
                    'RestrictionType': 'blacklist'|'whitelist'|'none',
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                }
            },
            'WebACLId': 'string',
            'HttpVersion': 'http1.1'|'http2',
            'IsIPV6Enabled': True|False
        }
    )
    
    
    :type DistributionConfig: dict
    :param DistributionConfig: [REQUIRED]
            The distribution's configuration information.
            CallerReference (string) -- [REQUIRED]A unique value (for example, a date-time stamp) that ensures that the request can't be replayed.
            If the value of CallerReference is new (regardless of the content of the DistributionConfig object), CloudFront creates a new distribution.
            If CallerReference is a value that you already sent in a previous request to create a distribution, CloudFront returns a DistributionAlreadyExists error.
            Aliases (dict) --A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.
            Quantity (integer) -- [REQUIRED]The number of CNAME aliases, if any, that you want to associate with this distribution.
            Items (list) --A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.
            (string) --
            
            DefaultRootObject (string) --The object that you want CloudFront to request from your origin (for example, index.html ) when a viewer requests the root URL for your distribution (http://www.example.com ) instead of an object in your distribution (http://www.example.com/product-description.html ). Specifying a default root object avoids exposing the contents of your distribution.
            Specify only the object name, for example, index.html . Don't add a / before the object name.
            If you don't want to specify a default root object when you create a distribution, include an empty DefaultRootObject element.
            To delete the default root object from an existing distribution, update the distribution configuration and include an empty DefaultRootObject element.
            To replace the default root object, update the distribution configuration and specify the new object.
            For more information about the default root object, see Creating a Default Root Object in the Amazon CloudFront Developer Guide .
            Origins (dict) -- [REQUIRED]A complex type that contains information about origins for this distribution.
            Quantity (integer) -- [REQUIRED]The number of origins or origin groups for this distribution.
            Items (list) -- [REQUIRED]A complex type that contains origins or origin groups for this distribution.
            (dict) --A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web server), Amazon MediaStore, or other server from which CloudFront gets your files. This can also be an origin group, if you've created an origin group. You must specify at least one origin or origin group.
            For the current limit on the number of origins or origin groups that you can specify for a distribution, see Amazon CloudFront Limits in the AWS General Reference .
            Id (string) -- [REQUIRED]A unique identifier for the origin or origin group. The value of Id must be unique within the distribution.
            When you specify the value of TargetOriginId for the default cache behavior or for another cache behavior, you indicate the origin to which you want the cache behavior to route requests by specifying the value of the Id element for that origin. When a request matches the path pattern for that cache behavior, CloudFront routes the request to the specified origin. For more information, see Cache Behavior Settings in the Amazon CloudFront Developer Guide .
            DomainName (string) -- [REQUIRED]
            Amazon S3 origins : The DNS name of the Amazon S3 bucket from which you want CloudFront to get objects for this origin, for example, myawsbucket.s3.amazonaws.com . If you set up your bucket to be configured as a website endpoint, enter the Amazon S3 static website hosting endpoint for the bucket.
            For more information about specifying this value for different types of origins, see Origin Domain Name in the Amazon CloudFront Developer Guide .
            Constraints for Amazon S3 origins:
            If you configured Amazon S3 Transfer Acceleration for your bucket, don't specify the s3-accelerate endpoint for DomainName .
            The bucket name must be between 3 and 63 characters long (inclusive).
            The bucket name must contain only lowercase characters, numbers, periods, underscores, and dashes.
            The bucket name must not contain adjacent periods.
            Custom Origins : The DNS domain name for the HTTP server from which you want CloudFront to get objects for this origin, for example, www.example.com .
            Constraints for custom origins:
            DomainName must be a valid DNS name that contains only a-z, A-Z, 0-9, dot (.), hyphen (-), or underscore (_) characters.
            The name cannot exceed 128 characters.
            OriginPath (string) --An optional element that causes CloudFront to request your content from a directory in your Amazon S3 bucket or your custom origin. When you include the OriginPath element, specify the directory name, beginning with a / . CloudFront appends the directory name to the value of DomainName , for example, example.com/production . Do not include a / at the end of the directory name.
            For example, suppose you've specified the following values for your distribution:
            DomainName : An Amazon S3 bucket named myawsbucket .
            OriginPath : /production
            CNAME : example.com
            When a user enters example.com/index.html in a browser, CloudFront sends a request to Amazon S3 for myawsbucket/production/index.html .
            When a user enters example.com/acme/index.html in a browser, CloudFront sends a request to Amazon S3 for myawsbucket/production/acme/index.html .
            CustomHeaders (dict) --A complex type that contains names and values for the custom headers that you want.
            Quantity (integer) -- [REQUIRED]The number of custom headers, if any, for this distribution.
            Items (list) --
            Optional : A list that contains one OriginCustomHeader element for each custom header that you want CloudFront to forward to the origin. If Quantity is 0 , omit Items .
            (dict) --A complex type that contains HeaderName and HeaderValue elements, if any, for this distribution.
            HeaderName (string) -- [REQUIRED]The name of a header that you want CloudFront to forward to your origin. For more information, see Forwarding Custom Headers to Your Origin (Web Distributions Only) in the Amazon Amazon CloudFront Developer Guide .
            HeaderValue (string) -- [REQUIRED]The value for the header that you specified in the HeaderName field.
            
            S3OriginConfig (dict) --A complex type that contains information about the Amazon S3 origin. If the origin is a custom origin, use the CustomOriginConfig element instead.
            OriginAccessIdentity (string) -- [REQUIRED]The CloudFront origin access identity to associate with the origin. Use an origin access identity to configure the origin so that viewers can only access objects in an Amazon S3 bucket through CloudFront. The format of the value is:
            origin-access-identity/cloudfront/ID-of-origin-access-identity
            where `` ID-of-origin-access-identity `` is the value that CloudFront returned in the ID element when you created the origin access identity.
            If you want viewers to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element.
            To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element.
            To replace the origin access identity, update the distribution configuration and specify the new origin access identity.
            For more information about the origin access identity, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .
            CustomOriginConfig (dict) --A complex type that contains information about a custom origin. If the origin is an Amazon S3 bucket, use the S3OriginConfig element instead.
            HTTPPort (integer) -- [REQUIRED]The HTTP port the custom origin listens on.
            HTTPSPort (integer) -- [REQUIRED]The HTTPS port the custom origin listens on.
            OriginProtocolPolicy (string) -- [REQUIRED]The origin protocol policy to apply to your origin.
            OriginSslProtocols (dict) --The SSL/TLS protocols that you want CloudFront to use when communicating with your origin over HTTPS.
            Quantity (integer) -- [REQUIRED]The number of SSL/TLS protocols that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.
            Items (list) -- [REQUIRED]A list that contains allowed SSL/TLS protocols for this distribution.
            (string) --
            
            OriginReadTimeout (integer) --You can create a custom origin read timeout. All timeout units are in seconds. The default origin read timeout is 30 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 4 seconds; the maximum is 60 seconds.
            If you need to increase the maximum time limit, contact the AWS Support Center .
            OriginKeepaliveTimeout (integer) --You can create a custom keep-alive timeout. All timeout units are in seconds. The default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60 seconds.
            If you need to increase the maximum time limit, contact the AWS Support Center .
            
            
            OriginGroups (dict) --A complex type that contains information about origin groups for this distribution.
            Quantity (integer) -- [REQUIRED]The number of origin groups.
            Items (list) --The items (origin groups) in a distribution.
            (dict) --An origin group includes two origins (a primary origin and a second origin to failover to) and a failover criteria that you specify. You create an origin group to support origin failover in CloudFront. When you create or update a distribution, you can specifiy the origin group instead of a single origin, and CloudFront will failover from the primary origin to the second origin under the failover conditions that you've chosen.
            Id (string) -- [REQUIRED]The origin group's ID.
            FailoverCriteria (dict) -- [REQUIRED]A complex type that contains information about the failover criteria for an origin group.
            StatusCodes (dict) -- [REQUIRED]The status codes that, when returned from the primary origin, will trigger CloudFront to failover to the second origin.
            Quantity (integer) -- [REQUIRED]The number of status codes.
            Items (list) -- [REQUIRED]The items (status codes) for an origin group.
            (integer) --
            
            Members (dict) -- [REQUIRED]A complex type that contains information about the origins in an origin group.
            Quantity (integer) -- [REQUIRED]The number of origins in an origin group.
            Items (list) -- [REQUIRED]Items (origins) in an origin group.
            (dict) --An origin in an origin group.
            OriginId (string) -- [REQUIRED]The ID for an origin in an origin group.
            
            
            
            DefaultCacheBehavior (dict) -- [REQUIRED]A complex type that describes the default cache behavior if you don't specify a CacheBehavior element or if files don't match any of the values of PathPattern in CacheBehavior elements. You must create exactly one default cache behavior.
            TargetOriginId (string) -- [REQUIRED]The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.
            ForwardedValues (dict) -- [REQUIRED]A complex type that specifies how CloudFront handles query strings and cookies.
            QueryString (boolean) -- [REQUIRED]Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of QueryString and on the values that you specify for QueryStringCacheKeys , if any:
            If you specify true for QueryString and you don't specify any values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.
            If you specify true for QueryString and you specify one or more values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.
            If you specify false for QueryString , CloudFront doesn't forward any query string parameters to the origin, and doesn't cache based on query string parameters.
            For more information, see Configuring CloudFront to Cache Based on Query String Parameters in the Amazon CloudFront Developer Guide .
            Cookies (dict) -- [REQUIRED]A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see How CloudFront Forwards, Caches, and Logs Cookies in the Amazon CloudFront Developer Guide .
            Forward (string) -- [REQUIRED]Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the WhitelistedNames complex type.
            Amazon S3 doesn't process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the Forward element.
            WhitelistedNames (dict) --Required if you specify whitelist for the value of Forward: . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.
            If you specify all or none for the value of Forward , omit WhitelistedNames . If you change the value of Forward from whitelist to all or none and you don't delete the WhitelistedNames element and its child elements, CloudFront deletes them automatically.
            For the current limit on the number of cookie names that you can whitelist for each cache behavior, see Amazon CloudFront Limits in the AWS General Reference .
            Quantity (integer) -- [REQUIRED]The number of different cookies that you want CloudFront to forward to the origin for this cache behavior.
            Items (list) --A complex type that contains one Name element for each cookie that you want CloudFront to forward to the origin for this cache behavior.
            (string) --
            
            Headers (dict) --A complex type that specifies the Headers , if any, that you want CloudFront to base caching on for this cache behavior.
            Quantity (integer) -- [REQUIRED]The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:
            Forward all headers to your origin : Specify 1 for Quantity and * for Name .
            Warning
            CloudFront doesn't cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.
            Forward a whitelist of headers you specify : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in Name elements. CloudFront caches your objects based on the values in the specified headers.
            Forward only the default headers : Specify 0 for Quantity and omit Items . In this configuration, CloudFront doesn't cache based on the values in the request headers.
            Regardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:
            S3 bucket : See HTTP Request Headers That CloudFront Removes or Updates
            Custom origin : See HTTP Request Headers and CloudFront Behavior
            Items (list) --A list that contains one Name element for each header that you want CloudFront to use for caching in this cache behavior. If Quantity is 0 , omit Items .
            (string) --
            
            QueryStringCacheKeys (dict) --A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.
            Quantity (integer) -- [REQUIRED]The number of whitelisted query string parameters for this cache behavior.
            Items (list) --(Optional) A list that contains the query string parameters that you want CloudFront to use as a basis for caching for this cache behavior. If Quantity is 0, you can omit Items .
            (string) --
            
            TrustedSigners (dict) -- [REQUIRED]A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.
            If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items . For more information, see Serving Private Content through CloudFront in the Amazon Amazon CloudFront Developer Guide .
            If you don't want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items .
            To add, change, or remove one or more trusted signers, change Enabled to true (if it's currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
            Enabled (boolean) -- [REQUIRED]Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .
            Quantity (integer) -- [REQUIRED]The number of trusted signers for this cache behavior.
            Items (list) --
            Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .
            (string) --
            
            ViewerProtocolPolicy (string) -- [REQUIRED]The protocol that viewers can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern . You can specify the following options:
            allow-all : Viewers can use HTTP or HTTPS.
            redirect-to-https : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.
            https-only : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).
            For more information about requiring the HTTPS protocol, see Using an HTTPS Connection to Access Your Objects in the Amazon CloudFront Developer Guide .
            Note
            The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
            MinTTL (integer) -- [REQUIRED]The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) in the Amazon Amazon CloudFront Developer Guide .
            You must specify 0 for MinTTL if you configure CloudFront to forward all headers to your origin (under Headers , if you specify 1 for Quantity and * for Name ).
            AllowedMethods (dict) --A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:
            CloudFront forwards only GET and HEAD requests.
            CloudFront forwards only GET , HEAD , and OPTIONS requests.
            CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests.
            If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can't perform operations that you don't want them to. For example, you might not want users to have permissions to delete objects from your origin.
            Quantity (integer) -- [REQUIRED]The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET , HEAD , and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests).
            Items (list) -- [REQUIRED]A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.
            (string) --
            CachedMethods (dict) --A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:
            CloudFront caches responses to GET and HEAD requests.
            CloudFront caches responses to GET , HEAD , and OPTIONS requests.
            If you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.
            Quantity (integer) -- [REQUIRED]The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET , HEAD , and OPTIONS requests).
            Items (list) -- [REQUIRED]A complex type that contains the HTTP methods that you want CloudFront to cache responses to.
            (string) --
            
            SmoothStreaming (boolean) --Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true ; if not, specify false . If you specify true for SmoothStreaming , you can still distribute other content using this cache behavior if the content matches the value of PathPattern .
            DefaultTTL (integer) --The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
            MaxTTL (integer) --
            Compress (boolean) --Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true ; if not, specify false . For more information, see Serving Compressed Files in the Amazon CloudFront Developer Guide .
            LambdaFunctionAssociations (dict) --A complex type that contains zero or more Lambda function associations for a cache behavior.
            Quantity (integer) -- [REQUIRED]The number of Lambda function associations for this cache behavior.
            Items (list) --
            Optional : A complex type that contains LambdaFunctionAssociation items for this cache behavior. If Quantity is 0 , you can omit Items .
            (dict) --A complex type that contains a Lambda function association.
            LambdaFunctionARN (string) -- [REQUIRED]The ARN of the Lambda function. You must specify the ARN of a function version; you can't specify a Lambda alias or $LATEST.
            EventType (string) -- [REQUIRED]Specifies the event type that triggers a Lambda function invocation. You can specify the following values:
            viewer-request : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.
            origin-request : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn't execute.
            origin-response : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn't execute.
            viewer-response : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn't execute.
            IncludeBody (boolean) --A flag that allows a Lambda function to have read access to the body content. For more information, see Accessing the Request Body by Choosing the Include Body Option in the Amazon CloudFront Developer Guide.
            
            FieldLevelEncryptionId (string) --The value of ID for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.
            CacheBehaviors (dict) --A complex type that contains zero or more CacheBehavior elements.
            Quantity (integer) -- [REQUIRED]The number of cache behaviors for this distribution.
            Items (list) --Optional: A complex type that contains cache behaviors for this distribution. If Quantity is 0 , you can omit Items .
            (dict) --A complex type that describes how CloudFront processes requests.
            You must create at least as many cache behaviors (including the default cache behavior) as you have origins if you want CloudFront to distribute objects from all of the origins. Each cache behavior specifies the one origin from which you want CloudFront to get objects. If you have two origins and only the default cache behavior, the default cache behavior will cause CloudFront to get objects from one of the origins, but the other origin is never used.
            For the current limit on the number of cache behaviors that you can add to a distribution, see Amazon CloudFront Limits in the AWS General Reference .
            If you don't want to specify any cache behaviors, include only an empty CacheBehaviors element. Don't include an empty CacheBehavior element, or CloudFront returns a MalformedXML error.
            To delete all cache behaviors in an existing distribution, update the distribution configuration and include only an empty CacheBehaviors element.
            To add, change, or remove one or more cache behaviors, update the distribution configuration and specify all of the cache behaviors that you want to include in the updated distribution.
            For more information about cache behaviors, see Cache Behaviors in the Amazon CloudFront Developer Guide .
            PathPattern (string) -- [REQUIRED]The pattern (for example, images/*.jpg ) that specifies which requests to apply the behavior to. When CloudFront receives a viewer request, the requested path is compared with path patterns in the order in which cache behaviors are listed in the distribution.
            Note
            You can optionally include a slash (/ ) at the beginning of the path pattern. For example, /images/*.jpg . CloudFront behavior is the same with or without the leading / .
            The path pattern for the default cache behavior is * and cannot be changed. If the request for an object does not match the path pattern for any cache behaviors, CloudFront applies the behavior in the default cache behavior.
            For more information, see Path Pattern in the Amazon CloudFront Developer Guide .
            TargetOriginId (string) -- [REQUIRED]The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.
            ForwardedValues (dict) -- [REQUIRED]A complex type that specifies how CloudFront handles query strings and cookies.
            QueryString (boolean) -- [REQUIRED]Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of QueryString and on the values that you specify for QueryStringCacheKeys , if any:
            If you specify true for QueryString and you don't specify any values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.
            If you specify true for QueryString and you specify one or more values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.
            If you specify false for QueryString , CloudFront doesn't forward any query string parameters to the origin, and doesn't cache based on query string parameters.
            For more information, see Configuring CloudFront to Cache Based on Query String Parameters in the Amazon CloudFront Developer Guide .
            Cookies (dict) -- [REQUIRED]A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see How CloudFront Forwards, Caches, and Logs Cookies in the Amazon CloudFront Developer Guide .
            Forward (string) -- [REQUIRED]Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the WhitelistedNames complex type.
            Amazon S3 doesn't process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the Forward element.
            WhitelistedNames (dict) --Required if you specify whitelist for the value of Forward: . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.
            If you specify all or none for the value of Forward , omit WhitelistedNames . If you change the value of Forward from whitelist to all or none and you don't delete the WhitelistedNames element and its child elements, CloudFront deletes them automatically.
            For the current limit on the number of cookie names that you can whitelist for each cache behavior, see Amazon CloudFront Limits in the AWS General Reference .
            Quantity (integer) -- [REQUIRED]The number of different cookies that you want CloudFront to forward to the origin for this cache behavior.
            Items (list) --A complex type that contains one Name element for each cookie that you want CloudFront to forward to the origin for this cache behavior.
            (string) --
            
            Headers (dict) --A complex type that specifies the Headers , if any, that you want CloudFront to base caching on for this cache behavior.
            Quantity (integer) -- [REQUIRED]The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:
            Forward all headers to your origin : Specify 1 for Quantity and * for Name .
            Warning
            CloudFront doesn't cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.
            Forward a whitelist of headers you specify : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in Name elements. CloudFront caches your objects based on the values in the specified headers.
            Forward only the default headers : Specify 0 for Quantity and omit Items . In this configuration, CloudFront doesn't cache based on the values in the request headers.
            Regardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:
            S3 bucket : See HTTP Request Headers That CloudFront Removes or Updates
            Custom origin : See HTTP Request Headers and CloudFront Behavior
            Items (list) --A list that contains one Name element for each header that you want CloudFront to use for caching in this cache behavior. If Quantity is 0 , omit Items .
            (string) --
            
            QueryStringCacheKeys (dict) --A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.
            Quantity (integer) -- [REQUIRED]The number of whitelisted query string parameters for this cache behavior.
            Items (list) --(Optional) A list that contains the query string parameters that you want CloudFront to use as a basis for caching for this cache behavior. If Quantity is 0, you can omit Items .
            (string) --
            
            TrustedSigners (dict) -- [REQUIRED]A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.
            If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items . For more information, see Serving Private Content through CloudFront in the Amazon Amazon CloudFront Developer Guide .
            If you don't want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items .
            To add, change, or remove one or more trusted signers, change Enabled to true (if it's currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
            Enabled (boolean) -- [REQUIRED]Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .
            Quantity (integer) -- [REQUIRED]The number of trusted signers for this cache behavior.
            Items (list) --
            Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .
            (string) --
            
            ViewerProtocolPolicy (string) -- [REQUIRED]The protocol that viewers can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern . You can specify the following options:
            allow-all : Viewers can use HTTP or HTTPS.
            redirect-to-https : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.
            https-only : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).
            For more information about requiring the HTTPS protocol, see Using an HTTPS Connection to Access Your Objects in the Amazon CloudFront Developer Guide .
            Note
            The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
            MinTTL (integer) -- [REQUIRED]The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) in the Amazon Amazon CloudFront Developer Guide .
            You must specify 0 for MinTTL if you configure CloudFront to forward all headers to your origin (under Headers , if you specify 1 for Quantity and * for Name ).
            AllowedMethods (dict) --A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:
            CloudFront forwards only GET and HEAD requests.
            CloudFront forwards only GET , HEAD , and OPTIONS requests.
            CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests.
            If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can't perform operations that you don't want them to. For example, you might not want users to have permissions to delete objects from your origin.
            Quantity (integer) -- [REQUIRED]The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET , HEAD , and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests).
            Items (list) -- [REQUIRED]A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.
            (string) --
            CachedMethods (dict) --A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:
            CloudFront caches responses to GET and HEAD requests.
            CloudFront caches responses to GET , HEAD , and OPTIONS requests.
            If you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.
            Quantity (integer) -- [REQUIRED]The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET , HEAD , and OPTIONS requests).
            Items (list) -- [REQUIRED]A complex type that contains the HTTP methods that you want CloudFront to cache responses to.
            (string) --
            
            SmoothStreaming (boolean) --Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true ; if not, specify false . If you specify true for SmoothStreaming , you can still distribute other content using this cache behavior if the content matches the value of PathPattern .
            DefaultTTL (integer) --The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
            MaxTTL (integer) --The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
            Compress (boolean) --Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true; if not, specify false. For more information, see Serving Compressed Files in the Amazon CloudFront Developer Guide .
            LambdaFunctionAssociations (dict) --A complex type that contains zero or more Lambda function associations for a cache behavior.
            Quantity (integer) -- [REQUIRED]The number of Lambda function associations for this cache behavior.
            Items (list) --
            Optional : A complex type that contains LambdaFunctionAssociation items for this cache behavior. If Quantity is 0 , you can omit Items .
            (dict) --A complex type that contains a Lambda function association.
            LambdaFunctionARN (string) -- [REQUIRED]The ARN of the Lambda function. You must specify the ARN of a function version; you can't specify a Lambda alias or $LATEST.
            EventType (string) -- [REQUIRED]Specifies the event type that triggers a Lambda function invocation. You can specify the following values:
            viewer-request : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.
            origin-request : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn't execute.
            origin-response : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn't execute.
            viewer-response : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn't execute.
            IncludeBody (boolean) --A flag that allows a Lambda function to have read access to the body content. For more information, see Accessing the Request Body by Choosing the Include Body Option in the Amazon CloudFront Developer Guide.
            
            FieldLevelEncryptionId (string) --The value of ID for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.
            
            CustomErrorResponses (dict) --A complex type that controls the following:
            Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.
            How long CloudFront caches HTTP status codes in the 4xx and 5xx range.
            For more information about custom error pages, see Customizing Error Responses in the Amazon CloudFront Developer Guide .
            Quantity (integer) -- [REQUIRED]The number of HTTP status codes for which you want to specify a custom error page and/or a caching duration. If Quantity is 0 , you can omit Items .
            Items (list) --A complex type that contains a CustomErrorResponse element for each HTTP status code for which you want to specify a custom error page and/or a caching duration.
            (dict) --A complex type that controls:
            Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.
            How long CloudFront caches HTTP status codes in the 4xx and 5xx range.
            For more information about custom error pages, see Customizing Error Responses in the Amazon CloudFront Developer Guide .
            ErrorCode (integer) -- [REQUIRED]The HTTP status code for which you want to specify a custom error page and/or a caching duration.
            ResponsePagePath (string) --The path to the custom error page that you want CloudFront to return to a viewer when your origin returns the HTTP status code specified by ErrorCode , for example, /4xx-errors/403-forbidden.html . If you want to store your objects and your custom error pages in different locations, your distribution must include a cache behavior for which the following is true:
            The value of PathPattern matches the path to your custom error messages. For example, suppose you saved custom error pages for 4xx errors in an Amazon S3 bucket in a directory named /4xx-errors . Your distribution must include a cache behavior for which the path pattern routes requests for your custom error pages to that location, for example, /4xx-errors/* .
            The value of TargetOriginId specifies the value of the ID element for the origin that contains your custom error pages.
            If you specify a value for ResponsePagePath , you must also specify a value for ResponseCode . If you don't want to specify a value, include an empty element, <ResponsePagePath> , in the XML document.
            We recommend that you store custom error pages in an Amazon S3 bucket. If you store custom error pages on an HTTP server and the server starts to return 5xx errors, CloudFront can't get the files that you want to return to viewers because the origin server is unavailable.
            ResponseCode (string) --The HTTP status code that you want CloudFront to return to the viewer along with the custom error page. There are a variety of reasons that you might want CloudFront to return a status code different from the status code that your origin returned to CloudFront, for example:
            Some Internet devices (some firewalls and corporate proxies, for example) intercept HTTP 4xx and 5xx and prevent the response from being returned to the viewer. If you substitute 200 , the response typically won't be intercepted.
            If you don't care about distinguishing among different client errors or server errors, you can specify 400 or 500 as the ResponseCode for all 4xx or 5xx errors.
            You might want to return a 200 status code (OK) and static website so your customers don't know that your website is down.
            If you specify a value for ResponseCode , you must also specify a value for ResponsePagePath . If you don't want to specify a value, include an empty element, <ResponseCode> , in the XML document.
            ErrorCachingMinTTL (integer) --The minimum amount of time, in seconds, that you want CloudFront to cache the HTTP status code specified in ErrorCode . When this time period has elapsed, CloudFront queries your origin to see whether the problem that caused the error has been resolved and the requested object is now available.
            If you don't want to specify a value, include an empty element, <ErrorCachingMinTTL> , in the XML document.
            For more information, see Customizing Error Responses in the Amazon CloudFront Developer Guide .
            
            Comment (string) -- [REQUIRED]Any comments you want to include about the distribution.
            If you don't want to specify a comment, include an empty Comment element.
            To delete an existing comment, update the distribution configuration and include an empty Comment element.
            To add or change a comment, update the distribution configuration and specify the new comment.
            Logging (dict) --A complex type that controls whether access logs are written for the distribution.
            For more information about logging, see Access Logs in the Amazon CloudFront Developer Guide .
            Enabled (boolean) -- [REQUIRED]Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you don't want to enable logging when you create a distribution or if you want to disable logging for an existing distribution, specify false for Enabled , and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket , prefix , and IncludeCookies , the values are automatically deleted.
            IncludeCookies (boolean) -- [REQUIRED]Specifies whether you want CloudFront to include cookies in access logs, specify true for IncludeCookies . If you choose to include cookies in logs, CloudFront logs all cookies regardless of how you configure the cache behaviors for this distribution. If you don't want to include cookies when you create a distribution or if you want to disable include cookies for an existing distribution, specify false for IncludeCookies .
            Bucket (string) -- [REQUIRED]The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com .
            Prefix (string) -- [REQUIRED]An optional string that you want CloudFront to prefix to the access log filenames for this distribution, for example, myprefix/ . If you want to enable logging, but you don't want to specify a prefix, you still must include an empty Prefix element in the Logging element.
            PriceClass (string) --The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All , CloudFront responds to requests for your objects from all CloudFront edge locations.
            If you specify a price class other than PriceClass_All , CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Viewers who are in or near regions that are excluded from your specified price class may encounter slower performance.
            For more information about price classes, see Choosing the Price Class for a CloudFront Distribution in the Amazon CloudFront Developer Guide . For information about CloudFront pricing, including how price classes (such as Price Class 100) map to CloudFront regions, see Amazon CloudFront Pricing . For price class information, scroll down to see the table at the bottom of the page.
            Enabled (boolean) -- [REQUIRED]From this field, you can enable or disable the selected distribution.
            ViewerCertificate (dict) --
            CloudFrontDefaultCertificate (boolean) --For information about how and when to use CloudFrontDefaultCertificate , see ViewerCertificate .
            IAMCertificateId (string) --For information about how and when to use IAMCertificateId , see ViewerCertificate .
            ACMCertificateArn (string) --For information about how and when to use ACMCertificateArn , see ViewerCertificate .
            SSLSupportMethod (string) --If you specify a value for ViewerCertificate$ACMCertificateArn or for ViewerCertificate$IAMCertificateId , you must also specify how you want CloudFront to serve HTTPS requests: using a method that works for all clients or one that works for most clients:
            vip : CloudFront uses dedicated IP addresses for your content and can respond to HTTPS requests from any viewer. However, you will incur additional monthly charges.
            sni-only : CloudFront can respond to HTTPS requests from viewers that support Server Name Indication (SNI). All modern browsers support SNI, but some browsers still in use don't support SNI. If some of your users' browsers don't support SNI, we recommend that you do one of the following:
            Use the vip option (dedicated IP addresses) instead of sni-only .
            Use the CloudFront SSL/TLS certificate instead of a custom certificate. This requires that you use the CloudFront domain name of your distribution in the URLs for your objects, for example, https://d111111abcdef8.cloudfront.net/logo.png .
            If you can control which browser your users use, upgrade the browser to one that supports SNI.
            Use HTTP instead of HTTPS.
            Don't specify a value for SSLSupportMethod if you specified <CloudFrontDefaultCertificate>true<CloudFrontDefaultCertificate> .
            For more information, see Using Alternate Domain Names and HTTPS in the Amazon CloudFront Developer Guide .
            MinimumProtocolVersion (string) --Specify the security policy that you want CloudFront to use for HTTPS connections. A security policy determines two settings:
            The minimum SSL/TLS protocol that CloudFront uses to communicate with viewers
            The cipher that CloudFront uses to encrypt the content that it returns to viewers
            Note
            On the CloudFront console, this setting is called Security policy .
            We recommend that you specify TLSv1.1_2016 unless your users are using browsers or devices that do not support TLSv1.1 or later.
            When both of the following are true, you must specify TLSv1 or later for the security policy:
            You're using a custom certificate: you specified a value for ACMCertificateArn or for IAMCertificateId
            You're using SNI: you specified sni-only for SSLSupportMethod
            If you specify true for CloudFrontDefaultCertificate , CloudFront automatically sets the security policy to TLSv1 regardless of the value that you specify for MinimumProtocolVersion .
            For information about the relationship between the security policy that you choose and the protocols and ciphers that CloudFront uses to communicate with viewers, see Supported SSL/TLS Protocols and Ciphers for Communication Between Viewers and CloudFront in the Amazon CloudFront Developer Guide .
            Certificate (string) --This field has been deprecated. Use one of the following fields instead:
            ViewerCertificate$ACMCertificateArn
            ViewerCertificate$IAMCertificateId
            ViewerCertificate$CloudFrontDefaultCertificate
            CertificateSource (string) --This field has been deprecated. Use one of the following fields instead:
            ViewerCertificate$ACMCertificateArn
            ViewerCertificate$IAMCertificateId
            ViewerCertificate$CloudFrontDefaultCertificate
            
            Restrictions (dict) --
            GeoRestriction (dict) -- [REQUIRED]A complex type that controls the countries in which your content is distributed. CloudFront determines the location of your users using MaxMind GeoIP databases.
            RestrictionType (string) -- [REQUIRED]The method that you want to use to restrict distribution of your content by country:
            none : No geo restriction is enabled, meaning access to content is not restricted by client geo location.
            blacklist : The Location elements specify the countries in which you don't want CloudFront to distribute your content.
            whitelist : The Location elements specify the countries in which you want CloudFront to distribute your content.
            Quantity (integer) -- [REQUIRED]When geo restriction is enabled , this is the number of countries in your whitelist or blacklist . Otherwise, when it is not enabled, Quantity is 0 , and you can omit Items .
            Items (list) --A complex type that contains a Location element for each country in which you want CloudFront either to distribute your content (whitelist ) or not distribute your content (blacklist ).
            The Location element is a two-letter, uppercase country code for a country that you want to include in your blacklist or whitelist . Include one Location element for each country.
            CloudFront and MaxMind both use ISO 3166 country codes. For the current list of countries and the corresponding codes, see ISO 3166-1-alpha-2 code on the International Organization for Standardization website. You can also refer to the country list on the CloudFront console, which includes both country names and codes.
            (string) --
            
            WebACLId (string) --A unique identifier that specifies the AWS WAF web ACL, if any, to associate with this distribution.
            AWS WAF is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to CloudFront, and lets you control access to your content. Based on conditions that you specify, such as the IP addresses that requests originate from or the values of query strings, CloudFront responds to requests either with the requested content or with an HTTP 403 status code (Forbidden). You can also configure CloudFront to return a custom error page when a request is blocked. For more information about AWS WAF, see the AWS WAF Developer Guide .
            HttpVersion (string) --(Optional) Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. The default value for new web distributions is http2. Viewers that don't support HTTP/2 automatically use an earlier HTTP version.
            For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support Server Name Identification (SNI).
            In general, configuring CloudFront to communicate with viewers using HTTP/2 reduces latency. You can improve performance by optimizing for HTTP/2. For more information, do an Internet search for 'http/2 optimization.'
            IsIPV6Enabled (boolean) --If you want CloudFront to respond to IPv6 DNS requests with an IPv6 address for your distribution, specify true . If you specify false , CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution.
            In general, you should enable IPv6 if you have users on IPv6 networks who want to access your content. However, if you're using signed URLs or signed cookies to restrict access to your content, and if you're using a custom policy that includes the IpAddress parameter to restrict the IP addresses that can access your content, don't enable IPv6. If you want to restrict access to some content by IP address and not restrict access to other content (or restrict access but not by IP address), you can create two distributions. For more information, see Creating a Signed URL Using a Custom Policy in the Amazon CloudFront Developer Guide .
            If you're using an Amazon Route 53 alias resource record set to route traffic to your CloudFront distribution, you need to create a second alias resource record set when both of the following are true:
            You enable IPv6 for the distribution
            You're using alternate domain names in the URLs for your objects
            For more information, see Routing Traffic to an Amazon CloudFront Web Distribution by Using Your Domain Name in the Amazon Route 53 Developer Guide .
            If you created a CNAME resource record set, either with Amazon Route 53 or with another DNS service, you don't need to make any changes. A CNAME record will route traffic to your distribution regardless of the IP address format of the viewer request.
            

    :rtype: dict
    :return: {
        'Distribution': {
            'Id': 'string',
            'ARN': 'string',
            'Status': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'InProgressInvalidationBatches': 123,
            'DomainName': 'string',
            'ActiveTrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    {
                        'AwsAccountNumber': 'string',
                        'KeyPairIds': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                ]
            },
            'DistributionConfig': {
                'CallerReference': 'string',
                'Aliases': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'DefaultRootObject': 'string',
                'Origins': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Id': 'string',
                            'DomainName': 'string',
                            'OriginPath': 'string',
                            'CustomHeaders': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'HeaderName': 'string',
                                        'HeaderValue': 'string'
                                    },
                                ]
                            },
                            'S3OriginConfig': {
                                'OriginAccessIdentity': 'string'
                            },
                            'CustomOriginConfig': {
                                'HTTPPort': 123,
                                'HTTPSPort': 123,
                                'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                                'OriginSslProtocols': {
                                    'Quantity': 123,
                                    'Items': [
                                        'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                                    ]
                                },
                                'OriginReadTimeout': 123,
                                'OriginKeepaliveTimeout': 123
                            }
                        },
                    ]
                },
                'OriginGroups': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Id': 'string',
                            'FailoverCriteria': {
                                'StatusCodes': {
                                    'Quantity': 123,
                                    'Items': [
                                        123,
                                    ]
                                }
                            },
                            'Members': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'OriginId': 'string'
                                    },
                                ]
                            }
                        },
                    ]
                },
                'DefaultCacheBehavior': {
                    'TargetOriginId': 'string',
                    'ForwardedValues': {
                        'QueryString': True|False,
                        'Cookies': {
                            'Forward': 'none'|'whitelist'|'all',
                            'WhitelistedNames': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'Headers': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'QueryStringCacheKeys': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'TrustedSigners': {
                        'Enabled': True|False,
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                    'MinTTL': 123,
                    'AllowedMethods': {
                        'Quantity': 123,
                        'Items': [
                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                        ],
                        'CachedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ]
                        }
                    },
                    'SmoothStreaming': True|False,
                    'DefaultTTL': 123,
                    'MaxTTL': 123,
                    'Compress': True|False,
                    'LambdaFunctionAssociations': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'LambdaFunctionARN': 'string',
                                'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                'IncludeBody': True|False
                            },
                        ]
                    },
                    'FieldLevelEncryptionId': 'string'
                },
                'CacheBehaviors': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'PathPattern': 'string',
                            'TargetOriginId': 'string',
                            'ForwardedValues': {
                                'QueryString': True|False,
                                'Cookies': {
                                    'Forward': 'none'|'whitelist'|'all',
                                    'WhitelistedNames': {
                                        'Quantity': 123,
                                        'Items': [
                                            'string',
                                        ]
                                    }
                                },
                                'Headers': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                },
                                'QueryStringCacheKeys': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                            'TrustedSigners': {
                                'Enabled': True|False,
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            },
                            'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                            'MinTTL': 123,
                            'AllowedMethods': {
                                'Quantity': 123,
                                'Items': [
                                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                ],
                                'CachedMethods': {
                                    'Quantity': 123,
                                    'Items': [
                                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                    ]
                                }
                            },
                            'SmoothStreaming': True|False,
                            'DefaultTTL': 123,
                            'MaxTTL': 123,
                            'Compress': True|False,
                            'LambdaFunctionAssociations': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'LambdaFunctionARN': 'string',
                                        'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                        'IncludeBody': True|False
                                    },
                                ]
                            },
                            'FieldLevelEncryptionId': 'string'
                        },
                    ]
                },
                'CustomErrorResponses': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'ErrorCode': 123,
                            'ResponsePagePath': 'string',
                            'ResponseCode': 'string',
                            'ErrorCachingMinTTL': 123
                        },
                    ]
                },
                'Comment': 'string',
                'Logging': {
                    'Enabled': True|False,
                    'IncludeCookies': True|False,
                    'Bucket': 'string',
                    'Prefix': 'string'
                },
                'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                'Enabled': True|False,
                'ViewerCertificate': {
                    'CloudFrontDefaultCertificate': True|False,
                    'IAMCertificateId': 'string',
                    'ACMCertificateArn': 'string',
                    'SSLSupportMethod': 'sni-only'|'vip',
                    'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
                    'Certificate': 'string',
                    'CertificateSource': 'cloudfront'|'iam'|'acm'
                },
                'Restrictions': {
                    'GeoRestriction': {
                        'RestrictionType': 'blacklist'|'whitelist'|'none',
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
                'WebACLId': 'string',
                'HttpVersion': 'http1.1'|'http2',
                'IsIPV6Enabled': True|False
            }
        },
        'Location': 'string',
        'ETag': 'string'
    }
    
    
    :returns: 
    If you configured Amazon S3 Transfer Acceleration for your bucket, don't specify the s3-accelerate endpoint for DomainName .
    The bucket name must be between 3 and 63 characters long (inclusive).
    The bucket name must contain only lowercase characters, numbers, periods, underscores, and dashes.
    The bucket name must not contain adjacent periods.
    
    """
    pass

def create_distribution_with_tags(DistributionConfigWithTags=None):
    """
    Create a new distribution with tags.
    See also: AWS API Documentation
    
    
    :example: response = client.create_distribution_with_tags(
        DistributionConfigWithTags={
            'DistributionConfig': {
                'CallerReference': 'string',
                'Aliases': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'DefaultRootObject': 'string',
                'Origins': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Id': 'string',
                            'DomainName': 'string',
                            'OriginPath': 'string',
                            'CustomHeaders': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'HeaderName': 'string',
                                        'HeaderValue': 'string'
                                    },
                                ]
                            },
                            'S3OriginConfig': {
                                'OriginAccessIdentity': 'string'
                            },
                            'CustomOriginConfig': {
                                'HTTPPort': 123,
                                'HTTPSPort': 123,
                                'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                                'OriginSslProtocols': {
                                    'Quantity': 123,
                                    'Items': [
                                        'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                                    ]
                                },
                                'OriginReadTimeout': 123,
                                'OriginKeepaliveTimeout': 123
                            }
                        },
                    ]
                },
                'OriginGroups': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Id': 'string',
                            'FailoverCriteria': {
                                'StatusCodes': {
                                    'Quantity': 123,
                                    'Items': [
                                        123,
                                    ]
                                }
                            },
                            'Members': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'OriginId': 'string'
                                    },
                                ]
                            }
                        },
                    ]
                },
                'DefaultCacheBehavior': {
                    'TargetOriginId': 'string',
                    'ForwardedValues': {
                        'QueryString': True|False,
                        'Cookies': {
                            'Forward': 'none'|'whitelist'|'all',
                            'WhitelistedNames': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'Headers': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'QueryStringCacheKeys': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'TrustedSigners': {
                        'Enabled': True|False,
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                    'MinTTL': 123,
                    'AllowedMethods': {
                        'Quantity': 123,
                        'Items': [
                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                        ],
                        'CachedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ]
                        }
                    },
                    'SmoothStreaming': True|False,
                    'DefaultTTL': 123,
                    'MaxTTL': 123,
                    'Compress': True|False,
                    'LambdaFunctionAssociations': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'LambdaFunctionARN': 'string',
                                'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                'IncludeBody': True|False
                            },
                        ]
                    },
                    'FieldLevelEncryptionId': 'string'
                },
                'CacheBehaviors': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'PathPattern': 'string',
                            'TargetOriginId': 'string',
                            'ForwardedValues': {
                                'QueryString': True|False,
                                'Cookies': {
                                    'Forward': 'none'|'whitelist'|'all',
                                    'WhitelistedNames': {
                                        'Quantity': 123,
                                        'Items': [
                                            'string',
                                        ]
                                    }
                                },
                                'Headers': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                },
                                'QueryStringCacheKeys': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                            'TrustedSigners': {
                                'Enabled': True|False,
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            },
                            'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                            'MinTTL': 123,
                            'AllowedMethods': {
                                'Quantity': 123,
                                'Items': [
                                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                ],
                                'CachedMethods': {
                                    'Quantity': 123,
                                    'Items': [
                                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                    ]
                                }
                            },
                            'SmoothStreaming': True|False,
                            'DefaultTTL': 123,
                            'MaxTTL': 123,
                            'Compress': True|False,
                            'LambdaFunctionAssociations': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'LambdaFunctionARN': 'string',
                                        'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                        'IncludeBody': True|False
                                    },
                                ]
                            },
                            'FieldLevelEncryptionId': 'string'
                        },
                    ]
                },
                'CustomErrorResponses': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'ErrorCode': 123,
                            'ResponsePagePath': 'string',
                            'ResponseCode': 'string',
                            'ErrorCachingMinTTL': 123
                        },
                    ]
                },
                'Comment': 'string',
                'Logging': {
                    'Enabled': True|False,
                    'IncludeCookies': True|False,
                    'Bucket': 'string',
                    'Prefix': 'string'
                },
                'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                'Enabled': True|False,
                'ViewerCertificate': {
                    'CloudFrontDefaultCertificate': True|False,
                    'IAMCertificateId': 'string',
                    'ACMCertificateArn': 'string',
                    'SSLSupportMethod': 'sni-only'|'vip',
                    'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
                    'Certificate': 'string',
                    'CertificateSource': 'cloudfront'|'iam'|'acm'
                },
                'Restrictions': {
                    'GeoRestriction': {
                        'RestrictionType': 'blacklist'|'whitelist'|'none',
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
                'WebACLId': 'string',
                'HttpVersion': 'http1.1'|'http2',
                'IsIPV6Enabled': True|False
            },
            'Tags': {
                'Items': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
        }
    )
    
    
    :type DistributionConfigWithTags: dict
    :param DistributionConfigWithTags: [REQUIRED]
            The distribution's configuration information.
            DistributionConfig (dict) -- [REQUIRED]A distribution configuration.
            CallerReference (string) -- [REQUIRED]A unique value (for example, a date-time stamp) that ensures that the request can't be replayed.
            If the value of CallerReference is new (regardless of the content of the DistributionConfig object), CloudFront creates a new distribution.
            If CallerReference is a value that you already sent in a previous request to create a distribution, CloudFront returns a DistributionAlreadyExists error.
            Aliases (dict) --A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.
            Quantity (integer) -- [REQUIRED]The number of CNAME aliases, if any, that you want to associate with this distribution.
            Items (list) --A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.
            (string) --
            
            DefaultRootObject (string) --The object that you want CloudFront to request from your origin (for example, index.html ) when a viewer requests the root URL for your distribution (http://www.example.com ) instead of an object in your distribution (http://www.example.com/product-description.html ). Specifying a default root object avoids exposing the contents of your distribution.
            Specify only the object name, for example, index.html . Don't add a / before the object name.
            If you don't want to specify a default root object when you create a distribution, include an empty DefaultRootObject element.
            To delete the default root object from an existing distribution, update the distribution configuration and include an empty DefaultRootObject element.
            To replace the default root object, update the distribution configuration and specify the new object.
            For more information about the default root object, see Creating a Default Root Object in the Amazon CloudFront Developer Guide .
            Origins (dict) -- [REQUIRED]A complex type that contains information about origins for this distribution.
            Quantity (integer) -- [REQUIRED]The number of origins or origin groups for this distribution.
            Items (list) -- [REQUIRED]A complex type that contains origins or origin groups for this distribution.
            (dict) --A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web server), Amazon MediaStore, or other server from which CloudFront gets your files. This can also be an origin group, if you've created an origin group. You must specify at least one origin or origin group.
            For the current limit on the number of origins or origin groups that you can specify for a distribution, see Amazon CloudFront Limits in the AWS General Reference .
            Id (string) -- [REQUIRED]A unique identifier for the origin or origin group. The value of Id must be unique within the distribution.
            When you specify the value of TargetOriginId for the default cache behavior or for another cache behavior, you indicate the origin to which you want the cache behavior to route requests by specifying the value of the Id element for that origin. When a request matches the path pattern for that cache behavior, CloudFront routes the request to the specified origin. For more information, see Cache Behavior Settings in the Amazon CloudFront Developer Guide .
            DomainName (string) -- [REQUIRED]
            Amazon S3 origins : The DNS name of the Amazon S3 bucket from which you want CloudFront to get objects for this origin, for example, myawsbucket.s3.amazonaws.com . If you set up your bucket to be configured as a website endpoint, enter the Amazon S3 static website hosting endpoint for the bucket.
            For more information about specifying this value for different types of origins, see Origin Domain Name in the Amazon CloudFront Developer Guide .
            Constraints for Amazon S3 origins:
            If you configured Amazon S3 Transfer Acceleration for your bucket, don't specify the s3-accelerate endpoint for DomainName .
            The bucket name must be between 3 and 63 characters long (inclusive).
            The bucket name must contain only lowercase characters, numbers, periods, underscores, and dashes.
            The bucket name must not contain adjacent periods.
            Custom Origins : The DNS domain name for the HTTP server from which you want CloudFront to get objects for this origin, for example, www.example.com .
            Constraints for custom origins:
            DomainName must be a valid DNS name that contains only a-z, A-Z, 0-9, dot (.), hyphen (-), or underscore (_) characters.
            The name cannot exceed 128 characters.
            OriginPath (string) --An optional element that causes CloudFront to request your content from a directory in your Amazon S3 bucket or your custom origin. When you include the OriginPath element, specify the directory name, beginning with a / . CloudFront appends the directory name to the value of DomainName , for example, example.com/production . Do not include a / at the end of the directory name.
            For example, suppose you've specified the following values for your distribution:
            DomainName : An Amazon S3 bucket named myawsbucket .
            OriginPath : /production
            CNAME : example.com
            When a user enters example.com/index.html in a browser, CloudFront sends a request to Amazon S3 for myawsbucket/production/index.html .
            When a user enters example.com/acme/index.html in a browser, CloudFront sends a request to Amazon S3 for myawsbucket/production/acme/index.html .
            CustomHeaders (dict) --A complex type that contains names and values for the custom headers that you want.
            Quantity (integer) -- [REQUIRED]The number of custom headers, if any, for this distribution.
            Items (list) --
            Optional : A list that contains one OriginCustomHeader element for each custom header that you want CloudFront to forward to the origin. If Quantity is 0 , omit Items .
            (dict) --A complex type that contains HeaderName and HeaderValue elements, if any, for this distribution.
            HeaderName (string) -- [REQUIRED]The name of a header that you want CloudFront to forward to your origin. For more information, see Forwarding Custom Headers to Your Origin (Web Distributions Only) in the Amazon Amazon CloudFront Developer Guide .
            HeaderValue (string) -- [REQUIRED]The value for the header that you specified in the HeaderName field.
            
            S3OriginConfig (dict) --A complex type that contains information about the Amazon S3 origin. If the origin is a custom origin, use the CustomOriginConfig element instead.
            OriginAccessIdentity (string) -- [REQUIRED]The CloudFront origin access identity to associate with the origin. Use an origin access identity to configure the origin so that viewers can only access objects in an Amazon S3 bucket through CloudFront. The format of the value is:
            origin-access-identity/cloudfront/ID-of-origin-access-identity
            where `` ID-of-origin-access-identity `` is the value that CloudFront returned in the ID element when you created the origin access identity.
            If you want viewers to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element.
            To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element.
            To replace the origin access identity, update the distribution configuration and specify the new origin access identity.
            For more information about the origin access identity, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .
            CustomOriginConfig (dict) --A complex type that contains information about a custom origin. If the origin is an Amazon S3 bucket, use the S3OriginConfig element instead.
            HTTPPort (integer) -- [REQUIRED]The HTTP port the custom origin listens on.
            HTTPSPort (integer) -- [REQUIRED]The HTTPS port the custom origin listens on.
            OriginProtocolPolicy (string) -- [REQUIRED]The origin protocol policy to apply to your origin.
            OriginSslProtocols (dict) --The SSL/TLS protocols that you want CloudFront to use when communicating with your origin over HTTPS.
            Quantity (integer) -- [REQUIRED]The number of SSL/TLS protocols that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.
            Items (list) -- [REQUIRED]A list that contains allowed SSL/TLS protocols for this distribution.
            (string) --
            
            OriginReadTimeout (integer) --You can create a custom origin read timeout. All timeout units are in seconds. The default origin read timeout is 30 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 4 seconds; the maximum is 60 seconds.
            If you need to increase the maximum time limit, contact the AWS Support Center .
            OriginKeepaliveTimeout (integer) --You can create a custom keep-alive timeout. All timeout units are in seconds. The default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60 seconds.
            If you need to increase the maximum time limit, contact the AWS Support Center .
            
            
            OriginGroups (dict) --A complex type that contains information about origin groups for this distribution.
            Quantity (integer) -- [REQUIRED]The number of origin groups.
            Items (list) --The items (origin groups) in a distribution.
            (dict) --An origin group includes two origins (a primary origin and a second origin to failover to) and a failover criteria that you specify. You create an origin group to support origin failover in CloudFront. When you create or update a distribution, you can specifiy the origin group instead of a single origin, and CloudFront will failover from the primary origin to the second origin under the failover conditions that you've chosen.
            Id (string) -- [REQUIRED]The origin group's ID.
            FailoverCriteria (dict) -- [REQUIRED]A complex type that contains information about the failover criteria for an origin group.
            StatusCodes (dict) -- [REQUIRED]The status codes that, when returned from the primary origin, will trigger CloudFront to failover to the second origin.
            Quantity (integer) -- [REQUIRED]The number of status codes.
            Items (list) -- [REQUIRED]The items (status codes) for an origin group.
            (integer) --
            
            Members (dict) -- [REQUIRED]A complex type that contains information about the origins in an origin group.
            Quantity (integer) -- [REQUIRED]The number of origins in an origin group.
            Items (list) -- [REQUIRED]Items (origins) in an origin group.
            (dict) --An origin in an origin group.
            OriginId (string) -- [REQUIRED]The ID for an origin in an origin group.
            
            
            
            DefaultCacheBehavior (dict) -- [REQUIRED]A complex type that describes the default cache behavior if you don't specify a CacheBehavior element or if files don't match any of the values of PathPattern in CacheBehavior elements. You must create exactly one default cache behavior.
            TargetOriginId (string) -- [REQUIRED]The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.
            ForwardedValues (dict) -- [REQUIRED]A complex type that specifies how CloudFront handles query strings and cookies.
            QueryString (boolean) -- [REQUIRED]Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of QueryString and on the values that you specify for QueryStringCacheKeys , if any:
            If you specify true for QueryString and you don't specify any values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.
            If you specify true for QueryString and you specify one or more values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.
            If you specify false for QueryString , CloudFront doesn't forward any query string parameters to the origin, and doesn't cache based on query string parameters.
            For more information, see Configuring CloudFront to Cache Based on Query String Parameters in the Amazon CloudFront Developer Guide .
            Cookies (dict) -- [REQUIRED]A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see How CloudFront Forwards, Caches, and Logs Cookies in the Amazon CloudFront Developer Guide .
            Forward (string) -- [REQUIRED]Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the WhitelistedNames complex type.
            Amazon S3 doesn't process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the Forward element.
            WhitelistedNames (dict) --Required if you specify whitelist for the value of Forward: . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.
            If you specify all or none for the value of Forward , omit WhitelistedNames . If you change the value of Forward from whitelist to all or none and you don't delete the WhitelistedNames element and its child elements, CloudFront deletes them automatically.
            For the current limit on the number of cookie names that you can whitelist for each cache behavior, see Amazon CloudFront Limits in the AWS General Reference .
            Quantity (integer) -- [REQUIRED]The number of different cookies that you want CloudFront to forward to the origin for this cache behavior.
            Items (list) --A complex type that contains one Name element for each cookie that you want CloudFront to forward to the origin for this cache behavior.
            (string) --
            
            Headers (dict) --A complex type that specifies the Headers , if any, that you want CloudFront to base caching on for this cache behavior.
            Quantity (integer) -- [REQUIRED]The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:
            Forward all headers to your origin : Specify 1 for Quantity and * for Name .
            Warning
            CloudFront doesn't cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.
            Forward a whitelist of headers you specify : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in Name elements. CloudFront caches your objects based on the values in the specified headers.
            Forward only the default headers : Specify 0 for Quantity and omit Items . In this configuration, CloudFront doesn't cache based on the values in the request headers.
            Regardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:
            S3 bucket : See HTTP Request Headers That CloudFront Removes or Updates
            Custom origin : See HTTP Request Headers and CloudFront Behavior
            Items (list) --A list that contains one Name element for each header that you want CloudFront to use for caching in this cache behavior. If Quantity is 0 , omit Items .
            (string) --
            
            QueryStringCacheKeys (dict) --A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.
            Quantity (integer) -- [REQUIRED]The number of whitelisted query string parameters for this cache behavior.
            Items (list) --(Optional) A list that contains the query string parameters that you want CloudFront to use as a basis for caching for this cache behavior. If Quantity is 0, you can omit Items .
            (string) --
            
            TrustedSigners (dict) -- [REQUIRED]A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.
            If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items . For more information, see Serving Private Content through CloudFront in the Amazon Amazon CloudFront Developer Guide .
            If you don't want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items .
            To add, change, or remove one or more trusted signers, change Enabled to true (if it's currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
            Enabled (boolean) -- [REQUIRED]Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .
            Quantity (integer) -- [REQUIRED]The number of trusted signers for this cache behavior.
            Items (list) --
            Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .
            (string) --
            
            ViewerProtocolPolicy (string) -- [REQUIRED]The protocol that viewers can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern . You can specify the following options:
            allow-all : Viewers can use HTTP or HTTPS.
            redirect-to-https : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.
            https-only : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).
            For more information about requiring the HTTPS protocol, see Using an HTTPS Connection to Access Your Objects in the Amazon CloudFront Developer Guide .
            Note
            The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
            MinTTL (integer) -- [REQUIRED]The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) in the Amazon Amazon CloudFront Developer Guide .
            You must specify 0 for MinTTL if you configure CloudFront to forward all headers to your origin (under Headers , if you specify 1 for Quantity and * for Name ).
            AllowedMethods (dict) --A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:
            CloudFront forwards only GET and HEAD requests.
            CloudFront forwards only GET , HEAD , and OPTIONS requests.
            CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests.
            If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can't perform operations that you don't want them to. For example, you might not want users to have permissions to delete objects from your origin.
            Quantity (integer) -- [REQUIRED]The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET , HEAD , and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests).
            Items (list) -- [REQUIRED]A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.
            (string) --
            CachedMethods (dict) --A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:
            CloudFront caches responses to GET and HEAD requests.
            CloudFront caches responses to GET , HEAD , and OPTIONS requests.
            If you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.
            Quantity (integer) -- [REQUIRED]The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET , HEAD , and OPTIONS requests).
            Items (list) -- [REQUIRED]A complex type that contains the HTTP methods that you want CloudFront to cache responses to.
            (string) --
            
            SmoothStreaming (boolean) --Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true ; if not, specify false . If you specify true for SmoothStreaming , you can still distribute other content using this cache behavior if the content matches the value of PathPattern .
            DefaultTTL (integer) --The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
            MaxTTL (integer) --
            Compress (boolean) --Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true ; if not, specify false . For more information, see Serving Compressed Files in the Amazon CloudFront Developer Guide .
            LambdaFunctionAssociations (dict) --A complex type that contains zero or more Lambda function associations for a cache behavior.
            Quantity (integer) -- [REQUIRED]The number of Lambda function associations for this cache behavior.
            Items (list) --
            Optional : A complex type that contains LambdaFunctionAssociation items for this cache behavior. If Quantity is 0 , you can omit Items .
            (dict) --A complex type that contains a Lambda function association.
            LambdaFunctionARN (string) -- [REQUIRED]The ARN of the Lambda function. You must specify the ARN of a function version; you can't specify a Lambda alias or $LATEST.
            EventType (string) -- [REQUIRED]Specifies the event type that triggers a Lambda function invocation. You can specify the following values:
            viewer-request : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.
            origin-request : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn't execute.
            origin-response : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn't execute.
            viewer-response : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn't execute.
            IncludeBody (boolean) --A flag that allows a Lambda function to have read access to the body content. For more information, see Accessing the Request Body by Choosing the Include Body Option in the Amazon CloudFront Developer Guide.
            
            FieldLevelEncryptionId (string) --The value of ID for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.
            CacheBehaviors (dict) --A complex type that contains zero or more CacheBehavior elements.
            Quantity (integer) -- [REQUIRED]The number of cache behaviors for this distribution.
            Items (list) --Optional: A complex type that contains cache behaviors for this distribution. If Quantity is 0 , you can omit Items .
            (dict) --A complex type that describes how CloudFront processes requests.
            You must create at least as many cache behaviors (including the default cache behavior) as you have origins if you want CloudFront to distribute objects from all of the origins. Each cache behavior specifies the one origin from which you want CloudFront to get objects. If you have two origins and only the default cache behavior, the default cache behavior will cause CloudFront to get objects from one of the origins, but the other origin is never used.
            For the current limit on the number of cache behaviors that you can add to a distribution, see Amazon CloudFront Limits in the AWS General Reference .
            If you don't want to specify any cache behaviors, include only an empty CacheBehaviors element. Don't include an empty CacheBehavior element, or CloudFront returns a MalformedXML error.
            To delete all cache behaviors in an existing distribution, update the distribution configuration and include only an empty CacheBehaviors element.
            To add, change, or remove one or more cache behaviors, update the distribution configuration and specify all of the cache behaviors that you want to include in the updated distribution.
            For more information about cache behaviors, see Cache Behaviors in the Amazon CloudFront Developer Guide .
            PathPattern (string) -- [REQUIRED]The pattern (for example, images/*.jpg ) that specifies which requests to apply the behavior to. When CloudFront receives a viewer request, the requested path is compared with path patterns in the order in which cache behaviors are listed in the distribution.
            Note
            You can optionally include a slash (/ ) at the beginning of the path pattern. For example, /images/*.jpg . CloudFront behavior is the same with or without the leading / .
            The path pattern for the default cache behavior is * and cannot be changed. If the request for an object does not match the path pattern for any cache behaviors, CloudFront applies the behavior in the default cache behavior.
            For more information, see Path Pattern in the Amazon CloudFront Developer Guide .
            TargetOriginId (string) -- [REQUIRED]The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.
            ForwardedValues (dict) -- [REQUIRED]A complex type that specifies how CloudFront handles query strings and cookies.
            QueryString (boolean) -- [REQUIRED]Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of QueryString and on the values that you specify for QueryStringCacheKeys , if any:
            If you specify true for QueryString and you don't specify any values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.
            If you specify true for QueryString and you specify one or more values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.
            If you specify false for QueryString , CloudFront doesn't forward any query string parameters to the origin, and doesn't cache based on query string parameters.
            For more information, see Configuring CloudFront to Cache Based on Query String Parameters in the Amazon CloudFront Developer Guide .
            Cookies (dict) -- [REQUIRED]A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see How CloudFront Forwards, Caches, and Logs Cookies in the Amazon CloudFront Developer Guide .
            Forward (string) -- [REQUIRED]Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the WhitelistedNames complex type.
            Amazon S3 doesn't process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the Forward element.
            WhitelistedNames (dict) --Required if you specify whitelist for the value of Forward: . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.
            If you specify all or none for the value of Forward , omit WhitelistedNames . If you change the value of Forward from whitelist to all or none and you don't delete the WhitelistedNames element and its child elements, CloudFront deletes them automatically.
            For the current limit on the number of cookie names that you can whitelist for each cache behavior, see Amazon CloudFront Limits in the AWS General Reference .
            Quantity (integer) -- [REQUIRED]The number of different cookies that you want CloudFront to forward to the origin for this cache behavior.
            Items (list) --A complex type that contains one Name element for each cookie that you want CloudFront to forward to the origin for this cache behavior.
            (string) --
            
            Headers (dict) --A complex type that specifies the Headers , if any, that you want CloudFront to base caching on for this cache behavior.
            Quantity (integer) -- [REQUIRED]The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:
            Forward all headers to your origin : Specify 1 for Quantity and * for Name .
            Warning
            CloudFront doesn't cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.
            Forward a whitelist of headers you specify : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in Name elements. CloudFront caches your objects based on the values in the specified headers.
            Forward only the default headers : Specify 0 for Quantity and omit Items . In this configuration, CloudFront doesn't cache based on the values in the request headers.
            Regardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:
            S3 bucket : See HTTP Request Headers That CloudFront Removes or Updates
            Custom origin : See HTTP Request Headers and CloudFront Behavior
            Items (list) --A list that contains one Name element for each header that you want CloudFront to use for caching in this cache behavior. If Quantity is 0 , omit Items .
            (string) --
            
            QueryStringCacheKeys (dict) --A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.
            Quantity (integer) -- [REQUIRED]The number of whitelisted query string parameters for this cache behavior.
            Items (list) --(Optional) A list that contains the query string parameters that you want CloudFront to use as a basis for caching for this cache behavior. If Quantity is 0, you can omit Items .
            (string) --
            
            TrustedSigners (dict) -- [REQUIRED]A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.
            If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items . For more information, see Serving Private Content through CloudFront in the Amazon Amazon CloudFront Developer Guide .
            If you don't want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items .
            To add, change, or remove one or more trusted signers, change Enabled to true (if it's currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
            Enabled (boolean) -- [REQUIRED]Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .
            Quantity (integer) -- [REQUIRED]The number of trusted signers for this cache behavior.
            Items (list) --
            Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .
            (string) --
            
            ViewerProtocolPolicy (string) -- [REQUIRED]The protocol that viewers can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern . You can specify the following options:
            allow-all : Viewers can use HTTP or HTTPS.
            redirect-to-https : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.
            https-only : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).
            For more information about requiring the HTTPS protocol, see Using an HTTPS Connection to Access Your Objects in the Amazon CloudFront Developer Guide .
            Note
            The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
            MinTTL (integer) -- [REQUIRED]The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) in the Amazon Amazon CloudFront Developer Guide .
            You must specify 0 for MinTTL if you configure CloudFront to forward all headers to your origin (under Headers , if you specify 1 for Quantity and * for Name ).
            AllowedMethods (dict) --A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:
            CloudFront forwards only GET and HEAD requests.
            CloudFront forwards only GET , HEAD , and OPTIONS requests.
            CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests.
            If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can't perform operations that you don't want them to. For example, you might not want users to have permissions to delete objects from your origin.
            Quantity (integer) -- [REQUIRED]The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET , HEAD , and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests).
            Items (list) -- [REQUIRED]A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.
            (string) --
            CachedMethods (dict) --A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:
            CloudFront caches responses to GET and HEAD requests.
            CloudFront caches responses to GET , HEAD , and OPTIONS requests.
            If you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.
            Quantity (integer) -- [REQUIRED]The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET , HEAD , and OPTIONS requests).
            Items (list) -- [REQUIRED]A complex type that contains the HTTP methods that you want CloudFront to cache responses to.
            (string) --
            
            SmoothStreaming (boolean) --Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true ; if not, specify false . If you specify true for SmoothStreaming , you can still distribute other content using this cache behavior if the content matches the value of PathPattern .
            DefaultTTL (integer) --The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
            MaxTTL (integer) --The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
            Compress (boolean) --Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true; if not, specify false. For more information, see Serving Compressed Files in the Amazon CloudFront Developer Guide .
            LambdaFunctionAssociations (dict) --A complex type that contains zero or more Lambda function associations for a cache behavior.
            Quantity (integer) -- [REQUIRED]The number of Lambda function associations for this cache behavior.
            Items (list) --
            Optional : A complex type that contains LambdaFunctionAssociation items for this cache behavior. If Quantity is 0 , you can omit Items .
            (dict) --A complex type that contains a Lambda function association.
            LambdaFunctionARN (string) -- [REQUIRED]The ARN of the Lambda function. You must specify the ARN of a function version; you can't specify a Lambda alias or $LATEST.
            EventType (string) -- [REQUIRED]Specifies the event type that triggers a Lambda function invocation. You can specify the following values:
            viewer-request : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.
            origin-request : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn't execute.
            origin-response : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn't execute.
            viewer-response : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn't execute.
            IncludeBody (boolean) --A flag that allows a Lambda function to have read access to the body content. For more information, see Accessing the Request Body by Choosing the Include Body Option in the Amazon CloudFront Developer Guide.
            
            FieldLevelEncryptionId (string) --The value of ID for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.
            
            CustomErrorResponses (dict) --A complex type that controls the following:
            Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.
            How long CloudFront caches HTTP status codes in the 4xx and 5xx range.
            For more information about custom error pages, see Customizing Error Responses in the Amazon CloudFront Developer Guide .
            Quantity (integer) -- [REQUIRED]The number of HTTP status codes for which you want to specify a custom error page and/or a caching duration. If Quantity is 0 , you can omit Items .
            Items (list) --A complex type that contains a CustomErrorResponse element for each HTTP status code for which you want to specify a custom error page and/or a caching duration.
            (dict) --A complex type that controls:
            Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.
            How long CloudFront caches HTTP status codes in the 4xx and 5xx range.
            For more information about custom error pages, see Customizing Error Responses in the Amazon CloudFront Developer Guide .
            ErrorCode (integer) -- [REQUIRED]The HTTP status code for which you want to specify a custom error page and/or a caching duration.
            ResponsePagePath (string) --The path to the custom error page that you want CloudFront to return to a viewer when your origin returns the HTTP status code specified by ErrorCode , for example, /4xx-errors/403-forbidden.html . If you want to store your objects and your custom error pages in different locations, your distribution must include a cache behavior for which the following is true:
            The value of PathPattern matches the path to your custom error messages. For example, suppose you saved custom error pages for 4xx errors in an Amazon S3 bucket in a directory named /4xx-errors . Your distribution must include a cache behavior for which the path pattern routes requests for your custom error pages to that location, for example, /4xx-errors/* .
            The value of TargetOriginId specifies the value of the ID element for the origin that contains your custom error pages.
            If you specify a value for ResponsePagePath , you must also specify a value for ResponseCode . If you don't want to specify a value, include an empty element, <ResponsePagePath> , in the XML document.
            We recommend that you store custom error pages in an Amazon S3 bucket. If you store custom error pages on an HTTP server and the server starts to return 5xx errors, CloudFront can't get the files that you want to return to viewers because the origin server is unavailable.
            ResponseCode (string) --The HTTP status code that you want CloudFront to return to the viewer along with the custom error page. There are a variety of reasons that you might want CloudFront to return a status code different from the status code that your origin returned to CloudFront, for example:
            Some Internet devices (some firewalls and corporate proxies, for example) intercept HTTP 4xx and 5xx and prevent the response from being returned to the viewer. If you substitute 200 , the response typically won't be intercepted.
            If you don't care about distinguishing among different client errors or server errors, you can specify 400 or 500 as the ResponseCode for all 4xx or 5xx errors.
            You might want to return a 200 status code (OK) and static website so your customers don't know that your website is down.
            If you specify a value for ResponseCode , you must also specify a value for ResponsePagePath . If you don't want to specify a value, include an empty element, <ResponseCode> , in the XML document.
            ErrorCachingMinTTL (integer) --The minimum amount of time, in seconds, that you want CloudFront to cache the HTTP status code specified in ErrorCode . When this time period has elapsed, CloudFront queries your origin to see whether the problem that caused the error has been resolved and the requested object is now available.
            If you don't want to specify a value, include an empty element, <ErrorCachingMinTTL> , in the XML document.
            For more information, see Customizing Error Responses in the Amazon CloudFront Developer Guide .
            
            Comment (string) -- [REQUIRED]Any comments you want to include about the distribution.
            If you don't want to specify a comment, include an empty Comment element.
            To delete an existing comment, update the distribution configuration and include an empty Comment element.
            To add or change a comment, update the distribution configuration and specify the new comment.
            Logging (dict) --A complex type that controls whether access logs are written for the distribution.
            For more information about logging, see Access Logs in the Amazon CloudFront Developer Guide .
            Enabled (boolean) -- [REQUIRED]Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you don't want to enable logging when you create a distribution or if you want to disable logging for an existing distribution, specify false for Enabled , and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket , prefix , and IncludeCookies , the values are automatically deleted.
            IncludeCookies (boolean) -- [REQUIRED]Specifies whether you want CloudFront to include cookies in access logs, specify true for IncludeCookies . If you choose to include cookies in logs, CloudFront logs all cookies regardless of how you configure the cache behaviors for this distribution. If you don't want to include cookies when you create a distribution or if you want to disable include cookies for an existing distribution, specify false for IncludeCookies .
            Bucket (string) -- [REQUIRED]The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com .
            Prefix (string) -- [REQUIRED]An optional string that you want CloudFront to prefix to the access log filenames for this distribution, for example, myprefix/ . If you want to enable logging, but you don't want to specify a prefix, you still must include an empty Prefix element in the Logging element.
            PriceClass (string) --The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All , CloudFront responds to requests for your objects from all CloudFront edge locations.
            If you specify a price class other than PriceClass_All , CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Viewers who are in or near regions that are excluded from your specified price class may encounter slower performance.
            For more information about price classes, see Choosing the Price Class for a CloudFront Distribution in the Amazon CloudFront Developer Guide . For information about CloudFront pricing, including how price classes (such as Price Class 100) map to CloudFront regions, see Amazon CloudFront Pricing . For price class information, scroll down to see the table at the bottom of the page.
            Enabled (boolean) -- [REQUIRED]From this field, you can enable or disable the selected distribution.
            ViewerCertificate (dict) --
            CloudFrontDefaultCertificate (boolean) --For information about how and when to use CloudFrontDefaultCertificate , see ViewerCertificate .
            IAMCertificateId (string) --For information about how and when to use IAMCertificateId , see ViewerCertificate .
            ACMCertificateArn (string) --For information about how and when to use ACMCertificateArn , see ViewerCertificate .
            SSLSupportMethod (string) --If you specify a value for ViewerCertificate$ACMCertificateArn or for ViewerCertificate$IAMCertificateId , you must also specify how you want CloudFront to serve HTTPS requests: using a method that works for all clients or one that works for most clients:
            vip : CloudFront uses dedicated IP addresses for your content and can respond to HTTPS requests from any viewer. However, you will incur additional monthly charges.
            sni-only : CloudFront can respond to HTTPS requests from viewers that support Server Name Indication (SNI). All modern browsers support SNI, but some browsers still in use don't support SNI. If some of your users' browsers don't support SNI, we recommend that you do one of the following:
            Use the vip option (dedicated IP addresses) instead of sni-only .
            Use the CloudFront SSL/TLS certificate instead of a custom certificate. This requires that you use the CloudFront domain name of your distribution in the URLs for your objects, for example, https://d111111abcdef8.cloudfront.net/logo.png .
            If you can control which browser your users use, upgrade the browser to one that supports SNI.
            Use HTTP instead of HTTPS.
            Don't specify a value for SSLSupportMethod if you specified <CloudFrontDefaultCertificate>true<CloudFrontDefaultCertificate> .
            For more information, see Using Alternate Domain Names and HTTPS in the Amazon CloudFront Developer Guide .
            MinimumProtocolVersion (string) --Specify the security policy that you want CloudFront to use for HTTPS connections. A security policy determines two settings:
            The minimum SSL/TLS protocol that CloudFront uses to communicate with viewers
            The cipher that CloudFront uses to encrypt the content that it returns to viewers
            Note
            On the CloudFront console, this setting is called Security policy .
            We recommend that you specify TLSv1.1_2016 unless your users are using browsers or devices that do not support TLSv1.1 or later.
            When both of the following are true, you must specify TLSv1 or later for the security policy:
            You're using a custom certificate: you specified a value for ACMCertificateArn or for IAMCertificateId
            You're using SNI: you specified sni-only for SSLSupportMethod
            If you specify true for CloudFrontDefaultCertificate , CloudFront automatically sets the security policy to TLSv1 regardless of the value that you specify for MinimumProtocolVersion .
            For information about the relationship between the security policy that you choose and the protocols and ciphers that CloudFront uses to communicate with viewers, see Supported SSL/TLS Protocols and Ciphers for Communication Between Viewers and CloudFront in the Amazon CloudFront Developer Guide .
            Certificate (string) --This field has been deprecated. Use one of the following fields instead:
            ViewerCertificate$ACMCertificateArn
            ViewerCertificate$IAMCertificateId
            ViewerCertificate$CloudFrontDefaultCertificate
            CertificateSource (string) --This field has been deprecated. Use one of the following fields instead:
            ViewerCertificate$ACMCertificateArn
            ViewerCertificate$IAMCertificateId
            ViewerCertificate$CloudFrontDefaultCertificate
            
            Restrictions (dict) --
            GeoRestriction (dict) -- [REQUIRED]A complex type that controls the countries in which your content is distributed. CloudFront determines the location of your users using MaxMind GeoIP databases.
            RestrictionType (string) -- [REQUIRED]The method that you want to use to restrict distribution of your content by country:
            none : No geo restriction is enabled, meaning access to content is not restricted by client geo location.
            blacklist : The Location elements specify the countries in which you don't want CloudFront to distribute your content.
            whitelist : The Location elements specify the countries in which you want CloudFront to distribute your content.
            Quantity (integer) -- [REQUIRED]When geo restriction is enabled , this is the number of countries in your whitelist or blacklist . Otherwise, when it is not enabled, Quantity is 0 , and you can omit Items .
            Items (list) --A complex type that contains a Location element for each country in which you want CloudFront either to distribute your content (whitelist ) or not distribute your content (blacklist ).
            The Location element is a two-letter, uppercase country code for a country that you want to include in your blacklist or whitelist . Include one Location element for each country.
            CloudFront and MaxMind both use ISO 3166 country codes. For the current list of countries and the corresponding codes, see ISO 3166-1-alpha-2 code on the International Organization for Standardization website. You can also refer to the country list on the CloudFront console, which includes both country names and codes.
            (string) --
            
            WebACLId (string) --A unique identifier that specifies the AWS WAF web ACL, if any, to associate with this distribution.
            AWS WAF is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to CloudFront, and lets you control access to your content. Based on conditions that you specify, such as the IP addresses that requests originate from or the values of query strings, CloudFront responds to requests either with the requested content or with an HTTP 403 status code (Forbidden). You can also configure CloudFront to return a custom error page when a request is blocked. For more information about AWS WAF, see the AWS WAF Developer Guide .
            HttpVersion (string) --(Optional) Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. The default value for new web distributions is http2. Viewers that don't support HTTP/2 automatically use an earlier HTTP version.
            For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support Server Name Identification (SNI).
            In general, configuring CloudFront to communicate with viewers using HTTP/2 reduces latency. You can improve performance by optimizing for HTTP/2. For more information, do an Internet search for 'http/2 optimization.'
            IsIPV6Enabled (boolean) --If you want CloudFront to respond to IPv6 DNS requests with an IPv6 address for your distribution, specify true . If you specify false , CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution.
            In general, you should enable IPv6 if you have users on IPv6 networks who want to access your content. However, if you're using signed URLs or signed cookies to restrict access to your content, and if you're using a custom policy that includes the IpAddress parameter to restrict the IP addresses that can access your content, don't enable IPv6. If you want to restrict access to some content by IP address and not restrict access to other content (or restrict access but not by IP address), you can create two distributions. For more information, see Creating a Signed URL Using a Custom Policy in the Amazon CloudFront Developer Guide .
            If you're using an Amazon Route 53 alias resource record set to route traffic to your CloudFront distribution, you need to create a second alias resource record set when both of the following are true:
            You enable IPv6 for the distribution
            You're using alternate domain names in the URLs for your objects
            For more information, see Routing Traffic to an Amazon CloudFront Web Distribution by Using Your Domain Name in the Amazon Route 53 Developer Guide .
            If you created a CNAME resource record set, either with Amazon Route 53 or with another DNS service, you don't need to make any changes. A CNAME record will route traffic to your distribution regardless of the IP address format of the viewer request.
            Tags (dict) -- [REQUIRED]A complex type that contains zero or more Tag elements.
            Items (list) --A complex type that contains Tag elements.
            (dict) --A complex type that contains Tag key and Tag value.
            Key (string) -- [REQUIRED]A string that contains Tag key.
            The string length should be between 1 and 128 characters. Valid characters include a-z , A-Z , 0-9 , space, and the special characters _ - . : / = + @ .
            Value (string) --A string that contains an optional Tag value.
            The string length should be between 0 and 256 characters. Valid characters include a-z , A-Z , 0-9 , space, and the special characters _ - . : / = + @ .
            
            
            

    :rtype: dict
    :return: {
        'Distribution': {
            'Id': 'string',
            'ARN': 'string',
            'Status': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'InProgressInvalidationBatches': 123,
            'DomainName': 'string',
            'ActiveTrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    {
                        'AwsAccountNumber': 'string',
                        'KeyPairIds': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                ]
            },
            'DistributionConfig': {
                'CallerReference': 'string',
                'Aliases': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'DefaultRootObject': 'string',
                'Origins': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Id': 'string',
                            'DomainName': 'string',
                            'OriginPath': 'string',
                            'CustomHeaders': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'HeaderName': 'string',
                                        'HeaderValue': 'string'
                                    },
                                ]
                            },
                            'S3OriginConfig': {
                                'OriginAccessIdentity': 'string'
                            },
                            'CustomOriginConfig': {
                                'HTTPPort': 123,
                                'HTTPSPort': 123,
                                'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                                'OriginSslProtocols': {
                                    'Quantity': 123,
                                    'Items': [
                                        'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                                    ]
                                },
                                'OriginReadTimeout': 123,
                                'OriginKeepaliveTimeout': 123
                            }
                        },
                    ]
                },
                'OriginGroups': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Id': 'string',
                            'FailoverCriteria': {
                                'StatusCodes': {
                                    'Quantity': 123,
                                    'Items': [
                                        123,
                                    ]
                                }
                            },
                            'Members': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'OriginId': 'string'
                                    },
                                ]
                            }
                        },
                    ]
                },
                'DefaultCacheBehavior': {
                    'TargetOriginId': 'string',
                    'ForwardedValues': {
                        'QueryString': True|False,
                        'Cookies': {
                            'Forward': 'none'|'whitelist'|'all',
                            'WhitelistedNames': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'Headers': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'QueryStringCacheKeys': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'TrustedSigners': {
                        'Enabled': True|False,
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                    'MinTTL': 123,
                    'AllowedMethods': {
                        'Quantity': 123,
                        'Items': [
                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                        ],
                        'CachedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ]
                        }
                    },
                    'SmoothStreaming': True|False,
                    'DefaultTTL': 123,
                    'MaxTTL': 123,
                    'Compress': True|False,
                    'LambdaFunctionAssociations': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'LambdaFunctionARN': 'string',
                                'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                'IncludeBody': True|False
                            },
                        ]
                    },
                    'FieldLevelEncryptionId': 'string'
                },
                'CacheBehaviors': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'PathPattern': 'string',
                            'TargetOriginId': 'string',
                            'ForwardedValues': {
                                'QueryString': True|False,
                                'Cookies': {
                                    'Forward': 'none'|'whitelist'|'all',
                                    'WhitelistedNames': {
                                        'Quantity': 123,
                                        'Items': [
                                            'string',
                                        ]
                                    }
                                },
                                'Headers': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                },
                                'QueryStringCacheKeys': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                            'TrustedSigners': {
                                'Enabled': True|False,
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            },
                            'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                            'MinTTL': 123,
                            'AllowedMethods': {
                                'Quantity': 123,
                                'Items': [
                                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                ],
                                'CachedMethods': {
                                    'Quantity': 123,
                                    'Items': [
                                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                    ]
                                }
                            },
                            'SmoothStreaming': True|False,
                            'DefaultTTL': 123,
                            'MaxTTL': 123,
                            'Compress': True|False,
                            'LambdaFunctionAssociations': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'LambdaFunctionARN': 'string',
                                        'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                        'IncludeBody': True|False
                                    },
                                ]
                            },
                            'FieldLevelEncryptionId': 'string'
                        },
                    ]
                },
                'CustomErrorResponses': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'ErrorCode': 123,
                            'ResponsePagePath': 'string',
                            'ResponseCode': 'string',
                            'ErrorCachingMinTTL': 123
                        },
                    ]
                },
                'Comment': 'string',
                'Logging': {
                    'Enabled': True|False,
                    'IncludeCookies': True|False,
                    'Bucket': 'string',
                    'Prefix': 'string'
                },
                'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                'Enabled': True|False,
                'ViewerCertificate': {
                    'CloudFrontDefaultCertificate': True|False,
                    'IAMCertificateId': 'string',
                    'ACMCertificateArn': 'string',
                    'SSLSupportMethod': 'sni-only'|'vip',
                    'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
                    'Certificate': 'string',
                    'CertificateSource': 'cloudfront'|'iam'|'acm'
                },
                'Restrictions': {
                    'GeoRestriction': {
                        'RestrictionType': 'blacklist'|'whitelist'|'none',
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
                'WebACLId': 'string',
                'HttpVersion': 'http1.1'|'http2',
                'IsIPV6Enabled': True|False
            }
        },
        'Location': 'string',
        'ETag': 'string'
    }
    
    
    :returns: 
    If you configured Amazon S3 Transfer Acceleration for your bucket, don't specify the s3-accelerate endpoint for DomainName .
    The bucket name must be between 3 and 63 characters long (inclusive).
    The bucket name must contain only lowercase characters, numbers, periods, underscores, and dashes.
    The bucket name must not contain adjacent periods.
    
    """
    pass

def create_field_level_encryption_config(FieldLevelEncryptionConfig=None):
    """
    Create a new field-level encryption configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.create_field_level_encryption_config(
        FieldLevelEncryptionConfig={
            'CallerReference': 'string',
            'Comment': 'string',
            'QueryArgProfileConfig': {
                'ForwardWhenQueryArgProfileIsUnknown': True|False,
                'QueryArgProfiles': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'QueryArg': 'string',
                            'ProfileId': 'string'
                        },
                    ]
                }
            },
            'ContentTypeProfileConfig': {
                'ForwardWhenContentTypeIsUnknown': True|False,
                'ContentTypeProfiles': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Format': 'URLEncoded',
                            'ProfileId': 'string',
                            'ContentType': 'string'
                        },
                    ]
                }
            }
        }
    )
    
    
    :type FieldLevelEncryptionConfig: dict
    :param FieldLevelEncryptionConfig: [REQUIRED]
            The request to create a new field-level encryption configuration.
            CallerReference (string) -- [REQUIRED]A unique number that ensures the request can't be replayed.
            Comment (string) --An optional comment about the configuration.
            QueryArgProfileConfig (dict) --A complex data type that specifies when to forward content if a profile isn't found and the profile that can be provided as a query argument in a request.
            ForwardWhenQueryArgProfileIsUnknown (boolean) -- [REQUIRED]Flag to set if you want a request to be forwarded to the origin even if the profile specified by the field-level encryption query argument, fle-profile, is unknown.
            QueryArgProfiles (dict) --Profiles specified for query argument-profile mapping for field-level encryption.
            Quantity (integer) -- [REQUIRED]Number of profiles for query argument-profile mapping for field-level encryption.
            Items (list) --Number of items for query argument-profile mapping for field-level encryption.
            (dict) --Query argument-profile mapping for field-level encryption.
            QueryArg (string) -- [REQUIRED]Query argument for field-level encryption query argument-profile mapping.
            ProfileId (string) -- [REQUIRED]ID of profile to use for field-level encryption query argument-profile mapping
            
            
            ContentTypeProfileConfig (dict) --A complex data type that specifies when to forward content if a content type isn't recognized and profiles to use as by default in a request if a query argument doesn't specify a profile to use.
            ForwardWhenContentTypeIsUnknown (boolean) -- [REQUIRED]The setting in a field-level encryption content type-profile mapping that specifies what to do when an unknown content type is provided for the profile. If true, content is forwarded without being encrypted when the content type is unknown. If false (the default), an error is returned when the content type is unknown.
            ContentTypeProfiles (dict) --The configuration for a field-level encryption content type-profile.
            Quantity (integer) -- [REQUIRED]The number of field-level encryption content type-profile mappings.
            Items (list) --Items in a field-level encryption content type-profile mapping.
            (dict) --A field-level encryption content type profile.
            Format (string) -- [REQUIRED]The format for a field-level encryption content type-profile mapping.
            ProfileId (string) --The profile ID for a field-level encryption content type-profile mapping.
            ContentType (string) -- [REQUIRED]The content type for a field-level encryption content type-profile mapping.
            
            
            

    :rtype: dict
    :return: {
        'FieldLevelEncryption': {
            'Id': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'FieldLevelEncryptionConfig': {
                'CallerReference': 'string',
                'Comment': 'string',
                'QueryArgProfileConfig': {
                    'ForwardWhenQueryArgProfileIsUnknown': True|False,
                    'QueryArgProfiles': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'QueryArg': 'string',
                                'ProfileId': 'string'
                            },
                        ]
                    }
                },
                'ContentTypeProfileConfig': {
                    'ForwardWhenContentTypeIsUnknown': True|False,
                    'ContentTypeProfiles': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'Format': 'URLEncoded',
                                'ProfileId': 'string',
                                'ContentType': 'string'
                            },
                        ]
                    }
                }
            }
        },
        'Location': 'string',
        'ETag': 'string'
    }
    
    
    """
    pass

def create_field_level_encryption_profile(FieldLevelEncryptionProfileConfig=None):
    """
    Create a field-level encryption profile.
    See also: AWS API Documentation
    
    
    :example: response = client.create_field_level_encryption_profile(
        FieldLevelEncryptionProfileConfig={
            'Name': 'string',
            'CallerReference': 'string',
            'Comment': 'string',
            'EncryptionEntities': {
                'Quantity': 123,
                'Items': [
                    {
                        'PublicKeyId': 'string',
                        'ProviderId': 'string',
                        'FieldPatterns': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                ]
            }
        }
    )
    
    
    :type FieldLevelEncryptionProfileConfig: dict
    :param FieldLevelEncryptionProfileConfig: [REQUIRED]
            The request to create a field-level encryption profile.
            Name (string) -- [REQUIRED]Profile name for the field-level encryption profile.
            CallerReference (string) -- [REQUIRED]A unique number that ensures that the request can't be replayed.
            Comment (string) --An optional comment for the field-level encryption profile.
            EncryptionEntities (dict) -- [REQUIRED]A complex data type of encryption entities for the field-level encryption profile that include the public key ID, provider, and field patterns for specifying which fields to encrypt with this key.
            Quantity (integer) -- [REQUIRED]Number of field pattern items in a field-level encryption content type-profile mapping.
            Items (list) --An array of field patterns in a field-level encryption content type-profile mapping.
            (dict) --Complex data type for field-level encryption profiles that includes the encryption key and field pattern specifications.
            PublicKeyId (string) -- [REQUIRED]The public key associated with a set of field-level encryption patterns, to be used when encrypting the fields that match the patterns.
            ProviderId (string) -- [REQUIRED]The provider associated with the public key being used for encryption. This value must also be provided with the private key for applications to be able to decrypt data.
            FieldPatterns (dict) -- [REQUIRED]Field patterns in a field-level encryption content type profile specify the fields that you want to be encrypted. You can provide the full field name, or any beginning characters followed by a wildcard (*). You can't overlap field patterns. For example, you can't have both ABC* and AB*. Note that field patterns are case-sensitive.
            Quantity (integer) -- [REQUIRED]The number of field-level encryption field patterns.
            Items (list) --An array of the field-level encryption field patterns.
            (string) --
            
            
            

    :rtype: dict
    :return: {
        'FieldLevelEncryptionProfile': {
            'Id': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'FieldLevelEncryptionProfileConfig': {
                'Name': 'string',
                'CallerReference': 'string',
                'Comment': 'string',
                'EncryptionEntities': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'PublicKeyId': 'string',
                            'ProviderId': 'string',
                            'FieldPatterns': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                    ]
                }
            }
        },
        'Location': 'string',
        'ETag': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_invalidation(DistributionId=None, InvalidationBatch=None):
    """
    Create a new invalidation.
    See also: AWS API Documentation
    
    
    :example: response = client.create_invalidation(
        DistributionId='string',
        InvalidationBatch={
            'Paths': {
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'CallerReference': 'string'
        }
    )
    
    
    :type DistributionId: string
    :param DistributionId: [REQUIRED]
            The distribution's id.
            

    :type InvalidationBatch: dict
    :param InvalidationBatch: [REQUIRED]
            The batch information for the invalidation.
            Paths (dict) -- [REQUIRED]A complex type that contains information about the objects that you want to invalidate. For more information, see Specifying the Objects to Invalidate in the Amazon CloudFront Developer Guide .
            Quantity (integer) -- [REQUIRED]The number of objects that you want to invalidate.
            Items (list) --A complex type that contains a list of the paths that you want to invalidate.
            (string) --
            
            CallerReference (string) -- [REQUIRED]A value that you specify to uniquely identify an invalidation request. CloudFront uses the value to prevent you from accidentally resubmitting an identical request. Whenever you create a new invalidation request, you must specify a new value for CallerReference and change other values in the request as applicable. One way to ensure that the value of CallerReference is unique is to use a timestamp , for example, 20120301090000 .
            If you make a second invalidation request with the same value for CallerReference , and if the rest of the request is the same, CloudFront doesn't create a new invalidation request. Instead, CloudFront returns information about the invalidation request that you previously created with the same CallerReference .
            If CallerReference is a value you already sent in a previous invalidation batch request but the content of any Path is different from the original request, CloudFront returns an InvalidationBatchAlreadyExists error.
            

    :rtype: dict
    :return: {
        'Location': 'string',
        'Invalidation': {
            'Id': 'string',
            'Status': 'string',
            'CreateTime': datetime(2015, 1, 1),
            'InvalidationBatch': {
                'Paths': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'CallerReference': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_public_key(PublicKeyConfig=None):
    """
    Add a new public key to CloudFront to use, for example, for field-level encryption. You can add a maximum of 10 public keys with one AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.create_public_key(
        PublicKeyConfig={
            'CallerReference': 'string',
            'Name': 'string',
            'EncodedKey': 'string',
            'Comment': 'string'
        }
    )
    
    
    :type PublicKeyConfig: dict
    :param PublicKeyConfig: [REQUIRED]
            The request to add a public key to CloudFront.
            CallerReference (string) -- [REQUIRED]A unique number that ensures that the request can't be replayed.
            Name (string) -- [REQUIRED]The name for a public key you add to CloudFront to use with features like field-level encryption.
            EncodedKey (string) -- [REQUIRED]The encoded public key that you want to add to CloudFront to use with features like field-level encryption.
            Comment (string) --An optional comment about a public key.
            

    :rtype: dict
    :return: {
        'PublicKey': {
            'Id': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'PublicKeyConfig': {
                'CallerReference': 'string',
                'Name': 'string',
                'EncodedKey': 'string',
                'Comment': 'string'
            }
        },
        'Location': 'string',
        'ETag': 'string'
    }
    
    
    """
    pass

def create_streaming_distribution(StreamingDistributionConfig=None):
    """
    Creates a new RMTP distribution. An RTMP distribution is similar to a web distribution, but an RTMP distribution streams media files using the Adobe Real-Time Messaging Protocol (RTMP) instead of serving files using HTTP.
    To create a new web distribution, submit a POST request to the CloudFront API version /distribution resource. The request body must include a document with a StreamingDistributionConfig element. The response echoes the StreamingDistributionConfig element and returns other information about the RTMP distribution.
    To get the status of your request, use the GET StreamingDistribution API action. When the value of Enabled is true and the value of Status is Deployed , your distribution is ready. A distribution usually deploys in less than 15 minutes.
    For more information about web distributions, see Working with RTMP Distributions in the Amazon CloudFront Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_streaming_distribution(
        StreamingDistributionConfig={
            'CallerReference': 'string',
            'S3Origin': {
                'DomainName': 'string',
                'OriginAccessIdentity': 'string'
            },
            'Aliases': {
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'Comment': 'string',
            'Logging': {
                'Enabled': True|False,
                'Bucket': 'string',
                'Prefix': 'string'
            },
            'TrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
            'Enabled': True|False
        }
    )
    
    
    :type StreamingDistributionConfig: dict
    :param StreamingDistributionConfig: [REQUIRED]
            The streaming distribution's configuration information.
            CallerReference (string) -- [REQUIRED]A unique value (for example, a date-time stamp) that ensures that the request can't be replayed.
            If the value of CallerReference is new (regardless of the content of the StreamingDistributionConfig object), CloudFront creates a new distribution.
            If CallerReference is a value that you already sent in a previous request to create a distribution, CloudFront returns a DistributionAlreadyExists error.
            S3Origin (dict) -- [REQUIRED]A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.
            DomainName (string) -- [REQUIRED]The DNS name of the Amazon S3 origin.
            OriginAccessIdentity (string) -- [REQUIRED]The CloudFront origin access identity to associate with the RTMP distribution. Use an origin access identity to configure the distribution so that end users can only access objects in an Amazon S3 bucket through CloudFront.
            If you want end users to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element.
            To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element.
            To replace the origin access identity, update the distribution configuration and specify the new origin access identity.
            For more information, see Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content in the Amazon Amazon CloudFront Developer Guide .
            Aliases (dict) --A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution.
            Quantity (integer) -- [REQUIRED]The number of CNAME aliases, if any, that you want to associate with this distribution.
            Items (list) --A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.
            (string) --
            
            Comment (string) -- [REQUIRED]Any comments you want to include about the streaming distribution.
            Logging (dict) --A complex type that controls whether access logs are written for the streaming distribution.
            Enabled (boolean) -- [REQUIRED]Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you don't want to enable logging when you create a streaming distribution or if you want to disable logging for an existing streaming distribution, specify false for Enabled , and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket and Prefix , the values are automatically deleted.
            Bucket (string) -- [REQUIRED]The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com .
            Prefix (string) -- [REQUIRED]An optional string that you want CloudFront to prefix to the access log filenames for this streaming distribution, for example, myprefix/ . If you want to enable logging, but you don't want to specify a prefix, you still must include an empty Prefix element in the Logging element.
            TrustedSigners (dict) -- [REQUIRED]A complex type that specifies any AWS accounts that you want to permit to create signed URLs for private content. If you want the distribution to use signed URLs, include this element; if you want the distribution to use public URLs, remove this element. For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .
            Enabled (boolean) -- [REQUIRED]Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .
            Quantity (integer) -- [REQUIRED]The number of trusted signers for this cache behavior.
            Items (list) --
            Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .
            (string) --
            
            PriceClass (string) --A complex type that contains information about price class for this streaming distribution.
            Enabled (boolean) -- [REQUIRED]Whether the streaming distribution is enabled to accept user requests for content.
            

    :rtype: dict
    :return: {
        'StreamingDistribution': {
            'Id': 'string',
            'ARN': 'string',
            'Status': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'DomainName': 'string',
            'ActiveTrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    {
                        'AwsAccountNumber': 'string',
                        'KeyPairIds': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                ]
            },
            'StreamingDistributionConfig': {
                'CallerReference': 'string',
                'S3Origin': {
                    'DomainName': 'string',
                    'OriginAccessIdentity': 'string'
                },
                'Aliases': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'Comment': 'string',
                'Logging': {
                    'Enabled': True|False,
                    'Bucket': 'string',
                    'Prefix': 'string'
                },
                'TrustedSigners': {
                    'Enabled': True|False,
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                'Enabled': True|False
            }
        },
        'Location': 'string',
        'ETag': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_streaming_distribution_with_tags(StreamingDistributionConfigWithTags=None):
    """
    Create a new streaming distribution with tags.
    See also: AWS API Documentation
    
    
    :example: response = client.create_streaming_distribution_with_tags(
        StreamingDistributionConfigWithTags={
            'StreamingDistributionConfig': {
                'CallerReference': 'string',
                'S3Origin': {
                    'DomainName': 'string',
                    'OriginAccessIdentity': 'string'
                },
                'Aliases': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'Comment': 'string',
                'Logging': {
                    'Enabled': True|False,
                    'Bucket': 'string',
                    'Prefix': 'string'
                },
                'TrustedSigners': {
                    'Enabled': True|False,
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                'Enabled': True|False
            },
            'Tags': {
                'Items': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
        }
    )
    
    
    :type StreamingDistributionConfigWithTags: dict
    :param StreamingDistributionConfigWithTags: [REQUIRED]
            The streaming distribution's configuration information.
            StreamingDistributionConfig (dict) -- [REQUIRED]A streaming distribution Configuration.
            CallerReference (string) -- [REQUIRED]A unique value (for example, a date-time stamp) that ensures that the request can't be replayed.
            If the value of CallerReference is new (regardless of the content of the StreamingDistributionConfig object), CloudFront creates a new distribution.
            If CallerReference is a value that you already sent in a previous request to create a distribution, CloudFront returns a DistributionAlreadyExists error.
            S3Origin (dict) -- [REQUIRED]A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.
            DomainName (string) -- [REQUIRED]The DNS name of the Amazon S3 origin.
            OriginAccessIdentity (string) -- [REQUIRED]The CloudFront origin access identity to associate with the RTMP distribution. Use an origin access identity to configure the distribution so that end users can only access objects in an Amazon S3 bucket through CloudFront.
            If you want end users to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element.
            To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element.
            To replace the origin access identity, update the distribution configuration and specify the new origin access identity.
            For more information, see Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content in the Amazon Amazon CloudFront Developer Guide .
            Aliases (dict) --A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution.
            Quantity (integer) -- [REQUIRED]The number of CNAME aliases, if any, that you want to associate with this distribution.
            Items (list) --A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.
            (string) --
            
            Comment (string) -- [REQUIRED]Any comments you want to include about the streaming distribution.
            Logging (dict) --A complex type that controls whether access logs are written for the streaming distribution.
            Enabled (boolean) -- [REQUIRED]Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you don't want to enable logging when you create a streaming distribution or if you want to disable logging for an existing streaming distribution, specify false for Enabled , and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket and Prefix , the values are automatically deleted.
            Bucket (string) -- [REQUIRED]The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com .
            Prefix (string) -- [REQUIRED]An optional string that you want CloudFront to prefix to the access log filenames for this streaming distribution, for example, myprefix/ . If you want to enable logging, but you don't want to specify a prefix, you still must include an empty Prefix element in the Logging element.
            TrustedSigners (dict) -- [REQUIRED]A complex type that specifies any AWS accounts that you want to permit to create signed URLs for private content. If you want the distribution to use signed URLs, include this element; if you want the distribution to use public URLs, remove this element. For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .
            Enabled (boolean) -- [REQUIRED]Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .
            Quantity (integer) -- [REQUIRED]The number of trusted signers for this cache behavior.
            Items (list) --
            Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .
            (string) --
            
            PriceClass (string) --A complex type that contains information about price class for this streaming distribution.
            Enabled (boolean) -- [REQUIRED]Whether the streaming distribution is enabled to accept user requests for content.
            Tags (dict) -- [REQUIRED]A complex type that contains zero or more Tag elements.
            Items (list) --A complex type that contains Tag elements.
            (dict) --A complex type that contains Tag key and Tag value.
            Key (string) -- [REQUIRED]A string that contains Tag key.
            The string length should be between 1 and 128 characters. Valid characters include a-z , A-Z , 0-9 , space, and the special characters _ - . : / = + @ .
            Value (string) --A string that contains an optional Tag value.
            The string length should be between 0 and 256 characters. Valid characters include a-z , A-Z , 0-9 , space, and the special characters _ - . : / = + @ .
            
            
            

    :rtype: dict
    :return: {
        'StreamingDistribution': {
            'Id': 'string',
            'ARN': 'string',
            'Status': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'DomainName': 'string',
            'ActiveTrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    {
                        'AwsAccountNumber': 'string',
                        'KeyPairIds': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                ]
            },
            'StreamingDistributionConfig': {
                'CallerReference': 'string',
                'S3Origin': {
                    'DomainName': 'string',
                    'OriginAccessIdentity': 'string'
                },
                'Aliases': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'Comment': 'string',
                'Logging': {
                    'Enabled': True|False,
                    'Bucket': 'string',
                    'Prefix': 'string'
                },
                'TrustedSigners': {
                    'Enabled': True|False,
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                'Enabled': True|False
            }
        },
        'Location': 'string',
        'ETag': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_cloud_front_origin_access_identity(Id=None, IfMatch=None):
    """
    Delete an origin access identity.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_cloud_front_origin_access_identity(
        Id='string',
        IfMatch='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The origin access identity's ID.
            

    :type IfMatch: string
    :param IfMatch: The value of the ETag header you received from a previous GET or PUT request. For example: E2QWRUHAPOMQZL .

    """
    pass

def delete_distribution(Id=None, IfMatch=None):
    """
    Delete a distribution.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_distribution(
        Id='string',
        IfMatch='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The distribution ID.
            

    :type IfMatch: string
    :param IfMatch: The value of the ETag header that you received when you disabled the distribution. For example: E2QWRUHAPOMQZL .

    """
    pass

def delete_field_level_encryption_config(Id=None, IfMatch=None):
    """
    Remove a field-level encryption configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_field_level_encryption_config(
        Id='string',
        IfMatch='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The ID of the configuration you want to delete from CloudFront.
            

    :type IfMatch: string
    :param IfMatch: The value of the ETag header that you received when retrieving the configuration identity to delete. For example: E2QWRUHAPOMQZL .

    """
    pass

def delete_field_level_encryption_profile(Id=None, IfMatch=None):
    """
    Remove a field-level encryption profile.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_field_level_encryption_profile(
        Id='string',
        IfMatch='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            Request the ID of the profile you want to delete from CloudFront.
            

    :type IfMatch: string
    :param IfMatch: The value of the ETag header that you received when retrieving the profile to delete. For example: E2QWRUHAPOMQZL .

    """
    pass

def delete_public_key(Id=None, IfMatch=None):
    """
    Remove a public key you previously added to CloudFront.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_public_key(
        Id='string',
        IfMatch='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The ID of the public key you want to remove from CloudFront.
            

    :type IfMatch: string
    :param IfMatch: The value of the ETag header that you received when retrieving the public key identity to delete. For example: E2QWRUHAPOMQZL .

    """
    pass

def delete_streaming_distribution(Id=None, IfMatch=None):
    """
    Delete a streaming distribution. To delete an RTMP distribution using the CloudFront API, perform the following steps.
    For information about deleting a distribution using the CloudFront console, see Deleting a Distribution in the Amazon CloudFront Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_streaming_distribution(
        Id='string',
        IfMatch='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The distribution ID.
            

    :type IfMatch: string
    :param IfMatch: The value of the ETag header that you received when you disabled the streaming distribution. For example: E2QWRUHAPOMQZL .

    :returns: 
    Id (string) -- [REQUIRED]
    The distribution ID.
    
    IfMatch (string) -- The value of the ETag header that you received when you disabled the streaming distribution. For example: E2QWRUHAPOMQZL .
    
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

def get_cloud_front_origin_access_identity(Id=None):
    """
    Get the information about an origin access identity.
    See also: AWS API Documentation
    
    
    :example: response = client.get_cloud_front_origin_access_identity(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The identity's ID.
            

    :rtype: dict
    :return: {
        'CloudFrontOriginAccessIdentity': {
            'Id': 'string',
            'S3CanonicalUserId': 'string',
            'CloudFrontOriginAccessIdentityConfig': {
                'CallerReference': 'string',
                'Comment': 'string'
            }
        },
        'ETag': 'string'
    }
    
    
    """
    pass

def get_cloud_front_origin_access_identity_config(Id=None):
    """
    Get the configuration information about an origin access identity.
    See also: AWS API Documentation
    
    
    :example: response = client.get_cloud_front_origin_access_identity_config(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The identity's ID.
            

    :rtype: dict
    :return: {
        'CloudFrontOriginAccessIdentityConfig': {
            'CallerReference': 'string',
            'Comment': 'string'
        },
        'ETag': 'string'
    }
    
    
    """
    pass

def get_distribution(Id=None):
    """
    Get the information about a distribution.
    See also: AWS API Documentation
    
    
    :example: response = client.get_distribution(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The distribution's ID.
            

    :rtype: dict
    :return: {
        'Distribution': {
            'Id': 'string',
            'ARN': 'string',
            'Status': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'InProgressInvalidationBatches': 123,
            'DomainName': 'string',
            'ActiveTrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    {
                        'AwsAccountNumber': 'string',
                        'KeyPairIds': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                ]
            },
            'DistributionConfig': {
                'CallerReference': 'string',
                'Aliases': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'DefaultRootObject': 'string',
                'Origins': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Id': 'string',
                            'DomainName': 'string',
                            'OriginPath': 'string',
                            'CustomHeaders': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'HeaderName': 'string',
                                        'HeaderValue': 'string'
                                    },
                                ]
                            },
                            'S3OriginConfig': {
                                'OriginAccessIdentity': 'string'
                            },
                            'CustomOriginConfig': {
                                'HTTPPort': 123,
                                'HTTPSPort': 123,
                                'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                                'OriginSslProtocols': {
                                    'Quantity': 123,
                                    'Items': [
                                        'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                                    ]
                                },
                                'OriginReadTimeout': 123,
                                'OriginKeepaliveTimeout': 123
                            }
                        },
                    ]
                },
                'OriginGroups': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Id': 'string',
                            'FailoverCriteria': {
                                'StatusCodes': {
                                    'Quantity': 123,
                                    'Items': [
                                        123,
                                    ]
                                }
                            },
                            'Members': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'OriginId': 'string'
                                    },
                                ]
                            }
                        },
                    ]
                },
                'DefaultCacheBehavior': {
                    'TargetOriginId': 'string',
                    'ForwardedValues': {
                        'QueryString': True|False,
                        'Cookies': {
                            'Forward': 'none'|'whitelist'|'all',
                            'WhitelistedNames': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'Headers': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'QueryStringCacheKeys': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'TrustedSigners': {
                        'Enabled': True|False,
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                    'MinTTL': 123,
                    'AllowedMethods': {
                        'Quantity': 123,
                        'Items': [
                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                        ],
                        'CachedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ]
                        }
                    },
                    'SmoothStreaming': True|False,
                    'DefaultTTL': 123,
                    'MaxTTL': 123,
                    'Compress': True|False,
                    'LambdaFunctionAssociations': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'LambdaFunctionARN': 'string',
                                'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                'IncludeBody': True|False
                            },
                        ]
                    },
                    'FieldLevelEncryptionId': 'string'
                },
                'CacheBehaviors': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'PathPattern': 'string',
                            'TargetOriginId': 'string',
                            'ForwardedValues': {
                                'QueryString': True|False,
                                'Cookies': {
                                    'Forward': 'none'|'whitelist'|'all',
                                    'WhitelistedNames': {
                                        'Quantity': 123,
                                        'Items': [
                                            'string',
                                        ]
                                    }
                                },
                                'Headers': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                },
                                'QueryStringCacheKeys': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                            'TrustedSigners': {
                                'Enabled': True|False,
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            },
                            'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                            'MinTTL': 123,
                            'AllowedMethods': {
                                'Quantity': 123,
                                'Items': [
                                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                ],
                                'CachedMethods': {
                                    'Quantity': 123,
                                    'Items': [
                                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                    ]
                                }
                            },
                            'SmoothStreaming': True|False,
                            'DefaultTTL': 123,
                            'MaxTTL': 123,
                            'Compress': True|False,
                            'LambdaFunctionAssociations': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'LambdaFunctionARN': 'string',
                                        'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                        'IncludeBody': True|False
                                    },
                                ]
                            },
                            'FieldLevelEncryptionId': 'string'
                        },
                    ]
                },
                'CustomErrorResponses': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'ErrorCode': 123,
                            'ResponsePagePath': 'string',
                            'ResponseCode': 'string',
                            'ErrorCachingMinTTL': 123
                        },
                    ]
                },
                'Comment': 'string',
                'Logging': {
                    'Enabled': True|False,
                    'IncludeCookies': True|False,
                    'Bucket': 'string',
                    'Prefix': 'string'
                },
                'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                'Enabled': True|False,
                'ViewerCertificate': {
                    'CloudFrontDefaultCertificate': True|False,
                    'IAMCertificateId': 'string',
                    'ACMCertificateArn': 'string',
                    'SSLSupportMethod': 'sni-only'|'vip',
                    'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
                    'Certificate': 'string',
                    'CertificateSource': 'cloudfront'|'iam'|'acm'
                },
                'Restrictions': {
                    'GeoRestriction': {
                        'RestrictionType': 'blacklist'|'whitelist'|'none',
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
                'WebACLId': 'string',
                'HttpVersion': 'http1.1'|'http2',
                'IsIPV6Enabled': True|False
            }
        },
        'ETag': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_distribution_config(Id=None):
    """
    Get the configuration information about a distribution.
    See also: AWS API Documentation
    
    
    :example: response = client.get_distribution_config(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The distribution's ID.
            

    :rtype: dict
    :return: {
        'DistributionConfig': {
            'CallerReference': 'string',
            'Aliases': {
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'DefaultRootObject': 'string',
            'Origins': {
                'Quantity': 123,
                'Items': [
                    {
                        'Id': 'string',
                        'DomainName': 'string',
                        'OriginPath': 'string',
                        'CustomHeaders': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'HeaderName': 'string',
                                    'HeaderValue': 'string'
                                },
                            ]
                        },
                        'S3OriginConfig': {
                            'OriginAccessIdentity': 'string'
                        },
                        'CustomOriginConfig': {
                            'HTTPPort': 123,
                            'HTTPSPort': 123,
                            'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                            'OriginSslProtocols': {
                                'Quantity': 123,
                                'Items': [
                                    'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                                ]
                            },
                            'OriginReadTimeout': 123,
                            'OriginKeepaliveTimeout': 123
                        }
                    },
                ]
            },
            'OriginGroups': {
                'Quantity': 123,
                'Items': [
                    {
                        'Id': 'string',
                        'FailoverCriteria': {
                            'StatusCodes': {
                                'Quantity': 123,
                                'Items': [
                                    123,
                                ]
                            }
                        },
                        'Members': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'OriginId': 'string'
                                },
                            ]
                        }
                    },
                ]
            },
            'DefaultCacheBehavior': {
                'TargetOriginId': 'string',
                'ForwardedValues': {
                    'QueryString': True|False,
                    'Cookies': {
                        'Forward': 'none'|'whitelist'|'all',
                        'WhitelistedNames': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'Headers': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'QueryStringCacheKeys': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
                'TrustedSigners': {
                    'Enabled': True|False,
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                'MinTTL': 123,
                'AllowedMethods': {
                    'Quantity': 123,
                    'Items': [
                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                    ],
                    'CachedMethods': {
                        'Quantity': 123,
                        'Items': [
                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                        ]
                    }
                },
                'SmoothStreaming': True|False,
                'DefaultTTL': 123,
                'MaxTTL': 123,
                'Compress': True|False,
                'LambdaFunctionAssociations': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'LambdaFunctionARN': 'string',
                            'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                            'IncludeBody': True|False
                        },
                    ]
                },
                'FieldLevelEncryptionId': 'string'
            },
            'CacheBehaviors': {
                'Quantity': 123,
                'Items': [
                    {
                        'PathPattern': 'string',
                        'TargetOriginId': 'string',
                        'ForwardedValues': {
                            'QueryString': True|False,
                            'Cookies': {
                                'Forward': 'none'|'whitelist'|'all',
                                'WhitelistedNames': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                            'Headers': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            },
                            'QueryStringCacheKeys': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'TrustedSigners': {
                            'Enabled': True|False,
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                        'MinTTL': 123,
                        'AllowedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ],
                            'CachedMethods': {
                                'Quantity': 123,
                                'Items': [
                                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                ]
                            }
                        },
                        'SmoothStreaming': True|False,
                        'DefaultTTL': 123,
                        'MaxTTL': 123,
                        'Compress': True|False,
                        'LambdaFunctionAssociations': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'LambdaFunctionARN': 'string',
                                    'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                    'IncludeBody': True|False
                                },
                            ]
                        },
                        'FieldLevelEncryptionId': 'string'
                    },
                ]
            },
            'CustomErrorResponses': {
                'Quantity': 123,
                'Items': [
                    {
                        'ErrorCode': 123,
                        'ResponsePagePath': 'string',
                        'ResponseCode': 'string',
                        'ErrorCachingMinTTL': 123
                    },
                ]
            },
            'Comment': 'string',
            'Logging': {
                'Enabled': True|False,
                'IncludeCookies': True|False,
                'Bucket': 'string',
                'Prefix': 'string'
            },
            'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
            'Enabled': True|False,
            'ViewerCertificate': {
                'CloudFrontDefaultCertificate': True|False,
                'IAMCertificateId': 'string',
                'ACMCertificateArn': 'string',
                'SSLSupportMethod': 'sni-only'|'vip',
                'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
                'Certificate': 'string',
                'CertificateSource': 'cloudfront'|'iam'|'acm'
            },
            'Restrictions': {
                'GeoRestriction': {
                    'RestrictionType': 'blacklist'|'whitelist'|'none',
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                }
            },
            'WebACLId': 'string',
            'HttpVersion': 'http1.1'|'http2',
            'IsIPV6Enabled': True|False
        },
        'ETag': 'string'
    }
    
    
    :returns: 
    If you configured Amazon S3 Transfer Acceleration for your bucket, don't specify the s3-accelerate endpoint for DomainName .
    The bucket name must be between 3 and 63 characters long (inclusive).
    The bucket name must contain only lowercase characters, numbers, periods, underscores, and dashes.
    The bucket name must not contain adjacent periods.
    
    """
    pass

def get_field_level_encryption(Id=None):
    """
    Get the field-level encryption configuration information.
    See also: AWS API Documentation
    
    
    :example: response = client.get_field_level_encryption(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            Request the ID for the field-level encryption configuration information.
            

    :rtype: dict
    :return: {
        'FieldLevelEncryption': {
            'Id': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'FieldLevelEncryptionConfig': {
                'CallerReference': 'string',
                'Comment': 'string',
                'QueryArgProfileConfig': {
                    'ForwardWhenQueryArgProfileIsUnknown': True|False,
                    'QueryArgProfiles': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'QueryArg': 'string',
                                'ProfileId': 'string'
                            },
                        ]
                    }
                },
                'ContentTypeProfileConfig': {
                    'ForwardWhenContentTypeIsUnknown': True|False,
                    'ContentTypeProfiles': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'Format': 'URLEncoded',
                                'ProfileId': 'string',
                                'ContentType': 'string'
                            },
                        ]
                    }
                }
            }
        },
        'ETag': 'string'
    }
    
    
    """
    pass

def get_field_level_encryption_config(Id=None):
    """
    Get the field-level encryption configuration information.
    See also: AWS API Documentation
    
    
    :example: response = client.get_field_level_encryption_config(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            Request the ID for the field-level encryption configuration information.
            

    :rtype: dict
    :return: {
        'FieldLevelEncryptionConfig': {
            'CallerReference': 'string',
            'Comment': 'string',
            'QueryArgProfileConfig': {
                'ForwardWhenQueryArgProfileIsUnknown': True|False,
                'QueryArgProfiles': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'QueryArg': 'string',
                            'ProfileId': 'string'
                        },
                    ]
                }
            },
            'ContentTypeProfileConfig': {
                'ForwardWhenContentTypeIsUnknown': True|False,
                'ContentTypeProfiles': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Format': 'URLEncoded',
                            'ProfileId': 'string',
                            'ContentType': 'string'
                        },
                    ]
                }
            }
        },
        'ETag': 'string'
    }
    
    
    """
    pass

def get_field_level_encryption_profile(Id=None):
    """
    Get the field-level encryption profile information.
    See also: AWS API Documentation
    
    
    :example: response = client.get_field_level_encryption_profile(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            Get the ID for the field-level encryption profile information.
            

    :rtype: dict
    :return: {
        'FieldLevelEncryptionProfile': {
            'Id': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'FieldLevelEncryptionProfileConfig': {
                'Name': 'string',
                'CallerReference': 'string',
                'Comment': 'string',
                'EncryptionEntities': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'PublicKeyId': 'string',
                            'ProviderId': 'string',
                            'FieldPatterns': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                    ]
                }
            }
        },
        'ETag': 'string'
    }
    
    
    """
    pass

def get_field_level_encryption_profile_config(Id=None):
    """
    Get the field-level encryption profile configuration information.
    See also: AWS API Documentation
    
    
    :example: response = client.get_field_level_encryption_profile_config(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            Get the ID for the field-level encryption profile configuration information.
            

    :rtype: dict
    :return: {
        'FieldLevelEncryptionProfileConfig': {
            'Name': 'string',
            'CallerReference': 'string',
            'Comment': 'string',
            'EncryptionEntities': {
                'Quantity': 123,
                'Items': [
                    {
                        'PublicKeyId': 'string',
                        'ProviderId': 'string',
                        'FieldPatterns': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                ]
            }
        },
        'ETag': 'string'
    }
    
    
    """
    pass

def get_invalidation(DistributionId=None, Id=None):
    """
    Get the information about an invalidation.
    See also: AWS API Documentation
    
    
    :example: response = client.get_invalidation(
        DistributionId='string',
        Id='string'
    )
    
    
    :type DistributionId: string
    :param DistributionId: [REQUIRED]
            The distribution's ID.
            

    :type Id: string
    :param Id: [REQUIRED]
            The identifier for the invalidation request, for example, IDFDVBD632BHDS5 .
            

    :rtype: dict
    :return: {
        'Invalidation': {
            'Id': 'string',
            'Status': 'string',
            'CreateTime': datetime(2015, 1, 1),
            'InvalidationBatch': {
                'Paths': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'CallerReference': 'string'
            }
        }
    }
    
    
    :returns: 
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

def get_public_key(Id=None):
    """
    Get the public key information.
    See also: AWS API Documentation
    
    
    :example: response = client.get_public_key(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            Request the ID for the public key.
            

    :rtype: dict
    :return: {
        'PublicKey': {
            'Id': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'PublicKeyConfig': {
                'CallerReference': 'string',
                'Name': 'string',
                'EncodedKey': 'string',
                'Comment': 'string'
            }
        },
        'ETag': 'string'
    }
    
    
    """
    pass

def get_public_key_config(Id=None):
    """
    Return public key configuration informaation
    See also: AWS API Documentation
    
    
    :example: response = client.get_public_key_config(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            Request the ID for the public key configuration.
            

    :rtype: dict
    :return: {
        'PublicKeyConfig': {
            'CallerReference': 'string',
            'Name': 'string',
            'EncodedKey': 'string',
            'Comment': 'string'
        },
        'ETag': 'string'
    }
    
    
    """
    pass

def get_streaming_distribution(Id=None):
    """
    Gets information about a specified RTMP distribution, including the distribution configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.get_streaming_distribution(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The streaming distribution's ID.
            

    :rtype: dict
    :return: {
        'StreamingDistribution': {
            'Id': 'string',
            'ARN': 'string',
            'Status': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'DomainName': 'string',
            'ActiveTrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    {
                        'AwsAccountNumber': 'string',
                        'KeyPairIds': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                ]
            },
            'StreamingDistributionConfig': {
                'CallerReference': 'string',
                'S3Origin': {
                    'DomainName': 'string',
                    'OriginAccessIdentity': 'string'
                },
                'Aliases': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'Comment': 'string',
                'Logging': {
                    'Enabled': True|False,
                    'Bucket': 'string',
                    'Prefix': 'string'
                },
                'TrustedSigners': {
                    'Enabled': True|False,
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                'Enabled': True|False
            }
        },
        'ETag': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_streaming_distribution_config(Id=None):
    """
    Get the configuration information about a streaming distribution.
    See also: AWS API Documentation
    
    
    :example: response = client.get_streaming_distribution_config(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The streaming distribution's ID.
            

    :rtype: dict
    :return: {
        'StreamingDistributionConfig': {
            'CallerReference': 'string',
            'S3Origin': {
                'DomainName': 'string',
                'OriginAccessIdentity': 'string'
            },
            'Aliases': {
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'Comment': 'string',
            'Logging': {
                'Enabled': True|False,
                'Bucket': 'string',
                'Prefix': 'string'
            },
            'TrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
            'Enabled': True|False
        },
        'ETag': 'string'
    }
    
    
    :returns: 
    (string) --
    
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

def list_cloud_front_origin_access_identities(Marker=None, MaxItems=None):
    """
    Lists origin access identities.
    See also: AWS API Documentation
    
    
    :example: response = client.list_cloud_front_origin_access_identities(
        Marker='string',
        MaxItems='string'
    )
    
    
    :type Marker: string
    :param Marker: Use this when paginating results to indicate where to begin in your list of origin access identities. The results include identities in the list that occur after the marker. To get the next page of results, set the Marker to the value of the NextMarker from the current page's response (which is also the ID of the last identity on that page).

    :type MaxItems: string
    :param MaxItems: The maximum number of origin access identities you want in the response body.

    :rtype: dict
    :return: {
        'CloudFrontOriginAccessIdentityList': {
            'Marker': 'string',
            'NextMarker': 'string',
            'MaxItems': 123,
            'IsTruncated': True|False,
            'Quantity': 123,
            'Items': [
                {
                    'Id': 'string',
                    'S3CanonicalUserId': 'string',
                    'Comment': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def list_distributions(Marker=None, MaxItems=None):
    """
    List distributions.
    See also: AWS API Documentation
    
    
    :example: response = client.list_distributions(
        Marker='string',
        MaxItems='string'
    )
    
    
    :type Marker: string
    :param Marker: Use this when paginating results to indicate where to begin in your list of distributions. The results include distributions in the list that occur after the marker. To get the next page of results, set the Marker to the value of the NextMarker from the current page's response (which is also the ID of the last distribution on that page).

    :type MaxItems: string
    :param MaxItems: The maximum number of distributions you want in the response body.

    :rtype: dict
    :return: {
        'DistributionList': {
            'Marker': 'string',
            'NextMarker': 'string',
            'MaxItems': 123,
            'IsTruncated': True|False,
            'Quantity': 123,
            'Items': [
                {
                    'Id': 'string',
                    'ARN': 'string',
                    'Status': 'string',
                    'LastModifiedTime': datetime(2015, 1, 1),
                    'DomainName': 'string',
                    'Aliases': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'Origins': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'Id': 'string',
                                'DomainName': 'string',
                                'OriginPath': 'string',
                                'CustomHeaders': {
                                    'Quantity': 123,
                                    'Items': [
                                        {
                                            'HeaderName': 'string',
                                            'HeaderValue': 'string'
                                        },
                                    ]
                                },
                                'S3OriginConfig': {
                                    'OriginAccessIdentity': 'string'
                                },
                                'CustomOriginConfig': {
                                    'HTTPPort': 123,
                                    'HTTPSPort': 123,
                                    'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                                    'OriginSslProtocols': {
                                        'Quantity': 123,
                                        'Items': [
                                            'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                                        ]
                                    },
                                    'OriginReadTimeout': 123,
                                    'OriginKeepaliveTimeout': 123
                                }
                            },
                        ]
                    },
                    'OriginGroups': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'Id': 'string',
                                'FailoverCriteria': {
                                    'StatusCodes': {
                                        'Quantity': 123,
                                        'Items': [
                                            123,
                                        ]
                                    }
                                },
                                'Members': {
                                    'Quantity': 123,
                                    'Items': [
                                        {
                                            'OriginId': 'string'
                                        },
                                    ]
                                }
                            },
                        ]
                    },
                    'DefaultCacheBehavior': {
                        'TargetOriginId': 'string',
                        'ForwardedValues': {
                            'QueryString': True|False,
                            'Cookies': {
                                'Forward': 'none'|'whitelist'|'all',
                                'WhitelistedNames': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                            'Headers': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            },
                            'QueryStringCacheKeys': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'TrustedSigners': {
                            'Enabled': True|False,
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                        'MinTTL': 123,
                        'AllowedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ],
                            'CachedMethods': {
                                'Quantity': 123,
                                'Items': [
                                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                ]
                            }
                        },
                        'SmoothStreaming': True|False,
                        'DefaultTTL': 123,
                        'MaxTTL': 123,
                        'Compress': True|False,
                        'LambdaFunctionAssociations': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'LambdaFunctionARN': 'string',
                                    'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                    'IncludeBody': True|False
                                },
                            ]
                        },
                        'FieldLevelEncryptionId': 'string'
                    },
                    'CacheBehaviors': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'PathPattern': 'string',
                                'TargetOriginId': 'string',
                                'ForwardedValues': {
                                    'QueryString': True|False,
                                    'Cookies': {
                                        'Forward': 'none'|'whitelist'|'all',
                                        'WhitelistedNames': {
                                            'Quantity': 123,
                                            'Items': [
                                                'string',
                                            ]
                                        }
                                    },
                                    'Headers': {
                                        'Quantity': 123,
                                        'Items': [
                                            'string',
                                        ]
                                    },
                                    'QueryStringCacheKeys': {
                                        'Quantity': 123,
                                        'Items': [
                                            'string',
                                        ]
                                    }
                                },
                                'TrustedSigners': {
                                    'Enabled': True|False,
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                },
                                'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                                'MinTTL': 123,
                                'AllowedMethods': {
                                    'Quantity': 123,
                                    'Items': [
                                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                    ],
                                    'CachedMethods': {
                                        'Quantity': 123,
                                        'Items': [
                                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                        ]
                                    }
                                },
                                'SmoothStreaming': True|False,
                                'DefaultTTL': 123,
                                'MaxTTL': 123,
                                'Compress': True|False,
                                'LambdaFunctionAssociations': {
                                    'Quantity': 123,
                                    'Items': [
                                        {
                                            'LambdaFunctionARN': 'string',
                                            'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                            'IncludeBody': True|False
                                        },
                                    ]
                                },
                                'FieldLevelEncryptionId': 'string'
                            },
                        ]
                    },
                    'CustomErrorResponses': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'ErrorCode': 123,
                                'ResponsePagePath': 'string',
                                'ResponseCode': 'string',
                                'ErrorCachingMinTTL': 123
                            },
                        ]
                    },
                    'Comment': 'string',
                    'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                    'Enabled': True|False,
                    'ViewerCertificate': {
                        'CloudFrontDefaultCertificate': True|False,
                        'IAMCertificateId': 'string',
                        'ACMCertificateArn': 'string',
                        'SSLSupportMethod': 'sni-only'|'vip',
                        'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
                        'Certificate': 'string',
                        'CertificateSource': 'cloudfront'|'iam'|'acm'
                    },
                    'Restrictions': {
                        'GeoRestriction': {
                            'RestrictionType': 'blacklist'|'whitelist'|'none',
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'WebACLId': 'string',
                    'HttpVersion': 'http1.1'|'http2',
                    'IsIPV6Enabled': True|False
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_distributions_by_web_acl_id(Marker=None, MaxItems=None, WebACLId=None):
    """
    List the distributions that are associated with a specified AWS WAF web ACL.
    See also: AWS API Documentation
    
    
    :example: response = client.list_distributions_by_web_acl_id(
        Marker='string',
        MaxItems='string',
        WebACLId='string'
    )
    
    
    :type Marker: string
    :param Marker: Use Marker and MaxItems to control pagination of results. If you have more than MaxItems distributions that satisfy the request, the response includes a NextMarker element. To get the next page of results, submit another request. For the value of Marker , specify the value of NextMarker from the last response. (For the first request, omit Marker .)

    :type MaxItems: string
    :param MaxItems: The maximum number of distributions that you want CloudFront to return in the response body. The maximum and default values are both 100.

    :type WebACLId: string
    :param WebACLId: [REQUIRED]
            The ID of the AWS WAF web ACL that you want to list the associated distributions. If you specify 'null' for the ID, the request returns a list of the distributions that aren't associated with a web ACL.
            

    :rtype: dict
    :return: {
        'DistributionList': {
            'Marker': 'string',
            'NextMarker': 'string',
            'MaxItems': 123,
            'IsTruncated': True|False,
            'Quantity': 123,
            'Items': [
                {
                    'Id': 'string',
                    'ARN': 'string',
                    'Status': 'string',
                    'LastModifiedTime': datetime(2015, 1, 1),
                    'DomainName': 'string',
                    'Aliases': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'Origins': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'Id': 'string',
                                'DomainName': 'string',
                                'OriginPath': 'string',
                                'CustomHeaders': {
                                    'Quantity': 123,
                                    'Items': [
                                        {
                                            'HeaderName': 'string',
                                            'HeaderValue': 'string'
                                        },
                                    ]
                                },
                                'S3OriginConfig': {
                                    'OriginAccessIdentity': 'string'
                                },
                                'CustomOriginConfig': {
                                    'HTTPPort': 123,
                                    'HTTPSPort': 123,
                                    'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                                    'OriginSslProtocols': {
                                        'Quantity': 123,
                                        'Items': [
                                            'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                                        ]
                                    },
                                    'OriginReadTimeout': 123,
                                    'OriginKeepaliveTimeout': 123
                                }
                            },
                        ]
                    },
                    'OriginGroups': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'Id': 'string',
                                'FailoverCriteria': {
                                    'StatusCodes': {
                                        'Quantity': 123,
                                        'Items': [
                                            123,
                                        ]
                                    }
                                },
                                'Members': {
                                    'Quantity': 123,
                                    'Items': [
                                        {
                                            'OriginId': 'string'
                                        },
                                    ]
                                }
                            },
                        ]
                    },
                    'DefaultCacheBehavior': {
                        'TargetOriginId': 'string',
                        'ForwardedValues': {
                            'QueryString': True|False,
                            'Cookies': {
                                'Forward': 'none'|'whitelist'|'all',
                                'WhitelistedNames': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                            'Headers': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            },
                            'QueryStringCacheKeys': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'TrustedSigners': {
                            'Enabled': True|False,
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                        'MinTTL': 123,
                        'AllowedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ],
                            'CachedMethods': {
                                'Quantity': 123,
                                'Items': [
                                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                ]
                            }
                        },
                        'SmoothStreaming': True|False,
                        'DefaultTTL': 123,
                        'MaxTTL': 123,
                        'Compress': True|False,
                        'LambdaFunctionAssociations': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'LambdaFunctionARN': 'string',
                                    'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                    'IncludeBody': True|False
                                },
                            ]
                        },
                        'FieldLevelEncryptionId': 'string'
                    },
                    'CacheBehaviors': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'PathPattern': 'string',
                                'TargetOriginId': 'string',
                                'ForwardedValues': {
                                    'QueryString': True|False,
                                    'Cookies': {
                                        'Forward': 'none'|'whitelist'|'all',
                                        'WhitelistedNames': {
                                            'Quantity': 123,
                                            'Items': [
                                                'string',
                                            ]
                                        }
                                    },
                                    'Headers': {
                                        'Quantity': 123,
                                        'Items': [
                                            'string',
                                        ]
                                    },
                                    'QueryStringCacheKeys': {
                                        'Quantity': 123,
                                        'Items': [
                                            'string',
                                        ]
                                    }
                                },
                                'TrustedSigners': {
                                    'Enabled': True|False,
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                },
                                'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                                'MinTTL': 123,
                                'AllowedMethods': {
                                    'Quantity': 123,
                                    'Items': [
                                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                    ],
                                    'CachedMethods': {
                                        'Quantity': 123,
                                        'Items': [
                                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                        ]
                                    }
                                },
                                'SmoothStreaming': True|False,
                                'DefaultTTL': 123,
                                'MaxTTL': 123,
                                'Compress': True|False,
                                'LambdaFunctionAssociations': {
                                    'Quantity': 123,
                                    'Items': [
                                        {
                                            'LambdaFunctionARN': 'string',
                                            'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                            'IncludeBody': True|False
                                        },
                                    ]
                                },
                                'FieldLevelEncryptionId': 'string'
                            },
                        ]
                    },
                    'CustomErrorResponses': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'ErrorCode': 123,
                                'ResponsePagePath': 'string',
                                'ResponseCode': 'string',
                                'ErrorCachingMinTTL': 123
                            },
                        ]
                    },
                    'Comment': 'string',
                    'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                    'Enabled': True|False,
                    'ViewerCertificate': {
                        'CloudFrontDefaultCertificate': True|False,
                        'IAMCertificateId': 'string',
                        'ACMCertificateArn': 'string',
                        'SSLSupportMethod': 'sni-only'|'vip',
                        'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
                        'Certificate': 'string',
                        'CertificateSource': 'cloudfront'|'iam'|'acm'
                    },
                    'Restrictions': {
                        'GeoRestriction': {
                            'RestrictionType': 'blacklist'|'whitelist'|'none',
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'WebACLId': 'string',
                    'HttpVersion': 'http1.1'|'http2',
                    'IsIPV6Enabled': True|False
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_field_level_encryption_configs(Marker=None, MaxItems=None):
    """
    List all field-level encryption configurations that have been created in CloudFront for this account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_field_level_encryption_configs(
        Marker='string',
        MaxItems='string'
    )
    
    
    :type Marker: string
    :param Marker: Use this when paginating results to indicate where to begin in your list of configurations. The results include configurations in the list that occur after the marker. To get the next page of results, set the Marker to the value of the NextMarker from the current page's response (which is also the ID of the last configuration on that page).

    :type MaxItems: string
    :param MaxItems: The maximum number of field-level encryption configurations you want in the response body.

    :rtype: dict
    :return: {
        'FieldLevelEncryptionList': {
            'NextMarker': 'string',
            'MaxItems': 123,
            'Quantity': 123,
            'Items': [
                {
                    'Id': 'string',
                    'LastModifiedTime': datetime(2015, 1, 1),
                    'Comment': 'string',
                    'QueryArgProfileConfig': {
                        'ForwardWhenQueryArgProfileIsUnknown': True|False,
                        'QueryArgProfiles': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'QueryArg': 'string',
                                    'ProfileId': 'string'
                                },
                            ]
                        }
                    },
                    'ContentTypeProfileConfig': {
                        'ForwardWhenContentTypeIsUnknown': True|False,
                        'ContentTypeProfiles': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'Format': 'URLEncoded',
                                    'ProfileId': 'string',
                                    'ContentType': 'string'
                                },
                            ]
                        }
                    }
                },
            ]
        }
    }
    
    
    """
    pass

def list_field_level_encryption_profiles(Marker=None, MaxItems=None):
    """
    Request a list of field-level encryption profiles that have been created in CloudFront for this account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_field_level_encryption_profiles(
        Marker='string',
        MaxItems='string'
    )
    
    
    :type Marker: string
    :param Marker: Use this when paginating results to indicate where to begin in your list of profiles. The results include profiles in the list that occur after the marker. To get the next page of results, set the Marker to the value of the NextMarker from the current page's response (which is also the ID of the last profile on that page).

    :type MaxItems: string
    :param MaxItems: The maximum number of field-level encryption profiles you want in the response body.

    :rtype: dict
    :return: {
        'FieldLevelEncryptionProfileList': {
            'NextMarker': 'string',
            'MaxItems': 123,
            'Quantity': 123,
            'Items': [
                {
                    'Id': 'string',
                    'LastModifiedTime': datetime(2015, 1, 1),
                    'Name': 'string',
                    'EncryptionEntities': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'PublicKeyId': 'string',
                                'ProviderId': 'string',
                                'FieldPatterns': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                        ]
                    },
                    'Comment': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_invalidations(DistributionId=None, Marker=None, MaxItems=None):
    """
    Lists invalidation batches.
    See also: AWS API Documentation
    
    
    :example: response = client.list_invalidations(
        DistributionId='string',
        Marker='string',
        MaxItems='string'
    )
    
    
    :type DistributionId: string
    :param DistributionId: [REQUIRED]
            The distribution's ID.
            

    :type Marker: string
    :param Marker: Use this parameter when paginating results to indicate where to begin in your list of invalidation batches. Because the results are returned in decreasing order from most recent to oldest, the most recent results are on the first page, the second page will contain earlier results, and so on. To get the next page of results, set Marker to the value of the NextMarker from the current page's response. This value is the same as the ID of the last invalidation batch on that page.

    :type MaxItems: string
    :param MaxItems: The maximum number of invalidation batches that you want in the response body.

    :rtype: dict
    :return: {
        'InvalidationList': {
            'Marker': 'string',
            'NextMarker': 'string',
            'MaxItems': 123,
            'IsTruncated': True|False,
            'Quantity': 123,
            'Items': [
                {
                    'Id': 'string',
                    'CreateTime': datetime(2015, 1, 1),
                    'Status': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def list_public_keys(Marker=None, MaxItems=None):
    """
    List all public keys that have been added to CloudFront for this account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_public_keys(
        Marker='string',
        MaxItems='string'
    )
    
    
    :type Marker: string
    :param Marker: Use this when paginating results to indicate where to begin in your list of public keys. The results include public keys in the list that occur after the marker. To get the next page of results, set the Marker to the value of the NextMarker from the current page's response (which is also the ID of the last public key on that page).

    :type MaxItems: string
    :param MaxItems: The maximum number of public keys you want in the response body.

    :rtype: dict
    :return: {
        'PublicKeyList': {
            'NextMarker': 'string',
            'MaxItems': 123,
            'Quantity': 123,
            'Items': [
                {
                    'Id': 'string',
                    'Name': 'string',
                    'CreatedTime': datetime(2015, 1, 1),
                    'EncodedKey': 'string',
                    'Comment': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def list_streaming_distributions(Marker=None, MaxItems=None):
    """
    List streaming distributions.
    See also: AWS API Documentation
    
    
    :example: response = client.list_streaming_distributions(
        Marker='string',
        MaxItems='string'
    )
    
    
    :type Marker: string
    :param Marker: The value that you provided for the Marker request parameter.

    :type MaxItems: string
    :param MaxItems: The value that you provided for the MaxItems request parameter.

    :rtype: dict
    :return: {
        'StreamingDistributionList': {
            'Marker': 'string',
            'NextMarker': 'string',
            'MaxItems': 123,
            'IsTruncated': True|False,
            'Quantity': 123,
            'Items': [
                {
                    'Id': 'string',
                    'ARN': 'string',
                    'Status': 'string',
                    'LastModifiedTime': datetime(2015, 1, 1),
                    'DomainName': 'string',
                    'S3Origin': {
                        'DomainName': 'string',
                        'OriginAccessIdentity': 'string'
                    },
                    'Aliases': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'TrustedSigners': {
                        'Enabled': True|False,
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'Comment': 'string',
                    'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                    'Enabled': True|False
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tags_for_resource(Resource=None):
    """
    List tags for a CloudFront resource.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags_for_resource(
        Resource='string'
    )
    
    
    :type Resource: string
    :param Resource: [REQUIRED]
            An ARN of a CloudFront resource.
            

    :rtype: dict
    :return: {
        'Tags': {
            'Items': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def tag_resource(Resource=None, Tags=None):
    """
    Add tags to a CloudFront resource.
    See also: AWS API Documentation
    
    
    :example: response = client.tag_resource(
        Resource='string',
        Tags={
            'Items': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    )
    
    
    :type Resource: string
    :param Resource: [REQUIRED]
            An ARN of a CloudFront resource.
            

    :type Tags: dict
    :param Tags: [REQUIRED]
            A complex type that contains zero or more Tag elements.
            Items (list) --A complex type that contains Tag elements.
            (dict) --A complex type that contains Tag key and Tag value.
            Key (string) -- [REQUIRED]A string that contains Tag key.
            The string length should be between 1 and 128 characters. Valid characters include a-z , A-Z , 0-9 , space, and the special characters _ - . : / = + @ .
            Value (string) --A string that contains an optional Tag value.
            The string length should be between 0 and 256 characters. Valid characters include a-z , A-Z , 0-9 , space, and the special characters _ - . : / = + @ .
            
            

    """
    pass

def untag_resource(Resource=None, TagKeys=None):
    """
    Remove tags from a CloudFront resource.
    See also: AWS API Documentation
    
    
    :example: response = client.untag_resource(
        Resource='string',
        TagKeys={
            'Items': [
                'string',
            ]
        }
    )
    
    
    :type Resource: string
    :param Resource: [REQUIRED]
            An ARN of a CloudFront resource.
            

    :type TagKeys: dict
    :param TagKeys: [REQUIRED]
            A complex type that contains zero or more Tag key elements.
            Items (list) --A complex type that contains Tag key elements.
            (string) --A string that contains Tag key.
            The string length should be between 1 and 128 characters. Valid characters include a-z , A-Z , 0-9 , space, and the special characters _ - . : / = + @ .
            
            

    """
    pass

def update_cloud_front_origin_access_identity(CloudFrontOriginAccessIdentityConfig=None, Id=None, IfMatch=None):
    """
    Update an origin access identity.
    See also: AWS API Documentation
    
    
    :example: response = client.update_cloud_front_origin_access_identity(
        CloudFrontOriginAccessIdentityConfig={
            'CallerReference': 'string',
            'Comment': 'string'
        },
        Id='string',
        IfMatch='string'
    )
    
    
    :type CloudFrontOriginAccessIdentityConfig: dict
    :param CloudFrontOriginAccessIdentityConfig: [REQUIRED]
            The identity's configuration information.
            CallerReference (string) -- [REQUIRED]A unique value (for example, a date-time stamp) that ensures that the request can't be replayed.
            If the value of CallerReference is new (regardless of the content of the CloudFrontOriginAccessIdentityConfig object), a new origin access identity is created.
            If the CallerReference is a value already sent in a previous identity request, and the content of the CloudFrontOriginAccessIdentityConfig is identical to the original request (ignoring white space), the response includes the same information returned to the original request.
            If the CallerReference is a value you already sent in a previous request to create an identity, but the content of the CloudFrontOriginAccessIdentityConfig is different from the original request, CloudFront returns a CloudFrontOriginAccessIdentityAlreadyExists error.
            Comment (string) -- [REQUIRED]Any comments you want to include about the origin access identity.
            

    :type Id: string
    :param Id: [REQUIRED]
            The identity's id.
            

    :type IfMatch: string
    :param IfMatch: The value of the ETag header that you received when retrieving the identity's configuration. For example: E2QWRUHAPOMQZL .

    :rtype: dict
    :return: {
        'CloudFrontOriginAccessIdentity': {
            'Id': 'string',
            'S3CanonicalUserId': 'string',
            'CloudFrontOriginAccessIdentityConfig': {
                'CallerReference': 'string',
                'Comment': 'string'
            }
        },
        'ETag': 'string'
    }
    
    
    """
    pass

def update_distribution(DistributionConfig=None, Id=None, IfMatch=None):
    """
    Updates the configuration for a web distribution.
    The update process includes getting the current distribution configuration, updating the XML document that is returned to make your changes, and then submitting an UpdateDistribution request to make the updates.
    For information about updating a distribution using the CloudFront console instead, see Creating a Distribution in the Amazon CloudFront Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.update_distribution(
        DistributionConfig={
            'CallerReference': 'string',
            'Aliases': {
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'DefaultRootObject': 'string',
            'Origins': {
                'Quantity': 123,
                'Items': [
                    {
                        'Id': 'string',
                        'DomainName': 'string',
                        'OriginPath': 'string',
                        'CustomHeaders': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'HeaderName': 'string',
                                    'HeaderValue': 'string'
                                },
                            ]
                        },
                        'S3OriginConfig': {
                            'OriginAccessIdentity': 'string'
                        },
                        'CustomOriginConfig': {
                            'HTTPPort': 123,
                            'HTTPSPort': 123,
                            'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                            'OriginSslProtocols': {
                                'Quantity': 123,
                                'Items': [
                                    'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                                ]
                            },
                            'OriginReadTimeout': 123,
                            'OriginKeepaliveTimeout': 123
                        }
                    },
                ]
            },
            'OriginGroups': {
                'Quantity': 123,
                'Items': [
                    {
                        'Id': 'string',
                        'FailoverCriteria': {
                            'StatusCodes': {
                                'Quantity': 123,
                                'Items': [
                                    123,
                                ]
                            }
                        },
                        'Members': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'OriginId': 'string'
                                },
                            ]
                        }
                    },
                ]
            },
            'DefaultCacheBehavior': {
                'TargetOriginId': 'string',
                'ForwardedValues': {
                    'QueryString': True|False,
                    'Cookies': {
                        'Forward': 'none'|'whitelist'|'all',
                        'WhitelistedNames': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'Headers': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'QueryStringCacheKeys': {
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
                'TrustedSigners': {
                    'Enabled': True|False,
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                'MinTTL': 123,
                'AllowedMethods': {
                    'Quantity': 123,
                    'Items': [
                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                    ],
                    'CachedMethods': {
                        'Quantity': 123,
                        'Items': [
                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                        ]
                    }
                },
                'SmoothStreaming': True|False,
                'DefaultTTL': 123,
                'MaxTTL': 123,
                'Compress': True|False,
                'LambdaFunctionAssociations': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'LambdaFunctionARN': 'string',
                            'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                            'IncludeBody': True|False
                        },
                    ]
                },
                'FieldLevelEncryptionId': 'string'
            },
            'CacheBehaviors': {
                'Quantity': 123,
                'Items': [
                    {
                        'PathPattern': 'string',
                        'TargetOriginId': 'string',
                        'ForwardedValues': {
                            'QueryString': True|False,
                            'Cookies': {
                                'Forward': 'none'|'whitelist'|'all',
                                'WhitelistedNames': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                            'Headers': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            },
                            'QueryStringCacheKeys': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'TrustedSigners': {
                            'Enabled': True|False,
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                        'MinTTL': 123,
                        'AllowedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ],
                            'CachedMethods': {
                                'Quantity': 123,
                                'Items': [
                                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                ]
                            }
                        },
                        'SmoothStreaming': True|False,
                        'DefaultTTL': 123,
                        'MaxTTL': 123,
                        'Compress': True|False,
                        'LambdaFunctionAssociations': {
                            'Quantity': 123,
                            'Items': [
                                {
                                    'LambdaFunctionARN': 'string',
                                    'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                    'IncludeBody': True|False
                                },
                            ]
                        },
                        'FieldLevelEncryptionId': 'string'
                    },
                ]
            },
            'CustomErrorResponses': {
                'Quantity': 123,
                'Items': [
                    {
                        'ErrorCode': 123,
                        'ResponsePagePath': 'string',
                        'ResponseCode': 'string',
                        'ErrorCachingMinTTL': 123
                    },
                ]
            },
            'Comment': 'string',
            'Logging': {
                'Enabled': True|False,
                'IncludeCookies': True|False,
                'Bucket': 'string',
                'Prefix': 'string'
            },
            'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
            'Enabled': True|False,
            'ViewerCertificate': {
                'CloudFrontDefaultCertificate': True|False,
                'IAMCertificateId': 'string',
                'ACMCertificateArn': 'string',
                'SSLSupportMethod': 'sni-only'|'vip',
                'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
                'Certificate': 'string',
                'CertificateSource': 'cloudfront'|'iam'|'acm'
            },
            'Restrictions': {
                'GeoRestriction': {
                    'RestrictionType': 'blacklist'|'whitelist'|'none',
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                }
            },
            'WebACLId': 'string',
            'HttpVersion': 'http1.1'|'http2',
            'IsIPV6Enabled': True|False
        },
        Id='string',
        IfMatch='string'
    )
    
    
    :type DistributionConfig: dict
    :param DistributionConfig: [REQUIRED]
            The distribution's configuration information.
            CallerReference (string) -- [REQUIRED]A unique value (for example, a date-time stamp) that ensures that the request can't be replayed.
            If the value of CallerReference is new (regardless of the content of the DistributionConfig object), CloudFront creates a new distribution.
            If CallerReference is a value that you already sent in a previous request to create a distribution, CloudFront returns a DistributionAlreadyExists error.
            Aliases (dict) --A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.
            Quantity (integer) -- [REQUIRED]The number of CNAME aliases, if any, that you want to associate with this distribution.
            Items (list) --A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.
            (string) --
            
            DefaultRootObject (string) --The object that you want CloudFront to request from your origin (for example, index.html ) when a viewer requests the root URL for your distribution (http://www.example.com ) instead of an object in your distribution (http://www.example.com/product-description.html ). Specifying a default root object avoids exposing the contents of your distribution.
            Specify only the object name, for example, index.html . Don't add a / before the object name.
            If you don't want to specify a default root object when you create a distribution, include an empty DefaultRootObject element.
            To delete the default root object from an existing distribution, update the distribution configuration and include an empty DefaultRootObject element.
            To replace the default root object, update the distribution configuration and specify the new object.
            For more information about the default root object, see Creating a Default Root Object in the Amazon CloudFront Developer Guide .
            Origins (dict) -- [REQUIRED]A complex type that contains information about origins for this distribution.
            Quantity (integer) -- [REQUIRED]The number of origins or origin groups for this distribution.
            Items (list) -- [REQUIRED]A complex type that contains origins or origin groups for this distribution.
            (dict) --A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web server), Amazon MediaStore, or other server from which CloudFront gets your files. This can also be an origin group, if you've created an origin group. You must specify at least one origin or origin group.
            For the current limit on the number of origins or origin groups that you can specify for a distribution, see Amazon CloudFront Limits in the AWS General Reference .
            Id (string) -- [REQUIRED]A unique identifier for the origin or origin group. The value of Id must be unique within the distribution.
            When you specify the value of TargetOriginId for the default cache behavior or for another cache behavior, you indicate the origin to which you want the cache behavior to route requests by specifying the value of the Id element for that origin. When a request matches the path pattern for that cache behavior, CloudFront routes the request to the specified origin. For more information, see Cache Behavior Settings in the Amazon CloudFront Developer Guide .
            DomainName (string) -- [REQUIRED]
            Amazon S3 origins : The DNS name of the Amazon S3 bucket from which you want CloudFront to get objects for this origin, for example, myawsbucket.s3.amazonaws.com . If you set up your bucket to be configured as a website endpoint, enter the Amazon S3 static website hosting endpoint for the bucket.
            For more information about specifying this value for different types of origins, see Origin Domain Name in the Amazon CloudFront Developer Guide .
            Constraints for Amazon S3 origins:
            If you configured Amazon S3 Transfer Acceleration for your bucket, don't specify the s3-accelerate endpoint for DomainName .
            The bucket name must be between 3 and 63 characters long (inclusive).
            The bucket name must contain only lowercase characters, numbers, periods, underscores, and dashes.
            The bucket name must not contain adjacent periods.
            Custom Origins : The DNS domain name for the HTTP server from which you want CloudFront to get objects for this origin, for example, www.example.com .
            Constraints for custom origins:
            DomainName must be a valid DNS name that contains only a-z, A-Z, 0-9, dot (.), hyphen (-), or underscore (_) characters.
            The name cannot exceed 128 characters.
            OriginPath (string) --An optional element that causes CloudFront to request your content from a directory in your Amazon S3 bucket or your custom origin. When you include the OriginPath element, specify the directory name, beginning with a / . CloudFront appends the directory name to the value of DomainName , for example, example.com/production . Do not include a / at the end of the directory name.
            For example, suppose you've specified the following values for your distribution:
            DomainName : An Amazon S3 bucket named myawsbucket .
            OriginPath : /production
            CNAME : example.com
            When a user enters example.com/index.html in a browser, CloudFront sends a request to Amazon S3 for myawsbucket/production/index.html .
            When a user enters example.com/acme/index.html in a browser, CloudFront sends a request to Amazon S3 for myawsbucket/production/acme/index.html .
            CustomHeaders (dict) --A complex type that contains names and values for the custom headers that you want.
            Quantity (integer) -- [REQUIRED]The number of custom headers, if any, for this distribution.
            Items (list) --
            Optional : A list that contains one OriginCustomHeader element for each custom header that you want CloudFront to forward to the origin. If Quantity is 0 , omit Items .
            (dict) --A complex type that contains HeaderName and HeaderValue elements, if any, for this distribution.
            HeaderName (string) -- [REQUIRED]The name of a header that you want CloudFront to forward to your origin. For more information, see Forwarding Custom Headers to Your Origin (Web Distributions Only) in the Amazon Amazon CloudFront Developer Guide .
            HeaderValue (string) -- [REQUIRED]The value for the header that you specified in the HeaderName field.
            
            S3OriginConfig (dict) --A complex type that contains information about the Amazon S3 origin. If the origin is a custom origin, use the CustomOriginConfig element instead.
            OriginAccessIdentity (string) -- [REQUIRED]The CloudFront origin access identity to associate with the origin. Use an origin access identity to configure the origin so that viewers can only access objects in an Amazon S3 bucket through CloudFront. The format of the value is:
            origin-access-identity/cloudfront/ID-of-origin-access-identity
            where `` ID-of-origin-access-identity `` is the value that CloudFront returned in the ID element when you created the origin access identity.
            If you want viewers to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element.
            To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element.
            To replace the origin access identity, update the distribution configuration and specify the new origin access identity.
            For more information about the origin access identity, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .
            CustomOriginConfig (dict) --A complex type that contains information about a custom origin. If the origin is an Amazon S3 bucket, use the S3OriginConfig element instead.
            HTTPPort (integer) -- [REQUIRED]The HTTP port the custom origin listens on.
            HTTPSPort (integer) -- [REQUIRED]The HTTPS port the custom origin listens on.
            OriginProtocolPolicy (string) -- [REQUIRED]The origin protocol policy to apply to your origin.
            OriginSslProtocols (dict) --The SSL/TLS protocols that you want CloudFront to use when communicating with your origin over HTTPS.
            Quantity (integer) -- [REQUIRED]The number of SSL/TLS protocols that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.
            Items (list) -- [REQUIRED]A list that contains allowed SSL/TLS protocols for this distribution.
            (string) --
            
            OriginReadTimeout (integer) --You can create a custom origin read timeout. All timeout units are in seconds. The default origin read timeout is 30 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 4 seconds; the maximum is 60 seconds.
            If you need to increase the maximum time limit, contact the AWS Support Center .
            OriginKeepaliveTimeout (integer) --You can create a custom keep-alive timeout. All timeout units are in seconds. The default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60 seconds.
            If you need to increase the maximum time limit, contact the AWS Support Center .
            
            
            OriginGroups (dict) --A complex type that contains information about origin groups for this distribution.
            Quantity (integer) -- [REQUIRED]The number of origin groups.
            Items (list) --The items (origin groups) in a distribution.
            (dict) --An origin group includes two origins (a primary origin and a second origin to failover to) and a failover criteria that you specify. You create an origin group to support origin failover in CloudFront. When you create or update a distribution, you can specifiy the origin group instead of a single origin, and CloudFront will failover from the primary origin to the second origin under the failover conditions that you've chosen.
            Id (string) -- [REQUIRED]The origin group's ID.
            FailoverCriteria (dict) -- [REQUIRED]A complex type that contains information about the failover criteria for an origin group.
            StatusCodes (dict) -- [REQUIRED]The status codes that, when returned from the primary origin, will trigger CloudFront to failover to the second origin.
            Quantity (integer) -- [REQUIRED]The number of status codes.
            Items (list) -- [REQUIRED]The items (status codes) for an origin group.
            (integer) --
            
            Members (dict) -- [REQUIRED]A complex type that contains information about the origins in an origin group.
            Quantity (integer) -- [REQUIRED]The number of origins in an origin group.
            Items (list) -- [REQUIRED]Items (origins) in an origin group.
            (dict) --An origin in an origin group.
            OriginId (string) -- [REQUIRED]The ID for an origin in an origin group.
            
            
            
            DefaultCacheBehavior (dict) -- [REQUIRED]A complex type that describes the default cache behavior if you don't specify a CacheBehavior element or if files don't match any of the values of PathPattern in CacheBehavior elements. You must create exactly one default cache behavior.
            TargetOriginId (string) -- [REQUIRED]The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.
            ForwardedValues (dict) -- [REQUIRED]A complex type that specifies how CloudFront handles query strings and cookies.
            QueryString (boolean) -- [REQUIRED]Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of QueryString and on the values that you specify for QueryStringCacheKeys , if any:
            If you specify true for QueryString and you don't specify any values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.
            If you specify true for QueryString and you specify one or more values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.
            If you specify false for QueryString , CloudFront doesn't forward any query string parameters to the origin, and doesn't cache based on query string parameters.
            For more information, see Configuring CloudFront to Cache Based on Query String Parameters in the Amazon CloudFront Developer Guide .
            Cookies (dict) -- [REQUIRED]A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see How CloudFront Forwards, Caches, and Logs Cookies in the Amazon CloudFront Developer Guide .
            Forward (string) -- [REQUIRED]Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the WhitelistedNames complex type.
            Amazon S3 doesn't process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the Forward element.
            WhitelistedNames (dict) --Required if you specify whitelist for the value of Forward: . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.
            If you specify all or none for the value of Forward , omit WhitelistedNames . If you change the value of Forward from whitelist to all or none and you don't delete the WhitelistedNames element and its child elements, CloudFront deletes them automatically.
            For the current limit on the number of cookie names that you can whitelist for each cache behavior, see Amazon CloudFront Limits in the AWS General Reference .
            Quantity (integer) -- [REQUIRED]The number of different cookies that you want CloudFront to forward to the origin for this cache behavior.
            Items (list) --A complex type that contains one Name element for each cookie that you want CloudFront to forward to the origin for this cache behavior.
            (string) --
            
            Headers (dict) --A complex type that specifies the Headers , if any, that you want CloudFront to base caching on for this cache behavior.
            Quantity (integer) -- [REQUIRED]The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:
            Forward all headers to your origin : Specify 1 for Quantity and * for Name .
            Warning
            CloudFront doesn't cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.
            Forward a whitelist of headers you specify : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in Name elements. CloudFront caches your objects based on the values in the specified headers.
            Forward only the default headers : Specify 0 for Quantity and omit Items . In this configuration, CloudFront doesn't cache based on the values in the request headers.
            Regardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:
            S3 bucket : See HTTP Request Headers That CloudFront Removes or Updates
            Custom origin : See HTTP Request Headers and CloudFront Behavior
            Items (list) --A list that contains one Name element for each header that you want CloudFront to use for caching in this cache behavior. If Quantity is 0 , omit Items .
            (string) --
            
            QueryStringCacheKeys (dict) --A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.
            Quantity (integer) -- [REQUIRED]The number of whitelisted query string parameters for this cache behavior.
            Items (list) --(Optional) A list that contains the query string parameters that you want CloudFront to use as a basis for caching for this cache behavior. If Quantity is 0, you can omit Items .
            (string) --
            
            TrustedSigners (dict) -- [REQUIRED]A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.
            If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items . For more information, see Serving Private Content through CloudFront in the Amazon Amazon CloudFront Developer Guide .
            If you don't want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items .
            To add, change, or remove one or more trusted signers, change Enabled to true (if it's currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
            Enabled (boolean) -- [REQUIRED]Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .
            Quantity (integer) -- [REQUIRED]The number of trusted signers for this cache behavior.
            Items (list) --
            Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .
            (string) --
            
            ViewerProtocolPolicy (string) -- [REQUIRED]The protocol that viewers can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern . You can specify the following options:
            allow-all : Viewers can use HTTP or HTTPS.
            redirect-to-https : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.
            https-only : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).
            For more information about requiring the HTTPS protocol, see Using an HTTPS Connection to Access Your Objects in the Amazon CloudFront Developer Guide .
            Note
            The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
            MinTTL (integer) -- [REQUIRED]The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) in the Amazon Amazon CloudFront Developer Guide .
            You must specify 0 for MinTTL if you configure CloudFront to forward all headers to your origin (under Headers , if you specify 1 for Quantity and * for Name ).
            AllowedMethods (dict) --A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:
            CloudFront forwards only GET and HEAD requests.
            CloudFront forwards only GET , HEAD , and OPTIONS requests.
            CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests.
            If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can't perform operations that you don't want them to. For example, you might not want users to have permissions to delete objects from your origin.
            Quantity (integer) -- [REQUIRED]The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET , HEAD , and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests).
            Items (list) -- [REQUIRED]A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.
            (string) --
            CachedMethods (dict) --A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:
            CloudFront caches responses to GET and HEAD requests.
            CloudFront caches responses to GET , HEAD , and OPTIONS requests.
            If you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.
            Quantity (integer) -- [REQUIRED]The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET , HEAD , and OPTIONS requests).
            Items (list) -- [REQUIRED]A complex type that contains the HTTP methods that you want CloudFront to cache responses to.
            (string) --
            
            SmoothStreaming (boolean) --Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true ; if not, specify false . If you specify true for SmoothStreaming , you can still distribute other content using this cache behavior if the content matches the value of PathPattern .
            DefaultTTL (integer) --The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
            MaxTTL (integer) --
            Compress (boolean) --Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true ; if not, specify false . For more information, see Serving Compressed Files in the Amazon CloudFront Developer Guide .
            LambdaFunctionAssociations (dict) --A complex type that contains zero or more Lambda function associations for a cache behavior.
            Quantity (integer) -- [REQUIRED]The number of Lambda function associations for this cache behavior.
            Items (list) --
            Optional : A complex type that contains LambdaFunctionAssociation items for this cache behavior. If Quantity is 0 , you can omit Items .
            (dict) --A complex type that contains a Lambda function association.
            LambdaFunctionARN (string) -- [REQUIRED]The ARN of the Lambda function. You must specify the ARN of a function version; you can't specify a Lambda alias or $LATEST.
            EventType (string) -- [REQUIRED]Specifies the event type that triggers a Lambda function invocation. You can specify the following values:
            viewer-request : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.
            origin-request : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn't execute.
            origin-response : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn't execute.
            viewer-response : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn't execute.
            IncludeBody (boolean) --A flag that allows a Lambda function to have read access to the body content. For more information, see Accessing the Request Body by Choosing the Include Body Option in the Amazon CloudFront Developer Guide.
            
            FieldLevelEncryptionId (string) --The value of ID for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.
            CacheBehaviors (dict) --A complex type that contains zero or more CacheBehavior elements.
            Quantity (integer) -- [REQUIRED]The number of cache behaviors for this distribution.
            Items (list) --Optional: A complex type that contains cache behaviors for this distribution. If Quantity is 0 , you can omit Items .
            (dict) --A complex type that describes how CloudFront processes requests.
            You must create at least as many cache behaviors (including the default cache behavior) as you have origins if you want CloudFront to distribute objects from all of the origins. Each cache behavior specifies the one origin from which you want CloudFront to get objects. If you have two origins and only the default cache behavior, the default cache behavior will cause CloudFront to get objects from one of the origins, but the other origin is never used.
            For the current limit on the number of cache behaviors that you can add to a distribution, see Amazon CloudFront Limits in the AWS General Reference .
            If you don't want to specify any cache behaviors, include only an empty CacheBehaviors element. Don't include an empty CacheBehavior element, or CloudFront returns a MalformedXML error.
            To delete all cache behaviors in an existing distribution, update the distribution configuration and include only an empty CacheBehaviors element.
            To add, change, or remove one or more cache behaviors, update the distribution configuration and specify all of the cache behaviors that you want to include in the updated distribution.
            For more information about cache behaviors, see Cache Behaviors in the Amazon CloudFront Developer Guide .
            PathPattern (string) -- [REQUIRED]The pattern (for example, images/*.jpg ) that specifies which requests to apply the behavior to. When CloudFront receives a viewer request, the requested path is compared with path patterns in the order in which cache behaviors are listed in the distribution.
            Note
            You can optionally include a slash (/ ) at the beginning of the path pattern. For example, /images/*.jpg . CloudFront behavior is the same with or without the leading / .
            The path pattern for the default cache behavior is * and cannot be changed. If the request for an object does not match the path pattern for any cache behaviors, CloudFront applies the behavior in the default cache behavior.
            For more information, see Path Pattern in the Amazon CloudFront Developer Guide .
            TargetOriginId (string) -- [REQUIRED]The value of ID for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior in your distribution.
            ForwardedValues (dict) -- [REQUIRED]A complex type that specifies how CloudFront handles query strings and cookies.
            QueryString (boolean) -- [REQUIRED]Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of QueryString and on the values that you specify for QueryStringCacheKeys , if any:
            If you specify true for QueryString and you don't specify any values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.
            If you specify true for QueryString and you specify one or more values for QueryStringCacheKeys , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.
            If you specify false for QueryString , CloudFront doesn't forward any query string parameters to the origin, and doesn't cache based on query string parameters.
            For more information, see Configuring CloudFront to Cache Based on Query String Parameters in the Amazon CloudFront Developer Guide .
            Cookies (dict) -- [REQUIRED]A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see How CloudFront Forwards, Caches, and Logs Cookies in the Amazon CloudFront Developer Guide .
            Forward (string) -- [REQUIRED]Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the WhitelistedNames complex type.
            Amazon S3 doesn't process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the Forward element.
            WhitelistedNames (dict) --Required if you specify whitelist for the value of Forward: . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.
            If you specify all or none for the value of Forward , omit WhitelistedNames . If you change the value of Forward from whitelist to all or none and you don't delete the WhitelistedNames element and its child elements, CloudFront deletes them automatically.
            For the current limit on the number of cookie names that you can whitelist for each cache behavior, see Amazon CloudFront Limits in the AWS General Reference .
            Quantity (integer) -- [REQUIRED]The number of different cookies that you want CloudFront to forward to the origin for this cache behavior.
            Items (list) --A complex type that contains one Name element for each cookie that you want CloudFront to forward to the origin for this cache behavior.
            (string) --
            
            Headers (dict) --A complex type that specifies the Headers , if any, that you want CloudFront to base caching on for this cache behavior.
            Quantity (integer) -- [REQUIRED]The number of different headers that you want CloudFront to base caching on for this cache behavior. You can configure each cache behavior in a web distribution to do one of the following:
            Forward all headers to your origin : Specify 1 for Quantity and * for Name .
            Warning
            CloudFront doesn't cache the objects that are associated with this cache behavior. Instead, CloudFront sends every request to the origin.
            Forward a whitelist of headers you specify : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in Name elements. CloudFront caches your objects based on the values in the specified headers.
            Forward only the default headers : Specify 0 for Quantity and omit Items . In this configuration, CloudFront doesn't cache based on the values in the request headers.
            Regardless of which option you choose, CloudFront forwards headers to your origin based on whether the origin is an S3 bucket or a custom origin. See the following documentation:
            S3 bucket : See HTTP Request Headers That CloudFront Removes or Updates
            Custom origin : See HTTP Request Headers and CloudFront Behavior
            Items (list) --A list that contains one Name element for each header that you want CloudFront to use for caching in this cache behavior. If Quantity is 0 , omit Items .
            (string) --
            
            QueryStringCacheKeys (dict) --A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.
            Quantity (integer) -- [REQUIRED]The number of whitelisted query string parameters for this cache behavior.
            Items (list) --(Optional) A list that contains the query string parameters that you want CloudFront to use as a basis for caching for this cache behavior. If Quantity is 0, you can omit Items .
            (string) --
            
            TrustedSigners (dict) -- [REQUIRED]A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.
            If you want to require signed URLs in requests for objects in the target origin that match the PathPattern for this cache behavior, specify true for Enabled , and specify the applicable values for Quantity and Items . For more information, see Serving Private Content through CloudFront in the Amazon Amazon CloudFront Developer Guide .
            If you don't want to require signed URLs in requests for objects that match PathPattern , specify false for Enabled and 0 for Quantity . Omit Items .
            To add, change, or remove one or more trusted signers, change Enabled to true (if it's currently false ), change Quantity as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
            Enabled (boolean) -- [REQUIRED]Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .
            Quantity (integer) -- [REQUIRED]The number of trusted signers for this cache behavior.
            Items (list) --
            Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .
            (string) --
            
            ViewerProtocolPolicy (string) -- [REQUIRED]The protocol that viewers can use to access the files in the origin specified by TargetOriginId when a request matches the path pattern in PathPattern . You can specify the following options:
            allow-all : Viewers can use HTTP or HTTPS.
            redirect-to-https : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.
            https-only : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).
            For more information about requiring the HTTPS protocol, see Using an HTTPS Connection to Access Your Objects in the Amazon CloudFront Developer Guide .
            Note
            The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
            MinTTL (integer) -- [REQUIRED]The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) in the Amazon Amazon CloudFront Developer Guide .
            You must specify 0 for MinTTL if you configure CloudFront to forward all headers to your origin (under Headers , if you specify 1 for Quantity and * for Name ).
            AllowedMethods (dict) --A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:
            CloudFront forwards only GET and HEAD requests.
            CloudFront forwards only GET , HEAD , and OPTIONS requests.
            CloudFront forwards GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests.
            If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users can't perform operations that you don't want them to. For example, you might not want users to have permissions to delete objects from your origin.
            Quantity (integer) -- [REQUIRED]The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for GET and HEAD requests), 3 (for GET , HEAD , and OPTIONS requests) and 7 (for GET, HEAD, OPTIONS, PUT, PATCH, POST , and DELETE requests).
            Items (list) -- [REQUIRED]A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.
            (string) --
            CachedMethods (dict) --A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:
            CloudFront caches responses to GET and HEAD requests.
            CloudFront caches responses to GET , HEAD , and OPTIONS requests.
            If you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.
            Quantity (integer) -- [REQUIRED]The number of HTTP methods for which you want CloudFront to cache responses. Valid values are 2 (for caching responses to GET and HEAD requests) and 3 (for caching responses to GET , HEAD , and OPTIONS requests).
            Items (list) -- [REQUIRED]A complex type that contains the HTTP methods that you want CloudFront to cache responses to.
            (string) --
            
            SmoothStreaming (boolean) --Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify true ; if not, specify false . If you specify true for SmoothStreaming , you can still distribute other content using this cache behavior if the content matches the value of PathPattern .
            DefaultTTL (integer) --The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
            MaxTTL (integer) --The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as Cache-Control max-age , Cache-Control s-maxage , and Expires to objects. For more information, see Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration) in the Amazon CloudFront Developer Guide .
            Compress (boolean) --Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true; if not, specify false. For more information, see Serving Compressed Files in the Amazon CloudFront Developer Guide .
            LambdaFunctionAssociations (dict) --A complex type that contains zero or more Lambda function associations for a cache behavior.
            Quantity (integer) -- [REQUIRED]The number of Lambda function associations for this cache behavior.
            Items (list) --
            Optional : A complex type that contains LambdaFunctionAssociation items for this cache behavior. If Quantity is 0 , you can omit Items .
            (dict) --A complex type that contains a Lambda function association.
            LambdaFunctionARN (string) -- [REQUIRED]The ARN of the Lambda function. You must specify the ARN of a function version; you can't specify a Lambda alias or $LATEST.
            EventType (string) -- [REQUIRED]Specifies the event type that triggers a Lambda function invocation. You can specify the following values:
            viewer-request : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.
            origin-request : The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn't execute.
            origin-response : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn't execute.
            viewer-response : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesn't execute.
            IncludeBody (boolean) --A flag that allows a Lambda function to have read access to the body content. For more information, see Accessing the Request Body by Choosing the Include Body Option in the Amazon CloudFront Developer Guide.
            
            FieldLevelEncryptionId (string) --The value of ID for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for a cache behavior or for the default cache behavior in your distribution.
            
            CustomErrorResponses (dict) --A complex type that controls the following:
            Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.
            How long CloudFront caches HTTP status codes in the 4xx and 5xx range.
            For more information about custom error pages, see Customizing Error Responses in the Amazon CloudFront Developer Guide .
            Quantity (integer) -- [REQUIRED]The number of HTTP status codes for which you want to specify a custom error page and/or a caching duration. If Quantity is 0 , you can omit Items .
            Items (list) --A complex type that contains a CustomErrorResponse element for each HTTP status code for which you want to specify a custom error page and/or a caching duration.
            (dict) --A complex type that controls:
            Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.
            How long CloudFront caches HTTP status codes in the 4xx and 5xx range.
            For more information about custom error pages, see Customizing Error Responses in the Amazon CloudFront Developer Guide .
            ErrorCode (integer) -- [REQUIRED]The HTTP status code for which you want to specify a custom error page and/or a caching duration.
            ResponsePagePath (string) --The path to the custom error page that you want CloudFront to return to a viewer when your origin returns the HTTP status code specified by ErrorCode , for example, /4xx-errors/403-forbidden.html . If you want to store your objects and your custom error pages in different locations, your distribution must include a cache behavior for which the following is true:
            The value of PathPattern matches the path to your custom error messages. For example, suppose you saved custom error pages for 4xx errors in an Amazon S3 bucket in a directory named /4xx-errors . Your distribution must include a cache behavior for which the path pattern routes requests for your custom error pages to that location, for example, /4xx-errors/* .
            The value of TargetOriginId specifies the value of the ID element for the origin that contains your custom error pages.
            If you specify a value for ResponsePagePath , you must also specify a value for ResponseCode . If you don't want to specify a value, include an empty element, <ResponsePagePath> , in the XML document.
            We recommend that you store custom error pages in an Amazon S3 bucket. If you store custom error pages on an HTTP server and the server starts to return 5xx errors, CloudFront can't get the files that you want to return to viewers because the origin server is unavailable.
            ResponseCode (string) --The HTTP status code that you want CloudFront to return to the viewer along with the custom error page. There are a variety of reasons that you might want CloudFront to return a status code different from the status code that your origin returned to CloudFront, for example:
            Some Internet devices (some firewalls and corporate proxies, for example) intercept HTTP 4xx and 5xx and prevent the response from being returned to the viewer. If you substitute 200 , the response typically won't be intercepted.
            If you don't care about distinguishing among different client errors or server errors, you can specify 400 or 500 as the ResponseCode for all 4xx or 5xx errors.
            You might want to return a 200 status code (OK) and static website so your customers don't know that your website is down.
            If you specify a value for ResponseCode , you must also specify a value for ResponsePagePath . If you don't want to specify a value, include an empty element, <ResponseCode> , in the XML document.
            ErrorCachingMinTTL (integer) --The minimum amount of time, in seconds, that you want CloudFront to cache the HTTP status code specified in ErrorCode . When this time period has elapsed, CloudFront queries your origin to see whether the problem that caused the error has been resolved and the requested object is now available.
            If you don't want to specify a value, include an empty element, <ErrorCachingMinTTL> , in the XML document.
            For more information, see Customizing Error Responses in the Amazon CloudFront Developer Guide .
            
            Comment (string) -- [REQUIRED]Any comments you want to include about the distribution.
            If you don't want to specify a comment, include an empty Comment element.
            To delete an existing comment, update the distribution configuration and include an empty Comment element.
            To add or change a comment, update the distribution configuration and specify the new comment.
            Logging (dict) --A complex type that controls whether access logs are written for the distribution.
            For more information about logging, see Access Logs in the Amazon CloudFront Developer Guide .
            Enabled (boolean) -- [REQUIRED]Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you don't want to enable logging when you create a distribution or if you want to disable logging for an existing distribution, specify false for Enabled , and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket , prefix , and IncludeCookies , the values are automatically deleted.
            IncludeCookies (boolean) -- [REQUIRED]Specifies whether you want CloudFront to include cookies in access logs, specify true for IncludeCookies . If you choose to include cookies in logs, CloudFront logs all cookies regardless of how you configure the cache behaviors for this distribution. If you don't want to include cookies when you create a distribution or if you want to disable include cookies for an existing distribution, specify false for IncludeCookies .
            Bucket (string) -- [REQUIRED]The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com .
            Prefix (string) -- [REQUIRED]An optional string that you want CloudFront to prefix to the access log filenames for this distribution, for example, myprefix/ . If you want to enable logging, but you don't want to specify a prefix, you still must include an empty Prefix element in the Logging element.
            PriceClass (string) --The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All , CloudFront responds to requests for your objects from all CloudFront edge locations.
            If you specify a price class other than PriceClass_All , CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Viewers who are in or near regions that are excluded from your specified price class may encounter slower performance.
            For more information about price classes, see Choosing the Price Class for a CloudFront Distribution in the Amazon CloudFront Developer Guide . For information about CloudFront pricing, including how price classes (such as Price Class 100) map to CloudFront regions, see Amazon CloudFront Pricing . For price class information, scroll down to see the table at the bottom of the page.
            Enabled (boolean) -- [REQUIRED]From this field, you can enable or disable the selected distribution.
            ViewerCertificate (dict) --
            CloudFrontDefaultCertificate (boolean) --For information about how and when to use CloudFrontDefaultCertificate , see ViewerCertificate .
            IAMCertificateId (string) --For information about how and when to use IAMCertificateId , see ViewerCertificate .
            ACMCertificateArn (string) --For information about how and when to use ACMCertificateArn , see ViewerCertificate .
            SSLSupportMethod (string) --If you specify a value for ViewerCertificate$ACMCertificateArn or for ViewerCertificate$IAMCertificateId , you must also specify how you want CloudFront to serve HTTPS requests: using a method that works for all clients or one that works for most clients:
            vip : CloudFront uses dedicated IP addresses for your content and can respond to HTTPS requests from any viewer. However, you will incur additional monthly charges.
            sni-only : CloudFront can respond to HTTPS requests from viewers that support Server Name Indication (SNI). All modern browsers support SNI, but some browsers still in use don't support SNI. If some of your users' browsers don't support SNI, we recommend that you do one of the following:
            Use the vip option (dedicated IP addresses) instead of sni-only .
            Use the CloudFront SSL/TLS certificate instead of a custom certificate. This requires that you use the CloudFront domain name of your distribution in the URLs for your objects, for example, https://d111111abcdef8.cloudfront.net/logo.png .
            If you can control which browser your users use, upgrade the browser to one that supports SNI.
            Use HTTP instead of HTTPS.
            Don't specify a value for SSLSupportMethod if you specified <CloudFrontDefaultCertificate>true<CloudFrontDefaultCertificate> .
            For more information, see Using Alternate Domain Names and HTTPS in the Amazon CloudFront Developer Guide .
            MinimumProtocolVersion (string) --Specify the security policy that you want CloudFront to use for HTTPS connections. A security policy determines two settings:
            The minimum SSL/TLS protocol that CloudFront uses to communicate with viewers
            The cipher that CloudFront uses to encrypt the content that it returns to viewers
            Note
            On the CloudFront console, this setting is called Security policy .
            We recommend that you specify TLSv1.1_2016 unless your users are using browsers or devices that do not support TLSv1.1 or later.
            When both of the following are true, you must specify TLSv1 or later for the security policy:
            You're using a custom certificate: you specified a value for ACMCertificateArn or for IAMCertificateId
            You're using SNI: you specified sni-only for SSLSupportMethod
            If you specify true for CloudFrontDefaultCertificate , CloudFront automatically sets the security policy to TLSv1 regardless of the value that you specify for MinimumProtocolVersion .
            For information about the relationship between the security policy that you choose and the protocols and ciphers that CloudFront uses to communicate with viewers, see Supported SSL/TLS Protocols and Ciphers for Communication Between Viewers and CloudFront in the Amazon CloudFront Developer Guide .
            Certificate (string) --This field has been deprecated. Use one of the following fields instead:
            ViewerCertificate$ACMCertificateArn
            ViewerCertificate$IAMCertificateId
            ViewerCertificate$CloudFrontDefaultCertificate
            CertificateSource (string) --This field has been deprecated. Use one of the following fields instead:
            ViewerCertificate$ACMCertificateArn
            ViewerCertificate$IAMCertificateId
            ViewerCertificate$CloudFrontDefaultCertificate
            
            Restrictions (dict) --
            GeoRestriction (dict) -- [REQUIRED]A complex type that controls the countries in which your content is distributed. CloudFront determines the location of your users using MaxMind GeoIP databases.
            RestrictionType (string) -- [REQUIRED]The method that you want to use to restrict distribution of your content by country:
            none : No geo restriction is enabled, meaning access to content is not restricted by client geo location.
            blacklist : The Location elements specify the countries in which you don't want CloudFront to distribute your content.
            whitelist : The Location elements specify the countries in which you want CloudFront to distribute your content.
            Quantity (integer) -- [REQUIRED]When geo restriction is enabled , this is the number of countries in your whitelist or blacklist . Otherwise, when it is not enabled, Quantity is 0 , and you can omit Items .
            Items (list) --A complex type that contains a Location element for each country in which you want CloudFront either to distribute your content (whitelist ) or not distribute your content (blacklist ).
            The Location element is a two-letter, uppercase country code for a country that you want to include in your blacklist or whitelist . Include one Location element for each country.
            CloudFront and MaxMind both use ISO 3166 country codes. For the current list of countries and the corresponding codes, see ISO 3166-1-alpha-2 code on the International Organization for Standardization website. You can also refer to the country list on the CloudFront console, which includes both country names and codes.
            (string) --
            
            WebACLId (string) --A unique identifier that specifies the AWS WAF web ACL, if any, to associate with this distribution.
            AWS WAF is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to CloudFront, and lets you control access to your content. Based on conditions that you specify, such as the IP addresses that requests originate from or the values of query strings, CloudFront responds to requests either with the requested content or with an HTTP 403 status code (Forbidden). You can also configure CloudFront to return a custom error page when a request is blocked. For more information about AWS WAF, see the AWS WAF Developer Guide .
            HttpVersion (string) --(Optional) Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. The default value for new web distributions is http2. Viewers that don't support HTTP/2 automatically use an earlier HTTP version.
            For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support Server Name Identification (SNI).
            In general, configuring CloudFront to communicate with viewers using HTTP/2 reduces latency. You can improve performance by optimizing for HTTP/2. For more information, do an Internet search for 'http/2 optimization.'
            IsIPV6Enabled (boolean) --If you want CloudFront to respond to IPv6 DNS requests with an IPv6 address for your distribution, specify true . If you specify false , CloudFront responds to IPv6 DNS requests with the DNS response code NOERROR and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution.
            In general, you should enable IPv6 if you have users on IPv6 networks who want to access your content. However, if you're using signed URLs or signed cookies to restrict access to your content, and if you're using a custom policy that includes the IpAddress parameter to restrict the IP addresses that can access your content, don't enable IPv6. If you want to restrict access to some content by IP address and not restrict access to other content (or restrict access but not by IP address), you can create two distributions. For more information, see Creating a Signed URL Using a Custom Policy in the Amazon CloudFront Developer Guide .
            If you're using an Amazon Route 53 alias resource record set to route traffic to your CloudFront distribution, you need to create a second alias resource record set when both of the following are true:
            You enable IPv6 for the distribution
            You're using alternate domain names in the URLs for your objects
            For more information, see Routing Traffic to an Amazon CloudFront Web Distribution by Using Your Domain Name in the Amazon Route 53 Developer Guide .
            If you created a CNAME resource record set, either with Amazon Route 53 or with another DNS service, you don't need to make any changes. A CNAME record will route traffic to your distribution regardless of the IP address format of the viewer request.
            

    :type Id: string
    :param Id: [REQUIRED]
            The distribution's id.
            

    :type IfMatch: string
    :param IfMatch: The value of the ETag header that you received when retrieving the distribution's configuration. For example: E2QWRUHAPOMQZL .

    :rtype: dict
    :return: {
        'Distribution': {
            'Id': 'string',
            'ARN': 'string',
            'Status': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'InProgressInvalidationBatches': 123,
            'DomainName': 'string',
            'ActiveTrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    {
                        'AwsAccountNumber': 'string',
                        'KeyPairIds': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                ]
            },
            'DistributionConfig': {
                'CallerReference': 'string',
                'Aliases': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'DefaultRootObject': 'string',
                'Origins': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Id': 'string',
                            'DomainName': 'string',
                            'OriginPath': 'string',
                            'CustomHeaders': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'HeaderName': 'string',
                                        'HeaderValue': 'string'
                                    },
                                ]
                            },
                            'S3OriginConfig': {
                                'OriginAccessIdentity': 'string'
                            },
                            'CustomOriginConfig': {
                                'HTTPPort': 123,
                                'HTTPSPort': 123,
                                'OriginProtocolPolicy': 'http-only'|'match-viewer'|'https-only',
                                'OriginSslProtocols': {
                                    'Quantity': 123,
                                    'Items': [
                                        'SSLv3'|'TLSv1'|'TLSv1.1'|'TLSv1.2',
                                    ]
                                },
                                'OriginReadTimeout': 123,
                                'OriginKeepaliveTimeout': 123
                            }
                        },
                    ]
                },
                'OriginGroups': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Id': 'string',
                            'FailoverCriteria': {
                                'StatusCodes': {
                                    'Quantity': 123,
                                    'Items': [
                                        123,
                                    ]
                                }
                            },
                            'Members': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'OriginId': 'string'
                                    },
                                ]
                            }
                        },
                    ]
                },
                'DefaultCacheBehavior': {
                    'TargetOriginId': 'string',
                    'ForwardedValues': {
                        'QueryString': True|False,
                        'Cookies': {
                            'Forward': 'none'|'whitelist'|'all',
                            'WhitelistedNames': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                        'Headers': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        },
                        'QueryStringCacheKeys': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                    'TrustedSigners': {
                        'Enabled': True|False,
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    },
                    'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                    'MinTTL': 123,
                    'AllowedMethods': {
                        'Quantity': 123,
                        'Items': [
                            'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                        ],
                        'CachedMethods': {
                            'Quantity': 123,
                            'Items': [
                                'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                            ]
                        }
                    },
                    'SmoothStreaming': True|False,
                    'DefaultTTL': 123,
                    'MaxTTL': 123,
                    'Compress': True|False,
                    'LambdaFunctionAssociations': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'LambdaFunctionARN': 'string',
                                'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                'IncludeBody': True|False
                            },
                        ]
                    },
                    'FieldLevelEncryptionId': 'string'
                },
                'CacheBehaviors': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'PathPattern': 'string',
                            'TargetOriginId': 'string',
                            'ForwardedValues': {
                                'QueryString': True|False,
                                'Cookies': {
                                    'Forward': 'none'|'whitelist'|'all',
                                    'WhitelistedNames': {
                                        'Quantity': 123,
                                        'Items': [
                                            'string',
                                        ]
                                    }
                                },
                                'Headers': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                },
                                'QueryStringCacheKeys': {
                                    'Quantity': 123,
                                    'Items': [
                                        'string',
                                    ]
                                }
                            },
                            'TrustedSigners': {
                                'Enabled': True|False,
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            },
                            'ViewerProtocolPolicy': 'allow-all'|'https-only'|'redirect-to-https',
                            'MinTTL': 123,
                            'AllowedMethods': {
                                'Quantity': 123,
                                'Items': [
                                    'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                ],
                                'CachedMethods': {
                                    'Quantity': 123,
                                    'Items': [
                                        'GET'|'HEAD'|'POST'|'PUT'|'PATCH'|'OPTIONS'|'DELETE',
                                    ]
                                }
                            },
                            'SmoothStreaming': True|False,
                            'DefaultTTL': 123,
                            'MaxTTL': 123,
                            'Compress': True|False,
                            'LambdaFunctionAssociations': {
                                'Quantity': 123,
                                'Items': [
                                    {
                                        'LambdaFunctionARN': 'string',
                                        'EventType': 'viewer-request'|'viewer-response'|'origin-request'|'origin-response',
                                        'IncludeBody': True|False
                                    },
                                ]
                            },
                            'FieldLevelEncryptionId': 'string'
                        },
                    ]
                },
                'CustomErrorResponses': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'ErrorCode': 123,
                            'ResponsePagePath': 'string',
                            'ResponseCode': 'string',
                            'ErrorCachingMinTTL': 123
                        },
                    ]
                },
                'Comment': 'string',
                'Logging': {
                    'Enabled': True|False,
                    'IncludeCookies': True|False,
                    'Bucket': 'string',
                    'Prefix': 'string'
                },
                'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                'Enabled': True|False,
                'ViewerCertificate': {
                    'CloudFrontDefaultCertificate': True|False,
                    'IAMCertificateId': 'string',
                    'ACMCertificateArn': 'string',
                    'SSLSupportMethod': 'sni-only'|'vip',
                    'MinimumProtocolVersion': 'SSLv3'|'TLSv1'|'TLSv1_2016'|'TLSv1.1_2016'|'TLSv1.2_2018',
                    'Certificate': 'string',
                    'CertificateSource': 'cloudfront'|'iam'|'acm'
                },
                'Restrictions': {
                    'GeoRestriction': {
                        'RestrictionType': 'blacklist'|'whitelist'|'none',
                        'Quantity': 123,
                        'Items': [
                            'string',
                        ]
                    }
                },
                'WebACLId': 'string',
                'HttpVersion': 'http1.1'|'http2',
                'IsIPV6Enabled': True|False
            }
        },
        'ETag': 'string'
    }
    
    
    :returns: 
    Update the XML document that was returned in the response to your GetDistributionConfig request to include your changes.
    
    """
    pass

def update_field_level_encryption_config(FieldLevelEncryptionConfig=None, Id=None, IfMatch=None):
    """
    Update a field-level encryption configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.update_field_level_encryption_config(
        FieldLevelEncryptionConfig={
            'CallerReference': 'string',
            'Comment': 'string',
            'QueryArgProfileConfig': {
                'ForwardWhenQueryArgProfileIsUnknown': True|False,
                'QueryArgProfiles': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'QueryArg': 'string',
                            'ProfileId': 'string'
                        },
                    ]
                }
            },
            'ContentTypeProfileConfig': {
                'ForwardWhenContentTypeIsUnknown': True|False,
                'ContentTypeProfiles': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'Format': 'URLEncoded',
                            'ProfileId': 'string',
                            'ContentType': 'string'
                        },
                    ]
                }
            }
        },
        Id='string',
        IfMatch='string'
    )
    
    
    :type FieldLevelEncryptionConfig: dict
    :param FieldLevelEncryptionConfig: [REQUIRED]
            Request to update a field-level encryption configuration.
            CallerReference (string) -- [REQUIRED]A unique number that ensures the request can't be replayed.
            Comment (string) --An optional comment about the configuration.
            QueryArgProfileConfig (dict) --A complex data type that specifies when to forward content if a profile isn't found and the profile that can be provided as a query argument in a request.
            ForwardWhenQueryArgProfileIsUnknown (boolean) -- [REQUIRED]Flag to set if you want a request to be forwarded to the origin even if the profile specified by the field-level encryption query argument, fle-profile, is unknown.
            QueryArgProfiles (dict) --Profiles specified for query argument-profile mapping for field-level encryption.
            Quantity (integer) -- [REQUIRED]Number of profiles for query argument-profile mapping for field-level encryption.
            Items (list) --Number of items for query argument-profile mapping for field-level encryption.
            (dict) --Query argument-profile mapping for field-level encryption.
            QueryArg (string) -- [REQUIRED]Query argument for field-level encryption query argument-profile mapping.
            ProfileId (string) -- [REQUIRED]ID of profile to use for field-level encryption query argument-profile mapping
            
            
            ContentTypeProfileConfig (dict) --A complex data type that specifies when to forward content if a content type isn't recognized and profiles to use as by default in a request if a query argument doesn't specify a profile to use.
            ForwardWhenContentTypeIsUnknown (boolean) -- [REQUIRED]The setting in a field-level encryption content type-profile mapping that specifies what to do when an unknown content type is provided for the profile. If true, content is forwarded without being encrypted when the content type is unknown. If false (the default), an error is returned when the content type is unknown.
            ContentTypeProfiles (dict) --The configuration for a field-level encryption content type-profile.
            Quantity (integer) -- [REQUIRED]The number of field-level encryption content type-profile mappings.
            Items (list) --Items in a field-level encryption content type-profile mapping.
            (dict) --A field-level encryption content type profile.
            Format (string) -- [REQUIRED]The format for a field-level encryption content type-profile mapping.
            ProfileId (string) --The profile ID for a field-level encryption content type-profile mapping.
            ContentType (string) -- [REQUIRED]The content type for a field-level encryption content type-profile mapping.
            
            
            

    :type Id: string
    :param Id: [REQUIRED]
            The ID of the configuration you want to update.
            

    :type IfMatch: string
    :param IfMatch: The value of the ETag header that you received when retrieving the configuration identity to update. For example: E2QWRUHAPOMQZL .

    :rtype: dict
    :return: {
        'FieldLevelEncryption': {
            'Id': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'FieldLevelEncryptionConfig': {
                'CallerReference': 'string',
                'Comment': 'string',
                'QueryArgProfileConfig': {
                    'ForwardWhenQueryArgProfileIsUnknown': True|False,
                    'QueryArgProfiles': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'QueryArg': 'string',
                                'ProfileId': 'string'
                            },
                        ]
                    }
                },
                'ContentTypeProfileConfig': {
                    'ForwardWhenContentTypeIsUnknown': True|False,
                    'ContentTypeProfiles': {
                        'Quantity': 123,
                        'Items': [
                            {
                                'Format': 'URLEncoded',
                                'ProfileId': 'string',
                                'ContentType': 'string'
                            },
                        ]
                    }
                }
            }
        },
        'ETag': 'string'
    }
    
    
    """
    pass

def update_field_level_encryption_profile(FieldLevelEncryptionProfileConfig=None, Id=None, IfMatch=None):
    """
    Update a field-level encryption profile.
    See also: AWS API Documentation
    
    
    :example: response = client.update_field_level_encryption_profile(
        FieldLevelEncryptionProfileConfig={
            'Name': 'string',
            'CallerReference': 'string',
            'Comment': 'string',
            'EncryptionEntities': {
                'Quantity': 123,
                'Items': [
                    {
                        'PublicKeyId': 'string',
                        'ProviderId': 'string',
                        'FieldPatterns': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                ]
            }
        },
        Id='string',
        IfMatch='string'
    )
    
    
    :type FieldLevelEncryptionProfileConfig: dict
    :param FieldLevelEncryptionProfileConfig: [REQUIRED]
            Request to update a field-level encryption profile.
            Name (string) -- [REQUIRED]Profile name for the field-level encryption profile.
            CallerReference (string) -- [REQUIRED]A unique number that ensures that the request can't be replayed.
            Comment (string) --An optional comment for the field-level encryption profile.
            EncryptionEntities (dict) -- [REQUIRED]A complex data type of encryption entities for the field-level encryption profile that include the public key ID, provider, and field patterns for specifying which fields to encrypt with this key.
            Quantity (integer) -- [REQUIRED]Number of field pattern items in a field-level encryption content type-profile mapping.
            Items (list) --An array of field patterns in a field-level encryption content type-profile mapping.
            (dict) --Complex data type for field-level encryption profiles that includes the encryption key and field pattern specifications.
            PublicKeyId (string) -- [REQUIRED]The public key associated with a set of field-level encryption patterns, to be used when encrypting the fields that match the patterns.
            ProviderId (string) -- [REQUIRED]The provider associated with the public key being used for encryption. This value must also be provided with the private key for applications to be able to decrypt data.
            FieldPatterns (dict) -- [REQUIRED]Field patterns in a field-level encryption content type profile specify the fields that you want to be encrypted. You can provide the full field name, or any beginning characters followed by a wildcard (*). You can't overlap field patterns. For example, you can't have both ABC* and AB*. Note that field patterns are case-sensitive.
            Quantity (integer) -- [REQUIRED]The number of field-level encryption field patterns.
            Items (list) --An array of the field-level encryption field patterns.
            (string) --
            
            
            

    :type Id: string
    :param Id: [REQUIRED]
            The ID of the field-level encryption profile request.
            

    :type IfMatch: string
    :param IfMatch: The value of the ETag header that you received when retrieving the profile identity to update. For example: E2QWRUHAPOMQZL .

    :rtype: dict
    :return: {
        'FieldLevelEncryptionProfile': {
            'Id': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'FieldLevelEncryptionProfileConfig': {
                'Name': 'string',
                'CallerReference': 'string',
                'Comment': 'string',
                'EncryptionEntities': {
                    'Quantity': 123,
                    'Items': [
                        {
                            'PublicKeyId': 'string',
                            'ProviderId': 'string',
                            'FieldPatterns': {
                                'Quantity': 123,
                                'Items': [
                                    'string',
                                ]
                            }
                        },
                    ]
                }
            }
        },
        'ETag': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_public_key(PublicKeyConfig=None, Id=None, IfMatch=None):
    """
    Update public key information. Note that the only value you can change is the comment.
    See also: AWS API Documentation
    
    
    :example: response = client.update_public_key(
        PublicKeyConfig={
            'CallerReference': 'string',
            'Name': 'string',
            'EncodedKey': 'string',
            'Comment': 'string'
        },
        Id='string',
        IfMatch='string'
    )
    
    
    :type PublicKeyConfig: dict
    :param PublicKeyConfig: [REQUIRED]
            Request to update public key information.
            CallerReference (string) -- [REQUIRED]A unique number that ensures that the request can't be replayed.
            Name (string) -- [REQUIRED]The name for a public key you add to CloudFront to use with features like field-level encryption.
            EncodedKey (string) -- [REQUIRED]The encoded public key that you want to add to CloudFront to use with features like field-level encryption.
            Comment (string) --An optional comment about a public key.
            

    :type Id: string
    :param Id: [REQUIRED]
            ID of the public key to be updated.
            

    :type IfMatch: string
    :param IfMatch: The value of the ETag header that you received when retrieving the public key to update. For example: E2QWRUHAPOMQZL .

    :rtype: dict
    :return: {
        'PublicKey': {
            'Id': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'PublicKeyConfig': {
                'CallerReference': 'string',
                'Name': 'string',
                'EncodedKey': 'string',
                'Comment': 'string'
            }
        },
        'ETag': 'string'
    }
    
    
    """
    pass

def update_streaming_distribution(StreamingDistributionConfig=None, Id=None, IfMatch=None):
    """
    Update a streaming distribution.
    See also: AWS API Documentation
    
    
    :example: response = client.update_streaming_distribution(
        StreamingDistributionConfig={
            'CallerReference': 'string',
            'S3Origin': {
                'DomainName': 'string',
                'OriginAccessIdentity': 'string'
            },
            'Aliases': {
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'Comment': 'string',
            'Logging': {
                'Enabled': True|False,
                'Bucket': 'string',
                'Prefix': 'string'
            },
            'TrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    'string',
                ]
            },
            'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
            'Enabled': True|False
        },
        Id='string',
        IfMatch='string'
    )
    
    
    :type StreamingDistributionConfig: dict
    :param StreamingDistributionConfig: [REQUIRED]
            The streaming distribution's configuration information.
            CallerReference (string) -- [REQUIRED]A unique value (for example, a date-time stamp) that ensures that the request can't be replayed.
            If the value of CallerReference is new (regardless of the content of the StreamingDistributionConfig object), CloudFront creates a new distribution.
            If CallerReference is a value that you already sent in a previous request to create a distribution, CloudFront returns a DistributionAlreadyExists error.
            S3Origin (dict) -- [REQUIRED]A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.
            DomainName (string) -- [REQUIRED]The DNS name of the Amazon S3 origin.
            OriginAccessIdentity (string) -- [REQUIRED]The CloudFront origin access identity to associate with the RTMP distribution. Use an origin access identity to configure the distribution so that end users can only access objects in an Amazon S3 bucket through CloudFront.
            If you want end users to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty OriginAccessIdentity element.
            To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty OriginAccessIdentity element.
            To replace the origin access identity, update the distribution configuration and specify the new origin access identity.
            For more information, see Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content in the Amazon Amazon CloudFront Developer Guide .
            Aliases (dict) --A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution.
            Quantity (integer) -- [REQUIRED]The number of CNAME aliases, if any, that you want to associate with this distribution.
            Items (list) --A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.
            (string) --
            
            Comment (string) -- [REQUIRED]Any comments you want to include about the streaming distribution.
            Logging (dict) --A complex type that controls whether access logs are written for the streaming distribution.
            Enabled (boolean) -- [REQUIRED]Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you don't want to enable logging when you create a streaming distribution or if you want to disable logging for an existing streaming distribution, specify false for Enabled , and specify empty Bucket and Prefix elements. If you specify false for Enabled but you specify values for Bucket and Prefix , the values are automatically deleted.
            Bucket (string) -- [REQUIRED]The Amazon S3 bucket to store the access logs in, for example, myawslogbucket.s3.amazonaws.com .
            Prefix (string) -- [REQUIRED]An optional string that you want CloudFront to prefix to the access log filenames for this streaming distribution, for example, myprefix/ . If you want to enable logging, but you don't want to specify a prefix, you still must include an empty Prefix element in the Logging element.
            TrustedSigners (dict) -- [REQUIRED]A complex type that specifies any AWS accounts that you want to permit to create signed URLs for private content. If you want the distribution to use signed URLs, include this element; if you want the distribution to use public URLs, remove this element. For more information, see Serving Private Content through CloudFront in the Amazon CloudFront Developer Guide .
            Enabled (boolean) -- [REQUIRED]Specifies whether you want to require viewers to use signed URLs to access the files specified by PathPattern and TargetOriginId .
            Quantity (integer) -- [REQUIRED]The number of trusted signers for this cache behavior.
            Items (list) --
            Optional : A complex type that contains trusted signers for this cache behavior. If Quantity is 0 , you can omit Items .
            (string) --
            
            PriceClass (string) --A complex type that contains information about price class for this streaming distribution.
            Enabled (boolean) -- [REQUIRED]Whether the streaming distribution is enabled to accept user requests for content.
            

    :type Id: string
    :param Id: [REQUIRED]
            The streaming distribution's id.
            

    :type IfMatch: string
    :param IfMatch: The value of the ETag header that you received when retrieving the streaming distribution's configuration. For example: E2QWRUHAPOMQZL .

    :rtype: dict
    :return: {
        'StreamingDistribution': {
            'Id': 'string',
            'ARN': 'string',
            'Status': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'DomainName': 'string',
            'ActiveTrustedSigners': {
                'Enabled': True|False,
                'Quantity': 123,
                'Items': [
                    {
                        'AwsAccountNumber': 'string',
                        'KeyPairIds': {
                            'Quantity': 123,
                            'Items': [
                                'string',
                            ]
                        }
                    },
                ]
            },
            'StreamingDistributionConfig': {
                'CallerReference': 'string',
                'S3Origin': {
                    'DomainName': 'string',
                    'OriginAccessIdentity': 'string'
                },
                'Aliases': {
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'Comment': 'string',
                'Logging': {
                    'Enabled': True|False,
                    'Bucket': 'string',
                    'Prefix': 'string'
                },
                'TrustedSigners': {
                    'Enabled': True|False,
                    'Quantity': 123,
                    'Items': [
                        'string',
                    ]
                },
                'PriceClass': 'PriceClass_100'|'PriceClass_200'|'PriceClass_All',
                'Enabled': True|False
            }
        },
        'ETag': 'string'
    }
    
    
    :returns: 
    self , which is the AWS account used to create the distribution.
    An AWS account number.
    
    """
    pass

