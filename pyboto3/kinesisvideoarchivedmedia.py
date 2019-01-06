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

def get_hls_streaming_session_url(StreamName=None, StreamARN=None, PlaybackMode=None, HLSFragmentSelector=None, DiscontinuityMode=None, Expires=None, MaxMediaPlaylistFragmentResults=None):
    """
    Retrieves an HTTP Live Streaming (HLS) URL for the stream. You can then open the URL in a browser or media player to view the stream contents.
    You must specify either the StreamName or the StreamARN .
    An Amazon Kinesis video stream has the following requirements for providing data through HLS:
    Kinesis Video Streams HLS sessions contain fragments in the fragmented MPEG-4 form (also called fMP4 or CMAF), rather than the MPEG-2 form (also called TS chunks, which the HLS specification also supports). For more information about HLS fragment types, see the HLS specification .
    The following procedure shows how to use HLS with Kinesis Video Streams:
    You can monitor the amount of data that the media player consumes by monitoring the GetMP4MediaFragment.OutgoingBytes Amazon CloudWatch metric. For information about using CloudWatch to monitor Kinesis Video Streams, see Monitoring Kinesis Video Streams . For pricing information, see Amazon Kinesis Video Streams Pricing and AWS Pricing . Charges for both HLS sessions and outgoing AWS data apply.
    For more information about HLS, see HTTP Live Streaming on the Apple Developer site .
    See also: AWS API Documentation
    
    
    :example: response = client.get_hls_streaming_session_url(
        StreamName='string',
        StreamARN='string',
        PlaybackMode='LIVE'|'ON_DEMAND',
        HLSFragmentSelector={
            'FragmentSelectorType': 'PRODUCER_TIMESTAMP'|'SERVER_TIMESTAMP',
            'TimestampRange': {
                'StartTimestamp': datetime(2015, 1, 1),
                'EndTimestamp': datetime(2015, 1, 1)
            }
        },
        DiscontinuityMode='ALWAYS'|'NEVER',
        Expires=123,
        MaxMediaPlaylistFragmentResults=123
    )
    
    
    :type StreamName: string
    :param StreamName: The name of the stream for which to retrieve the HLS master playlist URL.
            You must specify either the StreamName or the StreamARN .
            

    :type StreamARN: string
    :param StreamARN: The Amazon Resource Name (ARN) of the stream for which to retrieve the HLS master playlist URL.
            You must specify either the StreamName or the StreamARN .
            

    :type PlaybackMode: string
    :param PlaybackMode: Whether to retrieve live or archived, on-demand data.
            Features of the two types of session include the following:
            **LIVE ** : For sessions of this type, the HLS media playlist is continually updated with the latest fragments as they become available. We recommend that the media player retrieve a new playlist on a one-second interval. When this type of session is played in a media player, the user interface typically displays a 'live' notification, with no scrubber control for choosing the position in the playback window to display.
            Note
            In LIVE mode, the newest available fragments are included in an HLS media playlist, even if there is a gap between fragments (that is, if a fragment is missing). A gap like this might cause a media player to halt or cause a jump in playback. In this mode, fragments are not added to the HLS media playlist if they are older than the newest fragment in the playlist. If the missing fragment becomes available after a subsequent fragment is added to the playlist, the older fragment is not added, and the gap is not filled.
            **ON_DEMAND ** : For sessions of this type, the HLS media playlist contains all the fragments for the session, up to the number that is specified in MaxMediaPlaylistFragmentResults . The playlist must be retrieved only once for each session. When this type of session is played in a media player, the user interface typically displays a scrubber control for choosing the position in the playback window to display.
            In both playback modes, if FragmentSelectorType is PRODUCER_TIMESTAMP , and if there are multiple fragments with the same start time stamp, the fragment that has the larger fragment number (that is, the newer fragment) is included in the HLS media playlist. The other fragments are not included. Fragments that have different time stamps but have overlapping durations are still included in the HLS media playlist. This can lead to unexpected behavior in the media player.
            The default is LIVE .
            

    :type HLSFragmentSelector: dict
    :param HLSFragmentSelector: The time range of the requested fragment, and the source of the time stamps.
            This parameter is required if PlaybackMode is ON_DEMAND . This parameter is optional if PlaybackMode is LIVE . If PlaybackMode is LIVE , the FragmentSelectorType can be set, but the TimestampRange should not be set. If PlaybackMode is ON_DEMAND , both FragmentSelectorType and TimestampRange must be set.
            FragmentSelectorType (string) --The source of the time stamps for the requested media.
            When FragmentSelectorType is set to PRODUCER_TIMESTAMP and GetHLSStreamingSessionURLInput$PlaybackMode is ON_DEMAND , the first fragment ingested with a producer time stamp within the specified FragmentSelector$TimestampRange is included in the media playlist. In addition, the fragments with producer time stamps within the TimestampRange ingested immediately following the first fragment (up to the GetHLSStreamingSessionURLInput$MaxMediaPlaylistFragmentResults value) are included.
            Fragments that have duplicate producer time stamps are deduplicated. This means that if producers are producing a stream of fragments with producer time stamps that are approximately equal to the true clock time, the HLS media playlists will contain all of the fragments within the requested time stamp range. If some fragments are ingested within the same time range and very different points in time, only the oldest ingested collection of fragments are returned.
            When FragmentSelectorType is set to PRODUCER_TIMESTAMP and GetHLSStreamingSessionURLInput$PlaybackMode is LIVE , the producer time stamps are used in the MP4 fragments and for deduplication. But the most recently ingested fragments based on server time stamps are included in the HLS media playlist. This means that even if fragments ingested in the past have producer time stamps with values now, they are not included in the HLS media playlist.
            The default is SERVER_TIMESTAMP .
            TimestampRange (dict) --The start and end of the time stamp range for the requested media.
            This value should not be present if PlaybackType is LIVE .
            StartTimestamp (datetime) --The start of the time stamp range for the requested media.
            If the HLSTimestampRange value is specified, the StartTimestamp value is required.
            Note
            This value is inclusive. Fragments that start before the StartTimestamp and continue past it are included in the session. If FragmentSelectorType is SERVER_TIMESTAMP , the StartTimestamp must be later than the stream head.
            EndTimestamp (datetime) --The end of the time stamp range for the requested media. This value must be within 3 hours of the specified StartTimestamp , and it must be later than the StartTimestamp value.
            If FragmentSelectorType for the request is SERVER_TIMESTAMP , this value must be in the past.
            If the HLSTimestampRange value is specified, the EndTimestamp value is required.
            Note
            This value is inclusive. The EndTimestamp is compared to the (starting) time stamp of the fragment. Fragments that start before the EndTimestamp value and continue past it are included in the session.
            
            

    :type DiscontinuityMode: string
    :param DiscontinuityMode: Specifies when flags marking discontinuities between fragments will be added to the media playlists. The default is ALWAYS when HLSFragmentSelector is SERVER_TIMESTAMP , and NEVER when it is PRODUCER_TIMESTAMP .
            Media players typically build a timeline of media content to play, based on the time stamps of each fragment. This means that if there is any overlap between fragments (as is typical if HLSFragmentSelector is SERVER_TIMESTAMP ), the media player timeline has small gaps between fragments in some places, and overwrites frames in other places. When there are discontinuity flags between fragments, the media player is expected to reset the timeline, resulting in the fragment being played immediately after the previous fragment. We recommend that you always have discontinuity flags between fragments if the fragment time stamps are not accurate or if fragments might be missing. You should not place discontinuity flags between fragments for the player timeline to accurately map to the producer time stamps.
            

    :type Expires: integer
    :param Expires: The time in seconds until the requested session expires. This value can be between 300 (5 minutes) and 43200 (12 hours).
            When a session expires, no new calls to GetHLSMasterPlaylist , GetHLSMediaPlaylist , GetMP4InitFragment , or GetMP4MediaFragment can be made for that session.
            The default is 300 (5 minutes).
            

    :type MaxMediaPlaylistFragmentResults: integer
    :param MaxMediaPlaylistFragmentResults: The maximum number of fragments that are returned in the HLS media playlists.
            When the PlaybackMode is LIVE , the most recent fragments are returned up to this value. When the PlaybackMode is ON_DEMAND , the oldest fragments are returned, up to this maximum number.
            When there are a higher number of fragments available in a live HLS media playlist, video players often buffer content before starting playback. Increasing the buffer size increases the playback latency, but it decreases the likelihood that rebuffering will occur during playback. We recommend that a live HLS media playlist have a minimum of 3 fragments and a maximum of 10 fragments.
            The default is 5 fragments if PlaybackMode is LIVE , and 1,000 if PlaybackMode is ON_DEMAND .
            The maximum value of 1,000 fragments corresponds to more than 16 minutes of video on streams with 1-second fragments, and more than 2 1/2 hours of video on streams with 10-second fragments.
            

    :rtype: dict
    :return: {
        'HLSStreamingSessionURL': 'string'
    }
    
    
    :returns: 
    Get an endpoint using GetDataEndpoint , specifying GET_HLS_STREAMING_SESSION_URL for the APIName parameter.
    Retrieve the HLS URL using GetHLSStreamingSessionURL . Kinesis Video Streams creates an HLS streaming session to be used for accessing content in a stream using the HLS protocol. GetHLSStreamingSessionURL returns an authenticated URL (that includes an encrypted session token) for the session's HLS master playlist (the root resource needed for streaming with HLS).
    
    """
    pass

