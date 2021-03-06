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

def batch_update_schedule(ChannelId=None, Creates=None, Deletes=None):
    """
    Update a channel schedule
    See also: AWS API Documentation
    
    
    :example: response = client.batch_update_schedule(
        ChannelId='string',
        Creates={
            'ScheduleActions': [
                {
                    'ActionName': 'string',
                    'ScheduleActionSettings': {
                        'HlsTimedMetadataSettings': {
                            'Id3': 'string'
                        },
                        'InputSwitchSettings': {
                            'InputAttachmentNameReference': 'string'
                        },
                        'Scte35ReturnToNetworkSettings': {
                            'SpliceEventId': 123
                        },
                        'Scte35SpliceInsertSettings': {
                            'Duration': 123,
                            'SpliceEventId': 123
                        },
                        'Scte35TimeSignalSettings': {
                            'Scte35Descriptors': [
                                {
                                    'Scte35DescriptorSettings': {
                                        'SegmentationDescriptorScte35DescriptorSettings': {
                                            'DeliveryRestrictions': {
                                                'ArchiveAllowedFlag': 'ARCHIVE_NOT_ALLOWED'|'ARCHIVE_ALLOWED',
                                                'DeviceRestrictions': 'NONE'|'RESTRICT_GROUP0'|'RESTRICT_GROUP1'|'RESTRICT_GROUP2',
                                                'NoRegionalBlackoutFlag': 'REGIONAL_BLACKOUT'|'NO_REGIONAL_BLACKOUT',
                                                'WebDeliveryAllowedFlag': 'WEB_DELIVERY_NOT_ALLOWED'|'WEB_DELIVERY_ALLOWED'
                                            },
                                            'SegmentNum': 123,
                                            'SegmentationCancelIndicator': 'SEGMENTATION_EVENT_NOT_CANCELED'|'SEGMENTATION_EVENT_CANCELED',
                                            'SegmentationDuration': 123,
                                            'SegmentationEventId': 123,
                                            'SegmentationTypeId': 123,
                                            'SegmentationUpid': 'string',
                                            'SegmentationUpidType': 123,
                                            'SegmentsExpected': 123,
                                            'SubSegmentNum': 123,
                                            'SubSegmentsExpected': 123
                                        }
                                    }
                                },
                            ]
                        },
                        'StaticImageActivateSettings': {
                            'Duration': 123,
                            'FadeIn': 123,
                            'FadeOut': 123,
                            'Height': 123,
                            'Image': {
                                'PasswordParam': 'string',
                                'Uri': 'string',
                                'Username': 'string'
                            },
                            'ImageX': 123,
                            'ImageY': 123,
                            'Layer': 123,
                            'Opacity': 123,
                            'Width': 123
                        },
                        'StaticImageDeactivateSettings': {
                            'FadeOut': 123,
                            'Layer': 123
                        }
                    },
                    'ScheduleActionStartSettings': {
                        'FixedModeScheduleActionStartSettings': {
                            'Time': 'string'
                        },
                        'FollowModeScheduleActionStartSettings': {
                            'FollowPoint': 'END'|'START',
                            'ReferenceActionName': 'string'
                        }
                    }
                },
            ]
        },
        Deletes={
            'ActionNames': [
                'string',
            ]
        }
    )
    
    
    :type ChannelId: string
    :param ChannelId: [REQUIRED] Id of the channel whose schedule is being updated.

    :type Creates: dict
    :param Creates: Schedule actions to create in the schedule.
            ScheduleActions (list) -- [REQUIRED] A list of schedule actions to create.
            (dict) -- Contains information on a single schedule action.
            ActionName (string) -- [REQUIRED] The name of the action, must be unique within the schedule. This name provides the main reference to an action once it is added to the schedule. A name is unique if it is no longer in the schedule. The schedule is automatically cleaned up to remove actions with a start time of more than 1 hour ago (approximately) so at that point a name can be reused.
            ScheduleActionSettings (dict) -- [REQUIRED] Settings for this schedule action.
            HlsTimedMetadataSettings (dict) -- Settings to emit HLS metadata
            Id3 (string) -- [REQUIRED] Base64 string formatted according to the ID3 specification: http://id3.org/id3v2.4.0-structure
            InputSwitchSettings (dict) -- Settings to switch an input
            InputAttachmentNameReference (string) -- [REQUIRED] The name of the input attachment that should be switched to by this action.
            Scte35ReturnToNetworkSettings (dict) -- Settings for SCTE-35 return_to_network message
            SpliceEventId (integer) -- [REQUIRED] The splice_event_id for the SCTE-35 splice_insert, as defined in SCTE-35.
            Scte35SpliceInsertSettings (dict) -- Settings for SCTE-35 splice_insert message
            Duration (integer) -- Optional, the duration for the splice_insert, in 90 KHz ticks. To convert seconds to ticks, multiple the seconds by 90,000. If you enter a duration, there is an expectation that the downstream system can read the duration and cue in at that time. If you do not enter a duration, the splice_insert will continue indefinitely and there is an expectation that you will enter a return_to_network to end the splice_insert at the appropriate time.
            SpliceEventId (integer) -- [REQUIRED] The splice_event_id for the SCTE-35 splice_insert, as defined in SCTE-35.
            Scte35TimeSignalSettings (dict) -- Settings for SCTE-35 time_signal message
            Scte35Descriptors (list) -- [REQUIRED] The list of SCTE-35 descriptors accompanying the SCTE-35 time_signal.
            (dict) -- Holds one set of SCTE-35 Descriptor Settings.
            Scte35DescriptorSettings (dict) -- [REQUIRED] SCTE-35 Descriptor Settings.
            SegmentationDescriptorScte35DescriptorSettings (dict) -- [REQUIRED] SCTE-35 Segmentation Descriptor.
            DeliveryRestrictions (dict) -- Holds the four SCTE-35 delivery restriction parameters.
            ArchiveAllowedFlag (string) -- [REQUIRED] Corresponds to SCTE-35 archive_allowed_flag.
            DeviceRestrictions (string) -- [REQUIRED] Corresponds to SCTE-35 device_restrictions parameter.
            NoRegionalBlackoutFlag (string) -- [REQUIRED] Corresponds to SCTE-35 no_regional_blackout_flag parameter.
            WebDeliveryAllowedFlag (string) -- [REQUIRED] Corresponds to SCTE-35 web_delivery_allowed_flag parameter.
            SegmentNum (integer) -- Corresponds to SCTE-35 segment_num. A value that is valid for the specified segmentation_type_id.
            SegmentationCancelIndicator (string) -- [REQUIRED] Corresponds to SCTE-35 segmentation_event_cancel_indicator.
            SegmentationDuration (integer) -- Corresponds to SCTE-35 segmentation_duration. Optional. The duration for the time_signal, in 90 KHz ticks. To convert seconds to ticks, multiple the seconds by 90,000. Enter time in 90 KHz clock ticks. If you do not enter a duration, the time_signal will continue until you insert a cancellation message.
            SegmentationEventId (integer) -- [REQUIRED] Corresponds to SCTE-35 segmentation_event_id.
            SegmentationTypeId (integer) -- Corresponds to SCTE-35 segmentation_type_id. One of the segmentation_type_id values listed in the SCTE-35 specification. On the console, enter the ID in decimal (for example, '52'). In the CLI, API, or an SDK, enter the ID in hex (for example, '0x34') or decimal (for example, '52').
            SegmentationUpid (string) -- Corresponds to SCTE-35 segmentation_upid. Enter a string containing the hexadecimal representation of the characters that make up the SCTE-35 segmentation_upid value. Must contain an even number of hex characters. Do not include spaces between each hex pair. For example, the ASCII 'ADS Information' becomes hex '41445320496e666f726d6174696f6e.
            SegmentationUpidType (integer) -- Corresponds to SCTE-35 segmentation_upid_type. On the console, enter one of the types listed in the SCTE-35 specification, converted to a decimal. For example, '0x0C' hex from the specification is '12' in decimal. In the CLI, API, or an SDK, enter one of the types listed in the SCTE-35 specification, in either hex (for example, '0x0C' ) or in decimal (for example, '12').
            SegmentsExpected (integer) -- Corresponds to SCTE-35 segments_expected. A value that is valid for the specified segmentation_type_id.
            SubSegmentNum (integer) -- Corresponds to SCTE-35 sub_segment_num. A value that is valid for the specified segmentation_type_id.
            SubSegmentsExpected (integer) -- Corresponds to SCTE-35 sub_segments_expected. A value that is valid for the specified segmentation_type_id.
            
            
            StaticImageActivateSettings (dict) -- Settings to activate a static image overlay
            Duration (integer) -- The duration in milliseconds for the image to remain on the video. If omitted or set to 0 the duration is unlimited and the image will remain until it is explicitly deactivated.
            FadeIn (integer) -- The time in milliseconds for the image to fade in. The fade-in starts at the start time of the overlay. Default is 0 (no fade-in).
            FadeOut (integer) -- Applies only if a duration is specified. The time in milliseconds for the image to fade out. The fade-out starts when the duration time is hit, so it effectively extends the duration. Default is 0 (no fade-out).
            Height (integer) -- The height of the image when inserted into the video, in pixels. The overlay will be scaled up or down to the specified height. Leave blank to use the native height of the overlay.
            Image (dict) -- [REQUIRED] The location and filename of the image file to overlay on the video. The file must be a 32-bit BMP, PNG, or TGA file, and must not be larger (in pixels) than the input video.
            PasswordParam (string) -- key used to extract the password from EC2 Parameter store
            Uri (string) -- [REQUIRED] Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: 'rtmp://fmsserver/live'.
            Username (string) -- Documentation update needed
            ImageX (integer) -- Placement of the left edge of the overlay relative to the left edge of the video frame, in pixels. 0 (the default) is the left edge of the frame. If the placement causes the overlay to extend beyond the right edge of the underlying video, then the overlay is cropped on the right.
            ImageY (integer) -- Placement of the top edge of the overlay relative to the top edge of the video frame, in pixels. 0 (the default) is the top edge of the frame. If the placement causes the overlay to extend beyond the bottom edge of the underlying video, then the overlay is cropped on the bottom.
            Layer (integer) -- The number of the layer, 0 to 7. There are 8 layers that can be overlaid on the video, each layer with a different image. The layers are in Z order, which means that overlays with higher values of layer are inserted on top of overlays with lower values of layer. Default is 0.
            Opacity (integer) -- Opacity of image where 0 is transparent and 100 is fully opaque. Default is 100.
            Width (integer) -- The width of the image when inserted into the video, in pixels. The overlay will be scaled up or down to the specified width. Leave blank to use the native width of the overlay.
            StaticImageDeactivateSettings (dict) -- Settings to deactivate a static image overlay
            FadeOut (integer) -- The time in milliseconds for the image to fade out. Default is 0 (no fade-out).
            Layer (integer) -- The image overlay layer to deactivate, 0 to 7. Default is 0.
            
            ScheduleActionStartSettings (dict) -- [REQUIRED] The time for the action to start in the channel.
            FixedModeScheduleActionStartSettings (dict) -- Holds the start time for the action.
            Time (string) -- [REQUIRED] Start time for the action to start in the channel. (Not the time for the action to be added to the schedule: actions are always added to the schedule immediately.) UTC format: yyyy-mm-ddThh:mm:ss.nnnZ. All the letters are digits (for example, mm might be 01) except for the two constants 'T' for time and 'Z' for 'UTC format'.
            FollowModeScheduleActionStartSettings (dict) -- Specifies an action to follow for scheduling this action.
            FollowPoint (string) -- [REQUIRED] Identifies whether this action starts relative to the start or relative to the end of the reference action.
            ReferenceActionName (string) -- [REQUIRED] The action name of another action that this one refers to.
            
            
            

    :type Deletes: dict
    :param Deletes: Schedule actions to delete from the schedule.
            ActionNames (list) -- [REQUIRED] A list of schedule actions to delete.
            (string) -- Placeholder documentation for __string
            

    :rtype: dict
    :return: {
        'Creates': {
            'ScheduleActions': [
                {
                    'ActionName': 'string',
                    'ScheduleActionSettings': {
                        'HlsTimedMetadataSettings': {
                            'Id3': 'string'
                        },
                        'InputSwitchSettings': {
                            'InputAttachmentNameReference': 'string'
                        },
                        'Scte35ReturnToNetworkSettings': {
                            'SpliceEventId': 123
                        },
                        'Scte35SpliceInsertSettings': {
                            'Duration': 123,
                            'SpliceEventId': 123
                        },
                        'Scte35TimeSignalSettings': {
                            'Scte35Descriptors': [
                                {
                                    'Scte35DescriptorSettings': {
                                        'SegmentationDescriptorScte35DescriptorSettings': {
                                            'DeliveryRestrictions': {
                                                'ArchiveAllowedFlag': 'ARCHIVE_NOT_ALLOWED'|'ARCHIVE_ALLOWED',
                                                'DeviceRestrictions': 'NONE'|'RESTRICT_GROUP0'|'RESTRICT_GROUP1'|'RESTRICT_GROUP2',
                                                'NoRegionalBlackoutFlag': 'REGIONAL_BLACKOUT'|'NO_REGIONAL_BLACKOUT',
                                                'WebDeliveryAllowedFlag': 'WEB_DELIVERY_NOT_ALLOWED'|'WEB_DELIVERY_ALLOWED'
                                            },
                                            'SegmentNum': 123,
                                            'SegmentationCancelIndicator': 'SEGMENTATION_EVENT_NOT_CANCELED'|'SEGMENTATION_EVENT_CANCELED',
                                            'SegmentationDuration': 123,
                                            'SegmentationEventId': 123,
                                            'SegmentationTypeId': 123,
                                            'SegmentationUpid': 'string',
                                            'SegmentationUpidType': 123,
                                            'SegmentsExpected': 123,
                                            'SubSegmentNum': 123,
                                            'SubSegmentsExpected': 123
                                        }
                                    }
                                },
                            ]
                        },
                        'StaticImageActivateSettings': {
                            'Duration': 123,
                            'FadeIn': 123,
                            'FadeOut': 123,
                            'Height': 123,
                            'Image': {
                                'PasswordParam': 'string',
                                'Uri': 'string',
                                'Username': 'string'
                            },
                            'ImageX': 123,
                            'ImageY': 123,
                            'Layer': 123,
                            'Opacity': 123,
                            'Width': 123
                        },
                        'StaticImageDeactivateSettings': {
                            'FadeOut': 123,
                            'Layer': 123
                        }
                    },
                    'ScheduleActionStartSettings': {
                        'FixedModeScheduleActionStartSettings': {
                            'Time': 'string'
                        },
                        'FollowModeScheduleActionStartSettings': {
                            'FollowPoint': 'END'|'START',
                            'ReferenceActionName': 'string'
                        }
                    }
                },
            ]
        },
        'Deletes': {
            'ScheduleActions': [
                {
                    'ActionName': 'string',
                    'ScheduleActionSettings': {
                        'HlsTimedMetadataSettings': {
                            'Id3': 'string'
                        },
                        'InputSwitchSettings': {
                            'InputAttachmentNameReference': 'string'
                        },
                        'Scte35ReturnToNetworkSettings': {
                            'SpliceEventId': 123
                        },
                        'Scte35SpliceInsertSettings': {
                            'Duration': 123,
                            'SpliceEventId': 123
                        },
                        'Scte35TimeSignalSettings': {
                            'Scte35Descriptors': [
                                {
                                    'Scte35DescriptorSettings': {
                                        'SegmentationDescriptorScte35DescriptorSettings': {
                                            'DeliveryRestrictions': {
                                                'ArchiveAllowedFlag': 'ARCHIVE_NOT_ALLOWED'|'ARCHIVE_ALLOWED',
                                                'DeviceRestrictions': 'NONE'|'RESTRICT_GROUP0'|'RESTRICT_GROUP1'|'RESTRICT_GROUP2',
                                                'NoRegionalBlackoutFlag': 'REGIONAL_BLACKOUT'|'NO_REGIONAL_BLACKOUT',
                                                'WebDeliveryAllowedFlag': 'WEB_DELIVERY_NOT_ALLOWED'|'WEB_DELIVERY_ALLOWED'
                                            },
                                            'SegmentNum': 123,
                                            'SegmentationCancelIndicator': 'SEGMENTATION_EVENT_NOT_CANCELED'|'SEGMENTATION_EVENT_CANCELED',
                                            'SegmentationDuration': 123,
                                            'SegmentationEventId': 123,
                                            'SegmentationTypeId': 123,
                                            'SegmentationUpid': 'string',
                                            'SegmentationUpidType': 123,
                                            'SegmentsExpected': 123,
                                            'SubSegmentNum': 123,
                                            'SubSegmentsExpected': 123
                                        }
                                    }
                                },
                            ]
                        },
                        'StaticImageActivateSettings': {
                            'Duration': 123,
                            'FadeIn': 123,
                            'FadeOut': 123,
                            'Height': 123,
                            'Image': {
                                'PasswordParam': 'string',
                                'Uri': 'string',
                                'Username': 'string'
                            },
                            'ImageX': 123,
                            'ImageY': 123,
                            'Layer': 123,
                            'Opacity': 123,
                            'Width': 123
                        },
                        'StaticImageDeactivateSettings': {
                            'FadeOut': 123,
                            'Layer': 123
                        }
                    },
                    'ScheduleActionStartSettings': {
                        'FixedModeScheduleActionStartSettings': {
                            'Time': 'string'
                        },
                        'FollowModeScheduleActionStartSettings': {
                            'FollowPoint': 'END'|'START',
                            'ReferenceActionName': 'string'
                        }
                    }
                },
            ]
        }
    }
    
    
    :returns: 
    (dict) -- Successful update of the schedule.
    Creates (dict) -- Schedule actions created in the schedule.
    ScheduleActions (list) -- List of actions that have been created in the schedule.
    (dict) -- Contains information on a single schedule action.
    ActionName (string) -- The name of the action, must be unique within the schedule. This name provides the main reference to an action once it is added to the schedule. A name is unique if it is no longer in the schedule. The schedule is automatically cleaned up to remove actions with a start time of more than 1 hour ago (approximately) so at that point a name can be reused.
    ScheduleActionSettings (dict) -- Settings for this schedule action.
    HlsTimedMetadataSettings (dict) -- Settings to emit HLS metadata
    Id3 (string) -- Base64 string formatted according to the ID3 specification: http://id3.org/id3v2.4.0-structure
    
    
    InputSwitchSettings (dict) -- Settings to switch an input
    InputAttachmentNameReference (string) -- The name of the input attachment that should be switched to by this action.
    
    
    Scte35ReturnToNetworkSettings (dict) -- Settings for SCTE-35 return_to_network message
    SpliceEventId (integer) -- The splice_event_id for the SCTE-35 splice_insert, as defined in SCTE-35.
    
    
    Scte35SpliceInsertSettings (dict) -- Settings for SCTE-35 splice_insert message
    Duration (integer) -- Optional, the duration for the splice_insert, in 90 KHz ticks. To convert seconds to ticks, multiple the seconds by 90,000. If you enter a duration, there is an expectation that the downstream system can read the duration and cue in at that time. If you do not enter a duration, the splice_insert will continue indefinitely and there is an expectation that you will enter a return_to_network to end the splice_insert at the appropriate time.
    SpliceEventId (integer) -- The splice_event_id for the SCTE-35 splice_insert, as defined in SCTE-35.
    
    
    Scte35TimeSignalSettings (dict) -- Settings for SCTE-35 time_signal message
    Scte35Descriptors (list) -- The list of SCTE-35 descriptors accompanying the SCTE-35 time_signal.
    (dict) -- Holds one set of SCTE-35 Descriptor Settings.
    Scte35DescriptorSettings (dict) -- SCTE-35 Descriptor Settings.
    SegmentationDescriptorScte35DescriptorSettings (dict) -- SCTE-35 Segmentation Descriptor.
    DeliveryRestrictions (dict) -- Holds the four SCTE-35 delivery restriction parameters.
    ArchiveAllowedFlag (string) -- Corresponds to SCTE-35 archive_allowed_flag.
    DeviceRestrictions (string) -- Corresponds to SCTE-35 device_restrictions parameter.
    NoRegionalBlackoutFlag (string) -- Corresponds to SCTE-35 no_regional_blackout_flag parameter.
    WebDeliveryAllowedFlag (string) -- Corresponds to SCTE-35 web_delivery_allowed_flag parameter.
    
    
    SegmentNum (integer) -- Corresponds to SCTE-35 segment_num. A value that is valid for the specified segmentation_type_id.
    SegmentationCancelIndicator (string) -- Corresponds to SCTE-35 segmentation_event_cancel_indicator.
    SegmentationDuration (integer) -- Corresponds to SCTE-35 segmentation_duration. Optional. The duration for the time_signal, in 90 KHz ticks. To convert seconds to ticks, multiple the seconds by 90,000. Enter time in 90 KHz clock ticks. If you do not enter a duration, the time_signal will continue until you insert a cancellation message.
    SegmentationEventId (integer) -- Corresponds to SCTE-35 segmentation_event_id.
    SegmentationTypeId (integer) -- Corresponds to SCTE-35 segmentation_type_id. One of the segmentation_type_id values listed in the SCTE-35 specification. On the console, enter the ID in decimal (for example, "52"). In the CLI, API, or an SDK, enter the ID in hex (for example, "0x34") or decimal (for example, "52").
    SegmentationUpid (string) -- Corresponds to SCTE-35 segmentation_upid. Enter a string containing the hexadecimal representation of the characters that make up the SCTE-35 segmentation_upid value. Must contain an even number of hex characters. Do not include spaces between each hex pair. For example, the ASCII "ADS Information" becomes hex "41445320496e666f726d6174696f6e.
    SegmentationUpidType (integer) -- Corresponds to SCTE-35 segmentation_upid_type. On the console, enter one of the types listed in the SCTE-35 specification, converted to a decimal. For example, "0x0C" hex from the specification is "12" in decimal. In the CLI, API, or an SDK, enter one of the types listed in the SCTE-35 specification, in either hex (for example, "0x0C" ) or in decimal (for example, "12").
    SegmentsExpected (integer) -- Corresponds to SCTE-35 segments_expected. A value that is valid for the specified segmentation_type_id.
    SubSegmentNum (integer) -- Corresponds to SCTE-35 sub_segment_num. A value that is valid for the specified segmentation_type_id.
    SubSegmentsExpected (integer) -- Corresponds to SCTE-35 sub_segments_expected. A value that is valid for the specified segmentation_type_id.
    
    
    
    
    
    
    
    
    
    
    StaticImageActivateSettings (dict) -- Settings to activate a static image overlay
    Duration (integer) -- The duration in milliseconds for the image to remain on the video. If omitted or set to 0 the duration is unlimited and the image will remain until it is explicitly deactivated.
    FadeIn (integer) -- The time in milliseconds for the image to fade in. The fade-in starts at the start time of the overlay. Default is 0 (no fade-in).
    FadeOut (integer) -- Applies only if a duration is specified. The time in milliseconds for the image to fade out. The fade-out starts when the duration time is hit, so it effectively extends the duration. Default is 0 (no fade-out).
    Height (integer) -- The height of the image when inserted into the video, in pixels. The overlay will be scaled up or down to the specified height. Leave blank to use the native height of the overlay.
    Image (dict) -- The location and filename of the image file to overlay on the video. The file must be a 32-bit BMP, PNG, or TGA file, and must not be larger (in pixels) than the input video.
    PasswordParam (string) -- key used to extract the password from EC2 Parameter store
    Uri (string) -- Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: "rtmp://fmsserver/live".
    Username (string) -- Documentation update needed
    
    
    ImageX (integer) -- Placement of the left edge of the overlay relative to the left edge of the video frame, in pixels. 0 (the default) is the left edge of the frame. If the placement causes the overlay to extend beyond the right edge of the underlying video, then the overlay is cropped on the right.
    ImageY (integer) -- Placement of the top edge of the overlay relative to the top edge of the video frame, in pixels. 0 (the default) is the top edge of the frame. If the placement causes the overlay to extend beyond the bottom edge of the underlying video, then the overlay is cropped on the bottom.
    Layer (integer) -- The number of the layer, 0 to 7. There are 8 layers that can be overlaid on the video, each layer with a different image. The layers are in Z order, which means that overlays with higher values of layer are inserted on top of overlays with lower values of layer. Default is 0.
    Opacity (integer) -- Opacity of image where 0 is transparent and 100 is fully opaque. Default is 100.
    Width (integer) -- The width of the image when inserted into the video, in pixels. The overlay will be scaled up or down to the specified width. Leave blank to use the native width of the overlay.
    
    
    StaticImageDeactivateSettings (dict) -- Settings to deactivate a static image overlay
    FadeOut (integer) -- The time in milliseconds for the image to fade out. Default is 0 (no fade-out).
    Layer (integer) -- The image overlay layer to deactivate, 0 to 7. Default is 0.
    
    
    
    
    ScheduleActionStartSettings (dict) -- The time for the action to start in the channel.
    FixedModeScheduleActionStartSettings (dict) -- Holds the start time for the action.
    Time (string) -- Start time for the action to start in the channel. (Not the time for the action to be added to the schedule: actions are always added to the schedule immediately.) UTC format: yyyy-mm-ddThh:mm:ss.nnnZ. All the letters are digits (for example, mm might be 01) except for the two constants "T" for time and "Z" for "UTC format".
    
    
    FollowModeScheduleActionStartSettings (dict) -- Specifies an action to follow for scheduling this action.
    FollowPoint (string) -- Identifies whether this action starts relative to the start or relative to the end of the reference action.
    ReferenceActionName (string) -- The action name of another action that this one refers to.
    
    
    
    
    
    
    
    
    
    
    Deletes (dict) -- Schedule actions deleted from the schedule.
    ScheduleActions (list) -- List of actions that have been deleted from the schedule.
    (dict) -- Contains information on a single schedule action.
    ActionName (string) -- The name of the action, must be unique within the schedule. This name provides the main reference to an action once it is added to the schedule. A name is unique if it is no longer in the schedule. The schedule is automatically cleaned up to remove actions with a start time of more than 1 hour ago (approximately) so at that point a name can be reused.
    ScheduleActionSettings (dict) -- Settings for this schedule action.
    HlsTimedMetadataSettings (dict) -- Settings to emit HLS metadata
    Id3 (string) -- Base64 string formatted according to the ID3 specification: http://id3.org/id3v2.4.0-structure
    
    
    InputSwitchSettings (dict) -- Settings to switch an input
    InputAttachmentNameReference (string) -- The name of the input attachment that should be switched to by this action.
    
    
    Scte35ReturnToNetworkSettings (dict) -- Settings for SCTE-35 return_to_network message
    SpliceEventId (integer) -- The splice_event_id for the SCTE-35 splice_insert, as defined in SCTE-35.
    
    
    Scte35SpliceInsertSettings (dict) -- Settings for SCTE-35 splice_insert message
    Duration (integer) -- Optional, the duration for the splice_insert, in 90 KHz ticks. To convert seconds to ticks, multiple the seconds by 90,000. If you enter a duration, there is an expectation that the downstream system can read the duration and cue in at that time. If you do not enter a duration, the splice_insert will continue indefinitely and there is an expectation that you will enter a return_to_network to end the splice_insert at the appropriate time.
    SpliceEventId (integer) -- The splice_event_id for the SCTE-35 splice_insert, as defined in SCTE-35.
    
    
    Scte35TimeSignalSettings (dict) -- Settings for SCTE-35 time_signal message
    Scte35Descriptors (list) -- The list of SCTE-35 descriptors accompanying the SCTE-35 time_signal.
    (dict) -- Holds one set of SCTE-35 Descriptor Settings.
    Scte35DescriptorSettings (dict) -- SCTE-35 Descriptor Settings.
    SegmentationDescriptorScte35DescriptorSettings (dict) -- SCTE-35 Segmentation Descriptor.
    DeliveryRestrictions (dict) -- Holds the four SCTE-35 delivery restriction parameters.
    ArchiveAllowedFlag (string) -- Corresponds to SCTE-35 archive_allowed_flag.
    DeviceRestrictions (string) -- Corresponds to SCTE-35 device_restrictions parameter.
    NoRegionalBlackoutFlag (string) -- Corresponds to SCTE-35 no_regional_blackout_flag parameter.
    WebDeliveryAllowedFlag (string) -- Corresponds to SCTE-35 web_delivery_allowed_flag parameter.
    
    
    SegmentNum (integer) -- Corresponds to SCTE-35 segment_num. A value that is valid for the specified segmentation_type_id.
    SegmentationCancelIndicator (string) -- Corresponds to SCTE-35 segmentation_event_cancel_indicator.
    SegmentationDuration (integer) -- Corresponds to SCTE-35 segmentation_duration. Optional. The duration for the time_signal, in 90 KHz ticks. To convert seconds to ticks, multiple the seconds by 90,000. Enter time in 90 KHz clock ticks. If you do not enter a duration, the time_signal will continue until you insert a cancellation message.
    SegmentationEventId (integer) -- Corresponds to SCTE-35 segmentation_event_id.
    SegmentationTypeId (integer) -- Corresponds to SCTE-35 segmentation_type_id. One of the segmentation_type_id values listed in the SCTE-35 specification. On the console, enter the ID in decimal (for example, "52"). In the CLI, API, or an SDK, enter the ID in hex (for example, "0x34") or decimal (for example, "52").
    SegmentationUpid (string) -- Corresponds to SCTE-35 segmentation_upid. Enter a string containing the hexadecimal representation of the characters that make up the SCTE-35 segmentation_upid value. Must contain an even number of hex characters. Do not include spaces between each hex pair. For example, the ASCII "ADS Information" becomes hex "41445320496e666f726d6174696f6e.
    SegmentationUpidType (integer) -- Corresponds to SCTE-35 segmentation_upid_type. On the console, enter one of the types listed in the SCTE-35 specification, converted to a decimal. For example, "0x0C" hex from the specification is "12" in decimal. In the CLI, API, or an SDK, enter one of the types listed in the SCTE-35 specification, in either hex (for example, "0x0C" ) or in decimal (for example, "12").
    SegmentsExpected (integer) -- Corresponds to SCTE-35 segments_expected. A value that is valid for the specified segmentation_type_id.
    SubSegmentNum (integer) -- Corresponds to SCTE-35 sub_segment_num. A value that is valid for the specified segmentation_type_id.
    SubSegmentsExpected (integer) -- Corresponds to SCTE-35 sub_segments_expected. A value that is valid for the specified segmentation_type_id.
    
    
    
    
    
    
    
    
    
    
    StaticImageActivateSettings (dict) -- Settings to activate a static image overlay
    Duration (integer) -- The duration in milliseconds for the image to remain on the video. If omitted or set to 0 the duration is unlimited and the image will remain until it is explicitly deactivated.
    FadeIn (integer) -- The time in milliseconds for the image to fade in. The fade-in starts at the start time of the overlay. Default is 0 (no fade-in).
    FadeOut (integer) -- Applies only if a duration is specified. The time in milliseconds for the image to fade out. The fade-out starts when the duration time is hit, so it effectively extends the duration. Default is 0 (no fade-out).
    Height (integer) -- The height of the image when inserted into the video, in pixels. The overlay will be scaled up or down to the specified height. Leave blank to use the native height of the overlay.
    Image (dict) -- The location and filename of the image file to overlay on the video. The file must be a 32-bit BMP, PNG, or TGA file, and must not be larger (in pixels) than the input video.
    PasswordParam (string) -- key used to extract the password from EC2 Parameter store
    Uri (string) -- Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: "rtmp://fmsserver/live".
    Username (string) -- Documentation update needed
    
    
    ImageX (integer) -- Placement of the left edge of the overlay relative to the left edge of the video frame, in pixels. 0 (the default) is the left edge of the frame. If the placement causes the overlay to extend beyond the right edge of the underlying video, then the overlay is cropped on the right.
    ImageY (integer) -- Placement of the top edge of the overlay relative to the top edge of the video frame, in pixels. 0 (the default) is the top edge of the frame. If the placement causes the overlay to extend beyond the bottom edge of the underlying video, then the overlay is cropped on the bottom.
    Layer (integer) -- The number of the layer, 0 to 7. There are 8 layers that can be overlaid on the video, each layer with a different image. The layers are in Z order, which means that overlays with higher values of layer are inserted on top of overlays with lower values of layer. Default is 0.
    Opacity (integer) -- Opacity of image where 0 is transparent and 100 is fully opaque. Default is 100.
    Width (integer) -- The width of the image when inserted into the video, in pixels. The overlay will be scaled up or down to the specified width. Leave blank to use the native width of the overlay.
    
    
    StaticImageDeactivateSettings (dict) -- Settings to deactivate a static image overlay
    FadeOut (integer) -- The time in milliseconds for the image to fade out. Default is 0 (no fade-out).
    Layer (integer) -- The image overlay layer to deactivate, 0 to 7. Default is 0.
    
    
    
    
    ScheduleActionStartSettings (dict) -- The time for the action to start in the channel.
    FixedModeScheduleActionStartSettings (dict) -- Holds the start time for the action.
    Time (string) -- Start time for the action to start in the channel. (Not the time for the action to be added to the schedule: actions are always added to the schedule immediately.) UTC format: yyyy-mm-ddThh:mm:ss.nnnZ. All the letters are digits (for example, mm might be 01) except for the two constants "T" for time and "Z" for "UTC format".
    
    
    FollowModeScheduleActionStartSettings (dict) -- Specifies an action to follow for scheduling this action.
    FollowPoint (string) -- Identifies whether this action starts relative to the start or relative to the end of the reference action.
    ReferenceActionName (string) -- The action name of another action that this one refers to.
    
    
    
    
    
    
    
    
    
    
    
    
    
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

def create_channel(Destinations=None, EncoderSettings=None, InputAttachments=None, InputSpecification=None, LogLevel=None, Name=None, RequestId=None, Reserved=None, RoleArn=None):
    """
    Creates a new channel
    See also: AWS API Documentation
    
    
    :example: response = client.create_channel(
        Destinations=[
            {
                'Id': 'string',
                'Settings': [
                    {
                        'PasswordParam': 'string',
                        'StreamName': 'string',
                        'Url': 'string',
                        'Username': 'string'
                    },
                ]
            },
        ],
        EncoderSettings={
            'AudioDescriptions': [
                {
                    'AudioNormalizationSettings': {
                        'Algorithm': 'ITU_1770_1'|'ITU_1770_2',
                        'AlgorithmControl': 'CORRECT_AUDIO',
                        'TargetLkfs': 123.0
                    },
                    'AudioSelectorName': 'string',
                    'AudioType': 'CLEAN_EFFECTS'|'HEARING_IMPAIRED'|'UNDEFINED'|'VISUAL_IMPAIRED_COMMENTARY',
                    'AudioTypeControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                    'CodecSettings': {
                        'AacSettings': {
                            'Bitrate': 123.0,
                            'CodingMode': 'AD_RECEIVER_MIX'|'CODING_MODE_1_0'|'CODING_MODE_1_1'|'CODING_MODE_2_0'|'CODING_MODE_5_1',
                            'InputType': 'BROADCASTER_MIXED_AD'|'NORMAL',
                            'Profile': 'HEV1'|'HEV2'|'LC',
                            'RateControlMode': 'CBR'|'VBR',
                            'RawFormat': 'LATM_LOAS'|'NONE',
                            'SampleRate': 123.0,
                            'Spec': 'MPEG2'|'MPEG4',
                            'VbrQuality': 'HIGH'|'LOW'|'MEDIUM_HIGH'|'MEDIUM_LOW'
                        },
                        'Ac3Settings': {
                            'Bitrate': 123.0,
                            'BitstreamMode': 'COMMENTARY'|'COMPLETE_MAIN'|'DIALOGUE'|'EMERGENCY'|'HEARING_IMPAIRED'|'MUSIC_AND_EFFECTS'|'VISUALLY_IMPAIRED'|'VOICE_OVER',
                            'CodingMode': 'CODING_MODE_1_0'|'CODING_MODE_1_1'|'CODING_MODE_2_0'|'CODING_MODE_3_2_LFE',
                            'Dialnorm': 123,
                            'DrcProfile': 'FILM_STANDARD'|'NONE',
                            'LfeFilter': 'DISABLED'|'ENABLED',
                            'MetadataControl': 'FOLLOW_INPUT'|'USE_CONFIGURED'
                        },
                        'Eac3Settings': {
                            'AttenuationControl': 'ATTENUATE_3_DB'|'NONE',
                            'Bitrate': 123.0,
                            'BitstreamMode': 'COMMENTARY'|'COMPLETE_MAIN'|'EMERGENCY'|'HEARING_IMPAIRED'|'VISUALLY_IMPAIRED',
                            'CodingMode': 'CODING_MODE_1_0'|'CODING_MODE_2_0'|'CODING_MODE_3_2',
                            'DcFilter': 'DISABLED'|'ENABLED',
                            'Dialnorm': 123,
                            'DrcLine': 'FILM_LIGHT'|'FILM_STANDARD'|'MUSIC_LIGHT'|'MUSIC_STANDARD'|'NONE'|'SPEECH',
                            'DrcRf': 'FILM_LIGHT'|'FILM_STANDARD'|'MUSIC_LIGHT'|'MUSIC_STANDARD'|'NONE'|'SPEECH',
                            'LfeControl': 'LFE'|'NO_LFE',
                            'LfeFilter': 'DISABLED'|'ENABLED',
                            'LoRoCenterMixLevel': 123.0,
                            'LoRoSurroundMixLevel': 123.0,
                            'LtRtCenterMixLevel': 123.0,
                            'LtRtSurroundMixLevel': 123.0,
                            'MetadataControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                            'PassthroughControl': 'NO_PASSTHROUGH'|'WHEN_POSSIBLE',
                            'PhaseControl': 'NO_SHIFT'|'SHIFT_90_DEGREES',
                            'StereoDownmix': 'DPL2'|'LO_RO'|'LT_RT'|'NOT_INDICATED',
                            'SurroundExMode': 'DISABLED'|'ENABLED'|'NOT_INDICATED',
                            'SurroundMode': 'DISABLED'|'ENABLED'|'NOT_INDICATED'
                        },
                        'Mp2Settings': {
                            'Bitrate': 123.0,
                            'CodingMode': 'CODING_MODE_1_0'|'CODING_MODE_2_0',
                            'SampleRate': 123.0
                        },
                        'PassThroughSettings': {}
    
                    },
                    'LanguageCode': 'string',
                    'LanguageCodeControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                    'Name': 'string',
                    'RemixSettings': {
                        'ChannelMappings': [
                            {
                                'InputChannelLevels': [
                                    {
                                        'Gain': 123,
                                        'InputChannel': 123
                                    },
                                ],
                                'OutputChannel': 123
                            },
                        ],
                        'ChannelsIn': 123,
                        'ChannelsOut': 123
                    },
                    'StreamName': 'string'
                },
            ],
            'AvailBlanking': {
                'AvailBlankingImage': {
                    'PasswordParam': 'string',
                    'Uri': 'string',
                    'Username': 'string'
                },
                'State': 'DISABLED'|'ENABLED'
            },
            'AvailConfiguration': {
                'AvailSettings': {
                    'Scte35SpliceInsert': {
                        'AdAvailOffset': 123,
                        'NoRegionalBlackoutFlag': 'FOLLOW'|'IGNORE',
                        'WebDeliveryAllowedFlag': 'FOLLOW'|'IGNORE'
                    },
                    'Scte35TimeSignalApos': {
                        'AdAvailOffset': 123,
                        'NoRegionalBlackoutFlag': 'FOLLOW'|'IGNORE',
                        'WebDeliveryAllowedFlag': 'FOLLOW'|'IGNORE'
                    }
                }
            },
            'BlackoutSlate': {
                'BlackoutSlateImage': {
                    'PasswordParam': 'string',
                    'Uri': 'string',
                    'Username': 'string'
                },
                'NetworkEndBlackout': 'DISABLED'|'ENABLED',
                'NetworkEndBlackoutImage': {
                    'PasswordParam': 'string',
                    'Uri': 'string',
                    'Username': 'string'
                },
                'NetworkId': 'string',
                'State': 'DISABLED'|'ENABLED'
            },
            'CaptionDescriptions': [
                {
                    'CaptionSelectorName': 'string',
                    'DestinationSettings': {
                        'AribDestinationSettings': {}
                        ,
                        'BurnInDestinationSettings': {
                            'Alignment': 'CENTERED'|'LEFT'|'SMART',
                            'BackgroundColor': 'BLACK'|'NONE'|'WHITE',
                            'BackgroundOpacity': 123,
                            'Font': {
                                'PasswordParam': 'string',
                                'Uri': 'string',
                                'Username': 'string'
                            },
                            'FontColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                            'FontOpacity': 123,
                            'FontResolution': 123,
                            'FontSize': 'string',
                            'OutlineColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                            'OutlineSize': 123,
                            'ShadowColor': 'BLACK'|'NONE'|'WHITE',
                            'ShadowOpacity': 123,
                            'ShadowXOffset': 123,
                            'ShadowYOffset': 123,
                            'TeletextGridControl': 'FIXED'|'SCALED',
                            'XPosition': 123,
                            'YPosition': 123
                        },
                        'DvbSubDestinationSettings': {
                            'Alignment': 'CENTERED'|'LEFT'|'SMART',
                            'BackgroundColor': 'BLACK'|'NONE'|'WHITE',
                            'BackgroundOpacity': 123,
                            'Font': {
                                'PasswordParam': 'string',
                                'Uri': 'string',
                                'Username': 'string'
                            },
                            'FontColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                            'FontOpacity': 123,
                            'FontResolution': 123,
                            'FontSize': 'string',
                            'OutlineColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                            'OutlineSize': 123,
                            'ShadowColor': 'BLACK'|'NONE'|'WHITE',
                            'ShadowOpacity': 123,
                            'ShadowXOffset': 123,
                            'ShadowYOffset': 123,
                            'TeletextGridControl': 'FIXED'|'SCALED',
                            'XPosition': 123,
                            'YPosition': 123
                        },
                        'EmbeddedDestinationSettings': {}
                        ,
                        'EmbeddedPlusScte20DestinationSettings': {}
                        ,
                        'RtmpCaptionInfoDestinationSettings': {}
                        ,
                        'Scte20PlusEmbeddedDestinationSettings': {}
                        ,
                        'Scte27DestinationSettings': {}
                        ,
                        'SmpteTtDestinationSettings': {}
                        ,
                        'TeletextDestinationSettings': {}
                        ,
                        'TtmlDestinationSettings': {
                            'StyleControl': 'PASSTHROUGH'|'USE_CONFIGURED'
                        },
                        'WebvttDestinationSettings': {}
    
                    },
                    'LanguageCode': 'string',
                    'LanguageDescription': 'string',
                    'Name': 'string'
                },
            ],
            'GlobalConfiguration': {
                'InitialAudioGain': 123,
                'InputEndAction': 'NONE'|'SWITCH_AND_LOOP_INPUTS',
                'InputLossBehavior': {
                    'BlackFrameMsec': 123,
                    'InputLossImageColor': 'string',
                    'InputLossImageSlate': {
                        'PasswordParam': 'string',
                        'Uri': 'string',
                        'Username': 'string'
                    },
                    'InputLossImageType': 'COLOR'|'SLATE',
                    'RepeatFrameMsec': 123
                },
                'OutputTimingSource': 'INPUT_CLOCK'|'SYSTEM_CLOCK',
                'SupportLowFramerateInputs': 'DISABLED'|'ENABLED'
            },
            'OutputGroups': [
                {
                    'Name': 'string',
                    'OutputGroupSettings': {
                        'ArchiveGroupSettings': {
                            'Destination': {
                                'DestinationRefId': 'string'
                            },
                            'RolloverInterval': 123
                        },
                        'HlsGroupSettings': {
                            'AdMarkers': [
                                'ADOBE'|'ELEMENTAL'|'ELEMENTAL_SCTE35',
                            ],
                            'BaseUrlContent': 'string',
                            'BaseUrlManifest': 'string',
                            'CaptionLanguageMappings': [
                                {
                                    'CaptionChannel': 123,
                                    'LanguageCode': 'string',
                                    'LanguageDescription': 'string'
                                },
                            ],
                            'CaptionLanguageSetting': 'INSERT'|'NONE'|'OMIT',
                            'ClientCache': 'DISABLED'|'ENABLED',
                            'CodecSpecification': 'RFC_4281'|'RFC_6381',
                            'ConstantIv': 'string',
                            'Destination': {
                                'DestinationRefId': 'string'
                            },
                            'DirectoryStructure': 'SINGLE_DIRECTORY'|'SUBDIRECTORY_PER_STREAM',
                            'EncryptionType': 'AES128'|'SAMPLE_AES',
                            'HlsCdnSettings': {
                                'HlsAkamaiSettings': {
                                    'ConnectionRetryInterval': 123,
                                    'FilecacheDuration': 123,
                                    'HttpTransferMode': 'CHUNKED'|'NON_CHUNKED',
                                    'NumRetries': 123,
                                    'RestartDelay': 123,
                                    'Salt': 'string',
                                    'Token': 'string'
                                },
                                'HlsBasicPutSettings': {
                                    'ConnectionRetryInterval': 123,
                                    'FilecacheDuration': 123,
                                    'NumRetries': 123,
                                    'RestartDelay': 123
                                },
                                'HlsMediaStoreSettings': {
                                    'ConnectionRetryInterval': 123,
                                    'FilecacheDuration': 123,
                                    'MediaStoreStorageClass': 'TEMPORAL',
                                    'NumRetries': 123,
                                    'RestartDelay': 123
                                },
                                'HlsWebdavSettings': {
                                    'ConnectionRetryInterval': 123,
                                    'FilecacheDuration': 123,
                                    'HttpTransferMode': 'CHUNKED'|'NON_CHUNKED',
                                    'NumRetries': 123,
                                    'RestartDelay': 123
                                }
                            },
                            'IndexNSegments': 123,
                            'InputLossAction': 'EMIT_OUTPUT'|'PAUSE_OUTPUT',
                            'IvInManifest': 'EXCLUDE'|'INCLUDE',
                            'IvSource': 'EXPLICIT'|'FOLLOWS_SEGMENT_NUMBER',
                            'KeepSegments': 123,
                            'KeyFormat': 'string',
                            'KeyFormatVersions': 'string',
                            'KeyProviderSettings': {
                                'StaticKeySettings': {
                                    'KeyProviderServer': {
                                        'PasswordParam': 'string',
                                        'Uri': 'string',
                                        'Username': 'string'
                                    },
                                    'StaticKeyValue': 'string'
                                }
                            },
                            'ManifestCompression': 'GZIP'|'NONE',
                            'ManifestDurationFormat': 'FLOATING_POINT'|'INTEGER',
                            'MinSegmentLength': 123,
                            'Mode': 'LIVE'|'VOD',
                            'OutputSelection': 'MANIFESTS_AND_SEGMENTS'|'SEGMENTS_ONLY',
                            'ProgramDateTime': 'EXCLUDE'|'INCLUDE',
                            'ProgramDateTimePeriod': 123,
                            'RedundantManifest': 'DISABLED'|'ENABLED',
                            'SegmentLength': 123,
                            'SegmentationMode': 'USE_INPUT_SEGMENTATION'|'USE_SEGMENT_DURATION',
                            'SegmentsPerSubdirectory': 123,
                            'StreamInfResolution': 'EXCLUDE'|'INCLUDE',
                            'TimedMetadataId3Frame': 'NONE'|'PRIV'|'TDRL',
                            'TimedMetadataId3Period': 123,
                            'TimestampDeltaMilliseconds': 123,
                            'TsFileMode': 'SEGMENTED_FILES'|'SINGLE_FILE'
                        },
                        'MsSmoothGroupSettings': {
                            'AcquisitionPointId': 'string',
                            'AudioOnlyTimecodeControl': 'PASSTHROUGH'|'USE_CONFIGURED_CLOCK',
                            'CertificateMode': 'SELF_SIGNED'|'VERIFY_AUTHENTICITY',
                            'ConnectionRetryInterval': 123,
                            'Destination': {
                                'DestinationRefId': 'string'
                            },
                            'EventId': 'string',
                            'EventIdMode': 'NO_EVENT_ID'|'USE_CONFIGURED'|'USE_TIMESTAMP',
                            'EventStopBehavior': 'NONE'|'SEND_EOS',
                            'FilecacheDuration': 123,
                            'FragmentLength': 123,
                            'InputLossAction': 'EMIT_OUTPUT'|'PAUSE_OUTPUT',
                            'NumRetries': 123,
                            'RestartDelay': 123,
                            'SegmentationMode': 'USE_INPUT_SEGMENTATION'|'USE_SEGMENT_DURATION',
                            'SendDelayMs': 123,
                            'SparseTrackType': 'NONE'|'SCTE_35',
                            'StreamManifestBehavior': 'DO_NOT_SEND'|'SEND',
                            'TimestampOffset': 'string',
                            'TimestampOffsetMode': 'USE_CONFIGURED_OFFSET'|'USE_EVENT_START_DATE'
                        },
                        'RtmpGroupSettings': {
                            'AuthenticationScheme': 'AKAMAI'|'COMMON',
                            'CacheFullBehavior': 'DISCONNECT_IMMEDIATELY'|'WAIT_FOR_SERVER',
                            'CacheLength': 123,
                            'CaptionData': 'ALL'|'FIELD1_608'|'FIELD1_AND_FIELD2_608',
                            'InputLossAction': 'EMIT_OUTPUT'|'PAUSE_OUTPUT',
                            'RestartDelay': 123
                        },
                        'UdpGroupSettings': {
                            'InputLossAction': 'DROP_PROGRAM'|'DROP_TS'|'EMIT_PROGRAM',
                            'TimedMetadataId3Frame': 'NONE'|'PRIV'|'TDRL',
                            'TimedMetadataId3Period': 123
                        }
                    },
                    'Outputs': [
                        {
                            'AudioDescriptionNames': [
                                'string',
                            ],
                            'CaptionDescriptionNames': [
                                'string',
                            ],
                            'OutputName': 'string',
                            'OutputSettings': {
                                'ArchiveOutputSettings': {
                                    'ContainerSettings': {
                                        'M2tsSettings': {
                                            'AbsentInputAudioBehavior': 'DROP'|'ENCODE_SILENCE',
                                            'Arib': 'DISABLED'|'ENABLED',
                                            'AribCaptionsPid': 'string',
                                            'AribCaptionsPidControl': 'AUTO'|'USE_CONFIGURED',
                                            'AudioBufferModel': 'ATSC'|'DVB',
                                            'AudioFramesPerPes': 123,
                                            'AudioPids': 'string',
                                            'AudioStreamType': 'ATSC'|'DVB',
                                            'Bitrate': 123,
                                            'BufferModel': 'MULTIPLEX'|'NONE',
                                            'CcDescriptor': 'DISABLED'|'ENABLED',
                                            'DvbNitSettings': {
                                                'NetworkId': 123,
                                                'NetworkName': 'string',
                                                'RepInterval': 123
                                            },
                                            'DvbSdtSettings': {
                                                'OutputSdt': 'SDT_FOLLOW'|'SDT_FOLLOW_IF_PRESENT'|'SDT_MANUAL'|'SDT_NONE',
                                                'RepInterval': 123,
                                                'ServiceName': 'string',
                                                'ServiceProviderName': 'string'
                                            },
                                            'DvbSubPids': 'string',
                                            'DvbTdtSettings': {
                                                'RepInterval': 123
                                            },
                                            'DvbTeletextPid': 'string',
                                            'Ebif': 'NONE'|'PASSTHROUGH',
                                            'EbpAudioInterval': 'VIDEO_AND_FIXED_INTERVALS'|'VIDEO_INTERVAL',
                                            'EbpLookaheadMs': 123,
                                            'EbpPlacement': 'VIDEO_AND_AUDIO_PIDS'|'VIDEO_PID',
                                            'EcmPid': 'string',
                                            'EsRateInPes': 'EXCLUDE'|'INCLUDE',
                                            'EtvPlatformPid': 'string',
                                            'EtvSignalPid': 'string',
                                            'FragmentTime': 123.0,
                                            'Klv': 'NONE'|'PASSTHROUGH',
                                            'KlvDataPids': 'string',
                                            'NullPacketBitrate': 123.0,
                                            'PatInterval': 123,
                                            'PcrControl': 'CONFIGURED_PCR_PERIOD'|'PCR_EVERY_PES_PACKET',
                                            'PcrPeriod': 123,
                                            'PcrPid': 'string',
                                            'PmtInterval': 123,
                                            'PmtPid': 'string',
                                            'ProgramNum': 123,
                                            'RateMode': 'CBR'|'VBR',
                                            'Scte27Pids': 'string',
                                            'Scte35Control': 'NONE'|'PASSTHROUGH',
                                            'Scte35Pid': 'string',
                                            'SegmentationMarkers': 'EBP'|'EBP_LEGACY'|'NONE'|'PSI_SEGSTART'|'RAI_ADAPT'|'RAI_SEGSTART',
                                            'SegmentationStyle': 'MAINTAIN_CADENCE'|'RESET_CADENCE',
                                            'SegmentationTime': 123.0,
                                            'TimedMetadataBehavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                            'TimedMetadataPid': 'string',
                                            'TransportStreamId': 123,
                                            'VideoPid': 'string'
                                        }
                                    },
                                    'Extension': 'string',
                                    'NameModifier': 'string'
                                },
                                'HlsOutputSettings': {
                                    'HlsSettings': {
                                        'AudioOnlyHlsSettings': {
                                            'AudioGroupId': 'string',
                                            'AudioOnlyImage': {
                                                'PasswordParam': 'string',
                                                'Uri': 'string',
                                                'Username': 'string'
                                            },
                                            'AudioTrackType': 'ALTERNATE_AUDIO_AUTO_SELECT'|'ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT'|'ALTERNATE_AUDIO_NOT_AUTO_SELECT'|'AUDIO_ONLY_VARIANT_STREAM'
                                        },
                                        'StandardHlsSettings': {
                                            'AudioRenditionSets': 'string',
                                            'M3u8Settings': {
                                                'AudioFramesPerPes': 123,
                                                'AudioPids': 'string',
                                                'EcmPid': 'string',
                                                'PatInterval': 123,
                                                'PcrControl': 'CONFIGURED_PCR_PERIOD'|'PCR_EVERY_PES_PACKET',
                                                'PcrPeriod': 123,
                                                'PcrPid': 'string',
                                                'PmtInterval': 123,
                                                'PmtPid': 'string',
                                                'ProgramNum': 123,
                                                'Scte35Behavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                                'Scte35Pid': 'string',
                                                'TimedMetadataBehavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                                'TimedMetadataPid': 'string',
                                                'TransportStreamId': 123,
                                                'VideoPid': 'string'
                                            }
                                        }
                                    },
                                    'NameModifier': 'string',
                                    'SegmentModifier': 'string'
                                },
                                'MsSmoothOutputSettings': {
                                    'NameModifier': 'string'
                                },
                                'RtmpOutputSettings': {
                                    'CertificateMode': 'SELF_SIGNED'|'VERIFY_AUTHENTICITY',
                                    'ConnectionRetryInterval': 123,
                                    'Destination': {
                                        'DestinationRefId': 'string'
                                    },
                                    'NumRetries': 123
                                },
                                'UdpOutputSettings': {
                                    'BufferMsec': 123,
                                    'ContainerSettings': {
                                        'M2tsSettings': {
                                            'AbsentInputAudioBehavior': 'DROP'|'ENCODE_SILENCE',
                                            'Arib': 'DISABLED'|'ENABLED',
                                            'AribCaptionsPid': 'string',
                                            'AribCaptionsPidControl': 'AUTO'|'USE_CONFIGURED',
                                            'AudioBufferModel': 'ATSC'|'DVB',
                                            'AudioFramesPerPes': 123,
                                            'AudioPids': 'string',
                                            'AudioStreamType': 'ATSC'|'DVB',
                                            'Bitrate': 123,
                                            'BufferModel': 'MULTIPLEX'|'NONE',
                                            'CcDescriptor': 'DISABLED'|'ENABLED',
                                            'DvbNitSettings': {
                                                'NetworkId': 123,
                                                'NetworkName': 'string',
                                                'RepInterval': 123
                                            },
                                            'DvbSdtSettings': {
                                                'OutputSdt': 'SDT_FOLLOW'|'SDT_FOLLOW_IF_PRESENT'|'SDT_MANUAL'|'SDT_NONE',
                                                'RepInterval': 123,
                                                'ServiceName': 'string',
                                                'ServiceProviderName': 'string'
                                            },
                                            'DvbSubPids': 'string',
                                            'DvbTdtSettings': {
                                                'RepInterval': 123
                                            },
                                            'DvbTeletextPid': 'string',
                                            'Ebif': 'NONE'|'PASSTHROUGH',
                                            'EbpAudioInterval': 'VIDEO_AND_FIXED_INTERVALS'|'VIDEO_INTERVAL',
                                            'EbpLookaheadMs': 123,
                                            'EbpPlacement': 'VIDEO_AND_AUDIO_PIDS'|'VIDEO_PID',
                                            'EcmPid': 'string',
                                            'EsRateInPes': 'EXCLUDE'|'INCLUDE',
                                            'EtvPlatformPid': 'string',
                                            'EtvSignalPid': 'string',
                                            'FragmentTime': 123.0,
                                            'Klv': 'NONE'|'PASSTHROUGH',
                                            'KlvDataPids': 'string',
                                            'NullPacketBitrate': 123.0,
                                            'PatInterval': 123,
                                            'PcrControl': 'CONFIGURED_PCR_PERIOD'|'PCR_EVERY_PES_PACKET',
                                            'PcrPeriod': 123,
                                            'PcrPid': 'string',
                                            'PmtInterval': 123,
                                            'PmtPid': 'string',
                                            'ProgramNum': 123,
                                            'RateMode': 'CBR'|'VBR',
                                            'Scte27Pids': 'string',
                                            'Scte35Control': 'NONE'|'PASSTHROUGH',
                                            'Scte35Pid': 'string',
                                            'SegmentationMarkers': 'EBP'|'EBP_LEGACY'|'NONE'|'PSI_SEGSTART'|'RAI_ADAPT'|'RAI_SEGSTART',
                                            'SegmentationStyle': 'MAINTAIN_CADENCE'|'RESET_CADENCE',
                                            'SegmentationTime': 123.0,
                                            'TimedMetadataBehavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                            'TimedMetadataPid': 'string',
                                            'TransportStreamId': 123,
                                            'VideoPid': 'string'
                                        }
                                    },
                                    'Destination': {
                                        'DestinationRefId': 'string'
                                    },
                                    'FecOutputSettings': {
                                        'ColumnDepth': 123,
                                        'IncludeFec': 'COLUMN'|'COLUMN_AND_ROW',
                                        'RowLength': 123
                                    }
                                }
                            },
                            'VideoDescriptionName': 'string'
                        },
                    ]
                },
            ],
            'TimecodeConfig': {
                'Source': 'EMBEDDED'|'SYSTEMCLOCK'|'ZEROBASED',
                'SyncThreshold': 123
            },
            'VideoDescriptions': [
                {
                    'CodecSettings': {
                        'H264Settings': {
                            'AdaptiveQuantization': 'HIGH'|'HIGHER'|'LOW'|'MAX'|'MEDIUM'|'OFF',
                            'AfdSignaling': 'AUTO'|'FIXED'|'NONE',
                            'Bitrate': 123,
                            'BufFillPct': 123,
                            'BufSize': 123,
                            'ColorMetadata': 'IGNORE'|'INSERT',
                            'EntropyEncoding': 'CABAC'|'CAVLC',
                            'FixedAfd': 'AFD_0000'|'AFD_0010'|'AFD_0011'|'AFD_0100'|'AFD_1000'|'AFD_1001'|'AFD_1010'|'AFD_1011'|'AFD_1101'|'AFD_1110'|'AFD_1111',
                            'FlickerAq': 'DISABLED'|'ENABLED',
                            'FramerateControl': 'INITIALIZE_FROM_SOURCE'|'SPECIFIED',
                            'FramerateDenominator': 123,
                            'FramerateNumerator': 123,
                            'GopBReference': 'DISABLED'|'ENABLED',
                            'GopClosedCadence': 123,
                            'GopNumBFrames': 123,
                            'GopSize': 123.0,
                            'GopSizeUnits': 'FRAMES'|'SECONDS',
                            'Level': 'H264_LEVEL_1'|'H264_LEVEL_1_1'|'H264_LEVEL_1_2'|'H264_LEVEL_1_3'|'H264_LEVEL_2'|'H264_LEVEL_2_1'|'H264_LEVEL_2_2'|'H264_LEVEL_3'|'H264_LEVEL_3_1'|'H264_LEVEL_3_2'|'H264_LEVEL_4'|'H264_LEVEL_4_1'|'H264_LEVEL_4_2'|'H264_LEVEL_5'|'H264_LEVEL_5_1'|'H264_LEVEL_5_2'|'H264_LEVEL_AUTO',
                            'LookAheadRateControl': 'HIGH'|'LOW'|'MEDIUM',
                            'MaxBitrate': 123,
                            'MinIInterval': 123,
                            'NumRefFrames': 123,
                            'ParControl': 'INITIALIZE_FROM_SOURCE'|'SPECIFIED',
                            'ParDenominator': 123,
                            'ParNumerator': 123,
                            'Profile': 'BASELINE'|'HIGH'|'HIGH_10BIT'|'HIGH_422'|'HIGH_422_10BIT'|'MAIN',
                            'QvbrQualityLevel': 123,
                            'RateControlMode': 'CBR'|'QVBR'|'VBR',
                            'ScanType': 'INTERLACED'|'PROGRESSIVE',
                            'SceneChangeDetect': 'DISABLED'|'ENABLED',
                            'Slices': 123,
                            'Softness': 123,
                            'SpatialAq': 'DISABLED'|'ENABLED',
                            'SubgopLength': 'DYNAMIC'|'FIXED',
                            'Syntax': 'DEFAULT'|'RP2027',
                            'TemporalAq': 'DISABLED'|'ENABLED',
                            'TimecodeInsertion': 'DISABLED'|'PIC_TIMING_SEI'
                        }
                    },
                    'Height': 123,
                    'Name': 'string',
                    'RespondToAfd': 'NONE'|'PASSTHROUGH'|'RESPOND',
                    'ScalingBehavior': 'DEFAULT'|'STRETCH_TO_OUTPUT',
                    'Sharpness': 123,
                    'Width': 123
                },
            ]
        },
        InputAttachments=[
            {
                'InputAttachmentName': 'string',
                'InputId': 'string',
                'InputSettings': {
                    'AudioSelectors': [
                        {
                            'Name': 'string',
                            'SelectorSettings': {
                                'AudioLanguageSelection': {
                                    'LanguageCode': 'string',
                                    'LanguageSelectionPolicy': 'LOOSE'|'STRICT'
                                },
                                'AudioPidSelection': {
                                    'Pid': 123
                                }
                            }
                        },
                    ],
                    'CaptionSelectors': [
                        {
                            'LanguageCode': 'string',
                            'Name': 'string',
                            'SelectorSettings': {
                                'AribSourceSettings': {}
                                ,
                                'DvbSubSourceSettings': {
                                    'Pid': 123
                                },
                                'EmbeddedSourceSettings': {
                                    'Convert608To708': 'DISABLED'|'UPCONVERT',
                                    'Scte20Detection': 'AUTO'|'OFF',
                                    'Source608ChannelNumber': 123,
                                    'Source608TrackNumber': 123
                                },
                                'Scte20SourceSettings': {
                                    'Convert608To708': 'DISABLED'|'UPCONVERT',
                                    'Source608ChannelNumber': 123
                                },
                                'Scte27SourceSettings': {
                                    'Pid': 123
                                },
                                'TeletextSourceSettings': {
                                    'PageNumber': 'string'
                                }
                            }
                        },
                    ],
                    'DeblockFilter': 'DISABLED'|'ENABLED',
                    'DenoiseFilter': 'DISABLED'|'ENABLED',
                    'FilterStrength': 123,
                    'InputFilter': 'AUTO'|'DISABLED'|'FORCED',
                    'NetworkInputSettings': {
                        'HlsInputSettings': {
                            'Bandwidth': 123,
                            'BufferSegments': 123,
                            'Retries': 123,
                            'RetryInterval': 123
                        },
                        'ServerValidation': 'CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME'|'CHECK_CRYPTOGRAPHY_ONLY'
                    },
                    'SourceEndBehavior': 'CONTINUE'|'LOOP',
                    'VideoSelector': {
                        'ColorSpace': 'FOLLOW'|'REC_601'|'REC_709',
                        'ColorSpaceUsage': 'FALLBACK'|'FORCE',
                        'SelectorSettings': {
                            'VideoSelectorPid': {
                                'Pid': 123
                            },
                            'VideoSelectorProgramId': {
                                'ProgramId': 123
                            }
                        }
                    }
                }
            },
        ],
        InputSpecification={
            'Codec': 'MPEG2'|'AVC'|'HEVC',
            'MaximumBitrate': 'MAX_10_MBPS'|'MAX_20_MBPS'|'MAX_50_MBPS',
            'Resolution': 'SD'|'HD'|'UHD'
        },
        LogLevel='ERROR'|'WARNING'|'INFO'|'DEBUG'|'DISABLED',
        Name='string',
        RequestId='string',
        Reserved='string',
        RoleArn='string'
    )
    
    
    :type Destinations: list
    :param Destinations: Placeholder documentation for __listOfOutputDestination
            (dict) -- Placeholder documentation for OutputDestination
            Id (string) -- User-specified id. This is used in an output group or an output.
            Settings (list) -- Destination settings for output; one for each redundant encoder.
            (dict) -- Placeholder documentation for OutputDestinationSettings
            PasswordParam (string) -- key used to extract the password from EC2 Parameter store
            StreamName (string) -- Stream name for RTMP destinations (URLs of type rtmp://)
            Url (string) -- A URL specifying a destination
            Username (string) -- username for destination
            
            

    :type EncoderSettings: dict
    :param EncoderSettings: Placeholder documentation for EncoderSettings
            AudioDescriptions (list) -- [REQUIRED] Placeholder documentation for __listOfAudioDescription
            (dict) -- Placeholder documentation for AudioDescription
            AudioNormalizationSettings (dict) -- Advanced audio normalization settings.
            Algorithm (string) -- Audio normalization algorithm to use. itu17701 conforms to the CALM Act specification, itu17702 conforms to the EBU R-128 specification.
            AlgorithmControl (string) -- When set to correctAudio the output audio is corrected using the chosen algorithm. If set to measureOnly, the audio will be measured but not adjusted.
            TargetLkfs (float) -- Target LKFS(loudness) to adjust volume to. If no value is entered, a default value will be used according to the chosen algorithm. The CALM Act (1770-1) recommends a target of -24 LKFS. The EBU R-128 specification (1770-2) recommends a target of -23 LKFS.
            AudioSelectorName (string) -- [REQUIRED] The name of the AudioSelector used as the source for this AudioDescription.
            AudioType (string) -- Applies only if audioTypeControl is useConfigured. The values for audioType are defined in ISO-IEC 13818-1.
            AudioTypeControl (string) -- Determines how audio type is determined. followInput: If the input contains an ISO 639 audioType, then that value is passed through to the output. If the input contains no ISO 639 audioType, the value in Audio Type is included in the output. useConfigured: The value in Audio Type is included in the output. Note that this field and audioType are both ignored if inputType is broadcasterMixedAd.
            CodecSettings (dict) -- Audio codec settings.
            AacSettings (dict) -- Placeholder documentation for AacSettings
            Bitrate (float) -- Average bitrate in bits/second. Valid values depend on rate control mode and profile.
            CodingMode (string) -- Mono, Stereo, or 5.1 channel layout. Valid values depend on rate control mode and profile. The adReceiverMix setting receives a stereo description plus control track and emits a mono AAC encode of the description track, with control data emitted in the PES header as per ETSI TS 101 154 Annex E.
            InputType (string) -- Set to 'broadcasterMixedAd' when input contains pre-mixed main audio + AD (narration) as a stereo pair. The Audio Type field (audioType) will be set to 3, which signals to downstream systems that this stream contains 'broadcaster mixed AD'. Note that the input received by the encoder must contain pre-mixed audio; the encoder does not perform the mixing. The values in audioTypeControl and audioType (in AudioDescription) are ignored when set to broadcasterMixedAd. Leave set to 'normal' when input does not contain pre-mixed audio + AD.
            Profile (string) -- AAC Profile.
            RateControlMode (string) -- Rate Control Mode.
            RawFormat (string) -- Sets LATM / LOAS AAC output for raw containers.
            SampleRate (float) -- Sample rate in Hz. Valid values depend on rate control mode and profile.
            Spec (string) -- Use MPEG-2 AAC audio instead of MPEG-4 AAC audio for raw or MPEG-2 Transport Stream containers.
            VbrQuality (string) -- VBR Quality Level - Only used if rateControlMode is VBR.
            Ac3Settings (dict) -- Placeholder documentation for Ac3Settings
            Bitrate (float) -- Average bitrate in bits/second. Valid bitrates depend on the coding mode.
            BitstreamMode (string) -- Specifies the bitstream mode (bsmod) for the emitted AC-3 stream. See ATSC A/52-2012 for background on these values.
            CodingMode (string) -- Dolby Digital coding mode. Determines number of channels.
            Dialnorm (integer) -- Sets the dialnorm for the output. If excluded and input audio is Dolby Digital, dialnorm will be passed through.
            DrcProfile (string) -- If set to filmStandard, adds dynamic range compression signaling to the output bitstream as defined in the Dolby Digital specification.
            LfeFilter (string) -- When set to enabled, applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid in codingMode32Lfe mode.
            MetadataControl (string) -- When set to 'followInput', encoder metadata will be sourced from the DD, DD+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used.
            Eac3Settings (dict) -- Placeholder documentation for Eac3Settings
            AttenuationControl (string) -- When set to attenuate3Db, applies a 3 dB attenuation to the surround channels. Only used for 3/2 coding mode.
            Bitrate (float) -- Average bitrate in bits/second. Valid bitrates depend on the coding mode.
            BitstreamMode (string) -- Specifies the bitstream mode (bsmod) for the emitted E-AC-3 stream. See ATSC A/52-2012 (Annex E) for background on these values.
            CodingMode (string) -- Dolby Digital Plus coding mode. Determines number of channels.
            DcFilter (string) -- When set to enabled, activates a DC highpass filter for all input channels.
            Dialnorm (integer) -- Sets the dialnorm for the output. If blank and input audio is Dolby Digital Plus, dialnorm will be passed through.
            DrcLine (string) -- Sets the Dolby dynamic range compression profile.
            DrcRf (string) -- Sets the profile for heavy Dolby dynamic range compression, ensures that the instantaneous signal peaks do not exceed specified levels.
            LfeControl (string) -- When encoding 3/2 audio, setting to lfe enables the LFE channel
            LfeFilter (string) -- When set to enabled, applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with codingMode32 coding mode.
            LoRoCenterMixLevel (float) -- Left only/Right only center mix level. Only used for 3/2 coding mode.
            LoRoSurroundMixLevel (float) -- Left only/Right only surround mix level. Only used for 3/2 coding mode.
            LtRtCenterMixLevel (float) -- Left total/Right total center mix level. Only used for 3/2 coding mode.
            LtRtSurroundMixLevel (float) -- Left total/Right total surround mix level. Only used for 3/2 coding mode.
            MetadataControl (string) -- When set to followInput, encoder metadata will be sourced from the DD, DD+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used.
            PassthroughControl (string) -- When set to whenPossible, input DD+ audio will be passed through if it is present on the input. This detection is dynamic over the life of the transcode. Inputs that alternate between DD+ and non-DD+ content will have a consistent DD+ output as the system alternates between passthrough and encoding.
            PhaseControl (string) -- When set to shift90Degrees, applies a 90-degree phase shift to the surround channels. Only used for 3/2 coding mode.
            StereoDownmix (string) -- Stereo downmix preference. Only used for 3/2 coding mode.
            SurroundExMode (string) -- When encoding 3/2 audio, sets whether an extra center back surround channel is matrix encoded into the left and right surround channels.
            SurroundMode (string) -- When encoding 2/0 audio, sets whether Dolby Surround is matrix encoded into the two channels.
            Mp2Settings (dict) -- Placeholder documentation for Mp2Settings
            Bitrate (float) -- Average bitrate in bits/second.
            CodingMode (string) -- The MPEG2 Audio coding mode. Valid values are codingMode10 (for mono) or codingMode20 (for stereo).
            SampleRate (float) -- Sample rate in Hz.
            PassThroughSettings (dict) -- Placeholder documentation for PassThroughSettings
            LanguageCode (string) -- Indicates the language of the audio output track. Only used if languageControlMode is useConfigured, or there is no ISO 639 language code specified in the input.
            LanguageCodeControl (string) -- Choosing followInput will cause the ISO 639 language code of the output to follow the ISO 639 language code of the input. The languageCode will be used when useConfigured is set, or when followInput is selected but there is no ISO 639 language code specified by the input.
            Name (string) -- [REQUIRED] The name of this AudioDescription. Outputs will use this name to uniquely identify this AudioDescription. Description names should be unique within this Live Event.
            RemixSettings (dict) -- Settings that control how input audio channels are remixed into the output audio channels.
            ChannelMappings (list) -- [REQUIRED] Mapping of input channels to output channels, with appropriate gain adjustments.
            (dict) -- Placeholder documentation for AudioChannelMapping
            InputChannelLevels (list) -- [REQUIRED] Indices and gain values for each input channel that should be remixed into this output channel.
            (dict) -- Placeholder documentation for InputChannelLevel
            Gain (integer) -- [REQUIRED] Remixing value. Units are in dB and acceptable values are within the range from -60 (mute) and 6 dB.
            InputChannel (integer) -- [REQUIRED] The index of the input channel used as a source.
            
            OutputChannel (integer) -- [REQUIRED] The index of the output channel being produced.
            
            ChannelsIn (integer) -- Number of input channels to be used.
            ChannelsOut (integer) -- Number of output channels to be produced. Valid values: 1, 2, 4, 6, 8
            StreamName (string) -- Used for MS Smooth and Apple HLS outputs. Indicates the name displayed by the player (eg. English, or Director Commentary).
            
            AvailBlanking (dict) -- Settings for ad avail blanking.
            AvailBlankingImage (dict) -- Blanking image to be used. Leave empty for solid black. Only bmp and png images are supported.
            PasswordParam (string) -- key used to extract the password from EC2 Parameter store
            Uri (string) -- [REQUIRED] Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: 'rtmp://fmsserver/live'.
            Username (string) -- Documentation update needed
            State (string) -- When set to enabled, causes video, audio and captions to be blanked when insertion metadata is added.
            AvailConfiguration (dict) -- Event-wide configuration settings for ad avail insertion.
            AvailSettings (dict) -- Ad avail settings.
            Scte35SpliceInsert (dict) -- Placeholder documentation for Scte35SpliceInsert
            AdAvailOffset (integer) -- When specified, this offset (in milliseconds) is added to the input Ad Avail PTS time. This only applies to embedded SCTE 104/35 messages and does not apply to OOB messages.
            NoRegionalBlackoutFlag (string) -- When set to ignore, Segment Descriptors with noRegionalBlackoutFlag set to 0 will no longer trigger blackouts or Ad Avail slates
            WebDeliveryAllowedFlag (string) -- When set to ignore, Segment Descriptors with webDeliveryAllowedFlag set to 0 will no longer trigger blackouts or Ad Avail slates
            Scte35TimeSignalApos (dict) -- Placeholder documentation for Scte35TimeSignalApos
            AdAvailOffset (integer) -- When specified, this offset (in milliseconds) is added to the input Ad Avail PTS time. This only applies to embedded SCTE 104/35 messages and does not apply to OOB messages.
            NoRegionalBlackoutFlag (string) -- When set to ignore, Segment Descriptors with noRegionalBlackoutFlag set to 0 will no longer trigger blackouts or Ad Avail slates
            WebDeliveryAllowedFlag (string) -- When set to ignore, Segment Descriptors with webDeliveryAllowedFlag set to 0 will no longer trigger blackouts or Ad Avail slates
            
            BlackoutSlate (dict) -- Settings for blackout slate.
            BlackoutSlateImage (dict) -- Blackout slate image to be used. Leave empty for solid black. Only bmp and png images are supported.
            PasswordParam (string) -- key used to extract the password from EC2 Parameter store
            Uri (string) -- [REQUIRED] Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: 'rtmp://fmsserver/live'.
            Username (string) -- Documentation update needed
            NetworkEndBlackout (string) -- Setting to enabled causes the encoder to blackout the video, audio, and captions, and raise the 'Network Blackout Image' slate when an SCTE104/35 Network End Segmentation Descriptor is encountered. The blackout will be lifted when the Network Start Segmentation Descriptor is encountered. The Network End and Network Start descriptors must contain a network ID that matches the value entered in 'Network ID'.
            NetworkEndBlackoutImage (dict) -- Path to local file to use as Network End Blackout image. Image will be scaled to fill the entire output raster.
            PasswordParam (string) -- key used to extract the password from EC2 Parameter store
            Uri (string) -- [REQUIRED] Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: 'rtmp://fmsserver/live'.
            Username (string) -- Documentation update needed
            NetworkId (string) -- Provides Network ID that matches EIDR ID format (e.g., '10.XXXX/XXXX-XXXX-XXXX-XXXX-XXXX-C').
            State (string) -- When set to enabled, causes video, audio and captions to be blanked when indicated by program metadata.
            CaptionDescriptions (list) -- Settings for caption decriptions
            (dict) -- Output groups for this Live Event. Output groups contain information about where streams should be distributed.
            CaptionSelectorName (string) -- [REQUIRED] Specifies which input caption selector to use as a caption source when generating output captions. This field should match a captionSelector name.
            DestinationSettings (dict) -- Additional settings for captions destination that depend on the destination type.
            AribDestinationSettings (dict) -- Placeholder documentation for AribDestinationSettings
            BurnInDestinationSettings (dict) -- Placeholder documentation for BurnInDestinationSettings
            Alignment (string) -- If no explicit xPosition or yPosition is provided, setting alignment to centered will place the captions at the bottom center of the output. Similarly, setting a left alignment will align captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. Selecting 'smart' justification will left-justify live subtitles and center-justify pre-recorded subtitles. All burn-in and DVB-Sub font settings must match.
            BackgroundColor (string) -- Specifies the color of the rectangle behind the captions. All burn-in and DVB-Sub font settings must match.
            BackgroundOpacity (integer) -- Specifies the opacity of the background rectangle. 255 is opaque; 0 is transparent. Leaving this parameter out is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
            Font (dict) -- External font file used for caption burn-in. File extension must be 'ttf' or 'tte'. Although the user can select output fonts for many different types of input captions, embedded, STL and teletext sources use a strict grid system. Using external fonts with these caption sources could cause unexpected display of proportional fonts. All burn-in and DVB-Sub font settings must match.
            PasswordParam (string) -- key used to extract the password from EC2 Parameter store
            Uri (string) -- [REQUIRED] Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: 'rtmp://fmsserver/live'.
            Username (string) -- Documentation update needed
            FontColor (string) -- Specifies the color of the burned-in captions. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
            FontOpacity (integer) -- Specifies the opacity of the burned-in captions. 255 is opaque; 0 is transparent. All burn-in and DVB-Sub font settings must match.
            FontResolution (integer) -- Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and DVB-Sub font settings must match.
            FontSize (string) -- When set to 'auto' fontSize will scale depending on the size of the output. Giving a positive integer will specify the exact font size in points. All burn-in and DVB-Sub font settings must match.
            OutlineColor (string) -- Specifies font outline color. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
            OutlineSize (integer) -- Specifies font outline size in pixels. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
            ShadowColor (string) -- Specifies the color of the shadow cast by the captions. All burn-in and DVB-Sub font settings must match.
            ShadowOpacity (integer) -- Specifies the opacity of the shadow. 255 is opaque; 0 is transparent. Leaving this parameter out is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
            ShadowXOffset (integer) -- Specifies the horizontal offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left. All burn-in and DVB-Sub font settings must match.
            ShadowYOffset (integer) -- Specifies the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. All burn-in and DVB-Sub font settings must match.
            TeletextGridControl (string) -- Controls whether a fixed grid size will be used to generate the output subtitles bitmap. Only applicable for Teletext inputs and DVB-Sub/Burn-in outputs.
            XPosition (integer) -- Specifies the horizontal position of the caption relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit xPosition is provided, the horizontal caption position will be determined by the alignment parameter. All burn-in and DVB-Sub font settings must match.
            YPosition (integer) -- Specifies the vertical position of the caption relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit yPosition is provided, the caption will be positioned towards the bottom of the output. All burn-in and DVB-Sub font settings must match.
            DvbSubDestinationSettings (dict) -- Placeholder documentation for DvbSubDestinationSettings
            Alignment (string) -- If no explicit xPosition or yPosition is provided, setting alignment to centered will place the captions at the bottom center of the output. Similarly, setting a left alignment will align captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. Selecting 'smart' justification will left-justify live subtitles and center-justify pre-recorded subtitles. This option is not valid for source captions that are STL or 608/embedded. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
            BackgroundColor (string) -- Specifies the color of the rectangle behind the captions. All burn-in and DVB-Sub font settings must match.
            BackgroundOpacity (integer) -- Specifies the opacity of the background rectangle. 255 is opaque; 0 is transparent. Leaving this parameter blank is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
            Font (dict) -- External font file used for caption burn-in. File extension must be 'ttf' or 'tte'. Although the user can select output fonts for many different types of input captions, embedded, STL and teletext sources use a strict grid system. Using external fonts with these caption sources could cause unexpected display of proportional fonts. All burn-in and DVB-Sub font settings must match.
            PasswordParam (string) -- key used to extract the password from EC2 Parameter store
            Uri (string) -- [REQUIRED] Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: 'rtmp://fmsserver/live'.
            Username (string) -- Documentation update needed
            FontColor (string) -- Specifies the color of the burned-in captions. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
            FontOpacity (integer) -- Specifies the opacity of the burned-in captions. 255 is opaque; 0 is transparent. All burn-in and DVB-Sub font settings must match.
            FontResolution (integer) -- Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and DVB-Sub font settings must match.
            FontSize (string) -- When set to auto fontSize will scale depending on the size of the output. Giving a positive integer will specify the exact font size in points. All burn-in and DVB-Sub font settings must match.
            OutlineColor (string) -- Specifies font outline color. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
            OutlineSize (integer) -- Specifies font outline size in pixels. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
            ShadowColor (string) -- Specifies the color of the shadow cast by the captions. All burn-in and DVB-Sub font settings must match.
            ShadowOpacity (integer) -- Specifies the opacity of the shadow. 255 is opaque; 0 is transparent. Leaving this parameter blank is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
            ShadowXOffset (integer) -- Specifies the horizontal offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left. All burn-in and DVB-Sub font settings must match.
            ShadowYOffset (integer) -- Specifies the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. All burn-in and DVB-Sub font settings must match.
            TeletextGridControl (string) -- Controls whether a fixed grid size will be used to generate the output subtitles bitmap. Only applicable for Teletext inputs and DVB-Sub/Burn-in outputs.
            XPosition (integer) -- Specifies the horizontal position of the caption relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit xPosition is provided, the horizontal caption position will be determined by the alignment parameter. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
            YPosition (integer) -- Specifies the vertical position of the caption relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit yPosition is provided, the caption will be positioned towards the bottom of the output. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
            EmbeddedDestinationSettings (dict) -- Placeholder documentation for EmbeddedDestinationSettings
            EmbeddedPlusScte20DestinationSettings (dict) -- Placeholder documentation for EmbeddedPlusScte20DestinationSettings
            RtmpCaptionInfoDestinationSettings (dict) -- Placeholder documentation for RtmpCaptionInfoDestinationSettings
            Scte20PlusEmbeddedDestinationSettings (dict) -- Placeholder documentation for Scte20PlusEmbeddedDestinationSettings
            Scte27DestinationSettings (dict) -- Placeholder documentation for Scte27DestinationSettings
            SmpteTtDestinationSettings (dict) -- Placeholder documentation for SmpteTtDestinationSettings
            TeletextDestinationSettings (dict) -- Placeholder documentation for TeletextDestinationSettings
            TtmlDestinationSettings (dict) -- Placeholder documentation for TtmlDestinationSettings
            StyleControl (string) -- When set to passthrough, passes through style and position information from a TTML-like input source (TTML, SMPTE-TT, CFF-TT) to the CFF-TT output or TTML output.
            WebvttDestinationSettings (dict) -- Placeholder documentation for WebvttDestinationSettings
            LanguageCode (string) -- ISO 639-2 three-digit code: http://www.loc.gov/standards/iso639-2/
            LanguageDescription (string) -- Human readable information to indicate captions available for players (eg. English, or Spanish).
            Name (string) -- [REQUIRED] Name of the caption description. Used to associate a caption description with an output. Names must be unique within an event.
            
            GlobalConfiguration (dict) -- Configuration settings that apply to the event as a whole.
            InitialAudioGain (integer) -- Value to set the initial audio gain for the Live Event.
            InputEndAction (string) -- Indicates the action to take when the current input completes (e.g. end-of-file). When switchAndLoopInputs is configured the encoder will restart at the beginning of the first input. When 'none' is configured the encoder will transcode either black, a solid color, or a user specified slate images per the 'Input Loss Behavior' configuration until the next input switch occurs (which is controlled through the Channel Schedule API).
            InputLossBehavior (dict) -- Settings for system actions when input is lost.
            BlackFrameMsec (integer) -- Documentation update needed
            InputLossImageColor (string) -- When input loss image type is 'color' this field specifies the color to use. Value: 6 hex characters representing the values of RGB.
            InputLossImageSlate (dict) -- When input loss image type is 'slate' these fields specify the parameters for accessing the slate.
            PasswordParam (string) -- key used to extract the password from EC2 Parameter store
            Uri (string) -- [REQUIRED] Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: 'rtmp://fmsserver/live'.
            Username (string) -- Documentation update needed
            InputLossImageType (string) -- Indicates whether to substitute a solid color or a slate into the output after input loss exceeds blackFrameMsec.
            RepeatFrameMsec (integer) -- Documentation update needed
            OutputTimingSource (string) -- Indicates whether the rate of frames emitted by the Live encoder should be paced by its system clock (which optionally may be locked to another source via NTP) or should be locked to the clock of the source that is providing the input stream.
            SupportLowFramerateInputs (string) -- Adjusts video input buffer for streams with very low video framerates. This is commonly set to enabled for music channels with less than one video frame per second.
            OutputGroups (list) -- [REQUIRED] Placeholder documentation for __listOfOutputGroup
            (dict) -- Output groups for this Live Event. Output groups contain information about where streams should be distributed.
            Name (string) -- Custom output group name optionally defined by the user. Only letters, numbers, and the underscore character allowed; only 32 characters allowed.
            OutputGroupSettings (dict) -- [REQUIRED] Settings associated with the output group.
            ArchiveGroupSettings (dict) -- Placeholder documentation for ArchiveGroupSettings
            Destination (dict) -- [REQUIRED] A directory and base filename where archive files should be written. If the base filename portion of the URI is left blank, the base filename of the first input will be automatically inserted.
            DestinationRefId (string) -- Placeholder documentation for __string
            RolloverInterval (integer) -- Number of seconds to write to archive file before closing and starting a new one.
            HlsGroupSettings (dict) -- Placeholder documentation for HlsGroupSettings
            AdMarkers (list) -- Choose one or more ad marker types to pass SCTE35 signals through to this group of Apple HLS outputs.
            (string) -- Placeholder documentation for HlsAdMarkers
            BaseUrlContent (string) -- A partial URI prefix that will be prepended to each output in the media .m3u8 file. Can be used if base manifest is delivered from a different URL than the main .m3u8 file.
            BaseUrlManifest (string) -- A partial URI prefix that will be prepended to each output in the media .m3u8 file. Can be used if base manifest is delivered from a different URL than the main .m3u8 file.
            CaptionLanguageMappings (list) -- Mapping of up to 4 caption channels to caption languages. Is only meaningful if captionLanguageSetting is set to 'insert'.
            (dict) -- Maps a caption channel to an ISO 693-2 language code (http://www.loc.gov/standards/iso639-2), with an optional description.
            CaptionChannel (integer) -- [REQUIRED] The closed caption channel being described by this CaptionLanguageMapping. Each channel mapping must have a unique channel number (maximum of 4)
            LanguageCode (string) -- [REQUIRED] Three character ISO 639-2 language code (see http://www.loc.gov/standards/iso639-2)
            LanguageDescription (string) -- [REQUIRED] Textual description of language
            
            CaptionLanguageSetting (string) -- Applies only to 608 Embedded output captions. insert: Include CLOSED-CAPTIONS lines in the manifest. Specify at least one language in the CC1 Language Code field. One CLOSED-CAPTION line is added for each Language Code you specify. Make sure to specify the languages in the order in which they appear in the original source (if the source is embedded format) or the order of the caption selectors (if the source is other than embedded). Otherwise, languages in the manifest will not match up properly with the output captions. none: Include CLOSED-CAPTIONS=NONE line in the manifest. omit: Omit any CLOSED-CAPTIONS line from the manifest.
            ClientCache (string) -- When set to 'disabled', sets the #EXT-X-ALLOW-CACHE:no tag in the manifest, which prevents clients from saving media segments for later replay.
            CodecSpecification (string) -- Specification to use (RFC-6381 or the default RFC-4281) during m3u8 playlist generation.
            ConstantIv (string) -- For use with encryptionType. This is a 128-bit, 16-byte hex value represented by a 32-character text string. If ivSource is set to 'explicit' then this parameter is required and is used as the IV for encryption.
            Destination (dict) -- [REQUIRED] A directory or HTTP destination for the HLS segments, manifest files, and encryption keys (if enabled).
            DestinationRefId (string) -- Placeholder documentation for __string
            DirectoryStructure (string) -- Place segments in subdirectories.
            EncryptionType (string) -- Encrypts the segments with the given encryption scheme. Exclude this parameter if no encryption is desired.
            HlsCdnSettings (dict) -- Parameters that control interactions with the CDN.
            HlsAkamaiSettings (dict) -- Placeholder documentation for HlsAkamaiSettings
            ConnectionRetryInterval (integer) -- Number of seconds to wait before retrying connection to the CDN if the connection is lost.
            FilecacheDuration (integer) -- Size in seconds of file cache for streaming outputs.
            HttpTransferMode (string) -- Specify whether or not to use chunked transfer encoding to Akamai. User should contact Akamai to enable this feature.
            NumRetries (integer) -- Number of retry attempts that will be made before the Live Event is put into an error state.
            RestartDelay (integer) -- If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart.
            Salt (string) -- Salt for authenticated Akamai.
            Token (string) -- Token parameter for authenticated akamai. If not specified, _gda_ is used.
            HlsBasicPutSettings (dict) -- Placeholder documentation for HlsBasicPutSettings
            ConnectionRetryInterval (integer) -- Number of seconds to wait before retrying connection to the CDN if the connection is lost.
            FilecacheDuration (integer) -- Size in seconds of file cache for streaming outputs.
            NumRetries (integer) -- Number of retry attempts that will be made before the Live Event is put into an error state.
            RestartDelay (integer) -- If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart.
            HlsMediaStoreSettings (dict) -- Placeholder documentation for HlsMediaStoreSettings
            ConnectionRetryInterval (integer) -- Number of seconds to wait before retrying connection to the CDN if the connection is lost.
            FilecacheDuration (integer) -- Size in seconds of file cache for streaming outputs.
            MediaStoreStorageClass (string) -- When set to temporal, output files are stored in non-persistent memory for faster reading and writing.
            NumRetries (integer) -- Number of retry attempts that will be made before the Live Event is put into an error state.
            RestartDelay (integer) -- If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart.
            HlsWebdavSettings (dict) -- Placeholder documentation for HlsWebdavSettings
            ConnectionRetryInterval (integer) -- Number of seconds to wait before retrying connection to the CDN if the connection is lost.
            FilecacheDuration (integer) -- Size in seconds of file cache for streaming outputs.
            HttpTransferMode (string) -- Specify whether or not to use chunked transfer encoding to WebDAV.
            NumRetries (integer) -- Number of retry attempts that will be made before the Live Event is put into an error state.
            RestartDelay (integer) -- If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart.
            
            IndexNSegments (integer) -- If mode is 'live', the number of segments to retain in the manifest (.m3u8) file. This number must be less than or equal to keepSegments. If mode is 'vod', this parameter has no effect.
            InputLossAction (string) -- Parameter that control output group behavior on input loss.
            IvInManifest (string) -- For use with encryptionType. The IV (Initialization Vector) is a 128-bit number used in conjunction with the key for encrypting blocks. If set to 'include', IV is listed in the manifest, otherwise the IV is not in the manifest.
            IvSource (string) -- For use with encryptionType. The IV (Initialization Vector) is a 128-bit number used in conjunction with the key for encrypting blocks. If this setting is 'followsSegmentNumber', it will cause the IV to change every segment (to match the segment number). If this is set to 'explicit', you must enter a constantIv value.
            KeepSegments (integer) -- If mode is 'live', the number of TS segments to retain in the destination directory. If mode is 'vod', this parameter has no effect.
            KeyFormat (string) -- The value specifies how the key is represented in the resource identified by the URI. If parameter is absent, an implicit value of 'identity' is used. A reverse DNS string can also be given.
            KeyFormatVersions (string) -- Either a single positive integer version value or a slash delimited list of version values (1/2/3).
            KeyProviderSettings (dict) -- The key provider settings.
            StaticKeySettings (dict) -- Placeholder documentation for StaticKeySettings
            KeyProviderServer (dict) -- The URL of the license server used for protecting content.
            PasswordParam (string) -- key used to extract the password from EC2 Parameter store
            Uri (string) -- [REQUIRED] Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: 'rtmp://fmsserver/live'.
            Username (string) -- Documentation update needed
            StaticKeyValue (string) -- [REQUIRED] Static key value as a 32 character hexadecimal string.
            
            ManifestCompression (string) -- When set to gzip, compresses HLS playlist.
            ManifestDurationFormat (string) -- Indicates whether the output manifest should use floating point or integer values for segment duration.
            MinSegmentLength (integer) -- When set, minimumSegmentLength is enforced by looking ahead and back within the specified range for a nearby avail and extending the segment size if needed.
            Mode (string) -- If 'vod', all segments are indexed and kept permanently in the destination and manifest. If 'live', only the number segments specified in keepSegments and indexNSegments are kept; newer segments replace older segments, which may prevent players from rewinding all the way to the beginning of the event. VOD mode uses HLS EXT-X-PLAYLIST-TYPE of EVENT while the channel is running, converting it to a 'VOD' type manifest on completion of the stream.
            OutputSelection (string) -- Generates the .m3u8 playlist file for this HLS output group. The segmentsOnly option will output segments without the .m3u8 file.
            ProgramDateTime (string) -- Includes or excludes EXT-X-PROGRAM-DATE-TIME tag in .m3u8 manifest files. The value is calculated as follows: either the program date and time are initialized using the input timecode source, or the time is initialized using the input timecode source and the date is initialized using the timestampOffset.
            ProgramDateTimePeriod (integer) -- Period of insertion of EXT-X-PROGRAM-DATE-TIME entry, in seconds.
            RedundantManifest (string) -- When set to 'enabled', includes the media playlists from both pipelines in the master manifest (.m3u8) file.
            SegmentLength (integer) -- Length of MPEG-2 Transport Stream segments to create (in seconds). Note that segments will end on the next keyframe after this number of seconds, so actual segment length may be longer.
            SegmentationMode (string) -- useInputSegmentation has been deprecated. The configured segment size is always used.
            SegmentsPerSubdirectory (integer) -- Number of segments to write to a subdirectory before starting a new one. directoryStructure must be subdirectoryPerStream for this setting to have an effect.
            StreamInfResolution (string) -- Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag of variant manifest.
            TimedMetadataId3Frame (string) -- Indicates ID3 frame that has the timecode.
            TimedMetadataId3Period (integer) -- Timed Metadata interval in seconds.
            TimestampDeltaMilliseconds (integer) -- Provides an extra millisecond delta offset to fine tune the timestamps.
            TsFileMode (string) -- When set to 'singleFile', emits the program as a single media resource (.ts) file, and uses #EXT-X-BYTERANGE tags to index segment for playback. Playback of VOD mode content during event is not guaranteed due to HTTP server caching.
            MsSmoothGroupSettings (dict) -- Placeholder documentation for MsSmoothGroupSettings
            AcquisitionPointId (string) -- The value of the 'Acquisition Point Identity' element used in each message placed in the sparse track. Only enabled if sparseTrackType is not 'none'.
            AudioOnlyTimecodeControl (string) -- If set to passthrough for an audio-only MS Smooth output, the fragment absolute time will be set to the current timecode. This option does not write timecodes to the audio elementary stream.
            CertificateMode (string) -- If set to verifyAuthenticity, verify the https certificate chain to a trusted Certificate Authority (CA). This will cause https outputs to self-signed certificates to fail.
            ConnectionRetryInterval (integer) -- Number of seconds to wait before retrying connection to the IIS server if the connection is lost. Content will be cached during this time and the cache will be be delivered to the IIS server once the connection is re-established.
            Destination (dict) -- [REQUIRED] Smooth Streaming publish point on an IIS server. Elemental Live acts as a 'Push' encoder to IIS.
            DestinationRefId (string) -- Placeholder documentation for __string
            EventId (string) -- MS Smooth event ID to be sent to the IIS server. Should only be specified if eventIdMode is set to useConfigured.
            EventIdMode (string) -- Specifies whether or not to send an event ID to the IIS server. If no event ID is sent and the same Live Event is used without changing the publishing point, clients might see cached video from the previous run. Options: - 'useConfigured' - use the value provided in eventId - 'useTimestamp' - generate and send an event ID based on the current timestamp - 'noEventId' - do not send an event ID to the IIS server.
            EventStopBehavior (string) -- When set to sendEos, send EOS signal to IIS server when stopping the event
            FilecacheDuration (integer) -- Size in seconds of file cache for streaming outputs.
            FragmentLength (integer) -- Length of mp4 fragments to generate (in seconds). Fragment length must be compatible with GOP size and framerate.
            InputLossAction (string) -- Parameter that control output group behavior on input loss.
            NumRetries (integer) -- Number of retry attempts.
            RestartDelay (integer) -- Number of seconds before initiating a restart due to output failure, due to exhausting the numRetries on one segment, or exceeding filecacheDuration.
            SegmentationMode (string) -- useInputSegmentation has been deprecated. The configured segment size is always used.
            SendDelayMs (integer) -- Number of milliseconds to delay the output from the second pipeline.
            SparseTrackType (string) -- If set to scte35, use incoming SCTE-35 messages to generate a sparse track in this group of MS-Smooth outputs.
            StreamManifestBehavior (string) -- When set to send, send stream manifest so publishing point doesn't start until all streams start.
            TimestampOffset (string) -- Timestamp offset for the event. Only used if timestampOffsetMode is set to useConfiguredOffset.
            TimestampOffsetMode (string) -- Type of timestamp date offset to use. - useEventStartDate: Use the date the event was started as the offset - useConfiguredOffset: Use an explicitly configured date as the offset
            RtmpGroupSettings (dict) -- Placeholder documentation for RtmpGroupSettings
            AuthenticationScheme (string) -- Authentication scheme to use when connecting with CDN
            CacheFullBehavior (string) -- Controls behavior when content cache fills up. If remote origin server stalls the RTMP connection and does not accept content fast enough the 'Media Cache' will fill up. When the cache reaches the duration specified by cacheLength the cache will stop accepting new content. If set to disconnectImmediately, the RTMP output will force a disconnect. Clear the media cache, and reconnect after restartDelay seconds. If set to waitForServer, the RTMP output will wait up to 5 minutes to allow the origin server to begin accepting data again.
            CacheLength (integer) -- Cache length, in seconds, is used to calculate buffer size.
            CaptionData (string) -- Controls the types of data that passes to onCaptionInfo outputs. If set to 'all' then 608 and 708 carried DTVCC data will be passed. If set to 'field1AndField2608' then DTVCC data will be stripped out, but 608 data from both fields will be passed. If set to 'field1608' then only the data carried in 608 from field 1 video will be passed.
            InputLossAction (string) -- Controls the behavior of this RTMP group if input becomes unavailable. - emitOutput: Emit a slate until input returns. - pauseOutput: Stop transmitting data until input returns. This does not close the underlying RTMP connection.
            RestartDelay (integer) -- If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart.
            UdpGroupSettings (dict) -- Placeholder documentation for UdpGroupSettings
            InputLossAction (string) -- Specifies behavior of last resort when input video is lost, and no more backup inputs are available. When dropTs is selected the entire transport stream will stop being emitted. When dropProgram is selected the program can be dropped from the transport stream (and replaced with null packets to meet the TS bitrate requirement). Or, when emitProgram is chosen the transport stream will continue to be produced normally with repeat frames, black frames, or slate frames substituted for the absent input video.
            TimedMetadataId3Frame (string) -- Indicates ID3 frame that has the timecode.
            TimedMetadataId3Period (integer) -- Timed Metadata interval in seconds.
            
            Outputs (list) -- [REQUIRED] Placeholder documentation for __listOfOutput
            (dict) -- Output settings. There can be multiple outputs within a group.
            AudioDescriptionNames (list) -- The names of the AudioDescriptions used as audio sources for this output.
            (string) -- Placeholder documentation for __string
            CaptionDescriptionNames (list) -- The names of the CaptionDescriptions used as caption sources for this output.
            (string) -- Placeholder documentation for __string
            OutputName (string) -- The name used to identify an output.
            OutputSettings (dict) -- [REQUIRED] Output type-specific settings.
            ArchiveOutputSettings (dict) -- Placeholder documentation for ArchiveOutputSettings
            ContainerSettings (dict) -- [REQUIRED] Settings specific to the container type of the file.
            M2tsSettings (dict) -- Placeholder documentation for M2tsSettings
            AbsentInputAudioBehavior (string) -- When set to drop, output audio streams will be removed from the program if the selected input audio stream is removed from the input. This allows the output audio configuration to dynamically change based on input configuration. If this is set to encodeSilence, all output audio streams will output encoded silence when not connected to an active input stream.
            Arib (string) -- When set to enabled, uses ARIB-compliant field muxing and removes video descriptor.
            AribCaptionsPid (string) -- Packet Identifier (PID) for ARIB Captions in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            AribCaptionsPidControl (string) -- If set to auto, pid number used for ARIB Captions will be auto-selected from unused pids. If set to useConfigured, ARIB Captions will be on the configured pid number.
            AudioBufferModel (string) -- When set to dvb, uses DVB buffer model for Dolby Digital audio. When set to atsc, the ATSC model is used.
            AudioFramesPerPes (integer) -- The number of audio frames to insert for each PES packet.
            AudioPids (string) -- Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
            AudioStreamType (string) -- When set to atsc, uses stream type = 0x81 for AC3 and stream type = 0x87 for EAC3. When set to dvb, uses stream type = 0x06.
            Bitrate (integer) -- The output bitrate of the transport stream in bits per second. Setting to 0 lets the muxer automatically determine the appropriate bitrate.
            BufferModel (string) -- If set to multiplex, use multiplex buffer model for accurate interleaving. Setting to bufferModel to none can lead to lower latency, but low-memory devices may not be able to play back the stream without interruptions.
            CcDescriptor (string) -- When set to enabled, generates captionServiceDescriptor in PMT.
            DvbNitSettings (dict) -- Inserts DVB Network Information Table (NIT) at the specified table repetition interval.
            NetworkId (integer) -- [REQUIRED] The numeric value placed in the Network Information Table (NIT).
            NetworkName (string) -- [REQUIRED] The network name text placed in the networkNameDescriptor inside the Network Information Table. Maximum length is 256 characters.
            RepInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream.
            DvbSdtSettings (dict) -- Inserts DVB Service Description Table (SDT) at the specified table repetition interval.
            OutputSdt (string) -- Selects method of inserting SDT information into output stream. The sdtFollow setting copies SDT information from input stream to output stream. The sdtFollowIfPresent setting copies SDT information from input stream to output stream if SDT information is present in the input, otherwise it will fall back on the user-defined values. The sdtManual setting means user will enter the SDT information. The sdtNone setting means output stream will not contain SDT information.
            RepInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream.
            ServiceName (string) -- The service name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters.
            ServiceProviderName (string) -- The service provider name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters.
            DvbSubPids (string) -- Packet Identifier (PID) for input source DVB Subtitle data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
            DvbTdtSettings (dict) -- Inserts DVB Time and Date Table (TDT) at the specified table repetition interval.
            RepInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream.
            DvbTeletextPid (string) -- Packet Identifier (PID) for input source DVB Teletext data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            Ebif (string) -- If set to passthrough, passes any EBIF data from the input source to this output.
            EbpAudioInterval (string) -- When videoAndFixedIntervals is selected, audio EBP markers will be added to partitions 3 and 4. The interval between these additional markers will be fixed, and will be slightly shorter than the video EBP marker interval. Only available when EBP Cablelabs segmentation markers are selected. Partitions 1 and 2 will always follow the video interval.
            EbpLookaheadMs (integer) -- When set, enforces that Encoder Boundary Points do not come within the specified time interval of each other by looking ahead at input video. If another EBP is going to come in within the specified time interval, the current EBP is not emitted, and the segment is 'stretched' to the next marker. The lookahead value does not add latency to the system. The Live Event must be configured elsewhere to create sufficient latency to make the lookahead accurate.
            EbpPlacement (string) -- Controls placement of EBP on Audio PIDs. If set to videoAndAudioPids, EBP markers will be placed on the video PID and all audio PIDs. If set to videoPid, EBP markers will be placed on only the video PID.
            EcmPid (string) -- This field is unused and deprecated.
            EsRateInPes (string) -- Include or exclude the ES Rate field in the PES header.
            EtvPlatformPid (string) -- Packet Identifier (PID) for input source ETV Platform data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            EtvSignalPid (string) -- Packet Identifier (PID) for input source ETV Signal data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            FragmentTime (float) -- The length in seconds of each fragment. Only used with EBP markers.
            Klv (string) -- If set to passthrough, passes any KLV data from the input source to this output.
            KlvDataPids (string) -- Packet Identifier (PID) for input source KLV data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
            NullPacketBitrate (float) -- Value in bits per second of extra null packets to insert into the transport stream. This can be used if a downstream encryption system requires periodic null packets.
            PatInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000.
            PcrControl (string) -- When set to pcrEveryPesPacket, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream.
            PcrPeriod (integer) -- Maximum time in milliseconds between Program Clock Reference (PCRs) inserted into the transport stream.
            PcrPid (string) -- Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            PmtInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000.
            PmtPid (string) -- Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            ProgramNum (integer) -- The value of the program number field in the Program Map Table.
            RateMode (string) -- When vbr, does not insert null packets into transport stream to fill specified bitrate. The bitrate setting acts as the maximum bitrate when vbr is set.
            Scte27Pids (string) -- Packet Identifier (PID) for input source SCTE-27 data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
            Scte35Control (string) -- Optionally pass SCTE-35 signals from the input source to this output.
            Scte35Pid (string) -- Packet Identifier (PID) of the SCTE-35 stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            SegmentationMarkers (string) -- Inserts segmentation markers at each segmentationTime period. raiSegstart sets the Random Access Indicator bit in the adaptation field. raiAdapt sets the RAI bit and adds the current timecode in the private data bytes. psiSegstart inserts PAT and PMT tables at the start of segments. ebp adds Encoder Boundary Point information to the adaptation field as per OpenCable specification OC-SP-EBP-I01-130118. ebpLegacy adds Encoder Boundary Point information to the adaptation field using a legacy proprietary format.
            SegmentationStyle (string) -- The segmentation style parameter controls how segmentation markers are inserted into the transport stream. With avails, it is possible that segments may be truncated, which can influence where future segmentation markers are inserted. When a segmentation style of 'resetCadence' is selected and a segment is truncated due to an avail, we will reset the segmentation cadence. This means the subsequent segment will have a duration of $segmentationTime seconds. When a segmentation style of 'maintainCadence' is selected and a segment is truncated due to an avail, we will not reset the segmentation cadence. This means the subsequent segment will likely be truncated as well. However, all segments after that will have a duration of $segmentationTime seconds. Note that EBP lookahead is a slight exception to this rule.
            SegmentationTime (float) -- The length in seconds of each segment. Required unless markers is set to None_.
            TimedMetadataBehavior (string) -- When set to passthrough, timed metadata will be passed through from input to output.
            TimedMetadataPid (string) -- Packet Identifier (PID) of the timed metadata stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            TransportStreamId (integer) -- The value of the transport stream ID field in the Program Map Table.
            VideoPid (string) -- Packet Identifier (PID) of the elementary video stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            
            Extension (string) -- Output file extension. If excluded, this will be auto-selected from the container type.
            NameModifier (string) -- String concatenated to the end of the destination filename. Required for multiple outputs of the same type.
            HlsOutputSettings (dict) -- Placeholder documentation for HlsOutputSettings
            HlsSettings (dict) -- [REQUIRED] Settings regarding the underlying stream. These settings are different for audio-only outputs.
            AudioOnlyHlsSettings (dict) -- Placeholder documentation for AudioOnlyHlsSettings
            AudioGroupId (string) -- Specifies the group to which the audio Rendition belongs.
            AudioOnlyImage (dict) -- For use with an audio only Stream. Must be a .jpg or .png file. If given, this image will be used as the cover-art for the audio only output. Ideally, it should be formatted for an iPhone screen for two reasons. The iPhone does not resize the image, it crops a centered image on the top/bottom and left/right. Additionally, this image file gets saved bit-for-bit into every 10-second segment file, so will increase bandwidth by {image file size} * {segment count} * {user count.}.
            PasswordParam (string) -- key used to extract the password from EC2 Parameter store
            Uri (string) -- [REQUIRED] Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: 'rtmp://fmsserver/live'.
            Username (string) -- Documentation update needed
            AudioTrackType (string) -- Four types of audio-only tracks are supported: Audio-Only Variant Stream The client can play back this audio-only stream instead of video in low-bandwidth scenarios. Represented as an EXT-X-STREAM-INF in the HLS manifest. Alternate Audio, Auto Select, Default Alternate rendition that the client should try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=YES, AUTOSELECT=YES Alternate Audio, Auto Select, Not Default Alternate rendition that the client may try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=YES Alternate Audio, not Auto Select Alternate rendition that the client will not try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=NO
            StandardHlsSettings (dict) -- Placeholder documentation for StandardHlsSettings
            AudioRenditionSets (string) -- List all the audio groups that are used with the video output stream. Input all the audio GROUP-IDs that are associated to the video, separate by ','.
            M3u8Settings (dict) -- [REQUIRED] Settings information for the .m3u8 container
            AudioFramesPerPes (integer) -- The number of audio frames to insert for each PES packet.
            AudioPids (string) -- Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values.
            EcmPid (string) -- This parameter is unused and deprecated.
            PatInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream. A value of '0' writes out the PMT once per segment file.
            PcrControl (string) -- When set to pcrEveryPesPacket, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream.
            PcrPeriod (integer) -- Maximum time in milliseconds between Program Clock References (PCRs) inserted into the transport stream.
            PcrPid (string) -- Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID. Can be entered as a decimal or hexadecimal value.
            PmtInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream. A value of '0' writes out the PMT once per segment file.
            PmtPid (string) -- Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream. Can be entered as a decimal or hexadecimal value.
            ProgramNum (integer) -- The value of the program number field in the Program Map Table.
            Scte35Behavior (string) -- If set to passthrough, passes any SCTE-35 signals from the input source to this output.
            Scte35Pid (string) -- Packet Identifier (PID) of the SCTE-35 stream in the transport stream. Can be entered as a decimal or hexadecimal value.
            TimedMetadataBehavior (string) -- When set to passthrough, timed metadata is passed through from input to output.
            TimedMetadataPid (string) -- Packet Identifier (PID) of the timed metadata stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            TransportStreamId (integer) -- The value of the transport stream ID field in the Program Map Table.
            VideoPid (string) -- Packet Identifier (PID) of the elementary video stream in the transport stream. Can be entered as a decimal or hexadecimal value.
            
            NameModifier (string) -- String concatenated to the end of the destination filename. Accepts 'Format Identifiers':#formatIdentifierParameters.
            SegmentModifier (string) -- String concatenated to end of segment filenames.
            MsSmoothOutputSettings (dict) -- Placeholder documentation for MsSmoothOutputSettings
            NameModifier (string) -- String concatenated to the end of the destination filename. Required for multiple outputs of the same type.
            RtmpOutputSettings (dict) -- Placeholder documentation for RtmpOutputSettings
            CertificateMode (string) -- If set to verifyAuthenticity, verify the tls certificate chain to a trusted Certificate Authority (CA). This will cause rtmps outputs with self-signed certificates to fail.
            ConnectionRetryInterval (integer) -- Number of seconds to wait before retrying a connection to the Flash Media server if the connection is lost.
            Destination (dict) -- [REQUIRED] The RTMP endpoint excluding the stream name (eg. rtmp://host/appname). For connection to Akamai, a username and password must be supplied. URI fields accept format identifiers.
            DestinationRefId (string) -- Placeholder documentation for __string
            NumRetries (integer) -- Number of retry attempts.
            UdpOutputSettings (dict) -- Placeholder documentation for UdpOutputSettings
            BufferMsec (integer) -- UDP output buffering in milliseconds. Larger values increase latency through the transcoder but simultaneously assist the transcoder in maintaining a constant, low-jitter UDP/RTP output while accommodating clock recovery, input switching, input disruptions, picture reordering, etc.
            ContainerSettings (dict) -- [REQUIRED] Placeholder documentation for UdpContainerSettings
            M2tsSettings (dict) -- Placeholder documentation for M2tsSettings
            AbsentInputAudioBehavior (string) -- When set to drop, output audio streams will be removed from the program if the selected input audio stream is removed from the input. This allows the output audio configuration to dynamically change based on input configuration. If this is set to encodeSilence, all output audio streams will output encoded silence when not connected to an active input stream.
            Arib (string) -- When set to enabled, uses ARIB-compliant field muxing and removes video descriptor.
            AribCaptionsPid (string) -- Packet Identifier (PID) for ARIB Captions in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            AribCaptionsPidControl (string) -- If set to auto, pid number used for ARIB Captions will be auto-selected from unused pids. If set to useConfigured, ARIB Captions will be on the configured pid number.
            AudioBufferModel (string) -- When set to dvb, uses DVB buffer model for Dolby Digital audio. When set to atsc, the ATSC model is used.
            AudioFramesPerPes (integer) -- The number of audio frames to insert for each PES packet.
            AudioPids (string) -- Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
            AudioStreamType (string) -- When set to atsc, uses stream type = 0x81 for AC3 and stream type = 0x87 for EAC3. When set to dvb, uses stream type = 0x06.
            Bitrate (integer) -- The output bitrate of the transport stream in bits per second. Setting to 0 lets the muxer automatically determine the appropriate bitrate.
            BufferModel (string) -- If set to multiplex, use multiplex buffer model for accurate interleaving. Setting to bufferModel to none can lead to lower latency, but low-memory devices may not be able to play back the stream without interruptions.
            CcDescriptor (string) -- When set to enabled, generates captionServiceDescriptor in PMT.
            DvbNitSettings (dict) -- Inserts DVB Network Information Table (NIT) at the specified table repetition interval.
            NetworkId (integer) -- [REQUIRED] The numeric value placed in the Network Information Table (NIT).
            NetworkName (string) -- [REQUIRED] The network name text placed in the networkNameDescriptor inside the Network Information Table. Maximum length is 256 characters.
            RepInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream.
            DvbSdtSettings (dict) -- Inserts DVB Service Description Table (SDT) at the specified table repetition interval.
            OutputSdt (string) -- Selects method of inserting SDT information into output stream. The sdtFollow setting copies SDT information from input stream to output stream. The sdtFollowIfPresent setting copies SDT information from input stream to output stream if SDT information is present in the input, otherwise it will fall back on the user-defined values. The sdtManual setting means user will enter the SDT information. The sdtNone setting means output stream will not contain SDT information.
            RepInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream.
            ServiceName (string) -- The service name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters.
            ServiceProviderName (string) -- The service provider name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters.
            DvbSubPids (string) -- Packet Identifier (PID) for input source DVB Subtitle data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
            DvbTdtSettings (dict) -- Inserts DVB Time and Date Table (TDT) at the specified table repetition interval.
            RepInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream.
            DvbTeletextPid (string) -- Packet Identifier (PID) for input source DVB Teletext data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            Ebif (string) -- If set to passthrough, passes any EBIF data from the input source to this output.
            EbpAudioInterval (string) -- When videoAndFixedIntervals is selected, audio EBP markers will be added to partitions 3 and 4. The interval between these additional markers will be fixed, and will be slightly shorter than the video EBP marker interval. Only available when EBP Cablelabs segmentation markers are selected. Partitions 1 and 2 will always follow the video interval.
            EbpLookaheadMs (integer) -- When set, enforces that Encoder Boundary Points do not come within the specified time interval of each other by looking ahead at input video. If another EBP is going to come in within the specified time interval, the current EBP is not emitted, and the segment is 'stretched' to the next marker. The lookahead value does not add latency to the system. The Live Event must be configured elsewhere to create sufficient latency to make the lookahead accurate.
            EbpPlacement (string) -- Controls placement of EBP on Audio PIDs. If set to videoAndAudioPids, EBP markers will be placed on the video PID and all audio PIDs. If set to videoPid, EBP markers will be placed on only the video PID.
            EcmPid (string) -- This field is unused and deprecated.
            EsRateInPes (string) -- Include or exclude the ES Rate field in the PES header.
            EtvPlatformPid (string) -- Packet Identifier (PID) for input source ETV Platform data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            EtvSignalPid (string) -- Packet Identifier (PID) for input source ETV Signal data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            FragmentTime (float) -- The length in seconds of each fragment. Only used with EBP markers.
            Klv (string) -- If set to passthrough, passes any KLV data from the input source to this output.
            KlvDataPids (string) -- Packet Identifier (PID) for input source KLV data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
            NullPacketBitrate (float) -- Value in bits per second of extra null packets to insert into the transport stream. This can be used if a downstream encryption system requires periodic null packets.
            PatInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000.
            PcrControl (string) -- When set to pcrEveryPesPacket, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream.
            PcrPeriod (integer) -- Maximum time in milliseconds between Program Clock Reference (PCRs) inserted into the transport stream.
            PcrPid (string) -- Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            PmtInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000.
            PmtPid (string) -- Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            ProgramNum (integer) -- The value of the program number field in the Program Map Table.
            RateMode (string) -- When vbr, does not insert null packets into transport stream to fill specified bitrate. The bitrate setting acts as the maximum bitrate when vbr is set.
            Scte27Pids (string) -- Packet Identifier (PID) for input source SCTE-27 data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
            Scte35Control (string) -- Optionally pass SCTE-35 signals from the input source to this output.
            Scte35Pid (string) -- Packet Identifier (PID) of the SCTE-35 stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            SegmentationMarkers (string) -- Inserts segmentation markers at each segmentationTime period. raiSegstart sets the Random Access Indicator bit in the adaptation field. raiAdapt sets the RAI bit and adds the current timecode in the private data bytes. psiSegstart inserts PAT and PMT tables at the start of segments. ebp adds Encoder Boundary Point information to the adaptation field as per OpenCable specification OC-SP-EBP-I01-130118. ebpLegacy adds Encoder Boundary Point information to the adaptation field using a legacy proprietary format.
            SegmentationStyle (string) -- The segmentation style parameter controls how segmentation markers are inserted into the transport stream. With avails, it is possible that segments may be truncated, which can influence where future segmentation markers are inserted. When a segmentation style of 'resetCadence' is selected and a segment is truncated due to an avail, we will reset the segmentation cadence. This means the subsequent segment will have a duration of $segmentationTime seconds. When a segmentation style of 'maintainCadence' is selected and a segment is truncated due to an avail, we will not reset the segmentation cadence. This means the subsequent segment will likely be truncated as well. However, all segments after that will have a duration of $segmentationTime seconds. Note that EBP lookahead is a slight exception to this rule.
            SegmentationTime (float) -- The length in seconds of each segment. Required unless markers is set to None_.
            TimedMetadataBehavior (string) -- When set to passthrough, timed metadata will be passed through from input to output.
            TimedMetadataPid (string) -- Packet Identifier (PID) of the timed metadata stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            TransportStreamId (integer) -- The value of the transport stream ID field in the Program Map Table.
            VideoPid (string) -- Packet Identifier (PID) of the elementary video stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            
            Destination (dict) -- [REQUIRED] Destination address and port number for RTP or UDP packets. Can be unicast or multicast RTP or UDP (eg. rtp://239.10.10.10:5001 or udp://10.100.100.100:5002).
            DestinationRefId (string) -- Placeholder documentation for __string
            FecOutputSettings (dict) -- Settings for enabling and adjusting Forward Error Correction on UDP outputs.
            ColumnDepth (integer) -- Parameter D from SMPTE 2022-1. The height of the FEC protection matrix. The number of transport stream packets per column error correction packet. Must be between 4 and 20, inclusive.
            IncludeFec (string) -- Enables column only or column and row based FEC
            RowLength (integer) -- Parameter L from SMPTE 2022-1. The width of the FEC protection matrix. Must be between 1 and 20, inclusive. If only Column FEC is used, then larger values increase robustness. If Row FEC is used, then this is the number of transport stream packets per row error correction packet, and the value must be between 4 and 20, inclusive, if includeFec is columnAndRow. If includeFec is column, this value must be 1 to 20, inclusive.
            
            VideoDescriptionName (string) -- The name of the VideoDescription used as the source for this output.
            
            
            TimecodeConfig (dict) -- [REQUIRED] Contains settings used to acquire and adjust timecode information from inputs.
            Source (string) -- [REQUIRED] Identifies the source for the timecode that will be associated with the events outputs. -Embedded (embedded): Initialize the output timecode with timecode from the the source. If no embedded timecode is detected in the source, the system falls back to using 'Start at 0' (zerobased). -System Clock (systemclock): Use the UTC time. -Start at 0 (zerobased): The time of the first frame of the event will be 00:00:00:00.
            SyncThreshold (integer) -- Threshold in frames beyond which output timecode is resynchronized to the input timecode. Discrepancies below this threshold are permitted to avoid unnecessary discontinuities in the output timecode. No timecode sync when this is not specified.
            VideoDescriptions (list) -- [REQUIRED] Placeholder documentation for __listOfVideoDescription
            (dict) -- Video settings for this stream.
            CodecSettings (dict) -- Video codec settings.
            H264Settings (dict) -- Placeholder documentation for H264Settings
            AdaptiveQuantization (string) -- Adaptive quantization. Allows intra-frame quantizers to vary to improve visual quality.
            AfdSignaling (string) -- Indicates that AFD values will be written into the output stream. If afdSignaling is 'auto', the system will try to preserve the input AFD value (in cases where multiple AFD values are valid). If set to 'fixed', the AFD value will be the value configured in the fixedAfd parameter.
            Bitrate (integer) -- Average bitrate in bits/second. Required when the rate control mode is VBR or CBR. Not used for QVBR. In an MS Smooth output group, each output must have a unique value when its bitrate is rounded down to the nearest multiple of 1000.
            BufFillPct (integer) -- Percentage of the buffer that should initially be filled (HRD buffer model).
            BufSize (integer) -- Size of buffer (HRD buffer model) in bits/second.
            ColorMetadata (string) -- Includes colorspace metadata in the output.
            EntropyEncoding (string) -- Entropy encoding mode. Use cabac (must be in Main or High profile) or cavlc.
            FixedAfd (string) -- Four bit AFD value to write on all frames of video in the output stream. Only valid when afdSignaling is set to 'Fixed'.
            FlickerAq (string) -- If set to enabled, adjust quantization within each frame to reduce flicker or 'pop' on I-frames.
            FramerateControl (string) -- This field indicates how the output video frame rate is specified. If 'specified' is selected then the output video frame rate is determined by framerateNumerator and framerateDenominator, else if 'initializeFromSource' is selected then the output video frame rate will be set equal to the input video frame rate of the first input.
            FramerateDenominator (integer) -- Framerate denominator.
            FramerateNumerator (integer) -- Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976 fps.
            GopBReference (string) -- Documentation update needed
            GopClosedCadence (integer) -- Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting.
            GopNumBFrames (integer) -- Number of B-frames between reference frames.
            GopSize (float) -- GOP size (keyframe interval) in units of either frames or seconds per gopSizeUnits. Must be greater than zero.
            GopSizeUnits (string) -- Indicates if the gopSize is specified in frames or seconds. If seconds the system will convert the gopSize into a frame count at run time.
            Level (string) -- H.264 Level.
            LookAheadRateControl (string) -- Amount of lookahead. A value of low can decrease latency and memory usage, while high can produce better quality for certain content.
            MaxBitrate (integer) -- For QVBR: See the tooltip for Quality level For VBR: Set the maximum bitrate in order to accommodate expected spikes in the complexity of the video.
            MinIInterval (integer) -- Only meaningful if sceneChangeDetect is set to enabled. Enforces separation between repeated (cadence) I-frames and I-frames inserted by Scene Change Detection. If a scene change I-frame is within I-interval frames of a cadence I-frame, the GOP is shrunk and/or stretched to the scene change I-frame. GOP stretch requires enabling lookahead as well as setting I-interval. The normal cadence resumes for the next GOP. Note: Maximum GOP stretch = GOP size + Min-I-interval - 1
            NumRefFrames (integer) -- Number of reference frames to use. The encoder may use more than requested if using B-frames and/or interlaced encoding.
            ParControl (string) -- This field indicates how the output pixel aspect ratio is specified. If 'specified' is selected then the output video pixel aspect ratio is determined by parNumerator and parDenominator, else if 'initializeFromSource' is selected then the output pixsel aspect ratio will be set equal to the input video pixel aspect ratio of the first input.
            ParDenominator (integer) -- Pixel Aspect Ratio denominator.
            ParNumerator (integer) -- Pixel Aspect Ratio numerator.
            Profile (string) -- H.264 Profile.
            QvbrQualityLevel (integer) -- Controls the target quality for the video encode. Applies only when the rate control mode is QVBR. Set values for the QVBR quality level field and Max bitrate field that suit your most important viewing devices. Recommended values are: - Primary screen: Quality level: 8 to 10. Max bitrate: 4M - PC or tablet: Quality level: 7. Max bitrate: 1.5M to 3M - Smartphone: Quality level: 6. Max bitrate: 1M to 1.5M
            RateControlMode (string) -- Rate control mode. QVBR: Quality will match the specified quality level except when it is constrained by the maximum bitrate. Recommended if you or your viewers pay for bandwidth. VBR: Quality and bitrate vary, depending on the video complexity. Recommended instead of QVBR if you want to maintain a specific average bitrate over the duration of the channel. CBR: Quality varies, depending on the video complexity. Recommended only if you distribute your assets to devices that cannot handle variable bitrates.
            ScanType (string) -- Sets the scan type of the output to progressive or top-field-first interlaced.
            SceneChangeDetect (string) -- Scene change detection. - On: inserts I-frames when scene change is detected. - Off: does not force an I-frame when scene change is detected.
            Slices (integer) -- Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures. This field is optional; when no value is specified the encoder will choose the number of slices based on encode resolution.
            Softness (integer) -- Softness. Selects quantizer matrix, larger values reduce high-frequency content in the encoded image.
            SpatialAq (string) -- If set to enabled, adjust quantization within each frame based on spatial variation of content complexity.
            SubgopLength (string) -- If set to fixed, use gopNumBFrames B-frames per sub-GOP. If set to dynamic, optimize the number of B-frames used for each sub-GOP to improve visual quality.
            Syntax (string) -- Produces a bitstream compliant with SMPTE RP-2027.
            TemporalAq (string) -- If set to enabled, adjust quantization within each frame based on temporal variation of content complexity.
            TimecodeInsertion (string) -- Determines how timecodes should be inserted into the video elementary stream. - 'disabled': Do not include timecodes - 'picTimingSei': Pass through picture timing SEI messages from the source specified in Timecode Config
            
            Height (integer) -- Output video height (in pixels). Leave blank to use source video height. If left blank, width must also be unspecified.
            Name (string) -- [REQUIRED] The name of this VideoDescription. Outputs will use this name to uniquely identify this Description. Description names should be unique within this Live Event.
            RespondToAfd (string) -- Indicates how to respond to the AFD values in the input stream. Setting to 'respond' causes input video to be clipped, depending on AFD value, input display aspect ratio and output display aspect ratio.
            ScalingBehavior (string) -- When set to 'stretchToOutput', automatically configures the output position to stretch the video to the specified output resolution. This option will override any position value.
            Sharpness (integer) -- Changes the width of the anti-alias filter kernel used for scaling. Only applies if scaling is being performed and antiAlias is set to true. 0 is the softest setting, 100 the sharpest, and 50 recommended for most content.
            Width (integer) -- Output video width (in pixels). Leave out to use source video width. If left out, height must also be left out. Display aspect ratio is always preserved by letterboxing or pillarboxing when necessary.
            
            

    :type InputAttachments: list
    :param InputAttachments: List of input attachments for channel.
            (dict) -- Placeholder documentation for InputAttachment
            InputAttachmentName (string) -- User-specified name for the attachment. This is required if the user wants to use this input in an input switch action.
            InputId (string) -- The ID of the input
            InputSettings (dict) -- Settings of an input (caption selector, etc.)
            AudioSelectors (list) -- Used to select the audio stream to decode for inputs that have multiple available.
            (dict) -- Placeholder documentation for AudioSelector
            Name (string) -- [REQUIRED] The name of this AudioSelector. AudioDescriptions will use this name to uniquely identify this Selector. Selector names should be unique per input.
            SelectorSettings (dict) -- The audio selector settings.
            AudioLanguageSelection (dict) -- Placeholder documentation for AudioLanguageSelection
            LanguageCode (string) -- [REQUIRED] Selects a specific three-letter language code from within an audio source.
            LanguageSelectionPolicy (string) -- When set to 'strict', the transport stream demux strictly identifies audio streams by their language descriptor. If a PMT update occurs such that an audio stream matching the initially selected language is no longer present then mute will be encoded until the language returns. If 'loose', then on a PMT update the demux will choose another audio stream in the program with the same stream type if it can't find one with the same language.
            AudioPidSelection (dict) -- Placeholder documentation for AudioPidSelection
            Pid (integer) -- [REQUIRED] Selects a specific PID from within a source.
            
            
            CaptionSelectors (list) -- Used to select the caption input to use for inputs that have multiple available.
            (dict) -- Output groups for this Live Event. Output groups contain information about where streams should be distributed.
            LanguageCode (string) -- When specified this field indicates the three letter language code of the caption track to extract from the source.
            Name (string) -- [REQUIRED] Name identifier for a caption selector. This name is used to associate this caption selector with one or more caption descriptions. Names must be unique within an event.
            SelectorSettings (dict) -- Caption selector settings.
            AribSourceSettings (dict) -- Placeholder documentation for AribSourceSettings
            DvbSubSourceSettings (dict) -- Placeholder documentation for DvbSubSourceSettings
            Pid (integer) -- When using DVB-Sub with Burn-In or SMPTE-TT, use this PID for the source content. Unused for DVB-Sub passthrough. All DVB-Sub content is passed through, regardless of selectors.
            EmbeddedSourceSettings (dict) -- Placeholder documentation for EmbeddedSourceSettings
            Convert608To708 (string) -- If upconvert, 608 data is both passed through via the '608 compatibility bytes' fields of the 708 wrapper as well as translated into 708. 708 data present in the source content will be discarded.
            Scte20Detection (string) -- Set to 'auto' to handle streams with intermittent and/or non-aligned SCTE-20 and Embedded captions.
            Source608ChannelNumber (integer) -- Specifies the 608/708 channel number within the video track from which to extract captions. Unused for passthrough.
            Source608TrackNumber (integer) -- This field is unused and deprecated.
            Scte20SourceSettings (dict) -- Placeholder documentation for Scte20SourceSettings
            Convert608To708 (string) -- If upconvert, 608 data is both passed through via the '608 compatibility bytes' fields of the 708 wrapper as well as translated into 708. 708 data present in the source content will be discarded.
            Source608ChannelNumber (integer) -- Specifies the 608/708 channel number within the video track from which to extract captions. Unused for passthrough.
            Scte27SourceSettings (dict) -- Placeholder documentation for Scte27SourceSettings
            Pid (integer) -- The pid field is used in conjunction with the caption selector languageCode field as follows: - Specify PID and Language: Extracts captions from that PID; the language is 'informational'. - Specify PID and omit Language: Extracts the specified PID. - Omit PID and specify Language: Extracts the specified language, whichever PID that happens to be. - Omit PID and omit Language: Valid only if source is DVB-Sub that is being passed through; all languages will be passed through.
            TeletextSourceSettings (dict) -- Placeholder documentation for TeletextSourceSettings
            PageNumber (string) -- Specifies the teletext page number within the data stream from which to extract captions. Range of 0x100 (256) to 0x8FF (2303). Unused for passthrough. Should be specified as a hexadecimal string with no '0x' prefix.
            
            
            DeblockFilter (string) -- Enable or disable the deblock filter when filtering.
            DenoiseFilter (string) -- Enable or disable the denoise filter when filtering.
            FilterStrength (integer) -- Adjusts the magnitude of filtering from 1 (minimal) to 5 (strongest).
            InputFilter (string) -- Turns on the filter for this input. MPEG-2 inputs have the deblocking filter enabled by default. 1) auto - filtering will be applied depending on input type/quality 2) disabled - no filtering will be applied to the input 3) forced - filtering will be applied regardless of input type
            NetworkInputSettings (dict) -- Input settings.
            HlsInputSettings (dict) -- Specifies HLS input settings when the uri is for a HLS manifest.
            Bandwidth (integer) -- When specified the HLS stream with the m3u8 BANDWIDTH that most closely matches this value will be chosen, otherwise the highest bandwidth stream in the m3u8 will be chosen. The bitrate is specified in bits per second, as in an HLS manifest.
            BufferSegments (integer) -- When specified, reading of the HLS input will begin this many buffer segments from the end (most recently written segment). When not specified, the HLS input will begin with the first segment specified in the m3u8.
            Retries (integer) -- The number of consecutive times that attempts to read a manifest or segment must fail before the input is considered unavailable.
            RetryInterval (integer) -- The number of seconds between retries when an attempt to read a manifest or segment fails.
            ServerValidation (string) -- Check HTTPS server certificates. When set to checkCryptographyOnly, cryptography in the certificate will be checked, but not the server's name. Certain subdomains (notably S3 buckets that use dots in the bucket name) do not strictly match the corresponding certificate's wildcard pattern and would otherwise cause the event to error. This setting is ignored for protocols that do not use https.
            SourceEndBehavior (string) -- Loop input if it is a file. This allows a file input to be streamed indefinitely.
            VideoSelector (dict) -- Informs which video elementary stream to decode for input types that have multiple available.
            ColorSpace (string) -- Specifies the colorspace of an input. This setting works in tandem with colorSpaceConversion to determine if any conversion will be performed.
            ColorSpaceUsage (string) -- Applies only if colorSpace is a value other than follow. This field controls how the value in the colorSpace field will be used. fallback means that when the input does include color space data, that data will be used, but when the input has no color space data, the value in colorSpace will be used. Choose fallback if your input is sometimes missing color space data, but when it does have color space data, that data is correct. force means to always use the value in colorSpace. Choose force if your input usually has no color space data or might have unreliable color space data.
            SelectorSettings (dict) -- The video selector settings.
            VideoSelectorPid (dict) -- Placeholder documentation for VideoSelectorPid
            Pid (integer) -- Selects a specific PID from within a video source.
            VideoSelectorProgramId (dict) -- Placeholder documentation for VideoSelectorProgramId
            ProgramId (integer) -- Selects a specific program from within a multi-program transport stream. If the program doesn't exist, the first program within the transport stream will be selected by default.
            
            
            

    :type InputSpecification: dict
    :param InputSpecification: Specification of input for this channel (max. bitrate, resolution, codec, etc.)
            Codec (string) -- Input codec
            MaximumBitrate (string) -- Maximum input bitrate, categorized coarsely
            Resolution (string) -- Input resolution, categorized coarsely
            

    :type LogLevel: string
    :param LogLevel: The log level to write to CloudWatch Logs.

    :type Name: string
    :param Name: Name of channel.

    :type RequestId: string
    :param RequestId: Unique request ID to be specified. This is needed to prevent retries from creating multiple resources. This field is autopopulated if not provided.

    :type Reserved: string
    :param Reserved: Deprecated field that's only usable by whitelisted customers.

    :type RoleArn: string
    :param RoleArn: An optional Amazon Resource Name (ARN) of the role to assume when running the Channel.

    :rtype: dict
    :return: {
        'Channel': {
            'Arn': 'string',
            'Destinations': [
                {
                    'Id': 'string',
                    'Settings': [
                        {
                            'PasswordParam': 'string',
                            'StreamName': 'string',
                            'Url': 'string',
                            'Username': 'string'
                        },
                    ]
                },
            ],
            'EgressEndpoints': [
                {
                    'SourceIp': 'string'
                },
            ],
            'EncoderSettings': {
                'AudioDescriptions': [
                    {
                        'AudioNormalizationSettings': {
                            'Algorithm': 'ITU_1770_1'|'ITU_1770_2',
                            'AlgorithmControl': 'CORRECT_AUDIO',
                            'TargetLkfs': 123.0
                        },
                        'AudioSelectorName': 'string',
                        'AudioType': 'CLEAN_EFFECTS'|'HEARING_IMPAIRED'|'UNDEFINED'|'VISUAL_IMPAIRED_COMMENTARY',
                        'AudioTypeControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                        'CodecSettings': {
                            'AacSettings': {
                                'Bitrate': 123.0,
                                'CodingMode': 'AD_RECEIVER_MIX'|'CODING_MODE_1_0'|'CODING_MODE_1_1'|'CODING_MODE_2_0'|'CODING_MODE_5_1',
                                'InputType': 'BROADCASTER_MIXED_AD'|'NORMAL',
                                'Profile': 'HEV1'|'HEV2'|'LC',
                                'RateControlMode': 'CBR'|'VBR',
                                'RawFormat': 'LATM_LOAS'|'NONE',
                                'SampleRate': 123.0,
                                'Spec': 'MPEG2'|'MPEG4',
                                'VbrQuality': 'HIGH'|'LOW'|'MEDIUM_HIGH'|'MEDIUM_LOW'
                            },
                            'Ac3Settings': {
                                'Bitrate': 123.0,
                                'BitstreamMode': 'COMMENTARY'|'COMPLETE_MAIN'|'DIALOGUE'|'EMERGENCY'|'HEARING_IMPAIRED'|'MUSIC_AND_EFFECTS'|'VISUALLY_IMPAIRED'|'VOICE_OVER',
                                'CodingMode': 'CODING_MODE_1_0'|'CODING_MODE_1_1'|'CODING_MODE_2_0'|'CODING_MODE_3_2_LFE',
                                'Dialnorm': 123,
                                'DrcProfile': 'FILM_STANDARD'|'NONE',
                                'LfeFilter': 'DISABLED'|'ENABLED',
                                'MetadataControl': 'FOLLOW_INPUT'|'USE_CONFIGURED'
                            },
                            'Eac3Settings': {
                                'AttenuationControl': 'ATTENUATE_3_DB'|'NONE',
                                'Bitrate': 123.0,
                                'BitstreamMode': 'COMMENTARY'|'COMPLETE_MAIN'|'EMERGENCY'|'HEARING_IMPAIRED'|'VISUALLY_IMPAIRED',
                                'CodingMode': 'CODING_MODE_1_0'|'CODING_MODE_2_0'|'CODING_MODE_3_2',
                                'DcFilter': 'DISABLED'|'ENABLED',
                                'Dialnorm': 123,
                                'DrcLine': 'FILM_LIGHT'|'FILM_STANDARD'|'MUSIC_LIGHT'|'MUSIC_STANDARD'|'NONE'|'SPEECH',
                                'DrcRf': 'FILM_LIGHT'|'FILM_STANDARD'|'MUSIC_LIGHT'|'MUSIC_STANDARD'|'NONE'|'SPEECH',
                                'LfeControl': 'LFE'|'NO_LFE',
                                'LfeFilter': 'DISABLED'|'ENABLED',
                                'LoRoCenterMixLevel': 123.0,
                                'LoRoSurroundMixLevel': 123.0,
                                'LtRtCenterMixLevel': 123.0,
                                'LtRtSurroundMixLevel': 123.0,
                                'MetadataControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                                'PassthroughControl': 'NO_PASSTHROUGH'|'WHEN_POSSIBLE',
                                'PhaseControl': 'NO_SHIFT'|'SHIFT_90_DEGREES',
                                'StereoDownmix': 'DPL2'|'LO_RO'|'LT_RT'|'NOT_INDICATED',
                                'SurroundExMode': 'DISABLED'|'ENABLED'|'NOT_INDICATED',
                                'SurroundMode': 'DISABLED'|'ENABLED'|'NOT_INDICATED'
                            },
                            'Mp2Settings': {
                                'Bitrate': 123.0,
                                'CodingMode': 'CODING_MODE_1_0'|'CODING_MODE_2_0',
                                'SampleRate': 123.0
                            },
                            'PassThroughSettings': {}
                        },
                        'LanguageCode': 'string',
                        'LanguageCodeControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                        'Name': 'string',
                        'RemixSettings': {
                            'ChannelMappings': [
                                {
                                    'InputChannelLevels': [
                                        {
                                            'Gain': 123,
                                            'InputChannel': 123
                                        },
                                    ],
                                    'OutputChannel': 123
                                },
                            ],
                            'ChannelsIn': 123,
                            'ChannelsOut': 123
                        },
                        'StreamName': 'string'
                    },
                ],
                'AvailBlanking': {
                    'AvailBlankingImage': {
                        'PasswordParam': 'string',
                        'Uri': 'string',
                        'Username': 'string'
                    },
                    'State': 'DISABLED'|'ENABLED'
                },
                'AvailConfiguration': {
                    'AvailSettings': {
                        'Scte35SpliceInsert': {
                            'AdAvailOffset': 123,
                            'NoRegionalBlackoutFlag': 'FOLLOW'|'IGNORE',
                            'WebDeliveryAllowedFlag': 'FOLLOW'|'IGNORE'
                        },
                        'Scte35TimeSignalApos': {
                            'AdAvailOffset': 123,
                            'NoRegionalBlackoutFlag': 'FOLLOW'|'IGNORE',
                            'WebDeliveryAllowedFlag': 'FOLLOW'|'IGNORE'
                        }
                    }
                },
                'BlackoutSlate': {
                    'BlackoutSlateImage': {
                        'PasswordParam': 'string',
                        'Uri': 'string',
                        'Username': 'string'
                    },
                    'NetworkEndBlackout': 'DISABLED'|'ENABLED',
                    'NetworkEndBlackoutImage': {
                        'PasswordParam': 'string',
                        'Uri': 'string',
                        'Username': 'string'
                    },
                    'NetworkId': 'string',
                    'State': 'DISABLED'|'ENABLED'
                },
                'CaptionDescriptions': [
                    {
                        'CaptionSelectorName': 'string',
                        'DestinationSettings': {
                            'AribDestinationSettings': {},
                            'BurnInDestinationSettings': {
                                'Alignment': 'CENTERED'|'LEFT'|'SMART',
                                'BackgroundColor': 'BLACK'|'NONE'|'WHITE',
                                'BackgroundOpacity': 123,
                                'Font': {
                                    'PasswordParam': 'string',
                                    'Uri': 'string',
                                    'Username': 'string'
                                },
                                'FontColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                                'FontOpacity': 123,
                                'FontResolution': 123,
                                'FontSize': 'string',
                                'OutlineColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                                'OutlineSize': 123,
                                'ShadowColor': 'BLACK'|'NONE'|'WHITE',
                                'ShadowOpacity': 123,
                                'ShadowXOffset': 123,
                                'ShadowYOffset': 123,
                                'TeletextGridControl': 'FIXED'|'SCALED',
                                'XPosition': 123,
                                'YPosition': 123
                            },
                            'DvbSubDestinationSettings': {
                                'Alignment': 'CENTERED'|'LEFT'|'SMART',
                                'BackgroundColor': 'BLACK'|'NONE'|'WHITE',
                                'BackgroundOpacity': 123,
                                'Font': {
                                    'PasswordParam': 'string',
                                    'Uri': 'string',
                                    'Username': 'string'
                                },
                                'FontColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                                'FontOpacity': 123,
                                'FontResolution': 123,
                                'FontSize': 'string',
                                'OutlineColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                                'OutlineSize': 123,
                                'ShadowColor': 'BLACK'|'NONE'|'WHITE',
                                'ShadowOpacity': 123,
                                'ShadowXOffset': 123,
                                'ShadowYOffset': 123,
                                'TeletextGridControl': 'FIXED'|'SCALED',
                                'XPosition': 123,
                                'YPosition': 123
                            },
                            'EmbeddedDestinationSettings': {},
                            'EmbeddedPlusScte20DestinationSettings': {},
                            'RtmpCaptionInfoDestinationSettings': {},
                            'Scte20PlusEmbeddedDestinationSettings': {},
                            'Scte27DestinationSettings': {},
                            'SmpteTtDestinationSettings': {},
                            'TeletextDestinationSettings': {},
                            'TtmlDestinationSettings': {
                                'StyleControl': 'PASSTHROUGH'|'USE_CONFIGURED'
                            },
                            'WebvttDestinationSettings': {}
                        },
                        'LanguageCode': 'string',
                        'LanguageDescription': 'string',
                        'Name': 'string'
                    },
                ],
                'GlobalConfiguration': {
                    'InitialAudioGain': 123,
                    'InputEndAction': 'NONE'|'SWITCH_AND_LOOP_INPUTS',
                    'InputLossBehavior': {
                        'BlackFrameMsec': 123,
                        'InputLossImageColor': 'string',
                        'InputLossImageSlate': {
                            'PasswordParam': 'string',
                            'Uri': 'string',
                            'Username': 'string'
                        },
                        'InputLossImageType': 'COLOR'|'SLATE',
                        'RepeatFrameMsec': 123
                    },
                    'OutputTimingSource': 'INPUT_CLOCK'|'SYSTEM_CLOCK',
                    'SupportLowFramerateInputs': 'DISABLED'|'ENABLED'
                },
                'OutputGroups': [
                    {
                        'Name': 'string',
                        'OutputGroupSettings': {
                            'ArchiveGroupSettings': {
                                'Destination': {
                                    'DestinationRefId': 'string'
                                },
                                'RolloverInterval': 123
                            },
                            'HlsGroupSettings': {
                                'AdMarkers': [
                                    'ADOBE'|'ELEMENTAL'|'ELEMENTAL_SCTE35',
                                ],
                                'BaseUrlContent': 'string',
                                'BaseUrlManifest': 'string',
                                'CaptionLanguageMappings': [
                                    {
                                        'CaptionChannel': 123,
                                        'LanguageCode': 'string',
                                        'LanguageDescription': 'string'
                                    },
                                ],
                                'CaptionLanguageSetting': 'INSERT'|'NONE'|'OMIT',
                                'ClientCache': 'DISABLED'|'ENABLED',
                                'CodecSpecification': 'RFC_4281'|'RFC_6381',
                                'ConstantIv': 'string',
                                'Destination': {
                                    'DestinationRefId': 'string'
                                },
                                'DirectoryStructure': 'SINGLE_DIRECTORY'|'SUBDIRECTORY_PER_STREAM',
                                'EncryptionType': 'AES128'|'SAMPLE_AES',
                                'HlsCdnSettings': {
                                    'HlsAkamaiSettings': {
                                        'ConnectionRetryInterval': 123,
                                        'FilecacheDuration': 123,
                                        'HttpTransferMode': 'CHUNKED'|'NON_CHUNKED',
                                        'NumRetries': 123,
                                        'RestartDelay': 123,
                                        'Salt': 'string',
                                        'Token': 'string'
                                    },
                                    'HlsBasicPutSettings': {
                                        'ConnectionRetryInterval': 123,
                                        'FilecacheDuration': 123,
                                        'NumRetries': 123,
                                        'RestartDelay': 123
                                    },
                                    'HlsMediaStoreSettings': {
                                        'ConnectionRetryInterval': 123,
                                        'FilecacheDuration': 123,
                                        'MediaStoreStorageClass': 'TEMPORAL',
                                        'NumRetries': 123,
                                        'RestartDelay': 123
                                    },
                                    'HlsWebdavSettings': {
                                        'ConnectionRetryInterval': 123,
                                        'FilecacheDuration': 123,
                                        'HttpTransferMode': 'CHUNKED'|'NON_CHUNKED',
                                        'NumRetries': 123,
                                        'RestartDelay': 123
                                    }
                                },
                                'IndexNSegments': 123,
                                'InputLossAction': 'EMIT_OUTPUT'|'PAUSE_OUTPUT',
                                'IvInManifest': 'EXCLUDE'|'INCLUDE',
                                'IvSource': 'EXPLICIT'|'FOLLOWS_SEGMENT_NUMBER',
                                'KeepSegments': 123,
                                'KeyFormat': 'string',
                                'KeyFormatVersions': 'string',
                                'KeyProviderSettings': {
                                    'StaticKeySettings': {
                                        'KeyProviderServer': {
                                            'PasswordParam': 'string',
                                            'Uri': 'string',
                                            'Username': 'string'
                                        },
                                        'StaticKeyValue': 'string'
                                    }
                                },
                                'ManifestCompression': 'GZIP'|'NONE',
                                'ManifestDurationFormat': 'FLOATING_POINT'|'INTEGER',
                                'MinSegmentLength': 123,
                                'Mode': 'LIVE'|'VOD',
                                'OutputSelection': 'MANIFESTS_AND_SEGMENTS'|'SEGMENTS_ONLY',
                                'ProgramDateTime': 'EXCLUDE'|'INCLUDE',
                                'ProgramDateTimePeriod': 123,
                                'RedundantManifest': 'DISABLED'|'ENABLED',
                                'SegmentLength': 123,
                                'SegmentationMode': 'USE_INPUT_SEGMENTATION'|'USE_SEGMENT_DURATION',
                                'SegmentsPerSubdirectory': 123,
                                'StreamInfResolution': 'EXCLUDE'|'INCLUDE',
                                'TimedMetadataId3Frame': 'NONE'|'PRIV'|'TDRL',
                                'TimedMetadataId3Period': 123,
                                'TimestampDeltaMilliseconds': 123,
                                'TsFileMode': 'SEGMENTED_FILES'|'SINGLE_FILE'
                            },
                            'MsSmoothGroupSettings': {
                                'AcquisitionPointId': 'string',
                                'AudioOnlyTimecodeControl': 'PASSTHROUGH'|'USE_CONFIGURED_CLOCK',
                                'CertificateMode': 'SELF_SIGNED'|'VERIFY_AUTHENTICITY',
                                'ConnectionRetryInterval': 123,
                                'Destination': {
                                    'DestinationRefId': 'string'
                                },
                                'EventId': 'string',
                                'EventIdMode': 'NO_EVENT_ID'|'USE_CONFIGURED'|'USE_TIMESTAMP',
                                'EventStopBehavior': 'NONE'|'SEND_EOS',
                                'FilecacheDuration': 123,
                                'FragmentLength': 123,
                                'InputLossAction': 'EMIT_OUTPUT'|'PAUSE_OUTPUT',
                                'NumRetries': 123,
                                'RestartDelay': 123,
                                'SegmentationMode': 'USE_INPUT_SEGMENTATION'|'USE_SEGMENT_DURATION',
                                'SendDelayMs': 123,
                                'SparseTrackType': 'NONE'|'SCTE_35',
                                'StreamManifestBehavior': 'DO_NOT_SEND'|'SEND',
                                'TimestampOffset': 'string',
                                'TimestampOffsetMode': 'USE_CONFIGURED_OFFSET'|'USE_EVENT_START_DATE'
                            },
                            'RtmpGroupSettings': {
                                'AuthenticationScheme': 'AKAMAI'|'COMMON',
                                'CacheFullBehavior': 'DISCONNECT_IMMEDIATELY'|'WAIT_FOR_SERVER',
                                'CacheLength': 123,
                                'CaptionData': 'ALL'|'FIELD1_608'|'FIELD1_AND_FIELD2_608',
                                'InputLossAction': 'EMIT_OUTPUT'|'PAUSE_OUTPUT',
                                'RestartDelay': 123
                            },
                            'UdpGroupSettings': {
                                'InputLossAction': 'DROP_PROGRAM'|'DROP_TS'|'EMIT_PROGRAM',
                                'TimedMetadataId3Frame': 'NONE'|'PRIV'|'TDRL',
                                'TimedMetadataId3Period': 123
                            }
                        },
                        'Outputs': [
                            {
                                'AudioDescriptionNames': [
                                    'string',
                                ],
                                'CaptionDescriptionNames': [
                                    'string',
                                ],
                                'OutputName': 'string',
                                'OutputSettings': {
                                    'ArchiveOutputSettings': {
                                        'ContainerSettings': {
                                            'M2tsSettings': {
                                                'AbsentInputAudioBehavior': 'DROP'|'ENCODE_SILENCE',
                                                'Arib': 'DISABLED'|'ENABLED',
                                                'AribCaptionsPid': 'string',
                                                'AribCaptionsPidControl': 'AUTO'|'USE_CONFIGURED',
                                                'AudioBufferModel': 'ATSC'|'DVB',
                                                'AudioFramesPerPes': 123,
                                                'AudioPids': 'string',
                                                'AudioStreamType': 'ATSC'|'DVB',
                                                'Bitrate': 123,
                                                'BufferModel': 'MULTIPLEX'|'NONE',
                                                'CcDescriptor': 'DISABLED'|'ENABLED',
                                                'DvbNitSettings': {
                                                    'NetworkId': 123,
                                                    'NetworkName': 'string',
                                                    'RepInterval': 123
                                                },
                                                'DvbSdtSettings': {
                                                    'OutputSdt': 'SDT_FOLLOW'|'SDT_FOLLOW_IF_PRESENT'|'SDT_MANUAL'|'SDT_NONE',
                                                    'RepInterval': 123,
                                                    'ServiceName': 'string',
                                                    'ServiceProviderName': 'string'
                                                },
                                                'DvbSubPids': 'string',
                                                'DvbTdtSettings': {
                                                    'RepInterval': 123
                                                },
                                                'DvbTeletextPid': 'string',
                                                'Ebif': 'NONE'|'PASSTHROUGH',
                                                'EbpAudioInterval': 'VIDEO_AND_FIXED_INTERVALS'|'VIDEO_INTERVAL',
                                                'EbpLookaheadMs': 123,
                                                'EbpPlacement': 'VIDEO_AND_AUDIO_PIDS'|'VIDEO_PID',
                                                'EcmPid': 'string',
                                                'EsRateInPes': 'EXCLUDE'|'INCLUDE',
                                                'EtvPlatformPid': 'string',
                                                'EtvSignalPid': 'string',
                                                'FragmentTime': 123.0,
                                                'Klv': 'NONE'|'PASSTHROUGH',
                                                'KlvDataPids': 'string',
                                                'NullPacketBitrate': 123.0,
                                                'PatInterval': 123,
                                                'PcrControl': 'CONFIGURED_PCR_PERIOD'|'PCR_EVERY_PES_PACKET',
                                                'PcrPeriod': 123,
                                                'PcrPid': 'string',
                                                'PmtInterval': 123,
                                                'PmtPid': 'string',
                                                'ProgramNum': 123,
                                                'RateMode': 'CBR'|'VBR',
                                                'Scte27Pids': 'string',
                                                'Scte35Control': 'NONE'|'PASSTHROUGH',
                                                'Scte35Pid': 'string',
                                                'SegmentationMarkers': 'EBP'|'EBP_LEGACY'|'NONE'|'PSI_SEGSTART'|'RAI_ADAPT'|'RAI_SEGSTART',
                                                'SegmentationStyle': 'MAINTAIN_CADENCE'|'RESET_CADENCE',
                                                'SegmentationTime': 123.0,
                                                'TimedMetadataBehavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                                'TimedMetadataPid': 'string',
                                                'TransportStreamId': 123,
                                                'VideoPid': 'string'
                                            }
                                        },
                                        'Extension': 'string',
                                        'NameModifier': 'string'
                                    },
                                    'HlsOutputSettings': {
                                        'HlsSettings': {
                                            'AudioOnlyHlsSettings': {
                                                'AudioGroupId': 'string',
                                                'AudioOnlyImage': {
                                                    'PasswordParam': 'string',
                                                    'Uri': 'string',
                                                    'Username': 'string'
                                                },
                                                'AudioTrackType': 'ALTERNATE_AUDIO_AUTO_SELECT'|'ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT'|'ALTERNATE_AUDIO_NOT_AUTO_SELECT'|'AUDIO_ONLY_VARIANT_STREAM'
                                            },
                                            'StandardHlsSettings': {
                                                'AudioRenditionSets': 'string',
                                                'M3u8Settings': {
                                                    'AudioFramesPerPes': 123,
                                                    'AudioPids': 'string',
                                                    'EcmPid': 'string',
                                                    'PatInterval': 123,
                                                    'PcrControl': 'CONFIGURED_PCR_PERIOD'|'PCR_EVERY_PES_PACKET',
                                                    'PcrPeriod': 123,
                                                    'PcrPid': 'string',
                                                    'PmtInterval': 123,
                                                    'PmtPid': 'string',
                                                    'ProgramNum': 123,
                                                    'Scte35Behavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                                    'Scte35Pid': 'string',
                                                    'TimedMetadataBehavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                                    'TimedMetadataPid': 'string',
                                                    'TransportStreamId': 123,
                                                    'VideoPid': 'string'
                                                }
                                            }
                                        },
                                        'NameModifier': 'string',
                                        'SegmentModifier': 'string'
                                    },
                                    'MsSmoothOutputSettings': {
                                        'NameModifier': 'string'
                                    },
                                    'RtmpOutputSettings': {
                                        'CertificateMode': 'SELF_SIGNED'|'VERIFY_AUTHENTICITY',
                                        'ConnectionRetryInterval': 123,
                                        'Destination': {
                                            'DestinationRefId': 'string'
                                        },
                                        'NumRetries': 123
                                    },
                                    'UdpOutputSettings': {
                                        'BufferMsec': 123,
                                        'ContainerSettings': {
                                            'M2tsSettings': {
                                                'AbsentInputAudioBehavior': 'DROP'|'ENCODE_SILENCE',
                                                'Arib': 'DISABLED'|'ENABLED',
                                                'AribCaptionsPid': 'string',
                                                'AribCaptionsPidControl': 'AUTO'|'USE_CONFIGURED',
                                                'AudioBufferModel': 'ATSC'|'DVB',
                                                'AudioFramesPerPes': 123,
                                                'AudioPids': 'string',
                                                'AudioStreamType': 'ATSC'|'DVB',
                                                'Bitrate': 123,
                                                'BufferModel': 'MULTIPLEX'|'NONE',
                                                'CcDescriptor': 'DISABLED'|'ENABLED',
                                                'DvbNitSettings': {
                                                    'NetworkId': 123,
                                                    'NetworkName': 'string',
                                                    'RepInterval': 123
                                                },
                                                'DvbSdtSettings': {
                                                    'OutputSdt': 'SDT_FOLLOW'|'SDT_FOLLOW_IF_PRESENT'|'SDT_MANUAL'|'SDT_NONE',
                                                    'RepInterval': 123,
                                                    'ServiceName': 'string',
                                                    'ServiceProviderName': 'string'
                                                },
                                                'DvbSubPids': 'string',
                                                'DvbTdtSettings': {
                                                    'RepInterval': 123
                                                },
                                                'DvbTeletextPid': 'string',
                                                'Ebif': 'NONE'|'PASSTHROUGH',
                                                'EbpAudioInterval': 'VIDEO_AND_FIXED_INTERVALS'|'VIDEO_INTERVAL',
                                                'EbpLookaheadMs': 123,
                                                'EbpPlacement': 'VIDEO_AND_AUDIO_PIDS'|'VIDEO_PID',
                                                'EcmPid': 'string',
                                                'EsRateInPes': 'EXCLUDE'|'INCLUDE',
                                                'EtvPlatformPid': 'string',
                                                'EtvSignalPid': 'string',
                                                'FragmentTime': 123.0,
                                                'Klv': 'NONE'|'PASSTHROUGH',
                                                'KlvDataPids': 'string',
                                                'NullPacketBitrate': 123.0,
                                                'PatInterval': 123,
                                                'PcrControl': 'CONFIGURED_PCR_PERIOD'|'PCR_EVERY_PES_PACKET',
                                                'PcrPeriod': 123,
                                                'PcrPid': 'string',
                                                'PmtInterval': 123,
                                                'PmtPid': 'string',
                                                'ProgramNum': 123,
                                                'RateMode': 'CBR'|'VBR',
                                                'Scte27Pids': 'string',
                                                'Scte35Control': 'NONE'|'PASSTHROUGH',
                                                'Scte35Pid': 'string',
                                                'SegmentationMarkers': 'EBP'|'EBP_LEGACY'|'NONE'|'PSI_SEGSTART'|'RAI_ADAPT'|'RAI_SEGSTART',
                                                'SegmentationStyle': 'MAINTAIN_CADENCE'|'RESET_CADENCE',
                                                'SegmentationTime': 123.0,
                                                'TimedMetadataBehavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                                'TimedMetadataPid': 'string',
                                                'TransportStreamId': 123,
                                                'VideoPid': 'string'
                                            }
                                        },
                                        'Destination': {
                                            'DestinationRefId': 'string'
                                        },
                                        'FecOutputSettings': {
                                            'ColumnDepth': 123,
                                            'IncludeFec': 'COLUMN'|'COLUMN_AND_ROW',
                                            'RowLength': 123
                                        }
                                    }
                                },
                                'VideoDescriptionName': 'string'
                            },
                        ]
                    },
                ],
                'TimecodeConfig': {
                    'Source': 'EMBEDDED'|'SYSTEMCLOCK'|'ZEROBASED',
                    'SyncThreshold': 123
                },
                'VideoDescriptions': [
                    {
                        'CodecSettings': {
                            'H264Settings': {
                                'AdaptiveQuantization': 'HIGH'|'HIGHER'|'LOW'|'MAX'|'MEDIUM'|'OFF',
                                'AfdSignaling': 'AUTO'|'FIXED'|'NONE',
                                'Bitrate': 123,
                                'BufFillPct': 123,
                                'BufSize': 123,
                                'ColorMetadata': 'IGNORE'|'INSERT',
                                'EntropyEncoding': 'CABAC'|'CAVLC',
                                'FixedAfd': 'AFD_0000'|'AFD_0010'|'AFD_0011'|'AFD_0100'|'AFD_1000'|'AFD_1001'|'AFD_1010'|'AFD_1011'|'AFD_1101'|'AFD_1110'|'AFD_1111',
                                'FlickerAq': 'DISABLED'|'ENABLED',
                                'FramerateControl': 'INITIALIZE_FROM_SOURCE'|'SPECIFIED',
                                'FramerateDenominator': 123,
                                'FramerateNumerator': 123,
                                'GopBReference': 'DISABLED'|'ENABLED',
                                'GopClosedCadence': 123,
                                'GopNumBFrames': 123,
                                'GopSize': 123.0,
                                'GopSizeUnits': 'FRAMES'|'SECONDS',
                                'Level': 'H264_LEVEL_1'|'H264_LEVEL_1_1'|'H264_LEVEL_1_2'|'H264_LEVEL_1_3'|'H264_LEVEL_2'|'H264_LEVEL_2_1'|'H264_LEVEL_2_2'|'H264_LEVEL_3'|'H264_LEVEL_3_1'|'H264_LEVEL_3_2'|'H264_LEVEL_4'|'H264_LEVEL_4_1'|'H264_LEVEL_4_2'|'H264_LEVEL_5'|'H264_LEVEL_5_1'|'H264_LEVEL_5_2'|'H264_LEVEL_AUTO',
                                'LookAheadRateControl': 'HIGH'|'LOW'|'MEDIUM',
                                'MaxBitrate': 123,
                                'MinIInterval': 123,
                                'NumRefFrames': 123,
                                'ParControl': 'INITIALIZE_FROM_SOURCE'|'SPECIFIED',
                                'ParDenominator': 123,
                                'ParNumerator': 123,
                                'Profile': 'BASELINE'|'HIGH'|'HIGH_10BIT'|'HIGH_422'|'HIGH_422_10BIT'|'MAIN',
                                'QvbrQualityLevel': 123,
                                'RateControlMode': 'CBR'|'QVBR'|'VBR',
                                'ScanType': 'INTERLACED'|'PROGRESSIVE',
                                'SceneChangeDetect': 'DISABLED'|'ENABLED',
                                'Slices': 123,
                                'Softness': 123,
                                'SpatialAq': 'DISABLED'|'ENABLED',
                                'SubgopLength': 'DYNAMIC'|'FIXED',
                                'Syntax': 'DEFAULT'|'RP2027',
                                'TemporalAq': 'DISABLED'|'ENABLED',
                                'TimecodeInsertion': 'DISABLED'|'PIC_TIMING_SEI'
                            }
                        },
                        'Height': 123,
                        'Name': 'string',
                        'RespondToAfd': 'NONE'|'PASSTHROUGH'|'RESPOND',
                        'ScalingBehavior': 'DEFAULT'|'STRETCH_TO_OUTPUT',
                        'Sharpness': 123,
                        'Width': 123
                    },
                ]
            },
            'Id': 'string',
            'InputAttachments': [
                {
                    'InputAttachmentName': 'string',
                    'InputId': 'string',
                    'InputSettings': {
                        'AudioSelectors': [
                            {
                                'Name': 'string',
                                'SelectorSettings': {
                                    'AudioLanguageSelection': {
                                        'LanguageCode': 'string',
                                        'LanguageSelectionPolicy': 'LOOSE'|'STRICT'
                                    },
                                    'AudioPidSelection': {
                                        'Pid': 123
                                    }
                                }
                            },
                        ],
                        'CaptionSelectors': [
                            {
                                'LanguageCode': 'string',
                                'Name': 'string',
                                'SelectorSettings': {
                                    'AribSourceSettings': {},
                                    'DvbSubSourceSettings': {
                                        'Pid': 123
                                    },
                                    'EmbeddedSourceSettings': {
                                        'Convert608To708': 'DISABLED'|'UPCONVERT',
                                        'Scte20Detection': 'AUTO'|'OFF',
                                        'Source608ChannelNumber': 123,
                                        'Source608TrackNumber': 123
                                    },
                                    'Scte20SourceSettings': {
                                        'Convert608To708': 'DISABLED'|'UPCONVERT',
                                        'Source608ChannelNumber': 123
                                    },
                                    'Scte27SourceSettings': {
                                        'Pid': 123
                                    },
                                    'TeletextSourceSettings': {
                                        'PageNumber': 'string'
                                    }
                                }
                            },
                        ],
                        'DeblockFilter': 'DISABLED'|'ENABLED',
                        'DenoiseFilter': 'DISABLED'|'ENABLED',
                        'FilterStrength': 123,
                        'InputFilter': 'AUTO'|'DISABLED'|'FORCED',
                        'NetworkInputSettings': {
                            'HlsInputSettings': {
                                'Bandwidth': 123,
                                'BufferSegments': 123,
                                'Retries': 123,
                                'RetryInterval': 123
                            },
                            'ServerValidation': 'CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME'|'CHECK_CRYPTOGRAPHY_ONLY'
                        },
                        'SourceEndBehavior': 'CONTINUE'|'LOOP',
                        'VideoSelector': {
                            'ColorSpace': 'FOLLOW'|'REC_601'|'REC_709',
                            'ColorSpaceUsage': 'FALLBACK'|'FORCE',
                            'SelectorSettings': {
                                'VideoSelectorPid': {
                                    'Pid': 123
                                },
                                'VideoSelectorProgramId': {
                                    'ProgramId': 123
                                }
                            }
                        }
                    }
                },
            ],
            'InputSpecification': {
                'Codec': 'MPEG2'|'AVC'|'HEVC',
                'MaximumBitrate': 'MAX_10_MBPS'|'MAX_20_MBPS'|'MAX_50_MBPS',
                'Resolution': 'SD'|'HD'|'UHD'
            },
            'LogLevel': 'ERROR'|'WARNING'|'INFO'|'DEBUG'|'DISABLED',
            'Name': 'string',
            'PipelinesRunningCount': 123,
            'RoleArn': 'string',
            'State': 'CREATING'|'CREATE_FAILED'|'IDLE'|'STARTING'|'RUNNING'|'RECOVERING'|'STOPPING'|'DELETING'|'DELETED'
        }
    }
    
    
    :returns: 
    (dict) -- Creation of channel is started.
    Channel (dict) -- Placeholder documentation for Channel
    Arn (string) -- The unique arn of the channel.
    Destinations (list) -- A list of destinations of the channel. For UDP outputs, there is one destination per output. For other types (HLS, for example), there is one destination per packager.
    (dict) -- Placeholder documentation for OutputDestination
    Id (string) -- User-specified id. This is used in an output group or an output.
    Settings (list) -- Destination settings for output; one for each redundant encoder.
    (dict) -- Placeholder documentation for OutputDestinationSettings
    PasswordParam (string) -- key used to extract the password from EC2 Parameter store
    StreamName (string) -- Stream name for RTMP destinations (URLs of type rtmp://)
    Url (string) -- A URL specifying a destination
    Username (string) -- username for destination
    
    
    
    
    
    
    
    
    EgressEndpoints (list) -- The endpoints where outgoing connections initiate from
    (dict) -- Placeholder documentation for ChannelEgressEndpoint
    SourceIp (string) -- Public IP of where a channel's output comes from
    
    
    
    
    EncoderSettings (dict) -- Placeholder documentation for EncoderSettings
    AudioDescriptions (list) -- Placeholder documentation for __listOfAudioDescription
    (dict) -- Placeholder documentation for AudioDescription
    AudioNormalizationSettings (dict) -- Advanced audio normalization settings.
    Algorithm (string) -- Audio normalization algorithm to use. itu17701 conforms to the CALM Act specification, itu17702 conforms to the EBU R-128 specification.
    AlgorithmControl (string) -- When set to correctAudio the output audio is corrected using the chosen algorithm. If set to measureOnly, the audio will be measured but not adjusted.
    TargetLkfs (float) -- Target LKFS(loudness) to adjust volume to. If no value is entered, a default value will be used according to the chosen algorithm. The CALM Act (1770-1) recommends a target of -24 LKFS. The EBU R-128 specification (1770-2) recommends a target of -23 LKFS.
    
    
    AudioSelectorName (string) -- The name of the AudioSelector used as the source for this AudioDescription.
    AudioType (string) -- Applies only if audioTypeControl is useConfigured. The values for audioType are defined in ISO-IEC 13818-1.
    AudioTypeControl (string) -- Determines how audio type is determined. followInput: If the input contains an ISO 639 audioType, then that value is passed through to the output. If the input contains no ISO 639 audioType, the value in Audio Type is included in the output. useConfigured: The value in Audio Type is included in the output. Note that this field and audioType are both ignored if inputType is broadcasterMixedAd.
    CodecSettings (dict) -- Audio codec settings.
    AacSettings (dict) -- Placeholder documentation for AacSettings
    Bitrate (float) -- Average bitrate in bits/second. Valid values depend on rate control mode and profile.
    CodingMode (string) -- Mono, Stereo, or 5.1 channel layout. Valid values depend on rate control mode and profile. The adReceiverMix setting receives a stereo description plus control track and emits a mono AAC encode of the description track, with control data emitted in the PES header as per ETSI TS 101 154 Annex E.
    InputType (string) -- Set to "broadcasterMixedAd" when input contains pre-mixed main audio + AD (narration) as a stereo pair. The Audio Type field (audioType) will be set to 3, which signals to downstream systems that this stream contains "broadcaster mixed AD". Note that the input received by the encoder must contain pre-mixed audio; the encoder does not perform the mixing. The values in audioTypeControl and audioType (in AudioDescription) are ignored when set to broadcasterMixedAd. Leave set to "normal" when input does not contain pre-mixed audio + AD.
    Profile (string) -- AAC Profile.
    RateControlMode (string) -- Rate Control Mode.
    RawFormat (string) -- Sets LATM / LOAS AAC output for raw containers.
    SampleRate (float) -- Sample rate in Hz. Valid values depend on rate control mode and profile.
    Spec (string) -- Use MPEG-2 AAC audio instead of MPEG-4 AAC audio for raw or MPEG-2 Transport Stream containers.
    VbrQuality (string) -- VBR Quality Level - Only used if rateControlMode is VBR.
    
    
    Ac3Settings (dict) -- Placeholder documentation for Ac3Settings
    Bitrate (float) -- Average bitrate in bits/second. Valid bitrates depend on the coding mode.
    BitstreamMode (string) -- Specifies the bitstream mode (bsmod) for the emitted AC-3 stream. See ATSC A/52-2012 for background on these values.
    CodingMode (string) -- Dolby Digital coding mode. Determines number of channels.
    Dialnorm (integer) -- Sets the dialnorm for the output. If excluded and input audio is Dolby Digital, dialnorm will be passed through.
    DrcProfile (string) -- If set to filmStandard, adds dynamic range compression signaling to the output bitstream as defined in the Dolby Digital specification.
    LfeFilter (string) -- When set to enabled, applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid in codingMode32Lfe mode.
    MetadataControl (string) -- When set to "followInput", encoder metadata will be sourced from the DD, DD+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used.
    
    
    Eac3Settings (dict) -- Placeholder documentation for Eac3Settings
    AttenuationControl (string) -- When set to attenuate3Db, applies a 3 dB attenuation to the surround channels. Only used for 3/2 coding mode.
    Bitrate (float) -- Average bitrate in bits/second. Valid bitrates depend on the coding mode.
    BitstreamMode (string) -- Specifies the bitstream mode (bsmod) for the emitted E-AC-3 stream. See ATSC A/52-2012 (Annex E) for background on these values.
    CodingMode (string) -- Dolby Digital Plus coding mode. Determines number of channels.
    DcFilter (string) -- When set to enabled, activates a DC highpass filter for all input channels.
    Dialnorm (integer) -- Sets the dialnorm for the output. If blank and input audio is Dolby Digital Plus, dialnorm will be passed through.
    DrcLine (string) -- Sets the Dolby dynamic range compression profile.
    DrcRf (string) -- Sets the profile for heavy Dolby dynamic range compression, ensures that the instantaneous signal peaks do not exceed specified levels.
    LfeControl (string) -- When encoding 3/2 audio, setting to lfe enables the LFE channel
    LfeFilter (string) -- When set to enabled, applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with codingMode32 coding mode.
    LoRoCenterMixLevel (float) -- Left only/Right only center mix level. Only used for 3/2 coding mode.
    LoRoSurroundMixLevel (float) -- Left only/Right only surround mix level. Only used for 3/2 coding mode.
    LtRtCenterMixLevel (float) -- Left total/Right total center mix level. Only used for 3/2 coding mode.
    LtRtSurroundMixLevel (float) -- Left total/Right total surround mix level. Only used for 3/2 coding mode.
    MetadataControl (string) -- When set to followInput, encoder metadata will be sourced from the DD, DD+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used.
    PassthroughControl (string) -- When set to whenPossible, input DD+ audio will be passed through if it is present on the input. This detection is dynamic over the life of the transcode. Inputs that alternate between DD+ and non-DD+ content will have a consistent DD+ output as the system alternates between passthrough and encoding.
    PhaseControl (string) -- When set to shift90Degrees, applies a 90-degree phase shift to the surround channels. Only used for 3/2 coding mode.
    StereoDownmix (string) -- Stereo downmix preference. Only used for 3/2 coding mode.
    SurroundExMode (string) -- When encoding 3/2 audio, sets whether an extra center back surround channel is matrix encoded into the left and right surround channels.
    SurroundMode (string) -- When encoding 2/0 audio, sets whether Dolby Surround is matrix encoded into the two channels.
    
    
    Mp2Settings (dict) -- Placeholder documentation for Mp2Settings
    Bitrate (float) -- Average bitrate in bits/second.
    CodingMode (string) -- The MPEG2 Audio coding mode. Valid values are codingMode10 (for mono) or codingMode20 (for stereo).
    SampleRate (float) -- Sample rate in Hz.
    
    
    PassThroughSettings (dict) -- Placeholder documentation for PassThroughSettings
    
    
    LanguageCode (string) -- Indicates the language of the audio output track. Only used if languageControlMode is useConfigured, or there is no ISO 639 language code specified in the input.
    LanguageCodeControl (string) -- Choosing followInput will cause the ISO 639 language code of the output to follow the ISO 639 language code of the input. The languageCode will be used when useConfigured is set, or when followInput is selected but there is no ISO 639 language code specified by the input.
    Name (string) -- The name of this AudioDescription. Outputs will use this name to uniquely identify this AudioDescription. Description names should be unique within this Live Event.
    RemixSettings (dict) -- Settings that control how input audio channels are remixed into the output audio channels.
    ChannelMappings (list) -- Mapping of input channels to output channels, with appropriate gain adjustments.
    (dict) -- Placeholder documentation for AudioChannelMapping
    InputChannelLevels (list) -- Indices and gain values for each input channel that should be remixed into this output channel.
    (dict) -- Placeholder documentation for InputChannelLevel
    Gain (integer) -- Remixing value. Units are in dB and acceptable values are within the range from -60 (mute) and 6 dB.
    InputChannel (integer) -- The index of the input channel used as a source.
    
    
    
    
    OutputChannel (integer) -- The index of the output channel being produced.
    
    
    
    
    ChannelsIn (integer) -- Number of input channels to be used.
    ChannelsOut (integer) -- Number of output channels to be produced. Valid values: 1, 2, 4, 6, 8
    
    
    StreamName (string) -- Used for MS Smooth and Apple HLS outputs. Indicates the name displayed by the player (eg. English, or Director Commentary).
    
    
    
    
    AvailBlanking (dict) -- Settings for ad avail blanking.
    AvailBlankingImage (dict) -- Blanking image to be used. Leave empty for solid black. Only bmp and png images are supported.
    PasswordParam (string) -- key used to extract the password from EC2 Parameter store
    Uri (string) -- Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: "rtmp://fmsserver/live".
    Username (string) -- Documentation update needed
    
    
    State (string) -- When set to enabled, causes video, audio and captions to be blanked when insertion metadata is added.
    
    
    AvailConfiguration (dict) -- Event-wide configuration settings for ad avail insertion.
    AvailSettings (dict) -- Ad avail settings.
    Scte35SpliceInsert (dict) -- Placeholder documentation for Scte35SpliceInsert
    AdAvailOffset (integer) -- When specified, this offset (in milliseconds) is added to the input Ad Avail PTS time. This only applies to embedded SCTE 104/35 messages and does not apply to OOB messages.
    NoRegionalBlackoutFlag (string) -- When set to ignore, Segment Descriptors with noRegionalBlackoutFlag set to 0 will no longer trigger blackouts or Ad Avail slates
    WebDeliveryAllowedFlag (string) -- When set to ignore, Segment Descriptors with webDeliveryAllowedFlag set to 0 will no longer trigger blackouts or Ad Avail slates
    
    
    Scte35TimeSignalApos (dict) -- Placeholder documentation for Scte35TimeSignalApos
    AdAvailOffset (integer) -- When specified, this offset (in milliseconds) is added to the input Ad Avail PTS time. This only applies to embedded SCTE 104/35 messages and does not apply to OOB messages.
    NoRegionalBlackoutFlag (string) -- When set to ignore, Segment Descriptors with noRegionalBlackoutFlag set to 0 will no longer trigger blackouts or Ad Avail slates
    WebDeliveryAllowedFlag (string) -- When set to ignore, Segment Descriptors with webDeliveryAllowedFlag set to 0 will no longer trigger blackouts or Ad Avail slates
    
    
    
    
    
    
    BlackoutSlate (dict) -- Settings for blackout slate.
    BlackoutSlateImage (dict) -- Blackout slate image to be used. Leave empty for solid black. Only bmp and png images are supported.
    PasswordParam (string) -- key used to extract the password from EC2 Parameter store
    Uri (string) -- Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: "rtmp://fmsserver/live".
    Username (string) -- Documentation update needed
    
    
    NetworkEndBlackout (string) -- Setting to enabled causes the encoder to blackout the video, audio, and captions, and raise the "Network Blackout Image" slate when an SCTE104/35 Network End Segmentation Descriptor is encountered. The blackout will be lifted when the Network Start Segmentation Descriptor is encountered. The Network End and Network Start descriptors must contain a network ID that matches the value entered in "Network ID".
    NetworkEndBlackoutImage (dict) -- Path to local file to use as Network End Blackout image. Image will be scaled to fill the entire output raster.
    PasswordParam (string) -- key used to extract the password from EC2 Parameter store
    Uri (string) -- Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: "rtmp://fmsserver/live".
    Username (string) -- Documentation update needed
    
    
    NetworkId (string) -- Provides Network ID that matches EIDR ID format (e.g., "10.XXXX/XXXX-XXXX-XXXX-XXXX-XXXX-C").
    State (string) -- When set to enabled, causes video, audio and captions to be blanked when indicated by program metadata.
    
    
    CaptionDescriptions (list) -- Settings for caption decriptions
    (dict) -- Output groups for this Live Event. Output groups contain information about where streams should be distributed.
    CaptionSelectorName (string) -- Specifies which input caption selector to use as a caption source when generating output captions. This field should match a captionSelector name.
    DestinationSettings (dict) -- Additional settings for captions destination that depend on the destination type.
    AribDestinationSettings (dict) -- Placeholder documentation for AribDestinationSettings
    BurnInDestinationSettings (dict) -- Placeholder documentation for BurnInDestinationSettings
    Alignment (string) -- If no explicit xPosition or yPosition is provided, setting alignment to centered will place the captions at the bottom center of the output. Similarly, setting a left alignment will align captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. Selecting "smart" justification will left-justify live subtitles and center-justify pre-recorded subtitles. All burn-in and DVB-Sub font settings must match.
    BackgroundColor (string) -- Specifies the color of the rectangle behind the captions. All burn-in and DVB-Sub font settings must match.
    BackgroundOpacity (integer) -- Specifies the opacity of the background rectangle. 255 is opaque; 0 is transparent. Leaving this parameter out is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
    Font (dict) -- External font file used for caption burn-in. File extension must be 'ttf' or 'tte'. Although the user can select output fonts for many different types of input captions, embedded, STL and teletext sources use a strict grid system. Using external fonts with these caption sources could cause unexpected display of proportional fonts. All burn-in and DVB-Sub font settings must match.
    PasswordParam (string) -- key used to extract the password from EC2 Parameter store
    Uri (string) -- Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: "rtmp://fmsserver/live".
    Username (string) -- Documentation update needed
    
    
    FontColor (string) -- Specifies the color of the burned-in captions. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
    FontOpacity (integer) -- Specifies the opacity of the burned-in captions. 255 is opaque; 0 is transparent. All burn-in and DVB-Sub font settings must match.
    FontResolution (integer) -- Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and DVB-Sub font settings must match.
    FontSize (string) -- When set to 'auto' fontSize will scale depending on the size of the output. Giving a positive integer will specify the exact font size in points. All burn-in and DVB-Sub font settings must match.
    OutlineColor (string) -- Specifies font outline color. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
    OutlineSize (integer) -- Specifies font outline size in pixels. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
    ShadowColor (string) -- Specifies the color of the shadow cast by the captions. All burn-in and DVB-Sub font settings must match.
    ShadowOpacity (integer) -- Specifies the opacity of the shadow. 255 is opaque; 0 is transparent. Leaving this parameter out is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
    ShadowXOffset (integer) -- Specifies the horizontal offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left. All burn-in and DVB-Sub font settings must match.
    ShadowYOffset (integer) -- Specifies the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. All burn-in and DVB-Sub font settings must match.
    TeletextGridControl (string) -- Controls whether a fixed grid size will be used to generate the output subtitles bitmap. Only applicable for Teletext inputs and DVB-Sub/Burn-in outputs.
    XPosition (integer) -- Specifies the horizontal position of the caption relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit xPosition is provided, the horizontal caption position will be determined by the alignment parameter. All burn-in and DVB-Sub font settings must match.
    YPosition (integer) -- Specifies the vertical position of the caption relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit yPosition is provided, the caption will be positioned towards the bottom of the output. All burn-in and DVB-Sub font settings must match.
    
    
    DvbSubDestinationSettings (dict) -- Placeholder documentation for DvbSubDestinationSettings
    Alignment (string) -- If no explicit xPosition or yPosition is provided, setting alignment to centered will place the captions at the bottom center of the output. Similarly, setting a left alignment will align captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. Selecting "smart" justification will left-justify live subtitles and center-justify pre-recorded subtitles. This option is not valid for source captions that are STL or 608/embedded. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
    BackgroundColor (string) -- Specifies the color of the rectangle behind the captions. All burn-in and DVB-Sub font settings must match.
    BackgroundOpacity (integer) -- Specifies the opacity of the background rectangle. 255 is opaque; 0 is transparent. Leaving this parameter blank is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
    Font (dict) -- External font file used for caption burn-in. File extension must be 'ttf' or 'tte'. Although the user can select output fonts for many different types of input captions, embedded, STL and teletext sources use a strict grid system. Using external fonts with these caption sources could cause unexpected display of proportional fonts. All burn-in and DVB-Sub font settings must match.
    PasswordParam (string) -- key used to extract the password from EC2 Parameter store
    Uri (string) -- Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: "rtmp://fmsserver/live".
    Username (string) -- Documentation update needed
    
    
    FontColor (string) -- Specifies the color of the burned-in captions. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
    FontOpacity (integer) -- Specifies the opacity of the burned-in captions. 255 is opaque; 0 is transparent. All burn-in and DVB-Sub font settings must match.
    FontResolution (integer) -- Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and DVB-Sub font settings must match.
    FontSize (string) -- When set to auto fontSize will scale depending on the size of the output. Giving a positive integer will specify the exact font size in points. All burn-in and DVB-Sub font settings must match.
    OutlineColor (string) -- Specifies font outline color. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
    OutlineSize (integer) -- Specifies font outline size in pixels. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
    ShadowColor (string) -- Specifies the color of the shadow cast by the captions. All burn-in and DVB-Sub font settings must match.
    ShadowOpacity (integer) -- Specifies the opacity of the shadow. 255 is opaque; 0 is transparent. Leaving this parameter blank is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
    ShadowXOffset (integer) -- Specifies the horizontal offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left. All burn-in and DVB-Sub font settings must match.
    ShadowYOffset (integer) -- Specifies the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. All burn-in and DVB-Sub font settings must match.
    TeletextGridControl (string) -- Controls whether a fixed grid size will be used to generate the output subtitles bitmap. Only applicable for Teletext inputs and DVB-Sub/Burn-in outputs.
    XPosition (integer) -- Specifies the horizontal position of the caption relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit xPosition is provided, the horizontal caption position will be determined by the alignment parameter. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
    YPosition (integer) -- Specifies the vertical position of the caption relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit yPosition is provided, the caption will be positioned towards the bottom of the output. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
    
    
    EmbeddedDestinationSettings (dict) -- Placeholder documentation for EmbeddedDestinationSettings
    EmbeddedPlusScte20DestinationSettings (dict) -- Placeholder documentation for EmbeddedPlusScte20DestinationSettings
    RtmpCaptionInfoDestinationSettings (dict) -- Placeholder documentation for RtmpCaptionInfoDestinationSettings
    Scte20PlusEmbeddedDestinationSettings (dict) -- Placeholder documentation for Scte20PlusEmbeddedDestinationSettings
    Scte27DestinationSettings (dict) -- Placeholder documentation for Scte27DestinationSettings
    SmpteTtDestinationSettings (dict) -- Placeholder documentation for SmpteTtDestinationSettings
    TeletextDestinationSettings (dict) -- Placeholder documentation for TeletextDestinationSettings
    TtmlDestinationSettings (dict) -- Placeholder documentation for TtmlDestinationSettings
    StyleControl (string) -- When set to passthrough, passes through style and position information from a TTML-like input source (TTML, SMPTE-TT, CFF-TT) to the CFF-TT output or TTML output.
    
    
    WebvttDestinationSettings (dict) -- Placeholder documentation for WebvttDestinationSettings
    
    
    LanguageCode (string) -- ISO 639-2 three-digit code: http://www.loc.gov/standards/iso639-2/
    LanguageDescription (string) -- Human readable information to indicate captions available for players (eg. English, or Spanish).
    Name (string) -- Name of the caption description. Used to associate a caption description with an output. Names must be unique within an event.
    
    
    
    
    GlobalConfiguration (dict) -- Configuration settings that apply to the event as a whole.
    InitialAudioGain (integer) -- Value to set the initial audio gain for the Live Event.
    InputEndAction (string) -- Indicates the action to take when the current input completes (e.g. end-of-file). When switchAndLoopInputs is configured the encoder will restart at the beginning of the first input. When "none" is configured the encoder will transcode either black, a solid color, or a user specified slate images per the "Input Loss Behavior" configuration until the next input switch occurs (which is controlled through the Channel Schedule API).
    InputLossBehavior (dict) -- Settings for system actions when input is lost.
    BlackFrameMsec (integer) -- Documentation update needed
    InputLossImageColor (string) -- When input loss image type is "color" this field specifies the color to use. Value: 6 hex characters representing the values of RGB.
    InputLossImageSlate (dict) -- When input loss image type is "slate" these fields specify the parameters for accessing the slate.
    PasswordParam (string) -- key used to extract the password from EC2 Parameter store
    Uri (string) -- Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: "rtmp://fmsserver/live".
    Username (string) -- Documentation update needed
    
    
    InputLossImageType (string) -- Indicates whether to substitute a solid color or a slate into the output after input loss exceeds blackFrameMsec.
    RepeatFrameMsec (integer) -- Documentation update needed
    
    
    OutputTimingSource (string) -- Indicates whether the rate of frames emitted by the Live encoder should be paced by its system clock (which optionally may be locked to another source via NTP) or should be locked to the clock of the source that is providing the input stream.
    SupportLowFramerateInputs (string) -- Adjusts video input buffer for streams with very low video framerates. This is commonly set to enabled for music channels with less than one video frame per second.
    
    
    OutputGroups (list) -- Placeholder documentation for __listOfOutputGroup
    (dict) -- Output groups for this Live Event. Output groups contain information about where streams should be distributed.
    Name (string) -- Custom output group name optionally defined by the user. Only letters, numbers, and the underscore character allowed; only 32 characters allowed.
    OutputGroupSettings (dict) -- Settings associated with the output group.
    ArchiveGroupSettings (dict) -- Placeholder documentation for ArchiveGroupSettings
    Destination (dict) -- A directory and base filename where archive files should be written. If the base filename portion of the URI is left blank, the base filename of the first input will be automatically inserted.
    DestinationRefId (string) -- Placeholder documentation for __string
    
    
    RolloverInterval (integer) -- Number of seconds to write to archive file before closing and starting a new one.
    
    
    HlsGroupSettings (dict) -- Placeholder documentation for HlsGroupSettings
    AdMarkers (list) -- Choose one or more ad marker types to pass SCTE35 signals through to this group of Apple HLS outputs.
    (string) -- Placeholder documentation for HlsAdMarkers
    
    
    BaseUrlContent (string) -- A partial URI prefix that will be prepended to each output in the media .m3u8 file. Can be used if base manifest is delivered from a different URL than the main .m3u8 file.
    BaseUrlManifest (string) -- A partial URI prefix that will be prepended to each output in the media .m3u8 file. Can be used if base manifest is delivered from a different URL than the main .m3u8 file.
    CaptionLanguageMappings (list) -- Mapping of up to 4 caption channels to caption languages. Is only meaningful if captionLanguageSetting is set to "insert".
    (dict) -- Maps a caption channel to an ISO 693-2 language code (http://www.loc.gov/standards/iso639-2), with an optional description.
    CaptionChannel (integer) -- The closed caption channel being described by this CaptionLanguageMapping. Each channel mapping must have a unique channel number (maximum of 4)
    LanguageCode (string) -- Three character ISO 639-2 language code (see http://www.loc.gov/standards/iso639-2)
    LanguageDescription (string) -- Textual description of language
    
    
    
    
    CaptionLanguageSetting (string) -- Applies only to 608 Embedded output captions. insert: Include CLOSED-CAPTIONS lines in the manifest. Specify at least one language in the CC1 Language Code field. One CLOSED-CAPTION line is added for each Language Code you specify. Make sure to specify the languages in the order in which they appear in the original source (if the source is embedded format) or the order of the caption selectors (if the source is other than embedded). Otherwise, languages in the manifest will not match up properly with the output captions. none: Include CLOSED-CAPTIONS=NONE line in the manifest. omit: Omit any CLOSED-CAPTIONS line from the manifest.
    ClientCache (string) -- When set to "disabled", sets the #EXT-X-ALLOW-CACHE:no tag in the manifest, which prevents clients from saving media segments for later replay.
    CodecSpecification (string) -- Specification to use (RFC-6381 or the default RFC-4281) during m3u8 playlist generation.
    ConstantIv (string) -- For use with encryptionType. This is a 128-bit, 16-byte hex value represented by a 32-character text string. If ivSource is set to "explicit" then this parameter is required and is used as the IV for encryption.
    Destination (dict) -- A directory or HTTP destination for the HLS segments, manifest files, and encryption keys (if enabled).
    DestinationRefId (string) -- Placeholder documentation for __string
    
    
    DirectoryStructure (string) -- Place segments in subdirectories.
    EncryptionType (string) -- Encrypts the segments with the given encryption scheme. Exclude this parameter if no encryption is desired.
    HlsCdnSettings (dict) -- Parameters that control interactions with the CDN.
    HlsAkamaiSettings (dict) -- Placeholder documentation for HlsAkamaiSettings
    ConnectionRetryInterval (integer) -- Number of seconds to wait before retrying connection to the CDN if the connection is lost.
    FilecacheDuration (integer) -- Size in seconds of file cache for streaming outputs.
    HttpTransferMode (string) -- Specify whether or not to use chunked transfer encoding to Akamai. User should contact Akamai to enable this feature.
    NumRetries (integer) -- Number of retry attempts that will be made before the Live Event is put into an error state.
    RestartDelay (integer) -- If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart.
    Salt (string) -- Salt for authenticated Akamai.
    Token (string) -- Token parameter for authenticated akamai. If not specified, _gda_ is used.
    
    
    HlsBasicPutSettings (dict) -- Placeholder documentation for HlsBasicPutSettings
    ConnectionRetryInterval (integer) -- Number of seconds to wait before retrying connection to the CDN if the connection is lost.
    FilecacheDuration (integer) -- Size in seconds of file cache for streaming outputs.
    NumRetries (integer) -- Number of retry attempts that will be made before the Live Event is put into an error state.
    RestartDelay (integer) -- If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart.
    
    
    HlsMediaStoreSettings (dict) -- Placeholder documentation for HlsMediaStoreSettings
    ConnectionRetryInterval (integer) -- Number of seconds to wait before retrying connection to the CDN if the connection is lost.
    FilecacheDuration (integer) -- Size in seconds of file cache for streaming outputs.
    MediaStoreStorageClass (string) -- When set to temporal, output files are stored in non-persistent memory for faster reading and writing.
    NumRetries (integer) -- Number of retry attempts that will be made before the Live Event is put into an error state.
    RestartDelay (integer) -- If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart.
    
    
    HlsWebdavSettings (dict) -- Placeholder documentation for HlsWebdavSettings
    ConnectionRetryInterval (integer) -- Number of seconds to wait before retrying connection to the CDN if the connection is lost.
    FilecacheDuration (integer) -- Size in seconds of file cache for streaming outputs.
    HttpTransferMode (string) -- Specify whether or not to use chunked transfer encoding to WebDAV.
    NumRetries (integer) -- Number of retry attempts that will be made before the Live Event is put into an error state.
    RestartDelay (integer) -- If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart.
    
    
    
    
    IndexNSegments (integer) -- If mode is "live", the number of segments to retain in the manifest (.m3u8) file. This number must be less than or equal to keepSegments. If mode is "vod", this parameter has no effect.
    InputLossAction (string) -- Parameter that control output group behavior on input loss.
    IvInManifest (string) -- For use with encryptionType. The IV (Initialization Vector) is a 128-bit number used in conjunction with the key for encrypting blocks. If set to "include", IV is listed in the manifest, otherwise the IV is not in the manifest.
    IvSource (string) -- For use with encryptionType. The IV (Initialization Vector) is a 128-bit number used in conjunction with the key for encrypting blocks. If this setting is "followsSegmentNumber", it will cause the IV to change every segment (to match the segment number). If this is set to "explicit", you must enter a constantIv value.
    KeepSegments (integer) -- If mode is "live", the number of TS segments to retain in the destination directory. If mode is "vod", this parameter has no effect.
    KeyFormat (string) -- The value specifies how the key is represented in the resource identified by the URI. If parameter is absent, an implicit value of "identity" is used. A reverse DNS string can also be given.
    KeyFormatVersions (string) -- Either a single positive integer version value or a slash delimited list of version values (1/2/3).
    KeyProviderSettings (dict) -- The key provider settings.
    StaticKeySettings (dict) -- Placeholder documentation for StaticKeySettings
    KeyProviderServer (dict) -- The URL of the license server used for protecting content.
    PasswordParam (string) -- key used to extract the password from EC2 Parameter store
    Uri (string) -- Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: "rtmp://fmsserver/live".
    Username (string) -- Documentation update needed
    
    
    StaticKeyValue (string) -- Static key value as a 32 character hexadecimal string.
    
    
    
    
    ManifestCompression (string) -- When set to gzip, compresses HLS playlist.
    ManifestDurationFormat (string) -- Indicates whether the output manifest should use floating point or integer values for segment duration.
    MinSegmentLength (integer) -- When set, minimumSegmentLength is enforced by looking ahead and back within the specified range for a nearby avail and extending the segment size if needed.
    Mode (string) -- If "vod", all segments are indexed and kept permanently in the destination and manifest. If "live", only the number segments specified in keepSegments and indexNSegments are kept; newer segments replace older segments, which may prevent players from rewinding all the way to the beginning of the event. VOD mode uses HLS EXT-X-PLAYLIST-TYPE of EVENT while the channel is running, converting it to a "VOD" type manifest on completion of the stream.
    OutputSelection (string) -- Generates the .m3u8 playlist file for this HLS output group. The segmentsOnly option will output segments without the .m3u8 file.
    ProgramDateTime (string) -- Includes or excludes EXT-X-PROGRAM-DATE-TIME tag in .m3u8 manifest files. The value is calculated as follows: either the program date and time are initialized using the input timecode source, or the time is initialized using the input timecode source and the date is initialized using the timestampOffset.
    ProgramDateTimePeriod (integer) -- Period of insertion of EXT-X-PROGRAM-DATE-TIME entry, in seconds.
    RedundantManifest (string) -- When set to "enabled", includes the media playlists from both pipelines in the master manifest (.m3u8) file.
    SegmentLength (integer) -- Length of MPEG-2 Transport Stream segments to create (in seconds). Note that segments will end on the next keyframe after this number of seconds, so actual segment length may be longer.
    SegmentationMode (string) -- useInputSegmentation has been deprecated. The configured segment size is always used.
    SegmentsPerSubdirectory (integer) -- Number of segments to write to a subdirectory before starting a new one. directoryStructure must be subdirectoryPerStream for this setting to have an effect.
    StreamInfResolution (string) -- Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag of variant manifest.
    TimedMetadataId3Frame (string) -- Indicates ID3 frame that has the timecode.
    TimedMetadataId3Period (integer) -- Timed Metadata interval in seconds.
    TimestampDeltaMilliseconds (integer) -- Provides an extra millisecond delta offset to fine tune the timestamps.
    TsFileMode (string) -- When set to "singleFile", emits the program as a single media resource (.ts) file, and uses #EXT-X-BYTERANGE tags to index segment for playback. Playback of VOD mode content during event is not guaranteed due to HTTP server caching.
    
    
    MsSmoothGroupSettings (dict) -- Placeholder documentation for MsSmoothGroupSettings
    AcquisitionPointId (string) -- The value of the "Acquisition Point Identity" element used in each message placed in the sparse track. Only enabled if sparseTrackType is not "none".
    AudioOnlyTimecodeControl (string) -- If set to passthrough for an audio-only MS Smooth output, the fragment absolute time will be set to the current timecode. This option does not write timecodes to the audio elementary stream.
    CertificateMode (string) -- If set to verifyAuthenticity, verify the https certificate chain to a trusted Certificate Authority (CA). This will cause https outputs to self-signed certificates to fail.
    ConnectionRetryInterval (integer) -- Number of seconds to wait before retrying connection to the IIS server if the connection is lost. Content will be cached during this time and the cache will be be delivered to the IIS server once the connection is re-established.
    Destination (dict) -- Smooth Streaming publish point on an IIS server. Elemental Live acts as a "Push" encoder to IIS.
    DestinationRefId (string) -- Placeholder documentation for __string
    
    
    EventId (string) -- MS Smooth event ID to be sent to the IIS server. Should only be specified if eventIdMode is set to useConfigured.
    EventIdMode (string) -- Specifies whether or not to send an event ID to the IIS server. If no event ID is sent and the same Live Event is used without changing the publishing point, clients might see cached video from the previous run. Options: - "useConfigured" - use the value provided in eventId - "useTimestamp" - generate and send an event ID based on the current timestamp - "noEventId" - do not send an event ID to the IIS server.
    EventStopBehavior (string) -- When set to sendEos, send EOS signal to IIS server when stopping the event
    FilecacheDuration (integer) -- Size in seconds of file cache for streaming outputs.
    FragmentLength (integer) -- Length of mp4 fragments to generate (in seconds). Fragment length must be compatible with GOP size and framerate.
    InputLossAction (string) -- Parameter that control output group behavior on input loss.
    NumRetries (integer) -- Number of retry attempts.
    RestartDelay (integer) -- Number of seconds before initiating a restart due to output failure, due to exhausting the numRetries on one segment, or exceeding filecacheDuration.
    SegmentationMode (string) -- useInputSegmentation has been deprecated. The configured segment size is always used.
    SendDelayMs (integer) -- Number of milliseconds to delay the output from the second pipeline.
    SparseTrackType (string) -- If set to scte35, use incoming SCTE-35 messages to generate a sparse track in this group of MS-Smooth outputs.
    StreamManifestBehavior (string) -- When set to send, send stream manifest so publishing point doesn't start until all streams start.
    TimestampOffset (string) -- Timestamp offset for the event. Only used if timestampOffsetMode is set to useConfiguredOffset.
    TimestampOffsetMode (string) -- Type of timestamp date offset to use. - useEventStartDate: Use the date the event was started as the offset - useConfiguredOffset: Use an explicitly configured date as the offset
    
    
    RtmpGroupSettings (dict) -- Placeholder documentation for RtmpGroupSettings
    AuthenticationScheme (string) -- Authentication scheme to use when connecting with CDN
    CacheFullBehavior (string) -- Controls behavior when content cache fills up. If remote origin server stalls the RTMP connection and does not accept content fast enough the 'Media Cache' will fill up. When the cache reaches the duration specified by cacheLength the cache will stop accepting new content. If set to disconnectImmediately, the RTMP output will force a disconnect. Clear the media cache, and reconnect after restartDelay seconds. If set to waitForServer, the RTMP output will wait up to 5 minutes to allow the origin server to begin accepting data again.
    CacheLength (integer) -- Cache length, in seconds, is used to calculate buffer size.
    CaptionData (string) -- Controls the types of data that passes to onCaptionInfo outputs. If set to 'all' then 608 and 708 carried DTVCC data will be passed. If set to 'field1AndField2608' then DTVCC data will be stripped out, but 608 data from both fields will be passed. If set to 'field1608' then only the data carried in 608 from field 1 video will be passed.
    InputLossAction (string) -- Controls the behavior of this RTMP group if input becomes unavailable. - emitOutput: Emit a slate until input returns. - pauseOutput: Stop transmitting data until input returns. This does not close the underlying RTMP connection.
    RestartDelay (integer) -- If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart.
    
    
    UdpGroupSettings (dict) -- Placeholder documentation for UdpGroupSettings
    InputLossAction (string) -- Specifies behavior of last resort when input video is lost, and no more backup inputs are available. When dropTs is selected the entire transport stream will stop being emitted. When dropProgram is selected the program can be dropped from the transport stream (and replaced with null packets to meet the TS bitrate requirement). Or, when emitProgram is chosen the transport stream will continue to be produced normally with repeat frames, black frames, or slate frames substituted for the absent input video.
    TimedMetadataId3Frame (string) -- Indicates ID3 frame that has the timecode.
    TimedMetadataId3Period (integer) -- Timed Metadata interval in seconds.
    
    
    
    
    Outputs (list) -- Placeholder documentation for __listOfOutput
    (dict) -- Output settings. There can be multiple outputs within a group.
    AudioDescriptionNames (list) -- The names of the AudioDescriptions used as audio sources for this output.
    (string) -- Placeholder documentation for __string
    
    
    CaptionDescriptionNames (list) -- The names of the CaptionDescriptions used as caption sources for this output.
    (string) -- Placeholder documentation for __string
    
    
    OutputName (string) -- The name used to identify an output.
    OutputSettings (dict) -- Output type-specific settings.
    ArchiveOutputSettings (dict) -- Placeholder documentation for ArchiveOutputSettings
    ContainerSettings (dict) -- Settings specific to the container type of the file.
    M2tsSettings (dict) -- Placeholder documentation for M2tsSettings
    AbsentInputAudioBehavior (string) -- When set to drop, output audio streams will be removed from the program if the selected input audio stream is removed from the input. This allows the output audio configuration to dynamically change based on input configuration. If this is set to encodeSilence, all output audio streams will output encoded silence when not connected to an active input stream.
    Arib (string) -- When set to enabled, uses ARIB-compliant field muxing and removes video descriptor.
    AribCaptionsPid (string) -- Packet Identifier (PID) for ARIB Captions in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    AribCaptionsPidControl (string) -- If set to auto, pid number used for ARIB Captions will be auto-selected from unused pids. If set to useConfigured, ARIB Captions will be on the configured pid number.
    AudioBufferModel (string) -- When set to dvb, uses DVB buffer model for Dolby Digital audio. When set to atsc, the ATSC model is used.
    AudioFramesPerPes (integer) -- The number of audio frames to insert for each PES packet.
    AudioPids (string) -- Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
    AudioStreamType (string) -- When set to atsc, uses stream type = 0x81 for AC3 and stream type = 0x87 for EAC3. When set to dvb, uses stream type = 0x06.
    Bitrate (integer) -- The output bitrate of the transport stream in bits per second. Setting to 0 lets the muxer automatically determine the appropriate bitrate.
    BufferModel (string) -- If set to multiplex, use multiplex buffer model for accurate interleaving. Setting to bufferModel to none can lead to lower latency, but low-memory devices may not be able to play back the stream without interruptions.
    CcDescriptor (string) -- When set to enabled, generates captionServiceDescriptor in PMT.
    DvbNitSettings (dict) -- Inserts DVB Network Information Table (NIT) at the specified table repetition interval.
    NetworkId (integer) -- The numeric value placed in the Network Information Table (NIT).
    NetworkName (string) -- The network name text placed in the networkNameDescriptor inside the Network Information Table. Maximum length is 256 characters.
    RepInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream.
    
    
    DvbSdtSettings (dict) -- Inserts DVB Service Description Table (SDT) at the specified table repetition interval.
    OutputSdt (string) -- Selects method of inserting SDT information into output stream. The sdtFollow setting copies SDT information from input stream to output stream. The sdtFollowIfPresent setting copies SDT information from input stream to output stream if SDT information is present in the input, otherwise it will fall back on the user-defined values. The sdtManual setting means user will enter the SDT information. The sdtNone setting means output stream will not contain SDT information.
    RepInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream.
    ServiceName (string) -- The service name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters.
    ServiceProviderName (string) -- The service provider name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters.
    
    
    DvbSubPids (string) -- Packet Identifier (PID) for input source DVB Subtitle data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
    DvbTdtSettings (dict) -- Inserts DVB Time and Date Table (TDT) at the specified table repetition interval.
    RepInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream.
    
    
    DvbTeletextPid (string) -- Packet Identifier (PID) for input source DVB Teletext data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    Ebif (string) -- If set to passthrough, passes any EBIF data from the input source to this output.
    EbpAudioInterval (string) -- When videoAndFixedIntervals is selected, audio EBP markers will be added to partitions 3 and 4. The interval between these additional markers will be fixed, and will be slightly shorter than the video EBP marker interval. Only available when EBP Cablelabs segmentation markers are selected. Partitions 1 and 2 will always follow the video interval.
    EbpLookaheadMs (integer) -- When set, enforces that Encoder Boundary Points do not come within the specified time interval of each other by looking ahead at input video. If another EBP is going to come in within the specified time interval, the current EBP is not emitted, and the segment is "stretched" to the next marker. The lookahead value does not add latency to the system. The Live Event must be configured elsewhere to create sufficient latency to make the lookahead accurate.
    EbpPlacement (string) -- Controls placement of EBP on Audio PIDs. If set to videoAndAudioPids, EBP markers will be placed on the video PID and all audio PIDs. If set to videoPid, EBP markers will be placed on only the video PID.
    EcmPid (string) -- This field is unused and deprecated.
    EsRateInPes (string) -- Include or exclude the ES Rate field in the PES header.
    EtvPlatformPid (string) -- Packet Identifier (PID) for input source ETV Platform data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    EtvSignalPid (string) -- Packet Identifier (PID) for input source ETV Signal data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    FragmentTime (float) -- The length in seconds of each fragment. Only used with EBP markers.
    Klv (string) -- If set to passthrough, passes any KLV data from the input source to this output.
    KlvDataPids (string) -- Packet Identifier (PID) for input source KLV data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
    NullPacketBitrate (float) -- Value in bits per second of extra null packets to insert into the transport stream. This can be used if a downstream encryption system requires periodic null packets.
    PatInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000.
    PcrControl (string) -- When set to pcrEveryPesPacket, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream.
    PcrPeriod (integer) -- Maximum time in milliseconds between Program Clock Reference (PCRs) inserted into the transport stream.
    PcrPid (string) -- Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    PmtInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000.
    PmtPid (string) -- Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    ProgramNum (integer) -- The value of the program number field in the Program Map Table.
    RateMode (string) -- When vbr, does not insert null packets into transport stream to fill specified bitrate. The bitrate setting acts as the maximum bitrate when vbr is set.
    Scte27Pids (string) -- Packet Identifier (PID) for input source SCTE-27 data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
    Scte35Control (string) -- Optionally pass SCTE-35 signals from the input source to this output.
    Scte35Pid (string) -- Packet Identifier (PID) of the SCTE-35 stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    SegmentationMarkers (string) -- Inserts segmentation markers at each segmentationTime period. raiSegstart sets the Random Access Indicator bit in the adaptation field. raiAdapt sets the RAI bit and adds the current timecode in the private data bytes. psiSegstart inserts PAT and PMT tables at the start of segments. ebp adds Encoder Boundary Point information to the adaptation field as per OpenCable specification OC-SP-EBP-I01-130118. ebpLegacy adds Encoder Boundary Point information to the adaptation field using a legacy proprietary format.
    SegmentationStyle (string) -- The segmentation style parameter controls how segmentation markers are inserted into the transport stream. With avails, it is possible that segments may be truncated, which can influence where future segmentation markers are inserted. When a segmentation style of "resetCadence" is selected and a segment is truncated due to an avail, we will reset the segmentation cadence. This means the subsequent segment will have a duration of $segmentationTime seconds. When a segmentation style of "maintainCadence" is selected and a segment is truncated due to an avail, we will not reset the segmentation cadence. This means the subsequent segment will likely be truncated as well. However, all segments after that will have a duration of $segmentationTime seconds. Note that EBP lookahead is a slight exception to this rule.
    SegmentationTime (float) -- The length in seconds of each segment. Required unless markers is set to None_.
    TimedMetadataBehavior (string) -- When set to passthrough, timed metadata will be passed through from input to output.
    TimedMetadataPid (string) -- Packet Identifier (PID) of the timed metadata stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    TransportStreamId (integer) -- The value of the transport stream ID field in the Program Map Table.
    VideoPid (string) -- Packet Identifier (PID) of the elementary video stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    
    
    
    
    Extension (string) -- Output file extension. If excluded, this will be auto-selected from the container type.
    NameModifier (string) -- String concatenated to the end of the destination filename. Required for multiple outputs of the same type.
    
    
    HlsOutputSettings (dict) -- Placeholder documentation for HlsOutputSettings
    HlsSettings (dict) -- Settings regarding the underlying stream. These settings are different for audio-only outputs.
    AudioOnlyHlsSettings (dict) -- Placeholder documentation for AudioOnlyHlsSettings
    AudioGroupId (string) -- Specifies the group to which the audio Rendition belongs.
    AudioOnlyImage (dict) -- For use with an audio only Stream. Must be a .jpg or .png file. If given, this image will be used as the cover-art for the audio only output. Ideally, it should be formatted for an iPhone screen for two reasons. The iPhone does not resize the image, it crops a centered image on the top/bottom and left/right. Additionally, this image file gets saved bit-for-bit into every 10-second segment file, so will increase bandwidth by {image file size} * {segment count} * {user count.}.
    PasswordParam (string) -- key used to extract the password from EC2 Parameter store
    Uri (string) -- Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: "rtmp://fmsserver/live".
    Username (string) -- Documentation update needed
    
    
    AudioTrackType (string) -- Four types of audio-only tracks are supported: Audio-Only Variant Stream The client can play back this audio-only stream instead of video in low-bandwidth scenarios. Represented as an EXT-X-STREAM-INF in the HLS manifest. Alternate Audio, Auto Select, Default Alternate rendition that the client should try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=YES, AUTOSELECT=YES Alternate Audio, Auto Select, Not Default Alternate rendition that the client may try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=YES Alternate Audio, not Auto Select Alternate rendition that the client will not try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=NO
    
    
    StandardHlsSettings (dict) -- Placeholder documentation for StandardHlsSettings
    AudioRenditionSets (string) -- List all the audio groups that are used with the video output stream. Input all the audio GROUP-IDs that are associated to the video, separate by ','.
    M3u8Settings (dict) -- Settings information for the .m3u8 container
    AudioFramesPerPes (integer) -- The number of audio frames to insert for each PES packet.
    AudioPids (string) -- Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values.
    EcmPid (string) -- This parameter is unused and deprecated.
    PatInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream. A value of "0" writes out the PMT once per segment file.
    PcrControl (string) -- When set to pcrEveryPesPacket, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream.
    PcrPeriod (integer) -- Maximum time in milliseconds between Program Clock References (PCRs) inserted into the transport stream.
    PcrPid (string) -- Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID. Can be entered as a decimal or hexadecimal value.
    PmtInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream. A value of "0" writes out the PMT once per segment file.
    PmtPid (string) -- Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream. Can be entered as a decimal or hexadecimal value.
    ProgramNum (integer) -- The value of the program number field in the Program Map Table.
    Scte35Behavior (string) -- If set to passthrough, passes any SCTE-35 signals from the input source to this output.
    Scte35Pid (string) -- Packet Identifier (PID) of the SCTE-35 stream in the transport stream. Can be entered as a decimal or hexadecimal value.
    TimedMetadataBehavior (string) -- When set to passthrough, timed metadata is passed through from input to output.
    TimedMetadataPid (string) -- Packet Identifier (PID) of the timed metadata stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    TransportStreamId (integer) -- The value of the transport stream ID field in the Program Map Table.
    VideoPid (string) -- Packet Identifier (PID) of the elementary video stream in the transport stream. Can be entered as a decimal or hexadecimal value.
    
    
    
    
    
    
    NameModifier (string) -- String concatenated to the end of the destination filename. Accepts "Format Identifiers":#formatIdentifierParameters.
    SegmentModifier (string) -- String concatenated to end of segment filenames.
    
    
    MsSmoothOutputSettings (dict) -- Placeholder documentation for MsSmoothOutputSettings
    NameModifier (string) -- String concatenated to the end of the destination filename. Required for multiple outputs of the same type.
    
    
    RtmpOutputSettings (dict) -- Placeholder documentation for RtmpOutputSettings
    CertificateMode (string) -- If set to verifyAuthenticity, verify the tls certificate chain to a trusted Certificate Authority (CA). This will cause rtmps outputs with self-signed certificates to fail.
    ConnectionRetryInterval (integer) -- Number of seconds to wait before retrying a connection to the Flash Media server if the connection is lost.
    Destination (dict) -- The RTMP endpoint excluding the stream name (eg. rtmp://host/appname). For connection to Akamai, a username and password must be supplied. URI fields accept format identifiers.
    DestinationRefId (string) -- Placeholder documentation for __string
    
    
    NumRetries (integer) -- Number of retry attempts.
    
    
    UdpOutputSettings (dict) -- Placeholder documentation for UdpOutputSettings
    BufferMsec (integer) -- UDP output buffering in milliseconds. Larger values increase latency through the transcoder but simultaneously assist the transcoder in maintaining a constant, low-jitter UDP/RTP output while accommodating clock recovery, input switching, input disruptions, picture reordering, etc.
    ContainerSettings (dict) -- Placeholder documentation for UdpContainerSettings
    M2tsSettings (dict) -- Placeholder documentation for M2tsSettings
    AbsentInputAudioBehavior (string) -- When set to drop, output audio streams will be removed from the program if the selected input audio stream is removed from the input. This allows the output audio configuration to dynamically change based on input configuration. If this is set to encodeSilence, all output audio streams will output encoded silence when not connected to an active input stream.
    Arib (string) -- When set to enabled, uses ARIB-compliant field muxing and removes video descriptor.
    AribCaptionsPid (string) -- Packet Identifier (PID) for ARIB Captions in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    AribCaptionsPidControl (string) -- If set to auto, pid number used for ARIB Captions will be auto-selected from unused pids. If set to useConfigured, ARIB Captions will be on the configured pid number.
    AudioBufferModel (string) -- When set to dvb, uses DVB buffer model for Dolby Digital audio. When set to atsc, the ATSC model is used.
    AudioFramesPerPes (integer) -- The number of audio frames to insert for each PES packet.
    AudioPids (string) -- Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
    AudioStreamType (string) -- When set to atsc, uses stream type = 0x81 for AC3 and stream type = 0x87 for EAC3. When set to dvb, uses stream type = 0x06.
    Bitrate (integer) -- The output bitrate of the transport stream in bits per second. Setting to 0 lets the muxer automatically determine the appropriate bitrate.
    BufferModel (string) -- If set to multiplex, use multiplex buffer model for accurate interleaving. Setting to bufferModel to none can lead to lower latency, but low-memory devices may not be able to play back the stream without interruptions.
    CcDescriptor (string) -- When set to enabled, generates captionServiceDescriptor in PMT.
    DvbNitSettings (dict) -- Inserts DVB Network Information Table (NIT) at the specified table repetition interval.
    NetworkId (integer) -- The numeric value placed in the Network Information Table (NIT).
    NetworkName (string) -- The network name text placed in the networkNameDescriptor inside the Network Information Table. Maximum length is 256 characters.
    RepInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream.
    
    
    DvbSdtSettings (dict) -- Inserts DVB Service Description Table (SDT) at the specified table repetition interval.
    OutputSdt (string) -- Selects method of inserting SDT information into output stream. The sdtFollow setting copies SDT information from input stream to output stream. The sdtFollowIfPresent setting copies SDT information from input stream to output stream if SDT information is present in the input, otherwise it will fall back on the user-defined values. The sdtManual setting means user will enter the SDT information. The sdtNone setting means output stream will not contain SDT information.
    RepInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream.
    ServiceName (string) -- The service name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters.
    ServiceProviderName (string) -- The service provider name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters.
    
    
    DvbSubPids (string) -- Packet Identifier (PID) for input source DVB Subtitle data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
    DvbTdtSettings (dict) -- Inserts DVB Time and Date Table (TDT) at the specified table repetition interval.
    RepInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream.
    
    
    DvbTeletextPid (string) -- Packet Identifier (PID) for input source DVB Teletext data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    Ebif (string) -- If set to passthrough, passes any EBIF data from the input source to this output.
    EbpAudioInterval (string) -- When videoAndFixedIntervals is selected, audio EBP markers will be added to partitions 3 and 4. The interval between these additional markers will be fixed, and will be slightly shorter than the video EBP marker interval. Only available when EBP Cablelabs segmentation markers are selected. Partitions 1 and 2 will always follow the video interval.
    EbpLookaheadMs (integer) -- When set, enforces that Encoder Boundary Points do not come within the specified time interval of each other by looking ahead at input video. If another EBP is going to come in within the specified time interval, the current EBP is not emitted, and the segment is "stretched" to the next marker. The lookahead value does not add latency to the system. The Live Event must be configured elsewhere to create sufficient latency to make the lookahead accurate.
    EbpPlacement (string) -- Controls placement of EBP on Audio PIDs. If set to videoAndAudioPids, EBP markers will be placed on the video PID and all audio PIDs. If set to videoPid, EBP markers will be placed on only the video PID.
    EcmPid (string) -- This field is unused and deprecated.
    EsRateInPes (string) -- Include or exclude the ES Rate field in the PES header.
    EtvPlatformPid (string) -- Packet Identifier (PID) for input source ETV Platform data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    EtvSignalPid (string) -- Packet Identifier (PID) for input source ETV Signal data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    FragmentTime (float) -- The length in seconds of each fragment. Only used with EBP markers.
    Klv (string) -- If set to passthrough, passes any KLV data from the input source to this output.
    KlvDataPids (string) -- Packet Identifier (PID) for input source KLV data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
    NullPacketBitrate (float) -- Value in bits per second of extra null packets to insert into the transport stream. This can be used if a downstream encryption system requires periodic null packets.
    PatInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000.
    PcrControl (string) -- When set to pcrEveryPesPacket, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream.
    PcrPeriod (integer) -- Maximum time in milliseconds between Program Clock Reference (PCRs) inserted into the transport stream.
    PcrPid (string) -- Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    PmtInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000.
    PmtPid (string) -- Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    ProgramNum (integer) -- The value of the program number field in the Program Map Table.
    RateMode (string) -- When vbr, does not insert null packets into transport stream to fill specified bitrate. The bitrate setting acts as the maximum bitrate when vbr is set.
    Scte27Pids (string) -- Packet Identifier (PID) for input source SCTE-27 data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
    Scte35Control (string) -- Optionally pass SCTE-35 signals from the input source to this output.
    Scte35Pid (string) -- Packet Identifier (PID) of the SCTE-35 stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    SegmentationMarkers (string) -- Inserts segmentation markers at each segmentationTime period. raiSegstart sets the Random Access Indicator bit in the adaptation field. raiAdapt sets the RAI bit and adds the current timecode in the private data bytes. psiSegstart inserts PAT and PMT tables at the start of segments. ebp adds Encoder Boundary Point information to the adaptation field as per OpenCable specification OC-SP-EBP-I01-130118. ebpLegacy adds Encoder Boundary Point information to the adaptation field using a legacy proprietary format.
    SegmentationStyle (string) -- The segmentation style parameter controls how segmentation markers are inserted into the transport stream. With avails, it is possible that segments may be truncated, which can influence where future segmentation markers are inserted. When a segmentation style of "resetCadence" is selected and a segment is truncated due to an avail, we will reset the segmentation cadence. This means the subsequent segment will have a duration of $segmentationTime seconds. When a segmentation style of "maintainCadence" is selected and a segment is truncated due to an avail, we will not reset the segmentation cadence. This means the subsequent segment will likely be truncated as well. However, all segments after that will have a duration of $segmentationTime seconds. Note that EBP lookahead is a slight exception to this rule.
    SegmentationTime (float) -- The length in seconds of each segment. Required unless markers is set to None_.
    TimedMetadataBehavior (string) -- When set to passthrough, timed metadata will be passed through from input to output.
    TimedMetadataPid (string) -- Packet Identifier (PID) of the timed metadata stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    TransportStreamId (integer) -- The value of the transport stream ID field in the Program Map Table.
    VideoPid (string) -- Packet Identifier (PID) of the elementary video stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    
    
    
    
    Destination (dict) -- Destination address and port number for RTP or UDP packets. Can be unicast or multicast RTP or UDP (eg. rtp://239.10.10.10:5001 or udp://10.100.100.100:5002).
    DestinationRefId (string) -- Placeholder documentation for __string
    
    
    FecOutputSettings (dict) -- Settings for enabling and adjusting Forward Error Correction on UDP outputs.
    ColumnDepth (integer) -- Parameter D from SMPTE 2022-1. The height of the FEC protection matrix. The number of transport stream packets per column error correction packet. Must be between 4 and 20, inclusive.
    IncludeFec (string) -- Enables column only or column and row based FEC
    RowLength (integer) -- Parameter L from SMPTE 2022-1. The width of the FEC protection matrix. Must be between 1 and 20, inclusive. If only Column FEC is used, then larger values increase robustness. If Row FEC is used, then this is the number of transport stream packets per row error correction packet, and the value must be between 4 and 20, inclusive, if includeFec is columnAndRow. If includeFec is column, this value must be 1 to 20, inclusive.
    
    
    
    
    
    
    VideoDescriptionName (string) -- The name of the VideoDescription used as the source for this output.
    
    
    
    
    
    
    
    
    TimecodeConfig (dict) -- Contains settings used to acquire and adjust timecode information from inputs.
    Source (string) -- Identifies the source for the timecode that will be associated with the events outputs. -Embedded (embedded): Initialize the output timecode with timecode from the the source. If no embedded timecode is detected in the source, the system falls back to using "Start at 0" (zerobased). -System Clock (systemclock): Use the UTC time. -Start at 0 (zerobased): The time of the first frame of the event will be 00:00:00:00.
    SyncThreshold (integer) -- Threshold in frames beyond which output timecode is resynchronized to the input timecode. Discrepancies below this threshold are permitted to avoid unnecessary discontinuities in the output timecode. No timecode sync when this is not specified.
    
    
    VideoDescriptions (list) -- Placeholder documentation for __listOfVideoDescription
    (dict) -- Video settings for this stream.
    CodecSettings (dict) -- Video codec settings.
    H264Settings (dict) -- Placeholder documentation for H264Settings
    AdaptiveQuantization (string) -- Adaptive quantization. Allows intra-frame quantizers to vary to improve visual quality.
    AfdSignaling (string) -- Indicates that AFD values will be written into the output stream. If afdSignaling is "auto", the system will try to preserve the input AFD value (in cases where multiple AFD values are valid). If set to "fixed", the AFD value will be the value configured in the fixedAfd parameter.
    Bitrate (integer) -- Average bitrate in bits/second. Required when the rate control mode is VBR or CBR. Not used for QVBR. In an MS Smooth output group, each output must have a unique value when its bitrate is rounded down to the nearest multiple of 1000.
    BufFillPct (integer) -- Percentage of the buffer that should initially be filled (HRD buffer model).
    BufSize (integer) -- Size of buffer (HRD buffer model) in bits/second.
    ColorMetadata (string) -- Includes colorspace metadata in the output.
    EntropyEncoding (string) -- Entropy encoding mode. Use cabac (must be in Main or High profile) or cavlc.
    FixedAfd (string) -- Four bit AFD value to write on all frames of video in the output stream. Only valid when afdSignaling is set to 'Fixed'.
    FlickerAq (string) -- If set to enabled, adjust quantization within each frame to reduce flicker or 'pop' on I-frames.
    FramerateControl (string) -- This field indicates how the output video frame rate is specified. If "specified" is selected then the output video frame rate is determined by framerateNumerator and framerateDenominator, else if "initializeFromSource" is selected then the output video frame rate will be set equal to the input video frame rate of the first input.
    FramerateDenominator (integer) -- Framerate denominator.
    FramerateNumerator (integer) -- Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976 fps.
    GopBReference (string) -- Documentation update needed
    GopClosedCadence (integer) -- Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting.
    GopNumBFrames (integer) -- Number of B-frames between reference frames.
    GopSize (float) -- GOP size (keyframe interval) in units of either frames or seconds per gopSizeUnits. Must be greater than zero.
    GopSizeUnits (string) -- Indicates if the gopSize is specified in frames or seconds. If seconds the system will convert the gopSize into a frame count at run time.
    Level (string) -- H.264 Level.
    LookAheadRateControl (string) -- Amount of lookahead. A value of low can decrease latency and memory usage, while high can produce better quality for certain content.
    MaxBitrate (integer) -- For QVBR: See the tooltip for Quality level For VBR: Set the maximum bitrate in order to accommodate expected spikes in the complexity of the video.
    MinIInterval (integer) -- Only meaningful if sceneChangeDetect is set to enabled. Enforces separation between repeated (cadence) I-frames and I-frames inserted by Scene Change Detection. If a scene change I-frame is within I-interval frames of a cadence I-frame, the GOP is shrunk and/or stretched to the scene change I-frame. GOP stretch requires enabling lookahead as well as setting I-interval. The normal cadence resumes for the next GOP. Note: Maximum GOP stretch = GOP size + Min-I-interval - 1
    NumRefFrames (integer) -- Number of reference frames to use. The encoder may use more than requested if using B-frames and/or interlaced encoding.
    ParControl (string) -- This field indicates how the output pixel aspect ratio is specified. If "specified" is selected then the output video pixel aspect ratio is determined by parNumerator and parDenominator, else if "initializeFromSource" is selected then the output pixsel aspect ratio will be set equal to the input video pixel aspect ratio of the first input.
    ParDenominator (integer) -- Pixel Aspect Ratio denominator.
    ParNumerator (integer) -- Pixel Aspect Ratio numerator.
    Profile (string) -- H.264 Profile.
    QvbrQualityLevel (integer) -- Controls the target quality for the video encode. Applies only when the rate control mode is QVBR. Set values for the QVBR quality level field and Max bitrate field that suit your most important viewing devices. Recommended values are: - Primary screen: Quality level: 8 to 10. Max bitrate: 4M - PC or tablet: Quality level: 7. Max bitrate: 1.5M to 3M - Smartphone: Quality level: 6. Max bitrate: 1M to 1.5M
    RateControlMode (string) -- Rate control mode. QVBR: Quality will match the specified quality level except when it is constrained by the maximum bitrate. Recommended if you or your viewers pay for bandwidth. VBR: Quality and bitrate vary, depending on the video complexity. Recommended instead of QVBR if you want to maintain a specific average bitrate over the duration of the channel. CBR: Quality varies, depending on the video complexity. Recommended only if you distribute your assets to devices that cannot handle variable bitrates.
    ScanType (string) -- Sets the scan type of the output to progressive or top-field-first interlaced.
    SceneChangeDetect (string) -- Scene change detection. - On: inserts I-frames when scene change is detected. - Off: does not force an I-frame when scene change is detected.
    Slices (integer) -- Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures. This field is optional; when no value is specified the encoder will choose the number of slices based on encode resolution.
    Softness (integer) -- Softness. Selects quantizer matrix, larger values reduce high-frequency content in the encoded image.
    SpatialAq (string) -- If set to enabled, adjust quantization within each frame based on spatial variation of content complexity.
    SubgopLength (string) -- If set to fixed, use gopNumBFrames B-frames per sub-GOP. If set to dynamic, optimize the number of B-frames used for each sub-GOP to improve visual quality.
    Syntax (string) -- Produces a bitstream compliant with SMPTE RP-2027.
    TemporalAq (string) -- If set to enabled, adjust quantization within each frame based on temporal variation of content complexity.
    TimecodeInsertion (string) -- Determines how timecodes should be inserted into the video elementary stream. - 'disabled': Do not include timecodes - 'picTimingSei': Pass through picture timing SEI messages from the source specified in Timecode Config
    
    
    
    
    Height (integer) -- Output video height (in pixels). Leave blank to use source video height. If left blank, width must also be unspecified.
    Name (string) -- The name of this VideoDescription. Outputs will use this name to uniquely identify this Description. Description names should be unique within this Live Event.
    RespondToAfd (string) -- Indicates how to respond to the AFD values in the input stream. Setting to "respond" causes input video to be clipped, depending on AFD value, input display aspect ratio and output display aspect ratio.
    ScalingBehavior (string) -- When set to "stretchToOutput", automatically configures the output position to stretch the video to the specified output resolution. This option will override any position value.
    Sharpness (integer) -- Changes the width of the anti-alias filter kernel used for scaling. Only applies if scaling is being performed and antiAlias is set to true. 0 is the softest setting, 100 the sharpest, and 50 recommended for most content.
    Width (integer) -- Output video width (in pixels). Leave out to use source video width. If left out, height must also be left out. Display aspect ratio is always preserved by letterboxing or pillarboxing when necessary.
    
    
    
    
    
    
    Id (string) -- The unique id of the channel.
    InputAttachments (list) -- List of input attachments for channel.
    (dict) -- Placeholder documentation for InputAttachment
    InputAttachmentName (string) -- User-specified name for the attachment. This is required if the user wants to use this input in an input switch action.
    InputId (string) -- The ID of the input
    InputSettings (dict) -- Settings of an input (caption selector, etc.)
    AudioSelectors (list) -- Used to select the audio stream to decode for inputs that have multiple available.
    (dict) -- Placeholder documentation for AudioSelector
    Name (string) -- The name of this AudioSelector. AudioDescriptions will use this name to uniquely identify this Selector. Selector names should be unique per input.
    SelectorSettings (dict) -- The audio selector settings.
    AudioLanguageSelection (dict) -- Placeholder documentation for AudioLanguageSelection
    LanguageCode (string) -- Selects a specific three-letter language code from within an audio source.
    LanguageSelectionPolicy (string) -- When set to "strict", the transport stream demux strictly identifies audio streams by their language descriptor. If a PMT update occurs such that an audio stream matching the initially selected language is no longer present then mute will be encoded until the language returns. If "loose", then on a PMT update the demux will choose another audio stream in the program with the same stream type if it can't find one with the same language.
    
    
    AudioPidSelection (dict) -- Placeholder documentation for AudioPidSelection
    Pid (integer) -- Selects a specific PID from within a source.
    
    
    
    
    
    
    
    
    CaptionSelectors (list) -- Used to select the caption input to use for inputs that have multiple available.
    (dict) -- Output groups for this Live Event. Output groups contain information about where streams should be distributed.
    LanguageCode (string) -- When specified this field indicates the three letter language code of the caption track to extract from the source.
    Name (string) -- Name identifier for a caption selector. This name is used to associate this caption selector with one or more caption descriptions. Names must be unique within an event.
    SelectorSettings (dict) -- Caption selector settings.
    AribSourceSettings (dict) -- Placeholder documentation for AribSourceSettings
    DvbSubSourceSettings (dict) -- Placeholder documentation for DvbSubSourceSettings
    Pid (integer) -- When using DVB-Sub with Burn-In or SMPTE-TT, use this PID for the source content. Unused for DVB-Sub passthrough. All DVB-Sub content is passed through, regardless of selectors.
    
    
    EmbeddedSourceSettings (dict) -- Placeholder documentation for EmbeddedSourceSettings
    Convert608To708 (string) -- If upconvert, 608 data is both passed through via the "608 compatibility bytes" fields of the 708 wrapper as well as translated into 708. 708 data present in the source content will be discarded.
    Scte20Detection (string) -- Set to "auto" to handle streams with intermittent and/or non-aligned SCTE-20 and Embedded captions.
    Source608ChannelNumber (integer) -- Specifies the 608/708 channel number within the video track from which to extract captions. Unused for passthrough.
    Source608TrackNumber (integer) -- This field is unused and deprecated.
    
    
    Scte20SourceSettings (dict) -- Placeholder documentation for Scte20SourceSettings
    Convert608To708 (string) -- If upconvert, 608 data is both passed through via the "608 compatibility bytes" fields of the 708 wrapper as well as translated into 708. 708 data present in the source content will be discarded.
    Source608ChannelNumber (integer) -- Specifies the 608/708 channel number within the video track from which to extract captions. Unused for passthrough.
    
    
    Scte27SourceSettings (dict) -- Placeholder documentation for Scte27SourceSettings
    Pid (integer) -- The pid field is used in conjunction with the caption selector languageCode field as follows: - Specify PID and Language: Extracts captions from that PID; the language is "informational". - Specify PID and omit Language: Extracts the specified PID. - Omit PID and specify Language: Extracts the specified language, whichever PID that happens to be. - Omit PID and omit Language: Valid only if source is DVB-Sub that is being passed through; all languages will be passed through.
    
    
    TeletextSourceSettings (dict) -- Placeholder documentation for TeletextSourceSettings
    PageNumber (string) -- Specifies the teletext page number within the data stream from which to extract captions. Range of 0x100 (256) to 0x8FF (2303). Unused for passthrough. Should be specified as a hexadecimal string with no "0x" prefix.
    
    
    
    
    
    
    
    
    DeblockFilter (string) -- Enable or disable the deblock filter when filtering.
    DenoiseFilter (string) -- Enable or disable the denoise filter when filtering.
    FilterStrength (integer) -- Adjusts the magnitude of filtering from 1 (minimal) to 5 (strongest).
    InputFilter (string) -- Turns on the filter for this input. MPEG-2 inputs have the deblocking filter enabled by default. 1) auto - filtering will be applied depending on input type/quality 2) disabled - no filtering will be applied to the input 3) forced - filtering will be applied regardless of input type
    NetworkInputSettings (dict) -- Input settings.
    HlsInputSettings (dict) -- Specifies HLS input settings when the uri is for a HLS manifest.
    Bandwidth (integer) -- When specified the HLS stream with the m3u8 BANDWIDTH that most closely matches this value will be chosen, otherwise the highest bandwidth stream in the m3u8 will be chosen. The bitrate is specified in bits per second, as in an HLS manifest.
    BufferSegments (integer) -- When specified, reading of the HLS input will begin this many buffer segments from the end (most recently written segment). When not specified, the HLS input will begin with the first segment specified in the m3u8.
    Retries (integer) -- The number of consecutive times that attempts to read a manifest or segment must fail before the input is considered unavailable.
    RetryInterval (integer) -- The number of seconds between retries when an attempt to read a manifest or segment fails.
    
    
    ServerValidation (string) -- Check HTTPS server certificates. When set to checkCryptographyOnly, cryptography in the certificate will be checked, but not the server's name. Certain subdomains (notably S3 buckets that use dots in the bucket name) do not strictly match the corresponding certificate's wildcard pattern and would otherwise cause the event to error. This setting is ignored for protocols that do not use https.
    
    
    SourceEndBehavior (string) -- Loop input if it is a file. This allows a file input to be streamed indefinitely.
    VideoSelector (dict) -- Informs which video elementary stream to decode for input types that have multiple available.
    ColorSpace (string) -- Specifies the colorspace of an input. This setting works in tandem with colorSpaceConversion to determine if any conversion will be performed.
    ColorSpaceUsage (string) -- Applies only if colorSpace is a value other than follow. This field controls how the value in the colorSpace field will be used. fallback means that when the input does include color space data, that data will be used, but when the input has no color space data, the value in colorSpace will be used. Choose fallback if your input is sometimes missing color space data, but when it does have color space data, that data is correct. force means to always use the value in colorSpace. Choose force if your input usually has no color space data or might have unreliable color space data.
    SelectorSettings (dict) -- The video selector settings.
    VideoSelectorPid (dict) -- Placeholder documentation for VideoSelectorPid
    Pid (integer) -- Selects a specific PID from within a video source.
    
    
    VideoSelectorProgramId (dict) -- Placeholder documentation for VideoSelectorProgramId
    ProgramId (integer) -- Selects a specific program from within a multi-program transport stream. If the program doesn't exist, the first program within the transport stream will be selected by default.
    
    
    
    
    
    
    
    
    
    
    
    
    InputSpecification (dict) -- Placeholder documentation for InputSpecification
    Codec (string) -- Input codec
    MaximumBitrate (string) -- Maximum input bitrate, categorized coarsely
    Resolution (string) -- Input resolution, categorized coarsely
    
    
    LogLevel (string) -- The log level being written to CloudWatch Logs.
    Name (string) -- The name of the channel. (user-mutable)
    PipelinesRunningCount (integer) -- The number of currently healthy pipelines.
    RoleArn (string) -- The Amazon Resource Name (ARN) of the role assumed when running the Channel.
    State (string) -- Placeholder documentation for ChannelState
    
    
    
    
    
    """
    pass

def create_input(Destinations=None, InputSecurityGroups=None, MediaConnectFlows=None, Name=None, RequestId=None, RoleArn=None, Sources=None, Type=None):
    """
    Create an input
    See also: AWS API Documentation
    
    
    :example: response = client.create_input(
        Destinations=[
            {
                'StreamName': 'string'
            },
        ],
        InputSecurityGroups=[
            'string',
        ],
        MediaConnectFlows=[
            {
                'FlowArn': 'string'
            },
        ],
        Name='string',
        RequestId='string',
        RoleArn='string',
        Sources=[
            {
                'PasswordParam': 'string',
                'Url': 'string',
                'Username': 'string'
            },
        ],
        Type='UDP_PUSH'|'RTP_PUSH'|'RTMP_PUSH'|'RTMP_PULL'|'URL_PULL'|'MP4_FILE'|'MEDIACONNECT'
    )
    
    
    :type Destinations: list
    :param Destinations: Destination settings for PUSH type inputs.
            (dict) -- Endpoint settings for a PUSH type input.
            StreamName (string) -- A unique name for the location the RTMP stream is being pushed to.
            

    :type InputSecurityGroups: list
    :param InputSecurityGroups: A list of security groups referenced by IDs to attach to the input.
            (string) -- Placeholder documentation for __string
            

    :type MediaConnectFlows: list
    :param MediaConnectFlows: A list of the MediaConnect Flows that you want to use in this input. You can specify as few as one Flow and presently, as many as two. The only requirement is when you have more than one is that each Flow is in a separate Availability Zone as this ensures your EML input is redundant to AZ issues.
            (dict) -- The settings for a MediaConnect Flow.
            FlowArn (string) -- The ARN of the MediaConnect Flow that you want to use as a source.
            

    :type Name: string
    :param Name: Name of the input.

    :type RequestId: string
    :param RequestId: Unique identifier of the request to ensure the request is handled exactly once in case of retries. This field is autopopulated if not provided.

    :type RoleArn: string
    :param RoleArn: The Amazon Resource Name (ARN) of the role this input assumes during and after creation.

    :type Sources: list
    :param Sources: The source URLs for a PULL-type input. Every PULL type input needs exactly two source URLs for redundancy. Only specify sources for PULL type Inputs. Leave Destinations empty.
            (dict) -- Settings for for a PULL type input.
            PasswordParam (string) -- The key used to extract the password from EC2 Parameter store.
            Url (string) -- This represents the customer's source URL where stream is pulled from.
            Username (string) -- The username for the input source.
            

    :type Type: string
    :param Type: Placeholder documentation for InputType

    :rtype: dict
    :return: {
        'Input': {
            'Arn': 'string',
            'AttachedChannels': [
                'string',
            ],
            'Destinations': [
                {
                    'Ip': 'string',
                    'Port': 'string',
                    'Url': 'string'
                },
            ],
            'Id': 'string',
            'MediaConnectFlows': [
                {
                    'FlowArn': 'string'
                },
            ],
            'Name': 'string',
            'RoleArn': 'string',
            'SecurityGroups': [
                'string',
            ],
            'Sources': [
                {
                    'PasswordParam': 'string',
                    'Url': 'string',
                    'Username': 'string'
                },
            ],
            'State': 'CREATING'|'DETACHED'|'ATTACHED'|'DELETING'|'DELETED',
            'Type': 'UDP_PUSH'|'RTP_PUSH'|'RTMP_PUSH'|'RTMP_PULL'|'URL_PULL'|'MP4_FILE'|'MEDIACONNECT'
        }
    }
    
    
    :returns: 
    (dict) -- Successfully created the input.
    Input (dict) -- Placeholder documentation for Input
    Arn (string) -- The Unique ARN of the input (generated, immutable).
    AttachedChannels (list) -- A list of channel IDs that that input is attached to (currently an input can only be attached to one channel).
    (string) -- Placeholder documentation for __string
    
    
    Destinations (list) -- A list of the destinations of the input (PUSH-type).
    (dict) -- The settings for a PUSH type input.
    Ip (string) -- The system-generated static IP address of endpoint. It remains fixed for the lifetime of the input.
    Port (string) -- The port number for the input.
    Url (string) -- This represents the endpoint that the customer stream will be pushed to.
    
    
    
    
    Id (string) -- The generated ID of the input (unique for user account, immutable).
    MediaConnectFlows (list) -- A list of MediaConnect Flows for this input.
    (dict) -- The settings for a MediaConnect Flow.
    FlowArn (string) -- The unique ARN of the MediaConnect Flow being used as a source.
    
    
    
    
    Name (string) -- The user-assigned name (This is a mutable value).
    RoleArn (string) -- The Amazon Resource Name (ARN) of the role this input assumes during and after creation.
    SecurityGroups (list) -- A list of IDs for all the security groups attached to the input.
    (string) -- Placeholder documentation for __string
    
    
    Sources (list) -- A list of the sources of the input (PULL-type).
    (dict) -- The settings for a PULL type input.
    PasswordParam (string) -- The key used to extract the password from EC2 Parameter store.
    Url (string) -- This represents the customer's source URL where stream is pulled from.
    Username (string) -- The username for the input source.
    
    
    
    
    State (string) -- Placeholder documentation for InputState
    Type (string) -- Placeholder documentation for InputType
    
    
    
    
    
    """
    pass

def create_input_security_group(WhitelistRules=None):
    """
    Creates a Input Security Group
    See also: AWS API Documentation
    
    
    :example: response = client.create_input_security_group(
        WhitelistRules=[
            {
                'Cidr': 'string'
            },
        ]
    )
    
    
    :type WhitelistRules: list
    :param WhitelistRules: List of IPv4 CIDR addresses to whitelist
            (dict) -- An IPv4 CIDR to whitelist.
            Cidr (string) -- The IPv4 CIDR to whitelist.
            

    :rtype: dict
    :return: {
        'SecurityGroup': {
            'Arn': 'string',
            'Id': 'string',
            'Inputs': [
                'string',
            ],
            'State': 'IDLE'|'IN_USE'|'UPDATING'|'DELETED',
            'WhitelistRules': [
                {
                    'Cidr': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    (dict) -- Successfully created the Input Security Group.
    SecurityGroup (dict) -- An Input Security Group
    Arn (string) -- Unique ARN of Input Security Group
    Id (string) -- The Id of the Input Security Group
    Inputs (list) -- The list of inputs currently using this Input Security Group.
    (string) -- Placeholder documentation for __string
    
    
    State (string) -- The current state of the Input Security Group.
    WhitelistRules (list) -- Whitelist rules and their sync status
    (dict) -- Whitelist rule
    Cidr (string) -- The IPv4 CIDR that's whitelisted.
    
    
    
    
    
    
    
    
    
    """
    pass

def delete_channel(ChannelId=None):
    """
    Starts deletion of channel. The associated outputs are also deleted.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_channel(
        ChannelId='string'
    )
    
    
    :type ChannelId: string
    :param ChannelId: [REQUIRED] Unique ID of the channel.

    :rtype: dict
    :return: {
        'Arn': 'string',
        'Destinations': [
            {
                'Id': 'string',
                'Settings': [
                    {
                        'PasswordParam': 'string',
                        'StreamName': 'string',
                        'Url': 'string',
                        'Username': 'string'
                    },
                ]
            },
        ],
        'EgressEndpoints': [
            {
                'SourceIp': 'string'
            },
        ],
        'EncoderSettings': {
            'AudioDescriptions': [
                {
                    'AudioNormalizationSettings': {
                        'Algorithm': 'ITU_1770_1'|'ITU_1770_2',
                        'AlgorithmControl': 'CORRECT_AUDIO',
                        'TargetLkfs': 123.0
                    },
                    'AudioSelectorName': 'string',
                    'AudioType': 'CLEAN_EFFECTS'|'HEARING_IMPAIRED'|'UNDEFINED'|'VISUAL_IMPAIRED_COMMENTARY',
                    'AudioTypeControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                    'CodecSettings': {
                        'AacSettings': {
                            'Bitrate': 123.0,
                            'CodingMode': 'AD_RECEIVER_MIX'|'CODING_MODE_1_0'|'CODING_MODE_1_1'|'CODING_MODE_2_0'|'CODING_MODE_5_1',
                            'InputType': 'BROADCASTER_MIXED_AD'|'NORMAL',
                            'Profile': 'HEV1'|'HEV2'|'LC',
                            'RateControlMode': 'CBR'|'VBR',
                            'RawFormat': 'LATM_LOAS'|'NONE',
                            'SampleRate': 123.0,
                            'Spec': 'MPEG2'|'MPEG4',
                            'VbrQuality': 'HIGH'|'LOW'|'MEDIUM_HIGH'|'MEDIUM_LOW'
                        },
                        'Ac3Settings': {
                            'Bitrate': 123.0,
                            'BitstreamMode': 'COMMENTARY'|'COMPLETE_MAIN'|'DIALOGUE'|'EMERGENCY'|'HEARING_IMPAIRED'|'MUSIC_AND_EFFECTS'|'VISUALLY_IMPAIRED'|'VOICE_OVER',
                            'CodingMode': 'CODING_MODE_1_0'|'CODING_MODE_1_1'|'CODING_MODE_2_0'|'CODING_MODE_3_2_LFE',
                            'Dialnorm': 123,
                            'DrcProfile': 'FILM_STANDARD'|'NONE',
                            'LfeFilter': 'DISABLED'|'ENABLED',
                            'MetadataControl': 'FOLLOW_INPUT'|'USE_CONFIGURED'
                        },
                        'Eac3Settings': {
                            'AttenuationControl': 'ATTENUATE_3_DB'|'NONE',
                            'Bitrate': 123.0,
                            'BitstreamMode': 'COMMENTARY'|'COMPLETE_MAIN'|'EMERGENCY'|'HEARING_IMPAIRED'|'VISUALLY_IMPAIRED',
                            'CodingMode': 'CODING_MODE_1_0'|'CODING_MODE_2_0'|'CODING_MODE_3_2',
                            'DcFilter': 'DISABLED'|'ENABLED',
                            'Dialnorm': 123,
                            'DrcLine': 'FILM_LIGHT'|'FILM_STANDARD'|'MUSIC_LIGHT'|'MUSIC_STANDARD'|'NONE'|'SPEECH',
                            'DrcRf': 'FILM_LIGHT'|'FILM_STANDARD'|'MUSIC_LIGHT'|'MUSIC_STANDARD'|'NONE'|'SPEECH',
                            'LfeControl': 'LFE'|'NO_LFE',
                            'LfeFilter': 'DISABLED'|'ENABLED',
                            'LoRoCenterMixLevel': 123.0,
                            'LoRoSurroundMixLevel': 123.0,
                            'LtRtCenterMixLevel': 123.0,
                            'LtRtSurroundMixLevel': 123.0,
                            'MetadataControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                            'PassthroughControl': 'NO_PASSTHROUGH'|'WHEN_POSSIBLE',
                            'PhaseControl': 'NO_SHIFT'|'SHIFT_90_DEGREES',
                            'StereoDownmix': 'DPL2'|'LO_RO'|'LT_RT'|'NOT_INDICATED',
                            'SurroundExMode': 'DISABLED'|'ENABLED'|'NOT_INDICATED',
                            'SurroundMode': 'DISABLED'|'ENABLED'|'NOT_INDICATED'
                        },
                        'Mp2Settings': {
                            'Bitrate': 123.0,
                            'CodingMode': 'CODING_MODE_1_0'|'CODING_MODE_2_0',
                            'SampleRate': 123.0
                        },
                        'PassThroughSettings': {}
                    },
                    'LanguageCode': 'string',
                    'LanguageCodeControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                    'Name': 'string',
                    'RemixSettings': {
                        'ChannelMappings': [
                            {
                                'InputChannelLevels': [
                                    {
                                        'Gain': 123,
                                        'InputChannel': 123
                                    },
                                ],
                                'OutputChannel': 123
                            },
                        ],
                        'ChannelsIn': 123,
                        'ChannelsOut': 123
                    },
                    'StreamName': 'string'
                },
            ],
            'AvailBlanking': {
                'AvailBlankingImage': {
                    'PasswordParam': 'string',
                    'Uri': 'string',
                    'Username': 'string'
                },
                'State': 'DISABLED'|'ENABLED'
            },
            'AvailConfiguration': {
                'AvailSettings': {
                    'Scte35SpliceInsert': {
                        'AdAvailOffset': 123,
                        'NoRegionalBlackoutFlag': 'FOLLOW'|'IGNORE',
                        'WebDeliveryAllowedFlag': 'FOLLOW'|'IGNORE'
                    },
                    'Scte35TimeSignalApos': {
                        'AdAvailOffset': 123,
                        'NoRegionalBlackoutFlag': 'FOLLOW'|'IGNORE',
                        'WebDeliveryAllowedFlag': 'FOLLOW'|'IGNORE'
                    }
                }
            },
            'BlackoutSlate': {
                'BlackoutSlateImage': {
                    'PasswordParam': 'string',
                    'Uri': 'string',
                    'Username': 'string'
                },
                'NetworkEndBlackout': 'DISABLED'|'ENABLED',
                'NetworkEndBlackoutImage': {
                    'PasswordParam': 'string',
                    'Uri': 'string',
                    'Username': 'string'
                },
                'NetworkId': 'string',
                'State': 'DISABLED'|'ENABLED'
            },
            'CaptionDescriptions': [
                {
                    'CaptionSelectorName': 'string',
                    'DestinationSettings': {
                        'AribDestinationSettings': {},
                        'BurnInDestinationSettings': {
                            'Alignment': 'CENTERED'|'LEFT'|'SMART',
                            'BackgroundColor': 'BLACK'|'NONE'|'WHITE',
                            'BackgroundOpacity': 123,
                            'Font': {
                                'PasswordParam': 'string',
                                'Uri': 'string',
                                'Username': 'string'
                            },
                            'FontColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                            'FontOpacity': 123,
                            'FontResolution': 123,
                            'FontSize': 'string',
                            'OutlineColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                            'OutlineSize': 123,
                            'ShadowColor': 'BLACK'|'NONE'|'WHITE',
                            'ShadowOpacity': 123,
                            'ShadowXOffset': 123,
                            'ShadowYOffset': 123,
                            'TeletextGridControl': 'FIXED'|'SCALED',
                            'XPosition': 123,
                            'YPosition': 123
                        },
                        'DvbSubDestinationSettings': {
                            'Alignment': 'CENTERED'|'LEFT'|'SMART',
                            'BackgroundColor': 'BLACK'|'NONE'|'WHITE',
                            'BackgroundOpacity': 123,
                            'Font': {
                                'PasswordParam': 'string',
                                'Uri': 'string',
                                'Username': 'string'
                            },
                            'FontColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                            'FontOpacity': 123,
                            'FontResolution': 123,
                            'FontSize': 'string',
                            'OutlineColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                            'OutlineSize': 123,
                            'ShadowColor': 'BLACK'|'NONE'|'WHITE',
                            'ShadowOpacity': 123,
                            'ShadowXOffset': 123,
                            'ShadowYOffset': 123,
                            'TeletextGridControl': 'FIXED'|'SCALED',
                            'XPosition': 123,
                            'YPosition': 123
                        },
                        'EmbeddedDestinationSettings': {},
                        'EmbeddedPlusScte20DestinationSettings': {},
                        'RtmpCaptionInfoDestinationSettings': {},
                        'Scte20PlusEmbeddedDestinationSettings': {},
                        'Scte27DestinationSettings': {},
                        'SmpteTtDestinationSettings': {},
                        'TeletextDestinationSettings': {},
                        'TtmlDestinationSettings': {
                            'StyleControl': 'PASSTHROUGH'|'USE_CONFIGURED'
                        },
                        'WebvttDestinationSettings': {}
                    },
                    'LanguageCode': 'string',
                    'LanguageDescription': 'string',
                    'Name': 'string'
                },
            ],
            'GlobalConfiguration': {
                'InitialAudioGain': 123,
                'InputEndAction': 'NONE'|'SWITCH_AND_LOOP_INPUTS',
                'InputLossBehavior': {
                    'BlackFrameMsec': 123,
                    'InputLossImageColor': 'string',
                    'InputLossImageSlate': {
                        'PasswordParam': 'string',
                        'Uri': 'string',
                        'Username': 'string'
                    },
                    'InputLossImageType': 'COLOR'|'SLATE',
                    'RepeatFrameMsec': 123
                },
                'OutputTimingSource': 'INPUT_CLOCK'|'SYSTEM_CLOCK',
                'SupportLowFramerateInputs': 'DISABLED'|'ENABLED'
            },
            'OutputGroups': [
                {
                    'Name': 'string',
                    'OutputGroupSettings': {
                        'ArchiveGroupSettings': {
                            'Destination': {
                                'DestinationRefId': 'string'
                            },
                            'RolloverInterval': 123
                        },
                        'HlsGroupSettings': {
                            'AdMarkers': [
                                'ADOBE'|'ELEMENTAL'|'ELEMENTAL_SCTE35',
                            ],
                            'BaseUrlContent': 'string',
                            'BaseUrlManifest': 'string',
                            'CaptionLanguageMappings': [
                                {
                                    'CaptionChannel': 123,
                                    'LanguageCode': 'string',
                                    'LanguageDescription': 'string'
                                },
                            ],
                            'CaptionLanguageSetting': 'INSERT'|'NONE'|'OMIT',
                            'ClientCache': 'DISABLED'|'ENABLED',
                            'CodecSpecification': 'RFC_4281'|'RFC_6381',
                            'ConstantIv': 'string',
                            'Destination': {
                                'DestinationRefId': 'string'
                            },
                            'DirectoryStructure': 'SINGLE_DIRECTORY'|'SUBDIRECTORY_PER_STREAM',
                            'EncryptionType': 'AES128'|'SAMPLE_AES',
                            'HlsCdnSettings': {
                                'HlsAkamaiSettings': {
                                    'ConnectionRetryInterval': 123,
                                    'FilecacheDuration': 123,
                                    'HttpTransferMode': 'CHUNKED'|'NON_CHUNKED',
                                    'NumRetries': 123,
                                    'RestartDelay': 123,
                                    'Salt': 'string',
                                    'Token': 'string'
                                },
                                'HlsBasicPutSettings': {
                                    'ConnectionRetryInterval': 123,
                                    'FilecacheDuration': 123,
                                    'NumRetries': 123,
                                    'RestartDelay': 123
                                },
                                'HlsMediaStoreSettings': {
                                    'ConnectionRetryInterval': 123,
                                    'FilecacheDuration': 123,
                                    'MediaStoreStorageClass': 'TEMPORAL',
                                    'NumRetries': 123,
                                    'RestartDelay': 123
                                },
                                'HlsWebdavSettings': {
                                    'ConnectionRetryInterval': 123,
                                    'FilecacheDuration': 123,
                                    'HttpTransferMode': 'CHUNKED'|'NON_CHUNKED',
                                    'NumRetries': 123,
                                    'RestartDelay': 123
                                }
                            },
                            'IndexNSegments': 123,
                            'InputLossAction': 'EMIT_OUTPUT'|'PAUSE_OUTPUT',
                            'IvInManifest': 'EXCLUDE'|'INCLUDE',
                            'IvSource': 'EXPLICIT'|'FOLLOWS_SEGMENT_NUMBER',
                            'KeepSegments': 123,
                            'KeyFormat': 'string',
                            'KeyFormatVersions': 'string',
                            'KeyProviderSettings': {
                                'StaticKeySettings': {
                                    'KeyProviderServer': {
                                        'PasswordParam': 'string',
                                        'Uri': 'string',
                                        'Username': 'string'
                                    },
                                    'StaticKeyValue': 'string'
                                }
                            },
                            'ManifestCompression': 'GZIP'|'NONE',
                            'ManifestDurationFormat': 'FLOATING_POINT'|'INTEGER',
                            'MinSegmentLength': 123,
                            'Mode': 'LIVE'|'VOD',
                            'OutputSelection': 'MANIFESTS_AND_SEGMENTS'|'SEGMENTS_ONLY',
                            'ProgramDateTime': 'EXCLUDE'|'INCLUDE',
                            'ProgramDateTimePeriod': 123,
                            'RedundantManifest': 'DISABLED'|'ENABLED',
                            'SegmentLength': 123,
                            'SegmentationMode': 'USE_INPUT_SEGMENTATION'|'USE_SEGMENT_DURATION',
                            'SegmentsPerSubdirectory': 123,
                            'StreamInfResolution': 'EXCLUDE'|'INCLUDE',
                            'TimedMetadataId3Frame': 'NONE'|'PRIV'|'TDRL',
                            'TimedMetadataId3Period': 123,
                            'TimestampDeltaMilliseconds': 123,
                            'TsFileMode': 'SEGMENTED_FILES'|'SINGLE_FILE'
                        },
                        'MsSmoothGroupSettings': {
                            'AcquisitionPointId': 'string',
                            'AudioOnlyTimecodeControl': 'PASSTHROUGH'|'USE_CONFIGURED_CLOCK',
                            'CertificateMode': 'SELF_SIGNED'|'VERIFY_AUTHENTICITY',
                            'ConnectionRetryInterval': 123,
                            'Destination': {
                                'DestinationRefId': 'string'
                            },
                            'EventId': 'string',
                            'EventIdMode': 'NO_EVENT_ID'|'USE_CONFIGURED'|'USE_TIMESTAMP',
                            'EventStopBehavior': 'NONE'|'SEND_EOS',
                            'FilecacheDuration': 123,
                            'FragmentLength': 123,
                            'InputLossAction': 'EMIT_OUTPUT'|'PAUSE_OUTPUT',
                            'NumRetries': 123,
                            'RestartDelay': 123,
                            'SegmentationMode': 'USE_INPUT_SEGMENTATION'|'USE_SEGMENT_DURATION',
                            'SendDelayMs': 123,
                            'SparseTrackType': 'NONE'|'SCTE_35',
                            'StreamManifestBehavior': 'DO_NOT_SEND'|'SEND',
                            'TimestampOffset': 'string',
                            'TimestampOffsetMode': 'USE_CONFIGURED_OFFSET'|'USE_EVENT_START_DATE'
                        },
                        'RtmpGroupSettings': {
                            'AuthenticationScheme': 'AKAMAI'|'COMMON',
                            'CacheFullBehavior': 'DISCONNECT_IMMEDIATELY'|'WAIT_FOR_SERVER',
                            'CacheLength': 123,
                            'CaptionData': 'ALL'|'FIELD1_608'|'FIELD1_AND_FIELD2_608',
                            'InputLossAction': 'EMIT_OUTPUT'|'PAUSE_OUTPUT',
                            'RestartDelay': 123
                        },
                        'UdpGroupSettings': {
                            'InputLossAction': 'DROP_PROGRAM'|'DROP_TS'|'EMIT_PROGRAM',
                            'TimedMetadataId3Frame': 'NONE'|'PRIV'|'TDRL',
                            'TimedMetadataId3Period': 123
                        }
                    },
                    'Outputs': [
                        {
                            'AudioDescriptionNames': [
                                'string',
                            ],
                            'CaptionDescriptionNames': [
                                'string',
                            ],
                            'OutputName': 'string',
                            'OutputSettings': {
                                'ArchiveOutputSettings': {
                                    'ContainerSettings': {
                                        'M2tsSettings': {
                                            'AbsentInputAudioBehavior': 'DROP'|'ENCODE_SILENCE',
                                            'Arib': 'DISABLED'|'ENABLED',
                                            'AribCaptionsPid': 'string',
                                            'AribCaptionsPidControl': 'AUTO'|'USE_CONFIGURED',
                                            'AudioBufferModel': 'ATSC'|'DVB',
                                            'AudioFramesPerPes': 123,
                                            'AudioPids': 'string',
                                            'AudioStreamType': 'ATSC'|'DVB',
                                            'Bitrate': 123,
                                            'BufferModel': 'MULTIPLEX'|'NONE',
                                            'CcDescriptor': 'DISABLED'|'ENABLED',
                                            'DvbNitSettings': {
                                                'NetworkId': 123,
                                                'NetworkName': 'string',
                                                'RepInterval': 123
                                            },
                                            'DvbSdtSettings': {
                                                'OutputSdt': 'SDT_FOLLOW'|'SDT_FOLLOW_IF_PRESENT'|'SDT_MANUAL'|'SDT_NONE',
                                                'RepInterval': 123,
                                                'ServiceName': 'string',
                                                'ServiceProviderName': 'string'
                                            },
                                            'DvbSubPids': 'string',
                                            'DvbTdtSettings': {
                                                'RepInterval': 123
                                            },
                                            'DvbTeletextPid': 'string',
                                            'Ebif': 'NONE'|'PASSTHROUGH',
                                            'EbpAudioInterval': 'VIDEO_AND_FIXED_INTERVALS'|'VIDEO_INTERVAL',
                                            'EbpLookaheadMs': 123,
                                            'EbpPlacement': 'VIDEO_AND_AUDIO_PIDS'|'VIDEO_PID',
                                            'EcmPid': 'string',
                                            'EsRateInPes': 'EXCLUDE'|'INCLUDE',
                                            'EtvPlatformPid': 'string',
                                            'EtvSignalPid': 'string',
                                            'FragmentTime': 123.0,
                                            'Klv': 'NONE'|'PASSTHROUGH',
                                            'KlvDataPids': 'string',
                                            'NullPacketBitrate': 123.0,
                                            'PatInterval': 123,
                                            'PcrControl': 'CONFIGURED_PCR_PERIOD'|'PCR_EVERY_PES_PACKET',
                                            'PcrPeriod': 123,
                                            'PcrPid': 'string',
                                            'PmtInterval': 123,
                                            'PmtPid': 'string',
                                            'ProgramNum': 123,
                                            'RateMode': 'CBR'|'VBR',
                                            'Scte27Pids': 'string',
                                            'Scte35Control': 'NONE'|'PASSTHROUGH',
                                            'Scte35Pid': 'string',
                                            'SegmentationMarkers': 'EBP'|'EBP_LEGACY'|'NONE'|'PSI_SEGSTART'|'RAI_ADAPT'|'RAI_SEGSTART',
                                            'SegmentationStyle': 'MAINTAIN_CADENCE'|'RESET_CADENCE',
                                            'SegmentationTime': 123.0,
                                            'TimedMetadataBehavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                            'TimedMetadataPid': 'string',
                                            'TransportStreamId': 123,
                                            'VideoPid': 'string'
                                        }
                                    },
                                    'Extension': 'string',
                                    'NameModifier': 'string'
                                },
                                'HlsOutputSettings': {
                                    'HlsSettings': {
                                        'AudioOnlyHlsSettings': {
                                            'AudioGroupId': 'string',
                                            'AudioOnlyImage': {
                                                'PasswordParam': 'string',
                                                'Uri': 'string',
                                                'Username': 'string'
                                            },
                                            'AudioTrackType': 'ALTERNATE_AUDIO_AUTO_SELECT'|'ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT'|'ALTERNATE_AUDIO_NOT_AUTO_SELECT'|'AUDIO_ONLY_VARIANT_STREAM'
                                        },
                                        'StandardHlsSettings': {
                                            'AudioRenditionSets': 'string',
                                            'M3u8Settings': {
                                                'AudioFramesPerPes': 123,
                                                'AudioPids': 'string',
                                                'EcmPid': 'string',
                                                'PatInterval': 123,
                                                'PcrControl': 'CONFIGURED_PCR_PERIOD'|'PCR_EVERY_PES_PACKET',
                                                'PcrPeriod': 123,
                                                'PcrPid': 'string',
                                                'PmtInterval': 123,
                                                'PmtPid': 'string',
                                                'ProgramNum': 123,
                                                'Scte35Behavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                                'Scte35Pid': 'string',
                                                'TimedMetadataBehavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                                'TimedMetadataPid': 'string',
                                                'TransportStreamId': 123,
                                                'VideoPid': 'string'
                                            }
                                        }
                                    },
                                    'NameModifier': 'string',
                                    'SegmentModifier': 'string'
                                },
                                'MsSmoothOutputSettings': {
                                    'NameModifier': 'string'
                                },
                                'RtmpOutputSettings': {
                                    'CertificateMode': 'SELF_SIGNED'|'VERIFY_AUTHENTICITY',
                                    'ConnectionRetryInterval': 123,
                                    'Destination': {
                                        'DestinationRefId': 'string'
                                    },
                                    'NumRetries': 123
                                },
                                'UdpOutputSettings': {
                                    'BufferMsec': 123,
                                    'ContainerSettings': {
                                        'M2tsSettings': {
                                            'AbsentInputAudioBehavior': 'DROP'|'ENCODE_SILENCE',
                                            'Arib': 'DISABLED'|'ENABLED',
                                            'AribCaptionsPid': 'string',
                                            'AribCaptionsPidControl': 'AUTO'|'USE_CONFIGURED',
                                            'AudioBufferModel': 'ATSC'|'DVB',
                                            'AudioFramesPerPes': 123,
                                            'AudioPids': 'string',
                                            'AudioStreamType': 'ATSC'|'DVB',
                                            'Bitrate': 123,
                                            'BufferModel': 'MULTIPLEX'|'NONE',
                                            'CcDescriptor': 'DISABLED'|'ENABLED',
                                            'DvbNitSettings': {
                                                'NetworkId': 123,
                                                'NetworkName': 'string',
                                                'RepInterval': 123
                                            },
                                            'DvbSdtSettings': {
                                                'OutputSdt': 'SDT_FOLLOW'|'SDT_FOLLOW_IF_PRESENT'|'SDT_MANUAL'|'SDT_NONE',
                                                'RepInterval': 123,
                                                'ServiceName': 'string',
                                                'ServiceProviderName': 'string'
                                            },
                                            'DvbSubPids': 'string',
                                            'DvbTdtSettings': {
                                                'RepInterval': 123
                                            },
                                            'DvbTeletextPid': 'string',
                                            'Ebif': 'NONE'|'PASSTHROUGH',
                                            'EbpAudioInterval': 'VIDEO_AND_FIXED_INTERVALS'|'VIDEO_INTERVAL',
                                            'EbpLookaheadMs': 123,
                                            'EbpPlacement': 'VIDEO_AND_AUDIO_PIDS'|'VIDEO_PID',
                                            'EcmPid': 'string',
                                            'EsRateInPes': 'EXCLUDE'|'INCLUDE',
                                            'EtvPlatformPid': 'string',
                                            'EtvSignalPid': 'string',
                                            'FragmentTime': 123.0,
                                            'Klv': 'NONE'|'PASSTHROUGH',
                                            'KlvDataPids': 'string',
                                            'NullPacketBitrate': 123.0,
                                            'PatInterval': 123,
                                            'PcrControl': 'CONFIGURED_PCR_PERIOD'|'PCR_EVERY_PES_PACKET',
                                            'PcrPeriod': 123,
                                            'PcrPid': 'string',
                                            'PmtInterval': 123,
                                            'PmtPid': 'string',
                                            'ProgramNum': 123,
                                            'RateMode': 'CBR'|'VBR',
                                            'Scte27Pids': 'string',
                                            'Scte35Control': 'NONE'|'PASSTHROUGH',
                                            'Scte35Pid': 'string',
                                            'SegmentationMarkers': 'EBP'|'EBP_LEGACY'|'NONE'|'PSI_SEGSTART'|'RAI_ADAPT'|'RAI_SEGSTART',
                                            'SegmentationStyle': 'MAINTAIN_CADENCE'|'RESET_CADENCE',
                                            'SegmentationTime': 123.0,
                                            'TimedMetadataBehavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                            'TimedMetadataPid': 'string',
                                            'TransportStreamId': 123,
                                            'VideoPid': 'string'
                                        }
                                    },
                                    'Destination': {
                                        'DestinationRefId': 'string'
                                    },
                                    'FecOutputSettings': {
                                        'ColumnDepth': 123,
                                        'IncludeFec': 'COLUMN'|'COLUMN_AND_ROW',
                                        'RowLength': 123
                                    }
                                }
                            },
                            'VideoDescriptionName': 'string'
                        },
                    ]
                },
            ],
            'TimecodeConfig': {
                'Source': 'EMBEDDED'|'SYSTEMCLOCK'|'ZEROBASED',
                'SyncThreshold': 123
            },
            'VideoDescriptions': [
                {
                    'CodecSettings': {
                        'H264Settings': {
                            'AdaptiveQuantization': 'HIGH'|'HIGHER'|'LOW'|'MAX'|'MEDIUM'|'OFF',
                            'AfdSignaling': 'AUTO'|'FIXED'|'NONE',
                            'Bitrate': 123,
                            'BufFillPct': 123,
                            'BufSize': 123,
                            'ColorMetadata': 'IGNORE'|'INSERT',
                            'EntropyEncoding': 'CABAC'|'CAVLC',
                            'FixedAfd': 'AFD_0000'|'AFD_0010'|'AFD_0011'|'AFD_0100'|'AFD_1000'|'AFD_1001'|'AFD_1010'|'AFD_1011'|'AFD_1101'|'AFD_1110'|'AFD_1111',
                            'FlickerAq': 'DISABLED'|'ENABLED',
                            'FramerateControl': 'INITIALIZE_FROM_SOURCE'|'SPECIFIED',
                            'FramerateDenominator': 123,
                            'FramerateNumerator': 123,
                            'GopBReference': 'DISABLED'|'ENABLED',
                            'GopClosedCadence': 123,
                            'GopNumBFrames': 123,
                            'GopSize': 123.0,
                            'GopSizeUnits': 'FRAMES'|'SECONDS',
                            'Level': 'H264_LEVEL_1'|'H264_LEVEL_1_1'|'H264_LEVEL_1_2'|'H264_LEVEL_1_3'|'H264_LEVEL_2'|'H264_LEVEL_2_1'|'H264_LEVEL_2_2'|'H264_LEVEL_3'|'H264_LEVEL_3_1'|'H264_LEVEL_3_2'|'H264_LEVEL_4'|'H264_LEVEL_4_1'|'H264_LEVEL_4_2'|'H264_LEVEL_5'|'H264_LEVEL_5_1'|'H264_LEVEL_5_2'|'H264_LEVEL_AUTO',
                            'LookAheadRateControl': 'HIGH'|'LOW'|'MEDIUM',
                            'MaxBitrate': 123,
                            'MinIInterval': 123,
                            'NumRefFrames': 123,
                            'ParControl': 'INITIALIZE_FROM_SOURCE'|'SPECIFIED',
                            'ParDenominator': 123,
                            'ParNumerator': 123,
                            'Profile': 'BASELINE'|'HIGH'|'HIGH_10BIT'|'HIGH_422'|'HIGH_422_10BIT'|'MAIN',
                            'QvbrQualityLevel': 123,
                            'RateControlMode': 'CBR'|'QVBR'|'VBR',
                            'ScanType': 'INTERLACED'|'PROGRESSIVE',
                            'SceneChangeDetect': 'DISABLED'|'ENABLED',
                            'Slices': 123,
                            'Softness': 123,
                            'SpatialAq': 'DISABLED'|'ENABLED',
                            'SubgopLength': 'DYNAMIC'|'FIXED',
                            'Syntax': 'DEFAULT'|'RP2027',
                            'TemporalAq': 'DISABLED'|'ENABLED',
                            'TimecodeInsertion': 'DISABLED'|'PIC_TIMING_SEI'
                        }
                    },
                    'Height': 123,
                    'Name': 'string',
                    'RespondToAfd': 'NONE'|'PASSTHROUGH'|'RESPOND',
                    'ScalingBehavior': 'DEFAULT'|'STRETCH_TO_OUTPUT',
                    'Sharpness': 123,
                    'Width': 123
                },
            ]
        },
        'Id': 'string',
        'InputAttachments': [
            {
                'InputAttachmentName': 'string',
                'InputId': 'string',
                'InputSettings': {
                    'AudioSelectors': [
                        {
                            'Name': 'string',
                            'SelectorSettings': {
                                'AudioLanguageSelection': {
                                    'LanguageCode': 'string',
                                    'LanguageSelectionPolicy': 'LOOSE'|'STRICT'
                                },
                                'AudioPidSelection': {
                                    'Pid': 123
                                }
                            }
                        },
                    ],
                    'CaptionSelectors': [
                        {
                            'LanguageCode': 'string',
                            'Name': 'string',
                            'SelectorSettings': {
                                'AribSourceSettings': {},
                                'DvbSubSourceSettings': {
                                    'Pid': 123
                                },
                                'EmbeddedSourceSettings': {
                                    'Convert608To708': 'DISABLED'|'UPCONVERT',
                                    'Scte20Detection': 'AUTO'|'OFF',
                                    'Source608ChannelNumber': 123,
                                    'Source608TrackNumber': 123
                                },
                                'Scte20SourceSettings': {
                                    'Convert608To708': 'DISABLED'|'UPCONVERT',
                                    'Source608ChannelNumber': 123
                                },
                                'Scte27SourceSettings': {
                                    'Pid': 123
                                },
                                'TeletextSourceSettings': {
                                    'PageNumber': 'string'
                                }
                            }
                        },
                    ],
                    'DeblockFilter': 'DISABLED'|'ENABLED',
                    'DenoiseFilter': 'DISABLED'|'ENABLED',
                    'FilterStrength': 123,
                    'InputFilter': 'AUTO'|'DISABLED'|'FORCED',
                    'NetworkInputSettings': {
                        'HlsInputSettings': {
                            'Bandwidth': 123,
                            'BufferSegments': 123,
                            'Retries': 123,
                            'RetryInterval': 123
                        },
                        'ServerValidation': 'CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME'|'CHECK_CRYPTOGRAPHY_ONLY'
                    },
                    'SourceEndBehavior': 'CONTINUE'|'LOOP',
                    'VideoSelector': {
                        'ColorSpace': 'FOLLOW'|'REC_601'|'REC_709',
                        'ColorSpaceUsage': 'FALLBACK'|'FORCE',
                        'SelectorSettings': {
                            'VideoSelectorPid': {
                                'Pid': 123
                            },
                            'VideoSelectorProgramId': {
                                'ProgramId': 123
                            }
                        }
                    }
                }
            },
        ],
        'InputSpecification': {
            'Codec': 'MPEG2'|'AVC'|'HEVC',
            'MaximumBitrate': 'MAX_10_MBPS'|'MAX_20_MBPS'|'MAX_50_MBPS',
            'Resolution': 'SD'|'HD'|'UHD'
        },
        'LogLevel': 'ERROR'|'WARNING'|'INFO'|'DEBUG'|'DISABLED',
        'Name': 'string',
        'PipelinesRunningCount': 123,
        'RoleArn': 'string',
        'State': 'CREATING'|'CREATE_FAILED'|'IDLE'|'STARTING'|'RUNNING'|'RECOVERING'|'STOPPING'|'DELETING'|'DELETED'
    }
    
    
    """
    pass

def delete_input(InputId=None):
    """
    Deletes the input end point
    See also: AWS API Documentation
    
    
    :example: response = client.delete_input(
        InputId='string'
    )
    
    
    :type InputId: string
    :param InputId: [REQUIRED] Unique ID of the input

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_input_security_group(InputSecurityGroupId=None):
    """
    Deletes an Input Security Group
    See also: AWS API Documentation
    
    
    :example: response = client.delete_input_security_group(
        InputSecurityGroupId='string'
    )
    
    
    :type InputSecurityGroupId: string
    :param InputSecurityGroupId: [REQUIRED] The Input Security Group to delete

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_reservation(ReservationId=None):
    """
    Delete an expired reservation.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_reservation(
        ReservationId='string'
    )
    
    
    :type ReservationId: string
    :param ReservationId: [REQUIRED] Unique reservation ID, e.g. '1234567'

    :rtype: dict
    :return: {
        'Arn': 'string',
        'Count': 123,
        'CurrencyCode': 'string',
        'Duration': 123,
        'DurationUnits': 'MONTHS',
        'End': 'string',
        'FixedPrice': 123.0,
        'Name': 'string',
        'OfferingDescription': 'string',
        'OfferingId': 'string',
        'OfferingType': 'NO_UPFRONT',
        'Region': 'string',
        'ReservationId': 'string',
        'ResourceSpecification': {
            'Codec': 'MPEG2'|'AVC'|'HEVC'|'AUDIO',
            'MaximumBitrate': 'MAX_10_MBPS'|'MAX_20_MBPS'|'MAX_50_MBPS',
            'MaximumFramerate': 'MAX_30_FPS'|'MAX_60_FPS',
            'Resolution': 'SD'|'HD'|'UHD',
            'ResourceType': 'INPUT'|'OUTPUT'|'CHANNEL',
            'SpecialFeature': 'ADVANCED_AUDIO'|'AUDIO_NORMALIZATION',
            'VideoQuality': 'STANDARD'|'ENHANCED'|'PREMIUM'
        },
        'Start': 'string',
        'State': 'ACTIVE'|'EXPIRED'|'CANCELED'|'DELETED',
        'UsagePrice': 123.0
    }
    
    
    """
    pass

def describe_channel(ChannelId=None):
    """
    Gets details about a channel
    See also: AWS API Documentation
    
    
    :example: response = client.describe_channel(
        ChannelId='string'
    )
    
    
    :type ChannelId: string
    :param ChannelId: [REQUIRED] channel ID

    :rtype: dict
    :return: {
        'Arn': 'string',
        'Destinations': [
            {
                'Id': 'string',
                'Settings': [
                    {
                        'PasswordParam': 'string',
                        'StreamName': 'string',
                        'Url': 'string',
                        'Username': 'string'
                    },
                ]
            },
        ],
        'EgressEndpoints': [
            {
                'SourceIp': 'string'
            },
        ],
        'EncoderSettings': {
            'AudioDescriptions': [
                {
                    'AudioNormalizationSettings': {
                        'Algorithm': 'ITU_1770_1'|'ITU_1770_2',
                        'AlgorithmControl': 'CORRECT_AUDIO',
                        'TargetLkfs': 123.0
                    },
                    'AudioSelectorName': 'string',
                    'AudioType': 'CLEAN_EFFECTS'|'HEARING_IMPAIRED'|'UNDEFINED'|'VISUAL_IMPAIRED_COMMENTARY',
                    'AudioTypeControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                    'CodecSettings': {
                        'AacSettings': {
                            'Bitrate': 123.0,
                            'CodingMode': 'AD_RECEIVER_MIX'|'CODING_MODE_1_0'|'CODING_MODE_1_1'|'CODING_MODE_2_0'|'CODING_MODE_5_1',
                            'InputType': 'BROADCASTER_MIXED_AD'|'NORMAL',
                            'Profile': 'HEV1'|'HEV2'|'LC',
                            'RateControlMode': 'CBR'|'VBR',
                            'RawFormat': 'LATM_LOAS'|'NONE',
                            'SampleRate': 123.0,
                            'Spec': 'MPEG2'|'MPEG4',
                            'VbrQuality': 'HIGH'|'LOW'|'MEDIUM_HIGH'|'MEDIUM_LOW'
                        },
                        'Ac3Settings': {
                            'Bitrate': 123.0,
                            'BitstreamMode': 'COMMENTARY'|'COMPLETE_MAIN'|'DIALOGUE'|'EMERGENCY'|'HEARING_IMPAIRED'|'MUSIC_AND_EFFECTS'|'VISUALLY_IMPAIRED'|'VOICE_OVER',
                            'CodingMode': 'CODING_MODE_1_0'|'CODING_MODE_1_1'|'CODING_MODE_2_0'|'CODING_MODE_3_2_LFE',
                            'Dialnorm': 123,
                            'DrcProfile': 'FILM_STANDARD'|'NONE',
                            'LfeFilter': 'DISABLED'|'ENABLED',
                            'MetadataControl': 'FOLLOW_INPUT'|'USE_CONFIGURED'
                        },
                        'Eac3Settings': {
                            'AttenuationControl': 'ATTENUATE_3_DB'|'NONE',
                            'Bitrate': 123.0,
                            'BitstreamMode': 'COMMENTARY'|'COMPLETE_MAIN'|'EMERGENCY'|'HEARING_IMPAIRED'|'VISUALLY_IMPAIRED',
                            'CodingMode': 'CODING_MODE_1_0'|'CODING_MODE_2_0'|'CODING_MODE_3_2',
                            'DcFilter': 'DISABLED'|'ENABLED',
                            'Dialnorm': 123,
                            'DrcLine': 'FILM_LIGHT'|'FILM_STANDARD'|'MUSIC_LIGHT'|'MUSIC_STANDARD'|'NONE'|'SPEECH',
                            'DrcRf': 'FILM_LIGHT'|'FILM_STANDARD'|'MUSIC_LIGHT'|'MUSIC_STANDARD'|'NONE'|'SPEECH',
                            'LfeControl': 'LFE'|'NO_LFE',
                            'LfeFilter': 'DISABLED'|'ENABLED',
                            'LoRoCenterMixLevel': 123.0,
                            'LoRoSurroundMixLevel': 123.0,
                            'LtRtCenterMixLevel': 123.0,
                            'LtRtSurroundMixLevel': 123.0,
                            'MetadataControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                            'PassthroughControl': 'NO_PASSTHROUGH'|'WHEN_POSSIBLE',
                            'PhaseControl': 'NO_SHIFT'|'SHIFT_90_DEGREES',
                            'StereoDownmix': 'DPL2'|'LO_RO'|'LT_RT'|'NOT_INDICATED',
                            'SurroundExMode': 'DISABLED'|'ENABLED'|'NOT_INDICATED',
                            'SurroundMode': 'DISABLED'|'ENABLED'|'NOT_INDICATED'
                        },
                        'Mp2Settings': {
                            'Bitrate': 123.0,
                            'CodingMode': 'CODING_MODE_1_0'|'CODING_MODE_2_0',
                            'SampleRate': 123.0
                        },
                        'PassThroughSettings': {}
                    },
                    'LanguageCode': 'string',
                    'LanguageCodeControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                    'Name': 'string',
                    'RemixSettings': {
                        'ChannelMappings': [
                            {
                                'InputChannelLevels': [
                                    {
                                        'Gain': 123,
                                        'InputChannel': 123
                                    },
                                ],
                                'OutputChannel': 123
                            },
                        ],
                        'ChannelsIn': 123,
                        'ChannelsOut': 123
                    },
                    'StreamName': 'string'
                },
            ],
            'AvailBlanking': {
                'AvailBlankingImage': {
                    'PasswordParam': 'string',
                    'Uri': 'string',
                    'Username': 'string'
                },
                'State': 'DISABLED'|'ENABLED'
            },
            'AvailConfiguration': {
                'AvailSettings': {
                    'Scte35SpliceInsert': {
                        'AdAvailOffset': 123,
                        'NoRegionalBlackoutFlag': 'FOLLOW'|'IGNORE',
                        'WebDeliveryAllowedFlag': 'FOLLOW'|'IGNORE'
                    },
                    'Scte35TimeSignalApos': {
                        'AdAvailOffset': 123,
                        'NoRegionalBlackoutFlag': 'FOLLOW'|'IGNORE',
                        'WebDeliveryAllowedFlag': 'FOLLOW'|'IGNORE'
                    }
                }
            },
            'BlackoutSlate': {
                'BlackoutSlateImage': {
                    'PasswordParam': 'string',
                    'Uri': 'string',
                    'Username': 'string'
                },
                'NetworkEndBlackout': 'DISABLED'|'ENABLED',
                'NetworkEndBlackoutImage': {
                    'PasswordParam': 'string',
                    'Uri': 'string',
                    'Username': 'string'
                },
                'NetworkId': 'string',
                'State': 'DISABLED'|'ENABLED'
            },
            'CaptionDescriptions': [
                {
                    'CaptionSelectorName': 'string',
                    'DestinationSettings': {
                        'AribDestinationSettings': {},
                        'BurnInDestinationSettings': {
                            'Alignment': 'CENTERED'|'LEFT'|'SMART',
                            'BackgroundColor': 'BLACK'|'NONE'|'WHITE',
                            'BackgroundOpacity': 123,
                            'Font': {
                                'PasswordParam': 'string',
                                'Uri': 'string',
                                'Username': 'string'
                            },
                            'FontColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                            'FontOpacity': 123,
                            'FontResolution': 123,
                            'FontSize': 'string',
                            'OutlineColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                            'OutlineSize': 123,
                            'ShadowColor': 'BLACK'|'NONE'|'WHITE',
                            'ShadowOpacity': 123,
                            'ShadowXOffset': 123,
                            'ShadowYOffset': 123,
                            'TeletextGridControl': 'FIXED'|'SCALED',
                            'XPosition': 123,
                            'YPosition': 123
                        },
                        'DvbSubDestinationSettings': {
                            'Alignment': 'CENTERED'|'LEFT'|'SMART',
                            'BackgroundColor': 'BLACK'|'NONE'|'WHITE',
                            'BackgroundOpacity': 123,
                            'Font': {
                                'PasswordParam': 'string',
                                'Uri': 'string',
                                'Username': 'string'
                            },
                            'FontColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                            'FontOpacity': 123,
                            'FontResolution': 123,
                            'FontSize': 'string',
                            'OutlineColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                            'OutlineSize': 123,
                            'ShadowColor': 'BLACK'|'NONE'|'WHITE',
                            'ShadowOpacity': 123,
                            'ShadowXOffset': 123,
                            'ShadowYOffset': 123,
                            'TeletextGridControl': 'FIXED'|'SCALED',
                            'XPosition': 123,
                            'YPosition': 123
                        },
                        'EmbeddedDestinationSettings': {},
                        'EmbeddedPlusScte20DestinationSettings': {},
                        'RtmpCaptionInfoDestinationSettings': {},
                        'Scte20PlusEmbeddedDestinationSettings': {},
                        'Scte27DestinationSettings': {},
                        'SmpteTtDestinationSettings': {},
                        'TeletextDestinationSettings': {},
                        'TtmlDestinationSettings': {
                            'StyleControl': 'PASSTHROUGH'|'USE_CONFIGURED'
                        },
                        'WebvttDestinationSettings': {}
                    },
                    'LanguageCode': 'string',
                    'LanguageDescription': 'string',
                    'Name': 'string'
                },
            ],
            'GlobalConfiguration': {
                'InitialAudioGain': 123,
                'InputEndAction': 'NONE'|'SWITCH_AND_LOOP_INPUTS',
                'InputLossBehavior': {
                    'BlackFrameMsec': 123,
                    'InputLossImageColor': 'string',
                    'InputLossImageSlate': {
                        'PasswordParam': 'string',
                        'Uri': 'string',
                        'Username': 'string'
                    },
                    'InputLossImageType': 'COLOR'|'SLATE',
                    'RepeatFrameMsec': 123
                },
                'OutputTimingSource': 'INPUT_CLOCK'|'SYSTEM_CLOCK',
                'SupportLowFramerateInputs': 'DISABLED'|'ENABLED'
            },
            'OutputGroups': [
                {
                    'Name': 'string',
                    'OutputGroupSettings': {
                        'ArchiveGroupSettings': {
                            'Destination': {
                                'DestinationRefId': 'string'
                            },
                            'RolloverInterval': 123
                        },
                        'HlsGroupSettings': {
                            'AdMarkers': [
                                'ADOBE'|'ELEMENTAL'|'ELEMENTAL_SCTE35',
                            ],
                            'BaseUrlContent': 'string',
                            'BaseUrlManifest': 'string',
                            'CaptionLanguageMappings': [
                                {
                                    'CaptionChannel': 123,
                                    'LanguageCode': 'string',
                                    'LanguageDescription': 'string'
                                },
                            ],
                            'CaptionLanguageSetting': 'INSERT'|'NONE'|'OMIT',
                            'ClientCache': 'DISABLED'|'ENABLED',
                            'CodecSpecification': 'RFC_4281'|'RFC_6381',
                            'ConstantIv': 'string',
                            'Destination': {
                                'DestinationRefId': 'string'
                            },
                            'DirectoryStructure': 'SINGLE_DIRECTORY'|'SUBDIRECTORY_PER_STREAM',
                            'EncryptionType': 'AES128'|'SAMPLE_AES',
                            'HlsCdnSettings': {
                                'HlsAkamaiSettings': {
                                    'ConnectionRetryInterval': 123,
                                    'FilecacheDuration': 123,
                                    'HttpTransferMode': 'CHUNKED'|'NON_CHUNKED',
                                    'NumRetries': 123,
                                    'RestartDelay': 123,
                                    'Salt': 'string',
                                    'Token': 'string'
                                },
                                'HlsBasicPutSettings': {
                                    'ConnectionRetryInterval': 123,
                                    'FilecacheDuration': 123,
                                    'NumRetries': 123,
                                    'RestartDelay': 123
                                },
                                'HlsMediaStoreSettings': {
                                    'ConnectionRetryInterval': 123,
                                    'FilecacheDuration': 123,
                                    'MediaStoreStorageClass': 'TEMPORAL',
                                    'NumRetries': 123,
                                    'RestartDelay': 123
                                },
                                'HlsWebdavSettings': {
                                    'ConnectionRetryInterval': 123,
                                    'FilecacheDuration': 123,
                                    'HttpTransferMode': 'CHUNKED'|'NON_CHUNKED',
                                    'NumRetries': 123,
                                    'RestartDelay': 123
                                }
                            },
                            'IndexNSegments': 123,
                            'InputLossAction': 'EMIT_OUTPUT'|'PAUSE_OUTPUT',
                            'IvInManifest': 'EXCLUDE'|'INCLUDE',
                            'IvSource': 'EXPLICIT'|'FOLLOWS_SEGMENT_NUMBER',
                            'KeepSegments': 123,
                            'KeyFormat': 'string',
                            'KeyFormatVersions': 'string',
                            'KeyProviderSettings': {
                                'StaticKeySettings': {
                                    'KeyProviderServer': {
                                        'PasswordParam': 'string',
                                        'Uri': 'string',
                                        'Username': 'string'
                                    },
                                    'StaticKeyValue': 'string'
                                }
                            },
                            'ManifestCompression': 'GZIP'|'NONE',
                            'ManifestDurationFormat': 'FLOATING_POINT'|'INTEGER',
                            'MinSegmentLength': 123,
                            'Mode': 'LIVE'|'VOD',
                            'OutputSelection': 'MANIFESTS_AND_SEGMENTS'|'SEGMENTS_ONLY',
                            'ProgramDateTime': 'EXCLUDE'|'INCLUDE',
                            'ProgramDateTimePeriod': 123,
                            'RedundantManifest': 'DISABLED'|'ENABLED',
                            'SegmentLength': 123,
                            'SegmentationMode': 'USE_INPUT_SEGMENTATION'|'USE_SEGMENT_DURATION',
                            'SegmentsPerSubdirectory': 123,
                            'StreamInfResolution': 'EXCLUDE'|'INCLUDE',
                            'TimedMetadataId3Frame': 'NONE'|'PRIV'|'TDRL',
                            'TimedMetadataId3Period': 123,
                            'TimestampDeltaMilliseconds': 123,
                            'TsFileMode': 'SEGMENTED_FILES'|'SINGLE_FILE'
                        },
                        'MsSmoothGroupSettings': {
                            'AcquisitionPointId': 'string',
                            'AudioOnlyTimecodeControl': 'PASSTHROUGH'|'USE_CONFIGURED_CLOCK',
                            'CertificateMode': 'SELF_SIGNED'|'VERIFY_AUTHENTICITY',
                            'ConnectionRetryInterval': 123,
                            'Destination': {
                                'DestinationRefId': 'string'
                            },
                            'EventId': 'string',
                            'EventIdMode': 'NO_EVENT_ID'|'USE_CONFIGURED'|'USE_TIMESTAMP',
                            'EventStopBehavior': 'NONE'|'SEND_EOS',
                            'FilecacheDuration': 123,
                            'FragmentLength': 123,
                            'InputLossAction': 'EMIT_OUTPUT'|'PAUSE_OUTPUT',
                            'NumRetries': 123,
                            'RestartDelay': 123,
                            'SegmentationMode': 'USE_INPUT_SEGMENTATION'|'USE_SEGMENT_DURATION',
                            'SendDelayMs': 123,
                            'SparseTrackType': 'NONE'|'SCTE_35',
                            'StreamManifestBehavior': 'DO_NOT_SEND'|'SEND',
                            'TimestampOffset': 'string',
                            'TimestampOffsetMode': 'USE_CONFIGURED_OFFSET'|'USE_EVENT_START_DATE'
                        },
                        'RtmpGroupSettings': {
                            'AuthenticationScheme': 'AKAMAI'|'COMMON',
                            'CacheFullBehavior': 'DISCONNECT_IMMEDIATELY'|'WAIT_FOR_SERVER',
                            'CacheLength': 123,
                            'CaptionData': 'ALL'|'FIELD1_608'|'FIELD1_AND_FIELD2_608',
                            'InputLossAction': 'EMIT_OUTPUT'|'PAUSE_OUTPUT',
                            'RestartDelay': 123
                        },
                        'UdpGroupSettings': {
                            'InputLossAction': 'DROP_PROGRAM'|'DROP_TS'|'EMIT_PROGRAM',
                            'TimedMetadataId3Frame': 'NONE'|'PRIV'|'TDRL',
                            'TimedMetadataId3Period': 123
                        }
                    },
                    'Outputs': [
                        {
                            'AudioDescriptionNames': [
                                'string',
                            ],
                            'CaptionDescriptionNames': [
                                'string',
                            ],
                            'OutputName': 'string',
                            'OutputSettings': {
                                'ArchiveOutputSettings': {
                                    'ContainerSettings': {
                                        'M2tsSettings': {
                                            'AbsentInputAudioBehavior': 'DROP'|'ENCODE_SILENCE',
                                            'Arib': 'DISABLED'|'ENABLED',
                                            'AribCaptionsPid': 'string',
                                            'AribCaptionsPidControl': 'AUTO'|'USE_CONFIGURED',
                                            'AudioBufferModel': 'ATSC'|'DVB',
                                            'AudioFramesPerPes': 123,
                                            'AudioPids': 'string',
                                            'AudioStreamType': 'ATSC'|'DVB',
                                            'Bitrate': 123,
                                            'BufferModel': 'MULTIPLEX'|'NONE',
                                            'CcDescriptor': 'DISABLED'|'ENABLED',
                                            'DvbNitSettings': {
                                                'NetworkId': 123,
                                                'NetworkName': 'string',
                                                'RepInterval': 123
                                            },
                                            'DvbSdtSettings': {
                                                'OutputSdt': 'SDT_FOLLOW'|'SDT_FOLLOW_IF_PRESENT'|'SDT_MANUAL'|'SDT_NONE',
                                                'RepInterval': 123,
                                                'ServiceName': 'string',
                                                'ServiceProviderName': 'string'
                                            },
                                            'DvbSubPids': 'string',
                                            'DvbTdtSettings': {
                                                'RepInterval': 123
                                            },
                                            'DvbTeletextPid': 'string',
                                            'Ebif': 'NONE'|'PASSTHROUGH',
                                            'EbpAudioInterval': 'VIDEO_AND_FIXED_INTERVALS'|'VIDEO_INTERVAL',
                                            'EbpLookaheadMs': 123,
                                            'EbpPlacement': 'VIDEO_AND_AUDIO_PIDS'|'VIDEO_PID',
                                            'EcmPid': 'string',
                                            'EsRateInPes': 'EXCLUDE'|'INCLUDE',
                                            'EtvPlatformPid': 'string',
                                            'EtvSignalPid': 'string',
                                            'FragmentTime': 123.0,
                                            'Klv': 'NONE'|'PASSTHROUGH',
                                            'KlvDataPids': 'string',
                                            'NullPacketBitrate': 123.0,
                                            'PatInterval': 123,
                                            'PcrControl': 'CONFIGURED_PCR_PERIOD'|'PCR_EVERY_PES_PACKET',
                                            'PcrPeriod': 123,
                                            'PcrPid': 'string',
                                            'PmtInterval': 123,
                                            'PmtPid': 'string',
                                            'ProgramNum': 123,
                                            'RateMode': 'CBR'|'VBR',
                                            'Scte27Pids': 'string',
                                            'Scte35Control': 'NONE'|'PASSTHROUGH',
                                            'Scte35Pid': 'string',
                                            'SegmentationMarkers': 'EBP'|'EBP_LEGACY'|'NONE'|'PSI_SEGSTART'|'RAI_ADAPT'|'RAI_SEGSTART',
                                            'SegmentationStyle': 'MAINTAIN_CADENCE'|'RESET_CADENCE',
                                            'SegmentationTime': 123.0,
                                            'TimedMetadataBehavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                            'TimedMetadataPid': 'string',
                                            'TransportStreamId': 123,
                                            'VideoPid': 'string'
                                        }
                                    },
                                    'Extension': 'string',
                                    'NameModifier': 'string'
                                },
                                'HlsOutputSettings': {
                                    'HlsSettings': {
                                        'AudioOnlyHlsSettings': {
                                            'AudioGroupId': 'string',
                                            'AudioOnlyImage': {
                                                'PasswordParam': 'string',
                                                'Uri': 'string',
                                                'Username': 'string'
                                            },
                                            'AudioTrackType': 'ALTERNATE_AUDIO_AUTO_SELECT'|'ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT'|'ALTERNATE_AUDIO_NOT_AUTO_SELECT'|'AUDIO_ONLY_VARIANT_STREAM'
                                        },
                                        'StandardHlsSettings': {
                                            'AudioRenditionSets': 'string',
                                            'M3u8Settings': {
                                                'AudioFramesPerPes': 123,
                                                'AudioPids': 'string',
                                                'EcmPid': 'string',
                                                'PatInterval': 123,
                                                'PcrControl': 'CONFIGURED_PCR_PERIOD'|'PCR_EVERY_PES_PACKET',
                                                'PcrPeriod': 123,
                                                'PcrPid': 'string',
                                                'PmtInterval': 123,
                                                'PmtPid': 'string',
                                                'ProgramNum': 123,
                                                'Scte35Behavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                                'Scte35Pid': 'string',
                                                'TimedMetadataBehavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                                'TimedMetadataPid': 'string',
                                                'TransportStreamId': 123,
                                                'VideoPid': 'string'
                                            }
                                        }
                                    },
                                    'NameModifier': 'string',
                                    'SegmentModifier': 'string'
                                },
                                'MsSmoothOutputSettings': {
                                    'NameModifier': 'string'
                                },
                                'RtmpOutputSettings': {
                                    'CertificateMode': 'SELF_SIGNED'|'VERIFY_AUTHENTICITY',
                                    'ConnectionRetryInterval': 123,
                                    'Destination': {
                                        'DestinationRefId': 'string'
                                    },
                                    'NumRetries': 123
                                },
                                'UdpOutputSettings': {
                                    'BufferMsec': 123,
                                    'ContainerSettings': {
                                        'M2tsSettings': {
                                            'AbsentInputAudioBehavior': 'DROP'|'ENCODE_SILENCE',
                                            'Arib': 'DISABLED'|'ENABLED',
                                            'AribCaptionsPid': 'string',
                                            'AribCaptionsPidControl': 'AUTO'|'USE_CONFIGURED',
                                            'AudioBufferModel': 'ATSC'|'DVB',
                                            'AudioFramesPerPes': 123,
                                            'AudioPids': 'string',
                                            'AudioStreamType': 'ATSC'|'DVB',
                                            'Bitrate': 123,
                                            'BufferModel': 'MULTIPLEX'|'NONE',
                                            'CcDescriptor': 'DISABLED'|'ENABLED',
                                            'DvbNitSettings': {
                                                'NetworkId': 123,
                                                'NetworkName': 'string',
                                                'RepInterval': 123
                                            },
                                            'DvbSdtSettings': {
                                                'OutputSdt': 'SDT_FOLLOW'|'SDT_FOLLOW_IF_PRESENT'|'SDT_MANUAL'|'SDT_NONE',
                                                'RepInterval': 123,
                                                'ServiceName': 'string',
                                                'ServiceProviderName': 'string'
                                            },
                                            'DvbSubPids': 'string',
                                            'DvbTdtSettings': {
                                                'RepInterval': 123
                                            },
                                            'DvbTeletextPid': 'string',
                                            'Ebif': 'NONE'|'PASSTHROUGH',
                                            'EbpAudioInterval': 'VIDEO_AND_FIXED_INTERVALS'|'VIDEO_INTERVAL',
                                            'EbpLookaheadMs': 123,
                                            'EbpPlacement': 'VIDEO_AND_AUDIO_PIDS'|'VIDEO_PID',
                                            'EcmPid': 'string',
                                            'EsRateInPes': 'EXCLUDE'|'INCLUDE',
                                            'EtvPlatformPid': 'string',
                                            'EtvSignalPid': 'string',
                                            'FragmentTime': 123.0,
                                            'Klv': 'NONE'|'PASSTHROUGH',
                                            'KlvDataPids': 'string',
                                            'NullPacketBitrate': 123.0,
                                            'PatInterval': 123,
                                            'PcrControl': 'CONFIGURED_PCR_PERIOD'|'PCR_EVERY_PES_PACKET',
                                            'PcrPeriod': 123,
                                            'PcrPid': 'string',
                                            'PmtInterval': 123,
                                            'PmtPid': 'string',
                                            'ProgramNum': 123,
                                            'RateMode': 'CBR'|'VBR',
                                            'Scte27Pids': 'string',
                                            'Scte35Control': 'NONE'|'PASSTHROUGH',
                                            'Scte35Pid': 'string',
                                            'SegmentationMarkers': 'EBP'|'EBP_LEGACY'|'NONE'|'PSI_SEGSTART'|'RAI_ADAPT'|'RAI_SEGSTART',
                                            'SegmentationStyle': 'MAINTAIN_CADENCE'|'RESET_CADENCE',
                                            'SegmentationTime': 123.0,
                                            'TimedMetadataBehavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                            'TimedMetadataPid': 'string',
                                            'TransportStreamId': 123,
                                            'VideoPid': 'string'
                                        }
                                    },
                                    'Destination': {
                                        'DestinationRefId': 'string'
                                    },
                                    'FecOutputSettings': {
                                        'ColumnDepth': 123,
                                        'IncludeFec': 'COLUMN'|'COLUMN_AND_ROW',
                                        'RowLength': 123
                                    }
                                }
                            },
                            'VideoDescriptionName': 'string'
                        },
                    ]
                },
            ],
            'TimecodeConfig': {
                'Source': 'EMBEDDED'|'SYSTEMCLOCK'|'ZEROBASED',
                'SyncThreshold': 123
            },
            'VideoDescriptions': [
                {
                    'CodecSettings': {
                        'H264Settings': {
                            'AdaptiveQuantization': 'HIGH'|'HIGHER'|'LOW'|'MAX'|'MEDIUM'|'OFF',
                            'AfdSignaling': 'AUTO'|'FIXED'|'NONE',
                            'Bitrate': 123,
                            'BufFillPct': 123,
                            'BufSize': 123,
                            'ColorMetadata': 'IGNORE'|'INSERT',
                            'EntropyEncoding': 'CABAC'|'CAVLC',
                            'FixedAfd': 'AFD_0000'|'AFD_0010'|'AFD_0011'|'AFD_0100'|'AFD_1000'|'AFD_1001'|'AFD_1010'|'AFD_1011'|'AFD_1101'|'AFD_1110'|'AFD_1111',
                            'FlickerAq': 'DISABLED'|'ENABLED',
                            'FramerateControl': 'INITIALIZE_FROM_SOURCE'|'SPECIFIED',
                            'FramerateDenominator': 123,
                            'FramerateNumerator': 123,
                            'GopBReference': 'DISABLED'|'ENABLED',
                            'GopClosedCadence': 123,
                            'GopNumBFrames': 123,
                            'GopSize': 123.0,
                            'GopSizeUnits': 'FRAMES'|'SECONDS',
                            'Level': 'H264_LEVEL_1'|'H264_LEVEL_1_1'|'H264_LEVEL_1_2'|'H264_LEVEL_1_3'|'H264_LEVEL_2'|'H264_LEVEL_2_1'|'H264_LEVEL_2_2'|'H264_LEVEL_3'|'H264_LEVEL_3_1'|'H264_LEVEL_3_2'|'H264_LEVEL_4'|'H264_LEVEL_4_1'|'H264_LEVEL_4_2'|'H264_LEVEL_5'|'H264_LEVEL_5_1'|'H264_LEVEL_5_2'|'H264_LEVEL_AUTO',
                            'LookAheadRateControl': 'HIGH'|'LOW'|'MEDIUM',
                            'MaxBitrate': 123,
                            'MinIInterval': 123,
                            'NumRefFrames': 123,
                            'ParControl': 'INITIALIZE_FROM_SOURCE'|'SPECIFIED',
                            'ParDenominator': 123,
                            'ParNumerator': 123,
                            'Profile': 'BASELINE'|'HIGH'|'HIGH_10BIT'|'HIGH_422'|'HIGH_422_10BIT'|'MAIN',
                            'QvbrQualityLevel': 123,
                            'RateControlMode': 'CBR'|'QVBR'|'VBR',
                            'ScanType': 'INTERLACED'|'PROGRESSIVE',
                            'SceneChangeDetect': 'DISABLED'|'ENABLED',
                            'Slices': 123,
                            'Softness': 123,
                            'SpatialAq': 'DISABLED'|'ENABLED',
                            'SubgopLength': 'DYNAMIC'|'FIXED',
                            'Syntax': 'DEFAULT'|'RP2027',
                            'TemporalAq': 'DISABLED'|'ENABLED',
                            'TimecodeInsertion': 'DISABLED'|'PIC_TIMING_SEI'
                        }
                    },
                    'Height': 123,
                    'Name': 'string',
                    'RespondToAfd': 'NONE'|'PASSTHROUGH'|'RESPOND',
                    'ScalingBehavior': 'DEFAULT'|'STRETCH_TO_OUTPUT',
                    'Sharpness': 123,
                    'Width': 123
                },
            ]
        },
        'Id': 'string',
        'InputAttachments': [
            {
                'InputAttachmentName': 'string',
                'InputId': 'string',
                'InputSettings': {
                    'AudioSelectors': [
                        {
                            'Name': 'string',
                            'SelectorSettings': {
                                'AudioLanguageSelection': {
                                    'LanguageCode': 'string',
                                    'LanguageSelectionPolicy': 'LOOSE'|'STRICT'
                                },
                                'AudioPidSelection': {
                                    'Pid': 123
                                }
                            }
                        },
                    ],
                    'CaptionSelectors': [
                        {
                            'LanguageCode': 'string',
                            'Name': 'string',
                            'SelectorSettings': {
                                'AribSourceSettings': {},
                                'DvbSubSourceSettings': {
                                    'Pid': 123
                                },
                                'EmbeddedSourceSettings': {
                                    'Convert608To708': 'DISABLED'|'UPCONVERT',
                                    'Scte20Detection': 'AUTO'|'OFF',
                                    'Source608ChannelNumber': 123,
                                    'Source608TrackNumber': 123
                                },
                                'Scte20SourceSettings': {
                                    'Convert608To708': 'DISABLED'|'UPCONVERT',
                                    'Source608ChannelNumber': 123
                                },
                                'Scte27SourceSettings': {
                                    'Pid': 123
                                },
                                'TeletextSourceSettings': {
                                    'PageNumber': 'string'
                                }
                            }
                        },
                    ],
                    'DeblockFilter': 'DISABLED'|'ENABLED',
                    'DenoiseFilter': 'DISABLED'|'ENABLED',
                    'FilterStrength': 123,
                    'InputFilter': 'AUTO'|'DISABLED'|'FORCED',
                    'NetworkInputSettings': {
                        'HlsInputSettings': {
                            'Bandwidth': 123,
                            'BufferSegments': 123,
                            'Retries': 123,
                            'RetryInterval': 123
                        },
                        'ServerValidation': 'CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME'|'CHECK_CRYPTOGRAPHY_ONLY'
                    },
                    'SourceEndBehavior': 'CONTINUE'|'LOOP',
                    'VideoSelector': {
                        'ColorSpace': 'FOLLOW'|'REC_601'|'REC_709',
                        'ColorSpaceUsage': 'FALLBACK'|'FORCE',
                        'SelectorSettings': {
                            'VideoSelectorPid': {
                                'Pid': 123
                            },
                            'VideoSelectorProgramId': {
                                'ProgramId': 123
                            }
                        }
                    }
                }
            },
        ],
        'InputSpecification': {
            'Codec': 'MPEG2'|'AVC'|'HEVC',
            'MaximumBitrate': 'MAX_10_MBPS'|'MAX_20_MBPS'|'MAX_50_MBPS',
            'Resolution': 'SD'|'HD'|'UHD'
        },
        'LogLevel': 'ERROR'|'WARNING'|'INFO'|'DEBUG'|'DISABLED',
        'Name': 'string',
        'PipelinesRunningCount': 123,
        'RoleArn': 'string',
        'State': 'CREATING'|'CREATE_FAILED'|'IDLE'|'STARTING'|'RUNNING'|'RECOVERING'|'STOPPING'|'DELETING'|'DELETED'
    }
    
    
    """
    pass

def describe_input(InputId=None):
    """
    Produces details about an input
    See also: AWS API Documentation
    
    
    :example: response = client.describe_input(
        InputId='string'
    )
    
    
    :type InputId: string
    :param InputId: [REQUIRED] Unique ID of the input

    :rtype: dict
    :return: {
        'Arn': 'string',
        'AttachedChannels': [
            'string',
        ],
        'Destinations': [
            {
                'Ip': 'string',
                'Port': 'string',
                'Url': 'string'
            },
        ],
        'Id': 'string',
        'MediaConnectFlows': [
            {
                'FlowArn': 'string'
            },
        ],
        'Name': 'string',
        'RoleArn': 'string',
        'SecurityGroups': [
            'string',
        ],
        'Sources': [
            {
                'PasswordParam': 'string',
                'Url': 'string',
                'Username': 'string'
            },
        ],
        'State': 'CREATING'|'DETACHED'|'ATTACHED'|'DELETING'|'DELETED',
        'Type': 'UDP_PUSH'|'RTP_PUSH'|'RTMP_PUSH'|'RTMP_PULL'|'URL_PULL'|'MP4_FILE'|'MEDIACONNECT'
    }
    
    
    """
    pass

def describe_input_security_group(InputSecurityGroupId=None):
    """
    Produces a summary of an Input Security Group
    See also: AWS API Documentation
    
    
    :example: response = client.describe_input_security_group(
        InputSecurityGroupId='string'
    )
    
    
    :type InputSecurityGroupId: string
    :param InputSecurityGroupId: [REQUIRED] The id of the Input Security Group to describe

    :rtype: dict
    :return: {
        'Arn': 'string',
        'Id': 'string',
        'Inputs': [
            'string',
        ],
        'State': 'IDLE'|'IN_USE'|'UPDATING'|'DELETED',
        'WhitelistRules': [
            {
                'Cidr': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_offering(OfferingId=None):
    """
    Get details for an offering.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_offering(
        OfferingId='string'
    )
    
    
    :type OfferingId: string
    :param OfferingId: [REQUIRED] Unique offering ID, e.g. '87654321'

    :rtype: dict
    :return: {
        'Arn': 'string',
        'CurrencyCode': 'string',
        'Duration': 123,
        'DurationUnits': 'MONTHS',
        'FixedPrice': 123.0,
        'OfferingDescription': 'string',
        'OfferingId': 'string',
        'OfferingType': 'NO_UPFRONT',
        'Region': 'string',
        'ResourceSpecification': {
            'Codec': 'MPEG2'|'AVC'|'HEVC'|'AUDIO',
            'MaximumBitrate': 'MAX_10_MBPS'|'MAX_20_MBPS'|'MAX_50_MBPS',
            'MaximumFramerate': 'MAX_30_FPS'|'MAX_60_FPS',
            'Resolution': 'SD'|'HD'|'UHD',
            'ResourceType': 'INPUT'|'OUTPUT'|'CHANNEL',
            'SpecialFeature': 'ADVANCED_AUDIO'|'AUDIO_NORMALIZATION',
            'VideoQuality': 'STANDARD'|'ENHANCED'|'PREMIUM'
        },
        'UsagePrice': 123.0
    }
    
    
    """
    pass

def describe_reservation(ReservationId=None):
    """
    Get details for a reservation.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_reservation(
        ReservationId='string'
    )
    
    
    :type ReservationId: string
    :param ReservationId: [REQUIRED] Unique reservation ID, e.g. '1234567'

    :rtype: dict
    :return: {
        'Arn': 'string',
        'Count': 123,
        'CurrencyCode': 'string',
        'Duration': 123,
        'DurationUnits': 'MONTHS',
        'End': 'string',
        'FixedPrice': 123.0,
        'Name': 'string',
        'OfferingDescription': 'string',
        'OfferingId': 'string',
        'OfferingType': 'NO_UPFRONT',
        'Region': 'string',
        'ReservationId': 'string',
        'ResourceSpecification': {
            'Codec': 'MPEG2'|'AVC'|'HEVC'|'AUDIO',
            'MaximumBitrate': 'MAX_10_MBPS'|'MAX_20_MBPS'|'MAX_50_MBPS',
            'MaximumFramerate': 'MAX_30_FPS'|'MAX_60_FPS',
            'Resolution': 'SD'|'HD'|'UHD',
            'ResourceType': 'INPUT'|'OUTPUT'|'CHANNEL',
            'SpecialFeature': 'ADVANCED_AUDIO'|'AUDIO_NORMALIZATION',
            'VideoQuality': 'STANDARD'|'ENHANCED'|'PREMIUM'
        },
        'Start': 'string',
        'State': 'ACTIVE'|'EXPIRED'|'CANCELED'|'DELETED',
        'UsagePrice': 123.0
    }
    
    
    """
    pass

def describe_schedule(ChannelId=None, MaxResults=None, NextToken=None):
    """
    Get a channel schedule
    See also: AWS API Documentation
    
    
    :example: response = client.describe_schedule(
        ChannelId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ChannelId: string
    :param ChannelId: [REQUIRED] Id of the channel whose schedule is being updated.

    :type MaxResults: integer
    :param MaxResults: Placeholder documentation for MaxResults

    :type NextToken: string
    :param NextToken: Placeholder documentation for __string

    :rtype: dict
    :return: {
        'NextToken': 'string',
        'ScheduleActions': [
            {
                'ActionName': 'string',
                'ScheduleActionSettings': {
                    'HlsTimedMetadataSettings': {
                        'Id3': 'string'
                    },
                    'InputSwitchSettings': {
                        'InputAttachmentNameReference': 'string'
                    },
                    'Scte35ReturnToNetworkSettings': {
                        'SpliceEventId': 123
                    },
                    'Scte35SpliceInsertSettings': {
                        'Duration': 123,
                        'SpliceEventId': 123
                    },
                    'Scte35TimeSignalSettings': {
                        'Scte35Descriptors': [
                            {
                                'Scte35DescriptorSettings': {
                                    'SegmentationDescriptorScte35DescriptorSettings': {
                                        'DeliveryRestrictions': {
                                            'ArchiveAllowedFlag': 'ARCHIVE_NOT_ALLOWED'|'ARCHIVE_ALLOWED',
                                            'DeviceRestrictions': 'NONE'|'RESTRICT_GROUP0'|'RESTRICT_GROUP1'|'RESTRICT_GROUP2',
                                            'NoRegionalBlackoutFlag': 'REGIONAL_BLACKOUT'|'NO_REGIONAL_BLACKOUT',
                                            'WebDeliveryAllowedFlag': 'WEB_DELIVERY_NOT_ALLOWED'|'WEB_DELIVERY_ALLOWED'
                                        },
                                        'SegmentNum': 123,
                                        'SegmentationCancelIndicator': 'SEGMENTATION_EVENT_NOT_CANCELED'|'SEGMENTATION_EVENT_CANCELED',
                                        'SegmentationDuration': 123,
                                        'SegmentationEventId': 123,
                                        'SegmentationTypeId': 123,
                                        'SegmentationUpid': 'string',
                                        'SegmentationUpidType': 123,
                                        'SegmentsExpected': 123,
                                        'SubSegmentNum': 123,
                                        'SubSegmentsExpected': 123
                                    }
                                }
                            },
                        ]
                    },
                    'StaticImageActivateSettings': {
                        'Duration': 123,
                        'FadeIn': 123,
                        'FadeOut': 123,
                        'Height': 123,
                        'Image': {
                            'PasswordParam': 'string',
                            'Uri': 'string',
                            'Username': 'string'
                        },
                        'ImageX': 123,
                        'ImageY': 123,
                        'Layer': 123,
                        'Opacity': 123,
                        'Width': 123
                    },
                    'StaticImageDeactivateSettings': {
                        'FadeOut': 123,
                        'Layer': 123
                    }
                },
                'ScheduleActionStartSettings': {
                    'FixedModeScheduleActionStartSettings': {
                        'Time': 'string'
                    },
                    'FollowModeScheduleActionStartSettings': {
                        'FollowPoint': 'END'|'START',
                        'ReferenceActionName': 'string'
                    }
                }
            },
        ]
    }
    
    
    :returns: 
    (dict) -- An array of channel schedule actions.
    NextToken (string) -- The next token; for use in pagination.
    ScheduleActions (list) -- The list of actions in the schedule.
    (dict) -- Contains information on a single schedule action.
    ActionName (string) -- The name of the action, must be unique within the schedule. This name provides the main reference to an action once it is added to the schedule. A name is unique if it is no longer in the schedule. The schedule is automatically cleaned up to remove actions with a start time of more than 1 hour ago (approximately) so at that point a name can be reused.
    ScheduleActionSettings (dict) -- Settings for this schedule action.
    HlsTimedMetadataSettings (dict) -- Settings to emit HLS metadata
    Id3 (string) -- Base64 string formatted according to the ID3 specification: http://id3.org/id3v2.4.0-structure
    
    
    InputSwitchSettings (dict) -- Settings to switch an input
    InputAttachmentNameReference (string) -- The name of the input attachment that should be switched to by this action.
    
    
    Scte35ReturnToNetworkSettings (dict) -- Settings for SCTE-35 return_to_network message
    SpliceEventId (integer) -- The splice_event_id for the SCTE-35 splice_insert, as defined in SCTE-35.
    
    
    Scte35SpliceInsertSettings (dict) -- Settings for SCTE-35 splice_insert message
    Duration (integer) -- Optional, the duration for the splice_insert, in 90 KHz ticks. To convert seconds to ticks, multiple the seconds by 90,000. If you enter a duration, there is an expectation that the downstream system can read the duration and cue in at that time. If you do not enter a duration, the splice_insert will continue indefinitely and there is an expectation that you will enter a return_to_network to end the splice_insert at the appropriate time.
    SpliceEventId (integer) -- The splice_event_id for the SCTE-35 splice_insert, as defined in SCTE-35.
    
    
    Scte35TimeSignalSettings (dict) -- Settings for SCTE-35 time_signal message
    Scte35Descriptors (list) -- The list of SCTE-35 descriptors accompanying the SCTE-35 time_signal.
    (dict) -- Holds one set of SCTE-35 Descriptor Settings.
    Scte35DescriptorSettings (dict) -- SCTE-35 Descriptor Settings.
    SegmentationDescriptorScte35DescriptorSettings (dict) -- SCTE-35 Segmentation Descriptor.
    DeliveryRestrictions (dict) -- Holds the four SCTE-35 delivery restriction parameters.
    ArchiveAllowedFlag (string) -- Corresponds to SCTE-35 archive_allowed_flag.
    DeviceRestrictions (string) -- Corresponds to SCTE-35 device_restrictions parameter.
    NoRegionalBlackoutFlag (string) -- Corresponds to SCTE-35 no_regional_blackout_flag parameter.
    WebDeliveryAllowedFlag (string) -- Corresponds to SCTE-35 web_delivery_allowed_flag parameter.
    
    
    SegmentNum (integer) -- Corresponds to SCTE-35 segment_num. A value that is valid for the specified segmentation_type_id.
    SegmentationCancelIndicator (string) -- Corresponds to SCTE-35 segmentation_event_cancel_indicator.
    SegmentationDuration (integer) -- Corresponds to SCTE-35 segmentation_duration. Optional. The duration for the time_signal, in 90 KHz ticks. To convert seconds to ticks, multiple the seconds by 90,000. Enter time in 90 KHz clock ticks. If you do not enter a duration, the time_signal will continue until you insert a cancellation message.
    SegmentationEventId (integer) -- Corresponds to SCTE-35 segmentation_event_id.
    SegmentationTypeId (integer) -- Corresponds to SCTE-35 segmentation_type_id. One of the segmentation_type_id values listed in the SCTE-35 specification. On the console, enter the ID in decimal (for example, "52"). In the CLI, API, or an SDK, enter the ID in hex (for example, "0x34") or decimal (for example, "52").
    SegmentationUpid (string) -- Corresponds to SCTE-35 segmentation_upid. Enter a string containing the hexadecimal representation of the characters that make up the SCTE-35 segmentation_upid value. Must contain an even number of hex characters. Do not include spaces between each hex pair. For example, the ASCII "ADS Information" becomes hex "41445320496e666f726d6174696f6e.
    SegmentationUpidType (integer) -- Corresponds to SCTE-35 segmentation_upid_type. On the console, enter one of the types listed in the SCTE-35 specification, converted to a decimal. For example, "0x0C" hex from the specification is "12" in decimal. In the CLI, API, or an SDK, enter one of the types listed in the SCTE-35 specification, in either hex (for example, "0x0C" ) or in decimal (for example, "12").
    SegmentsExpected (integer) -- Corresponds to SCTE-35 segments_expected. A value that is valid for the specified segmentation_type_id.
    SubSegmentNum (integer) -- Corresponds to SCTE-35 sub_segment_num. A value that is valid for the specified segmentation_type_id.
    SubSegmentsExpected (integer) -- Corresponds to SCTE-35 sub_segments_expected. A value that is valid for the specified segmentation_type_id.
    
    
    
    
    
    
    
    
    
    
    StaticImageActivateSettings (dict) -- Settings to activate a static image overlay
    Duration (integer) -- The duration in milliseconds for the image to remain on the video. If omitted or set to 0 the duration is unlimited and the image will remain until it is explicitly deactivated.
    FadeIn (integer) -- The time in milliseconds for the image to fade in. The fade-in starts at the start time of the overlay. Default is 0 (no fade-in).
    FadeOut (integer) -- Applies only if a duration is specified. The time in milliseconds for the image to fade out. The fade-out starts when the duration time is hit, so it effectively extends the duration. Default is 0 (no fade-out).
    Height (integer) -- The height of the image when inserted into the video, in pixels. The overlay will be scaled up or down to the specified height. Leave blank to use the native height of the overlay.
    Image (dict) -- The location and filename of the image file to overlay on the video. The file must be a 32-bit BMP, PNG, or TGA file, and must not be larger (in pixels) than the input video.
    PasswordParam (string) -- key used to extract the password from EC2 Parameter store
    Uri (string) -- Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: "rtmp://fmsserver/live".
    Username (string) -- Documentation update needed
    
    
    ImageX (integer) -- Placement of the left edge of the overlay relative to the left edge of the video frame, in pixels. 0 (the default) is the left edge of the frame. If the placement causes the overlay to extend beyond the right edge of the underlying video, then the overlay is cropped on the right.
    ImageY (integer) -- Placement of the top edge of the overlay relative to the top edge of the video frame, in pixels. 0 (the default) is the top edge of the frame. If the placement causes the overlay to extend beyond the bottom edge of the underlying video, then the overlay is cropped on the bottom.
    Layer (integer) -- The number of the layer, 0 to 7. There are 8 layers that can be overlaid on the video, each layer with a different image. The layers are in Z order, which means that overlays with higher values of layer are inserted on top of overlays with lower values of layer. Default is 0.
    Opacity (integer) -- Opacity of image where 0 is transparent and 100 is fully opaque. Default is 100.
    Width (integer) -- The width of the image when inserted into the video, in pixels. The overlay will be scaled up or down to the specified width. Leave blank to use the native width of the overlay.
    
    
    StaticImageDeactivateSettings (dict) -- Settings to deactivate a static image overlay
    FadeOut (integer) -- The time in milliseconds for the image to fade out. Default is 0 (no fade-out).
    Layer (integer) -- The image overlay layer to deactivate, 0 to 7. Default is 0.
    
    
    
    
    ScheduleActionStartSettings (dict) -- The time for the action to start in the channel.
    FixedModeScheduleActionStartSettings (dict) -- Holds the start time for the action.
    Time (string) -- Start time for the action to start in the channel. (Not the time for the action to be added to the schedule: actions are always added to the schedule immediately.) UTC format: yyyy-mm-ddThh:mm:ss.nnnZ. All the letters are digits (for example, mm might be 01) except for the two constants "T" for time and "Z" for "UTC format".
    
    
    FollowModeScheduleActionStartSettings (dict) -- Specifies an action to follow for scheduling this action.
    FollowPoint (string) -- Identifies whether this action starts relative to the start or relative to the end of the reference action.
    ReferenceActionName (string) -- The action name of another action that this one refers to.
    
    
    
    
    
    
    
    
    
    
    
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

def list_channels(MaxResults=None, NextToken=None):
    """
    Produces list of channels that have been created
    See also: AWS API Documentation
    
    
    :example: response = client.list_channels(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: Placeholder documentation for MaxResults

    :type NextToken: string
    :param NextToken: Placeholder documentation for __string

    :rtype: dict
    :return: {
        'Channels': [
            {
                'Arn': 'string',
                'Destinations': [
                    {
                        'Id': 'string',
                        'Settings': [
                            {
                                'PasswordParam': 'string',
                                'StreamName': 'string',
                                'Url': 'string',
                                'Username': 'string'
                            },
                        ]
                    },
                ],
                'EgressEndpoints': [
                    {
                        'SourceIp': 'string'
                    },
                ],
                'Id': 'string',
                'InputAttachments': [
                    {
                        'InputAttachmentName': 'string',
                        'InputId': 'string',
                        'InputSettings': {
                            'AudioSelectors': [
                                {
                                    'Name': 'string',
                                    'SelectorSettings': {
                                        'AudioLanguageSelection': {
                                            'LanguageCode': 'string',
                                            'LanguageSelectionPolicy': 'LOOSE'|'STRICT'
                                        },
                                        'AudioPidSelection': {
                                            'Pid': 123
                                        }
                                    }
                                },
                            ],
                            'CaptionSelectors': [
                                {
                                    'LanguageCode': 'string',
                                    'Name': 'string',
                                    'SelectorSettings': {
                                        'AribSourceSettings': {},
                                        'DvbSubSourceSettings': {
                                            'Pid': 123
                                        },
                                        'EmbeddedSourceSettings': {
                                            'Convert608To708': 'DISABLED'|'UPCONVERT',
                                            'Scte20Detection': 'AUTO'|'OFF',
                                            'Source608ChannelNumber': 123,
                                            'Source608TrackNumber': 123
                                        },
                                        'Scte20SourceSettings': {
                                            'Convert608To708': 'DISABLED'|'UPCONVERT',
                                            'Source608ChannelNumber': 123
                                        },
                                        'Scte27SourceSettings': {
                                            'Pid': 123
                                        },
                                        'TeletextSourceSettings': {
                                            'PageNumber': 'string'
                                        }
                                    }
                                },
                            ],
                            'DeblockFilter': 'DISABLED'|'ENABLED',
                            'DenoiseFilter': 'DISABLED'|'ENABLED',
                            'FilterStrength': 123,
                            'InputFilter': 'AUTO'|'DISABLED'|'FORCED',
                            'NetworkInputSettings': {
                                'HlsInputSettings': {
                                    'Bandwidth': 123,
                                    'BufferSegments': 123,
                                    'Retries': 123,
                                    'RetryInterval': 123
                                },
                                'ServerValidation': 'CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME'|'CHECK_CRYPTOGRAPHY_ONLY'
                            },
                            'SourceEndBehavior': 'CONTINUE'|'LOOP',
                            'VideoSelector': {
                                'ColorSpace': 'FOLLOW'|'REC_601'|'REC_709',
                                'ColorSpaceUsage': 'FALLBACK'|'FORCE',
                                'SelectorSettings': {
                                    'VideoSelectorPid': {
                                        'Pid': 123
                                    },
                                    'VideoSelectorProgramId': {
                                        'ProgramId': 123
                                    }
                                }
                            }
                        }
                    },
                ],
                'InputSpecification': {
                    'Codec': 'MPEG2'|'AVC'|'HEVC',
                    'MaximumBitrate': 'MAX_10_MBPS'|'MAX_20_MBPS'|'MAX_50_MBPS',
                    'Resolution': 'SD'|'HD'|'UHD'
                },
                'LogLevel': 'ERROR'|'WARNING'|'INFO'|'DEBUG'|'DISABLED',
                'Name': 'string',
                'PipelinesRunningCount': 123,
                'RoleArn': 'string',
                'State': 'CREATING'|'CREATE_FAILED'|'IDLE'|'STARTING'|'RUNNING'|'RECOVERING'|'STOPPING'|'DELETING'|'DELETED'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (dict) -- An array of channels
    Channels (list) -- Placeholder documentation for __listOfChannelSummary
    (dict) -- Placeholder documentation for ChannelSummary
    Arn (string) -- The unique arn of the channel.
    Destinations (list) -- A list of destinations of the channel. For UDP outputs, there is one destination per output. For other types (HLS, for example), there is one destination per packager.
    (dict) -- Placeholder documentation for OutputDestination
    Id (string) -- User-specified id. This is used in an output group or an output.
    Settings (list) -- Destination settings for output; one for each redundant encoder.
    (dict) -- Placeholder documentation for OutputDestinationSettings
    PasswordParam (string) -- key used to extract the password from EC2 Parameter store
    StreamName (string) -- Stream name for RTMP destinations (URLs of type rtmp://)
    Url (string) -- A URL specifying a destination
    Username (string) -- username for destination
    
    
    
    
    
    
    
    
    EgressEndpoints (list) -- The endpoints where outgoing connections initiate from
    (dict) -- Placeholder documentation for ChannelEgressEndpoint
    SourceIp (string) -- Public IP of where a channel's output comes from
    
    
    
    
    Id (string) -- The unique id of the channel.
    InputAttachments (list) -- List of input attachments for channel.
    (dict) -- Placeholder documentation for InputAttachment
    InputAttachmentName (string) -- User-specified name for the attachment. This is required if the user wants to use this input in an input switch action.
    InputId (string) -- The ID of the input
    InputSettings (dict) -- Settings of an input (caption selector, etc.)
    AudioSelectors (list) -- Used to select the audio stream to decode for inputs that have multiple available.
    (dict) -- Placeholder documentation for AudioSelector
    Name (string) -- The name of this AudioSelector. AudioDescriptions will use this name to uniquely identify this Selector. Selector names should be unique per input.
    SelectorSettings (dict) -- The audio selector settings.
    AudioLanguageSelection (dict) -- Placeholder documentation for AudioLanguageSelection
    LanguageCode (string) -- Selects a specific three-letter language code from within an audio source.
    LanguageSelectionPolicy (string) -- When set to "strict", the transport stream demux strictly identifies audio streams by their language descriptor. If a PMT update occurs such that an audio stream matching the initially selected language is no longer present then mute will be encoded until the language returns. If "loose", then on a PMT update the demux will choose another audio stream in the program with the same stream type if it can't find one with the same language.
    
    
    AudioPidSelection (dict) -- Placeholder documentation for AudioPidSelection
    Pid (integer) -- Selects a specific PID from within a source.
    
    
    
    
    
    
    
    
    CaptionSelectors (list) -- Used to select the caption input to use for inputs that have multiple available.
    (dict) -- Output groups for this Live Event. Output groups contain information about where streams should be distributed.
    LanguageCode (string) -- When specified this field indicates the three letter language code of the caption track to extract from the source.
    Name (string) -- Name identifier for a caption selector. This name is used to associate this caption selector with one or more caption descriptions. Names must be unique within an event.
    SelectorSettings (dict) -- Caption selector settings.
    AribSourceSettings (dict) -- Placeholder documentation for AribSourceSettings
    DvbSubSourceSettings (dict) -- Placeholder documentation for DvbSubSourceSettings
    Pid (integer) -- When using DVB-Sub with Burn-In or SMPTE-TT, use this PID for the source content. Unused for DVB-Sub passthrough. All DVB-Sub content is passed through, regardless of selectors.
    
    
    EmbeddedSourceSettings (dict) -- Placeholder documentation for EmbeddedSourceSettings
    Convert608To708 (string) -- If upconvert, 608 data is both passed through via the "608 compatibility bytes" fields of the 708 wrapper as well as translated into 708. 708 data present in the source content will be discarded.
    Scte20Detection (string) -- Set to "auto" to handle streams with intermittent and/or non-aligned SCTE-20 and Embedded captions.
    Source608ChannelNumber (integer) -- Specifies the 608/708 channel number within the video track from which to extract captions. Unused for passthrough.
    Source608TrackNumber (integer) -- This field is unused and deprecated.
    
    
    Scte20SourceSettings (dict) -- Placeholder documentation for Scte20SourceSettings
    Convert608To708 (string) -- If upconvert, 608 data is both passed through via the "608 compatibility bytes" fields of the 708 wrapper as well as translated into 708. 708 data present in the source content will be discarded.
    Source608ChannelNumber (integer) -- Specifies the 608/708 channel number within the video track from which to extract captions. Unused for passthrough.
    
    
    Scte27SourceSettings (dict) -- Placeholder documentation for Scte27SourceSettings
    Pid (integer) -- The pid field is used in conjunction with the caption selector languageCode field as follows: - Specify PID and Language: Extracts captions from that PID; the language is "informational". - Specify PID and omit Language: Extracts the specified PID. - Omit PID and specify Language: Extracts the specified language, whichever PID that happens to be. - Omit PID and omit Language: Valid only if source is DVB-Sub that is being passed through; all languages will be passed through.
    
    
    TeletextSourceSettings (dict) -- Placeholder documentation for TeletextSourceSettings
    PageNumber (string) -- Specifies the teletext page number within the data stream from which to extract captions. Range of 0x100 (256) to 0x8FF (2303). Unused for passthrough. Should be specified as a hexadecimal string with no "0x" prefix.
    
    
    
    
    
    
    
    
    DeblockFilter (string) -- Enable or disable the deblock filter when filtering.
    DenoiseFilter (string) -- Enable or disable the denoise filter when filtering.
    FilterStrength (integer) -- Adjusts the magnitude of filtering from 1 (minimal) to 5 (strongest).
    InputFilter (string) -- Turns on the filter for this input. MPEG-2 inputs have the deblocking filter enabled by default. 1) auto - filtering will be applied depending on input type/quality 2) disabled - no filtering will be applied to the input 3) forced - filtering will be applied regardless of input type
    NetworkInputSettings (dict) -- Input settings.
    HlsInputSettings (dict) -- Specifies HLS input settings when the uri is for a HLS manifest.
    Bandwidth (integer) -- When specified the HLS stream with the m3u8 BANDWIDTH that most closely matches this value will be chosen, otherwise the highest bandwidth stream in the m3u8 will be chosen. The bitrate is specified in bits per second, as in an HLS manifest.
    BufferSegments (integer) -- When specified, reading of the HLS input will begin this many buffer segments from the end (most recently written segment). When not specified, the HLS input will begin with the first segment specified in the m3u8.
    Retries (integer) -- The number of consecutive times that attempts to read a manifest or segment must fail before the input is considered unavailable.
    RetryInterval (integer) -- The number of seconds between retries when an attempt to read a manifest or segment fails.
    
    
    ServerValidation (string) -- Check HTTPS server certificates. When set to checkCryptographyOnly, cryptography in the certificate will be checked, but not the server's name. Certain subdomains (notably S3 buckets that use dots in the bucket name) do not strictly match the corresponding certificate's wildcard pattern and would otherwise cause the event to error. This setting is ignored for protocols that do not use https.
    
    
    SourceEndBehavior (string) -- Loop input if it is a file. This allows a file input to be streamed indefinitely.
    VideoSelector (dict) -- Informs which video elementary stream to decode for input types that have multiple available.
    ColorSpace (string) -- Specifies the colorspace of an input. This setting works in tandem with colorSpaceConversion to determine if any conversion will be performed.
    ColorSpaceUsage (string) -- Applies only if colorSpace is a value other than follow. This field controls how the value in the colorSpace field will be used. fallback means that when the input does include color space data, that data will be used, but when the input has no color space data, the value in colorSpace will be used. Choose fallback if your input is sometimes missing color space data, but when it does have color space data, that data is correct. force means to always use the value in colorSpace. Choose force if your input usually has no color space data or might have unreliable color space data.
    SelectorSettings (dict) -- The video selector settings.
    VideoSelectorPid (dict) -- Placeholder documentation for VideoSelectorPid
    Pid (integer) -- Selects a specific PID from within a video source.
    
    
    VideoSelectorProgramId (dict) -- Placeholder documentation for VideoSelectorProgramId
    ProgramId (integer) -- Selects a specific program from within a multi-program transport stream. If the program doesn't exist, the first program within the transport stream will be selected by default.
    
    
    
    
    
    
    
    
    
    
    
    
    InputSpecification (dict) -- Placeholder documentation for InputSpecification
    Codec (string) -- Input codec
    MaximumBitrate (string) -- Maximum input bitrate, categorized coarsely
    Resolution (string) -- Input resolution, categorized coarsely
    
    
    LogLevel (string) -- The log level being written to CloudWatch Logs.
    Name (string) -- The name of the channel. (user-mutable)
    PipelinesRunningCount (integer) -- The number of currently healthy pipelines.
    RoleArn (string) -- The Amazon Resource Name (ARN) of the role assumed when running the Channel.
    State (string) -- Placeholder documentation for ChannelState
    
    
    
    
    NextToken (string) -- Placeholder documentation for __string
    
    
    
    """
    pass

def list_input_security_groups(MaxResults=None, NextToken=None):
    """
    Produces a list of Input Security Groups for an account
    See also: AWS API Documentation
    
    
    :example: response = client.list_input_security_groups(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: Placeholder documentation for MaxResults

    :type NextToken: string
    :param NextToken: Placeholder documentation for __string

    :rtype: dict
    :return: {
        'InputSecurityGroups': [
            {
                'Arn': 'string',
                'Id': 'string',
                'Inputs': [
                    'string',
                ],
                'State': 'IDLE'|'IN_USE'|'UPDATING'|'DELETED',
                'WhitelistRules': [
                    {
                        'Cidr': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (dict) -- An array of Input Security Groups
    InputSecurityGroups (list) -- List of input security groups
    (dict) -- An Input Security Group
    Arn (string) -- Unique ARN of Input Security Group
    Id (string) -- The Id of the Input Security Group
    Inputs (list) -- The list of inputs currently using this Input Security Group.
    (string) -- Placeholder documentation for __string
    
    
    State (string) -- The current state of the Input Security Group.
    WhitelistRules (list) -- Whitelist rules and their sync status
    (dict) -- Whitelist rule
    Cidr (string) -- The IPv4 CIDR that's whitelisted.
    
    
    
    
    
    
    
    
    NextToken (string) -- Placeholder documentation for __string
    
    
    
    """
    pass

def list_inputs(MaxResults=None, NextToken=None):
    """
    Produces list of inputs that have been created
    See also: AWS API Documentation
    
    
    :example: response = client.list_inputs(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: Placeholder documentation for MaxResults

    :type NextToken: string
    :param NextToken: Placeholder documentation for __string

    :rtype: dict
    :return: {
        'Inputs': [
            {
                'Arn': 'string',
                'AttachedChannels': [
                    'string',
                ],
                'Destinations': [
                    {
                        'Ip': 'string',
                        'Port': 'string',
                        'Url': 'string'
                    },
                ],
                'Id': 'string',
                'MediaConnectFlows': [
                    {
                        'FlowArn': 'string'
                    },
                ],
                'Name': 'string',
                'RoleArn': 'string',
                'SecurityGroups': [
                    'string',
                ],
                'Sources': [
                    {
                        'PasswordParam': 'string',
                        'Url': 'string',
                        'Username': 'string'
                    },
                ],
                'State': 'CREATING'|'DETACHED'|'ATTACHED'|'DELETING'|'DELETED',
                'Type': 'UDP_PUSH'|'RTP_PUSH'|'RTMP_PUSH'|'RTMP_PULL'|'URL_PULL'|'MP4_FILE'|'MEDIACONNECT'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (dict) -- An array of inputs
    Inputs (list) -- Placeholder documentation for __listOfInput
    (dict) -- Placeholder documentation for Input
    Arn (string) -- The Unique ARN of the input (generated, immutable).
    AttachedChannels (list) -- A list of channel IDs that that input is attached to (currently an input can only be attached to one channel).
    (string) -- Placeholder documentation for __string
    
    
    Destinations (list) -- A list of the destinations of the input (PUSH-type).
    (dict) -- The settings for a PUSH type input.
    Ip (string) -- The system-generated static IP address of endpoint. It remains fixed for the lifetime of the input.
    Port (string) -- The port number for the input.
    Url (string) -- This represents the endpoint that the customer stream will be pushed to.
    
    
    
    
    Id (string) -- The generated ID of the input (unique for user account, immutable).
    MediaConnectFlows (list) -- A list of MediaConnect Flows for this input.
    (dict) -- The settings for a MediaConnect Flow.
    FlowArn (string) -- The unique ARN of the MediaConnect Flow being used as a source.
    
    
    
    
    Name (string) -- The user-assigned name (This is a mutable value).
    RoleArn (string) -- The Amazon Resource Name (ARN) of the role this input assumes during and after creation.
    SecurityGroups (list) -- A list of IDs for all the security groups attached to the input.
    (string) -- Placeholder documentation for __string
    
    
    Sources (list) -- A list of the sources of the input (PULL-type).
    (dict) -- The settings for a PULL type input.
    PasswordParam (string) -- The key used to extract the password from EC2 Parameter store.
    Url (string) -- This represents the customer's source URL where stream is pulled from.
    Username (string) -- The username for the input source.
    
    
    
    
    State (string) -- Placeholder documentation for InputState
    Type (string) -- Placeholder documentation for InputType
    
    
    
    
    NextToken (string) -- Placeholder documentation for __string
    
    
    
    """
    pass

def list_offerings(ChannelConfiguration=None, Codec=None, MaxResults=None, MaximumBitrate=None, MaximumFramerate=None, NextToken=None, Resolution=None, ResourceType=None, SpecialFeature=None, VideoQuality=None):
    """
    List offerings available for purchase.
    See also: AWS API Documentation
    
    
    :example: response = client.list_offerings(
        ChannelConfiguration='string',
        Codec='string',
        MaxResults=123,
        MaximumBitrate='string',
        MaximumFramerate='string',
        NextToken='string',
        Resolution='string',
        ResourceType='string',
        SpecialFeature='string',
        VideoQuality='string'
    )
    
    
    :type ChannelConfiguration: string
    :param ChannelConfiguration: Filter to offerings that match the configuration of an existing channel, e.g. '2345678' (a channel ID)

    :type Codec: string
    :param Codec: Filter by codec, 'AVC', 'HEVC', 'MPEG2', or 'AUDIO'

    :type MaxResults: integer
    :param MaxResults: Placeholder documentation for MaxResults

    :type MaximumBitrate: string
    :param MaximumBitrate: Filter by bitrate, 'MAX_10_MBPS', 'MAX_20_MBPS', or 'MAX_50_MBPS'

    :type MaximumFramerate: string
    :param MaximumFramerate: Filter by framerate, 'MAX_30_FPS' or 'MAX_60_FPS'

    :type NextToken: string
    :param NextToken: Placeholder documentation for __string

    :type Resolution: string
    :param Resolution: Filter by resolution, 'SD', 'HD', or 'UHD'

    :type ResourceType: string
    :param ResourceType: Filter by resource type, 'INPUT', 'OUTPUT', or 'CHANNEL'

    :type SpecialFeature: string
    :param SpecialFeature: Filter by special feature, 'ADVANCED_AUDIO' or 'AUDIO_NORMALIZATION'

    :type VideoQuality: string
    :param VideoQuality: Filter by video quality, 'STANDARD', 'ENHANCED', or 'PREMIUM'

    :rtype: dict
    :return: {
        'NextToken': 'string',
        'Offerings': [
            {
                'Arn': 'string',
                'CurrencyCode': 'string',
                'Duration': 123,
                'DurationUnits': 'MONTHS',
                'FixedPrice': 123.0,
                'OfferingDescription': 'string',
                'OfferingId': 'string',
                'OfferingType': 'NO_UPFRONT',
                'Region': 'string',
                'ResourceSpecification': {
                    'Codec': 'MPEG2'|'AVC'|'HEVC'|'AUDIO',
                    'MaximumBitrate': 'MAX_10_MBPS'|'MAX_20_MBPS'|'MAX_50_MBPS',
                    'MaximumFramerate': 'MAX_30_FPS'|'MAX_60_FPS',
                    'Resolution': 'SD'|'HD'|'UHD',
                    'ResourceType': 'INPUT'|'OUTPUT'|'CHANNEL',
                    'SpecialFeature': 'ADVANCED_AUDIO'|'AUDIO_NORMALIZATION',
                    'VideoQuality': 'STANDARD'|'ENHANCED'|'PREMIUM'
                },
                'UsagePrice': 123.0
            },
        ]
    }
    
    
    :returns: 
    (dict) -- List of offerings
    NextToken (string) -- Token to retrieve the next page of results
    Offerings (list) -- List of offerings
    (dict) -- Reserved resources available for purchase
    Arn (string) -- Unique offering ARN, e.g. 'arn:aws:medialive:us-west-2:123456789012:offering:87654321'
    CurrencyCode (string) -- Currency code for usagePrice and fixedPrice in ISO-4217 format, e.g. 'USD'
    Duration (integer) -- Lease duration, e.g. '12'
    DurationUnits (string) -- Units for duration, e.g. 'MONTHS'
    FixedPrice (float) -- One-time charge for each reserved resource, e.g. '0.0' for a NO_UPFRONT offering
    OfferingDescription (string) -- Offering description, e.g. 'HD AVC output at 10-20 Mbps, 30 fps, and standard VQ in US West (Oregon)'
    OfferingId (string) -- Unique offering ID, e.g. '87654321'
    OfferingType (string) -- Offering type, e.g. 'NO_UPFRONT'
    Region (string) -- AWS region, e.g. 'us-west-2'
    ResourceSpecification (dict) -- Resource configuration details
    Codec (string) -- Codec, e.g. 'AVC'
    MaximumBitrate (string) -- Maximum bitrate, e.g. 'MAX_20_MBPS'
    MaximumFramerate (string) -- Maximum framerate, e.g. 'MAX_30_FPS' (Outputs only)
    Resolution (string) -- Resolution, e.g. 'HD'
    ResourceType (string) -- Resource type, 'INPUT', 'OUTPUT', or 'CHANNEL'
    SpecialFeature (string) -- Special feature, e.g. 'AUDIO_NORMALIZATION' (Channels only)
    VideoQuality (string) -- Video quality, e.g. 'STANDARD' (Outputs only)
    
    
    UsagePrice (float) -- Recurring usage charge for each reserved resource, e.g. '157.0'
    
    
    
    
    
    
    
    """
    pass

def list_reservations(Codec=None, MaxResults=None, MaximumBitrate=None, MaximumFramerate=None, NextToken=None, Resolution=None, ResourceType=None, SpecialFeature=None, VideoQuality=None):
    """
    List purchased reservations.
    See also: AWS API Documentation
    
    
    :example: response = client.list_reservations(
        Codec='string',
        MaxResults=123,
        MaximumBitrate='string',
        MaximumFramerate='string',
        NextToken='string',
        Resolution='string',
        ResourceType='string',
        SpecialFeature='string',
        VideoQuality='string'
    )
    
    
    :type Codec: string
    :param Codec: Filter by codec, 'AVC', 'HEVC', 'MPEG2', or 'AUDIO'

    :type MaxResults: integer
    :param MaxResults: Placeholder documentation for MaxResults

    :type MaximumBitrate: string
    :param MaximumBitrate: Filter by bitrate, 'MAX_10_MBPS', 'MAX_20_MBPS', or 'MAX_50_MBPS'

    :type MaximumFramerate: string
    :param MaximumFramerate: Filter by framerate, 'MAX_30_FPS' or 'MAX_60_FPS'

    :type NextToken: string
    :param NextToken: Placeholder documentation for __string

    :type Resolution: string
    :param Resolution: Filter by resolution, 'SD', 'HD', or 'UHD'

    :type ResourceType: string
    :param ResourceType: Filter by resource type, 'INPUT', 'OUTPUT', or 'CHANNEL'

    :type SpecialFeature: string
    :param SpecialFeature: Filter by special feature, 'ADVANCED_AUDIO' or 'AUDIO_NORMALIZATION'

    :type VideoQuality: string
    :param VideoQuality: Filter by video quality, 'STANDARD', 'ENHANCED', or 'PREMIUM'

    :rtype: dict
    :return: {
        'NextToken': 'string',
        'Reservations': [
            {
                'Arn': 'string',
                'Count': 123,
                'CurrencyCode': 'string',
                'Duration': 123,
                'DurationUnits': 'MONTHS',
                'End': 'string',
                'FixedPrice': 123.0,
                'Name': 'string',
                'OfferingDescription': 'string',
                'OfferingId': 'string',
                'OfferingType': 'NO_UPFRONT',
                'Region': 'string',
                'ReservationId': 'string',
                'ResourceSpecification': {
                    'Codec': 'MPEG2'|'AVC'|'HEVC'|'AUDIO',
                    'MaximumBitrate': 'MAX_10_MBPS'|'MAX_20_MBPS'|'MAX_50_MBPS',
                    'MaximumFramerate': 'MAX_30_FPS'|'MAX_60_FPS',
                    'Resolution': 'SD'|'HD'|'UHD',
                    'ResourceType': 'INPUT'|'OUTPUT'|'CHANNEL',
                    'SpecialFeature': 'ADVANCED_AUDIO'|'AUDIO_NORMALIZATION',
                    'VideoQuality': 'STANDARD'|'ENHANCED'|'PREMIUM'
                },
                'Start': 'string',
                'State': 'ACTIVE'|'EXPIRED'|'CANCELED'|'DELETED',
                'UsagePrice': 123.0
            },
        ]
    }
    
    
    :returns: 
    (dict) -- List of reservations
    NextToken (string) -- Token to retrieve the next page of results
    Reservations (list) -- List of reservations
    (dict) -- Reserved resources available to use
    Arn (string) -- Unique reservation ARN, e.g. 'arn:aws:medialive:us-west-2:123456789012:reservation:1234567'
    Count (integer) -- Number of reserved resources
    CurrencyCode (string) -- Currency code for usagePrice and fixedPrice in ISO-4217 format, e.g. 'USD'
    Duration (integer) -- Lease duration, e.g. '12'
    DurationUnits (string) -- Units for duration, e.g. 'MONTHS'
    End (string) -- Reservation UTC end date and time in ISO-8601 format, e.g. '2019-03-01T00:00:00'
    FixedPrice (float) -- One-time charge for each reserved resource, e.g. '0.0' for a NO_UPFRONT offering
    Name (string) -- User specified reservation name
    OfferingDescription (string) -- Offering description, e.g. 'HD AVC output at 10-20 Mbps, 30 fps, and standard VQ in US West (Oregon)'
    OfferingId (string) -- Unique offering ID, e.g. '87654321'
    OfferingType (string) -- Offering type, e.g. 'NO_UPFRONT'
    Region (string) -- AWS region, e.g. 'us-west-2'
    ReservationId (string) -- Unique reservation ID, e.g. '1234567'
    ResourceSpecification (dict) -- Resource configuration details
    Codec (string) -- Codec, e.g. 'AVC'
    MaximumBitrate (string) -- Maximum bitrate, e.g. 'MAX_20_MBPS'
    MaximumFramerate (string) -- Maximum framerate, e.g. 'MAX_30_FPS' (Outputs only)
    Resolution (string) -- Resolution, e.g. 'HD'
    ResourceType (string) -- Resource type, 'INPUT', 'OUTPUT', or 'CHANNEL'
    SpecialFeature (string) -- Special feature, e.g. 'AUDIO_NORMALIZATION' (Channels only)
    VideoQuality (string) -- Video quality, e.g. 'STANDARD' (Outputs only)
    
    
    Start (string) -- Reservation UTC start date and time in ISO-8601 format, e.g. '2018-03-01T00:00:00'
    State (string) -- Current state of reservation, e.g. 'ACTIVE'
    UsagePrice (float) -- Recurring usage charge for each reserved resource, e.g. '157.0'
    
    
    
    
    
    
    
    """
    pass

def purchase_offering(Count=None, Name=None, OfferingId=None, RequestId=None, Start=None):
    """
    Purchase an offering and create a reservation.
    See also: AWS API Documentation
    
    
    :example: response = client.purchase_offering(
        Count=123,
        Name='string',
        OfferingId='string',
        RequestId='string',
        Start='string'
    )
    
    
    :type Count: integer
    :param Count: [REQUIRED] Number of resources

    :type Name: string
    :param Name: Name for the new reservation

    :type OfferingId: string
    :param OfferingId: [REQUIRED] Offering to purchase, e.g. '87654321'

    :type RequestId: string
    :param RequestId: Unique request ID to be specified. This is needed to prevent retries from creating multiple resources.This field is autopopulated if not provided.

    :type Start: string
    :param Start: Requested reservation start time (UTC) in ISO-8601 format. The specified time must be between the first day of the current month and one year from now. If no value is given, the default is now.

    :rtype: dict
    :return: {
        'Reservation': {
            'Arn': 'string',
            'Count': 123,
            'CurrencyCode': 'string',
            'Duration': 123,
            'DurationUnits': 'MONTHS',
            'End': 'string',
            'FixedPrice': 123.0,
            'Name': 'string',
            'OfferingDescription': 'string',
            'OfferingId': 'string',
            'OfferingType': 'NO_UPFRONT',
            'Region': 'string',
            'ReservationId': 'string',
            'ResourceSpecification': {
                'Codec': 'MPEG2'|'AVC'|'HEVC'|'AUDIO',
                'MaximumBitrate': 'MAX_10_MBPS'|'MAX_20_MBPS'|'MAX_50_MBPS',
                'MaximumFramerate': 'MAX_30_FPS'|'MAX_60_FPS',
                'Resolution': 'SD'|'HD'|'UHD',
                'ResourceType': 'INPUT'|'OUTPUT'|'CHANNEL',
                'SpecialFeature': 'ADVANCED_AUDIO'|'AUDIO_NORMALIZATION',
                'VideoQuality': 'STANDARD'|'ENHANCED'|'PREMIUM'
            },
            'Start': 'string',
            'State': 'ACTIVE'|'EXPIRED'|'CANCELED'|'DELETED',
            'UsagePrice': 123.0
        }
    }
    
    
    :returns: 
    (dict) -- Purchased reservation
    Reservation (dict) -- Reserved resources available to use
    Arn (string) -- Unique reservation ARN, e.g. 'arn:aws:medialive:us-west-2:123456789012:reservation:1234567'
    Count (integer) -- Number of reserved resources
    CurrencyCode (string) -- Currency code for usagePrice and fixedPrice in ISO-4217 format, e.g. 'USD'
    Duration (integer) -- Lease duration, e.g. '12'
    DurationUnits (string) -- Units for duration, e.g. 'MONTHS'
    End (string) -- Reservation UTC end date and time in ISO-8601 format, e.g. '2019-03-01T00:00:00'
    FixedPrice (float) -- One-time charge for each reserved resource, e.g. '0.0' for a NO_UPFRONT offering
    Name (string) -- User specified reservation name
    OfferingDescription (string) -- Offering description, e.g. 'HD AVC output at 10-20 Mbps, 30 fps, and standard VQ in US West (Oregon)'
    OfferingId (string) -- Unique offering ID, e.g. '87654321'
    OfferingType (string) -- Offering type, e.g. 'NO_UPFRONT'
    Region (string) -- AWS region, e.g. 'us-west-2'
    ReservationId (string) -- Unique reservation ID, e.g. '1234567'
    ResourceSpecification (dict) -- Resource configuration details
    Codec (string) -- Codec, e.g. 'AVC'
    MaximumBitrate (string) -- Maximum bitrate, e.g. 'MAX_20_MBPS'
    MaximumFramerate (string) -- Maximum framerate, e.g. 'MAX_30_FPS' (Outputs only)
    Resolution (string) -- Resolution, e.g. 'HD'
    ResourceType (string) -- Resource type, 'INPUT', 'OUTPUT', or 'CHANNEL'
    SpecialFeature (string) -- Special feature, e.g. 'AUDIO_NORMALIZATION' (Channels only)
    VideoQuality (string) -- Video quality, e.g. 'STANDARD' (Outputs only)
    
    
    Start (string) -- Reservation UTC start date and time in ISO-8601 format, e.g. '2018-03-01T00:00:00'
    State (string) -- Current state of reservation, e.g. 'ACTIVE'
    UsagePrice (float) -- Recurring usage charge for each reserved resource, e.g. '157.0'
    
    
    
    
    
    """
    pass

def start_channel(ChannelId=None):
    """
    Starts an existing channel
    See also: AWS API Documentation
    
    
    :example: response = client.start_channel(
        ChannelId='string'
    )
    
    
    :type ChannelId: string
    :param ChannelId: [REQUIRED] A request to start a channel

    :rtype: dict
    :return: {
        'Arn': 'string',
        'Destinations': [
            {
                'Id': 'string',
                'Settings': [
                    {
                        'PasswordParam': 'string',
                        'StreamName': 'string',
                        'Url': 'string',
                        'Username': 'string'
                    },
                ]
            },
        ],
        'EgressEndpoints': [
            {
                'SourceIp': 'string'
            },
        ],
        'EncoderSettings': {
            'AudioDescriptions': [
                {
                    'AudioNormalizationSettings': {
                        'Algorithm': 'ITU_1770_1'|'ITU_1770_2',
                        'AlgorithmControl': 'CORRECT_AUDIO',
                        'TargetLkfs': 123.0
                    },
                    'AudioSelectorName': 'string',
                    'AudioType': 'CLEAN_EFFECTS'|'HEARING_IMPAIRED'|'UNDEFINED'|'VISUAL_IMPAIRED_COMMENTARY',
                    'AudioTypeControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                    'CodecSettings': {
                        'AacSettings': {
                            'Bitrate': 123.0,
                            'CodingMode': 'AD_RECEIVER_MIX'|'CODING_MODE_1_0'|'CODING_MODE_1_1'|'CODING_MODE_2_0'|'CODING_MODE_5_1',
                            'InputType': 'BROADCASTER_MIXED_AD'|'NORMAL',
                            'Profile': 'HEV1'|'HEV2'|'LC',
                            'RateControlMode': 'CBR'|'VBR',
                            'RawFormat': 'LATM_LOAS'|'NONE',
                            'SampleRate': 123.0,
                            'Spec': 'MPEG2'|'MPEG4',
                            'VbrQuality': 'HIGH'|'LOW'|'MEDIUM_HIGH'|'MEDIUM_LOW'
                        },
                        'Ac3Settings': {
                            'Bitrate': 123.0,
                            'BitstreamMode': 'COMMENTARY'|'COMPLETE_MAIN'|'DIALOGUE'|'EMERGENCY'|'HEARING_IMPAIRED'|'MUSIC_AND_EFFECTS'|'VISUALLY_IMPAIRED'|'VOICE_OVER',
                            'CodingMode': 'CODING_MODE_1_0'|'CODING_MODE_1_1'|'CODING_MODE_2_0'|'CODING_MODE_3_2_LFE',
                            'Dialnorm': 123,
                            'DrcProfile': 'FILM_STANDARD'|'NONE',
                            'LfeFilter': 'DISABLED'|'ENABLED',
                            'MetadataControl': 'FOLLOW_INPUT'|'USE_CONFIGURED'
                        },
                        'Eac3Settings': {
                            'AttenuationControl': 'ATTENUATE_3_DB'|'NONE',
                            'Bitrate': 123.0,
                            'BitstreamMode': 'COMMENTARY'|'COMPLETE_MAIN'|'EMERGENCY'|'HEARING_IMPAIRED'|'VISUALLY_IMPAIRED',
                            'CodingMode': 'CODING_MODE_1_0'|'CODING_MODE_2_0'|'CODING_MODE_3_2',
                            'DcFilter': 'DISABLED'|'ENABLED',
                            'Dialnorm': 123,
                            'DrcLine': 'FILM_LIGHT'|'FILM_STANDARD'|'MUSIC_LIGHT'|'MUSIC_STANDARD'|'NONE'|'SPEECH',
                            'DrcRf': 'FILM_LIGHT'|'FILM_STANDARD'|'MUSIC_LIGHT'|'MUSIC_STANDARD'|'NONE'|'SPEECH',
                            'LfeControl': 'LFE'|'NO_LFE',
                            'LfeFilter': 'DISABLED'|'ENABLED',
                            'LoRoCenterMixLevel': 123.0,
                            'LoRoSurroundMixLevel': 123.0,
                            'LtRtCenterMixLevel': 123.0,
                            'LtRtSurroundMixLevel': 123.0,
                            'MetadataControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                            'PassthroughControl': 'NO_PASSTHROUGH'|'WHEN_POSSIBLE',
                            'PhaseControl': 'NO_SHIFT'|'SHIFT_90_DEGREES',
                            'StereoDownmix': 'DPL2'|'LO_RO'|'LT_RT'|'NOT_INDICATED',
                            'SurroundExMode': 'DISABLED'|'ENABLED'|'NOT_INDICATED',
                            'SurroundMode': 'DISABLED'|'ENABLED'|'NOT_INDICATED'
                        },
                        'Mp2Settings': {
                            'Bitrate': 123.0,
                            'CodingMode': 'CODING_MODE_1_0'|'CODING_MODE_2_0',
                            'SampleRate': 123.0
                        },
                        'PassThroughSettings': {}
                    },
                    'LanguageCode': 'string',
                    'LanguageCodeControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                    'Name': 'string',
                    'RemixSettings': {
                        'ChannelMappings': [
                            {
                                'InputChannelLevels': [
                                    {
                                        'Gain': 123,
                                        'InputChannel': 123
                                    },
                                ],
                                'OutputChannel': 123
                            },
                        ],
                        'ChannelsIn': 123,
                        'ChannelsOut': 123
                    },
                    'StreamName': 'string'
                },
            ],
            'AvailBlanking': {
                'AvailBlankingImage': {
                    'PasswordParam': 'string',
                    'Uri': 'string',
                    'Username': 'string'
                },
                'State': 'DISABLED'|'ENABLED'
            },
            'AvailConfiguration': {
                'AvailSettings': {
                    'Scte35SpliceInsert': {
                        'AdAvailOffset': 123,
                        'NoRegionalBlackoutFlag': 'FOLLOW'|'IGNORE',
                        'WebDeliveryAllowedFlag': 'FOLLOW'|'IGNORE'
                    },
                    'Scte35TimeSignalApos': {
                        'AdAvailOffset': 123,
                        'NoRegionalBlackoutFlag': 'FOLLOW'|'IGNORE',
                        'WebDeliveryAllowedFlag': 'FOLLOW'|'IGNORE'
                    }
                }
            },
            'BlackoutSlate': {
                'BlackoutSlateImage': {
                    'PasswordParam': 'string',
                    'Uri': 'string',
                    'Username': 'string'
                },
                'NetworkEndBlackout': 'DISABLED'|'ENABLED',
                'NetworkEndBlackoutImage': {
                    'PasswordParam': 'string',
                    'Uri': 'string',
                    'Username': 'string'
                },
                'NetworkId': 'string',
                'State': 'DISABLED'|'ENABLED'
            },
            'CaptionDescriptions': [
                {
                    'CaptionSelectorName': 'string',
                    'DestinationSettings': {
                        'AribDestinationSettings': {},
                        'BurnInDestinationSettings': {
                            'Alignment': 'CENTERED'|'LEFT'|'SMART',
                            'BackgroundColor': 'BLACK'|'NONE'|'WHITE',
                            'BackgroundOpacity': 123,
                            'Font': {
                                'PasswordParam': 'string',
                                'Uri': 'string',
                                'Username': 'string'
                            },
                            'FontColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                            'FontOpacity': 123,
                            'FontResolution': 123,
                            'FontSize': 'string',
                            'OutlineColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                            'OutlineSize': 123,
                            'ShadowColor': 'BLACK'|'NONE'|'WHITE',
                            'ShadowOpacity': 123,
                            'ShadowXOffset': 123,
                            'ShadowYOffset': 123,
                            'TeletextGridControl': 'FIXED'|'SCALED',
                            'XPosition': 123,
                            'YPosition': 123
                        },
                        'DvbSubDestinationSettings': {
                            'Alignment': 'CENTERED'|'LEFT'|'SMART',
                            'BackgroundColor': 'BLACK'|'NONE'|'WHITE',
                            'BackgroundOpacity': 123,
                            'Font': {
                                'PasswordParam': 'string',
                                'Uri': 'string',
                                'Username': 'string'
                            },
                            'FontColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                            'FontOpacity': 123,
                            'FontResolution': 123,
                            'FontSize': 'string',
                            'OutlineColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                            'OutlineSize': 123,
                            'ShadowColor': 'BLACK'|'NONE'|'WHITE',
                            'ShadowOpacity': 123,
                            'ShadowXOffset': 123,
                            'ShadowYOffset': 123,
                            'TeletextGridControl': 'FIXED'|'SCALED',
                            'XPosition': 123,
                            'YPosition': 123
                        },
                        'EmbeddedDestinationSettings': {},
                        'EmbeddedPlusScte20DestinationSettings': {},
                        'RtmpCaptionInfoDestinationSettings': {},
                        'Scte20PlusEmbeddedDestinationSettings': {},
                        'Scte27DestinationSettings': {},
                        'SmpteTtDestinationSettings': {},
                        'TeletextDestinationSettings': {},
                        'TtmlDestinationSettings': {
                            'StyleControl': 'PASSTHROUGH'|'USE_CONFIGURED'
                        },
                        'WebvttDestinationSettings': {}
                    },
                    'LanguageCode': 'string',
                    'LanguageDescription': 'string',
                    'Name': 'string'
                },
            ],
            'GlobalConfiguration': {
                'InitialAudioGain': 123,
                'InputEndAction': 'NONE'|'SWITCH_AND_LOOP_INPUTS',
                'InputLossBehavior': {
                    'BlackFrameMsec': 123,
                    'InputLossImageColor': 'string',
                    'InputLossImageSlate': {
                        'PasswordParam': 'string',
                        'Uri': 'string',
                        'Username': 'string'
                    },
                    'InputLossImageType': 'COLOR'|'SLATE',
                    'RepeatFrameMsec': 123
                },
                'OutputTimingSource': 'INPUT_CLOCK'|'SYSTEM_CLOCK',
                'SupportLowFramerateInputs': 'DISABLED'|'ENABLED'
            },
            'OutputGroups': [
                {
                    'Name': 'string',
                    'OutputGroupSettings': {
                        'ArchiveGroupSettings': {
                            'Destination': {
                                'DestinationRefId': 'string'
                            },
                            'RolloverInterval': 123
                        },
                        'HlsGroupSettings': {
                            'AdMarkers': [
                                'ADOBE'|'ELEMENTAL'|'ELEMENTAL_SCTE35',
                            ],
                            'BaseUrlContent': 'string',
                            'BaseUrlManifest': 'string',
                            'CaptionLanguageMappings': [
                                {
                                    'CaptionChannel': 123,
                                    'LanguageCode': 'string',
                                    'LanguageDescription': 'string'
                                },
                            ],
                            'CaptionLanguageSetting': 'INSERT'|'NONE'|'OMIT',
                            'ClientCache': 'DISABLED'|'ENABLED',
                            'CodecSpecification': 'RFC_4281'|'RFC_6381',
                            'ConstantIv': 'string',
                            'Destination': {
                                'DestinationRefId': 'string'
                            },
                            'DirectoryStructure': 'SINGLE_DIRECTORY'|'SUBDIRECTORY_PER_STREAM',
                            'EncryptionType': 'AES128'|'SAMPLE_AES',
                            'HlsCdnSettings': {
                                'HlsAkamaiSettings': {
                                    'ConnectionRetryInterval': 123,
                                    'FilecacheDuration': 123,
                                    'HttpTransferMode': 'CHUNKED'|'NON_CHUNKED',
                                    'NumRetries': 123,
                                    'RestartDelay': 123,
                                    'Salt': 'string',
                                    'Token': 'string'
                                },
                                'HlsBasicPutSettings': {
                                    'ConnectionRetryInterval': 123,
                                    'FilecacheDuration': 123,
                                    'NumRetries': 123,
                                    'RestartDelay': 123
                                },
                                'HlsMediaStoreSettings': {
                                    'ConnectionRetryInterval': 123,
                                    'FilecacheDuration': 123,
                                    'MediaStoreStorageClass': 'TEMPORAL',
                                    'NumRetries': 123,
                                    'RestartDelay': 123
                                },
                                'HlsWebdavSettings': {
                                    'ConnectionRetryInterval': 123,
                                    'FilecacheDuration': 123,
                                    'HttpTransferMode': 'CHUNKED'|'NON_CHUNKED',
                                    'NumRetries': 123,
                                    'RestartDelay': 123
                                }
                            },
                            'IndexNSegments': 123,
                            'InputLossAction': 'EMIT_OUTPUT'|'PAUSE_OUTPUT',
                            'IvInManifest': 'EXCLUDE'|'INCLUDE',
                            'IvSource': 'EXPLICIT'|'FOLLOWS_SEGMENT_NUMBER',
                            'KeepSegments': 123,
                            'KeyFormat': 'string',
                            'KeyFormatVersions': 'string',
                            'KeyProviderSettings': {
                                'StaticKeySettings': {
                                    'KeyProviderServer': {
                                        'PasswordParam': 'string',
                                        'Uri': 'string',
                                        'Username': 'string'
                                    },
                                    'StaticKeyValue': 'string'
                                }
                            },
                            'ManifestCompression': 'GZIP'|'NONE',
                            'ManifestDurationFormat': 'FLOATING_POINT'|'INTEGER',
                            'MinSegmentLength': 123,
                            'Mode': 'LIVE'|'VOD',
                            'OutputSelection': 'MANIFESTS_AND_SEGMENTS'|'SEGMENTS_ONLY',
                            'ProgramDateTime': 'EXCLUDE'|'INCLUDE',
                            'ProgramDateTimePeriod': 123,
                            'RedundantManifest': 'DISABLED'|'ENABLED',
                            'SegmentLength': 123,
                            'SegmentationMode': 'USE_INPUT_SEGMENTATION'|'USE_SEGMENT_DURATION',
                            'SegmentsPerSubdirectory': 123,
                            'StreamInfResolution': 'EXCLUDE'|'INCLUDE',
                            'TimedMetadataId3Frame': 'NONE'|'PRIV'|'TDRL',
                            'TimedMetadataId3Period': 123,
                            'TimestampDeltaMilliseconds': 123,
                            'TsFileMode': 'SEGMENTED_FILES'|'SINGLE_FILE'
                        },
                        'MsSmoothGroupSettings': {
                            'AcquisitionPointId': 'string',
                            'AudioOnlyTimecodeControl': 'PASSTHROUGH'|'USE_CONFIGURED_CLOCK',
                            'CertificateMode': 'SELF_SIGNED'|'VERIFY_AUTHENTICITY',
                            'ConnectionRetryInterval': 123,
                            'Destination': {
                                'DestinationRefId': 'string'
                            },
                            'EventId': 'string',
                            'EventIdMode': 'NO_EVENT_ID'|'USE_CONFIGURED'|'USE_TIMESTAMP',
                            'EventStopBehavior': 'NONE'|'SEND_EOS',
                            'FilecacheDuration': 123,
                            'FragmentLength': 123,
                            'InputLossAction': 'EMIT_OUTPUT'|'PAUSE_OUTPUT',
                            'NumRetries': 123,
                            'RestartDelay': 123,
                            'SegmentationMode': 'USE_INPUT_SEGMENTATION'|'USE_SEGMENT_DURATION',
                            'SendDelayMs': 123,
                            'SparseTrackType': 'NONE'|'SCTE_35',
                            'StreamManifestBehavior': 'DO_NOT_SEND'|'SEND',
                            'TimestampOffset': 'string',
                            'TimestampOffsetMode': 'USE_CONFIGURED_OFFSET'|'USE_EVENT_START_DATE'
                        },
                        'RtmpGroupSettings': {
                            'AuthenticationScheme': 'AKAMAI'|'COMMON',
                            'CacheFullBehavior': 'DISCONNECT_IMMEDIATELY'|'WAIT_FOR_SERVER',
                            'CacheLength': 123,
                            'CaptionData': 'ALL'|'FIELD1_608'|'FIELD1_AND_FIELD2_608',
                            'InputLossAction': 'EMIT_OUTPUT'|'PAUSE_OUTPUT',
                            'RestartDelay': 123
                        },
                        'UdpGroupSettings': {
                            'InputLossAction': 'DROP_PROGRAM'|'DROP_TS'|'EMIT_PROGRAM',
                            'TimedMetadataId3Frame': 'NONE'|'PRIV'|'TDRL',
                            'TimedMetadataId3Period': 123
                        }
                    },
                    'Outputs': [
                        {
                            'AudioDescriptionNames': [
                                'string',
                            ],
                            'CaptionDescriptionNames': [
                                'string',
                            ],
                            'OutputName': 'string',
                            'OutputSettings': {
                                'ArchiveOutputSettings': {
                                    'ContainerSettings': {
                                        'M2tsSettings': {
                                            'AbsentInputAudioBehavior': 'DROP'|'ENCODE_SILENCE',
                                            'Arib': 'DISABLED'|'ENABLED',
                                            'AribCaptionsPid': 'string',
                                            'AribCaptionsPidControl': 'AUTO'|'USE_CONFIGURED',
                                            'AudioBufferModel': 'ATSC'|'DVB',
                                            'AudioFramesPerPes': 123,
                                            'AudioPids': 'string',
                                            'AudioStreamType': 'ATSC'|'DVB',
                                            'Bitrate': 123,
                                            'BufferModel': 'MULTIPLEX'|'NONE',
                                            'CcDescriptor': 'DISABLED'|'ENABLED',
                                            'DvbNitSettings': {
                                                'NetworkId': 123,
                                                'NetworkName': 'string',
                                                'RepInterval': 123
                                            },
                                            'DvbSdtSettings': {
                                                'OutputSdt': 'SDT_FOLLOW'|'SDT_FOLLOW_IF_PRESENT'|'SDT_MANUAL'|'SDT_NONE',
                                                'RepInterval': 123,
                                                'ServiceName': 'string',
                                                'ServiceProviderName': 'string'
                                            },
                                            'DvbSubPids': 'string',
                                            'DvbTdtSettings': {
                                                'RepInterval': 123
                                            },
                                            'DvbTeletextPid': 'string',
                                            'Ebif': 'NONE'|'PASSTHROUGH',
                                            'EbpAudioInterval': 'VIDEO_AND_FIXED_INTERVALS'|'VIDEO_INTERVAL',
                                            'EbpLookaheadMs': 123,
                                            'EbpPlacement': 'VIDEO_AND_AUDIO_PIDS'|'VIDEO_PID',
                                            'EcmPid': 'string',
                                            'EsRateInPes': 'EXCLUDE'|'INCLUDE',
                                            'EtvPlatformPid': 'string',
                                            'EtvSignalPid': 'string',
                                            'FragmentTime': 123.0,
                                            'Klv': 'NONE'|'PASSTHROUGH',
                                            'KlvDataPids': 'string',
                                            'NullPacketBitrate': 123.0,
                                            'PatInterval': 123,
                                            'PcrControl': 'CONFIGURED_PCR_PERIOD'|'PCR_EVERY_PES_PACKET',
                                            'PcrPeriod': 123,
                                            'PcrPid': 'string',
                                            'PmtInterval': 123,
                                            'PmtPid': 'string',
                                            'ProgramNum': 123,
                                            'RateMode': 'CBR'|'VBR',
                                            'Scte27Pids': 'string',
                                            'Scte35Control': 'NONE'|'PASSTHROUGH',
                                            'Scte35Pid': 'string',
                                            'SegmentationMarkers': 'EBP'|'EBP_LEGACY'|'NONE'|'PSI_SEGSTART'|'RAI_ADAPT'|'RAI_SEGSTART',
                                            'SegmentationStyle': 'MAINTAIN_CADENCE'|'RESET_CADENCE',
                                            'SegmentationTime': 123.0,
                                            'TimedMetadataBehavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                            'TimedMetadataPid': 'string',
                                            'TransportStreamId': 123,
                                            'VideoPid': 'string'
                                        }
                                    },
                                    'Extension': 'string',
                                    'NameModifier': 'string'
                                },
                                'HlsOutputSettings': {
                                    'HlsSettings': {
                                        'AudioOnlyHlsSettings': {
                                            'AudioGroupId': 'string',
                                            'AudioOnlyImage': {
                                                'PasswordParam': 'string',
                                                'Uri': 'string',
                                                'Username': 'string'
                                            },
                                            'AudioTrackType': 'ALTERNATE_AUDIO_AUTO_SELECT'|'ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT'|'ALTERNATE_AUDIO_NOT_AUTO_SELECT'|'AUDIO_ONLY_VARIANT_STREAM'
                                        },
                                        'StandardHlsSettings': {
                                            'AudioRenditionSets': 'string',
                                            'M3u8Settings': {
                                                'AudioFramesPerPes': 123,
                                                'AudioPids': 'string',
                                                'EcmPid': 'string',
                                                'PatInterval': 123,
                                                'PcrControl': 'CONFIGURED_PCR_PERIOD'|'PCR_EVERY_PES_PACKET',
                                                'PcrPeriod': 123,
                                                'PcrPid': 'string',
                                                'PmtInterval': 123,
                                                'PmtPid': 'string',
                                                'ProgramNum': 123,
                                                'Scte35Behavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                                'Scte35Pid': 'string',
                                                'TimedMetadataBehavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                                'TimedMetadataPid': 'string',
                                                'TransportStreamId': 123,
                                                'VideoPid': 'string'
                                            }
                                        }
                                    },
                                    'NameModifier': 'string',
                                    'SegmentModifier': 'string'
                                },
                                'MsSmoothOutputSettings': {
                                    'NameModifier': 'string'
                                },
                                'RtmpOutputSettings': {
                                    'CertificateMode': 'SELF_SIGNED'|'VERIFY_AUTHENTICITY',
                                    'ConnectionRetryInterval': 123,
                                    'Destination': {
                                        'DestinationRefId': 'string'
                                    },
                                    'NumRetries': 123
                                },
                                'UdpOutputSettings': {
                                    'BufferMsec': 123,
                                    'ContainerSettings': {
                                        'M2tsSettings': {
                                            'AbsentInputAudioBehavior': 'DROP'|'ENCODE_SILENCE',
                                            'Arib': 'DISABLED'|'ENABLED',
                                            'AribCaptionsPid': 'string',
                                            'AribCaptionsPidControl': 'AUTO'|'USE_CONFIGURED',
                                            'AudioBufferModel': 'ATSC'|'DVB',
                                            'AudioFramesPerPes': 123,
                                            'AudioPids': 'string',
                                            'AudioStreamType': 'ATSC'|'DVB',
                                            'Bitrate': 123,
                                            'BufferModel': 'MULTIPLEX'|'NONE',
                                            'CcDescriptor': 'DISABLED'|'ENABLED',
                                            'DvbNitSettings': {
                                                'NetworkId': 123,
                                                'NetworkName': 'string',
                                                'RepInterval': 123
                                            },
                                            'DvbSdtSettings': {
                                                'OutputSdt': 'SDT_FOLLOW'|'SDT_FOLLOW_IF_PRESENT'|'SDT_MANUAL'|'SDT_NONE',
                                                'RepInterval': 123,
                                                'ServiceName': 'string',
                                                'ServiceProviderName': 'string'
                                            },
                                            'DvbSubPids': 'string',
                                            'DvbTdtSettings': {
                                                'RepInterval': 123
                                            },
                                            'DvbTeletextPid': 'string',
                                            'Ebif': 'NONE'|'PASSTHROUGH',
                                            'EbpAudioInterval': 'VIDEO_AND_FIXED_INTERVALS'|'VIDEO_INTERVAL',
                                            'EbpLookaheadMs': 123,
                                            'EbpPlacement': 'VIDEO_AND_AUDIO_PIDS'|'VIDEO_PID',
                                            'EcmPid': 'string',
                                            'EsRateInPes': 'EXCLUDE'|'INCLUDE',
                                            'EtvPlatformPid': 'string',
                                            'EtvSignalPid': 'string',
                                            'FragmentTime': 123.0,
                                            'Klv': 'NONE'|'PASSTHROUGH',
                                            'KlvDataPids': 'string',
                                            'NullPacketBitrate': 123.0,
                                            'PatInterval': 123,
                                            'PcrControl': 'CONFIGURED_PCR_PERIOD'|'PCR_EVERY_PES_PACKET',
                                            'PcrPeriod': 123,
                                            'PcrPid': 'string',
                                            'PmtInterval': 123,
                                            'PmtPid': 'string',
                                            'ProgramNum': 123,
                                            'RateMode': 'CBR'|'VBR',
                                            'Scte27Pids': 'string',
                                            'Scte35Control': 'NONE'|'PASSTHROUGH',
                                            'Scte35Pid': 'string',
                                            'SegmentationMarkers': 'EBP'|'EBP_LEGACY'|'NONE'|'PSI_SEGSTART'|'RAI_ADAPT'|'RAI_SEGSTART',
                                            'SegmentationStyle': 'MAINTAIN_CADENCE'|'RESET_CADENCE',
                                            'SegmentationTime': 123.0,
                                            'TimedMetadataBehavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                            'TimedMetadataPid': 'string',
                                            'TransportStreamId': 123,
                                            'VideoPid': 'string'
                                        }
                                    },
                                    'Destination': {
                                        'DestinationRefId': 'string'
                                    },
                                    'FecOutputSettings': {
                                        'ColumnDepth': 123,
                                        'IncludeFec': 'COLUMN'|'COLUMN_AND_ROW',
                                        'RowLength': 123
                                    }
                                }
                            },
                            'VideoDescriptionName': 'string'
                        },
                    ]
                },
            ],
            'TimecodeConfig': {
                'Source': 'EMBEDDED'|'SYSTEMCLOCK'|'ZEROBASED',
                'SyncThreshold': 123
            },
            'VideoDescriptions': [
                {
                    'CodecSettings': {
                        'H264Settings': {
                            'AdaptiveQuantization': 'HIGH'|'HIGHER'|'LOW'|'MAX'|'MEDIUM'|'OFF',
                            'AfdSignaling': 'AUTO'|'FIXED'|'NONE',
                            'Bitrate': 123,
                            'BufFillPct': 123,
                            'BufSize': 123,
                            'ColorMetadata': 'IGNORE'|'INSERT',
                            'EntropyEncoding': 'CABAC'|'CAVLC',
                            'FixedAfd': 'AFD_0000'|'AFD_0010'|'AFD_0011'|'AFD_0100'|'AFD_1000'|'AFD_1001'|'AFD_1010'|'AFD_1011'|'AFD_1101'|'AFD_1110'|'AFD_1111',
                            'FlickerAq': 'DISABLED'|'ENABLED',
                            'FramerateControl': 'INITIALIZE_FROM_SOURCE'|'SPECIFIED',
                            'FramerateDenominator': 123,
                            'FramerateNumerator': 123,
                            'GopBReference': 'DISABLED'|'ENABLED',
                            'GopClosedCadence': 123,
                            'GopNumBFrames': 123,
                            'GopSize': 123.0,
                            'GopSizeUnits': 'FRAMES'|'SECONDS',
                            'Level': 'H264_LEVEL_1'|'H264_LEVEL_1_1'|'H264_LEVEL_1_2'|'H264_LEVEL_1_3'|'H264_LEVEL_2'|'H264_LEVEL_2_1'|'H264_LEVEL_2_2'|'H264_LEVEL_3'|'H264_LEVEL_3_1'|'H264_LEVEL_3_2'|'H264_LEVEL_4'|'H264_LEVEL_4_1'|'H264_LEVEL_4_2'|'H264_LEVEL_5'|'H264_LEVEL_5_1'|'H264_LEVEL_5_2'|'H264_LEVEL_AUTO',
                            'LookAheadRateControl': 'HIGH'|'LOW'|'MEDIUM',
                            'MaxBitrate': 123,
                            'MinIInterval': 123,
                            'NumRefFrames': 123,
                            'ParControl': 'INITIALIZE_FROM_SOURCE'|'SPECIFIED',
                            'ParDenominator': 123,
                            'ParNumerator': 123,
                            'Profile': 'BASELINE'|'HIGH'|'HIGH_10BIT'|'HIGH_422'|'HIGH_422_10BIT'|'MAIN',
                            'QvbrQualityLevel': 123,
                            'RateControlMode': 'CBR'|'QVBR'|'VBR',
                            'ScanType': 'INTERLACED'|'PROGRESSIVE',
                            'SceneChangeDetect': 'DISABLED'|'ENABLED',
                            'Slices': 123,
                            'Softness': 123,
                            'SpatialAq': 'DISABLED'|'ENABLED',
                            'SubgopLength': 'DYNAMIC'|'FIXED',
                            'Syntax': 'DEFAULT'|'RP2027',
                            'TemporalAq': 'DISABLED'|'ENABLED',
                            'TimecodeInsertion': 'DISABLED'|'PIC_TIMING_SEI'
                        }
                    },
                    'Height': 123,
                    'Name': 'string',
                    'RespondToAfd': 'NONE'|'PASSTHROUGH'|'RESPOND',
                    'ScalingBehavior': 'DEFAULT'|'STRETCH_TO_OUTPUT',
                    'Sharpness': 123,
                    'Width': 123
                },
            ]
        },
        'Id': 'string',
        'InputAttachments': [
            {
                'InputAttachmentName': 'string',
                'InputId': 'string',
                'InputSettings': {
                    'AudioSelectors': [
                        {
                            'Name': 'string',
                            'SelectorSettings': {
                                'AudioLanguageSelection': {
                                    'LanguageCode': 'string',
                                    'LanguageSelectionPolicy': 'LOOSE'|'STRICT'
                                },
                                'AudioPidSelection': {
                                    'Pid': 123
                                }
                            }
                        },
                    ],
                    'CaptionSelectors': [
                        {
                            'LanguageCode': 'string',
                            'Name': 'string',
                            'SelectorSettings': {
                                'AribSourceSettings': {},
                                'DvbSubSourceSettings': {
                                    'Pid': 123
                                },
                                'EmbeddedSourceSettings': {
                                    'Convert608To708': 'DISABLED'|'UPCONVERT',
                                    'Scte20Detection': 'AUTO'|'OFF',
                                    'Source608ChannelNumber': 123,
                                    'Source608TrackNumber': 123
                                },
                                'Scte20SourceSettings': {
                                    'Convert608To708': 'DISABLED'|'UPCONVERT',
                                    'Source608ChannelNumber': 123
                                },
                                'Scte27SourceSettings': {
                                    'Pid': 123
                                },
                                'TeletextSourceSettings': {
                                    'PageNumber': 'string'
                                }
                            }
                        },
                    ],
                    'DeblockFilter': 'DISABLED'|'ENABLED',
                    'DenoiseFilter': 'DISABLED'|'ENABLED',
                    'FilterStrength': 123,
                    'InputFilter': 'AUTO'|'DISABLED'|'FORCED',
                    'NetworkInputSettings': {
                        'HlsInputSettings': {
                            'Bandwidth': 123,
                            'BufferSegments': 123,
                            'Retries': 123,
                            'RetryInterval': 123
                        },
                        'ServerValidation': 'CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME'|'CHECK_CRYPTOGRAPHY_ONLY'
                    },
                    'SourceEndBehavior': 'CONTINUE'|'LOOP',
                    'VideoSelector': {
                        'ColorSpace': 'FOLLOW'|'REC_601'|'REC_709',
                        'ColorSpaceUsage': 'FALLBACK'|'FORCE',
                        'SelectorSettings': {
                            'VideoSelectorPid': {
                                'Pid': 123
                            },
                            'VideoSelectorProgramId': {
                                'ProgramId': 123
                            }
                        }
                    }
                }
            },
        ],
        'InputSpecification': {
            'Codec': 'MPEG2'|'AVC'|'HEVC',
            'MaximumBitrate': 'MAX_10_MBPS'|'MAX_20_MBPS'|'MAX_50_MBPS',
            'Resolution': 'SD'|'HD'|'UHD'
        },
        'LogLevel': 'ERROR'|'WARNING'|'INFO'|'DEBUG'|'DISABLED',
        'Name': 'string',
        'PipelinesRunningCount': 123,
        'RoleArn': 'string',
        'State': 'CREATING'|'CREATE_FAILED'|'IDLE'|'STARTING'|'RUNNING'|'RECOVERING'|'STOPPING'|'DELETING'|'DELETED'
    }
    
    
    """
    pass

def stop_channel(ChannelId=None):
    """
    Stops a running channel
    See also: AWS API Documentation
    
    
    :example: response = client.stop_channel(
        ChannelId='string'
    )
    
    
    :type ChannelId: string
    :param ChannelId: [REQUIRED] A request to stop a running channel

    :rtype: dict
    :return: {
        'Arn': 'string',
        'Destinations': [
            {
                'Id': 'string',
                'Settings': [
                    {
                        'PasswordParam': 'string',
                        'StreamName': 'string',
                        'Url': 'string',
                        'Username': 'string'
                    },
                ]
            },
        ],
        'EgressEndpoints': [
            {
                'SourceIp': 'string'
            },
        ],
        'EncoderSettings': {
            'AudioDescriptions': [
                {
                    'AudioNormalizationSettings': {
                        'Algorithm': 'ITU_1770_1'|'ITU_1770_2',
                        'AlgorithmControl': 'CORRECT_AUDIO',
                        'TargetLkfs': 123.0
                    },
                    'AudioSelectorName': 'string',
                    'AudioType': 'CLEAN_EFFECTS'|'HEARING_IMPAIRED'|'UNDEFINED'|'VISUAL_IMPAIRED_COMMENTARY',
                    'AudioTypeControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                    'CodecSettings': {
                        'AacSettings': {
                            'Bitrate': 123.0,
                            'CodingMode': 'AD_RECEIVER_MIX'|'CODING_MODE_1_0'|'CODING_MODE_1_1'|'CODING_MODE_2_0'|'CODING_MODE_5_1',
                            'InputType': 'BROADCASTER_MIXED_AD'|'NORMAL',
                            'Profile': 'HEV1'|'HEV2'|'LC',
                            'RateControlMode': 'CBR'|'VBR',
                            'RawFormat': 'LATM_LOAS'|'NONE',
                            'SampleRate': 123.0,
                            'Spec': 'MPEG2'|'MPEG4',
                            'VbrQuality': 'HIGH'|'LOW'|'MEDIUM_HIGH'|'MEDIUM_LOW'
                        },
                        'Ac3Settings': {
                            'Bitrate': 123.0,
                            'BitstreamMode': 'COMMENTARY'|'COMPLETE_MAIN'|'DIALOGUE'|'EMERGENCY'|'HEARING_IMPAIRED'|'MUSIC_AND_EFFECTS'|'VISUALLY_IMPAIRED'|'VOICE_OVER',
                            'CodingMode': 'CODING_MODE_1_0'|'CODING_MODE_1_1'|'CODING_MODE_2_0'|'CODING_MODE_3_2_LFE',
                            'Dialnorm': 123,
                            'DrcProfile': 'FILM_STANDARD'|'NONE',
                            'LfeFilter': 'DISABLED'|'ENABLED',
                            'MetadataControl': 'FOLLOW_INPUT'|'USE_CONFIGURED'
                        },
                        'Eac3Settings': {
                            'AttenuationControl': 'ATTENUATE_3_DB'|'NONE',
                            'Bitrate': 123.0,
                            'BitstreamMode': 'COMMENTARY'|'COMPLETE_MAIN'|'EMERGENCY'|'HEARING_IMPAIRED'|'VISUALLY_IMPAIRED',
                            'CodingMode': 'CODING_MODE_1_0'|'CODING_MODE_2_0'|'CODING_MODE_3_2',
                            'DcFilter': 'DISABLED'|'ENABLED',
                            'Dialnorm': 123,
                            'DrcLine': 'FILM_LIGHT'|'FILM_STANDARD'|'MUSIC_LIGHT'|'MUSIC_STANDARD'|'NONE'|'SPEECH',
                            'DrcRf': 'FILM_LIGHT'|'FILM_STANDARD'|'MUSIC_LIGHT'|'MUSIC_STANDARD'|'NONE'|'SPEECH',
                            'LfeControl': 'LFE'|'NO_LFE',
                            'LfeFilter': 'DISABLED'|'ENABLED',
                            'LoRoCenterMixLevel': 123.0,
                            'LoRoSurroundMixLevel': 123.0,
                            'LtRtCenterMixLevel': 123.0,
                            'LtRtSurroundMixLevel': 123.0,
                            'MetadataControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                            'PassthroughControl': 'NO_PASSTHROUGH'|'WHEN_POSSIBLE',
                            'PhaseControl': 'NO_SHIFT'|'SHIFT_90_DEGREES',
                            'StereoDownmix': 'DPL2'|'LO_RO'|'LT_RT'|'NOT_INDICATED',
                            'SurroundExMode': 'DISABLED'|'ENABLED'|'NOT_INDICATED',
                            'SurroundMode': 'DISABLED'|'ENABLED'|'NOT_INDICATED'
                        },
                        'Mp2Settings': {
                            'Bitrate': 123.0,
                            'CodingMode': 'CODING_MODE_1_0'|'CODING_MODE_2_0',
                            'SampleRate': 123.0
                        },
                        'PassThroughSettings': {}
                    },
                    'LanguageCode': 'string',
                    'LanguageCodeControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                    'Name': 'string',
                    'RemixSettings': {
                        'ChannelMappings': [
                            {
                                'InputChannelLevels': [
                                    {
                                        'Gain': 123,
                                        'InputChannel': 123
                                    },
                                ],
                                'OutputChannel': 123
                            },
                        ],
                        'ChannelsIn': 123,
                        'ChannelsOut': 123
                    },
                    'StreamName': 'string'
                },
            ],
            'AvailBlanking': {
                'AvailBlankingImage': {
                    'PasswordParam': 'string',
                    'Uri': 'string',
                    'Username': 'string'
                },
                'State': 'DISABLED'|'ENABLED'
            },
            'AvailConfiguration': {
                'AvailSettings': {
                    'Scte35SpliceInsert': {
                        'AdAvailOffset': 123,
                        'NoRegionalBlackoutFlag': 'FOLLOW'|'IGNORE',
                        'WebDeliveryAllowedFlag': 'FOLLOW'|'IGNORE'
                    },
                    'Scte35TimeSignalApos': {
                        'AdAvailOffset': 123,
                        'NoRegionalBlackoutFlag': 'FOLLOW'|'IGNORE',
                        'WebDeliveryAllowedFlag': 'FOLLOW'|'IGNORE'
                    }
                }
            },
            'BlackoutSlate': {
                'BlackoutSlateImage': {
                    'PasswordParam': 'string',
                    'Uri': 'string',
                    'Username': 'string'
                },
                'NetworkEndBlackout': 'DISABLED'|'ENABLED',
                'NetworkEndBlackoutImage': {
                    'PasswordParam': 'string',
                    'Uri': 'string',
                    'Username': 'string'
                },
                'NetworkId': 'string',
                'State': 'DISABLED'|'ENABLED'
            },
            'CaptionDescriptions': [
                {
                    'CaptionSelectorName': 'string',
                    'DestinationSettings': {
                        'AribDestinationSettings': {},
                        'BurnInDestinationSettings': {
                            'Alignment': 'CENTERED'|'LEFT'|'SMART',
                            'BackgroundColor': 'BLACK'|'NONE'|'WHITE',
                            'BackgroundOpacity': 123,
                            'Font': {
                                'PasswordParam': 'string',
                                'Uri': 'string',
                                'Username': 'string'
                            },
                            'FontColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                            'FontOpacity': 123,
                            'FontResolution': 123,
                            'FontSize': 'string',
                            'OutlineColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                            'OutlineSize': 123,
                            'ShadowColor': 'BLACK'|'NONE'|'WHITE',
                            'ShadowOpacity': 123,
                            'ShadowXOffset': 123,
                            'ShadowYOffset': 123,
                            'TeletextGridControl': 'FIXED'|'SCALED',
                            'XPosition': 123,
                            'YPosition': 123
                        },
                        'DvbSubDestinationSettings': {
                            'Alignment': 'CENTERED'|'LEFT'|'SMART',
                            'BackgroundColor': 'BLACK'|'NONE'|'WHITE',
                            'BackgroundOpacity': 123,
                            'Font': {
                                'PasswordParam': 'string',
                                'Uri': 'string',
                                'Username': 'string'
                            },
                            'FontColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                            'FontOpacity': 123,
                            'FontResolution': 123,
                            'FontSize': 'string',
                            'OutlineColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                            'OutlineSize': 123,
                            'ShadowColor': 'BLACK'|'NONE'|'WHITE',
                            'ShadowOpacity': 123,
                            'ShadowXOffset': 123,
                            'ShadowYOffset': 123,
                            'TeletextGridControl': 'FIXED'|'SCALED',
                            'XPosition': 123,
                            'YPosition': 123
                        },
                        'EmbeddedDestinationSettings': {},
                        'EmbeddedPlusScte20DestinationSettings': {},
                        'RtmpCaptionInfoDestinationSettings': {},
                        'Scte20PlusEmbeddedDestinationSettings': {},
                        'Scte27DestinationSettings': {},
                        'SmpteTtDestinationSettings': {},
                        'TeletextDestinationSettings': {},
                        'TtmlDestinationSettings': {
                            'StyleControl': 'PASSTHROUGH'|'USE_CONFIGURED'
                        },
                        'WebvttDestinationSettings': {}
                    },
                    'LanguageCode': 'string',
                    'LanguageDescription': 'string',
                    'Name': 'string'
                },
            ],
            'GlobalConfiguration': {
                'InitialAudioGain': 123,
                'InputEndAction': 'NONE'|'SWITCH_AND_LOOP_INPUTS',
                'InputLossBehavior': {
                    'BlackFrameMsec': 123,
                    'InputLossImageColor': 'string',
                    'InputLossImageSlate': {
                        'PasswordParam': 'string',
                        'Uri': 'string',
                        'Username': 'string'
                    },
                    'InputLossImageType': 'COLOR'|'SLATE',
                    'RepeatFrameMsec': 123
                },
                'OutputTimingSource': 'INPUT_CLOCK'|'SYSTEM_CLOCK',
                'SupportLowFramerateInputs': 'DISABLED'|'ENABLED'
            },
            'OutputGroups': [
                {
                    'Name': 'string',
                    'OutputGroupSettings': {
                        'ArchiveGroupSettings': {
                            'Destination': {
                                'DestinationRefId': 'string'
                            },
                            'RolloverInterval': 123
                        },
                        'HlsGroupSettings': {
                            'AdMarkers': [
                                'ADOBE'|'ELEMENTAL'|'ELEMENTAL_SCTE35',
                            ],
                            'BaseUrlContent': 'string',
                            'BaseUrlManifest': 'string',
                            'CaptionLanguageMappings': [
                                {
                                    'CaptionChannel': 123,
                                    'LanguageCode': 'string',
                                    'LanguageDescription': 'string'
                                },
                            ],
                            'CaptionLanguageSetting': 'INSERT'|'NONE'|'OMIT',
                            'ClientCache': 'DISABLED'|'ENABLED',
                            'CodecSpecification': 'RFC_4281'|'RFC_6381',
                            'ConstantIv': 'string',
                            'Destination': {
                                'DestinationRefId': 'string'
                            },
                            'DirectoryStructure': 'SINGLE_DIRECTORY'|'SUBDIRECTORY_PER_STREAM',
                            'EncryptionType': 'AES128'|'SAMPLE_AES',
                            'HlsCdnSettings': {
                                'HlsAkamaiSettings': {
                                    'ConnectionRetryInterval': 123,
                                    'FilecacheDuration': 123,
                                    'HttpTransferMode': 'CHUNKED'|'NON_CHUNKED',
                                    'NumRetries': 123,
                                    'RestartDelay': 123,
                                    'Salt': 'string',
                                    'Token': 'string'
                                },
                                'HlsBasicPutSettings': {
                                    'ConnectionRetryInterval': 123,
                                    'FilecacheDuration': 123,
                                    'NumRetries': 123,
                                    'RestartDelay': 123
                                },
                                'HlsMediaStoreSettings': {
                                    'ConnectionRetryInterval': 123,
                                    'FilecacheDuration': 123,
                                    'MediaStoreStorageClass': 'TEMPORAL',
                                    'NumRetries': 123,
                                    'RestartDelay': 123
                                },
                                'HlsWebdavSettings': {
                                    'ConnectionRetryInterval': 123,
                                    'FilecacheDuration': 123,
                                    'HttpTransferMode': 'CHUNKED'|'NON_CHUNKED',
                                    'NumRetries': 123,
                                    'RestartDelay': 123
                                }
                            },
                            'IndexNSegments': 123,
                            'InputLossAction': 'EMIT_OUTPUT'|'PAUSE_OUTPUT',
                            'IvInManifest': 'EXCLUDE'|'INCLUDE',
                            'IvSource': 'EXPLICIT'|'FOLLOWS_SEGMENT_NUMBER',
                            'KeepSegments': 123,
                            'KeyFormat': 'string',
                            'KeyFormatVersions': 'string',
                            'KeyProviderSettings': {
                                'StaticKeySettings': {
                                    'KeyProviderServer': {
                                        'PasswordParam': 'string',
                                        'Uri': 'string',
                                        'Username': 'string'
                                    },
                                    'StaticKeyValue': 'string'
                                }
                            },
                            'ManifestCompression': 'GZIP'|'NONE',
                            'ManifestDurationFormat': 'FLOATING_POINT'|'INTEGER',
                            'MinSegmentLength': 123,
                            'Mode': 'LIVE'|'VOD',
                            'OutputSelection': 'MANIFESTS_AND_SEGMENTS'|'SEGMENTS_ONLY',
                            'ProgramDateTime': 'EXCLUDE'|'INCLUDE',
                            'ProgramDateTimePeriod': 123,
                            'RedundantManifest': 'DISABLED'|'ENABLED',
                            'SegmentLength': 123,
                            'SegmentationMode': 'USE_INPUT_SEGMENTATION'|'USE_SEGMENT_DURATION',
                            'SegmentsPerSubdirectory': 123,
                            'StreamInfResolution': 'EXCLUDE'|'INCLUDE',
                            'TimedMetadataId3Frame': 'NONE'|'PRIV'|'TDRL',
                            'TimedMetadataId3Period': 123,
                            'TimestampDeltaMilliseconds': 123,
                            'TsFileMode': 'SEGMENTED_FILES'|'SINGLE_FILE'
                        },
                        'MsSmoothGroupSettings': {
                            'AcquisitionPointId': 'string',
                            'AudioOnlyTimecodeControl': 'PASSTHROUGH'|'USE_CONFIGURED_CLOCK',
                            'CertificateMode': 'SELF_SIGNED'|'VERIFY_AUTHENTICITY',
                            'ConnectionRetryInterval': 123,
                            'Destination': {
                                'DestinationRefId': 'string'
                            },
                            'EventId': 'string',
                            'EventIdMode': 'NO_EVENT_ID'|'USE_CONFIGURED'|'USE_TIMESTAMP',
                            'EventStopBehavior': 'NONE'|'SEND_EOS',
                            'FilecacheDuration': 123,
                            'FragmentLength': 123,
                            'InputLossAction': 'EMIT_OUTPUT'|'PAUSE_OUTPUT',
                            'NumRetries': 123,
                            'RestartDelay': 123,
                            'SegmentationMode': 'USE_INPUT_SEGMENTATION'|'USE_SEGMENT_DURATION',
                            'SendDelayMs': 123,
                            'SparseTrackType': 'NONE'|'SCTE_35',
                            'StreamManifestBehavior': 'DO_NOT_SEND'|'SEND',
                            'TimestampOffset': 'string',
                            'TimestampOffsetMode': 'USE_CONFIGURED_OFFSET'|'USE_EVENT_START_DATE'
                        },
                        'RtmpGroupSettings': {
                            'AuthenticationScheme': 'AKAMAI'|'COMMON',
                            'CacheFullBehavior': 'DISCONNECT_IMMEDIATELY'|'WAIT_FOR_SERVER',
                            'CacheLength': 123,
                            'CaptionData': 'ALL'|'FIELD1_608'|'FIELD1_AND_FIELD2_608',
                            'InputLossAction': 'EMIT_OUTPUT'|'PAUSE_OUTPUT',
                            'RestartDelay': 123
                        },
                        'UdpGroupSettings': {
                            'InputLossAction': 'DROP_PROGRAM'|'DROP_TS'|'EMIT_PROGRAM',
                            'TimedMetadataId3Frame': 'NONE'|'PRIV'|'TDRL',
                            'TimedMetadataId3Period': 123
                        }
                    },
                    'Outputs': [
                        {
                            'AudioDescriptionNames': [
                                'string',
                            ],
                            'CaptionDescriptionNames': [
                                'string',
                            ],
                            'OutputName': 'string',
                            'OutputSettings': {
                                'ArchiveOutputSettings': {
                                    'ContainerSettings': {
                                        'M2tsSettings': {
                                            'AbsentInputAudioBehavior': 'DROP'|'ENCODE_SILENCE',
                                            'Arib': 'DISABLED'|'ENABLED',
                                            'AribCaptionsPid': 'string',
                                            'AribCaptionsPidControl': 'AUTO'|'USE_CONFIGURED',
                                            'AudioBufferModel': 'ATSC'|'DVB',
                                            'AudioFramesPerPes': 123,
                                            'AudioPids': 'string',
                                            'AudioStreamType': 'ATSC'|'DVB',
                                            'Bitrate': 123,
                                            'BufferModel': 'MULTIPLEX'|'NONE',
                                            'CcDescriptor': 'DISABLED'|'ENABLED',
                                            'DvbNitSettings': {
                                                'NetworkId': 123,
                                                'NetworkName': 'string',
                                                'RepInterval': 123
                                            },
                                            'DvbSdtSettings': {
                                                'OutputSdt': 'SDT_FOLLOW'|'SDT_FOLLOW_IF_PRESENT'|'SDT_MANUAL'|'SDT_NONE',
                                                'RepInterval': 123,
                                                'ServiceName': 'string',
                                                'ServiceProviderName': 'string'
                                            },
                                            'DvbSubPids': 'string',
                                            'DvbTdtSettings': {
                                                'RepInterval': 123
                                            },
                                            'DvbTeletextPid': 'string',
                                            'Ebif': 'NONE'|'PASSTHROUGH',
                                            'EbpAudioInterval': 'VIDEO_AND_FIXED_INTERVALS'|'VIDEO_INTERVAL',
                                            'EbpLookaheadMs': 123,
                                            'EbpPlacement': 'VIDEO_AND_AUDIO_PIDS'|'VIDEO_PID',
                                            'EcmPid': 'string',
                                            'EsRateInPes': 'EXCLUDE'|'INCLUDE',
                                            'EtvPlatformPid': 'string',
                                            'EtvSignalPid': 'string',
                                            'FragmentTime': 123.0,
                                            'Klv': 'NONE'|'PASSTHROUGH',
                                            'KlvDataPids': 'string',
                                            'NullPacketBitrate': 123.0,
                                            'PatInterval': 123,
                                            'PcrControl': 'CONFIGURED_PCR_PERIOD'|'PCR_EVERY_PES_PACKET',
                                            'PcrPeriod': 123,
                                            'PcrPid': 'string',
                                            'PmtInterval': 123,
                                            'PmtPid': 'string',
                                            'ProgramNum': 123,
                                            'RateMode': 'CBR'|'VBR',
                                            'Scte27Pids': 'string',
                                            'Scte35Control': 'NONE'|'PASSTHROUGH',
                                            'Scte35Pid': 'string',
                                            'SegmentationMarkers': 'EBP'|'EBP_LEGACY'|'NONE'|'PSI_SEGSTART'|'RAI_ADAPT'|'RAI_SEGSTART',
                                            'SegmentationStyle': 'MAINTAIN_CADENCE'|'RESET_CADENCE',
                                            'SegmentationTime': 123.0,
                                            'TimedMetadataBehavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                            'TimedMetadataPid': 'string',
                                            'TransportStreamId': 123,
                                            'VideoPid': 'string'
                                        }
                                    },
                                    'Extension': 'string',
                                    'NameModifier': 'string'
                                },
                                'HlsOutputSettings': {
                                    'HlsSettings': {
                                        'AudioOnlyHlsSettings': {
                                            'AudioGroupId': 'string',
                                            'AudioOnlyImage': {
                                                'PasswordParam': 'string',
                                                'Uri': 'string',
                                                'Username': 'string'
                                            },
                                            'AudioTrackType': 'ALTERNATE_AUDIO_AUTO_SELECT'|'ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT'|'ALTERNATE_AUDIO_NOT_AUTO_SELECT'|'AUDIO_ONLY_VARIANT_STREAM'
                                        },
                                        'StandardHlsSettings': {
                                            'AudioRenditionSets': 'string',
                                            'M3u8Settings': {
                                                'AudioFramesPerPes': 123,
                                                'AudioPids': 'string',
                                                'EcmPid': 'string',
                                                'PatInterval': 123,
                                                'PcrControl': 'CONFIGURED_PCR_PERIOD'|'PCR_EVERY_PES_PACKET',
                                                'PcrPeriod': 123,
                                                'PcrPid': 'string',
                                                'PmtInterval': 123,
                                                'PmtPid': 'string',
                                                'ProgramNum': 123,
                                                'Scte35Behavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                                'Scte35Pid': 'string',
                                                'TimedMetadataBehavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                                'TimedMetadataPid': 'string',
                                                'TransportStreamId': 123,
                                                'VideoPid': 'string'
                                            }
                                        }
                                    },
                                    'NameModifier': 'string',
                                    'SegmentModifier': 'string'
                                },
                                'MsSmoothOutputSettings': {
                                    'NameModifier': 'string'
                                },
                                'RtmpOutputSettings': {
                                    'CertificateMode': 'SELF_SIGNED'|'VERIFY_AUTHENTICITY',
                                    'ConnectionRetryInterval': 123,
                                    'Destination': {
                                        'DestinationRefId': 'string'
                                    },
                                    'NumRetries': 123
                                },
                                'UdpOutputSettings': {
                                    'BufferMsec': 123,
                                    'ContainerSettings': {
                                        'M2tsSettings': {
                                            'AbsentInputAudioBehavior': 'DROP'|'ENCODE_SILENCE',
                                            'Arib': 'DISABLED'|'ENABLED',
                                            'AribCaptionsPid': 'string',
                                            'AribCaptionsPidControl': 'AUTO'|'USE_CONFIGURED',
                                            'AudioBufferModel': 'ATSC'|'DVB',
                                            'AudioFramesPerPes': 123,
                                            'AudioPids': 'string',
                                            'AudioStreamType': 'ATSC'|'DVB',
                                            'Bitrate': 123,
                                            'BufferModel': 'MULTIPLEX'|'NONE',
                                            'CcDescriptor': 'DISABLED'|'ENABLED',
                                            'DvbNitSettings': {
                                                'NetworkId': 123,
                                                'NetworkName': 'string',
                                                'RepInterval': 123
                                            },
                                            'DvbSdtSettings': {
                                                'OutputSdt': 'SDT_FOLLOW'|'SDT_FOLLOW_IF_PRESENT'|'SDT_MANUAL'|'SDT_NONE',
                                                'RepInterval': 123,
                                                'ServiceName': 'string',
                                                'ServiceProviderName': 'string'
                                            },
                                            'DvbSubPids': 'string',
                                            'DvbTdtSettings': {
                                                'RepInterval': 123
                                            },
                                            'DvbTeletextPid': 'string',
                                            'Ebif': 'NONE'|'PASSTHROUGH',
                                            'EbpAudioInterval': 'VIDEO_AND_FIXED_INTERVALS'|'VIDEO_INTERVAL',
                                            'EbpLookaheadMs': 123,
                                            'EbpPlacement': 'VIDEO_AND_AUDIO_PIDS'|'VIDEO_PID',
                                            'EcmPid': 'string',
                                            'EsRateInPes': 'EXCLUDE'|'INCLUDE',
                                            'EtvPlatformPid': 'string',
                                            'EtvSignalPid': 'string',
                                            'FragmentTime': 123.0,
                                            'Klv': 'NONE'|'PASSTHROUGH',
                                            'KlvDataPids': 'string',
                                            'NullPacketBitrate': 123.0,
                                            'PatInterval': 123,
                                            'PcrControl': 'CONFIGURED_PCR_PERIOD'|'PCR_EVERY_PES_PACKET',
                                            'PcrPeriod': 123,
                                            'PcrPid': 'string',
                                            'PmtInterval': 123,
                                            'PmtPid': 'string',
                                            'ProgramNum': 123,
                                            'RateMode': 'CBR'|'VBR',
                                            'Scte27Pids': 'string',
                                            'Scte35Control': 'NONE'|'PASSTHROUGH',
                                            'Scte35Pid': 'string',
                                            'SegmentationMarkers': 'EBP'|'EBP_LEGACY'|'NONE'|'PSI_SEGSTART'|'RAI_ADAPT'|'RAI_SEGSTART',
                                            'SegmentationStyle': 'MAINTAIN_CADENCE'|'RESET_CADENCE',
                                            'SegmentationTime': 123.0,
                                            'TimedMetadataBehavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                            'TimedMetadataPid': 'string',
                                            'TransportStreamId': 123,
                                            'VideoPid': 'string'
                                        }
                                    },
                                    'Destination': {
                                        'DestinationRefId': 'string'
                                    },
                                    'FecOutputSettings': {
                                        'ColumnDepth': 123,
                                        'IncludeFec': 'COLUMN'|'COLUMN_AND_ROW',
                                        'RowLength': 123
                                    }
                                }
                            },
                            'VideoDescriptionName': 'string'
                        },
                    ]
                },
            ],
            'TimecodeConfig': {
                'Source': 'EMBEDDED'|'SYSTEMCLOCK'|'ZEROBASED',
                'SyncThreshold': 123
            },
            'VideoDescriptions': [
                {
                    'CodecSettings': {
                        'H264Settings': {
                            'AdaptiveQuantization': 'HIGH'|'HIGHER'|'LOW'|'MAX'|'MEDIUM'|'OFF',
                            'AfdSignaling': 'AUTO'|'FIXED'|'NONE',
                            'Bitrate': 123,
                            'BufFillPct': 123,
                            'BufSize': 123,
                            'ColorMetadata': 'IGNORE'|'INSERT',
                            'EntropyEncoding': 'CABAC'|'CAVLC',
                            'FixedAfd': 'AFD_0000'|'AFD_0010'|'AFD_0011'|'AFD_0100'|'AFD_1000'|'AFD_1001'|'AFD_1010'|'AFD_1011'|'AFD_1101'|'AFD_1110'|'AFD_1111',
                            'FlickerAq': 'DISABLED'|'ENABLED',
                            'FramerateControl': 'INITIALIZE_FROM_SOURCE'|'SPECIFIED',
                            'FramerateDenominator': 123,
                            'FramerateNumerator': 123,
                            'GopBReference': 'DISABLED'|'ENABLED',
                            'GopClosedCadence': 123,
                            'GopNumBFrames': 123,
                            'GopSize': 123.0,
                            'GopSizeUnits': 'FRAMES'|'SECONDS',
                            'Level': 'H264_LEVEL_1'|'H264_LEVEL_1_1'|'H264_LEVEL_1_2'|'H264_LEVEL_1_3'|'H264_LEVEL_2'|'H264_LEVEL_2_1'|'H264_LEVEL_2_2'|'H264_LEVEL_3'|'H264_LEVEL_3_1'|'H264_LEVEL_3_2'|'H264_LEVEL_4'|'H264_LEVEL_4_1'|'H264_LEVEL_4_2'|'H264_LEVEL_5'|'H264_LEVEL_5_1'|'H264_LEVEL_5_2'|'H264_LEVEL_AUTO',
                            'LookAheadRateControl': 'HIGH'|'LOW'|'MEDIUM',
                            'MaxBitrate': 123,
                            'MinIInterval': 123,
                            'NumRefFrames': 123,
                            'ParControl': 'INITIALIZE_FROM_SOURCE'|'SPECIFIED',
                            'ParDenominator': 123,
                            'ParNumerator': 123,
                            'Profile': 'BASELINE'|'HIGH'|'HIGH_10BIT'|'HIGH_422'|'HIGH_422_10BIT'|'MAIN',
                            'QvbrQualityLevel': 123,
                            'RateControlMode': 'CBR'|'QVBR'|'VBR',
                            'ScanType': 'INTERLACED'|'PROGRESSIVE',
                            'SceneChangeDetect': 'DISABLED'|'ENABLED',
                            'Slices': 123,
                            'Softness': 123,
                            'SpatialAq': 'DISABLED'|'ENABLED',
                            'SubgopLength': 'DYNAMIC'|'FIXED',
                            'Syntax': 'DEFAULT'|'RP2027',
                            'TemporalAq': 'DISABLED'|'ENABLED',
                            'TimecodeInsertion': 'DISABLED'|'PIC_TIMING_SEI'
                        }
                    },
                    'Height': 123,
                    'Name': 'string',
                    'RespondToAfd': 'NONE'|'PASSTHROUGH'|'RESPOND',
                    'ScalingBehavior': 'DEFAULT'|'STRETCH_TO_OUTPUT',
                    'Sharpness': 123,
                    'Width': 123
                },
            ]
        },
        'Id': 'string',
        'InputAttachments': [
            {
                'InputAttachmentName': 'string',
                'InputId': 'string',
                'InputSettings': {
                    'AudioSelectors': [
                        {
                            'Name': 'string',
                            'SelectorSettings': {
                                'AudioLanguageSelection': {
                                    'LanguageCode': 'string',
                                    'LanguageSelectionPolicy': 'LOOSE'|'STRICT'
                                },
                                'AudioPidSelection': {
                                    'Pid': 123
                                }
                            }
                        },
                    ],
                    'CaptionSelectors': [
                        {
                            'LanguageCode': 'string',
                            'Name': 'string',
                            'SelectorSettings': {
                                'AribSourceSettings': {},
                                'DvbSubSourceSettings': {
                                    'Pid': 123
                                },
                                'EmbeddedSourceSettings': {
                                    'Convert608To708': 'DISABLED'|'UPCONVERT',
                                    'Scte20Detection': 'AUTO'|'OFF',
                                    'Source608ChannelNumber': 123,
                                    'Source608TrackNumber': 123
                                },
                                'Scte20SourceSettings': {
                                    'Convert608To708': 'DISABLED'|'UPCONVERT',
                                    'Source608ChannelNumber': 123
                                },
                                'Scte27SourceSettings': {
                                    'Pid': 123
                                },
                                'TeletextSourceSettings': {
                                    'PageNumber': 'string'
                                }
                            }
                        },
                    ],
                    'DeblockFilter': 'DISABLED'|'ENABLED',
                    'DenoiseFilter': 'DISABLED'|'ENABLED',
                    'FilterStrength': 123,
                    'InputFilter': 'AUTO'|'DISABLED'|'FORCED',
                    'NetworkInputSettings': {
                        'HlsInputSettings': {
                            'Bandwidth': 123,
                            'BufferSegments': 123,
                            'Retries': 123,
                            'RetryInterval': 123
                        },
                        'ServerValidation': 'CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME'|'CHECK_CRYPTOGRAPHY_ONLY'
                    },
                    'SourceEndBehavior': 'CONTINUE'|'LOOP',
                    'VideoSelector': {
                        'ColorSpace': 'FOLLOW'|'REC_601'|'REC_709',
                        'ColorSpaceUsage': 'FALLBACK'|'FORCE',
                        'SelectorSettings': {
                            'VideoSelectorPid': {
                                'Pid': 123
                            },
                            'VideoSelectorProgramId': {
                                'ProgramId': 123
                            }
                        }
                    }
                }
            },
        ],
        'InputSpecification': {
            'Codec': 'MPEG2'|'AVC'|'HEVC',
            'MaximumBitrate': 'MAX_10_MBPS'|'MAX_20_MBPS'|'MAX_50_MBPS',
            'Resolution': 'SD'|'HD'|'UHD'
        },
        'LogLevel': 'ERROR'|'WARNING'|'INFO'|'DEBUG'|'DISABLED',
        'Name': 'string',
        'PipelinesRunningCount': 123,
        'RoleArn': 'string',
        'State': 'CREATING'|'CREATE_FAILED'|'IDLE'|'STARTING'|'RUNNING'|'RECOVERING'|'STOPPING'|'DELETING'|'DELETED'
    }
    
    
    """
    pass

def update_channel(ChannelId=None, Destinations=None, EncoderSettings=None, InputAttachments=None, InputSpecification=None, LogLevel=None, Name=None, RoleArn=None):
    """
    Updates a channel.
    See also: AWS API Documentation
    
    
    :example: response = client.update_channel(
        ChannelId='string',
        Destinations=[
            {
                'Id': 'string',
                'Settings': [
                    {
                        'PasswordParam': 'string',
                        'StreamName': 'string',
                        'Url': 'string',
                        'Username': 'string'
                    },
                ]
            },
        ],
        EncoderSettings={
            'AudioDescriptions': [
                {
                    'AudioNormalizationSettings': {
                        'Algorithm': 'ITU_1770_1'|'ITU_1770_2',
                        'AlgorithmControl': 'CORRECT_AUDIO',
                        'TargetLkfs': 123.0
                    },
                    'AudioSelectorName': 'string',
                    'AudioType': 'CLEAN_EFFECTS'|'HEARING_IMPAIRED'|'UNDEFINED'|'VISUAL_IMPAIRED_COMMENTARY',
                    'AudioTypeControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                    'CodecSettings': {
                        'AacSettings': {
                            'Bitrate': 123.0,
                            'CodingMode': 'AD_RECEIVER_MIX'|'CODING_MODE_1_0'|'CODING_MODE_1_1'|'CODING_MODE_2_0'|'CODING_MODE_5_1',
                            'InputType': 'BROADCASTER_MIXED_AD'|'NORMAL',
                            'Profile': 'HEV1'|'HEV2'|'LC',
                            'RateControlMode': 'CBR'|'VBR',
                            'RawFormat': 'LATM_LOAS'|'NONE',
                            'SampleRate': 123.0,
                            'Spec': 'MPEG2'|'MPEG4',
                            'VbrQuality': 'HIGH'|'LOW'|'MEDIUM_HIGH'|'MEDIUM_LOW'
                        },
                        'Ac3Settings': {
                            'Bitrate': 123.0,
                            'BitstreamMode': 'COMMENTARY'|'COMPLETE_MAIN'|'DIALOGUE'|'EMERGENCY'|'HEARING_IMPAIRED'|'MUSIC_AND_EFFECTS'|'VISUALLY_IMPAIRED'|'VOICE_OVER',
                            'CodingMode': 'CODING_MODE_1_0'|'CODING_MODE_1_1'|'CODING_MODE_2_0'|'CODING_MODE_3_2_LFE',
                            'Dialnorm': 123,
                            'DrcProfile': 'FILM_STANDARD'|'NONE',
                            'LfeFilter': 'DISABLED'|'ENABLED',
                            'MetadataControl': 'FOLLOW_INPUT'|'USE_CONFIGURED'
                        },
                        'Eac3Settings': {
                            'AttenuationControl': 'ATTENUATE_3_DB'|'NONE',
                            'Bitrate': 123.0,
                            'BitstreamMode': 'COMMENTARY'|'COMPLETE_MAIN'|'EMERGENCY'|'HEARING_IMPAIRED'|'VISUALLY_IMPAIRED',
                            'CodingMode': 'CODING_MODE_1_0'|'CODING_MODE_2_0'|'CODING_MODE_3_2',
                            'DcFilter': 'DISABLED'|'ENABLED',
                            'Dialnorm': 123,
                            'DrcLine': 'FILM_LIGHT'|'FILM_STANDARD'|'MUSIC_LIGHT'|'MUSIC_STANDARD'|'NONE'|'SPEECH',
                            'DrcRf': 'FILM_LIGHT'|'FILM_STANDARD'|'MUSIC_LIGHT'|'MUSIC_STANDARD'|'NONE'|'SPEECH',
                            'LfeControl': 'LFE'|'NO_LFE',
                            'LfeFilter': 'DISABLED'|'ENABLED',
                            'LoRoCenterMixLevel': 123.0,
                            'LoRoSurroundMixLevel': 123.0,
                            'LtRtCenterMixLevel': 123.0,
                            'LtRtSurroundMixLevel': 123.0,
                            'MetadataControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                            'PassthroughControl': 'NO_PASSTHROUGH'|'WHEN_POSSIBLE',
                            'PhaseControl': 'NO_SHIFT'|'SHIFT_90_DEGREES',
                            'StereoDownmix': 'DPL2'|'LO_RO'|'LT_RT'|'NOT_INDICATED',
                            'SurroundExMode': 'DISABLED'|'ENABLED'|'NOT_INDICATED',
                            'SurroundMode': 'DISABLED'|'ENABLED'|'NOT_INDICATED'
                        },
                        'Mp2Settings': {
                            'Bitrate': 123.0,
                            'CodingMode': 'CODING_MODE_1_0'|'CODING_MODE_2_0',
                            'SampleRate': 123.0
                        },
                        'PassThroughSettings': {}
    
                    },
                    'LanguageCode': 'string',
                    'LanguageCodeControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                    'Name': 'string',
                    'RemixSettings': {
                        'ChannelMappings': [
                            {
                                'InputChannelLevels': [
                                    {
                                        'Gain': 123,
                                        'InputChannel': 123
                                    },
                                ],
                                'OutputChannel': 123
                            },
                        ],
                        'ChannelsIn': 123,
                        'ChannelsOut': 123
                    },
                    'StreamName': 'string'
                },
            ],
            'AvailBlanking': {
                'AvailBlankingImage': {
                    'PasswordParam': 'string',
                    'Uri': 'string',
                    'Username': 'string'
                },
                'State': 'DISABLED'|'ENABLED'
            },
            'AvailConfiguration': {
                'AvailSettings': {
                    'Scte35SpliceInsert': {
                        'AdAvailOffset': 123,
                        'NoRegionalBlackoutFlag': 'FOLLOW'|'IGNORE',
                        'WebDeliveryAllowedFlag': 'FOLLOW'|'IGNORE'
                    },
                    'Scte35TimeSignalApos': {
                        'AdAvailOffset': 123,
                        'NoRegionalBlackoutFlag': 'FOLLOW'|'IGNORE',
                        'WebDeliveryAllowedFlag': 'FOLLOW'|'IGNORE'
                    }
                }
            },
            'BlackoutSlate': {
                'BlackoutSlateImage': {
                    'PasswordParam': 'string',
                    'Uri': 'string',
                    'Username': 'string'
                },
                'NetworkEndBlackout': 'DISABLED'|'ENABLED',
                'NetworkEndBlackoutImage': {
                    'PasswordParam': 'string',
                    'Uri': 'string',
                    'Username': 'string'
                },
                'NetworkId': 'string',
                'State': 'DISABLED'|'ENABLED'
            },
            'CaptionDescriptions': [
                {
                    'CaptionSelectorName': 'string',
                    'DestinationSettings': {
                        'AribDestinationSettings': {}
                        ,
                        'BurnInDestinationSettings': {
                            'Alignment': 'CENTERED'|'LEFT'|'SMART',
                            'BackgroundColor': 'BLACK'|'NONE'|'WHITE',
                            'BackgroundOpacity': 123,
                            'Font': {
                                'PasswordParam': 'string',
                                'Uri': 'string',
                                'Username': 'string'
                            },
                            'FontColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                            'FontOpacity': 123,
                            'FontResolution': 123,
                            'FontSize': 'string',
                            'OutlineColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                            'OutlineSize': 123,
                            'ShadowColor': 'BLACK'|'NONE'|'WHITE',
                            'ShadowOpacity': 123,
                            'ShadowXOffset': 123,
                            'ShadowYOffset': 123,
                            'TeletextGridControl': 'FIXED'|'SCALED',
                            'XPosition': 123,
                            'YPosition': 123
                        },
                        'DvbSubDestinationSettings': {
                            'Alignment': 'CENTERED'|'LEFT'|'SMART',
                            'BackgroundColor': 'BLACK'|'NONE'|'WHITE',
                            'BackgroundOpacity': 123,
                            'Font': {
                                'PasswordParam': 'string',
                                'Uri': 'string',
                                'Username': 'string'
                            },
                            'FontColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                            'FontOpacity': 123,
                            'FontResolution': 123,
                            'FontSize': 'string',
                            'OutlineColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                            'OutlineSize': 123,
                            'ShadowColor': 'BLACK'|'NONE'|'WHITE',
                            'ShadowOpacity': 123,
                            'ShadowXOffset': 123,
                            'ShadowYOffset': 123,
                            'TeletextGridControl': 'FIXED'|'SCALED',
                            'XPosition': 123,
                            'YPosition': 123
                        },
                        'EmbeddedDestinationSettings': {}
                        ,
                        'EmbeddedPlusScte20DestinationSettings': {}
                        ,
                        'RtmpCaptionInfoDestinationSettings': {}
                        ,
                        'Scte20PlusEmbeddedDestinationSettings': {}
                        ,
                        'Scte27DestinationSettings': {}
                        ,
                        'SmpteTtDestinationSettings': {}
                        ,
                        'TeletextDestinationSettings': {}
                        ,
                        'TtmlDestinationSettings': {
                            'StyleControl': 'PASSTHROUGH'|'USE_CONFIGURED'
                        },
                        'WebvttDestinationSettings': {}
    
                    },
                    'LanguageCode': 'string',
                    'LanguageDescription': 'string',
                    'Name': 'string'
                },
            ],
            'GlobalConfiguration': {
                'InitialAudioGain': 123,
                'InputEndAction': 'NONE'|'SWITCH_AND_LOOP_INPUTS',
                'InputLossBehavior': {
                    'BlackFrameMsec': 123,
                    'InputLossImageColor': 'string',
                    'InputLossImageSlate': {
                        'PasswordParam': 'string',
                        'Uri': 'string',
                        'Username': 'string'
                    },
                    'InputLossImageType': 'COLOR'|'SLATE',
                    'RepeatFrameMsec': 123
                },
                'OutputTimingSource': 'INPUT_CLOCK'|'SYSTEM_CLOCK',
                'SupportLowFramerateInputs': 'DISABLED'|'ENABLED'
            },
            'OutputGroups': [
                {
                    'Name': 'string',
                    'OutputGroupSettings': {
                        'ArchiveGroupSettings': {
                            'Destination': {
                                'DestinationRefId': 'string'
                            },
                            'RolloverInterval': 123
                        },
                        'HlsGroupSettings': {
                            'AdMarkers': [
                                'ADOBE'|'ELEMENTAL'|'ELEMENTAL_SCTE35',
                            ],
                            'BaseUrlContent': 'string',
                            'BaseUrlManifest': 'string',
                            'CaptionLanguageMappings': [
                                {
                                    'CaptionChannel': 123,
                                    'LanguageCode': 'string',
                                    'LanguageDescription': 'string'
                                },
                            ],
                            'CaptionLanguageSetting': 'INSERT'|'NONE'|'OMIT',
                            'ClientCache': 'DISABLED'|'ENABLED',
                            'CodecSpecification': 'RFC_4281'|'RFC_6381',
                            'ConstantIv': 'string',
                            'Destination': {
                                'DestinationRefId': 'string'
                            },
                            'DirectoryStructure': 'SINGLE_DIRECTORY'|'SUBDIRECTORY_PER_STREAM',
                            'EncryptionType': 'AES128'|'SAMPLE_AES',
                            'HlsCdnSettings': {
                                'HlsAkamaiSettings': {
                                    'ConnectionRetryInterval': 123,
                                    'FilecacheDuration': 123,
                                    'HttpTransferMode': 'CHUNKED'|'NON_CHUNKED',
                                    'NumRetries': 123,
                                    'RestartDelay': 123,
                                    'Salt': 'string',
                                    'Token': 'string'
                                },
                                'HlsBasicPutSettings': {
                                    'ConnectionRetryInterval': 123,
                                    'FilecacheDuration': 123,
                                    'NumRetries': 123,
                                    'RestartDelay': 123
                                },
                                'HlsMediaStoreSettings': {
                                    'ConnectionRetryInterval': 123,
                                    'FilecacheDuration': 123,
                                    'MediaStoreStorageClass': 'TEMPORAL',
                                    'NumRetries': 123,
                                    'RestartDelay': 123
                                },
                                'HlsWebdavSettings': {
                                    'ConnectionRetryInterval': 123,
                                    'FilecacheDuration': 123,
                                    'HttpTransferMode': 'CHUNKED'|'NON_CHUNKED',
                                    'NumRetries': 123,
                                    'RestartDelay': 123
                                }
                            },
                            'IndexNSegments': 123,
                            'InputLossAction': 'EMIT_OUTPUT'|'PAUSE_OUTPUT',
                            'IvInManifest': 'EXCLUDE'|'INCLUDE',
                            'IvSource': 'EXPLICIT'|'FOLLOWS_SEGMENT_NUMBER',
                            'KeepSegments': 123,
                            'KeyFormat': 'string',
                            'KeyFormatVersions': 'string',
                            'KeyProviderSettings': {
                                'StaticKeySettings': {
                                    'KeyProviderServer': {
                                        'PasswordParam': 'string',
                                        'Uri': 'string',
                                        'Username': 'string'
                                    },
                                    'StaticKeyValue': 'string'
                                }
                            },
                            'ManifestCompression': 'GZIP'|'NONE',
                            'ManifestDurationFormat': 'FLOATING_POINT'|'INTEGER',
                            'MinSegmentLength': 123,
                            'Mode': 'LIVE'|'VOD',
                            'OutputSelection': 'MANIFESTS_AND_SEGMENTS'|'SEGMENTS_ONLY',
                            'ProgramDateTime': 'EXCLUDE'|'INCLUDE',
                            'ProgramDateTimePeriod': 123,
                            'RedundantManifest': 'DISABLED'|'ENABLED',
                            'SegmentLength': 123,
                            'SegmentationMode': 'USE_INPUT_SEGMENTATION'|'USE_SEGMENT_DURATION',
                            'SegmentsPerSubdirectory': 123,
                            'StreamInfResolution': 'EXCLUDE'|'INCLUDE',
                            'TimedMetadataId3Frame': 'NONE'|'PRIV'|'TDRL',
                            'TimedMetadataId3Period': 123,
                            'TimestampDeltaMilliseconds': 123,
                            'TsFileMode': 'SEGMENTED_FILES'|'SINGLE_FILE'
                        },
                        'MsSmoothGroupSettings': {
                            'AcquisitionPointId': 'string',
                            'AudioOnlyTimecodeControl': 'PASSTHROUGH'|'USE_CONFIGURED_CLOCK',
                            'CertificateMode': 'SELF_SIGNED'|'VERIFY_AUTHENTICITY',
                            'ConnectionRetryInterval': 123,
                            'Destination': {
                                'DestinationRefId': 'string'
                            },
                            'EventId': 'string',
                            'EventIdMode': 'NO_EVENT_ID'|'USE_CONFIGURED'|'USE_TIMESTAMP',
                            'EventStopBehavior': 'NONE'|'SEND_EOS',
                            'FilecacheDuration': 123,
                            'FragmentLength': 123,
                            'InputLossAction': 'EMIT_OUTPUT'|'PAUSE_OUTPUT',
                            'NumRetries': 123,
                            'RestartDelay': 123,
                            'SegmentationMode': 'USE_INPUT_SEGMENTATION'|'USE_SEGMENT_DURATION',
                            'SendDelayMs': 123,
                            'SparseTrackType': 'NONE'|'SCTE_35',
                            'StreamManifestBehavior': 'DO_NOT_SEND'|'SEND',
                            'TimestampOffset': 'string',
                            'TimestampOffsetMode': 'USE_CONFIGURED_OFFSET'|'USE_EVENT_START_DATE'
                        },
                        'RtmpGroupSettings': {
                            'AuthenticationScheme': 'AKAMAI'|'COMMON',
                            'CacheFullBehavior': 'DISCONNECT_IMMEDIATELY'|'WAIT_FOR_SERVER',
                            'CacheLength': 123,
                            'CaptionData': 'ALL'|'FIELD1_608'|'FIELD1_AND_FIELD2_608',
                            'InputLossAction': 'EMIT_OUTPUT'|'PAUSE_OUTPUT',
                            'RestartDelay': 123
                        },
                        'UdpGroupSettings': {
                            'InputLossAction': 'DROP_PROGRAM'|'DROP_TS'|'EMIT_PROGRAM',
                            'TimedMetadataId3Frame': 'NONE'|'PRIV'|'TDRL',
                            'TimedMetadataId3Period': 123
                        }
                    },
                    'Outputs': [
                        {
                            'AudioDescriptionNames': [
                                'string',
                            ],
                            'CaptionDescriptionNames': [
                                'string',
                            ],
                            'OutputName': 'string',
                            'OutputSettings': {
                                'ArchiveOutputSettings': {
                                    'ContainerSettings': {
                                        'M2tsSettings': {
                                            'AbsentInputAudioBehavior': 'DROP'|'ENCODE_SILENCE',
                                            'Arib': 'DISABLED'|'ENABLED',
                                            'AribCaptionsPid': 'string',
                                            'AribCaptionsPidControl': 'AUTO'|'USE_CONFIGURED',
                                            'AudioBufferModel': 'ATSC'|'DVB',
                                            'AudioFramesPerPes': 123,
                                            'AudioPids': 'string',
                                            'AudioStreamType': 'ATSC'|'DVB',
                                            'Bitrate': 123,
                                            'BufferModel': 'MULTIPLEX'|'NONE',
                                            'CcDescriptor': 'DISABLED'|'ENABLED',
                                            'DvbNitSettings': {
                                                'NetworkId': 123,
                                                'NetworkName': 'string',
                                                'RepInterval': 123
                                            },
                                            'DvbSdtSettings': {
                                                'OutputSdt': 'SDT_FOLLOW'|'SDT_FOLLOW_IF_PRESENT'|'SDT_MANUAL'|'SDT_NONE',
                                                'RepInterval': 123,
                                                'ServiceName': 'string',
                                                'ServiceProviderName': 'string'
                                            },
                                            'DvbSubPids': 'string',
                                            'DvbTdtSettings': {
                                                'RepInterval': 123
                                            },
                                            'DvbTeletextPid': 'string',
                                            'Ebif': 'NONE'|'PASSTHROUGH',
                                            'EbpAudioInterval': 'VIDEO_AND_FIXED_INTERVALS'|'VIDEO_INTERVAL',
                                            'EbpLookaheadMs': 123,
                                            'EbpPlacement': 'VIDEO_AND_AUDIO_PIDS'|'VIDEO_PID',
                                            'EcmPid': 'string',
                                            'EsRateInPes': 'EXCLUDE'|'INCLUDE',
                                            'EtvPlatformPid': 'string',
                                            'EtvSignalPid': 'string',
                                            'FragmentTime': 123.0,
                                            'Klv': 'NONE'|'PASSTHROUGH',
                                            'KlvDataPids': 'string',
                                            'NullPacketBitrate': 123.0,
                                            'PatInterval': 123,
                                            'PcrControl': 'CONFIGURED_PCR_PERIOD'|'PCR_EVERY_PES_PACKET',
                                            'PcrPeriod': 123,
                                            'PcrPid': 'string',
                                            'PmtInterval': 123,
                                            'PmtPid': 'string',
                                            'ProgramNum': 123,
                                            'RateMode': 'CBR'|'VBR',
                                            'Scte27Pids': 'string',
                                            'Scte35Control': 'NONE'|'PASSTHROUGH',
                                            'Scte35Pid': 'string',
                                            'SegmentationMarkers': 'EBP'|'EBP_LEGACY'|'NONE'|'PSI_SEGSTART'|'RAI_ADAPT'|'RAI_SEGSTART',
                                            'SegmentationStyle': 'MAINTAIN_CADENCE'|'RESET_CADENCE',
                                            'SegmentationTime': 123.0,
                                            'TimedMetadataBehavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                            'TimedMetadataPid': 'string',
                                            'TransportStreamId': 123,
                                            'VideoPid': 'string'
                                        }
                                    },
                                    'Extension': 'string',
                                    'NameModifier': 'string'
                                },
                                'HlsOutputSettings': {
                                    'HlsSettings': {
                                        'AudioOnlyHlsSettings': {
                                            'AudioGroupId': 'string',
                                            'AudioOnlyImage': {
                                                'PasswordParam': 'string',
                                                'Uri': 'string',
                                                'Username': 'string'
                                            },
                                            'AudioTrackType': 'ALTERNATE_AUDIO_AUTO_SELECT'|'ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT'|'ALTERNATE_AUDIO_NOT_AUTO_SELECT'|'AUDIO_ONLY_VARIANT_STREAM'
                                        },
                                        'StandardHlsSettings': {
                                            'AudioRenditionSets': 'string',
                                            'M3u8Settings': {
                                                'AudioFramesPerPes': 123,
                                                'AudioPids': 'string',
                                                'EcmPid': 'string',
                                                'PatInterval': 123,
                                                'PcrControl': 'CONFIGURED_PCR_PERIOD'|'PCR_EVERY_PES_PACKET',
                                                'PcrPeriod': 123,
                                                'PcrPid': 'string',
                                                'PmtInterval': 123,
                                                'PmtPid': 'string',
                                                'ProgramNum': 123,
                                                'Scte35Behavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                                'Scte35Pid': 'string',
                                                'TimedMetadataBehavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                                'TimedMetadataPid': 'string',
                                                'TransportStreamId': 123,
                                                'VideoPid': 'string'
                                            }
                                        }
                                    },
                                    'NameModifier': 'string',
                                    'SegmentModifier': 'string'
                                },
                                'MsSmoothOutputSettings': {
                                    'NameModifier': 'string'
                                },
                                'RtmpOutputSettings': {
                                    'CertificateMode': 'SELF_SIGNED'|'VERIFY_AUTHENTICITY',
                                    'ConnectionRetryInterval': 123,
                                    'Destination': {
                                        'DestinationRefId': 'string'
                                    },
                                    'NumRetries': 123
                                },
                                'UdpOutputSettings': {
                                    'BufferMsec': 123,
                                    'ContainerSettings': {
                                        'M2tsSettings': {
                                            'AbsentInputAudioBehavior': 'DROP'|'ENCODE_SILENCE',
                                            'Arib': 'DISABLED'|'ENABLED',
                                            'AribCaptionsPid': 'string',
                                            'AribCaptionsPidControl': 'AUTO'|'USE_CONFIGURED',
                                            'AudioBufferModel': 'ATSC'|'DVB',
                                            'AudioFramesPerPes': 123,
                                            'AudioPids': 'string',
                                            'AudioStreamType': 'ATSC'|'DVB',
                                            'Bitrate': 123,
                                            'BufferModel': 'MULTIPLEX'|'NONE',
                                            'CcDescriptor': 'DISABLED'|'ENABLED',
                                            'DvbNitSettings': {
                                                'NetworkId': 123,
                                                'NetworkName': 'string',
                                                'RepInterval': 123
                                            },
                                            'DvbSdtSettings': {
                                                'OutputSdt': 'SDT_FOLLOW'|'SDT_FOLLOW_IF_PRESENT'|'SDT_MANUAL'|'SDT_NONE',
                                                'RepInterval': 123,
                                                'ServiceName': 'string',
                                                'ServiceProviderName': 'string'
                                            },
                                            'DvbSubPids': 'string',
                                            'DvbTdtSettings': {
                                                'RepInterval': 123
                                            },
                                            'DvbTeletextPid': 'string',
                                            'Ebif': 'NONE'|'PASSTHROUGH',
                                            'EbpAudioInterval': 'VIDEO_AND_FIXED_INTERVALS'|'VIDEO_INTERVAL',
                                            'EbpLookaheadMs': 123,
                                            'EbpPlacement': 'VIDEO_AND_AUDIO_PIDS'|'VIDEO_PID',
                                            'EcmPid': 'string',
                                            'EsRateInPes': 'EXCLUDE'|'INCLUDE',
                                            'EtvPlatformPid': 'string',
                                            'EtvSignalPid': 'string',
                                            'FragmentTime': 123.0,
                                            'Klv': 'NONE'|'PASSTHROUGH',
                                            'KlvDataPids': 'string',
                                            'NullPacketBitrate': 123.0,
                                            'PatInterval': 123,
                                            'PcrControl': 'CONFIGURED_PCR_PERIOD'|'PCR_EVERY_PES_PACKET',
                                            'PcrPeriod': 123,
                                            'PcrPid': 'string',
                                            'PmtInterval': 123,
                                            'PmtPid': 'string',
                                            'ProgramNum': 123,
                                            'RateMode': 'CBR'|'VBR',
                                            'Scte27Pids': 'string',
                                            'Scte35Control': 'NONE'|'PASSTHROUGH',
                                            'Scte35Pid': 'string',
                                            'SegmentationMarkers': 'EBP'|'EBP_LEGACY'|'NONE'|'PSI_SEGSTART'|'RAI_ADAPT'|'RAI_SEGSTART',
                                            'SegmentationStyle': 'MAINTAIN_CADENCE'|'RESET_CADENCE',
                                            'SegmentationTime': 123.0,
                                            'TimedMetadataBehavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                            'TimedMetadataPid': 'string',
                                            'TransportStreamId': 123,
                                            'VideoPid': 'string'
                                        }
                                    },
                                    'Destination': {
                                        'DestinationRefId': 'string'
                                    },
                                    'FecOutputSettings': {
                                        'ColumnDepth': 123,
                                        'IncludeFec': 'COLUMN'|'COLUMN_AND_ROW',
                                        'RowLength': 123
                                    }
                                }
                            },
                            'VideoDescriptionName': 'string'
                        },
                    ]
                },
            ],
            'TimecodeConfig': {
                'Source': 'EMBEDDED'|'SYSTEMCLOCK'|'ZEROBASED',
                'SyncThreshold': 123
            },
            'VideoDescriptions': [
                {
                    'CodecSettings': {
                        'H264Settings': {
                            'AdaptiveQuantization': 'HIGH'|'HIGHER'|'LOW'|'MAX'|'MEDIUM'|'OFF',
                            'AfdSignaling': 'AUTO'|'FIXED'|'NONE',
                            'Bitrate': 123,
                            'BufFillPct': 123,
                            'BufSize': 123,
                            'ColorMetadata': 'IGNORE'|'INSERT',
                            'EntropyEncoding': 'CABAC'|'CAVLC',
                            'FixedAfd': 'AFD_0000'|'AFD_0010'|'AFD_0011'|'AFD_0100'|'AFD_1000'|'AFD_1001'|'AFD_1010'|'AFD_1011'|'AFD_1101'|'AFD_1110'|'AFD_1111',
                            'FlickerAq': 'DISABLED'|'ENABLED',
                            'FramerateControl': 'INITIALIZE_FROM_SOURCE'|'SPECIFIED',
                            'FramerateDenominator': 123,
                            'FramerateNumerator': 123,
                            'GopBReference': 'DISABLED'|'ENABLED',
                            'GopClosedCadence': 123,
                            'GopNumBFrames': 123,
                            'GopSize': 123.0,
                            'GopSizeUnits': 'FRAMES'|'SECONDS',
                            'Level': 'H264_LEVEL_1'|'H264_LEVEL_1_1'|'H264_LEVEL_1_2'|'H264_LEVEL_1_3'|'H264_LEVEL_2'|'H264_LEVEL_2_1'|'H264_LEVEL_2_2'|'H264_LEVEL_3'|'H264_LEVEL_3_1'|'H264_LEVEL_3_2'|'H264_LEVEL_4'|'H264_LEVEL_4_1'|'H264_LEVEL_4_2'|'H264_LEVEL_5'|'H264_LEVEL_5_1'|'H264_LEVEL_5_2'|'H264_LEVEL_AUTO',
                            'LookAheadRateControl': 'HIGH'|'LOW'|'MEDIUM',
                            'MaxBitrate': 123,
                            'MinIInterval': 123,
                            'NumRefFrames': 123,
                            'ParControl': 'INITIALIZE_FROM_SOURCE'|'SPECIFIED',
                            'ParDenominator': 123,
                            'ParNumerator': 123,
                            'Profile': 'BASELINE'|'HIGH'|'HIGH_10BIT'|'HIGH_422'|'HIGH_422_10BIT'|'MAIN',
                            'QvbrQualityLevel': 123,
                            'RateControlMode': 'CBR'|'QVBR'|'VBR',
                            'ScanType': 'INTERLACED'|'PROGRESSIVE',
                            'SceneChangeDetect': 'DISABLED'|'ENABLED',
                            'Slices': 123,
                            'Softness': 123,
                            'SpatialAq': 'DISABLED'|'ENABLED',
                            'SubgopLength': 'DYNAMIC'|'FIXED',
                            'Syntax': 'DEFAULT'|'RP2027',
                            'TemporalAq': 'DISABLED'|'ENABLED',
                            'TimecodeInsertion': 'DISABLED'|'PIC_TIMING_SEI'
                        }
                    },
                    'Height': 123,
                    'Name': 'string',
                    'RespondToAfd': 'NONE'|'PASSTHROUGH'|'RESPOND',
                    'ScalingBehavior': 'DEFAULT'|'STRETCH_TO_OUTPUT',
                    'Sharpness': 123,
                    'Width': 123
                },
            ]
        },
        InputAttachments=[
            {
                'InputAttachmentName': 'string',
                'InputId': 'string',
                'InputSettings': {
                    'AudioSelectors': [
                        {
                            'Name': 'string',
                            'SelectorSettings': {
                                'AudioLanguageSelection': {
                                    'LanguageCode': 'string',
                                    'LanguageSelectionPolicy': 'LOOSE'|'STRICT'
                                },
                                'AudioPidSelection': {
                                    'Pid': 123
                                }
                            }
                        },
                    ],
                    'CaptionSelectors': [
                        {
                            'LanguageCode': 'string',
                            'Name': 'string',
                            'SelectorSettings': {
                                'AribSourceSettings': {}
                                ,
                                'DvbSubSourceSettings': {
                                    'Pid': 123
                                },
                                'EmbeddedSourceSettings': {
                                    'Convert608To708': 'DISABLED'|'UPCONVERT',
                                    'Scte20Detection': 'AUTO'|'OFF',
                                    'Source608ChannelNumber': 123,
                                    'Source608TrackNumber': 123
                                },
                                'Scte20SourceSettings': {
                                    'Convert608To708': 'DISABLED'|'UPCONVERT',
                                    'Source608ChannelNumber': 123
                                },
                                'Scte27SourceSettings': {
                                    'Pid': 123
                                },
                                'TeletextSourceSettings': {
                                    'PageNumber': 'string'
                                }
                            }
                        },
                    ],
                    'DeblockFilter': 'DISABLED'|'ENABLED',
                    'DenoiseFilter': 'DISABLED'|'ENABLED',
                    'FilterStrength': 123,
                    'InputFilter': 'AUTO'|'DISABLED'|'FORCED',
                    'NetworkInputSettings': {
                        'HlsInputSettings': {
                            'Bandwidth': 123,
                            'BufferSegments': 123,
                            'Retries': 123,
                            'RetryInterval': 123
                        },
                        'ServerValidation': 'CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME'|'CHECK_CRYPTOGRAPHY_ONLY'
                    },
                    'SourceEndBehavior': 'CONTINUE'|'LOOP',
                    'VideoSelector': {
                        'ColorSpace': 'FOLLOW'|'REC_601'|'REC_709',
                        'ColorSpaceUsage': 'FALLBACK'|'FORCE',
                        'SelectorSettings': {
                            'VideoSelectorPid': {
                                'Pid': 123
                            },
                            'VideoSelectorProgramId': {
                                'ProgramId': 123
                            }
                        }
                    }
                }
            },
        ],
        InputSpecification={
            'Codec': 'MPEG2'|'AVC'|'HEVC',
            'MaximumBitrate': 'MAX_10_MBPS'|'MAX_20_MBPS'|'MAX_50_MBPS',
            'Resolution': 'SD'|'HD'|'UHD'
        },
        LogLevel='ERROR'|'WARNING'|'INFO'|'DEBUG'|'DISABLED',
        Name='string',
        RoleArn='string'
    )
    
    
    :type ChannelId: string
    :param ChannelId: [REQUIRED] channel ID

    :type Destinations: list
    :param Destinations: A list of output destinations for this channel.
            (dict) -- Placeholder documentation for OutputDestination
            Id (string) -- User-specified id. This is used in an output group or an output.
            Settings (list) -- Destination settings for output; one for each redundant encoder.
            (dict) -- Placeholder documentation for OutputDestinationSettings
            PasswordParam (string) -- key used to extract the password from EC2 Parameter store
            StreamName (string) -- Stream name for RTMP destinations (URLs of type rtmp://)
            Url (string) -- A URL specifying a destination
            Username (string) -- username for destination
            
            

    :type EncoderSettings: dict
    :param EncoderSettings: The encoder settings for this channel.
            AudioDescriptions (list) -- [REQUIRED] Placeholder documentation for __listOfAudioDescription
            (dict) -- Placeholder documentation for AudioDescription
            AudioNormalizationSettings (dict) -- Advanced audio normalization settings.
            Algorithm (string) -- Audio normalization algorithm to use. itu17701 conforms to the CALM Act specification, itu17702 conforms to the EBU R-128 specification.
            AlgorithmControl (string) -- When set to correctAudio the output audio is corrected using the chosen algorithm. If set to measureOnly, the audio will be measured but not adjusted.
            TargetLkfs (float) -- Target LKFS(loudness) to adjust volume to. If no value is entered, a default value will be used according to the chosen algorithm. The CALM Act (1770-1) recommends a target of -24 LKFS. The EBU R-128 specification (1770-2) recommends a target of -23 LKFS.
            AudioSelectorName (string) -- [REQUIRED] The name of the AudioSelector used as the source for this AudioDescription.
            AudioType (string) -- Applies only if audioTypeControl is useConfigured. The values for audioType are defined in ISO-IEC 13818-1.
            AudioTypeControl (string) -- Determines how audio type is determined. followInput: If the input contains an ISO 639 audioType, then that value is passed through to the output. If the input contains no ISO 639 audioType, the value in Audio Type is included in the output. useConfigured: The value in Audio Type is included in the output. Note that this field and audioType are both ignored if inputType is broadcasterMixedAd.
            CodecSettings (dict) -- Audio codec settings.
            AacSettings (dict) -- Placeholder documentation for AacSettings
            Bitrate (float) -- Average bitrate in bits/second. Valid values depend on rate control mode and profile.
            CodingMode (string) -- Mono, Stereo, or 5.1 channel layout. Valid values depend on rate control mode and profile. The adReceiverMix setting receives a stereo description plus control track and emits a mono AAC encode of the description track, with control data emitted in the PES header as per ETSI TS 101 154 Annex E.
            InputType (string) -- Set to 'broadcasterMixedAd' when input contains pre-mixed main audio + AD (narration) as a stereo pair. The Audio Type field (audioType) will be set to 3, which signals to downstream systems that this stream contains 'broadcaster mixed AD'. Note that the input received by the encoder must contain pre-mixed audio; the encoder does not perform the mixing. The values in audioTypeControl and audioType (in AudioDescription) are ignored when set to broadcasterMixedAd. Leave set to 'normal' when input does not contain pre-mixed audio + AD.
            Profile (string) -- AAC Profile.
            RateControlMode (string) -- Rate Control Mode.
            RawFormat (string) -- Sets LATM / LOAS AAC output for raw containers.
            SampleRate (float) -- Sample rate in Hz. Valid values depend on rate control mode and profile.
            Spec (string) -- Use MPEG-2 AAC audio instead of MPEG-4 AAC audio for raw or MPEG-2 Transport Stream containers.
            VbrQuality (string) -- VBR Quality Level - Only used if rateControlMode is VBR.
            Ac3Settings (dict) -- Placeholder documentation for Ac3Settings
            Bitrate (float) -- Average bitrate in bits/second. Valid bitrates depend on the coding mode.
            BitstreamMode (string) -- Specifies the bitstream mode (bsmod) for the emitted AC-3 stream. See ATSC A/52-2012 for background on these values.
            CodingMode (string) -- Dolby Digital coding mode. Determines number of channels.
            Dialnorm (integer) -- Sets the dialnorm for the output. If excluded and input audio is Dolby Digital, dialnorm will be passed through.
            DrcProfile (string) -- If set to filmStandard, adds dynamic range compression signaling to the output bitstream as defined in the Dolby Digital specification.
            LfeFilter (string) -- When set to enabled, applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid in codingMode32Lfe mode.
            MetadataControl (string) -- When set to 'followInput', encoder metadata will be sourced from the DD, DD+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used.
            Eac3Settings (dict) -- Placeholder documentation for Eac3Settings
            AttenuationControl (string) -- When set to attenuate3Db, applies a 3 dB attenuation to the surround channels. Only used for 3/2 coding mode.
            Bitrate (float) -- Average bitrate in bits/second. Valid bitrates depend on the coding mode.
            BitstreamMode (string) -- Specifies the bitstream mode (bsmod) for the emitted E-AC-3 stream. See ATSC A/52-2012 (Annex E) for background on these values.
            CodingMode (string) -- Dolby Digital Plus coding mode. Determines number of channels.
            DcFilter (string) -- When set to enabled, activates a DC highpass filter for all input channels.
            Dialnorm (integer) -- Sets the dialnorm for the output. If blank and input audio is Dolby Digital Plus, dialnorm will be passed through.
            DrcLine (string) -- Sets the Dolby dynamic range compression profile.
            DrcRf (string) -- Sets the profile for heavy Dolby dynamic range compression, ensures that the instantaneous signal peaks do not exceed specified levels.
            LfeControl (string) -- When encoding 3/2 audio, setting to lfe enables the LFE channel
            LfeFilter (string) -- When set to enabled, applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with codingMode32 coding mode.
            LoRoCenterMixLevel (float) -- Left only/Right only center mix level. Only used for 3/2 coding mode.
            LoRoSurroundMixLevel (float) -- Left only/Right only surround mix level. Only used for 3/2 coding mode.
            LtRtCenterMixLevel (float) -- Left total/Right total center mix level. Only used for 3/2 coding mode.
            LtRtSurroundMixLevel (float) -- Left total/Right total surround mix level. Only used for 3/2 coding mode.
            MetadataControl (string) -- When set to followInput, encoder metadata will be sourced from the DD, DD+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used.
            PassthroughControl (string) -- When set to whenPossible, input DD+ audio will be passed through if it is present on the input. This detection is dynamic over the life of the transcode. Inputs that alternate between DD+ and non-DD+ content will have a consistent DD+ output as the system alternates between passthrough and encoding.
            PhaseControl (string) -- When set to shift90Degrees, applies a 90-degree phase shift to the surround channels. Only used for 3/2 coding mode.
            StereoDownmix (string) -- Stereo downmix preference. Only used for 3/2 coding mode.
            SurroundExMode (string) -- When encoding 3/2 audio, sets whether an extra center back surround channel is matrix encoded into the left and right surround channels.
            SurroundMode (string) -- When encoding 2/0 audio, sets whether Dolby Surround is matrix encoded into the two channels.
            Mp2Settings (dict) -- Placeholder documentation for Mp2Settings
            Bitrate (float) -- Average bitrate in bits/second.
            CodingMode (string) -- The MPEG2 Audio coding mode. Valid values are codingMode10 (for mono) or codingMode20 (for stereo).
            SampleRate (float) -- Sample rate in Hz.
            PassThroughSettings (dict) -- Placeholder documentation for PassThroughSettings
            LanguageCode (string) -- Indicates the language of the audio output track. Only used if languageControlMode is useConfigured, or there is no ISO 639 language code specified in the input.
            LanguageCodeControl (string) -- Choosing followInput will cause the ISO 639 language code of the output to follow the ISO 639 language code of the input. The languageCode will be used when useConfigured is set, or when followInput is selected but there is no ISO 639 language code specified by the input.
            Name (string) -- [REQUIRED] The name of this AudioDescription. Outputs will use this name to uniquely identify this AudioDescription. Description names should be unique within this Live Event.
            RemixSettings (dict) -- Settings that control how input audio channels are remixed into the output audio channels.
            ChannelMappings (list) -- [REQUIRED] Mapping of input channels to output channels, with appropriate gain adjustments.
            (dict) -- Placeholder documentation for AudioChannelMapping
            InputChannelLevels (list) -- [REQUIRED] Indices and gain values for each input channel that should be remixed into this output channel.
            (dict) -- Placeholder documentation for InputChannelLevel
            Gain (integer) -- [REQUIRED] Remixing value. Units are in dB and acceptable values are within the range from -60 (mute) and 6 dB.
            InputChannel (integer) -- [REQUIRED] The index of the input channel used as a source.
            
            OutputChannel (integer) -- [REQUIRED] The index of the output channel being produced.
            
            ChannelsIn (integer) -- Number of input channels to be used.
            ChannelsOut (integer) -- Number of output channels to be produced. Valid values: 1, 2, 4, 6, 8
            StreamName (string) -- Used for MS Smooth and Apple HLS outputs. Indicates the name displayed by the player (eg. English, or Director Commentary).
            
            AvailBlanking (dict) -- Settings for ad avail blanking.
            AvailBlankingImage (dict) -- Blanking image to be used. Leave empty for solid black. Only bmp and png images are supported.
            PasswordParam (string) -- key used to extract the password from EC2 Parameter store
            Uri (string) -- [REQUIRED] Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: 'rtmp://fmsserver/live'.
            Username (string) -- Documentation update needed
            State (string) -- When set to enabled, causes video, audio and captions to be blanked when insertion metadata is added.
            AvailConfiguration (dict) -- Event-wide configuration settings for ad avail insertion.
            AvailSettings (dict) -- Ad avail settings.
            Scte35SpliceInsert (dict) -- Placeholder documentation for Scte35SpliceInsert
            AdAvailOffset (integer) -- When specified, this offset (in milliseconds) is added to the input Ad Avail PTS time. This only applies to embedded SCTE 104/35 messages and does not apply to OOB messages.
            NoRegionalBlackoutFlag (string) -- When set to ignore, Segment Descriptors with noRegionalBlackoutFlag set to 0 will no longer trigger blackouts or Ad Avail slates
            WebDeliveryAllowedFlag (string) -- When set to ignore, Segment Descriptors with webDeliveryAllowedFlag set to 0 will no longer trigger blackouts or Ad Avail slates
            Scte35TimeSignalApos (dict) -- Placeholder documentation for Scte35TimeSignalApos
            AdAvailOffset (integer) -- When specified, this offset (in milliseconds) is added to the input Ad Avail PTS time. This only applies to embedded SCTE 104/35 messages and does not apply to OOB messages.
            NoRegionalBlackoutFlag (string) -- When set to ignore, Segment Descriptors with noRegionalBlackoutFlag set to 0 will no longer trigger blackouts or Ad Avail slates
            WebDeliveryAllowedFlag (string) -- When set to ignore, Segment Descriptors with webDeliveryAllowedFlag set to 0 will no longer trigger blackouts or Ad Avail slates
            
            BlackoutSlate (dict) -- Settings for blackout slate.
            BlackoutSlateImage (dict) -- Blackout slate image to be used. Leave empty for solid black. Only bmp and png images are supported.
            PasswordParam (string) -- key used to extract the password from EC2 Parameter store
            Uri (string) -- [REQUIRED] Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: 'rtmp://fmsserver/live'.
            Username (string) -- Documentation update needed
            NetworkEndBlackout (string) -- Setting to enabled causes the encoder to blackout the video, audio, and captions, and raise the 'Network Blackout Image' slate when an SCTE104/35 Network End Segmentation Descriptor is encountered. The blackout will be lifted when the Network Start Segmentation Descriptor is encountered. The Network End and Network Start descriptors must contain a network ID that matches the value entered in 'Network ID'.
            NetworkEndBlackoutImage (dict) -- Path to local file to use as Network End Blackout image. Image will be scaled to fill the entire output raster.
            PasswordParam (string) -- key used to extract the password from EC2 Parameter store
            Uri (string) -- [REQUIRED] Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: 'rtmp://fmsserver/live'.
            Username (string) -- Documentation update needed
            NetworkId (string) -- Provides Network ID that matches EIDR ID format (e.g., '10.XXXX/XXXX-XXXX-XXXX-XXXX-XXXX-C').
            State (string) -- When set to enabled, causes video, audio and captions to be blanked when indicated by program metadata.
            CaptionDescriptions (list) -- Settings for caption decriptions
            (dict) -- Output groups for this Live Event. Output groups contain information about where streams should be distributed.
            CaptionSelectorName (string) -- [REQUIRED] Specifies which input caption selector to use as a caption source when generating output captions. This field should match a captionSelector name.
            DestinationSettings (dict) -- Additional settings for captions destination that depend on the destination type.
            AribDestinationSettings (dict) -- Placeholder documentation for AribDestinationSettings
            BurnInDestinationSettings (dict) -- Placeholder documentation for BurnInDestinationSettings
            Alignment (string) -- If no explicit xPosition or yPosition is provided, setting alignment to centered will place the captions at the bottom center of the output. Similarly, setting a left alignment will align captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. Selecting 'smart' justification will left-justify live subtitles and center-justify pre-recorded subtitles. All burn-in and DVB-Sub font settings must match.
            BackgroundColor (string) -- Specifies the color of the rectangle behind the captions. All burn-in and DVB-Sub font settings must match.
            BackgroundOpacity (integer) -- Specifies the opacity of the background rectangle. 255 is opaque; 0 is transparent. Leaving this parameter out is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
            Font (dict) -- External font file used for caption burn-in. File extension must be 'ttf' or 'tte'. Although the user can select output fonts for many different types of input captions, embedded, STL and teletext sources use a strict grid system. Using external fonts with these caption sources could cause unexpected display of proportional fonts. All burn-in and DVB-Sub font settings must match.
            PasswordParam (string) -- key used to extract the password from EC2 Parameter store
            Uri (string) -- [REQUIRED] Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: 'rtmp://fmsserver/live'.
            Username (string) -- Documentation update needed
            FontColor (string) -- Specifies the color of the burned-in captions. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
            FontOpacity (integer) -- Specifies the opacity of the burned-in captions. 255 is opaque; 0 is transparent. All burn-in and DVB-Sub font settings must match.
            FontResolution (integer) -- Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and DVB-Sub font settings must match.
            FontSize (string) -- When set to 'auto' fontSize will scale depending on the size of the output. Giving a positive integer will specify the exact font size in points. All burn-in and DVB-Sub font settings must match.
            OutlineColor (string) -- Specifies font outline color. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
            OutlineSize (integer) -- Specifies font outline size in pixels. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
            ShadowColor (string) -- Specifies the color of the shadow cast by the captions. All burn-in and DVB-Sub font settings must match.
            ShadowOpacity (integer) -- Specifies the opacity of the shadow. 255 is opaque; 0 is transparent. Leaving this parameter out is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
            ShadowXOffset (integer) -- Specifies the horizontal offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left. All burn-in and DVB-Sub font settings must match.
            ShadowYOffset (integer) -- Specifies the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. All burn-in and DVB-Sub font settings must match.
            TeletextGridControl (string) -- Controls whether a fixed grid size will be used to generate the output subtitles bitmap. Only applicable for Teletext inputs and DVB-Sub/Burn-in outputs.
            XPosition (integer) -- Specifies the horizontal position of the caption relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit xPosition is provided, the horizontal caption position will be determined by the alignment parameter. All burn-in and DVB-Sub font settings must match.
            YPosition (integer) -- Specifies the vertical position of the caption relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit yPosition is provided, the caption will be positioned towards the bottom of the output. All burn-in and DVB-Sub font settings must match.
            DvbSubDestinationSettings (dict) -- Placeholder documentation for DvbSubDestinationSettings
            Alignment (string) -- If no explicit xPosition or yPosition is provided, setting alignment to centered will place the captions at the bottom center of the output. Similarly, setting a left alignment will align captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. Selecting 'smart' justification will left-justify live subtitles and center-justify pre-recorded subtitles. This option is not valid for source captions that are STL or 608/embedded. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
            BackgroundColor (string) -- Specifies the color of the rectangle behind the captions. All burn-in and DVB-Sub font settings must match.
            BackgroundOpacity (integer) -- Specifies the opacity of the background rectangle. 255 is opaque; 0 is transparent. Leaving this parameter blank is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
            Font (dict) -- External font file used for caption burn-in. File extension must be 'ttf' or 'tte'. Although the user can select output fonts for many different types of input captions, embedded, STL and teletext sources use a strict grid system. Using external fonts with these caption sources could cause unexpected display of proportional fonts. All burn-in and DVB-Sub font settings must match.
            PasswordParam (string) -- key used to extract the password from EC2 Parameter store
            Uri (string) -- [REQUIRED] Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: 'rtmp://fmsserver/live'.
            Username (string) -- Documentation update needed
            FontColor (string) -- Specifies the color of the burned-in captions. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
            FontOpacity (integer) -- Specifies the opacity of the burned-in captions. 255 is opaque; 0 is transparent. All burn-in and DVB-Sub font settings must match.
            FontResolution (integer) -- Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and DVB-Sub font settings must match.
            FontSize (string) -- When set to auto fontSize will scale depending on the size of the output. Giving a positive integer will specify the exact font size in points. All burn-in and DVB-Sub font settings must match.
            OutlineColor (string) -- Specifies font outline color. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
            OutlineSize (integer) -- Specifies font outline size in pixels. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
            ShadowColor (string) -- Specifies the color of the shadow cast by the captions. All burn-in and DVB-Sub font settings must match.
            ShadowOpacity (integer) -- Specifies the opacity of the shadow. 255 is opaque; 0 is transparent. Leaving this parameter blank is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
            ShadowXOffset (integer) -- Specifies the horizontal offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left. All burn-in and DVB-Sub font settings must match.
            ShadowYOffset (integer) -- Specifies the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. All burn-in and DVB-Sub font settings must match.
            TeletextGridControl (string) -- Controls whether a fixed grid size will be used to generate the output subtitles bitmap. Only applicable for Teletext inputs and DVB-Sub/Burn-in outputs.
            XPosition (integer) -- Specifies the horizontal position of the caption relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit xPosition is provided, the horizontal caption position will be determined by the alignment parameter. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
            YPosition (integer) -- Specifies the vertical position of the caption relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit yPosition is provided, the caption will be positioned towards the bottom of the output. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
            EmbeddedDestinationSettings (dict) -- Placeholder documentation for EmbeddedDestinationSettings
            EmbeddedPlusScte20DestinationSettings (dict) -- Placeholder documentation for EmbeddedPlusScte20DestinationSettings
            RtmpCaptionInfoDestinationSettings (dict) -- Placeholder documentation for RtmpCaptionInfoDestinationSettings
            Scte20PlusEmbeddedDestinationSettings (dict) -- Placeholder documentation for Scte20PlusEmbeddedDestinationSettings
            Scte27DestinationSettings (dict) -- Placeholder documentation for Scte27DestinationSettings
            SmpteTtDestinationSettings (dict) -- Placeholder documentation for SmpteTtDestinationSettings
            TeletextDestinationSettings (dict) -- Placeholder documentation for TeletextDestinationSettings
            TtmlDestinationSettings (dict) -- Placeholder documentation for TtmlDestinationSettings
            StyleControl (string) -- When set to passthrough, passes through style and position information from a TTML-like input source (TTML, SMPTE-TT, CFF-TT) to the CFF-TT output or TTML output.
            WebvttDestinationSettings (dict) -- Placeholder documentation for WebvttDestinationSettings
            LanguageCode (string) -- ISO 639-2 three-digit code: http://www.loc.gov/standards/iso639-2/
            LanguageDescription (string) -- Human readable information to indicate captions available for players (eg. English, or Spanish).
            Name (string) -- [REQUIRED] Name of the caption description. Used to associate a caption description with an output. Names must be unique within an event.
            
            GlobalConfiguration (dict) -- Configuration settings that apply to the event as a whole.
            InitialAudioGain (integer) -- Value to set the initial audio gain for the Live Event.
            InputEndAction (string) -- Indicates the action to take when the current input completes (e.g. end-of-file). When switchAndLoopInputs is configured the encoder will restart at the beginning of the first input. When 'none' is configured the encoder will transcode either black, a solid color, or a user specified slate images per the 'Input Loss Behavior' configuration until the next input switch occurs (which is controlled through the Channel Schedule API).
            InputLossBehavior (dict) -- Settings for system actions when input is lost.
            BlackFrameMsec (integer) -- Documentation update needed
            InputLossImageColor (string) -- When input loss image type is 'color' this field specifies the color to use. Value: 6 hex characters representing the values of RGB.
            InputLossImageSlate (dict) -- When input loss image type is 'slate' these fields specify the parameters for accessing the slate.
            PasswordParam (string) -- key used to extract the password from EC2 Parameter store
            Uri (string) -- [REQUIRED] Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: 'rtmp://fmsserver/live'.
            Username (string) -- Documentation update needed
            InputLossImageType (string) -- Indicates whether to substitute a solid color or a slate into the output after input loss exceeds blackFrameMsec.
            RepeatFrameMsec (integer) -- Documentation update needed
            OutputTimingSource (string) -- Indicates whether the rate of frames emitted by the Live encoder should be paced by its system clock (which optionally may be locked to another source via NTP) or should be locked to the clock of the source that is providing the input stream.
            SupportLowFramerateInputs (string) -- Adjusts video input buffer for streams with very low video framerates. This is commonly set to enabled for music channels with less than one video frame per second.
            OutputGroups (list) -- [REQUIRED] Placeholder documentation for __listOfOutputGroup
            (dict) -- Output groups for this Live Event. Output groups contain information about where streams should be distributed.
            Name (string) -- Custom output group name optionally defined by the user. Only letters, numbers, and the underscore character allowed; only 32 characters allowed.
            OutputGroupSettings (dict) -- [REQUIRED] Settings associated with the output group.
            ArchiveGroupSettings (dict) -- Placeholder documentation for ArchiveGroupSettings
            Destination (dict) -- [REQUIRED] A directory and base filename where archive files should be written. If the base filename portion of the URI is left blank, the base filename of the first input will be automatically inserted.
            DestinationRefId (string) -- Placeholder documentation for __string
            RolloverInterval (integer) -- Number of seconds to write to archive file before closing and starting a new one.
            HlsGroupSettings (dict) -- Placeholder documentation for HlsGroupSettings
            AdMarkers (list) -- Choose one or more ad marker types to pass SCTE35 signals through to this group of Apple HLS outputs.
            (string) -- Placeholder documentation for HlsAdMarkers
            BaseUrlContent (string) -- A partial URI prefix that will be prepended to each output in the media .m3u8 file. Can be used if base manifest is delivered from a different URL than the main .m3u8 file.
            BaseUrlManifest (string) -- A partial URI prefix that will be prepended to each output in the media .m3u8 file. Can be used if base manifest is delivered from a different URL than the main .m3u8 file.
            CaptionLanguageMappings (list) -- Mapping of up to 4 caption channels to caption languages. Is only meaningful if captionLanguageSetting is set to 'insert'.
            (dict) -- Maps a caption channel to an ISO 693-2 language code (http://www.loc.gov/standards/iso639-2), with an optional description.
            CaptionChannel (integer) -- [REQUIRED] The closed caption channel being described by this CaptionLanguageMapping. Each channel mapping must have a unique channel number (maximum of 4)
            LanguageCode (string) -- [REQUIRED] Three character ISO 639-2 language code (see http://www.loc.gov/standards/iso639-2)
            LanguageDescription (string) -- [REQUIRED] Textual description of language
            
            CaptionLanguageSetting (string) -- Applies only to 608 Embedded output captions. insert: Include CLOSED-CAPTIONS lines in the manifest. Specify at least one language in the CC1 Language Code field. One CLOSED-CAPTION line is added for each Language Code you specify. Make sure to specify the languages in the order in which they appear in the original source (if the source is embedded format) or the order of the caption selectors (if the source is other than embedded). Otherwise, languages in the manifest will not match up properly with the output captions. none: Include CLOSED-CAPTIONS=NONE line in the manifest. omit: Omit any CLOSED-CAPTIONS line from the manifest.
            ClientCache (string) -- When set to 'disabled', sets the #EXT-X-ALLOW-CACHE:no tag in the manifest, which prevents clients from saving media segments for later replay.
            CodecSpecification (string) -- Specification to use (RFC-6381 or the default RFC-4281) during m3u8 playlist generation.
            ConstantIv (string) -- For use with encryptionType. This is a 128-bit, 16-byte hex value represented by a 32-character text string. If ivSource is set to 'explicit' then this parameter is required and is used as the IV for encryption.
            Destination (dict) -- [REQUIRED] A directory or HTTP destination for the HLS segments, manifest files, and encryption keys (if enabled).
            DestinationRefId (string) -- Placeholder documentation for __string
            DirectoryStructure (string) -- Place segments in subdirectories.
            EncryptionType (string) -- Encrypts the segments with the given encryption scheme. Exclude this parameter if no encryption is desired.
            HlsCdnSettings (dict) -- Parameters that control interactions with the CDN.
            HlsAkamaiSettings (dict) -- Placeholder documentation for HlsAkamaiSettings
            ConnectionRetryInterval (integer) -- Number of seconds to wait before retrying connection to the CDN if the connection is lost.
            FilecacheDuration (integer) -- Size in seconds of file cache for streaming outputs.
            HttpTransferMode (string) -- Specify whether or not to use chunked transfer encoding to Akamai. User should contact Akamai to enable this feature.
            NumRetries (integer) -- Number of retry attempts that will be made before the Live Event is put into an error state.
            RestartDelay (integer) -- If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart.
            Salt (string) -- Salt for authenticated Akamai.
            Token (string) -- Token parameter for authenticated akamai. If not specified, _gda_ is used.
            HlsBasicPutSettings (dict) -- Placeholder documentation for HlsBasicPutSettings
            ConnectionRetryInterval (integer) -- Number of seconds to wait before retrying connection to the CDN if the connection is lost.
            FilecacheDuration (integer) -- Size in seconds of file cache for streaming outputs.
            NumRetries (integer) -- Number of retry attempts that will be made before the Live Event is put into an error state.
            RestartDelay (integer) -- If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart.
            HlsMediaStoreSettings (dict) -- Placeholder documentation for HlsMediaStoreSettings
            ConnectionRetryInterval (integer) -- Number of seconds to wait before retrying connection to the CDN if the connection is lost.
            FilecacheDuration (integer) -- Size in seconds of file cache for streaming outputs.
            MediaStoreStorageClass (string) -- When set to temporal, output files are stored in non-persistent memory for faster reading and writing.
            NumRetries (integer) -- Number of retry attempts that will be made before the Live Event is put into an error state.
            RestartDelay (integer) -- If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart.
            HlsWebdavSettings (dict) -- Placeholder documentation for HlsWebdavSettings
            ConnectionRetryInterval (integer) -- Number of seconds to wait before retrying connection to the CDN if the connection is lost.
            FilecacheDuration (integer) -- Size in seconds of file cache for streaming outputs.
            HttpTransferMode (string) -- Specify whether or not to use chunked transfer encoding to WebDAV.
            NumRetries (integer) -- Number of retry attempts that will be made before the Live Event is put into an error state.
            RestartDelay (integer) -- If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart.
            
            IndexNSegments (integer) -- If mode is 'live', the number of segments to retain in the manifest (.m3u8) file. This number must be less than or equal to keepSegments. If mode is 'vod', this parameter has no effect.
            InputLossAction (string) -- Parameter that control output group behavior on input loss.
            IvInManifest (string) -- For use with encryptionType. The IV (Initialization Vector) is a 128-bit number used in conjunction with the key for encrypting blocks. If set to 'include', IV is listed in the manifest, otherwise the IV is not in the manifest.
            IvSource (string) -- For use with encryptionType. The IV (Initialization Vector) is a 128-bit number used in conjunction with the key for encrypting blocks. If this setting is 'followsSegmentNumber', it will cause the IV to change every segment (to match the segment number). If this is set to 'explicit', you must enter a constantIv value.
            KeepSegments (integer) -- If mode is 'live', the number of TS segments to retain in the destination directory. If mode is 'vod', this parameter has no effect.
            KeyFormat (string) -- The value specifies how the key is represented in the resource identified by the URI. If parameter is absent, an implicit value of 'identity' is used. A reverse DNS string can also be given.
            KeyFormatVersions (string) -- Either a single positive integer version value or a slash delimited list of version values (1/2/3).
            KeyProviderSettings (dict) -- The key provider settings.
            StaticKeySettings (dict) -- Placeholder documentation for StaticKeySettings
            KeyProviderServer (dict) -- The URL of the license server used for protecting content.
            PasswordParam (string) -- key used to extract the password from EC2 Parameter store
            Uri (string) -- [REQUIRED] Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: 'rtmp://fmsserver/live'.
            Username (string) -- Documentation update needed
            StaticKeyValue (string) -- [REQUIRED] Static key value as a 32 character hexadecimal string.
            
            ManifestCompression (string) -- When set to gzip, compresses HLS playlist.
            ManifestDurationFormat (string) -- Indicates whether the output manifest should use floating point or integer values for segment duration.
            MinSegmentLength (integer) -- When set, minimumSegmentLength is enforced by looking ahead and back within the specified range for a nearby avail and extending the segment size if needed.
            Mode (string) -- If 'vod', all segments are indexed and kept permanently in the destination and manifest. If 'live', only the number segments specified in keepSegments and indexNSegments are kept; newer segments replace older segments, which may prevent players from rewinding all the way to the beginning of the event. VOD mode uses HLS EXT-X-PLAYLIST-TYPE of EVENT while the channel is running, converting it to a 'VOD' type manifest on completion of the stream.
            OutputSelection (string) -- Generates the .m3u8 playlist file for this HLS output group. The segmentsOnly option will output segments without the .m3u8 file.
            ProgramDateTime (string) -- Includes or excludes EXT-X-PROGRAM-DATE-TIME tag in .m3u8 manifest files. The value is calculated as follows: either the program date and time are initialized using the input timecode source, or the time is initialized using the input timecode source and the date is initialized using the timestampOffset.
            ProgramDateTimePeriod (integer) -- Period of insertion of EXT-X-PROGRAM-DATE-TIME entry, in seconds.
            RedundantManifest (string) -- When set to 'enabled', includes the media playlists from both pipelines in the master manifest (.m3u8) file.
            SegmentLength (integer) -- Length of MPEG-2 Transport Stream segments to create (in seconds). Note that segments will end on the next keyframe after this number of seconds, so actual segment length may be longer.
            SegmentationMode (string) -- useInputSegmentation has been deprecated. The configured segment size is always used.
            SegmentsPerSubdirectory (integer) -- Number of segments to write to a subdirectory before starting a new one. directoryStructure must be subdirectoryPerStream for this setting to have an effect.
            StreamInfResolution (string) -- Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag of variant manifest.
            TimedMetadataId3Frame (string) -- Indicates ID3 frame that has the timecode.
            TimedMetadataId3Period (integer) -- Timed Metadata interval in seconds.
            TimestampDeltaMilliseconds (integer) -- Provides an extra millisecond delta offset to fine tune the timestamps.
            TsFileMode (string) -- When set to 'singleFile', emits the program as a single media resource (.ts) file, and uses #EXT-X-BYTERANGE tags to index segment for playback. Playback of VOD mode content during event is not guaranteed due to HTTP server caching.
            MsSmoothGroupSettings (dict) -- Placeholder documentation for MsSmoothGroupSettings
            AcquisitionPointId (string) -- The value of the 'Acquisition Point Identity' element used in each message placed in the sparse track. Only enabled if sparseTrackType is not 'none'.
            AudioOnlyTimecodeControl (string) -- If set to passthrough for an audio-only MS Smooth output, the fragment absolute time will be set to the current timecode. This option does not write timecodes to the audio elementary stream.
            CertificateMode (string) -- If set to verifyAuthenticity, verify the https certificate chain to a trusted Certificate Authority (CA). This will cause https outputs to self-signed certificates to fail.
            ConnectionRetryInterval (integer) -- Number of seconds to wait before retrying connection to the IIS server if the connection is lost. Content will be cached during this time and the cache will be be delivered to the IIS server once the connection is re-established.
            Destination (dict) -- [REQUIRED] Smooth Streaming publish point on an IIS server. Elemental Live acts as a 'Push' encoder to IIS.
            DestinationRefId (string) -- Placeholder documentation for __string
            EventId (string) -- MS Smooth event ID to be sent to the IIS server. Should only be specified if eventIdMode is set to useConfigured.
            EventIdMode (string) -- Specifies whether or not to send an event ID to the IIS server. If no event ID is sent and the same Live Event is used without changing the publishing point, clients might see cached video from the previous run. Options: - 'useConfigured' - use the value provided in eventId - 'useTimestamp' - generate and send an event ID based on the current timestamp - 'noEventId' - do not send an event ID to the IIS server.
            EventStopBehavior (string) -- When set to sendEos, send EOS signal to IIS server when stopping the event
            FilecacheDuration (integer) -- Size in seconds of file cache for streaming outputs.
            FragmentLength (integer) -- Length of mp4 fragments to generate (in seconds). Fragment length must be compatible with GOP size and framerate.
            InputLossAction (string) -- Parameter that control output group behavior on input loss.
            NumRetries (integer) -- Number of retry attempts.
            RestartDelay (integer) -- Number of seconds before initiating a restart due to output failure, due to exhausting the numRetries on one segment, or exceeding filecacheDuration.
            SegmentationMode (string) -- useInputSegmentation has been deprecated. The configured segment size is always used.
            SendDelayMs (integer) -- Number of milliseconds to delay the output from the second pipeline.
            SparseTrackType (string) -- If set to scte35, use incoming SCTE-35 messages to generate a sparse track in this group of MS-Smooth outputs.
            StreamManifestBehavior (string) -- When set to send, send stream manifest so publishing point doesn't start until all streams start.
            TimestampOffset (string) -- Timestamp offset for the event. Only used if timestampOffsetMode is set to useConfiguredOffset.
            TimestampOffsetMode (string) -- Type of timestamp date offset to use. - useEventStartDate: Use the date the event was started as the offset - useConfiguredOffset: Use an explicitly configured date as the offset
            RtmpGroupSettings (dict) -- Placeholder documentation for RtmpGroupSettings
            AuthenticationScheme (string) -- Authentication scheme to use when connecting with CDN
            CacheFullBehavior (string) -- Controls behavior when content cache fills up. If remote origin server stalls the RTMP connection and does not accept content fast enough the 'Media Cache' will fill up. When the cache reaches the duration specified by cacheLength the cache will stop accepting new content. If set to disconnectImmediately, the RTMP output will force a disconnect. Clear the media cache, and reconnect after restartDelay seconds. If set to waitForServer, the RTMP output will wait up to 5 minutes to allow the origin server to begin accepting data again.
            CacheLength (integer) -- Cache length, in seconds, is used to calculate buffer size.
            CaptionData (string) -- Controls the types of data that passes to onCaptionInfo outputs. If set to 'all' then 608 and 708 carried DTVCC data will be passed. If set to 'field1AndField2608' then DTVCC data will be stripped out, but 608 data from both fields will be passed. If set to 'field1608' then only the data carried in 608 from field 1 video will be passed.
            InputLossAction (string) -- Controls the behavior of this RTMP group if input becomes unavailable. - emitOutput: Emit a slate until input returns. - pauseOutput: Stop transmitting data until input returns. This does not close the underlying RTMP connection.
            RestartDelay (integer) -- If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart.
            UdpGroupSettings (dict) -- Placeholder documentation for UdpGroupSettings
            InputLossAction (string) -- Specifies behavior of last resort when input video is lost, and no more backup inputs are available. When dropTs is selected the entire transport stream will stop being emitted. When dropProgram is selected the program can be dropped from the transport stream (and replaced with null packets to meet the TS bitrate requirement). Or, when emitProgram is chosen the transport stream will continue to be produced normally with repeat frames, black frames, or slate frames substituted for the absent input video.
            TimedMetadataId3Frame (string) -- Indicates ID3 frame that has the timecode.
            TimedMetadataId3Period (integer) -- Timed Metadata interval in seconds.
            
            Outputs (list) -- [REQUIRED] Placeholder documentation for __listOfOutput
            (dict) -- Output settings. There can be multiple outputs within a group.
            AudioDescriptionNames (list) -- The names of the AudioDescriptions used as audio sources for this output.
            (string) -- Placeholder documentation for __string
            CaptionDescriptionNames (list) -- The names of the CaptionDescriptions used as caption sources for this output.
            (string) -- Placeholder documentation for __string
            OutputName (string) -- The name used to identify an output.
            OutputSettings (dict) -- [REQUIRED] Output type-specific settings.
            ArchiveOutputSettings (dict) -- Placeholder documentation for ArchiveOutputSettings
            ContainerSettings (dict) -- [REQUIRED] Settings specific to the container type of the file.
            M2tsSettings (dict) -- Placeholder documentation for M2tsSettings
            AbsentInputAudioBehavior (string) -- When set to drop, output audio streams will be removed from the program if the selected input audio stream is removed from the input. This allows the output audio configuration to dynamically change based on input configuration. If this is set to encodeSilence, all output audio streams will output encoded silence when not connected to an active input stream.
            Arib (string) -- When set to enabled, uses ARIB-compliant field muxing and removes video descriptor.
            AribCaptionsPid (string) -- Packet Identifier (PID) for ARIB Captions in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            AribCaptionsPidControl (string) -- If set to auto, pid number used for ARIB Captions will be auto-selected from unused pids. If set to useConfigured, ARIB Captions will be on the configured pid number.
            AudioBufferModel (string) -- When set to dvb, uses DVB buffer model for Dolby Digital audio. When set to atsc, the ATSC model is used.
            AudioFramesPerPes (integer) -- The number of audio frames to insert for each PES packet.
            AudioPids (string) -- Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
            AudioStreamType (string) -- When set to atsc, uses stream type = 0x81 for AC3 and stream type = 0x87 for EAC3. When set to dvb, uses stream type = 0x06.
            Bitrate (integer) -- The output bitrate of the transport stream in bits per second. Setting to 0 lets the muxer automatically determine the appropriate bitrate.
            BufferModel (string) -- If set to multiplex, use multiplex buffer model for accurate interleaving. Setting to bufferModel to none can lead to lower latency, but low-memory devices may not be able to play back the stream without interruptions.
            CcDescriptor (string) -- When set to enabled, generates captionServiceDescriptor in PMT.
            DvbNitSettings (dict) -- Inserts DVB Network Information Table (NIT) at the specified table repetition interval.
            NetworkId (integer) -- [REQUIRED] The numeric value placed in the Network Information Table (NIT).
            NetworkName (string) -- [REQUIRED] The network name text placed in the networkNameDescriptor inside the Network Information Table. Maximum length is 256 characters.
            RepInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream.
            DvbSdtSettings (dict) -- Inserts DVB Service Description Table (SDT) at the specified table repetition interval.
            OutputSdt (string) -- Selects method of inserting SDT information into output stream. The sdtFollow setting copies SDT information from input stream to output stream. The sdtFollowIfPresent setting copies SDT information from input stream to output stream if SDT information is present in the input, otherwise it will fall back on the user-defined values. The sdtManual setting means user will enter the SDT information. The sdtNone setting means output stream will not contain SDT information.
            RepInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream.
            ServiceName (string) -- The service name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters.
            ServiceProviderName (string) -- The service provider name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters.
            DvbSubPids (string) -- Packet Identifier (PID) for input source DVB Subtitle data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
            DvbTdtSettings (dict) -- Inserts DVB Time and Date Table (TDT) at the specified table repetition interval.
            RepInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream.
            DvbTeletextPid (string) -- Packet Identifier (PID) for input source DVB Teletext data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            Ebif (string) -- If set to passthrough, passes any EBIF data from the input source to this output.
            EbpAudioInterval (string) -- When videoAndFixedIntervals is selected, audio EBP markers will be added to partitions 3 and 4. The interval between these additional markers will be fixed, and will be slightly shorter than the video EBP marker interval. Only available when EBP Cablelabs segmentation markers are selected. Partitions 1 and 2 will always follow the video interval.
            EbpLookaheadMs (integer) -- When set, enforces that Encoder Boundary Points do not come within the specified time interval of each other by looking ahead at input video. If another EBP is going to come in within the specified time interval, the current EBP is not emitted, and the segment is 'stretched' to the next marker. The lookahead value does not add latency to the system. The Live Event must be configured elsewhere to create sufficient latency to make the lookahead accurate.
            EbpPlacement (string) -- Controls placement of EBP on Audio PIDs. If set to videoAndAudioPids, EBP markers will be placed on the video PID and all audio PIDs. If set to videoPid, EBP markers will be placed on only the video PID.
            EcmPid (string) -- This field is unused and deprecated.
            EsRateInPes (string) -- Include or exclude the ES Rate field in the PES header.
            EtvPlatformPid (string) -- Packet Identifier (PID) for input source ETV Platform data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            EtvSignalPid (string) -- Packet Identifier (PID) for input source ETV Signal data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            FragmentTime (float) -- The length in seconds of each fragment. Only used with EBP markers.
            Klv (string) -- If set to passthrough, passes any KLV data from the input source to this output.
            KlvDataPids (string) -- Packet Identifier (PID) for input source KLV data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
            NullPacketBitrate (float) -- Value in bits per second of extra null packets to insert into the transport stream. This can be used if a downstream encryption system requires periodic null packets.
            PatInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000.
            PcrControl (string) -- When set to pcrEveryPesPacket, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream.
            PcrPeriod (integer) -- Maximum time in milliseconds between Program Clock Reference (PCRs) inserted into the transport stream.
            PcrPid (string) -- Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            PmtInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000.
            PmtPid (string) -- Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            ProgramNum (integer) -- The value of the program number field in the Program Map Table.
            RateMode (string) -- When vbr, does not insert null packets into transport stream to fill specified bitrate. The bitrate setting acts as the maximum bitrate when vbr is set.
            Scte27Pids (string) -- Packet Identifier (PID) for input source SCTE-27 data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
            Scte35Control (string) -- Optionally pass SCTE-35 signals from the input source to this output.
            Scte35Pid (string) -- Packet Identifier (PID) of the SCTE-35 stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            SegmentationMarkers (string) -- Inserts segmentation markers at each segmentationTime period. raiSegstart sets the Random Access Indicator bit in the adaptation field. raiAdapt sets the RAI bit and adds the current timecode in the private data bytes. psiSegstart inserts PAT and PMT tables at the start of segments. ebp adds Encoder Boundary Point information to the adaptation field as per OpenCable specification OC-SP-EBP-I01-130118. ebpLegacy adds Encoder Boundary Point information to the adaptation field using a legacy proprietary format.
            SegmentationStyle (string) -- The segmentation style parameter controls how segmentation markers are inserted into the transport stream. With avails, it is possible that segments may be truncated, which can influence where future segmentation markers are inserted. When a segmentation style of 'resetCadence' is selected and a segment is truncated due to an avail, we will reset the segmentation cadence. This means the subsequent segment will have a duration of $segmentationTime seconds. When a segmentation style of 'maintainCadence' is selected and a segment is truncated due to an avail, we will not reset the segmentation cadence. This means the subsequent segment will likely be truncated as well. However, all segments after that will have a duration of $segmentationTime seconds. Note that EBP lookahead is a slight exception to this rule.
            SegmentationTime (float) -- The length in seconds of each segment. Required unless markers is set to None_.
            TimedMetadataBehavior (string) -- When set to passthrough, timed metadata will be passed through from input to output.
            TimedMetadataPid (string) -- Packet Identifier (PID) of the timed metadata stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            TransportStreamId (integer) -- The value of the transport stream ID field in the Program Map Table.
            VideoPid (string) -- Packet Identifier (PID) of the elementary video stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            
            Extension (string) -- Output file extension. If excluded, this will be auto-selected from the container type.
            NameModifier (string) -- String concatenated to the end of the destination filename. Required for multiple outputs of the same type.
            HlsOutputSettings (dict) -- Placeholder documentation for HlsOutputSettings
            HlsSettings (dict) -- [REQUIRED] Settings regarding the underlying stream. These settings are different for audio-only outputs.
            AudioOnlyHlsSettings (dict) -- Placeholder documentation for AudioOnlyHlsSettings
            AudioGroupId (string) -- Specifies the group to which the audio Rendition belongs.
            AudioOnlyImage (dict) -- For use with an audio only Stream. Must be a .jpg or .png file. If given, this image will be used as the cover-art for the audio only output. Ideally, it should be formatted for an iPhone screen for two reasons. The iPhone does not resize the image, it crops a centered image on the top/bottom and left/right. Additionally, this image file gets saved bit-for-bit into every 10-second segment file, so will increase bandwidth by {image file size} * {segment count} * {user count.}.
            PasswordParam (string) -- key used to extract the password from EC2 Parameter store
            Uri (string) -- [REQUIRED] Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: 'rtmp://fmsserver/live'.
            Username (string) -- Documentation update needed
            AudioTrackType (string) -- Four types of audio-only tracks are supported: Audio-Only Variant Stream The client can play back this audio-only stream instead of video in low-bandwidth scenarios. Represented as an EXT-X-STREAM-INF in the HLS manifest. Alternate Audio, Auto Select, Default Alternate rendition that the client should try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=YES, AUTOSELECT=YES Alternate Audio, Auto Select, Not Default Alternate rendition that the client may try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=YES Alternate Audio, not Auto Select Alternate rendition that the client will not try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=NO
            StandardHlsSettings (dict) -- Placeholder documentation for StandardHlsSettings
            AudioRenditionSets (string) -- List all the audio groups that are used with the video output stream. Input all the audio GROUP-IDs that are associated to the video, separate by ','.
            M3u8Settings (dict) -- [REQUIRED] Settings information for the .m3u8 container
            AudioFramesPerPes (integer) -- The number of audio frames to insert for each PES packet.
            AudioPids (string) -- Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values.
            EcmPid (string) -- This parameter is unused and deprecated.
            PatInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream. A value of '0' writes out the PMT once per segment file.
            PcrControl (string) -- When set to pcrEveryPesPacket, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream.
            PcrPeriod (integer) -- Maximum time in milliseconds between Program Clock References (PCRs) inserted into the transport stream.
            PcrPid (string) -- Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID. Can be entered as a decimal or hexadecimal value.
            PmtInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream. A value of '0' writes out the PMT once per segment file.
            PmtPid (string) -- Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream. Can be entered as a decimal or hexadecimal value.
            ProgramNum (integer) -- The value of the program number field in the Program Map Table.
            Scte35Behavior (string) -- If set to passthrough, passes any SCTE-35 signals from the input source to this output.
            Scte35Pid (string) -- Packet Identifier (PID) of the SCTE-35 stream in the transport stream. Can be entered as a decimal or hexadecimal value.
            TimedMetadataBehavior (string) -- When set to passthrough, timed metadata is passed through from input to output.
            TimedMetadataPid (string) -- Packet Identifier (PID) of the timed metadata stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            TransportStreamId (integer) -- The value of the transport stream ID field in the Program Map Table.
            VideoPid (string) -- Packet Identifier (PID) of the elementary video stream in the transport stream. Can be entered as a decimal or hexadecimal value.
            
            NameModifier (string) -- String concatenated to the end of the destination filename. Accepts 'Format Identifiers':#formatIdentifierParameters.
            SegmentModifier (string) -- String concatenated to end of segment filenames.
            MsSmoothOutputSettings (dict) -- Placeholder documentation for MsSmoothOutputSettings
            NameModifier (string) -- String concatenated to the end of the destination filename. Required for multiple outputs of the same type.
            RtmpOutputSettings (dict) -- Placeholder documentation for RtmpOutputSettings
            CertificateMode (string) -- If set to verifyAuthenticity, verify the tls certificate chain to a trusted Certificate Authority (CA). This will cause rtmps outputs with self-signed certificates to fail.
            ConnectionRetryInterval (integer) -- Number of seconds to wait before retrying a connection to the Flash Media server if the connection is lost.
            Destination (dict) -- [REQUIRED] The RTMP endpoint excluding the stream name (eg. rtmp://host/appname). For connection to Akamai, a username and password must be supplied. URI fields accept format identifiers.
            DestinationRefId (string) -- Placeholder documentation for __string
            NumRetries (integer) -- Number of retry attempts.
            UdpOutputSettings (dict) -- Placeholder documentation for UdpOutputSettings
            BufferMsec (integer) -- UDP output buffering in milliseconds. Larger values increase latency through the transcoder but simultaneously assist the transcoder in maintaining a constant, low-jitter UDP/RTP output while accommodating clock recovery, input switching, input disruptions, picture reordering, etc.
            ContainerSettings (dict) -- [REQUIRED] Placeholder documentation for UdpContainerSettings
            M2tsSettings (dict) -- Placeholder documentation for M2tsSettings
            AbsentInputAudioBehavior (string) -- When set to drop, output audio streams will be removed from the program if the selected input audio stream is removed from the input. This allows the output audio configuration to dynamically change based on input configuration. If this is set to encodeSilence, all output audio streams will output encoded silence when not connected to an active input stream.
            Arib (string) -- When set to enabled, uses ARIB-compliant field muxing and removes video descriptor.
            AribCaptionsPid (string) -- Packet Identifier (PID) for ARIB Captions in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            AribCaptionsPidControl (string) -- If set to auto, pid number used for ARIB Captions will be auto-selected from unused pids. If set to useConfigured, ARIB Captions will be on the configured pid number.
            AudioBufferModel (string) -- When set to dvb, uses DVB buffer model for Dolby Digital audio. When set to atsc, the ATSC model is used.
            AudioFramesPerPes (integer) -- The number of audio frames to insert for each PES packet.
            AudioPids (string) -- Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
            AudioStreamType (string) -- When set to atsc, uses stream type = 0x81 for AC3 and stream type = 0x87 for EAC3. When set to dvb, uses stream type = 0x06.
            Bitrate (integer) -- The output bitrate of the transport stream in bits per second. Setting to 0 lets the muxer automatically determine the appropriate bitrate.
            BufferModel (string) -- If set to multiplex, use multiplex buffer model for accurate interleaving. Setting to bufferModel to none can lead to lower latency, but low-memory devices may not be able to play back the stream without interruptions.
            CcDescriptor (string) -- When set to enabled, generates captionServiceDescriptor in PMT.
            DvbNitSettings (dict) -- Inserts DVB Network Information Table (NIT) at the specified table repetition interval.
            NetworkId (integer) -- [REQUIRED] The numeric value placed in the Network Information Table (NIT).
            NetworkName (string) -- [REQUIRED] The network name text placed in the networkNameDescriptor inside the Network Information Table. Maximum length is 256 characters.
            RepInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream.
            DvbSdtSettings (dict) -- Inserts DVB Service Description Table (SDT) at the specified table repetition interval.
            OutputSdt (string) -- Selects method of inserting SDT information into output stream. The sdtFollow setting copies SDT information from input stream to output stream. The sdtFollowIfPresent setting copies SDT information from input stream to output stream if SDT information is present in the input, otherwise it will fall back on the user-defined values. The sdtManual setting means user will enter the SDT information. The sdtNone setting means output stream will not contain SDT information.
            RepInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream.
            ServiceName (string) -- The service name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters.
            ServiceProviderName (string) -- The service provider name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters.
            DvbSubPids (string) -- Packet Identifier (PID) for input source DVB Subtitle data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
            DvbTdtSettings (dict) -- Inserts DVB Time and Date Table (TDT) at the specified table repetition interval.
            RepInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream.
            DvbTeletextPid (string) -- Packet Identifier (PID) for input source DVB Teletext data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            Ebif (string) -- If set to passthrough, passes any EBIF data from the input source to this output.
            EbpAudioInterval (string) -- When videoAndFixedIntervals is selected, audio EBP markers will be added to partitions 3 and 4. The interval between these additional markers will be fixed, and will be slightly shorter than the video EBP marker interval. Only available when EBP Cablelabs segmentation markers are selected. Partitions 1 and 2 will always follow the video interval.
            EbpLookaheadMs (integer) -- When set, enforces that Encoder Boundary Points do not come within the specified time interval of each other by looking ahead at input video. If another EBP is going to come in within the specified time interval, the current EBP is not emitted, and the segment is 'stretched' to the next marker. The lookahead value does not add latency to the system. The Live Event must be configured elsewhere to create sufficient latency to make the lookahead accurate.
            EbpPlacement (string) -- Controls placement of EBP on Audio PIDs. If set to videoAndAudioPids, EBP markers will be placed on the video PID and all audio PIDs. If set to videoPid, EBP markers will be placed on only the video PID.
            EcmPid (string) -- This field is unused and deprecated.
            EsRateInPes (string) -- Include or exclude the ES Rate field in the PES header.
            EtvPlatformPid (string) -- Packet Identifier (PID) for input source ETV Platform data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            EtvSignalPid (string) -- Packet Identifier (PID) for input source ETV Signal data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            FragmentTime (float) -- The length in seconds of each fragment. Only used with EBP markers.
            Klv (string) -- If set to passthrough, passes any KLV data from the input source to this output.
            KlvDataPids (string) -- Packet Identifier (PID) for input source KLV data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
            NullPacketBitrate (float) -- Value in bits per second of extra null packets to insert into the transport stream. This can be used if a downstream encryption system requires periodic null packets.
            PatInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000.
            PcrControl (string) -- When set to pcrEveryPesPacket, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream.
            PcrPeriod (integer) -- Maximum time in milliseconds between Program Clock Reference (PCRs) inserted into the transport stream.
            PcrPid (string) -- Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            PmtInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000.
            PmtPid (string) -- Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            ProgramNum (integer) -- The value of the program number field in the Program Map Table.
            RateMode (string) -- When vbr, does not insert null packets into transport stream to fill specified bitrate. The bitrate setting acts as the maximum bitrate when vbr is set.
            Scte27Pids (string) -- Packet Identifier (PID) for input source SCTE-27 data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
            Scte35Control (string) -- Optionally pass SCTE-35 signals from the input source to this output.
            Scte35Pid (string) -- Packet Identifier (PID) of the SCTE-35 stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            SegmentationMarkers (string) -- Inserts segmentation markers at each segmentationTime period. raiSegstart sets the Random Access Indicator bit in the adaptation field. raiAdapt sets the RAI bit and adds the current timecode in the private data bytes. psiSegstart inserts PAT and PMT tables at the start of segments. ebp adds Encoder Boundary Point information to the adaptation field as per OpenCable specification OC-SP-EBP-I01-130118. ebpLegacy adds Encoder Boundary Point information to the adaptation field using a legacy proprietary format.
            SegmentationStyle (string) -- The segmentation style parameter controls how segmentation markers are inserted into the transport stream. With avails, it is possible that segments may be truncated, which can influence where future segmentation markers are inserted. When a segmentation style of 'resetCadence' is selected and a segment is truncated due to an avail, we will reset the segmentation cadence. This means the subsequent segment will have a duration of $segmentationTime seconds. When a segmentation style of 'maintainCadence' is selected and a segment is truncated due to an avail, we will not reset the segmentation cadence. This means the subsequent segment will likely be truncated as well. However, all segments after that will have a duration of $segmentationTime seconds. Note that EBP lookahead is a slight exception to this rule.
            SegmentationTime (float) -- The length in seconds of each segment. Required unless markers is set to None_.
            TimedMetadataBehavior (string) -- When set to passthrough, timed metadata will be passed through from input to output.
            TimedMetadataPid (string) -- Packet Identifier (PID) of the timed metadata stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            TransportStreamId (integer) -- The value of the transport stream ID field in the Program Map Table.
            VideoPid (string) -- Packet Identifier (PID) of the elementary video stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
            
            Destination (dict) -- [REQUIRED] Destination address and port number for RTP or UDP packets. Can be unicast or multicast RTP or UDP (eg. rtp://239.10.10.10:5001 or udp://10.100.100.100:5002).
            DestinationRefId (string) -- Placeholder documentation for __string
            FecOutputSettings (dict) -- Settings for enabling and adjusting Forward Error Correction on UDP outputs.
            ColumnDepth (integer) -- Parameter D from SMPTE 2022-1. The height of the FEC protection matrix. The number of transport stream packets per column error correction packet. Must be between 4 and 20, inclusive.
            IncludeFec (string) -- Enables column only or column and row based FEC
            RowLength (integer) -- Parameter L from SMPTE 2022-1. The width of the FEC protection matrix. Must be between 1 and 20, inclusive. If only Column FEC is used, then larger values increase robustness. If Row FEC is used, then this is the number of transport stream packets per row error correction packet, and the value must be between 4 and 20, inclusive, if includeFec is columnAndRow. If includeFec is column, this value must be 1 to 20, inclusive.
            
            VideoDescriptionName (string) -- The name of the VideoDescription used as the source for this output.
            
            
            TimecodeConfig (dict) -- [REQUIRED] Contains settings used to acquire and adjust timecode information from inputs.
            Source (string) -- [REQUIRED] Identifies the source for the timecode that will be associated with the events outputs. -Embedded (embedded): Initialize the output timecode with timecode from the the source. If no embedded timecode is detected in the source, the system falls back to using 'Start at 0' (zerobased). -System Clock (systemclock): Use the UTC time. -Start at 0 (zerobased): The time of the first frame of the event will be 00:00:00:00.
            SyncThreshold (integer) -- Threshold in frames beyond which output timecode is resynchronized to the input timecode. Discrepancies below this threshold are permitted to avoid unnecessary discontinuities in the output timecode. No timecode sync when this is not specified.
            VideoDescriptions (list) -- [REQUIRED] Placeholder documentation for __listOfVideoDescription
            (dict) -- Video settings for this stream.
            CodecSettings (dict) -- Video codec settings.
            H264Settings (dict) -- Placeholder documentation for H264Settings
            AdaptiveQuantization (string) -- Adaptive quantization. Allows intra-frame quantizers to vary to improve visual quality.
            AfdSignaling (string) -- Indicates that AFD values will be written into the output stream. If afdSignaling is 'auto', the system will try to preserve the input AFD value (in cases where multiple AFD values are valid). If set to 'fixed', the AFD value will be the value configured in the fixedAfd parameter.
            Bitrate (integer) -- Average bitrate in bits/second. Required when the rate control mode is VBR or CBR. Not used for QVBR. In an MS Smooth output group, each output must have a unique value when its bitrate is rounded down to the nearest multiple of 1000.
            BufFillPct (integer) -- Percentage of the buffer that should initially be filled (HRD buffer model).
            BufSize (integer) -- Size of buffer (HRD buffer model) in bits/second.
            ColorMetadata (string) -- Includes colorspace metadata in the output.
            EntropyEncoding (string) -- Entropy encoding mode. Use cabac (must be in Main or High profile) or cavlc.
            FixedAfd (string) -- Four bit AFD value to write on all frames of video in the output stream. Only valid when afdSignaling is set to 'Fixed'.
            FlickerAq (string) -- If set to enabled, adjust quantization within each frame to reduce flicker or 'pop' on I-frames.
            FramerateControl (string) -- This field indicates how the output video frame rate is specified. If 'specified' is selected then the output video frame rate is determined by framerateNumerator and framerateDenominator, else if 'initializeFromSource' is selected then the output video frame rate will be set equal to the input video frame rate of the first input.
            FramerateDenominator (integer) -- Framerate denominator.
            FramerateNumerator (integer) -- Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976 fps.
            GopBReference (string) -- Documentation update needed
            GopClosedCadence (integer) -- Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting.
            GopNumBFrames (integer) -- Number of B-frames between reference frames.
            GopSize (float) -- GOP size (keyframe interval) in units of either frames or seconds per gopSizeUnits. Must be greater than zero.
            GopSizeUnits (string) -- Indicates if the gopSize is specified in frames or seconds. If seconds the system will convert the gopSize into a frame count at run time.
            Level (string) -- H.264 Level.
            LookAheadRateControl (string) -- Amount of lookahead. A value of low can decrease latency and memory usage, while high can produce better quality for certain content.
            MaxBitrate (integer) -- For QVBR: See the tooltip for Quality level For VBR: Set the maximum bitrate in order to accommodate expected spikes in the complexity of the video.
            MinIInterval (integer) -- Only meaningful if sceneChangeDetect is set to enabled. Enforces separation between repeated (cadence) I-frames and I-frames inserted by Scene Change Detection. If a scene change I-frame is within I-interval frames of a cadence I-frame, the GOP is shrunk and/or stretched to the scene change I-frame. GOP stretch requires enabling lookahead as well as setting I-interval. The normal cadence resumes for the next GOP. Note: Maximum GOP stretch = GOP size + Min-I-interval - 1
            NumRefFrames (integer) -- Number of reference frames to use. The encoder may use more than requested if using B-frames and/or interlaced encoding.
            ParControl (string) -- This field indicates how the output pixel aspect ratio is specified. If 'specified' is selected then the output video pixel aspect ratio is determined by parNumerator and parDenominator, else if 'initializeFromSource' is selected then the output pixsel aspect ratio will be set equal to the input video pixel aspect ratio of the first input.
            ParDenominator (integer) -- Pixel Aspect Ratio denominator.
            ParNumerator (integer) -- Pixel Aspect Ratio numerator.
            Profile (string) -- H.264 Profile.
            QvbrQualityLevel (integer) -- Controls the target quality for the video encode. Applies only when the rate control mode is QVBR. Set values for the QVBR quality level field and Max bitrate field that suit your most important viewing devices. Recommended values are: - Primary screen: Quality level: 8 to 10. Max bitrate: 4M - PC or tablet: Quality level: 7. Max bitrate: 1.5M to 3M - Smartphone: Quality level: 6. Max bitrate: 1M to 1.5M
            RateControlMode (string) -- Rate control mode. QVBR: Quality will match the specified quality level except when it is constrained by the maximum bitrate. Recommended if you or your viewers pay for bandwidth. VBR: Quality and bitrate vary, depending on the video complexity. Recommended instead of QVBR if you want to maintain a specific average bitrate over the duration of the channel. CBR: Quality varies, depending on the video complexity. Recommended only if you distribute your assets to devices that cannot handle variable bitrates.
            ScanType (string) -- Sets the scan type of the output to progressive or top-field-first interlaced.
            SceneChangeDetect (string) -- Scene change detection. - On: inserts I-frames when scene change is detected. - Off: does not force an I-frame when scene change is detected.
            Slices (integer) -- Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures. This field is optional; when no value is specified the encoder will choose the number of slices based on encode resolution.
            Softness (integer) -- Softness. Selects quantizer matrix, larger values reduce high-frequency content in the encoded image.
            SpatialAq (string) -- If set to enabled, adjust quantization within each frame based on spatial variation of content complexity.
            SubgopLength (string) -- If set to fixed, use gopNumBFrames B-frames per sub-GOP. If set to dynamic, optimize the number of B-frames used for each sub-GOP to improve visual quality.
            Syntax (string) -- Produces a bitstream compliant with SMPTE RP-2027.
            TemporalAq (string) -- If set to enabled, adjust quantization within each frame based on temporal variation of content complexity.
            TimecodeInsertion (string) -- Determines how timecodes should be inserted into the video elementary stream. - 'disabled': Do not include timecodes - 'picTimingSei': Pass through picture timing SEI messages from the source specified in Timecode Config
            
            Height (integer) -- Output video height (in pixels). Leave blank to use source video height. If left blank, width must also be unspecified.
            Name (string) -- [REQUIRED] The name of this VideoDescription. Outputs will use this name to uniquely identify this Description. Description names should be unique within this Live Event.
            RespondToAfd (string) -- Indicates how to respond to the AFD values in the input stream. Setting to 'respond' causes input video to be clipped, depending on AFD value, input display aspect ratio and output display aspect ratio.
            ScalingBehavior (string) -- When set to 'stretchToOutput', automatically configures the output position to stretch the video to the specified output resolution. This option will override any position value.
            Sharpness (integer) -- Changes the width of the anti-alias filter kernel used for scaling. Only applies if scaling is being performed and antiAlias is set to true. 0 is the softest setting, 100 the sharpest, and 50 recommended for most content.
            Width (integer) -- Output video width (in pixels). Leave out to use source video width. If left out, height must also be left out. Display aspect ratio is always preserved by letterboxing or pillarboxing when necessary.
            
            

    :type InputAttachments: list
    :param InputAttachments: Placeholder documentation for __listOfInputAttachment
            (dict) -- Placeholder documentation for InputAttachment
            InputAttachmentName (string) -- User-specified name for the attachment. This is required if the user wants to use this input in an input switch action.
            InputId (string) -- The ID of the input
            InputSettings (dict) -- Settings of an input (caption selector, etc.)
            AudioSelectors (list) -- Used to select the audio stream to decode for inputs that have multiple available.
            (dict) -- Placeholder documentation for AudioSelector
            Name (string) -- [REQUIRED] The name of this AudioSelector. AudioDescriptions will use this name to uniquely identify this Selector. Selector names should be unique per input.
            SelectorSettings (dict) -- The audio selector settings.
            AudioLanguageSelection (dict) -- Placeholder documentation for AudioLanguageSelection
            LanguageCode (string) -- [REQUIRED] Selects a specific three-letter language code from within an audio source.
            LanguageSelectionPolicy (string) -- When set to 'strict', the transport stream demux strictly identifies audio streams by their language descriptor. If a PMT update occurs such that an audio stream matching the initially selected language is no longer present then mute will be encoded until the language returns. If 'loose', then on a PMT update the demux will choose another audio stream in the program with the same stream type if it can't find one with the same language.
            AudioPidSelection (dict) -- Placeholder documentation for AudioPidSelection
            Pid (integer) -- [REQUIRED] Selects a specific PID from within a source.
            
            
            CaptionSelectors (list) -- Used to select the caption input to use for inputs that have multiple available.
            (dict) -- Output groups for this Live Event. Output groups contain information about where streams should be distributed.
            LanguageCode (string) -- When specified this field indicates the three letter language code of the caption track to extract from the source.
            Name (string) -- [REQUIRED] Name identifier for a caption selector. This name is used to associate this caption selector with one or more caption descriptions. Names must be unique within an event.
            SelectorSettings (dict) -- Caption selector settings.
            AribSourceSettings (dict) -- Placeholder documentation for AribSourceSettings
            DvbSubSourceSettings (dict) -- Placeholder documentation for DvbSubSourceSettings
            Pid (integer) -- When using DVB-Sub with Burn-In or SMPTE-TT, use this PID for the source content. Unused for DVB-Sub passthrough. All DVB-Sub content is passed through, regardless of selectors.
            EmbeddedSourceSettings (dict) -- Placeholder documentation for EmbeddedSourceSettings
            Convert608To708 (string) -- If upconvert, 608 data is both passed through via the '608 compatibility bytes' fields of the 708 wrapper as well as translated into 708. 708 data present in the source content will be discarded.
            Scte20Detection (string) -- Set to 'auto' to handle streams with intermittent and/or non-aligned SCTE-20 and Embedded captions.
            Source608ChannelNumber (integer) -- Specifies the 608/708 channel number within the video track from which to extract captions. Unused for passthrough.
            Source608TrackNumber (integer) -- This field is unused and deprecated.
            Scte20SourceSettings (dict) -- Placeholder documentation for Scte20SourceSettings
            Convert608To708 (string) -- If upconvert, 608 data is both passed through via the '608 compatibility bytes' fields of the 708 wrapper as well as translated into 708. 708 data present in the source content will be discarded.
            Source608ChannelNumber (integer) -- Specifies the 608/708 channel number within the video track from which to extract captions. Unused for passthrough.
            Scte27SourceSettings (dict) -- Placeholder documentation for Scte27SourceSettings
            Pid (integer) -- The pid field is used in conjunction with the caption selector languageCode field as follows: - Specify PID and Language: Extracts captions from that PID; the language is 'informational'. - Specify PID and omit Language: Extracts the specified PID. - Omit PID and specify Language: Extracts the specified language, whichever PID that happens to be. - Omit PID and omit Language: Valid only if source is DVB-Sub that is being passed through; all languages will be passed through.
            TeletextSourceSettings (dict) -- Placeholder documentation for TeletextSourceSettings
            PageNumber (string) -- Specifies the teletext page number within the data stream from which to extract captions. Range of 0x100 (256) to 0x8FF (2303). Unused for passthrough. Should be specified as a hexadecimal string with no '0x' prefix.
            
            
            DeblockFilter (string) -- Enable or disable the deblock filter when filtering.
            DenoiseFilter (string) -- Enable or disable the denoise filter when filtering.
            FilterStrength (integer) -- Adjusts the magnitude of filtering from 1 (minimal) to 5 (strongest).
            InputFilter (string) -- Turns on the filter for this input. MPEG-2 inputs have the deblocking filter enabled by default. 1) auto - filtering will be applied depending on input type/quality 2) disabled - no filtering will be applied to the input 3) forced - filtering will be applied regardless of input type
            NetworkInputSettings (dict) -- Input settings.
            HlsInputSettings (dict) -- Specifies HLS input settings when the uri is for a HLS manifest.
            Bandwidth (integer) -- When specified the HLS stream with the m3u8 BANDWIDTH that most closely matches this value will be chosen, otherwise the highest bandwidth stream in the m3u8 will be chosen. The bitrate is specified in bits per second, as in an HLS manifest.
            BufferSegments (integer) -- When specified, reading of the HLS input will begin this many buffer segments from the end (most recently written segment). When not specified, the HLS input will begin with the first segment specified in the m3u8.
            Retries (integer) -- The number of consecutive times that attempts to read a manifest or segment must fail before the input is considered unavailable.
            RetryInterval (integer) -- The number of seconds between retries when an attempt to read a manifest or segment fails.
            ServerValidation (string) -- Check HTTPS server certificates. When set to checkCryptographyOnly, cryptography in the certificate will be checked, but not the server's name. Certain subdomains (notably S3 buckets that use dots in the bucket name) do not strictly match the corresponding certificate's wildcard pattern and would otherwise cause the event to error. This setting is ignored for protocols that do not use https.
            SourceEndBehavior (string) -- Loop input if it is a file. This allows a file input to be streamed indefinitely.
            VideoSelector (dict) -- Informs which video elementary stream to decode for input types that have multiple available.
            ColorSpace (string) -- Specifies the colorspace of an input. This setting works in tandem with colorSpaceConversion to determine if any conversion will be performed.
            ColorSpaceUsage (string) -- Applies only if colorSpace is a value other than follow. This field controls how the value in the colorSpace field will be used. fallback means that when the input does include color space data, that data will be used, but when the input has no color space data, the value in colorSpace will be used. Choose fallback if your input is sometimes missing color space data, but when it does have color space data, that data is correct. force means to always use the value in colorSpace. Choose force if your input usually has no color space data or might have unreliable color space data.
            SelectorSettings (dict) -- The video selector settings.
            VideoSelectorPid (dict) -- Placeholder documentation for VideoSelectorPid
            Pid (integer) -- Selects a specific PID from within a video source.
            VideoSelectorProgramId (dict) -- Placeholder documentation for VideoSelectorProgramId
            ProgramId (integer) -- Selects a specific program from within a multi-program transport stream. If the program doesn't exist, the first program within the transport stream will be selected by default.
            
            
            

    :type InputSpecification: dict
    :param InputSpecification: Specification of input for this channel (max. bitrate, resolution, codec, etc.)
            Codec (string) -- Input codec
            MaximumBitrate (string) -- Maximum input bitrate, categorized coarsely
            Resolution (string) -- Input resolution, categorized coarsely
            

    :type LogLevel: string
    :param LogLevel: The log level to write to CloudWatch Logs.

    :type Name: string
    :param Name: The name of the channel.

    :type RoleArn: string
    :param RoleArn: An optional Amazon Resource Name (ARN) of the role to assume when running the Channel. If you do not specify this on an update call but the role was previously set that role will be removed.

    :rtype: dict
    :return: {
        'Channel': {
            'Arn': 'string',
            'Destinations': [
                {
                    'Id': 'string',
                    'Settings': [
                        {
                            'PasswordParam': 'string',
                            'StreamName': 'string',
                            'Url': 'string',
                            'Username': 'string'
                        },
                    ]
                },
            ],
            'EgressEndpoints': [
                {
                    'SourceIp': 'string'
                },
            ],
            'EncoderSettings': {
                'AudioDescriptions': [
                    {
                        'AudioNormalizationSettings': {
                            'Algorithm': 'ITU_1770_1'|'ITU_1770_2',
                            'AlgorithmControl': 'CORRECT_AUDIO',
                            'TargetLkfs': 123.0
                        },
                        'AudioSelectorName': 'string',
                        'AudioType': 'CLEAN_EFFECTS'|'HEARING_IMPAIRED'|'UNDEFINED'|'VISUAL_IMPAIRED_COMMENTARY',
                        'AudioTypeControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                        'CodecSettings': {
                            'AacSettings': {
                                'Bitrate': 123.0,
                                'CodingMode': 'AD_RECEIVER_MIX'|'CODING_MODE_1_0'|'CODING_MODE_1_1'|'CODING_MODE_2_0'|'CODING_MODE_5_1',
                                'InputType': 'BROADCASTER_MIXED_AD'|'NORMAL',
                                'Profile': 'HEV1'|'HEV2'|'LC',
                                'RateControlMode': 'CBR'|'VBR',
                                'RawFormat': 'LATM_LOAS'|'NONE',
                                'SampleRate': 123.0,
                                'Spec': 'MPEG2'|'MPEG4',
                                'VbrQuality': 'HIGH'|'LOW'|'MEDIUM_HIGH'|'MEDIUM_LOW'
                            },
                            'Ac3Settings': {
                                'Bitrate': 123.0,
                                'BitstreamMode': 'COMMENTARY'|'COMPLETE_MAIN'|'DIALOGUE'|'EMERGENCY'|'HEARING_IMPAIRED'|'MUSIC_AND_EFFECTS'|'VISUALLY_IMPAIRED'|'VOICE_OVER',
                                'CodingMode': 'CODING_MODE_1_0'|'CODING_MODE_1_1'|'CODING_MODE_2_0'|'CODING_MODE_3_2_LFE',
                                'Dialnorm': 123,
                                'DrcProfile': 'FILM_STANDARD'|'NONE',
                                'LfeFilter': 'DISABLED'|'ENABLED',
                                'MetadataControl': 'FOLLOW_INPUT'|'USE_CONFIGURED'
                            },
                            'Eac3Settings': {
                                'AttenuationControl': 'ATTENUATE_3_DB'|'NONE',
                                'Bitrate': 123.0,
                                'BitstreamMode': 'COMMENTARY'|'COMPLETE_MAIN'|'EMERGENCY'|'HEARING_IMPAIRED'|'VISUALLY_IMPAIRED',
                                'CodingMode': 'CODING_MODE_1_0'|'CODING_MODE_2_0'|'CODING_MODE_3_2',
                                'DcFilter': 'DISABLED'|'ENABLED',
                                'Dialnorm': 123,
                                'DrcLine': 'FILM_LIGHT'|'FILM_STANDARD'|'MUSIC_LIGHT'|'MUSIC_STANDARD'|'NONE'|'SPEECH',
                                'DrcRf': 'FILM_LIGHT'|'FILM_STANDARD'|'MUSIC_LIGHT'|'MUSIC_STANDARD'|'NONE'|'SPEECH',
                                'LfeControl': 'LFE'|'NO_LFE',
                                'LfeFilter': 'DISABLED'|'ENABLED',
                                'LoRoCenterMixLevel': 123.0,
                                'LoRoSurroundMixLevel': 123.0,
                                'LtRtCenterMixLevel': 123.0,
                                'LtRtSurroundMixLevel': 123.0,
                                'MetadataControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                                'PassthroughControl': 'NO_PASSTHROUGH'|'WHEN_POSSIBLE',
                                'PhaseControl': 'NO_SHIFT'|'SHIFT_90_DEGREES',
                                'StereoDownmix': 'DPL2'|'LO_RO'|'LT_RT'|'NOT_INDICATED',
                                'SurroundExMode': 'DISABLED'|'ENABLED'|'NOT_INDICATED',
                                'SurroundMode': 'DISABLED'|'ENABLED'|'NOT_INDICATED'
                            },
                            'Mp2Settings': {
                                'Bitrate': 123.0,
                                'CodingMode': 'CODING_MODE_1_0'|'CODING_MODE_2_0',
                                'SampleRate': 123.0
                            },
                            'PassThroughSettings': {}
                        },
                        'LanguageCode': 'string',
                        'LanguageCodeControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                        'Name': 'string',
                        'RemixSettings': {
                            'ChannelMappings': [
                                {
                                    'InputChannelLevels': [
                                        {
                                            'Gain': 123,
                                            'InputChannel': 123
                                        },
                                    ],
                                    'OutputChannel': 123
                                },
                            ],
                            'ChannelsIn': 123,
                            'ChannelsOut': 123
                        },
                        'StreamName': 'string'
                    },
                ],
                'AvailBlanking': {
                    'AvailBlankingImage': {
                        'PasswordParam': 'string',
                        'Uri': 'string',
                        'Username': 'string'
                    },
                    'State': 'DISABLED'|'ENABLED'
                },
                'AvailConfiguration': {
                    'AvailSettings': {
                        'Scte35SpliceInsert': {
                            'AdAvailOffset': 123,
                            'NoRegionalBlackoutFlag': 'FOLLOW'|'IGNORE',
                            'WebDeliveryAllowedFlag': 'FOLLOW'|'IGNORE'
                        },
                        'Scte35TimeSignalApos': {
                            'AdAvailOffset': 123,
                            'NoRegionalBlackoutFlag': 'FOLLOW'|'IGNORE',
                            'WebDeliveryAllowedFlag': 'FOLLOW'|'IGNORE'
                        }
                    }
                },
                'BlackoutSlate': {
                    'BlackoutSlateImage': {
                        'PasswordParam': 'string',
                        'Uri': 'string',
                        'Username': 'string'
                    },
                    'NetworkEndBlackout': 'DISABLED'|'ENABLED',
                    'NetworkEndBlackoutImage': {
                        'PasswordParam': 'string',
                        'Uri': 'string',
                        'Username': 'string'
                    },
                    'NetworkId': 'string',
                    'State': 'DISABLED'|'ENABLED'
                },
                'CaptionDescriptions': [
                    {
                        'CaptionSelectorName': 'string',
                        'DestinationSettings': {
                            'AribDestinationSettings': {},
                            'BurnInDestinationSettings': {
                                'Alignment': 'CENTERED'|'LEFT'|'SMART',
                                'BackgroundColor': 'BLACK'|'NONE'|'WHITE',
                                'BackgroundOpacity': 123,
                                'Font': {
                                    'PasswordParam': 'string',
                                    'Uri': 'string',
                                    'Username': 'string'
                                },
                                'FontColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                                'FontOpacity': 123,
                                'FontResolution': 123,
                                'FontSize': 'string',
                                'OutlineColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                                'OutlineSize': 123,
                                'ShadowColor': 'BLACK'|'NONE'|'WHITE',
                                'ShadowOpacity': 123,
                                'ShadowXOffset': 123,
                                'ShadowYOffset': 123,
                                'TeletextGridControl': 'FIXED'|'SCALED',
                                'XPosition': 123,
                                'YPosition': 123
                            },
                            'DvbSubDestinationSettings': {
                                'Alignment': 'CENTERED'|'LEFT'|'SMART',
                                'BackgroundColor': 'BLACK'|'NONE'|'WHITE',
                                'BackgroundOpacity': 123,
                                'Font': {
                                    'PasswordParam': 'string',
                                    'Uri': 'string',
                                    'Username': 'string'
                                },
                                'FontColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                                'FontOpacity': 123,
                                'FontResolution': 123,
                                'FontSize': 'string',
                                'OutlineColor': 'BLACK'|'BLUE'|'GREEN'|'RED'|'WHITE'|'YELLOW',
                                'OutlineSize': 123,
                                'ShadowColor': 'BLACK'|'NONE'|'WHITE',
                                'ShadowOpacity': 123,
                                'ShadowXOffset': 123,
                                'ShadowYOffset': 123,
                                'TeletextGridControl': 'FIXED'|'SCALED',
                                'XPosition': 123,
                                'YPosition': 123
                            },
                            'EmbeddedDestinationSettings': {},
                            'EmbeddedPlusScte20DestinationSettings': {},
                            'RtmpCaptionInfoDestinationSettings': {},
                            'Scte20PlusEmbeddedDestinationSettings': {},
                            'Scte27DestinationSettings': {},
                            'SmpteTtDestinationSettings': {},
                            'TeletextDestinationSettings': {},
                            'TtmlDestinationSettings': {
                                'StyleControl': 'PASSTHROUGH'|'USE_CONFIGURED'
                            },
                            'WebvttDestinationSettings': {}
                        },
                        'LanguageCode': 'string',
                        'LanguageDescription': 'string',
                        'Name': 'string'
                    },
                ],
                'GlobalConfiguration': {
                    'InitialAudioGain': 123,
                    'InputEndAction': 'NONE'|'SWITCH_AND_LOOP_INPUTS',
                    'InputLossBehavior': {
                        'BlackFrameMsec': 123,
                        'InputLossImageColor': 'string',
                        'InputLossImageSlate': {
                            'PasswordParam': 'string',
                            'Uri': 'string',
                            'Username': 'string'
                        },
                        'InputLossImageType': 'COLOR'|'SLATE',
                        'RepeatFrameMsec': 123
                    },
                    'OutputTimingSource': 'INPUT_CLOCK'|'SYSTEM_CLOCK',
                    'SupportLowFramerateInputs': 'DISABLED'|'ENABLED'
                },
                'OutputGroups': [
                    {
                        'Name': 'string',
                        'OutputGroupSettings': {
                            'ArchiveGroupSettings': {
                                'Destination': {
                                    'DestinationRefId': 'string'
                                },
                                'RolloverInterval': 123
                            },
                            'HlsGroupSettings': {
                                'AdMarkers': [
                                    'ADOBE'|'ELEMENTAL'|'ELEMENTAL_SCTE35',
                                ],
                                'BaseUrlContent': 'string',
                                'BaseUrlManifest': 'string',
                                'CaptionLanguageMappings': [
                                    {
                                        'CaptionChannel': 123,
                                        'LanguageCode': 'string',
                                        'LanguageDescription': 'string'
                                    },
                                ],
                                'CaptionLanguageSetting': 'INSERT'|'NONE'|'OMIT',
                                'ClientCache': 'DISABLED'|'ENABLED',
                                'CodecSpecification': 'RFC_4281'|'RFC_6381',
                                'ConstantIv': 'string',
                                'Destination': {
                                    'DestinationRefId': 'string'
                                },
                                'DirectoryStructure': 'SINGLE_DIRECTORY'|'SUBDIRECTORY_PER_STREAM',
                                'EncryptionType': 'AES128'|'SAMPLE_AES',
                                'HlsCdnSettings': {
                                    'HlsAkamaiSettings': {
                                        'ConnectionRetryInterval': 123,
                                        'FilecacheDuration': 123,
                                        'HttpTransferMode': 'CHUNKED'|'NON_CHUNKED',
                                        'NumRetries': 123,
                                        'RestartDelay': 123,
                                        'Salt': 'string',
                                        'Token': 'string'
                                    },
                                    'HlsBasicPutSettings': {
                                        'ConnectionRetryInterval': 123,
                                        'FilecacheDuration': 123,
                                        'NumRetries': 123,
                                        'RestartDelay': 123
                                    },
                                    'HlsMediaStoreSettings': {
                                        'ConnectionRetryInterval': 123,
                                        'FilecacheDuration': 123,
                                        'MediaStoreStorageClass': 'TEMPORAL',
                                        'NumRetries': 123,
                                        'RestartDelay': 123
                                    },
                                    'HlsWebdavSettings': {
                                        'ConnectionRetryInterval': 123,
                                        'FilecacheDuration': 123,
                                        'HttpTransferMode': 'CHUNKED'|'NON_CHUNKED',
                                        'NumRetries': 123,
                                        'RestartDelay': 123
                                    }
                                },
                                'IndexNSegments': 123,
                                'InputLossAction': 'EMIT_OUTPUT'|'PAUSE_OUTPUT',
                                'IvInManifest': 'EXCLUDE'|'INCLUDE',
                                'IvSource': 'EXPLICIT'|'FOLLOWS_SEGMENT_NUMBER',
                                'KeepSegments': 123,
                                'KeyFormat': 'string',
                                'KeyFormatVersions': 'string',
                                'KeyProviderSettings': {
                                    'StaticKeySettings': {
                                        'KeyProviderServer': {
                                            'PasswordParam': 'string',
                                            'Uri': 'string',
                                            'Username': 'string'
                                        },
                                        'StaticKeyValue': 'string'
                                    }
                                },
                                'ManifestCompression': 'GZIP'|'NONE',
                                'ManifestDurationFormat': 'FLOATING_POINT'|'INTEGER',
                                'MinSegmentLength': 123,
                                'Mode': 'LIVE'|'VOD',
                                'OutputSelection': 'MANIFESTS_AND_SEGMENTS'|'SEGMENTS_ONLY',
                                'ProgramDateTime': 'EXCLUDE'|'INCLUDE',
                                'ProgramDateTimePeriod': 123,
                                'RedundantManifest': 'DISABLED'|'ENABLED',
                                'SegmentLength': 123,
                                'SegmentationMode': 'USE_INPUT_SEGMENTATION'|'USE_SEGMENT_DURATION',
                                'SegmentsPerSubdirectory': 123,
                                'StreamInfResolution': 'EXCLUDE'|'INCLUDE',
                                'TimedMetadataId3Frame': 'NONE'|'PRIV'|'TDRL',
                                'TimedMetadataId3Period': 123,
                                'TimestampDeltaMilliseconds': 123,
                                'TsFileMode': 'SEGMENTED_FILES'|'SINGLE_FILE'
                            },
                            'MsSmoothGroupSettings': {
                                'AcquisitionPointId': 'string',
                                'AudioOnlyTimecodeControl': 'PASSTHROUGH'|'USE_CONFIGURED_CLOCK',
                                'CertificateMode': 'SELF_SIGNED'|'VERIFY_AUTHENTICITY',
                                'ConnectionRetryInterval': 123,
                                'Destination': {
                                    'DestinationRefId': 'string'
                                },
                                'EventId': 'string',
                                'EventIdMode': 'NO_EVENT_ID'|'USE_CONFIGURED'|'USE_TIMESTAMP',
                                'EventStopBehavior': 'NONE'|'SEND_EOS',
                                'FilecacheDuration': 123,
                                'FragmentLength': 123,
                                'InputLossAction': 'EMIT_OUTPUT'|'PAUSE_OUTPUT',
                                'NumRetries': 123,
                                'RestartDelay': 123,
                                'SegmentationMode': 'USE_INPUT_SEGMENTATION'|'USE_SEGMENT_DURATION',
                                'SendDelayMs': 123,
                                'SparseTrackType': 'NONE'|'SCTE_35',
                                'StreamManifestBehavior': 'DO_NOT_SEND'|'SEND',
                                'TimestampOffset': 'string',
                                'TimestampOffsetMode': 'USE_CONFIGURED_OFFSET'|'USE_EVENT_START_DATE'
                            },
                            'RtmpGroupSettings': {
                                'AuthenticationScheme': 'AKAMAI'|'COMMON',
                                'CacheFullBehavior': 'DISCONNECT_IMMEDIATELY'|'WAIT_FOR_SERVER',
                                'CacheLength': 123,
                                'CaptionData': 'ALL'|'FIELD1_608'|'FIELD1_AND_FIELD2_608',
                                'InputLossAction': 'EMIT_OUTPUT'|'PAUSE_OUTPUT',
                                'RestartDelay': 123
                            },
                            'UdpGroupSettings': {
                                'InputLossAction': 'DROP_PROGRAM'|'DROP_TS'|'EMIT_PROGRAM',
                                'TimedMetadataId3Frame': 'NONE'|'PRIV'|'TDRL',
                                'TimedMetadataId3Period': 123
                            }
                        },
                        'Outputs': [
                            {
                                'AudioDescriptionNames': [
                                    'string',
                                ],
                                'CaptionDescriptionNames': [
                                    'string',
                                ],
                                'OutputName': 'string',
                                'OutputSettings': {
                                    'ArchiveOutputSettings': {
                                        'ContainerSettings': {
                                            'M2tsSettings': {
                                                'AbsentInputAudioBehavior': 'DROP'|'ENCODE_SILENCE',
                                                'Arib': 'DISABLED'|'ENABLED',
                                                'AribCaptionsPid': 'string',
                                                'AribCaptionsPidControl': 'AUTO'|'USE_CONFIGURED',
                                                'AudioBufferModel': 'ATSC'|'DVB',
                                                'AudioFramesPerPes': 123,
                                                'AudioPids': 'string',
                                                'AudioStreamType': 'ATSC'|'DVB',
                                                'Bitrate': 123,
                                                'BufferModel': 'MULTIPLEX'|'NONE',
                                                'CcDescriptor': 'DISABLED'|'ENABLED',
                                                'DvbNitSettings': {
                                                    'NetworkId': 123,
                                                    'NetworkName': 'string',
                                                    'RepInterval': 123
                                                },
                                                'DvbSdtSettings': {
                                                    'OutputSdt': 'SDT_FOLLOW'|'SDT_FOLLOW_IF_PRESENT'|'SDT_MANUAL'|'SDT_NONE',
                                                    'RepInterval': 123,
                                                    'ServiceName': 'string',
                                                    'ServiceProviderName': 'string'
                                                },
                                                'DvbSubPids': 'string',
                                                'DvbTdtSettings': {
                                                    'RepInterval': 123
                                                },
                                                'DvbTeletextPid': 'string',
                                                'Ebif': 'NONE'|'PASSTHROUGH',
                                                'EbpAudioInterval': 'VIDEO_AND_FIXED_INTERVALS'|'VIDEO_INTERVAL',
                                                'EbpLookaheadMs': 123,
                                                'EbpPlacement': 'VIDEO_AND_AUDIO_PIDS'|'VIDEO_PID',
                                                'EcmPid': 'string',
                                                'EsRateInPes': 'EXCLUDE'|'INCLUDE',
                                                'EtvPlatformPid': 'string',
                                                'EtvSignalPid': 'string',
                                                'FragmentTime': 123.0,
                                                'Klv': 'NONE'|'PASSTHROUGH',
                                                'KlvDataPids': 'string',
                                                'NullPacketBitrate': 123.0,
                                                'PatInterval': 123,
                                                'PcrControl': 'CONFIGURED_PCR_PERIOD'|'PCR_EVERY_PES_PACKET',
                                                'PcrPeriod': 123,
                                                'PcrPid': 'string',
                                                'PmtInterval': 123,
                                                'PmtPid': 'string',
                                                'ProgramNum': 123,
                                                'RateMode': 'CBR'|'VBR',
                                                'Scte27Pids': 'string',
                                                'Scte35Control': 'NONE'|'PASSTHROUGH',
                                                'Scte35Pid': 'string',
                                                'SegmentationMarkers': 'EBP'|'EBP_LEGACY'|'NONE'|'PSI_SEGSTART'|'RAI_ADAPT'|'RAI_SEGSTART',
                                                'SegmentationStyle': 'MAINTAIN_CADENCE'|'RESET_CADENCE',
                                                'SegmentationTime': 123.0,
                                                'TimedMetadataBehavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                                'TimedMetadataPid': 'string',
                                                'TransportStreamId': 123,
                                                'VideoPid': 'string'
                                            }
                                        },
                                        'Extension': 'string',
                                        'NameModifier': 'string'
                                    },
                                    'HlsOutputSettings': {
                                        'HlsSettings': {
                                            'AudioOnlyHlsSettings': {
                                                'AudioGroupId': 'string',
                                                'AudioOnlyImage': {
                                                    'PasswordParam': 'string',
                                                    'Uri': 'string',
                                                    'Username': 'string'
                                                },
                                                'AudioTrackType': 'ALTERNATE_AUDIO_AUTO_SELECT'|'ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT'|'ALTERNATE_AUDIO_NOT_AUTO_SELECT'|'AUDIO_ONLY_VARIANT_STREAM'
                                            },
                                            'StandardHlsSettings': {
                                                'AudioRenditionSets': 'string',
                                                'M3u8Settings': {
                                                    'AudioFramesPerPes': 123,
                                                    'AudioPids': 'string',
                                                    'EcmPid': 'string',
                                                    'PatInterval': 123,
                                                    'PcrControl': 'CONFIGURED_PCR_PERIOD'|'PCR_EVERY_PES_PACKET',
                                                    'PcrPeriod': 123,
                                                    'PcrPid': 'string',
                                                    'PmtInterval': 123,
                                                    'PmtPid': 'string',
                                                    'ProgramNum': 123,
                                                    'Scte35Behavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                                    'Scte35Pid': 'string',
                                                    'TimedMetadataBehavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                                    'TimedMetadataPid': 'string',
                                                    'TransportStreamId': 123,
                                                    'VideoPid': 'string'
                                                }
                                            }
                                        },
                                        'NameModifier': 'string',
                                        'SegmentModifier': 'string'
                                    },
                                    'MsSmoothOutputSettings': {
                                        'NameModifier': 'string'
                                    },
                                    'RtmpOutputSettings': {
                                        'CertificateMode': 'SELF_SIGNED'|'VERIFY_AUTHENTICITY',
                                        'ConnectionRetryInterval': 123,
                                        'Destination': {
                                            'DestinationRefId': 'string'
                                        },
                                        'NumRetries': 123
                                    },
                                    'UdpOutputSettings': {
                                        'BufferMsec': 123,
                                        'ContainerSettings': {
                                            'M2tsSettings': {
                                                'AbsentInputAudioBehavior': 'DROP'|'ENCODE_SILENCE',
                                                'Arib': 'DISABLED'|'ENABLED',
                                                'AribCaptionsPid': 'string',
                                                'AribCaptionsPidControl': 'AUTO'|'USE_CONFIGURED',
                                                'AudioBufferModel': 'ATSC'|'DVB',
                                                'AudioFramesPerPes': 123,
                                                'AudioPids': 'string',
                                                'AudioStreamType': 'ATSC'|'DVB',
                                                'Bitrate': 123,
                                                'BufferModel': 'MULTIPLEX'|'NONE',
                                                'CcDescriptor': 'DISABLED'|'ENABLED',
                                                'DvbNitSettings': {
                                                    'NetworkId': 123,
                                                    'NetworkName': 'string',
                                                    'RepInterval': 123
                                                },
                                                'DvbSdtSettings': {
                                                    'OutputSdt': 'SDT_FOLLOW'|'SDT_FOLLOW_IF_PRESENT'|'SDT_MANUAL'|'SDT_NONE',
                                                    'RepInterval': 123,
                                                    'ServiceName': 'string',
                                                    'ServiceProviderName': 'string'
                                                },
                                                'DvbSubPids': 'string',
                                                'DvbTdtSettings': {
                                                    'RepInterval': 123
                                                },
                                                'DvbTeletextPid': 'string',
                                                'Ebif': 'NONE'|'PASSTHROUGH',
                                                'EbpAudioInterval': 'VIDEO_AND_FIXED_INTERVALS'|'VIDEO_INTERVAL',
                                                'EbpLookaheadMs': 123,
                                                'EbpPlacement': 'VIDEO_AND_AUDIO_PIDS'|'VIDEO_PID',
                                                'EcmPid': 'string',
                                                'EsRateInPes': 'EXCLUDE'|'INCLUDE',
                                                'EtvPlatformPid': 'string',
                                                'EtvSignalPid': 'string',
                                                'FragmentTime': 123.0,
                                                'Klv': 'NONE'|'PASSTHROUGH',
                                                'KlvDataPids': 'string',
                                                'NullPacketBitrate': 123.0,
                                                'PatInterval': 123,
                                                'PcrControl': 'CONFIGURED_PCR_PERIOD'|'PCR_EVERY_PES_PACKET',
                                                'PcrPeriod': 123,
                                                'PcrPid': 'string',
                                                'PmtInterval': 123,
                                                'PmtPid': 'string',
                                                'ProgramNum': 123,
                                                'RateMode': 'CBR'|'VBR',
                                                'Scte27Pids': 'string',
                                                'Scte35Control': 'NONE'|'PASSTHROUGH',
                                                'Scte35Pid': 'string',
                                                'SegmentationMarkers': 'EBP'|'EBP_LEGACY'|'NONE'|'PSI_SEGSTART'|'RAI_ADAPT'|'RAI_SEGSTART',
                                                'SegmentationStyle': 'MAINTAIN_CADENCE'|'RESET_CADENCE',
                                                'SegmentationTime': 123.0,
                                                'TimedMetadataBehavior': 'NO_PASSTHROUGH'|'PASSTHROUGH',
                                                'TimedMetadataPid': 'string',
                                                'TransportStreamId': 123,
                                                'VideoPid': 'string'
                                            }
                                        },
                                        'Destination': {
                                            'DestinationRefId': 'string'
                                        },
                                        'FecOutputSettings': {
                                            'ColumnDepth': 123,
                                            'IncludeFec': 'COLUMN'|'COLUMN_AND_ROW',
                                            'RowLength': 123
                                        }
                                    }
                                },
                                'VideoDescriptionName': 'string'
                            },
                        ]
                    },
                ],
                'TimecodeConfig': {
                    'Source': 'EMBEDDED'|'SYSTEMCLOCK'|'ZEROBASED',
                    'SyncThreshold': 123
                },
                'VideoDescriptions': [
                    {
                        'CodecSettings': {
                            'H264Settings': {
                                'AdaptiveQuantization': 'HIGH'|'HIGHER'|'LOW'|'MAX'|'MEDIUM'|'OFF',
                                'AfdSignaling': 'AUTO'|'FIXED'|'NONE',
                                'Bitrate': 123,
                                'BufFillPct': 123,
                                'BufSize': 123,
                                'ColorMetadata': 'IGNORE'|'INSERT',
                                'EntropyEncoding': 'CABAC'|'CAVLC',
                                'FixedAfd': 'AFD_0000'|'AFD_0010'|'AFD_0011'|'AFD_0100'|'AFD_1000'|'AFD_1001'|'AFD_1010'|'AFD_1011'|'AFD_1101'|'AFD_1110'|'AFD_1111',
                                'FlickerAq': 'DISABLED'|'ENABLED',
                                'FramerateControl': 'INITIALIZE_FROM_SOURCE'|'SPECIFIED',
                                'FramerateDenominator': 123,
                                'FramerateNumerator': 123,
                                'GopBReference': 'DISABLED'|'ENABLED',
                                'GopClosedCadence': 123,
                                'GopNumBFrames': 123,
                                'GopSize': 123.0,
                                'GopSizeUnits': 'FRAMES'|'SECONDS',
                                'Level': 'H264_LEVEL_1'|'H264_LEVEL_1_1'|'H264_LEVEL_1_2'|'H264_LEVEL_1_3'|'H264_LEVEL_2'|'H264_LEVEL_2_1'|'H264_LEVEL_2_2'|'H264_LEVEL_3'|'H264_LEVEL_3_1'|'H264_LEVEL_3_2'|'H264_LEVEL_4'|'H264_LEVEL_4_1'|'H264_LEVEL_4_2'|'H264_LEVEL_5'|'H264_LEVEL_5_1'|'H264_LEVEL_5_2'|'H264_LEVEL_AUTO',
                                'LookAheadRateControl': 'HIGH'|'LOW'|'MEDIUM',
                                'MaxBitrate': 123,
                                'MinIInterval': 123,
                                'NumRefFrames': 123,
                                'ParControl': 'INITIALIZE_FROM_SOURCE'|'SPECIFIED',
                                'ParDenominator': 123,
                                'ParNumerator': 123,
                                'Profile': 'BASELINE'|'HIGH'|'HIGH_10BIT'|'HIGH_422'|'HIGH_422_10BIT'|'MAIN',
                                'QvbrQualityLevel': 123,
                                'RateControlMode': 'CBR'|'QVBR'|'VBR',
                                'ScanType': 'INTERLACED'|'PROGRESSIVE',
                                'SceneChangeDetect': 'DISABLED'|'ENABLED',
                                'Slices': 123,
                                'Softness': 123,
                                'SpatialAq': 'DISABLED'|'ENABLED',
                                'SubgopLength': 'DYNAMIC'|'FIXED',
                                'Syntax': 'DEFAULT'|'RP2027',
                                'TemporalAq': 'DISABLED'|'ENABLED',
                                'TimecodeInsertion': 'DISABLED'|'PIC_TIMING_SEI'
                            }
                        },
                        'Height': 123,
                        'Name': 'string',
                        'RespondToAfd': 'NONE'|'PASSTHROUGH'|'RESPOND',
                        'ScalingBehavior': 'DEFAULT'|'STRETCH_TO_OUTPUT',
                        'Sharpness': 123,
                        'Width': 123
                    },
                ]
            },
            'Id': 'string',
            'InputAttachments': [
                {
                    'InputAttachmentName': 'string',
                    'InputId': 'string',
                    'InputSettings': {
                        'AudioSelectors': [
                            {
                                'Name': 'string',
                                'SelectorSettings': {
                                    'AudioLanguageSelection': {
                                        'LanguageCode': 'string',
                                        'LanguageSelectionPolicy': 'LOOSE'|'STRICT'
                                    },
                                    'AudioPidSelection': {
                                        'Pid': 123
                                    }
                                }
                            },
                        ],
                        'CaptionSelectors': [
                            {
                                'LanguageCode': 'string',
                                'Name': 'string',
                                'SelectorSettings': {
                                    'AribSourceSettings': {},
                                    'DvbSubSourceSettings': {
                                        'Pid': 123
                                    },
                                    'EmbeddedSourceSettings': {
                                        'Convert608To708': 'DISABLED'|'UPCONVERT',
                                        'Scte20Detection': 'AUTO'|'OFF',
                                        'Source608ChannelNumber': 123,
                                        'Source608TrackNumber': 123
                                    },
                                    'Scte20SourceSettings': {
                                        'Convert608To708': 'DISABLED'|'UPCONVERT',
                                        'Source608ChannelNumber': 123
                                    },
                                    'Scte27SourceSettings': {
                                        'Pid': 123
                                    },
                                    'TeletextSourceSettings': {
                                        'PageNumber': 'string'
                                    }
                                }
                            },
                        ],
                        'DeblockFilter': 'DISABLED'|'ENABLED',
                        'DenoiseFilter': 'DISABLED'|'ENABLED',
                        'FilterStrength': 123,
                        'InputFilter': 'AUTO'|'DISABLED'|'FORCED',
                        'NetworkInputSettings': {
                            'HlsInputSettings': {
                                'Bandwidth': 123,
                                'BufferSegments': 123,
                                'Retries': 123,
                                'RetryInterval': 123
                            },
                            'ServerValidation': 'CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME'|'CHECK_CRYPTOGRAPHY_ONLY'
                        },
                        'SourceEndBehavior': 'CONTINUE'|'LOOP',
                        'VideoSelector': {
                            'ColorSpace': 'FOLLOW'|'REC_601'|'REC_709',
                            'ColorSpaceUsage': 'FALLBACK'|'FORCE',
                            'SelectorSettings': {
                                'VideoSelectorPid': {
                                    'Pid': 123
                                },
                                'VideoSelectorProgramId': {
                                    'ProgramId': 123
                                }
                            }
                        }
                    }
                },
            ],
            'InputSpecification': {
                'Codec': 'MPEG2'|'AVC'|'HEVC',
                'MaximumBitrate': 'MAX_10_MBPS'|'MAX_20_MBPS'|'MAX_50_MBPS',
                'Resolution': 'SD'|'HD'|'UHD'
            },
            'LogLevel': 'ERROR'|'WARNING'|'INFO'|'DEBUG'|'DISABLED',
            'Name': 'string',
            'PipelinesRunningCount': 123,
            'RoleArn': 'string',
            'State': 'CREATING'|'CREATE_FAILED'|'IDLE'|'STARTING'|'RUNNING'|'RECOVERING'|'STOPPING'|'DELETING'|'DELETED'
        }
    }
    
    
    :returns: 
    (dict) -- Channel is successfully updated.
    Channel (dict) -- Placeholder documentation for Channel
    Arn (string) -- The unique arn of the channel.
    Destinations (list) -- A list of destinations of the channel. For UDP outputs, there is one destination per output. For other types (HLS, for example), there is one destination per packager.
    (dict) -- Placeholder documentation for OutputDestination
    Id (string) -- User-specified id. This is used in an output group or an output.
    Settings (list) -- Destination settings for output; one for each redundant encoder.
    (dict) -- Placeholder documentation for OutputDestinationSettings
    PasswordParam (string) -- key used to extract the password from EC2 Parameter store
    StreamName (string) -- Stream name for RTMP destinations (URLs of type rtmp://)
    Url (string) -- A URL specifying a destination
    Username (string) -- username for destination
    
    
    
    
    
    
    
    
    EgressEndpoints (list) -- The endpoints where outgoing connections initiate from
    (dict) -- Placeholder documentation for ChannelEgressEndpoint
    SourceIp (string) -- Public IP of where a channel's output comes from
    
    
    
    
    EncoderSettings (dict) -- Placeholder documentation for EncoderSettings
    AudioDescriptions (list) -- Placeholder documentation for __listOfAudioDescription
    (dict) -- Placeholder documentation for AudioDescription
    AudioNormalizationSettings (dict) -- Advanced audio normalization settings.
    Algorithm (string) -- Audio normalization algorithm to use. itu17701 conforms to the CALM Act specification, itu17702 conforms to the EBU R-128 specification.
    AlgorithmControl (string) -- When set to correctAudio the output audio is corrected using the chosen algorithm. If set to measureOnly, the audio will be measured but not adjusted.
    TargetLkfs (float) -- Target LKFS(loudness) to adjust volume to. If no value is entered, a default value will be used according to the chosen algorithm. The CALM Act (1770-1) recommends a target of -24 LKFS. The EBU R-128 specification (1770-2) recommends a target of -23 LKFS.
    
    
    AudioSelectorName (string) -- The name of the AudioSelector used as the source for this AudioDescription.
    AudioType (string) -- Applies only if audioTypeControl is useConfigured. The values for audioType are defined in ISO-IEC 13818-1.
    AudioTypeControl (string) -- Determines how audio type is determined. followInput: If the input contains an ISO 639 audioType, then that value is passed through to the output. If the input contains no ISO 639 audioType, the value in Audio Type is included in the output. useConfigured: The value in Audio Type is included in the output. Note that this field and audioType are both ignored if inputType is broadcasterMixedAd.
    CodecSettings (dict) -- Audio codec settings.
    AacSettings (dict) -- Placeholder documentation for AacSettings
    Bitrate (float) -- Average bitrate in bits/second. Valid values depend on rate control mode and profile.
    CodingMode (string) -- Mono, Stereo, or 5.1 channel layout. Valid values depend on rate control mode and profile. The adReceiverMix setting receives a stereo description plus control track and emits a mono AAC encode of the description track, with control data emitted in the PES header as per ETSI TS 101 154 Annex E.
    InputType (string) -- Set to "broadcasterMixedAd" when input contains pre-mixed main audio + AD (narration) as a stereo pair. The Audio Type field (audioType) will be set to 3, which signals to downstream systems that this stream contains "broadcaster mixed AD". Note that the input received by the encoder must contain pre-mixed audio; the encoder does not perform the mixing. The values in audioTypeControl and audioType (in AudioDescription) are ignored when set to broadcasterMixedAd. Leave set to "normal" when input does not contain pre-mixed audio + AD.
    Profile (string) -- AAC Profile.
    RateControlMode (string) -- Rate Control Mode.
    RawFormat (string) -- Sets LATM / LOAS AAC output for raw containers.
    SampleRate (float) -- Sample rate in Hz. Valid values depend on rate control mode and profile.
    Spec (string) -- Use MPEG-2 AAC audio instead of MPEG-4 AAC audio for raw or MPEG-2 Transport Stream containers.
    VbrQuality (string) -- VBR Quality Level - Only used if rateControlMode is VBR.
    
    
    Ac3Settings (dict) -- Placeholder documentation for Ac3Settings
    Bitrate (float) -- Average bitrate in bits/second. Valid bitrates depend on the coding mode.
    BitstreamMode (string) -- Specifies the bitstream mode (bsmod) for the emitted AC-3 stream. See ATSC A/52-2012 for background on these values.
    CodingMode (string) -- Dolby Digital coding mode. Determines number of channels.
    Dialnorm (integer) -- Sets the dialnorm for the output. If excluded and input audio is Dolby Digital, dialnorm will be passed through.
    DrcProfile (string) -- If set to filmStandard, adds dynamic range compression signaling to the output bitstream as defined in the Dolby Digital specification.
    LfeFilter (string) -- When set to enabled, applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid in codingMode32Lfe mode.
    MetadataControl (string) -- When set to "followInput", encoder metadata will be sourced from the DD, DD+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used.
    
    
    Eac3Settings (dict) -- Placeholder documentation for Eac3Settings
    AttenuationControl (string) -- When set to attenuate3Db, applies a 3 dB attenuation to the surround channels. Only used for 3/2 coding mode.
    Bitrate (float) -- Average bitrate in bits/second. Valid bitrates depend on the coding mode.
    BitstreamMode (string) -- Specifies the bitstream mode (bsmod) for the emitted E-AC-3 stream. See ATSC A/52-2012 (Annex E) for background on these values.
    CodingMode (string) -- Dolby Digital Plus coding mode. Determines number of channels.
    DcFilter (string) -- When set to enabled, activates a DC highpass filter for all input channels.
    Dialnorm (integer) -- Sets the dialnorm for the output. If blank and input audio is Dolby Digital Plus, dialnorm will be passed through.
    DrcLine (string) -- Sets the Dolby dynamic range compression profile.
    DrcRf (string) -- Sets the profile for heavy Dolby dynamic range compression, ensures that the instantaneous signal peaks do not exceed specified levels.
    LfeControl (string) -- When encoding 3/2 audio, setting to lfe enables the LFE channel
    LfeFilter (string) -- When set to enabled, applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid with codingMode32 coding mode.
    LoRoCenterMixLevel (float) -- Left only/Right only center mix level. Only used for 3/2 coding mode.
    LoRoSurroundMixLevel (float) -- Left only/Right only surround mix level. Only used for 3/2 coding mode.
    LtRtCenterMixLevel (float) -- Left total/Right total center mix level. Only used for 3/2 coding mode.
    LtRtSurroundMixLevel (float) -- Left total/Right total surround mix level. Only used for 3/2 coding mode.
    MetadataControl (string) -- When set to followInput, encoder metadata will be sourced from the DD, DD+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used.
    PassthroughControl (string) -- When set to whenPossible, input DD+ audio will be passed through if it is present on the input. This detection is dynamic over the life of the transcode. Inputs that alternate between DD+ and non-DD+ content will have a consistent DD+ output as the system alternates between passthrough and encoding.
    PhaseControl (string) -- When set to shift90Degrees, applies a 90-degree phase shift to the surround channels. Only used for 3/2 coding mode.
    StereoDownmix (string) -- Stereo downmix preference. Only used for 3/2 coding mode.
    SurroundExMode (string) -- When encoding 3/2 audio, sets whether an extra center back surround channel is matrix encoded into the left and right surround channels.
    SurroundMode (string) -- When encoding 2/0 audio, sets whether Dolby Surround is matrix encoded into the two channels.
    
    
    Mp2Settings (dict) -- Placeholder documentation for Mp2Settings
    Bitrate (float) -- Average bitrate in bits/second.
    CodingMode (string) -- The MPEG2 Audio coding mode. Valid values are codingMode10 (for mono) or codingMode20 (for stereo).
    SampleRate (float) -- Sample rate in Hz.
    
    
    PassThroughSettings (dict) -- Placeholder documentation for PassThroughSettings
    
    
    LanguageCode (string) -- Indicates the language of the audio output track. Only used if languageControlMode is useConfigured, or there is no ISO 639 language code specified in the input.
    LanguageCodeControl (string) -- Choosing followInput will cause the ISO 639 language code of the output to follow the ISO 639 language code of the input. The languageCode will be used when useConfigured is set, or when followInput is selected but there is no ISO 639 language code specified by the input.
    Name (string) -- The name of this AudioDescription. Outputs will use this name to uniquely identify this AudioDescription. Description names should be unique within this Live Event.
    RemixSettings (dict) -- Settings that control how input audio channels are remixed into the output audio channels.
    ChannelMappings (list) -- Mapping of input channels to output channels, with appropriate gain adjustments.
    (dict) -- Placeholder documentation for AudioChannelMapping
    InputChannelLevels (list) -- Indices and gain values for each input channel that should be remixed into this output channel.
    (dict) -- Placeholder documentation for InputChannelLevel
    Gain (integer) -- Remixing value. Units are in dB and acceptable values are within the range from -60 (mute) and 6 dB.
    InputChannel (integer) -- The index of the input channel used as a source.
    
    
    
    
    OutputChannel (integer) -- The index of the output channel being produced.
    
    
    
    
    ChannelsIn (integer) -- Number of input channels to be used.
    ChannelsOut (integer) -- Number of output channels to be produced. Valid values: 1, 2, 4, 6, 8
    
    
    StreamName (string) -- Used for MS Smooth and Apple HLS outputs. Indicates the name displayed by the player (eg. English, or Director Commentary).
    
    
    
    
    AvailBlanking (dict) -- Settings for ad avail blanking.
    AvailBlankingImage (dict) -- Blanking image to be used. Leave empty for solid black. Only bmp and png images are supported.
    PasswordParam (string) -- key used to extract the password from EC2 Parameter store
    Uri (string) -- Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: "rtmp://fmsserver/live".
    Username (string) -- Documentation update needed
    
    
    State (string) -- When set to enabled, causes video, audio and captions to be blanked when insertion metadata is added.
    
    
    AvailConfiguration (dict) -- Event-wide configuration settings for ad avail insertion.
    AvailSettings (dict) -- Ad avail settings.
    Scte35SpliceInsert (dict) -- Placeholder documentation for Scte35SpliceInsert
    AdAvailOffset (integer) -- When specified, this offset (in milliseconds) is added to the input Ad Avail PTS time. This only applies to embedded SCTE 104/35 messages and does not apply to OOB messages.
    NoRegionalBlackoutFlag (string) -- When set to ignore, Segment Descriptors with noRegionalBlackoutFlag set to 0 will no longer trigger blackouts or Ad Avail slates
    WebDeliveryAllowedFlag (string) -- When set to ignore, Segment Descriptors with webDeliveryAllowedFlag set to 0 will no longer trigger blackouts or Ad Avail slates
    
    
    Scte35TimeSignalApos (dict) -- Placeholder documentation for Scte35TimeSignalApos
    AdAvailOffset (integer) -- When specified, this offset (in milliseconds) is added to the input Ad Avail PTS time. This only applies to embedded SCTE 104/35 messages and does not apply to OOB messages.
    NoRegionalBlackoutFlag (string) -- When set to ignore, Segment Descriptors with noRegionalBlackoutFlag set to 0 will no longer trigger blackouts or Ad Avail slates
    WebDeliveryAllowedFlag (string) -- When set to ignore, Segment Descriptors with webDeliveryAllowedFlag set to 0 will no longer trigger blackouts or Ad Avail slates
    
    
    
    
    
    
    BlackoutSlate (dict) -- Settings for blackout slate.
    BlackoutSlateImage (dict) -- Blackout slate image to be used. Leave empty for solid black. Only bmp and png images are supported.
    PasswordParam (string) -- key used to extract the password from EC2 Parameter store
    Uri (string) -- Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: "rtmp://fmsserver/live".
    Username (string) -- Documentation update needed
    
    
    NetworkEndBlackout (string) -- Setting to enabled causes the encoder to blackout the video, audio, and captions, and raise the "Network Blackout Image" slate when an SCTE104/35 Network End Segmentation Descriptor is encountered. The blackout will be lifted when the Network Start Segmentation Descriptor is encountered. The Network End and Network Start descriptors must contain a network ID that matches the value entered in "Network ID".
    NetworkEndBlackoutImage (dict) -- Path to local file to use as Network End Blackout image. Image will be scaled to fill the entire output raster.
    PasswordParam (string) -- key used to extract the password from EC2 Parameter store
    Uri (string) -- Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: "rtmp://fmsserver/live".
    Username (string) -- Documentation update needed
    
    
    NetworkId (string) -- Provides Network ID that matches EIDR ID format (e.g., "10.XXXX/XXXX-XXXX-XXXX-XXXX-XXXX-C").
    State (string) -- When set to enabled, causes video, audio and captions to be blanked when indicated by program metadata.
    
    
    CaptionDescriptions (list) -- Settings for caption decriptions
    (dict) -- Output groups for this Live Event. Output groups contain information about where streams should be distributed.
    CaptionSelectorName (string) -- Specifies which input caption selector to use as a caption source when generating output captions. This field should match a captionSelector name.
    DestinationSettings (dict) -- Additional settings for captions destination that depend on the destination type.
    AribDestinationSettings (dict) -- Placeholder documentation for AribDestinationSettings
    BurnInDestinationSettings (dict) -- Placeholder documentation for BurnInDestinationSettings
    Alignment (string) -- If no explicit xPosition or yPosition is provided, setting alignment to centered will place the captions at the bottom center of the output. Similarly, setting a left alignment will align captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. Selecting "smart" justification will left-justify live subtitles and center-justify pre-recorded subtitles. All burn-in and DVB-Sub font settings must match.
    BackgroundColor (string) -- Specifies the color of the rectangle behind the captions. All burn-in and DVB-Sub font settings must match.
    BackgroundOpacity (integer) -- Specifies the opacity of the background rectangle. 255 is opaque; 0 is transparent. Leaving this parameter out is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
    Font (dict) -- External font file used for caption burn-in. File extension must be 'ttf' or 'tte'. Although the user can select output fonts for many different types of input captions, embedded, STL and teletext sources use a strict grid system. Using external fonts with these caption sources could cause unexpected display of proportional fonts. All burn-in and DVB-Sub font settings must match.
    PasswordParam (string) -- key used to extract the password from EC2 Parameter store
    Uri (string) -- Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: "rtmp://fmsserver/live".
    Username (string) -- Documentation update needed
    
    
    FontColor (string) -- Specifies the color of the burned-in captions. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
    FontOpacity (integer) -- Specifies the opacity of the burned-in captions. 255 is opaque; 0 is transparent. All burn-in and DVB-Sub font settings must match.
    FontResolution (integer) -- Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and DVB-Sub font settings must match.
    FontSize (string) -- When set to 'auto' fontSize will scale depending on the size of the output. Giving a positive integer will specify the exact font size in points. All burn-in and DVB-Sub font settings must match.
    OutlineColor (string) -- Specifies font outline color. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
    OutlineSize (integer) -- Specifies font outline size in pixels. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
    ShadowColor (string) -- Specifies the color of the shadow cast by the captions. All burn-in and DVB-Sub font settings must match.
    ShadowOpacity (integer) -- Specifies the opacity of the shadow. 255 is opaque; 0 is transparent. Leaving this parameter out is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
    ShadowXOffset (integer) -- Specifies the horizontal offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left. All burn-in and DVB-Sub font settings must match.
    ShadowYOffset (integer) -- Specifies the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. All burn-in and DVB-Sub font settings must match.
    TeletextGridControl (string) -- Controls whether a fixed grid size will be used to generate the output subtitles bitmap. Only applicable for Teletext inputs and DVB-Sub/Burn-in outputs.
    XPosition (integer) -- Specifies the horizontal position of the caption relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit xPosition is provided, the horizontal caption position will be determined by the alignment parameter. All burn-in and DVB-Sub font settings must match.
    YPosition (integer) -- Specifies the vertical position of the caption relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit yPosition is provided, the caption will be positioned towards the bottom of the output. All burn-in and DVB-Sub font settings must match.
    
    
    DvbSubDestinationSettings (dict) -- Placeholder documentation for DvbSubDestinationSettings
    Alignment (string) -- If no explicit xPosition or yPosition is provided, setting alignment to centered will place the captions at the bottom center of the output. Similarly, setting a left alignment will align captions to the bottom left of the output. If x and y positions are given in conjunction with the alignment parameter, the font will be justified (either left or centered) relative to those coordinates. Selecting "smart" justification will left-justify live subtitles and center-justify pre-recorded subtitles. This option is not valid for source captions that are STL or 608/embedded. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
    BackgroundColor (string) -- Specifies the color of the rectangle behind the captions. All burn-in and DVB-Sub font settings must match.
    BackgroundOpacity (integer) -- Specifies the opacity of the background rectangle. 255 is opaque; 0 is transparent. Leaving this parameter blank is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
    Font (dict) -- External font file used for caption burn-in. File extension must be 'ttf' or 'tte'. Although the user can select output fonts for many different types of input captions, embedded, STL and teletext sources use a strict grid system. Using external fonts with these caption sources could cause unexpected display of proportional fonts. All burn-in and DVB-Sub font settings must match.
    PasswordParam (string) -- key used to extract the password from EC2 Parameter store
    Uri (string) -- Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: "rtmp://fmsserver/live".
    Username (string) -- Documentation update needed
    
    
    FontColor (string) -- Specifies the color of the burned-in captions. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
    FontOpacity (integer) -- Specifies the opacity of the burned-in captions. 255 is opaque; 0 is transparent. All burn-in and DVB-Sub font settings must match.
    FontResolution (integer) -- Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and DVB-Sub font settings must match.
    FontSize (string) -- When set to auto fontSize will scale depending on the size of the output. Giving a positive integer will specify the exact font size in points. All burn-in and DVB-Sub font settings must match.
    OutlineColor (string) -- Specifies font outline color. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
    OutlineSize (integer) -- Specifies font outline size in pixels. This option is not valid for source captions that are either 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
    ShadowColor (string) -- Specifies the color of the shadow cast by the captions. All burn-in and DVB-Sub font settings must match.
    ShadowOpacity (integer) -- Specifies the opacity of the shadow. 255 is opaque; 0 is transparent. Leaving this parameter blank is equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font settings must match.
    ShadowXOffset (integer) -- Specifies the horizontal offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels to the left. All burn-in and DVB-Sub font settings must match.
    ShadowYOffset (integer) -- Specifies the vertical offset of the shadow relative to the captions in pixels. A value of -2 would result in a shadow offset 2 pixels above the text. All burn-in and DVB-Sub font settings must match.
    TeletextGridControl (string) -- Controls whether a fixed grid size will be used to generate the output subtitles bitmap. Only applicable for Teletext inputs and DVB-Sub/Burn-in outputs.
    XPosition (integer) -- Specifies the horizontal position of the caption relative to the left side of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the left of the output. If no explicit xPosition is provided, the horizontal caption position will be determined by the alignment parameter. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
    YPosition (integer) -- Specifies the vertical position of the caption relative to the top of the output in pixels. A value of 10 would result in the captions starting 10 pixels from the top of the output. If no explicit yPosition is provided, the caption will be positioned towards the bottom of the output. This option is not valid for source captions that are STL, 608/embedded or teletext. These source settings are already pre-defined by the caption stream. All burn-in and DVB-Sub font settings must match.
    
    
    EmbeddedDestinationSettings (dict) -- Placeholder documentation for EmbeddedDestinationSettings
    EmbeddedPlusScte20DestinationSettings (dict) -- Placeholder documentation for EmbeddedPlusScte20DestinationSettings
    RtmpCaptionInfoDestinationSettings (dict) -- Placeholder documentation for RtmpCaptionInfoDestinationSettings
    Scte20PlusEmbeddedDestinationSettings (dict) -- Placeholder documentation for Scte20PlusEmbeddedDestinationSettings
    Scte27DestinationSettings (dict) -- Placeholder documentation for Scte27DestinationSettings
    SmpteTtDestinationSettings (dict) -- Placeholder documentation for SmpteTtDestinationSettings
    TeletextDestinationSettings (dict) -- Placeholder documentation for TeletextDestinationSettings
    TtmlDestinationSettings (dict) -- Placeholder documentation for TtmlDestinationSettings
    StyleControl (string) -- When set to passthrough, passes through style and position information from a TTML-like input source (TTML, SMPTE-TT, CFF-TT) to the CFF-TT output or TTML output.
    
    
    WebvttDestinationSettings (dict) -- Placeholder documentation for WebvttDestinationSettings
    
    
    LanguageCode (string) -- ISO 639-2 three-digit code: http://www.loc.gov/standards/iso639-2/
    LanguageDescription (string) -- Human readable information to indicate captions available for players (eg. English, or Spanish).
    Name (string) -- Name of the caption description. Used to associate a caption description with an output. Names must be unique within an event.
    
    
    
    
    GlobalConfiguration (dict) -- Configuration settings that apply to the event as a whole.
    InitialAudioGain (integer) -- Value to set the initial audio gain for the Live Event.
    InputEndAction (string) -- Indicates the action to take when the current input completes (e.g. end-of-file). When switchAndLoopInputs is configured the encoder will restart at the beginning of the first input. When "none" is configured the encoder will transcode either black, a solid color, or a user specified slate images per the "Input Loss Behavior" configuration until the next input switch occurs (which is controlled through the Channel Schedule API).
    InputLossBehavior (dict) -- Settings for system actions when input is lost.
    BlackFrameMsec (integer) -- Documentation update needed
    InputLossImageColor (string) -- When input loss image type is "color" this field specifies the color to use. Value: 6 hex characters representing the values of RGB.
    InputLossImageSlate (dict) -- When input loss image type is "slate" these fields specify the parameters for accessing the slate.
    PasswordParam (string) -- key used to extract the password from EC2 Parameter store
    Uri (string) -- Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: "rtmp://fmsserver/live".
    Username (string) -- Documentation update needed
    
    
    InputLossImageType (string) -- Indicates whether to substitute a solid color or a slate into the output after input loss exceeds blackFrameMsec.
    RepeatFrameMsec (integer) -- Documentation update needed
    
    
    OutputTimingSource (string) -- Indicates whether the rate of frames emitted by the Live encoder should be paced by its system clock (which optionally may be locked to another source via NTP) or should be locked to the clock of the source that is providing the input stream.
    SupportLowFramerateInputs (string) -- Adjusts video input buffer for streams with very low video framerates. This is commonly set to enabled for music channels with less than one video frame per second.
    
    
    OutputGroups (list) -- Placeholder documentation for __listOfOutputGroup
    (dict) -- Output groups for this Live Event. Output groups contain information about where streams should be distributed.
    Name (string) -- Custom output group name optionally defined by the user. Only letters, numbers, and the underscore character allowed; only 32 characters allowed.
    OutputGroupSettings (dict) -- Settings associated with the output group.
    ArchiveGroupSettings (dict) -- Placeholder documentation for ArchiveGroupSettings
    Destination (dict) -- A directory and base filename where archive files should be written. If the base filename portion of the URI is left blank, the base filename of the first input will be automatically inserted.
    DestinationRefId (string) -- Placeholder documentation for __string
    
    
    RolloverInterval (integer) -- Number of seconds to write to archive file before closing and starting a new one.
    
    
    HlsGroupSettings (dict) -- Placeholder documentation for HlsGroupSettings
    AdMarkers (list) -- Choose one or more ad marker types to pass SCTE35 signals through to this group of Apple HLS outputs.
    (string) -- Placeholder documentation for HlsAdMarkers
    
    
    BaseUrlContent (string) -- A partial URI prefix that will be prepended to each output in the media .m3u8 file. Can be used if base manifest is delivered from a different URL than the main .m3u8 file.
    BaseUrlManifest (string) -- A partial URI prefix that will be prepended to each output in the media .m3u8 file. Can be used if base manifest is delivered from a different URL than the main .m3u8 file.
    CaptionLanguageMappings (list) -- Mapping of up to 4 caption channels to caption languages. Is only meaningful if captionLanguageSetting is set to "insert".
    (dict) -- Maps a caption channel to an ISO 693-2 language code (http://www.loc.gov/standards/iso639-2), with an optional description.
    CaptionChannel (integer) -- The closed caption channel being described by this CaptionLanguageMapping. Each channel mapping must have a unique channel number (maximum of 4)
    LanguageCode (string) -- Three character ISO 639-2 language code (see http://www.loc.gov/standards/iso639-2)
    LanguageDescription (string) -- Textual description of language
    
    
    
    
    CaptionLanguageSetting (string) -- Applies only to 608 Embedded output captions. insert: Include CLOSED-CAPTIONS lines in the manifest. Specify at least one language in the CC1 Language Code field. One CLOSED-CAPTION line is added for each Language Code you specify. Make sure to specify the languages in the order in which they appear in the original source (if the source is embedded format) or the order of the caption selectors (if the source is other than embedded). Otherwise, languages in the manifest will not match up properly with the output captions. none: Include CLOSED-CAPTIONS=NONE line in the manifest. omit: Omit any CLOSED-CAPTIONS line from the manifest.
    ClientCache (string) -- When set to "disabled", sets the #EXT-X-ALLOW-CACHE:no tag in the manifest, which prevents clients from saving media segments for later replay.
    CodecSpecification (string) -- Specification to use (RFC-6381 or the default RFC-4281) during m3u8 playlist generation.
    ConstantIv (string) -- For use with encryptionType. This is a 128-bit, 16-byte hex value represented by a 32-character text string. If ivSource is set to "explicit" then this parameter is required and is used as the IV for encryption.
    Destination (dict) -- A directory or HTTP destination for the HLS segments, manifest files, and encryption keys (if enabled).
    DestinationRefId (string) -- Placeholder documentation for __string
    
    
    DirectoryStructure (string) -- Place segments in subdirectories.
    EncryptionType (string) -- Encrypts the segments with the given encryption scheme. Exclude this parameter if no encryption is desired.
    HlsCdnSettings (dict) -- Parameters that control interactions with the CDN.
    HlsAkamaiSettings (dict) -- Placeholder documentation for HlsAkamaiSettings
    ConnectionRetryInterval (integer) -- Number of seconds to wait before retrying connection to the CDN if the connection is lost.
    FilecacheDuration (integer) -- Size in seconds of file cache for streaming outputs.
    HttpTransferMode (string) -- Specify whether or not to use chunked transfer encoding to Akamai. User should contact Akamai to enable this feature.
    NumRetries (integer) -- Number of retry attempts that will be made before the Live Event is put into an error state.
    RestartDelay (integer) -- If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart.
    Salt (string) -- Salt for authenticated Akamai.
    Token (string) -- Token parameter for authenticated akamai. If not specified, _gda_ is used.
    
    
    HlsBasicPutSettings (dict) -- Placeholder documentation for HlsBasicPutSettings
    ConnectionRetryInterval (integer) -- Number of seconds to wait before retrying connection to the CDN if the connection is lost.
    FilecacheDuration (integer) -- Size in seconds of file cache for streaming outputs.
    NumRetries (integer) -- Number of retry attempts that will be made before the Live Event is put into an error state.
    RestartDelay (integer) -- If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart.
    
    
    HlsMediaStoreSettings (dict) -- Placeholder documentation for HlsMediaStoreSettings
    ConnectionRetryInterval (integer) -- Number of seconds to wait before retrying connection to the CDN if the connection is lost.
    FilecacheDuration (integer) -- Size in seconds of file cache for streaming outputs.
    MediaStoreStorageClass (string) -- When set to temporal, output files are stored in non-persistent memory for faster reading and writing.
    NumRetries (integer) -- Number of retry attempts that will be made before the Live Event is put into an error state.
    RestartDelay (integer) -- If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart.
    
    
    HlsWebdavSettings (dict) -- Placeholder documentation for HlsWebdavSettings
    ConnectionRetryInterval (integer) -- Number of seconds to wait before retrying connection to the CDN if the connection is lost.
    FilecacheDuration (integer) -- Size in seconds of file cache for streaming outputs.
    HttpTransferMode (string) -- Specify whether or not to use chunked transfer encoding to WebDAV.
    NumRetries (integer) -- Number of retry attempts that will be made before the Live Event is put into an error state.
    RestartDelay (integer) -- If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart.
    
    
    
    
    IndexNSegments (integer) -- If mode is "live", the number of segments to retain in the manifest (.m3u8) file. This number must be less than or equal to keepSegments. If mode is "vod", this parameter has no effect.
    InputLossAction (string) -- Parameter that control output group behavior on input loss.
    IvInManifest (string) -- For use with encryptionType. The IV (Initialization Vector) is a 128-bit number used in conjunction with the key for encrypting blocks. If set to "include", IV is listed in the manifest, otherwise the IV is not in the manifest.
    IvSource (string) -- For use with encryptionType. The IV (Initialization Vector) is a 128-bit number used in conjunction with the key for encrypting blocks. If this setting is "followsSegmentNumber", it will cause the IV to change every segment (to match the segment number). If this is set to "explicit", you must enter a constantIv value.
    KeepSegments (integer) -- If mode is "live", the number of TS segments to retain in the destination directory. If mode is "vod", this parameter has no effect.
    KeyFormat (string) -- The value specifies how the key is represented in the resource identified by the URI. If parameter is absent, an implicit value of "identity" is used. A reverse DNS string can also be given.
    KeyFormatVersions (string) -- Either a single positive integer version value or a slash delimited list of version values (1/2/3).
    KeyProviderSettings (dict) -- The key provider settings.
    StaticKeySettings (dict) -- Placeholder documentation for StaticKeySettings
    KeyProviderServer (dict) -- The URL of the license server used for protecting content.
    PasswordParam (string) -- key used to extract the password from EC2 Parameter store
    Uri (string) -- Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: "rtmp://fmsserver/live".
    Username (string) -- Documentation update needed
    
    
    StaticKeyValue (string) -- Static key value as a 32 character hexadecimal string.
    
    
    
    
    ManifestCompression (string) -- When set to gzip, compresses HLS playlist.
    ManifestDurationFormat (string) -- Indicates whether the output manifest should use floating point or integer values for segment duration.
    MinSegmentLength (integer) -- When set, minimumSegmentLength is enforced by looking ahead and back within the specified range for a nearby avail and extending the segment size if needed.
    Mode (string) -- If "vod", all segments are indexed and kept permanently in the destination and manifest. If "live", only the number segments specified in keepSegments and indexNSegments are kept; newer segments replace older segments, which may prevent players from rewinding all the way to the beginning of the event. VOD mode uses HLS EXT-X-PLAYLIST-TYPE of EVENT while the channel is running, converting it to a "VOD" type manifest on completion of the stream.
    OutputSelection (string) -- Generates the .m3u8 playlist file for this HLS output group. The segmentsOnly option will output segments without the .m3u8 file.
    ProgramDateTime (string) -- Includes or excludes EXT-X-PROGRAM-DATE-TIME tag in .m3u8 manifest files. The value is calculated as follows: either the program date and time are initialized using the input timecode source, or the time is initialized using the input timecode source and the date is initialized using the timestampOffset.
    ProgramDateTimePeriod (integer) -- Period of insertion of EXT-X-PROGRAM-DATE-TIME entry, in seconds.
    RedundantManifest (string) -- When set to "enabled", includes the media playlists from both pipelines in the master manifest (.m3u8) file.
    SegmentLength (integer) -- Length of MPEG-2 Transport Stream segments to create (in seconds). Note that segments will end on the next keyframe after this number of seconds, so actual segment length may be longer.
    SegmentationMode (string) -- useInputSegmentation has been deprecated. The configured segment size is always used.
    SegmentsPerSubdirectory (integer) -- Number of segments to write to a subdirectory before starting a new one. directoryStructure must be subdirectoryPerStream for this setting to have an effect.
    StreamInfResolution (string) -- Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag of variant manifest.
    TimedMetadataId3Frame (string) -- Indicates ID3 frame that has the timecode.
    TimedMetadataId3Period (integer) -- Timed Metadata interval in seconds.
    TimestampDeltaMilliseconds (integer) -- Provides an extra millisecond delta offset to fine tune the timestamps.
    TsFileMode (string) -- When set to "singleFile", emits the program as a single media resource (.ts) file, and uses #EXT-X-BYTERANGE tags to index segment for playback. Playback of VOD mode content during event is not guaranteed due to HTTP server caching.
    
    
    MsSmoothGroupSettings (dict) -- Placeholder documentation for MsSmoothGroupSettings
    AcquisitionPointId (string) -- The value of the "Acquisition Point Identity" element used in each message placed in the sparse track. Only enabled if sparseTrackType is not "none".
    AudioOnlyTimecodeControl (string) -- If set to passthrough for an audio-only MS Smooth output, the fragment absolute time will be set to the current timecode. This option does not write timecodes to the audio elementary stream.
    CertificateMode (string) -- If set to verifyAuthenticity, verify the https certificate chain to a trusted Certificate Authority (CA). This will cause https outputs to self-signed certificates to fail.
    ConnectionRetryInterval (integer) -- Number of seconds to wait before retrying connection to the IIS server if the connection is lost. Content will be cached during this time and the cache will be be delivered to the IIS server once the connection is re-established.
    Destination (dict) -- Smooth Streaming publish point on an IIS server. Elemental Live acts as a "Push" encoder to IIS.
    DestinationRefId (string) -- Placeholder documentation for __string
    
    
    EventId (string) -- MS Smooth event ID to be sent to the IIS server. Should only be specified if eventIdMode is set to useConfigured.
    EventIdMode (string) -- Specifies whether or not to send an event ID to the IIS server. If no event ID is sent and the same Live Event is used without changing the publishing point, clients might see cached video from the previous run. Options: - "useConfigured" - use the value provided in eventId - "useTimestamp" - generate and send an event ID based on the current timestamp - "noEventId" - do not send an event ID to the IIS server.
    EventStopBehavior (string) -- When set to sendEos, send EOS signal to IIS server when stopping the event
    FilecacheDuration (integer) -- Size in seconds of file cache for streaming outputs.
    FragmentLength (integer) -- Length of mp4 fragments to generate (in seconds). Fragment length must be compatible with GOP size and framerate.
    InputLossAction (string) -- Parameter that control output group behavior on input loss.
    NumRetries (integer) -- Number of retry attempts.
    RestartDelay (integer) -- Number of seconds before initiating a restart due to output failure, due to exhausting the numRetries on one segment, or exceeding filecacheDuration.
    SegmentationMode (string) -- useInputSegmentation has been deprecated. The configured segment size is always used.
    SendDelayMs (integer) -- Number of milliseconds to delay the output from the second pipeline.
    SparseTrackType (string) -- If set to scte35, use incoming SCTE-35 messages to generate a sparse track in this group of MS-Smooth outputs.
    StreamManifestBehavior (string) -- When set to send, send stream manifest so publishing point doesn't start until all streams start.
    TimestampOffset (string) -- Timestamp offset for the event. Only used if timestampOffsetMode is set to useConfiguredOffset.
    TimestampOffsetMode (string) -- Type of timestamp date offset to use. - useEventStartDate: Use the date the event was started as the offset - useConfiguredOffset: Use an explicitly configured date as the offset
    
    
    RtmpGroupSettings (dict) -- Placeholder documentation for RtmpGroupSettings
    AuthenticationScheme (string) -- Authentication scheme to use when connecting with CDN
    CacheFullBehavior (string) -- Controls behavior when content cache fills up. If remote origin server stalls the RTMP connection and does not accept content fast enough the 'Media Cache' will fill up. When the cache reaches the duration specified by cacheLength the cache will stop accepting new content. If set to disconnectImmediately, the RTMP output will force a disconnect. Clear the media cache, and reconnect after restartDelay seconds. If set to waitForServer, the RTMP output will wait up to 5 minutes to allow the origin server to begin accepting data again.
    CacheLength (integer) -- Cache length, in seconds, is used to calculate buffer size.
    CaptionData (string) -- Controls the types of data that passes to onCaptionInfo outputs. If set to 'all' then 608 and 708 carried DTVCC data will be passed. If set to 'field1AndField2608' then DTVCC data will be stripped out, but 608 data from both fields will be passed. If set to 'field1608' then only the data carried in 608 from field 1 video will be passed.
    InputLossAction (string) -- Controls the behavior of this RTMP group if input becomes unavailable. - emitOutput: Emit a slate until input returns. - pauseOutput: Stop transmitting data until input returns. This does not close the underlying RTMP connection.
    RestartDelay (integer) -- If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart.
    
    
    UdpGroupSettings (dict) -- Placeholder documentation for UdpGroupSettings
    InputLossAction (string) -- Specifies behavior of last resort when input video is lost, and no more backup inputs are available. When dropTs is selected the entire transport stream will stop being emitted. When dropProgram is selected the program can be dropped from the transport stream (and replaced with null packets to meet the TS bitrate requirement). Or, when emitProgram is chosen the transport stream will continue to be produced normally with repeat frames, black frames, or slate frames substituted for the absent input video.
    TimedMetadataId3Frame (string) -- Indicates ID3 frame that has the timecode.
    TimedMetadataId3Period (integer) -- Timed Metadata interval in seconds.
    
    
    
    
    Outputs (list) -- Placeholder documentation for __listOfOutput
    (dict) -- Output settings. There can be multiple outputs within a group.
    AudioDescriptionNames (list) -- The names of the AudioDescriptions used as audio sources for this output.
    (string) -- Placeholder documentation for __string
    
    
    CaptionDescriptionNames (list) -- The names of the CaptionDescriptions used as caption sources for this output.
    (string) -- Placeholder documentation for __string
    
    
    OutputName (string) -- The name used to identify an output.
    OutputSettings (dict) -- Output type-specific settings.
    ArchiveOutputSettings (dict) -- Placeholder documentation for ArchiveOutputSettings
    ContainerSettings (dict) -- Settings specific to the container type of the file.
    M2tsSettings (dict) -- Placeholder documentation for M2tsSettings
    AbsentInputAudioBehavior (string) -- When set to drop, output audio streams will be removed from the program if the selected input audio stream is removed from the input. This allows the output audio configuration to dynamically change based on input configuration. If this is set to encodeSilence, all output audio streams will output encoded silence when not connected to an active input stream.
    Arib (string) -- When set to enabled, uses ARIB-compliant field muxing and removes video descriptor.
    AribCaptionsPid (string) -- Packet Identifier (PID) for ARIB Captions in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    AribCaptionsPidControl (string) -- If set to auto, pid number used for ARIB Captions will be auto-selected from unused pids. If set to useConfigured, ARIB Captions will be on the configured pid number.
    AudioBufferModel (string) -- When set to dvb, uses DVB buffer model for Dolby Digital audio. When set to atsc, the ATSC model is used.
    AudioFramesPerPes (integer) -- The number of audio frames to insert for each PES packet.
    AudioPids (string) -- Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
    AudioStreamType (string) -- When set to atsc, uses stream type = 0x81 for AC3 and stream type = 0x87 for EAC3. When set to dvb, uses stream type = 0x06.
    Bitrate (integer) -- The output bitrate of the transport stream in bits per second. Setting to 0 lets the muxer automatically determine the appropriate bitrate.
    BufferModel (string) -- If set to multiplex, use multiplex buffer model for accurate interleaving. Setting to bufferModel to none can lead to lower latency, but low-memory devices may not be able to play back the stream without interruptions.
    CcDescriptor (string) -- When set to enabled, generates captionServiceDescriptor in PMT.
    DvbNitSettings (dict) -- Inserts DVB Network Information Table (NIT) at the specified table repetition interval.
    NetworkId (integer) -- The numeric value placed in the Network Information Table (NIT).
    NetworkName (string) -- The network name text placed in the networkNameDescriptor inside the Network Information Table. Maximum length is 256 characters.
    RepInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream.
    
    
    DvbSdtSettings (dict) -- Inserts DVB Service Description Table (SDT) at the specified table repetition interval.
    OutputSdt (string) -- Selects method of inserting SDT information into output stream. The sdtFollow setting copies SDT information from input stream to output stream. The sdtFollowIfPresent setting copies SDT information from input stream to output stream if SDT information is present in the input, otherwise it will fall back on the user-defined values. The sdtManual setting means user will enter the SDT information. The sdtNone setting means output stream will not contain SDT information.
    RepInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream.
    ServiceName (string) -- The service name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters.
    ServiceProviderName (string) -- The service provider name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters.
    
    
    DvbSubPids (string) -- Packet Identifier (PID) for input source DVB Subtitle data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
    DvbTdtSettings (dict) -- Inserts DVB Time and Date Table (TDT) at the specified table repetition interval.
    RepInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream.
    
    
    DvbTeletextPid (string) -- Packet Identifier (PID) for input source DVB Teletext data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    Ebif (string) -- If set to passthrough, passes any EBIF data from the input source to this output.
    EbpAudioInterval (string) -- When videoAndFixedIntervals is selected, audio EBP markers will be added to partitions 3 and 4. The interval between these additional markers will be fixed, and will be slightly shorter than the video EBP marker interval. Only available when EBP Cablelabs segmentation markers are selected. Partitions 1 and 2 will always follow the video interval.
    EbpLookaheadMs (integer) -- When set, enforces that Encoder Boundary Points do not come within the specified time interval of each other by looking ahead at input video. If another EBP is going to come in within the specified time interval, the current EBP is not emitted, and the segment is "stretched" to the next marker. The lookahead value does not add latency to the system. The Live Event must be configured elsewhere to create sufficient latency to make the lookahead accurate.
    EbpPlacement (string) -- Controls placement of EBP on Audio PIDs. If set to videoAndAudioPids, EBP markers will be placed on the video PID and all audio PIDs. If set to videoPid, EBP markers will be placed on only the video PID.
    EcmPid (string) -- This field is unused and deprecated.
    EsRateInPes (string) -- Include or exclude the ES Rate field in the PES header.
    EtvPlatformPid (string) -- Packet Identifier (PID) for input source ETV Platform data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    EtvSignalPid (string) -- Packet Identifier (PID) for input source ETV Signal data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    FragmentTime (float) -- The length in seconds of each fragment. Only used with EBP markers.
    Klv (string) -- If set to passthrough, passes any KLV data from the input source to this output.
    KlvDataPids (string) -- Packet Identifier (PID) for input source KLV data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
    NullPacketBitrate (float) -- Value in bits per second of extra null packets to insert into the transport stream. This can be used if a downstream encryption system requires periodic null packets.
    PatInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000.
    PcrControl (string) -- When set to pcrEveryPesPacket, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream.
    PcrPeriod (integer) -- Maximum time in milliseconds between Program Clock Reference (PCRs) inserted into the transport stream.
    PcrPid (string) -- Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    PmtInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000.
    PmtPid (string) -- Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    ProgramNum (integer) -- The value of the program number field in the Program Map Table.
    RateMode (string) -- When vbr, does not insert null packets into transport stream to fill specified bitrate. The bitrate setting acts as the maximum bitrate when vbr is set.
    Scte27Pids (string) -- Packet Identifier (PID) for input source SCTE-27 data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
    Scte35Control (string) -- Optionally pass SCTE-35 signals from the input source to this output.
    Scte35Pid (string) -- Packet Identifier (PID) of the SCTE-35 stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    SegmentationMarkers (string) -- Inserts segmentation markers at each segmentationTime period. raiSegstart sets the Random Access Indicator bit in the adaptation field. raiAdapt sets the RAI bit and adds the current timecode in the private data bytes. psiSegstart inserts PAT and PMT tables at the start of segments. ebp adds Encoder Boundary Point information to the adaptation field as per OpenCable specification OC-SP-EBP-I01-130118. ebpLegacy adds Encoder Boundary Point information to the adaptation field using a legacy proprietary format.
    SegmentationStyle (string) -- The segmentation style parameter controls how segmentation markers are inserted into the transport stream. With avails, it is possible that segments may be truncated, which can influence where future segmentation markers are inserted. When a segmentation style of "resetCadence" is selected and a segment is truncated due to an avail, we will reset the segmentation cadence. This means the subsequent segment will have a duration of $segmentationTime seconds. When a segmentation style of "maintainCadence" is selected and a segment is truncated due to an avail, we will not reset the segmentation cadence. This means the subsequent segment will likely be truncated as well. However, all segments after that will have a duration of $segmentationTime seconds. Note that EBP lookahead is a slight exception to this rule.
    SegmentationTime (float) -- The length in seconds of each segment. Required unless markers is set to None_.
    TimedMetadataBehavior (string) -- When set to passthrough, timed metadata will be passed through from input to output.
    TimedMetadataPid (string) -- Packet Identifier (PID) of the timed metadata stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    TransportStreamId (integer) -- The value of the transport stream ID field in the Program Map Table.
    VideoPid (string) -- Packet Identifier (PID) of the elementary video stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    
    
    
    
    Extension (string) -- Output file extension. If excluded, this will be auto-selected from the container type.
    NameModifier (string) -- String concatenated to the end of the destination filename. Required for multiple outputs of the same type.
    
    
    HlsOutputSettings (dict) -- Placeholder documentation for HlsOutputSettings
    HlsSettings (dict) -- Settings regarding the underlying stream. These settings are different for audio-only outputs.
    AudioOnlyHlsSettings (dict) -- Placeholder documentation for AudioOnlyHlsSettings
    AudioGroupId (string) -- Specifies the group to which the audio Rendition belongs.
    AudioOnlyImage (dict) -- For use with an audio only Stream. Must be a .jpg or .png file. If given, this image will be used as the cover-art for the audio only output. Ideally, it should be formatted for an iPhone screen for two reasons. The iPhone does not resize the image, it crops a centered image on the top/bottom and left/right. Additionally, this image file gets saved bit-for-bit into every 10-second segment file, so will increase bandwidth by {image file size} * {segment count} * {user count.}.
    PasswordParam (string) -- key used to extract the password from EC2 Parameter store
    Uri (string) -- Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: "rtmp://fmsserver/live".
    Username (string) -- Documentation update needed
    
    
    AudioTrackType (string) -- Four types of audio-only tracks are supported: Audio-Only Variant Stream The client can play back this audio-only stream instead of video in low-bandwidth scenarios. Represented as an EXT-X-STREAM-INF in the HLS manifest. Alternate Audio, Auto Select, Default Alternate rendition that the client should try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=YES, AUTOSELECT=YES Alternate Audio, Auto Select, Not Default Alternate rendition that the client may try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=YES Alternate Audio, not Auto Select Alternate rendition that the client will not try to play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=NO
    
    
    StandardHlsSettings (dict) -- Placeholder documentation for StandardHlsSettings
    AudioRenditionSets (string) -- List all the audio groups that are used with the video output stream. Input all the audio GROUP-IDs that are associated to the video, separate by ','.
    M3u8Settings (dict) -- Settings information for the .m3u8 container
    AudioFramesPerPes (integer) -- The number of audio frames to insert for each PES packet.
    AudioPids (string) -- Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values.
    EcmPid (string) -- This parameter is unused and deprecated.
    PatInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream. A value of "0" writes out the PMT once per segment file.
    PcrControl (string) -- When set to pcrEveryPesPacket, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream.
    PcrPeriod (integer) -- Maximum time in milliseconds between Program Clock References (PCRs) inserted into the transport stream.
    PcrPid (string) -- Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID. Can be entered as a decimal or hexadecimal value.
    PmtInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream. A value of "0" writes out the PMT once per segment file.
    PmtPid (string) -- Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream. Can be entered as a decimal or hexadecimal value.
    ProgramNum (integer) -- The value of the program number field in the Program Map Table.
    Scte35Behavior (string) -- If set to passthrough, passes any SCTE-35 signals from the input source to this output.
    Scte35Pid (string) -- Packet Identifier (PID) of the SCTE-35 stream in the transport stream. Can be entered as a decimal or hexadecimal value.
    TimedMetadataBehavior (string) -- When set to passthrough, timed metadata is passed through from input to output.
    TimedMetadataPid (string) -- Packet Identifier (PID) of the timed metadata stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    TransportStreamId (integer) -- The value of the transport stream ID field in the Program Map Table.
    VideoPid (string) -- Packet Identifier (PID) of the elementary video stream in the transport stream. Can be entered as a decimal or hexadecimal value.
    
    
    
    
    
    
    NameModifier (string) -- String concatenated to the end of the destination filename. Accepts "Format Identifiers":#formatIdentifierParameters.
    SegmentModifier (string) -- String concatenated to end of segment filenames.
    
    
    MsSmoothOutputSettings (dict) -- Placeholder documentation for MsSmoothOutputSettings
    NameModifier (string) -- String concatenated to the end of the destination filename. Required for multiple outputs of the same type.
    
    
    RtmpOutputSettings (dict) -- Placeholder documentation for RtmpOutputSettings
    CertificateMode (string) -- If set to verifyAuthenticity, verify the tls certificate chain to a trusted Certificate Authority (CA). This will cause rtmps outputs with self-signed certificates to fail.
    ConnectionRetryInterval (integer) -- Number of seconds to wait before retrying a connection to the Flash Media server if the connection is lost.
    Destination (dict) -- The RTMP endpoint excluding the stream name (eg. rtmp://host/appname). For connection to Akamai, a username and password must be supplied. URI fields accept format identifiers.
    DestinationRefId (string) -- Placeholder documentation for __string
    
    
    NumRetries (integer) -- Number of retry attempts.
    
    
    UdpOutputSettings (dict) -- Placeholder documentation for UdpOutputSettings
    BufferMsec (integer) -- UDP output buffering in milliseconds. Larger values increase latency through the transcoder but simultaneously assist the transcoder in maintaining a constant, low-jitter UDP/RTP output while accommodating clock recovery, input switching, input disruptions, picture reordering, etc.
    ContainerSettings (dict) -- Placeholder documentation for UdpContainerSettings
    M2tsSettings (dict) -- Placeholder documentation for M2tsSettings
    AbsentInputAudioBehavior (string) -- When set to drop, output audio streams will be removed from the program if the selected input audio stream is removed from the input. This allows the output audio configuration to dynamically change based on input configuration. If this is set to encodeSilence, all output audio streams will output encoded silence when not connected to an active input stream.
    Arib (string) -- When set to enabled, uses ARIB-compliant field muxing and removes video descriptor.
    AribCaptionsPid (string) -- Packet Identifier (PID) for ARIB Captions in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    AribCaptionsPidControl (string) -- If set to auto, pid number used for ARIB Captions will be auto-selected from unused pids. If set to useConfigured, ARIB Captions will be on the configured pid number.
    AudioBufferModel (string) -- When set to dvb, uses DVB buffer model for Dolby Digital audio. When set to atsc, the ATSC model is used.
    AudioFramesPerPes (integer) -- The number of audio frames to insert for each PES packet.
    AudioPids (string) -- Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
    AudioStreamType (string) -- When set to atsc, uses stream type = 0x81 for AC3 and stream type = 0x87 for EAC3. When set to dvb, uses stream type = 0x06.
    Bitrate (integer) -- The output bitrate of the transport stream in bits per second. Setting to 0 lets the muxer automatically determine the appropriate bitrate.
    BufferModel (string) -- If set to multiplex, use multiplex buffer model for accurate interleaving. Setting to bufferModel to none can lead to lower latency, but low-memory devices may not be able to play back the stream without interruptions.
    CcDescriptor (string) -- When set to enabled, generates captionServiceDescriptor in PMT.
    DvbNitSettings (dict) -- Inserts DVB Network Information Table (NIT) at the specified table repetition interval.
    NetworkId (integer) -- The numeric value placed in the Network Information Table (NIT).
    NetworkName (string) -- The network name text placed in the networkNameDescriptor inside the Network Information Table. Maximum length is 256 characters.
    RepInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream.
    
    
    DvbSdtSettings (dict) -- Inserts DVB Service Description Table (SDT) at the specified table repetition interval.
    OutputSdt (string) -- Selects method of inserting SDT information into output stream. The sdtFollow setting copies SDT information from input stream to output stream. The sdtFollowIfPresent setting copies SDT information from input stream to output stream if SDT information is present in the input, otherwise it will fall back on the user-defined values. The sdtManual setting means user will enter the SDT information. The sdtNone setting means output stream will not contain SDT information.
    RepInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream.
    ServiceName (string) -- The service name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters.
    ServiceProviderName (string) -- The service provider name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters.
    
    
    DvbSubPids (string) -- Packet Identifier (PID) for input source DVB Subtitle data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
    DvbTdtSettings (dict) -- Inserts DVB Time and Date Table (TDT) at the specified table repetition interval.
    RepInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream.
    
    
    DvbTeletextPid (string) -- Packet Identifier (PID) for input source DVB Teletext data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    Ebif (string) -- If set to passthrough, passes any EBIF data from the input source to this output.
    EbpAudioInterval (string) -- When videoAndFixedIntervals is selected, audio EBP markers will be added to partitions 3 and 4. The interval between these additional markers will be fixed, and will be slightly shorter than the video EBP marker interval. Only available when EBP Cablelabs segmentation markers are selected. Partitions 1 and 2 will always follow the video interval.
    EbpLookaheadMs (integer) -- When set, enforces that Encoder Boundary Points do not come within the specified time interval of each other by looking ahead at input video. If another EBP is going to come in within the specified time interval, the current EBP is not emitted, and the segment is "stretched" to the next marker. The lookahead value does not add latency to the system. The Live Event must be configured elsewhere to create sufficient latency to make the lookahead accurate.
    EbpPlacement (string) -- Controls placement of EBP on Audio PIDs. If set to videoAndAudioPids, EBP markers will be placed on the video PID and all audio PIDs. If set to videoPid, EBP markers will be placed on only the video PID.
    EcmPid (string) -- This field is unused and deprecated.
    EsRateInPes (string) -- Include or exclude the ES Rate field in the PES header.
    EtvPlatformPid (string) -- Packet Identifier (PID) for input source ETV Platform data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    EtvSignalPid (string) -- Packet Identifier (PID) for input source ETV Signal data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    FragmentTime (float) -- The length in seconds of each fragment. Only used with EBP markers.
    Klv (string) -- If set to passthrough, passes any KLV data from the input source to this output.
    KlvDataPids (string) -- Packet Identifier (PID) for input source KLV data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
    NullPacketBitrate (float) -- Value in bits per second of extra null packets to insert into the transport stream. This can be used if a downstream encryption system requires periodic null packets.
    PatInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000.
    PcrControl (string) -- When set to pcrEveryPesPacket, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream.
    PcrPeriod (integer) -- Maximum time in milliseconds between Program Clock Reference (PCRs) inserted into the transport stream.
    PcrPid (string) -- Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    PmtInterval (integer) -- The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000.
    PmtPid (string) -- Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    ProgramNum (integer) -- The value of the program number field in the Program Map Table.
    RateMode (string) -- When vbr, does not insert null packets into transport stream to fill specified bitrate. The bitrate setting acts as the maximum bitrate when vbr is set.
    Scte27Pids (string) -- Packet Identifier (PID) for input source SCTE-27 data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
    Scte35Control (string) -- Optionally pass SCTE-35 signals from the input source to this output.
    Scte35Pid (string) -- Packet Identifier (PID) of the SCTE-35 stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    SegmentationMarkers (string) -- Inserts segmentation markers at each segmentationTime period. raiSegstart sets the Random Access Indicator bit in the adaptation field. raiAdapt sets the RAI bit and adds the current timecode in the private data bytes. psiSegstart inserts PAT and PMT tables at the start of segments. ebp adds Encoder Boundary Point information to the adaptation field as per OpenCable specification OC-SP-EBP-I01-130118. ebpLegacy adds Encoder Boundary Point information to the adaptation field using a legacy proprietary format.
    SegmentationStyle (string) -- The segmentation style parameter controls how segmentation markers are inserted into the transport stream. With avails, it is possible that segments may be truncated, which can influence where future segmentation markers are inserted. When a segmentation style of "resetCadence" is selected and a segment is truncated due to an avail, we will reset the segmentation cadence. This means the subsequent segment will have a duration of $segmentationTime seconds. When a segmentation style of "maintainCadence" is selected and a segment is truncated due to an avail, we will not reset the segmentation cadence. This means the subsequent segment will likely be truncated as well. However, all segments after that will have a duration of $segmentationTime seconds. Note that EBP lookahead is a slight exception to this rule.
    SegmentationTime (float) -- The length in seconds of each segment. Required unless markers is set to None_.
    TimedMetadataBehavior (string) -- When set to passthrough, timed metadata will be passed through from input to output.
    TimedMetadataPid (string) -- Packet Identifier (PID) of the timed metadata stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    TransportStreamId (integer) -- The value of the transport stream ID field in the Program Map Table.
    VideoPid (string) -- Packet Identifier (PID) of the elementary video stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    
    
    
    
    Destination (dict) -- Destination address and port number for RTP or UDP packets. Can be unicast or multicast RTP or UDP (eg. rtp://239.10.10.10:5001 or udp://10.100.100.100:5002).
    DestinationRefId (string) -- Placeholder documentation for __string
    
    
    FecOutputSettings (dict) -- Settings for enabling and adjusting Forward Error Correction on UDP outputs.
    ColumnDepth (integer) -- Parameter D from SMPTE 2022-1. The height of the FEC protection matrix. The number of transport stream packets per column error correction packet. Must be between 4 and 20, inclusive.
    IncludeFec (string) -- Enables column only or column and row based FEC
    RowLength (integer) -- Parameter L from SMPTE 2022-1. The width of the FEC protection matrix. Must be between 1 and 20, inclusive. If only Column FEC is used, then larger values increase robustness. If Row FEC is used, then this is the number of transport stream packets per row error correction packet, and the value must be between 4 and 20, inclusive, if includeFec is columnAndRow. If includeFec is column, this value must be 1 to 20, inclusive.
    
    
    
    
    
    
    VideoDescriptionName (string) -- The name of the VideoDescription used as the source for this output.
    
    
    
    
    
    
    
    
    TimecodeConfig (dict) -- Contains settings used to acquire and adjust timecode information from inputs.
    Source (string) -- Identifies the source for the timecode that will be associated with the events outputs. -Embedded (embedded): Initialize the output timecode with timecode from the the source. If no embedded timecode is detected in the source, the system falls back to using "Start at 0" (zerobased). -System Clock (systemclock): Use the UTC time. -Start at 0 (zerobased): The time of the first frame of the event will be 00:00:00:00.
    SyncThreshold (integer) -- Threshold in frames beyond which output timecode is resynchronized to the input timecode. Discrepancies below this threshold are permitted to avoid unnecessary discontinuities in the output timecode. No timecode sync when this is not specified.
    
    
    VideoDescriptions (list) -- Placeholder documentation for __listOfVideoDescription
    (dict) -- Video settings for this stream.
    CodecSettings (dict) -- Video codec settings.
    H264Settings (dict) -- Placeholder documentation for H264Settings
    AdaptiveQuantization (string) -- Adaptive quantization. Allows intra-frame quantizers to vary to improve visual quality.
    AfdSignaling (string) -- Indicates that AFD values will be written into the output stream. If afdSignaling is "auto", the system will try to preserve the input AFD value (in cases where multiple AFD values are valid). If set to "fixed", the AFD value will be the value configured in the fixedAfd parameter.
    Bitrate (integer) -- Average bitrate in bits/second. Required when the rate control mode is VBR or CBR. Not used for QVBR. In an MS Smooth output group, each output must have a unique value when its bitrate is rounded down to the nearest multiple of 1000.
    BufFillPct (integer) -- Percentage of the buffer that should initially be filled (HRD buffer model).
    BufSize (integer) -- Size of buffer (HRD buffer model) in bits/second.
    ColorMetadata (string) -- Includes colorspace metadata in the output.
    EntropyEncoding (string) -- Entropy encoding mode. Use cabac (must be in Main or High profile) or cavlc.
    FixedAfd (string) -- Four bit AFD value to write on all frames of video in the output stream. Only valid when afdSignaling is set to 'Fixed'.
    FlickerAq (string) -- If set to enabled, adjust quantization within each frame to reduce flicker or 'pop' on I-frames.
    FramerateControl (string) -- This field indicates how the output video frame rate is specified. If "specified" is selected then the output video frame rate is determined by framerateNumerator and framerateDenominator, else if "initializeFromSource" is selected then the output video frame rate will be set equal to the input video frame rate of the first input.
    FramerateDenominator (integer) -- Framerate denominator.
    FramerateNumerator (integer) -- Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976 fps.
    GopBReference (string) -- Documentation update needed
    GopClosedCadence (integer) -- Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting.
    GopNumBFrames (integer) -- Number of B-frames between reference frames.
    GopSize (float) -- GOP size (keyframe interval) in units of either frames or seconds per gopSizeUnits. Must be greater than zero.
    GopSizeUnits (string) -- Indicates if the gopSize is specified in frames or seconds. If seconds the system will convert the gopSize into a frame count at run time.
    Level (string) -- H.264 Level.
    LookAheadRateControl (string) -- Amount of lookahead. A value of low can decrease latency and memory usage, while high can produce better quality for certain content.
    MaxBitrate (integer) -- For QVBR: See the tooltip for Quality level For VBR: Set the maximum bitrate in order to accommodate expected spikes in the complexity of the video.
    MinIInterval (integer) -- Only meaningful if sceneChangeDetect is set to enabled. Enforces separation between repeated (cadence) I-frames and I-frames inserted by Scene Change Detection. If a scene change I-frame is within I-interval frames of a cadence I-frame, the GOP is shrunk and/or stretched to the scene change I-frame. GOP stretch requires enabling lookahead as well as setting I-interval. The normal cadence resumes for the next GOP. Note: Maximum GOP stretch = GOP size + Min-I-interval - 1
    NumRefFrames (integer) -- Number of reference frames to use. The encoder may use more than requested if using B-frames and/or interlaced encoding.
    ParControl (string) -- This field indicates how the output pixel aspect ratio is specified. If "specified" is selected then the output video pixel aspect ratio is determined by parNumerator and parDenominator, else if "initializeFromSource" is selected then the output pixsel aspect ratio will be set equal to the input video pixel aspect ratio of the first input.
    ParDenominator (integer) -- Pixel Aspect Ratio denominator.
    ParNumerator (integer) -- Pixel Aspect Ratio numerator.
    Profile (string) -- H.264 Profile.
    QvbrQualityLevel (integer) -- Controls the target quality for the video encode. Applies only when the rate control mode is QVBR. Set values for the QVBR quality level field and Max bitrate field that suit your most important viewing devices. Recommended values are: - Primary screen: Quality level: 8 to 10. Max bitrate: 4M - PC or tablet: Quality level: 7. Max bitrate: 1.5M to 3M - Smartphone: Quality level: 6. Max bitrate: 1M to 1.5M
    RateControlMode (string) -- Rate control mode. QVBR: Quality will match the specified quality level except when it is constrained by the maximum bitrate. Recommended if you or your viewers pay for bandwidth. VBR: Quality and bitrate vary, depending on the video complexity. Recommended instead of QVBR if you want to maintain a specific average bitrate over the duration of the channel. CBR: Quality varies, depending on the video complexity. Recommended only if you distribute your assets to devices that cannot handle variable bitrates.
    ScanType (string) -- Sets the scan type of the output to progressive or top-field-first interlaced.
    SceneChangeDetect (string) -- Scene change detection. - On: inserts I-frames when scene change is detected. - Off: does not force an I-frame when scene change is detected.
    Slices (integer) -- Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures. This field is optional; when no value is specified the encoder will choose the number of slices based on encode resolution.
    Softness (integer) -- Softness. Selects quantizer matrix, larger values reduce high-frequency content in the encoded image.
    SpatialAq (string) -- If set to enabled, adjust quantization within each frame based on spatial variation of content complexity.
    SubgopLength (string) -- If set to fixed, use gopNumBFrames B-frames per sub-GOP. If set to dynamic, optimize the number of B-frames used for each sub-GOP to improve visual quality.
    Syntax (string) -- Produces a bitstream compliant with SMPTE RP-2027.
    TemporalAq (string) -- If set to enabled, adjust quantization within each frame based on temporal variation of content complexity.
    TimecodeInsertion (string) -- Determines how timecodes should be inserted into the video elementary stream. - 'disabled': Do not include timecodes - 'picTimingSei': Pass through picture timing SEI messages from the source specified in Timecode Config
    
    
    
    
    Height (integer) -- Output video height (in pixels). Leave blank to use source video height. If left blank, width must also be unspecified.
    Name (string) -- The name of this VideoDescription. Outputs will use this name to uniquely identify this Description. Description names should be unique within this Live Event.
    RespondToAfd (string) -- Indicates how to respond to the AFD values in the input stream. Setting to "respond" causes input video to be clipped, depending on AFD value, input display aspect ratio and output display aspect ratio.
    ScalingBehavior (string) -- When set to "stretchToOutput", automatically configures the output position to stretch the video to the specified output resolution. This option will override any position value.
    Sharpness (integer) -- Changes the width of the anti-alias filter kernel used for scaling. Only applies if scaling is being performed and antiAlias is set to true. 0 is the softest setting, 100 the sharpest, and 50 recommended for most content.
    Width (integer) -- Output video width (in pixels). Leave out to use source video width. If left out, height must also be left out. Display aspect ratio is always preserved by letterboxing or pillarboxing when necessary.
    
    
    
    
    
    
    Id (string) -- The unique id of the channel.
    InputAttachments (list) -- List of input attachments for channel.
    (dict) -- Placeholder documentation for InputAttachment
    InputAttachmentName (string) -- User-specified name for the attachment. This is required if the user wants to use this input in an input switch action.
    InputId (string) -- The ID of the input
    InputSettings (dict) -- Settings of an input (caption selector, etc.)
    AudioSelectors (list) -- Used to select the audio stream to decode for inputs that have multiple available.
    (dict) -- Placeholder documentation for AudioSelector
    Name (string) -- The name of this AudioSelector. AudioDescriptions will use this name to uniquely identify this Selector. Selector names should be unique per input.
    SelectorSettings (dict) -- The audio selector settings.
    AudioLanguageSelection (dict) -- Placeholder documentation for AudioLanguageSelection
    LanguageCode (string) -- Selects a specific three-letter language code from within an audio source.
    LanguageSelectionPolicy (string) -- When set to "strict", the transport stream demux strictly identifies audio streams by their language descriptor. If a PMT update occurs such that an audio stream matching the initially selected language is no longer present then mute will be encoded until the language returns. If "loose", then on a PMT update the demux will choose another audio stream in the program with the same stream type if it can't find one with the same language.
    
    
    AudioPidSelection (dict) -- Placeholder documentation for AudioPidSelection
    Pid (integer) -- Selects a specific PID from within a source.
    
    
    
    
    
    
    
    
    CaptionSelectors (list) -- Used to select the caption input to use for inputs that have multiple available.
    (dict) -- Output groups for this Live Event. Output groups contain information about where streams should be distributed.
    LanguageCode (string) -- When specified this field indicates the three letter language code of the caption track to extract from the source.
    Name (string) -- Name identifier for a caption selector. This name is used to associate this caption selector with one or more caption descriptions. Names must be unique within an event.
    SelectorSettings (dict) -- Caption selector settings.
    AribSourceSettings (dict) -- Placeholder documentation for AribSourceSettings
    DvbSubSourceSettings (dict) -- Placeholder documentation for DvbSubSourceSettings
    Pid (integer) -- When using DVB-Sub with Burn-In or SMPTE-TT, use this PID for the source content. Unused for DVB-Sub passthrough. All DVB-Sub content is passed through, regardless of selectors.
    
    
    EmbeddedSourceSettings (dict) -- Placeholder documentation for EmbeddedSourceSettings
    Convert608To708 (string) -- If upconvert, 608 data is both passed through via the "608 compatibility bytes" fields of the 708 wrapper as well as translated into 708. 708 data present in the source content will be discarded.
    Scte20Detection (string) -- Set to "auto" to handle streams with intermittent and/or non-aligned SCTE-20 and Embedded captions.
    Source608ChannelNumber (integer) -- Specifies the 608/708 channel number within the video track from which to extract captions. Unused for passthrough.
    Source608TrackNumber (integer) -- This field is unused and deprecated.
    
    
    Scte20SourceSettings (dict) -- Placeholder documentation for Scte20SourceSettings
    Convert608To708 (string) -- If upconvert, 608 data is both passed through via the "608 compatibility bytes" fields of the 708 wrapper as well as translated into 708. 708 data present in the source content will be discarded.
    Source608ChannelNumber (integer) -- Specifies the 608/708 channel number within the video track from which to extract captions. Unused for passthrough.
    
    
    Scte27SourceSettings (dict) -- Placeholder documentation for Scte27SourceSettings
    Pid (integer) -- The pid field is used in conjunction with the caption selector languageCode field as follows: - Specify PID and Language: Extracts captions from that PID; the language is "informational". - Specify PID and omit Language: Extracts the specified PID. - Omit PID and specify Language: Extracts the specified language, whichever PID that happens to be. - Omit PID and omit Language: Valid only if source is DVB-Sub that is being passed through; all languages will be passed through.
    
    
    TeletextSourceSettings (dict) -- Placeholder documentation for TeletextSourceSettings
    PageNumber (string) -- Specifies the teletext page number within the data stream from which to extract captions. Range of 0x100 (256) to 0x8FF (2303). Unused for passthrough. Should be specified as a hexadecimal string with no "0x" prefix.
    
    
    
    
    
    
    
    
    DeblockFilter (string) -- Enable or disable the deblock filter when filtering.
    DenoiseFilter (string) -- Enable or disable the denoise filter when filtering.
    FilterStrength (integer) -- Adjusts the magnitude of filtering from 1 (minimal) to 5 (strongest).
    InputFilter (string) -- Turns on the filter for this input. MPEG-2 inputs have the deblocking filter enabled by default. 1) auto - filtering will be applied depending on input type/quality 2) disabled - no filtering will be applied to the input 3) forced - filtering will be applied regardless of input type
    NetworkInputSettings (dict) -- Input settings.
    HlsInputSettings (dict) -- Specifies HLS input settings when the uri is for a HLS manifest.
    Bandwidth (integer) -- When specified the HLS stream with the m3u8 BANDWIDTH that most closely matches this value will be chosen, otherwise the highest bandwidth stream in the m3u8 will be chosen. The bitrate is specified in bits per second, as in an HLS manifest.
    BufferSegments (integer) -- When specified, reading of the HLS input will begin this many buffer segments from the end (most recently written segment). When not specified, the HLS input will begin with the first segment specified in the m3u8.
    Retries (integer) -- The number of consecutive times that attempts to read a manifest or segment must fail before the input is considered unavailable.
    RetryInterval (integer) -- The number of seconds between retries when an attempt to read a manifest or segment fails.
    
    
    ServerValidation (string) -- Check HTTPS server certificates. When set to checkCryptographyOnly, cryptography in the certificate will be checked, but not the server's name. Certain subdomains (notably S3 buckets that use dots in the bucket name) do not strictly match the corresponding certificate's wildcard pattern and would otherwise cause the event to error. This setting is ignored for protocols that do not use https.
    
    
    SourceEndBehavior (string) -- Loop input if it is a file. This allows a file input to be streamed indefinitely.
    VideoSelector (dict) -- Informs which video elementary stream to decode for input types that have multiple available.
    ColorSpace (string) -- Specifies the colorspace of an input. This setting works in tandem with colorSpaceConversion to determine if any conversion will be performed.
    ColorSpaceUsage (string) -- Applies only if colorSpace is a value other than follow. This field controls how the value in the colorSpace field will be used. fallback means that when the input does include color space data, that data will be used, but when the input has no color space data, the value in colorSpace will be used. Choose fallback if your input is sometimes missing color space data, but when it does have color space data, that data is correct. force means to always use the value in colorSpace. Choose force if your input usually has no color space data or might have unreliable color space data.
    SelectorSettings (dict) -- The video selector settings.
    VideoSelectorPid (dict) -- Placeholder documentation for VideoSelectorPid
    Pid (integer) -- Selects a specific PID from within a video source.
    
    
    VideoSelectorProgramId (dict) -- Placeholder documentation for VideoSelectorProgramId
    ProgramId (integer) -- Selects a specific program from within a multi-program transport stream. If the program doesn't exist, the first program within the transport stream will be selected by default.
    
    
    
    
    
    
    
    
    
    
    
    
    InputSpecification (dict) -- Placeholder documentation for InputSpecification
    Codec (string) -- Input codec
    MaximumBitrate (string) -- Maximum input bitrate, categorized coarsely
    Resolution (string) -- Input resolution, categorized coarsely
    
    
    LogLevel (string) -- The log level being written to CloudWatch Logs.
    Name (string) -- The name of the channel. (user-mutable)
    PipelinesRunningCount (integer) -- The number of currently healthy pipelines.
    RoleArn (string) -- The Amazon Resource Name (ARN) of the role assumed when running the Channel.
    State (string) -- Placeholder documentation for ChannelState
    
    
    
    
    
    """
    pass

def update_input(Destinations=None, InputId=None, InputSecurityGroups=None, MediaConnectFlows=None, Name=None, RoleArn=None, Sources=None):
    """
    Updates an input.
    See also: AWS API Documentation
    
    
    :example: response = client.update_input(
        Destinations=[
            {
                'StreamName': 'string'
            },
        ],
        InputId='string',
        InputSecurityGroups=[
            'string',
        ],
        MediaConnectFlows=[
            {
                'FlowArn': 'string'
            },
        ],
        Name='string',
        RoleArn='string',
        Sources=[
            {
                'PasswordParam': 'string',
                'Url': 'string',
                'Username': 'string'
            },
        ]
    )
    
    
    :type Destinations: list
    :param Destinations: Destination settings for PUSH type inputs.
            (dict) -- Endpoint settings for a PUSH type input.
            StreamName (string) -- A unique name for the location the RTMP stream is being pushed to.
            

    :type InputId: string
    :param InputId: [REQUIRED] Unique ID of the input.

    :type InputSecurityGroups: list
    :param InputSecurityGroups: A list of security groups referenced by IDs to attach to the input.
            (string) -- Placeholder documentation for __string
            

    :type MediaConnectFlows: list
    :param MediaConnectFlows: A list of the MediaConnect Flow ARNs that you want to use as the source of the input. You can specify as few as one Flow and presently, as many as two. The only requirement is when you have more than one is that each Flow is in a separate Availability Zone as this ensures your EML input is redundant to AZ issues.
            (dict) -- The settings for a MediaConnect Flow.
            FlowArn (string) -- The ARN of the MediaConnect Flow that you want to use as a source.
            

    :type Name: string
    :param Name: Name of the input.

    :type RoleArn: string
    :param RoleArn: The Amazon Resource Name (ARN) of the role this input assumes during and after creation.

    :type Sources: list
    :param Sources: The source URLs for a PULL-type input. Every PULL type input needs exactly two source URLs for redundancy. Only specify sources for PULL type Inputs. Leave Destinations empty.
            (dict) -- Settings for for a PULL type input.
            PasswordParam (string) -- The key used to extract the password from EC2 Parameter store.
            Url (string) -- This represents the customer's source URL where stream is pulled from.
            Username (string) -- The username for the input source.
            

    :rtype: dict
    :return: {
        'Input': {
            'Arn': 'string',
            'AttachedChannels': [
                'string',
            ],
            'Destinations': [
                {
                    'Ip': 'string',
                    'Port': 'string',
                    'Url': 'string'
                },
            ],
            'Id': 'string',
            'MediaConnectFlows': [
                {
                    'FlowArn': 'string'
                },
            ],
            'Name': 'string',
            'RoleArn': 'string',
            'SecurityGroups': [
                'string',
            ],
            'Sources': [
                {
                    'PasswordParam': 'string',
                    'Url': 'string',
                    'Username': 'string'
                },
            ],
            'State': 'CREATING'|'DETACHED'|'ATTACHED'|'DELETING'|'DELETED',
            'Type': 'UDP_PUSH'|'RTP_PUSH'|'RTMP_PUSH'|'RTMP_PULL'|'URL_PULL'|'MP4_FILE'|'MEDIACONNECT'
        }
    }
    
    
    :returns: 
    (dict) -- The input update is successfully initiated.
    Input (dict) -- Placeholder documentation for Input
    Arn (string) -- The Unique ARN of the input (generated, immutable).
    AttachedChannels (list) -- A list of channel IDs that that input is attached to (currently an input can only be attached to one channel).
    (string) -- Placeholder documentation for __string
    
    
    Destinations (list) -- A list of the destinations of the input (PUSH-type).
    (dict) -- The settings for a PUSH type input.
    Ip (string) -- The system-generated static IP address of endpoint. It remains fixed for the lifetime of the input.
    Port (string) -- The port number for the input.
    Url (string) -- This represents the endpoint that the customer stream will be pushed to.
    
    
    
    
    Id (string) -- The generated ID of the input (unique for user account, immutable).
    MediaConnectFlows (list) -- A list of MediaConnect Flows for this input.
    (dict) -- The settings for a MediaConnect Flow.
    FlowArn (string) -- The unique ARN of the MediaConnect Flow being used as a source.
    
    
    
    
    Name (string) -- The user-assigned name (This is a mutable value).
    RoleArn (string) -- The Amazon Resource Name (ARN) of the role this input assumes during and after creation.
    SecurityGroups (list) -- A list of IDs for all the security groups attached to the input.
    (string) -- Placeholder documentation for __string
    
    
    Sources (list) -- A list of the sources of the input (PULL-type).
    (dict) -- The settings for a PULL type input.
    PasswordParam (string) -- The key used to extract the password from EC2 Parameter store.
    Url (string) -- This represents the customer's source URL where stream is pulled from.
    Username (string) -- The username for the input source.
    
    
    
    
    State (string) -- Placeholder documentation for InputState
    Type (string) -- Placeholder documentation for InputType
    
    
    
    
    
    """
    pass

def update_input_security_group(InputSecurityGroupId=None, WhitelistRules=None):
    """
    Update an Input Security Group's Whilelists.
    See also: AWS API Documentation
    
    
    :example: response = client.update_input_security_group(
        InputSecurityGroupId='string',
        WhitelistRules=[
            {
                'Cidr': 'string'
            },
        ]
    )
    
    
    :type InputSecurityGroupId: string
    :param InputSecurityGroupId: [REQUIRED] The id of the Input Security Group to update.

    :type WhitelistRules: list
    :param WhitelistRules: List of IPv4 CIDR addresses to whitelist
            (dict) -- An IPv4 CIDR to whitelist.
            Cidr (string) -- The IPv4 CIDR to whitelist.
            

    :rtype: dict
    :return: {
        'SecurityGroup': {
            'Arn': 'string',
            'Id': 'string',
            'Inputs': [
                'string',
            ],
            'State': 'IDLE'|'IN_USE'|'UPDATING'|'DELETED',
            'WhitelistRules': [
                {
                    'Cidr': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    (dict) -- Successfully initiated the update of the Input Security Group.
    SecurityGroup (dict) -- An Input Security Group
    Arn (string) -- Unique ARN of Input Security Group
    Id (string) -- The Id of the Input Security Group
    Inputs (list) -- The list of inputs currently using this Input Security Group.
    (string) -- Placeholder documentation for __string
    
    
    State (string) -- The current state of the Input Security Group.
    WhitelistRules (list) -- Whitelist rules and their sync status
    (dict) -- Whitelist rule
    Cidr (string) -- The IPv4 CIDR that's whitelisted.
    
    
    
    
    
    
    
    
    
    """
    pass

