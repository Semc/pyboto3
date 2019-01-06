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

def delete_playback_configuration(Name=None):
    """
    Deletes the configuration for the specified name.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_playback_configuration(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The identifier for the configuration.
            

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

def get_playback_configuration(Name=None):
    """
    Returns the configuration for the specified name.
    See also: AWS API Documentation
    
    
    :example: response = client.get_playback_configuration(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The identifier for the configuration.
            

    :rtype: dict
    :return: {
        'AdDecisionServerUrl': 'string',
        'CdnConfiguration': {
            'AdSegmentUrlPrefix': 'string',
            'ContentSegmentUrlPrefix': 'string'
        },
        'DashConfiguration': {
            'ManifestEndpointPrefix': 'string',
            'MpdLocation': 'string'
        },
        'HlsConfiguration': {
            'ManifestEndpointPrefix': 'string'
        },
        'Name': 'string',
        'PlaybackEndpointPrefix': 'string',
        'SessionInitializationEndpointPrefix': 'string',
        'SlateAdUrl': 'string',
        'TranscodeProfileName': 'string',
        'VideoContentSourceUrl': 'string'
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

def list_playback_configurations(MaxResults=None, NextToken=None):
    """
    Returns a list of the configurations defined in AWS Elemental MediaTailor. You can specify a max number of configurations to return at a time. The default max is 50. Results are returned in pagefuls. If AWS Elemental MediaTailor has more configurations than the specified max, it provides parameters in the response that you can use to retrieve the next pageful.
    See also: AWS API Documentation
    
    
    :example: response = client.list_playback_configurations(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: Maximum number of records to return.

    :type NextToken: string
    :param NextToken: Pagination token returned by the GET list request when results overrun the meximum allowed. Use the token to fetch the next page of results.

    :rtype: dict
    :return: {
        'Items': [
            {
                'AdDecisionServerUrl': 'string',
                'CdnConfiguration': {
                    'AdSegmentUrlPrefix': 'string',
                    'ContentSegmentUrlPrefix': 'string'
                },
                'Name': 'string',
                'SlateAdUrl': 'string',
                'VideoContentSourceUrl': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def put_playback_configuration(AdDecisionServerUrl=None, CdnConfiguration=None, DashConfiguration=None, Name=None, SlateAdUrl=None, TranscodeProfileName=None, VideoContentSourceUrl=None):
    """
    Adds a new configuration to AWS Elemental MediaTailor.
    See also: AWS API Documentation
    
    
    :example: response = client.put_playback_configuration(
        AdDecisionServerUrl='string',
        CdnConfiguration={
            'AdSegmentUrlPrefix': 'string',
            'ContentSegmentUrlPrefix': 'string'
        },
        DashConfiguration={
            'MpdLocation': 'string'
        },
        Name='string',
        SlateAdUrl='string',
        TranscodeProfileName='string',
        VideoContentSourceUrl='string'
    )
    
    
    :type AdDecisionServerUrl: string
    :param AdDecisionServerUrl: The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing you can provide a static VAST URL. The maximum length is 25000 characters.

    :type CdnConfiguration: dict
    :param CdnConfiguration: The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.
            AdSegmentUrlPrefix (string) --A non-default content delivery network (CDN) to serve ad segments. By default, AWS Elemental MediaTailor uses Amazon CloudFront with default cache settings as its CDN for ad segments. To set up an alternate CDN, create a rule in your CDN for the following origin: ads.mediatailor.<region>.amazonaws.com. Then specify the rule's name in this AdSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for ad segments.
            ContentSegmentUrlPrefix (string) --A content delivery network (CDN) to cache content segments, so that content requests don t always have to go to the origin server. First, create a rule in your CDN for the content segment origin server. Then specify the rule's name in this ContentSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for content segments.
            

    :type DashConfiguration: dict
    :param DashConfiguration: The configuration object for DASH content.
            MpdLocation (string) --The setting that controls whether MediaTailor includes the Location tag in DASH Manifests. MediaTailor populates the Location tag with the URL for manifest update requests, to be used by players that don't support sticky redirects. Disable this if you have CDN routing rules set up for accessing MediaTailor manifests and you are either using client-side reporting or your players support sticky HTTP redirects. Valid values are DISABLED and EMT_DEFAULT. The EMT_DEFAULT setting enables the inclusion of the tag and is the default value.
            

    :type Name: string
    :param Name: The identifier for the configuration.

    :type SlateAdUrl: string
    :param SlateAdUrl: The URL for a high-quality video asset to transcode and use to fill in time that's not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID configurations. For VPAID, the slate is required because AWS Elemental MediaTailor provides it in the slots that are designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.

    :type TranscodeProfileName: string
    :param TranscodeProfileName: Associate this playbackConfiguration with a custom transcode profile, overriding MediaTailor's dynamic transcoding defaults. Do not include this field if you have not setup custom profiles with the MediaTailor service team.

    :type VideoContentSourceUrl: string
    :param VideoContentSourceUrl: The URL prefix for the master playlist for the stream, minus the asset ID. The maximum length is 512 characters.

    :rtype: dict
    :return: {
        'AdDecisionServerUrl': 'string',
        'CdnConfiguration': {
            'AdSegmentUrlPrefix': 'string',
            'ContentSegmentUrlPrefix': 'string'
        },
        'DashConfiguration': {
            'ManifestEndpointPrefix': 'string',
            'MpdLocation': 'string'
        },
        'HlsConfiguration': {
            'ManifestEndpointPrefix': 'string'
        },
        'Name': 'string',
        'PlaybackEndpointPrefix': 'string',
        'SessionInitializationEndpointPrefix': 'string',
        'SlateAdUrl': 'string',
        'TranscodeProfileName': 'string',
        'VideoContentSourceUrl': 'string'
    }
    
    
    """
    pass