def get_media_for_fragment_list(StreamName=None, Fragments=None):
    """
    Gets media for a list of fragments (specified by fragment number) from the archived data in an Amazon Kinesis video stream.
    The following limits apply when using the GetMediaForFragmentList API:
    See also: AWS API Documentation
    
    
    :example: response = client.get_media_for_fragment_list(
        StreamName='string',
        Fragments=[
            'string',
        ]
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]
            The name of the stream from which to retrieve fragment media.
            

    :type Fragments: list
    :param Fragments: [REQUIRED]
            A list of the numbers of fragments for which to retrieve media. You retrieve these values with ListFragments .
            (string) --
            

    :rtype: dict
    :return: {
        'ContentType': 'string',
        'Payload': StreamingBody()
    }
    
    
    :returns: 
    StreamName (string) -- [REQUIRED]
    The name of the stream from which to retrieve fragment media.
    
    Fragments (list) -- [REQUIRED]
    A list of the numbers of fragments for which to retrieve media. You retrieve these values with  ListFragments .
    
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

def list_fragments(StreamName=None, MaxResults=None, NextToken=None, FragmentSelector=None):
    """
    Returns a list of  Fragment objects from the specified stream and start location within the archived data.
    See also: AWS API Documentation
    
    
    :example: response = client.list_fragments(
        StreamName='string',
        MaxResults=123,
        NextToken='string',
        FragmentSelector={
            'FragmentSelectorType': 'PRODUCER_TIMESTAMP'|'SERVER_TIMESTAMP',
            'TimestampRange': {
                'StartTimestamp': datetime(2015, 1, 1),
                'EndTimestamp': datetime(2015, 1, 1)
            }
        }
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]
            The name of the stream from which to retrieve a fragment list.
            

    :type MaxResults: integer
    :param MaxResults: The total number of fragments to return. If the total number of fragments available is more than the value specified in max-results , then a ListFragmentsOutput$NextToken is provided in the output that you can use to resume pagination.

    :type NextToken: string
    :param NextToken: A token to specify where to start paginating. This is the ListFragmentsOutput$NextToken from a previously truncated response.

    :type FragmentSelector: dict
    :param FragmentSelector: Describes the time stamp range and time stamp origin for the range of fragments to return.
            FragmentSelectorType (string) -- [REQUIRED]The origin of the time stamps to use (Server or Producer).
            TimestampRange (dict) -- [REQUIRED]The range of time stamps to return.
            StartTimestamp (datetime) -- [REQUIRED]The starting time stamp in the range of time stamps for which to return fragments.
            EndTimestamp (datetime) -- [REQUIRED]The ending time stamp in the range of time stamps for which to return fragments.
            
            

    :rtype: dict
    :return: {
        'Fragments': [
            {
                'FragmentNumber': 'string',
                'FragmentSizeInBytes': 123,
                'ProducerTimestamp': datetime(2015, 1, 1),
                'ServerTimestamp': datetime(2015, 1, 1),
                'FragmentLengthInMilliseconds': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

